# Change History for healthdata.json (Part 19)

### Changes from 761a84b to acf49f0 (Part 8/12)
**Author:** Automated

**Date:** 2025-01-31 15:36:25+00:00

**Message:** Updated data: Fri Jan 31 15:36:25 UTC 2025

```diff
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
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
+            "identifier": "https://data.cdc.gov/api/views/azpx-5hzx",
+            "description": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/hwwg-9k4v",
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
+            "identifier": "1db0f12c-e4d6-5a70-8c1b-5af9635999be",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2010",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData2010.csv",
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
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-07",
+            "temporal": "1999-2018",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-17",
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/visualization/"
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
+            "identifier": "https://data.cdc.gov/api/views/iqm3-hbev",
+            "description": "List of footnotes, notes, and source information for NHANES Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHANES Datasets.",
+            "title": "DQS NHANES Footnotes",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/ntaa-dtex",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-17",
+            "references": [
+                "https://chronicdata.cdc.gov/d/x7ys-5vpn"
+            ],
+            "keyword": [
+                "american lung association",
+                "cessation coverage",
+                "comprehensive medicaid coverage",
+                "medicaid coverage of cessation treatment",
+                "office on smoking and health",
+                "osh"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ntaa-dtex",
+            "description": "2008-2024. American Lung Association. Cessation Coverage.  Medicaid data compiled by the Centers for Disease Control and Prevention\u2019s Office on Smoking and Health were obtained from the State Tobacco Cessation Coverage Database, developed and administered by the American Lung Association.  Data from 2008-2012 are reported on an annual basis; beginning in 2013 data are reported on a quarterly basis.  Data include state-level information on Medicaid coverage of approved medications by the Food and Drug Administration (FDA) for tobacco cessation treatment; types of counseling recommended by the Public Health Service (PHS) and barriers to accessing cessation treatment. Note: Section 2502 of the Patient Protection and Affordable Care Act requires all state Medicaid programs to cover all FDA-approved tobacco cessation medications as of January 1, 2014. However, states are currently in the process of modifying their coverage to come into compliance with this requirement. Data in the STATE System on Medicaid coverage of tobacco cessation medications reflect evidence of coverage that is found in documentable sources, and may not yet reflect medications covered under this requirement.",
+            "title": "Medicaid Coverage Of Cessation Treatments And Barriers To Treatments",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ntaa-dtex/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ntaa-dtex/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ntaa-dtex/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ntaa-dtex/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Cessation-Coverage-/Medicaid-Coverage-Of-Cessation-Treatments-And-Barr/ntaa-dtex",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Cessation Coverage"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/n7uz-829a",
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
+            "identifier": "https://data.cdc.gov/api/views/n7uz-829a",
+            "description": "SARS-CoV-2 is a highly infectious respiratory virus that is primarily transmitted by respiratory aerosols and droplets emitted during activities such as talking, breathing, and coughing.  Because symptomatic and asymptomatic individuals with COVID-19 can exhibit a high viral load of SARS-CoV-2 in their respiratory fluids, the CDC recommends that people wear a face mask that covers the nose and mouth to reduce community transmission during the COVID-19 pandemic. Wearing a face mask to protect others from potentially infectious droplets, called source control, has been shown to be a highly effective infection control strategy to limit the spread of COVID-19.  The presence of mask face seal leaks enables respiratory aerosols to escape out rather than pass through the filtering materials of the mask, consequently reducing the benefits of wearing a face mask for source control.  As such, the current investigation examines various modifications that improve the fit of a medical or cloth face mask and reduce the amounts of expelled aerosols during simulated coughs and exhalations.",
+            "title": "Face mask fit modifications that improve source control performance dataset",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/n7uz-829a/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/hyc2-qtk4",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-03-21",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-11",
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
+            "identifier": "91d4309d-3ca8-5a1e-8f78-79984027392d",
+            "description": "Drugs that have been reported under the Medicaid Drug Rebate Program along with an indication of whether or not the required Average Manufacturer Price (AMP) was reported for each drug. All drugs are identified in the file by the 11-digit National Drug Code, product name, labeler name, and reported (R) or not reported (NR).",
+            "title": "Drug AMP Reporting - Monthly",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/drugampreportingmonthly-july2024.csv",
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
+            "issued": "2024-07-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-26",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "disability",
+                "gis",
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
+            "identifier": "https://data.cdc.gov/api/views/c7b2-4ecy",
+            "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 36 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2023 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/sutils/static/prosplign/prosplign.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "dataset",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/dz4r-nx2x",
+            "description": "A utility for computing alignment of proteins to genomic nucleotide sequence based on a variation of the Needleman Wunsch global alignment algorithm and specifically accounts for introns and splice signals.",
+            "title": "ProSplign",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/sutils/static/prosplign/prosplign.html",
+                    "mediaType": "text/html",
+                    "title": "ProSplign - Download"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/hzsh-xp8k",
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
+            "identifier": "75ff3421-7f51-5d22-af3c-83c71affd5eb",
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
+            "landingPage": "https://data.cdc.gov/d/ydsy-yh5w",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2016-01-07",
+            "keyword": [
+                "2015",
+                "invasive pneumococcal disease",
+                "legionellosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "pneumococcal",
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
+            "identifier": "https://data.cdc.gov/api/views/ydsy-yh5w",
+            "description": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years. Since 2010, case notifications for this condition were consolidated under one event code for Invasive pneumococcal disease.",
+            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/aging/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-04-29",
+            "@type": "dcat:Dataset",
+            "modified": "2024-04-29",
+            "references": [
+                "https://www.cdc.gov/aging/index.html"
+            ],
+            "keyword": [
+                "aging",
+                "alcohol",
+                "caregiver",
+                "cognitive health",
+                "falls",
+                "fruits and vegetables",
+                "obesity",
+                "overall health",
+                "screenings",
+                "smoking",
+                "vaccines"
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
+            "identifier": "https://data.cdc.gov/api/views/hfr9-rurv",
+            "description": "2015-2022. This data set contains data from BRFSS.",
+            "title": "Alzheimer's Disease and Healthy Aging Data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Healthy-Aging/Alzheimer-s-Disease-and-Healthy-Aging-Data/hfr9-rurv",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Healthy Aging"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-04-28",
+            "temporal": "2020-01-01/2020-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-04-03",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "quarterly",
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
+            "identifier": "https://data.cdc.gov/api/views/ypxr-mz8e",
+            "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by United States county of residence and age group, for 2020 by quarter.",
+            "title": "AH Provisional COVID-19 Deaths by Quarter, County and Age for 2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/respvaxview/about/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2024-2025",
+            "modified": "2025-01-29",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis-acm",
+                "rsv vaccination",
+                "vaccination",
+                "vaccination coverage",
+                "vaccine confidence"
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
+            "identifier": "https://data.cdc.gov/api/views/si7g-c2bs",
+            "description": "\u2022 National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on the updated 2024-25 COVID-19 vaccine, the 2024-25 seasonal flu vaccine, and the RSV vaccine uptake and confidence. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics. \n\n\u2022 The data start in September 2024.\n\n\u2022 The archived data can be found here: \n- 2023-24 season: https://data.cdc.gov/Vaccinations/National-Immunization-Survey-Adult-COVID-Module-NI/uc4z-hbsd/about_data\n- Before October 2023:  \nhttps://data.cdc.gov/Vaccinations/National-Immunization-Survey-Adult-COVID-Module-NI/udsf-9v7b/about_data",
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): RespVaxView| Data | Centers for Disease Control and Prevention (cdc.gov)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/si7g-c2bs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/si7g-c2bs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/si7g-c2bs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/si7g-c2bs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National, Region, State",
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
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service",
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
+                "original medicare"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data-viewer",
+            "description": "The Medicare Inpatient Hospitals by Provider and Service dataset provides information on inpatient discharges for Original Medicare Part A beneficiaries by IPPS\u00a0hospitals. It includes information on the use, payment, and hospital charges for more than 3,000 U.S. hospitals that received IPPS payments.\u00a0The data are organized by hospital and Medicare Severity Diagnosis Related Group (DRG).\n\n\u00a0\n\nHospitals determine what they will charge for items and services provided to patients, and these charges are the amount the hospital bills for an item or service. The Total Payment Amount includes the DRG amount, claim per diem amount, beneficiary primary payer claim payment amount, beneficiary Part A (Hospital Insurance)\u00a0coinsurance amount, beneficiary deductible amount, beneficiary blood deductible amount and diagnosis related group outlier amount.",
+            "title": "Medicare Inpatient Hospitals - by Provider and Service",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/7d1f4bcd-7dd9-4fd1-aa7f-91cd69e452d3/MUP_INP_RY24_P03_V10_DY22_PrvSvc.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/46bf50f8-0983-4ca2-b8d5-f2afbbf2e589/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/a754bf0b-0c51-4daf-876e-272f90a11c05/MUP_IHP_RY23_P03_V10_DY21_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/117d93f2-ce81-40fe-a4d4-8c03203b95e1/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/e57818f2-318c-4979-a612-c91eba44b011/MUP_IHP_RY23_P03_V10_DY20_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ef5bdbe1-27b4-4296-b320-52bd5d2183d7/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/6602e715-b301-4a38-954d-b8d5aec12b87/MUP_IHP_RY23_P03_V10_DY19_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6f6d93e1-ecf8-4b93-9845-091faf20f274/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/78d80cf4-fc5b-40db-8e88-ca44bc86102f/MUP_IHP_RY23_P03_V10_DY18_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09c12f06-e3fe-4cb0-81e9-945f2078c1df/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/ec9287b0-68e6-4818-8c64-3a0c68fcde49/MUP_IHP_RY23_P03_V10_DY17_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b61ba5eb-021b-4510-947e-0f198982b0e8/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/4f20bce0-607a-46c1-bd0d-78021b0624ec/MUP_IHP_RY23_P03_V10_DY16_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ca9e33a4-e46c-4de9-8377-3bbcd25d24dd/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/81895338-4c5c-4ad7-a490-8e5a9a972825/MUP_IHP_RY23_P03_V10_DY15_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e70315f5-4b02-46a8-81f4-16035b8665ab/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/dd6961c6-0eed-4a33-8527-8f66638819b8/MUP_IHP_RY23_P03_V10_DY14_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/635d7ccd-3dd7-4f1d-a82f-4bba7fe97509/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/3748379f-baf7-494d-abb7-653fc85176a3/MUP_IHP_RY23_P03_V10_DY13_PRVSVC.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2013-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cf60c282-a006-444c-9705-268f68b8e96d/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider and Service : 2013-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-provider-and-service-data-dictionary-0",
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
+            "landingPage": "https://data.cdc.gov/d/bucw-etpd",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-02",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Physical Effects Research Branch, Health Effects Laboratory Division",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/bucw-etpd",
+            "description": "Over-exposure of the hand-arm system to intense vibration and force over time may cause degeneration of the vascular, neurological, and musculoskeletal systems in the fingers. A novel animal model using rat tails has been developed to understand the health effects on human fingers exposed to vibration and force when operating powered hand tools or workpieces. The biodynamic responses, such as vibration stress, strain, and power absorption density, of the rat tails can be used to help evaluate the health effects related to vibration and force and to establish a dose-effect relationship. While the biodynamic responses of cadaver rat tails have been investigated, the objective of the current study was to determine whether the biodynamic responses of living rat tails are different from those of cadaver rat tails, and whether the biodynamic responses of both living and cadaver tails change with exposure duration. To make direct comparisons, the responses of both cadaver and living rat tails were examined on four different testing stations. The transfer function of each tail under a given contact force (2 N) was measured at each frequency in the one-third octave bands from 20 to 1000 Hz, and used to calculate the mechanical system parameters of the tails. The transfer function was also measured at different exposure durations to determine the time dependency of the response. The biodynamic responses of both cadaver and living rat tails, and the modeling results and time dependency are presented in a manuscript of this study (Warren et al., 2024), the original datasets measured in each trial of the tests are documented in this data description.",
+            "title": "Rat-Tail Models for Studying Hand-Arm Vibration Syndrome:  A Comparison between Living and Cadaver Rat Tails",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/bucw-etpd/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/nchs/dhcs/ed-visits/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-06-01",
+            "temporal": "2016/2022",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-25",
+            "keyword": [
+                "emergency department",
+                "national hospital ambulatory medical care survey",
+                "primary diagnosis",
+                "reason for visit"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:ambcare@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ycxr-emue",
+            "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS), conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to emergency departments to describe patterns of utilization and provision of ambulatory care delivery in the United States. Data are collected from nonfederal, general, and short-stay hospitals from all 50 U.S. states and the District of Columbia, and are used to develop nationally representative estimates. \n\nThe data include counts and rates of emergency department visits from 2016-2022 for the 10 leading primary diagnoses and reasons for visit, stratified by selected patient and hospital characteristics. Rankings for the 10 leading categories were identified using weighted data from 2022 and were then assessed in prior years.",
+            "title": "Estimates of Emergency Department Visits in the United States from 2016-2022",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
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
+            "landingPage": "https://seer.cancer.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "alaska",
+                "aleukemic",
+                "all sites",
+                "anus",
+                "appendix",
+                "arizona",
+                "ascending colon",
+                "bones and joints",
+                "brain",
+                "breast",
+                "california",
+                "cancer",
+                "cecum",
+                "cervix uteri",
+                "colon and rectum",
+                "community health",
+                "connecticut",
+                "corpus and uterus",
+                "corpus uteri",
+                "county",
+                "descending colon",
+                "digestive system",
+                "disease",
+                "endocrine system",
+                "epidemiology",
+                "esophagus",
+                "eye and orbit",
+                "floor of mouth",
+                "gallbladder",
+                "gum and other mouth",
+                "hawaii",
+                "health",
+                "hepatic flexure",
+                "hodgkin lymphoma",
+                "hodgkin - nodal",
+                "hypopharynx",
+                "incidence",
+                "iowa",
+                "kaposi sarcoma",
+                "large intestine",
+                "larynx",
+                "leukemia",
+                "lip",
+                "liver",
+                "lung and bronchus",
+                "lymphoma",
+                "male genital system",
+                "mesothelioma",
+                "miscellaneous",
+                "myeloma",
+                "nasopharynx",
+                "new mexico",
+                "nhl - extranodal",
+                "nhl - nodal",
+                "nos",
+                "nose",
+                "oropharynx",
+                "other biliary",
+                "other leukemia",
+                "ovary",
+                "pancreas",
+                "penis",
+                "peritoneum",
+                "pleura",
+                "prostate",
+                "rectum",
+                "registry",
+                "respiratory system",
+                "retroperitoneum",
+                "rural georgia",
+                "salivary gland",
+                "seer",
+                "seer 13",
+                "seer 9",
+                "sigmoid colon",
+                "small intestine",
+                "splenic flexure",
+                "stomach",
+                "subleukemic and nos",
+                "testis",
+                "thyroid",
+                "tongue",
+                "tonsil",
+                "trachea",
+                "transverse colon",
+                "ureter",
+                "urinary bladder",
+                "urinary system",
+                "us",
+                "utah",
+                "uterus",
+                "vagina",
+                "vulva"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Cancer Institute (NCI)",
+                "hasEmail": "mailto:NCIinfo@nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Cancer Institute (NCI), National Institutes of Health (NIH)"
+            },
+            "identifier": "68efde71-93b1-440d-b7d1-1847114d16ad",
+            "description": "<p>SEER Limited-Use cancer incidence data with associated population data. Geographic areas available are county and SEER registry.  The Surveillance, Epidemiology, and End Results (SEER) Program of the National Cancer Institute collects and distributes high quality, comprehensive cancer data from a number of population-based cancer registries. Data include patient demographics, primary tumor site, morphology, stage at diagnosis, first course of treatment, and follow-up for vital status. The SEER Program is the only comprehensive source of population-based information in the United States that includes stage of cancer at the time of diagnosis and survival rates within each stage.</p>",
+            "title": "Cancer Incidence - Surveillance, Epidemiology, and End Results (SEER) Registries Limited-Use",
+            "programCode": [
+                "009:047"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://seer.cancer.gov/canques/incidence.html",
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
+            "accessLevel": "restricted public",
+            "landingPage": "https://data.cdc.gov/d/b2qj-y9ew",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2023-06-06",
+            "@type": "dcat:Dataset",
+            "temporal": "2022",
+            "modified": "2023-06-06",
+            "keyword": [
+                "chronic health conditions",
+                "disability",
+                "firearms safety",
+                "gender identity",
+                "long covid",
+                "research-data-center",
+                "sdoh-access-to-health-care",
+                "sdoh-civic-participation",
+                "sdoh-employment",
+                "sdoh-higher-education",
+                "sdoh-high-school",
+                "sdoh-poverty-income",
+                "sdoh-source-of-health-care",
+                "sdoh-use-of-health-care",
+                "social participation",
+                "traumatic brain injury",
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
+            "identifier": "https://data.cdc.gov/api/views/b2qj-y9ew",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, and questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, along with questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+                    "@type": "dcat:Distribution",
+                    "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File"
+                }
+            ],
+            "spatial": "50 states and District of Columbia",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS7-technical-documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/state-snapshots",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "health care quality",
+                "nhqr",
+                "quality measurement",
+                "state health care"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "identifier": "234049e8-dd71-4b9d-8dc2-ab56471b9011",
+            "description": "<p>The State Snapshots provide graphical representations of State-specific health care quality information, including strengths, weaknesses, and opportunities for improvement. The goal is to help State officials and their public- and private-sector partners better understand health care quality and disparities in their State. State-level information used to create the State Snapshots is based on data collected for the National Healthcare Quality Report (NHQR). The State Snapshots include summary measures of quality of care and States' performances relative to all States, the region, and best performing States by overall health care quality, types of care (preventive, acute, and chronic), settings of care (hospitals, ambulatory care, nursing home, and home health), and clinical conditions (cancer, diabetes, heart disease, maternal and child health, and respiratory diseases). Special focus areas on diabetes, asthma, Healthy People 2010, clinical preventive services, disparities, payer, and variation over time are also featured. The Agency for Healthcare Research and Quality (AHRQ) has released the State Snapshots each year in conjunction with the 2004 NHQR through the 2009 NHQR.</p>",
+            "title": "State Snapshots",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ahrq.gov/data/state-snapshots.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health",
+                "Quality",
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/yqwx-bvu7",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
+                "invasive pneumococcal disease",
+                "legionellosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "pneumococcal",
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
+            "identifier": "https://data.cdc.gov/api/views/yqwx-bvu7",
+            "description": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years.",
+            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2023-07-19",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "keyword": [
+                "middle school",
+                "risk behavior",
+                "survey",
+                "youth online",
+                "yrbs"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DASH Public Inquiries",
+                "hasEmail": "mailto:nccddashinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/k5bc-k3g8",
+            "description": "1991-2017. Middle School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
+            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): Middle School",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/k5bc-k3g8",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Youth Risk Behaviors"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/uhs4-vv7g",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-09",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Allergy and Clinical Immunology Branch, Health Effects Laboratory Division",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/uhs4-vv7g",
+            "description": "Nickel is one of the most common contact allergens worldwide. Despite this prevalence, many of the underlying immunological mechanisms responsible for nickel allergy remain unclear. This knowledge gap is partially attributable to the inherent resistance of laboratory rodents (mice and rats) to dermal sensitization with nickel salts. The fundamental goal of this study was to assess the potential utility of the novel humanized Toll-like receptor-4 (hTLR-4) mouse model for use in future in vivo studies of nickel allergy. Accordingly, hTLR-4 positive and negative mice of both sexes were first incorporated into a Local Lymph Node Assay (LLNA) to evaluate dermal sensitization following topical exposure to soluble nickel salts (NiSO4). The ensuing immune responses were then characterized further by incorporating female and male hTLR-4 positive mice into a non-radioactive endpoint-based assay. Utilizing the same exposure scheme as in the LLNA, mice were euthanized following exposure and the auricular lymph nodes, spleen, and blood were collected to assess various immunological parameters associated with allergy and ACD.",
+            "title": "Assessment of dermal sensitization by nickel salts in a novel humanized TLR-4 mouse model",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/uhs4-vv7g/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/hatw-7gqy",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
+                "all serogroups",
+                "meningococcal disease (neisseria meningitidis)",
+                "mmwr",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "pertussis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hatw-7gqy",
+            "description": "NNDSS - Table II. Meningococcal to Pertussis - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Data for meningococcal disease, invasive caused by serogroups ACWY, serogroup B, other serogroups, and unknown serogroups are available in Table I.",
+            "title": "NNDSS - Table II. Meningococcal to Pertussis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/7xhe-mv2e",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
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
+            "identifier": "https://data.cdc.gov/api/views/7xhe-mv2e",
+            "description": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNotice:  Measles data for weeks 1-4 (in Table 1v) were updated on 02-28-2020 to correct the classification of imported and indigenous. For all weeks, measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.",
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/VAST/vast.shtml",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-07-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/w6ya-ncpm",
+            "description": "A computer algorithm that identifies similar protein 3-dimensional structures. Structure neighbors for every structure in MMDB are pre-computed and accessible via links on the MMDB Structure Summary pages.",
+            "title": "Vector Alignment Search Tool (VAST)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Structure/VAST/vast.shtml",
+                    "mediaType": "text/html",
+                    "title": "Vector Alignment Search Tool (VAST)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2013-11-01",
+            "references": [
+                "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135509.htm"
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
+            "identifier": "7e7f6062-5270-4e09-81c9-ff22261232ac",
+            "description": "This database contains product names and associated information developed by the Center for all products, both medical and non-medical, which emit radiation. It includes a three letter product code, a descriptor for radiation type, applicable performance standard(s), and a definition for the code.",
+            "title": "Radiation-emitting Electronic Product Codes",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "describedBy": "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135508.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/seuz-s2cv",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-24",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "ncird",
+                "ncird-corvd",
+                "ncird-id",
+                "respiratory-virus-response",
+                "rsv"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NREVSS",
+                "hasEmail": "mailto:Nrevss@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/seuz-s2cv",
+            "description": "Percent of tests positive for a pathogen is one of the surveillance metrics used to monitor respiratory pathogen transmission over time. The percent of tests positive is calculated by dividing the number of positive tests by the total number of tests administered, then multiplying by 100 [(# of positive tests/total tests) x 100]. These data include percent of tests positive values for the detection of severe acute respiratory virus coronavirus type 2 (SARS-CoV-2), the virus that causes COVID-19 and Respiratory syncytial virus (RSV) reported to the National Respiratory and Enteric Virus Surveillance System (NREVSS), a sentinel network of laboratories located through the US, includes clinical, public health and commercial laboratories; additional information available at: https://www.cdc.gov/surveillance/nrevss/index.html. Influenza results include clinical laboratory test results from NREVSS and U.S. World Health Organization collaborating laboratories; more details about influenza virologic surveillance are available here:\u202fhttps://www.cdc.gov/flu/weekly/overview.html. \n\nData represent calculations based on laboratory tests performed, not individual people tested. RSV and COVID-19 are limited to nucleic acid amplification tests (NAATs), also listed as polymerase chain reaction tests (PCR). Participating laboratories report weekly to CDC the total number of RSV tests performed that week and the number of those tests that were positive. The RSV trend graphs display the national average of the weekly % test positivity for the current, previous, and following weeks in accordance with the recommendations for assessing RSV trends by percent (https://academic.oup.com/jid/article/216/3/345/3860464). \n\nAll data are provisional and subject to change.",
+            "title": "Percent of Tests Positive for Viral Respiratory Pathogens",
+            "programCode": [
+                "009:037"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/seuz-s2cv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/seuz-s2cv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/seuz-s2cv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/seuz-s2cv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/uniform-facility-data-set-us-ufds-1998",
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
+            "identifier": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632",
+            "description": "<p>The Uniform Facility Data Set (UFDS) was designed to measure the scope and use of drug abuse treatment services in the United States. The survey collects information from each privately- and publicly-funded facility in the country that provides substance abuse treatment as well as from state-identified facilities that provide other substance abuse services. Data are collected on a number of topics including facility operation, services provided (assessment, therapy, testing, health, continuing care, special programs, transitional services, community outreach, ancillary), type of treatment, numbers of clients, and various client characteristics. The main objective of the UFDS is to produce data that can be used to assess the nature and extent of substance abuse treatment services, to assist in the forecast of treatment resource requirements, to analyze treatment service trends, to conduct national, regional, and state-level comparative analyses of treatment services and utilization, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its on-line equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov/.This\">http://findtreatment.samhsa.gov/.This</a> study has 1 Data Set.</p>",
+            "title": "Uniform Facility Data Set  US (UFDS-1998)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632",
+                    "description": "Uniform Facility Data Set  US (UFDS-1998) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/b58h-s9zx",
+            "bureauCode": [
+                "009:15"
+            ],
+            "issued": "2020-07-20",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-25",
+            "keyword": [
+                "covid-19",
+                "provider relief fund"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Chief Data Officer",
+                "hasEmail": "mailto:PRFdata@hrsa.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/b58h-s9zx",
+            "description": "The bipartisan CARES Act; the Paycheck Protection Program and Health Care Enhancement Act (PPPHCEA); and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act provided $178 billion in relief funds to hospitals and other healthcare providers on the front lines of the coronavirus response. The Department of Health and Human Services through the Health Resources and Services Administration is distributing two rounds of payments to hospitals in High Impact areas for positive COVID-19 admissions. In the first round of the High Impact Allocation, $12 billion was distributed to nearly 400 hospitals who provided inpatient care for 100 or more COVID-19 patients through April 10, 2020. $2 billion of these payments was distributed to these hospitals based on their Medicare disproportionate share and uncompensated care payments. In the second round of funding, $10 billion will be distributed to hospitals having over 161 COVID-19 admissions between January 1 and June 10, 2020.",
+            "title": "Provider Relief Fund COVID-19 High-Impact Payments",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Never",
+            "theme": [
+                "Administrative"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2004-01-01",
+            "keyword": [
+                "community health",
+                "foods",
+                "health",
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
+            "identifier": "e9412021-e775-4c64-9c04-98d6f666786f",
+            "description": "This feed describes all new items that are being recalled by the FDA.",
+            "title": "Food and Drug Administration--Recalls",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
+                    "mediaType": "application/rss+xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/skilled-nursing-facility-cost-report",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2011-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-25",
+            "references": [
+                "https://data.cms.gov/resources/skilled-nursing-facility-cost-report-methodology"
+            ],
+            "keyword": [
+                "financials",
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "skilled nursing",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a69d3df7-3f66-4a0d-b5b8-0d66049bd565/data-viewer",
+            "description": "The Skilled Nursing Facility (SNF) Cost Report dataset is a public use file that provides select measures from the skilled nursing facility\u00a0annual cost report. This data includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
+            "title": "Skilled Nursing Facility Cost Report",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a69d3df7-3f66-4a0d-b5b8-0d66049bd565/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Skilled Nursing Facility Cost Report : 2022-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/94119bf8-a863-421d-acfa-ec4cc0b9e96b/CostReportsnf_Final_22.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2022-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8d2fb665-b944-48cc-b0d7-97a6e5a90bf3/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2022-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/c355a614-47d5-474f-80e4-8f602bb96ff3/CostReportsnf_Final_21.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/633d1011-94cc-47d0-ae14-0fee1932f32c/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/6c9efef2-c0e6-47b1-8cf6-45997237815c/CostReportsnf_Final_20.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e0544322-7c25-44f4-b6c4-7f5f8a79819c/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/63b6f7bc-7c6e-4c9e-98c8-6dc032c1f861/CostReportsnf_Final_19.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2019-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/dda9576c-adbc-4a89-aa0c-0e8df7f0f74f/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2019-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/18161fdc-c49e-424e-9279-a39aa087fe58/CostReportsnf_Final_18.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2018-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/10333ed8-ca79-455c-9d2e-60cfed4a4c0e/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2018-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/e6a1e457-ffd3-4352-bc12-25cc261d98c6/CostReportsnf_Final_17.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2017-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/922f6a06-974c-45e5-8828-b5a61979f4af/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2017-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/737fd9bf-719c-4b13-a33f-2d238cd24e94/CostReportsnf_Final_16.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2016-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6a674cd7-d96e-4d5a-9d0a-c587decf2fef/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2016-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/d87bd689-6707-4902-8f10-9dd91b008eb9/CostReportsnf_Final_15.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2015-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9fce1ff4-ab0a-4cd1-885b-9dd4f121972f/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2015-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/d8dc1069-91b0-46c7-9648-7a7352a13725/CostReportsnf_Final_14.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2014-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ad033e02-cbc5-45d1-89d3-ba41018d5680/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2014-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/ba4bb18e-1c55-4bf1-a56c-7d1e91c903f4/CostReportsnf_Final_13.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2013-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3e296343-8cd3-42cf-888b-04f36a53e631/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2013-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/8a49b517-d567-4596-ac30-1b20d49e2fe0/CostReportsnf_Final_12.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2012-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ad680796-1935-4900-a239-e8811e033b82/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2012-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/9149cd79-b972-496a-ae69-e0c47fbda921/CostReportsnf_Final_11.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Cost Report : 2011-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f6fce67e-d888-4a56-b01b-28f49b17454e/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Cost Report : 2011-12-02"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-12/Skilled%20Nursing%20Facility%20Cost%20Report%20Data%20Dictionary_508.pdf",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-10-18",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-12-15/2022-05-06",
+            "modified": "2023-01-12",
+            "keyword": [
+                "covid-19",
+                "physicians"
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
+            "identifier": "https://data.cdc.gov/api/views/kk8c-wtm4",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS), conducted by the National Center for Health Statistics (NCHS), collects data on visits to physician offices to describe patterns of ambulatory care delivery in the United States. As part of NAMCS, the Physician Induction Interview collects information about practice characteristics at physician offices. Partway through the 2020 NAMCS, NCHS added questions to the Physician Induction Interview to assess physician experiences related to COVID-19 in office-based settings.\n\nThe data include nationally representative estimates of experiences related to COVID-19 among office-based physicians in the United States, including: shortages of personal protective equipment (PPE) in the past 3 months; the ability to test for COVID-19 in the past 3 months; providers testing positive for COVID-19 in the past 3 months; turning away COVID-19 patients in the past 3 months; and telemedicine or telehealth technology use before and after March 2020.  Estimates were derived from interviews with physicians in periods 3 and 4 of 2020 NAMCS and periods 1 through 4 of 2021 NAMCS, which occurred between December 15, 2020 and May 6, 2022.  The data are considered preliminary, and the results may change with the final data release.",
+            "title": "Physician Experiences Related to COVID-19 from the National Ambulatory Medical Care Survey",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/tsa/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/fj8w-mvxu",
+            "description": "TSA is an archive of computationally assembled transcript sequences from primary data such as ESTs and Next Generation Sequencing Technologies. The overlapping sequence reads from a complete transcriptome are assembled into transcripts by computational methods instead of by traditional cloning and sequencing of cloned cDNAs. The primary sequence data used in the assemblies must have been experimentally determined by the same submitter. TSA sequence records differ from GenBank records because there are no physical counterparts to the assemblies.",
+            "title": "Transcriptome Shotgun Assembly (TSA) Sequence Database and Submissions",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Traces/wgs/?term=tsa",
+                    "mediaType": "text/html",
+                    "title": "TSA - Query Interface"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/genbank/tsa/",
+                    "mediaType": "text/html",
+                    "title": "Download TSA"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://submit.ncbi.nlm.nih.gov/subs/tsa/",
+                    "description": "Submission details can be found in the TSA submission guide. https://www.ncbi.nlm.nih.gov/genbank/tsaguide",
+                    "@type": "dcat:Distribution",
+                    "title": "TSA Submission Portal"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/7dk4-g6vg",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "N/A",
+            "issued": "2023-07-06",
+            "@type": "dcat:Dataset",
+            "temporal": "8/1/2020 - 5/3/2024",
+            "modified": "2025-01-17",
+            "references": [
+                "CDT aggregate hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-state CDT Hospitalizations Landing Page: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-landing NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "inpatient beds"
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
+            "identifier": "https://data.cdc.gov/api/views/7dk4-g6vg",
+            "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\nThis dataset represents weekly COVID-19 hospitalization data and metrics aggregated to national, state/territory, and regional levels. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS).</li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.</li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files.</li><li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n\n<b>Metric details:</b><ul><li><b>Time Period:</b> timeseries data will update weekly on Mondays as soon as they are reviewed and verified, usually before 8 pm ET. Updates will occur the following day when reporting coincides with a federal holiday. Note: Weekly updates might be delayed due to delays in reporting. All data are provisional. Because these provisional counts are subject to change, including updates to data reported previously, adjustments can occur. Data may be updated since original publication due to delays in reporting (to account for data received after a given Thursday publication) or data quality corrections.</li><li><b>New COVID-19 Hospital Admissions (count):</b> Number of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>New COVID-19 Hospital Admissions (7-Day Average):</b> 7-day average of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>Cumulative COVID-19 Hospital Admissions:</b> Cumulative total number of admissions of patients with labo",
+            "title": "Weekly United States COVID-19 Hospitalization Metrics by Jurisdiction \u2013 ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ia8m-ebiw",
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
+            "identifier": "992936b2-2a72-5df6-a734-a56a8631b87a",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2012",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData2012.csv",
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
+            "landingPage": "https://data.cdc.gov/d/uw7a-a5t8",
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
+                "smallpox",
+                "streptococcal toxic shock syndrome",
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
+            "identifier": "https://data.cdc.gov/api/views/uw7a-a5t8",
+            "description": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uw7a-a5t8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uw7a-a5t8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uw7a-a5t8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uw7a-a5t8/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/tfu6-pjxh",
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
+                "tuberculosis",
+                "tularemia",
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
+            "identifier": "https://data.cdc.gov/api/views/tfu6-pjxh",
+            "description": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tfu6-pjxh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tfu6-pjxh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tfu6-pjxh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tfu6-pjxh/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-change-of-ownership-owner-information",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/60625dc8-b621-45f0-9423-077fd133b13e/data-viewer",
+            "description": "The Hospital Change of Ownership (CHOW) - Owner Information dataset provides information on individual and organizational ownership interest and managerial control associated with the buyer and seller organizations, role of the owner, association date, address of the organizational owner and other ownership details.",
+            "title": "Hospital Change of Ownership - Owner Information",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/60625dc8-b621-45f0-9423-077fd133b13e/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/e42d8d95-39eb-43a4-86ca-de774b00c7ca/Hospital_CHOW_Owners_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9573d9f5-1abd-4511-b426-b5966c56050f/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/b3ddd565-52d7-4d9c-a1c6-ca663a2a0d58/Hospital_CHOW_Owners_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ab0061aa-4513-465d-8e3d-162a993190b3/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/78be0289-f7fd-4866-8534-d4ebd4e4f68b/Hospital_CHOW_Owners_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/101960de-5d1a-4a2e-a878-9caaf39b7a9a/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/c754fd99-0df2-4ee5-94f7-cc3c3625732e/Hospital_CHOW_Owners_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1166689d-490e-41d0-842a-fde005fab35e/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/8be47b23-5303-4061-b829-93eacf59af9e/Hospital_CHOW_Owners_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fc7c14a2-6212-4622-bdd9-91e760a25084/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/c30c8b96-e62d-40fe-af46-990160c8d844/Hospital_CHOW_Owners_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4454b84e-4c23-4adb-8abb-8c05a272fe34/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/cb9cc51f-0c53-403c-ba79-ef47f9885929/Hospital_CHOW_Owners_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/24ff58f4-6d3e-449e-8eff-36a779bd8df2/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/f802e61c-1c57-406f-a7d7-73fa3dda4877/Hospital_CHOW_Owners_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fdf4fa07-c062-4e5f-adf8-61dda5ce6d11/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/4326a72d-6492-4e8d-becf-61bec43675ff/Hospital_CHOW_Owners_2022.12.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3960b721-c29b-4003-8a69-4d04f17e4797/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/975df6a2-f134-4b38-9a33-c10c1f07f371/Hospital_CHOW_Owners_2022.09.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f044600b-2eb3-4c60-870a-b16f6362ac8e/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/29a1dec3-b6a5-4c6e-93c3-4b97c3d9edee/Study_01.032.02_2022.07.01_PPEF_Hospital_CHOW_Owners_Extract.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/26ac5a32-b6c3-489c-85f9-3b3c1673f1c7/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/Hospital_CHOW_Owners_2022Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6f86d453-a29d-450d-ab8a-49b44ceb04ce/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership - Owner Information : 2022-03-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Owners_Data_Dictionary.pdf",
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
+            "landingPage": "https://data.cdc.gov/d/ttj2-zsyk",
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
+            "identifier": "https://data.cdc.gov/api/views/ttj2-zsyk",
+            "description": "NNDSS - Table II.  Vibriosis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Vibriosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttj2-zsyk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttj2-zsyk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttj2-zsyk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttj2-zsyk/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/advance-investment-payment-spend-plan",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-01-30",
+            "temporal": "2024-01-01/2024-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-29",
+            "references": [
+                "https://data.cms.gov/resources/advance-investment-payment-spend-plan-methodology"
+            ],
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "financials",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data-viewer",
+            "description": "The Advance Investment Payment Spend Plan data provides payment use, spending category, projected and actual spending of advanced investments payments by Accountable Care Organizations (ACOs).",
+            "title": "Advance Investment Payment Spend Plan",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Advance Investment Payment Spend Plan : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/AIP_PUF_12_13_2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Advance Investment Payment Spend Plan : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/329394bc-b58c-4458-a028-33a00ae47a84/data",
+                    "mediaType": "text/html",
+                    "title": "Advance Investment Payment Spend Plan : 2024-01-02"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/advance-investment-payment-spend-plan-data-dictionary",
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
+            "landingPage": "https://data.cdc.gov/d/x66v-w5ka",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-05-04",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-04",
+            "keyword": [
+                "centers for disease control and prevention",
+                "environmental health",
+                "foodborne"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "The National Environmental Assessment Reporting System (NEARS)",
+                "hasEmail": "mailto:nears@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/x66v-w5ka",
+            "description": "This study examined relationships between foodborne outbreak investigation characteristics, such as the epidemiological methods used, and the success of the investigation, as determined by whether the investigation identified an outbreak agent (i.e., pathogen), food item, and contributing factor. This study used data from the Centers for Disease Control and Prevention\u2019s (CDC) National Outbreak Reporting System (NORS) and National Environmental Assessment Reporting System (NEARS) to identify outbreak investigation characteristics associated with outbreak investigation success. We identified investigation characteristics that increase the probability of successful outbreak investigations: a robust epidemiology investigation method; a thorough environmental assessment, as measured by number of visits to complete the assessment; and the collection of clinical samples. This research highlights the importance of a comprehensive outbreak investigation, which includes epidemiology, environmental health, and laboratory personnel working together to solve the outbreak.",
+            "title": "Characteristics Associated with Successful Foodborne Outbreak Investigations, NEARS 2014 - 2016",
+            "programCode": [
+                "009:032"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Foodborne",
+                "Waterborne",
+                "and Related Diseases"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://cde.nlm.nih.gov/home",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-08-04",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-24",
+            "keyword": [
+                "dataset",
+                "health data standards",
+                "medical informatics",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/divb-gtqn",
+            "description": "The NIH Common Data Elements (CDE) Repository has been designed to provide access to structured human and machine-readable definitions of data elements that have been recommended or required by NIH Institutes and Centers and other organizations for use in research and for other purposes. Visit the NIH CDE Resource Portal for contextual information about the repository.",
+            "title": "NIH Common Data Elements Repository",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://cde.nlm.nih.gov/cde/search",
+                    "mediaType": "text/html",
+                    "title": "Search Common Data Elements and Download Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://cde.nlm.nih.gov/form/search",
+                    "mediaType": "text/html",
+                    "title": "Search Forms and Download Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Other"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597",
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment.  Data are collected on topics including facility operation, services offered (assessment and pre-treatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.  N-SSATS was titled the Uniform Facility Data Set (UFDS) in 1997 and 1998. Data from these years along with N-SSATS 2000 and  N-SSATS 2002 to N-SSATS 2011 are included in this concatenated dataset.This study has 1 Data Set.</p>",
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-1997-2011)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-1997-2011) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/icfy-anwh",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-11-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
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
+            "identifier": "743f9f04-4473-41e2-9da2-9a89db65ee55",
+            "description": "The MLR Summary Reports provide plan-specific MLRs for Medicaid managed care programs. The MLR summary report data include MLRs for MCOs, PIHPs, and PAHPs submitted by states under 42 CFR \u00a7 438.74.",
+            "title": "MLR Summary Reports",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mlr-public-use-file-07302024final.csv",
+                    "mediaType": "text/csv",
+                    "title": "MLR Summary Reports"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/office-refugee-resettlement-orr-overseas-refugee-arrival-data-fy-2000",
+            "bureauCode": [
+                "001:05"
+            ],
+            "issued": "2013-12-13",
+            "temporal": "2000-01-01T00:00:00-05:00/2000-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "administration-for-children-and-families-department-of-health-human-services",
+                "administrative",
+                "population statistics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jennifer Schmalz",
+                "hasEmail": "mailto:jennifer.schmalz@acf.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "identifier": "cf157d3d-72fa-4d8d-8f7c-4a0d0bc5e7b5",
+            "description": "<p>Office of Refugee Resettlement (ORR) Overseas Refugee Arrival Data FY 2000 sorted by country of origin and state of initial resettlement in the United States.</p>",
+            "title": "OFFICE OF REFUGEE RESETTLEMENT",
+            "programCode": [
+                "009:086"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/Safety/MedWatch/SafetyInformation/SafetyAlertsforHumanMedicalProducts/default.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "definitions"
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
+            "identifier": "2003711a-3d1c-4a0c-9928-09de5c42e2cf",
+            "description": "MedWatch alerts provide timely new safety information on human drugs, medical devices, vaccines and other biologics, dietary supplements, and cosmetics. The alerts contain actionable information that may impact both treatment and diagnostic choices for healthcare professional and patient.",
+            "title": "MedWatch Safety Alerts for Human Medical Products",
+            "programCode": [
+                "009:008"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/downloads/Safety/MedWatch/SafetyInformation/UCM189811.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/office-based-physician-health-it-adoption-and-use",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2021-12-01",
+            "references": [
+                "https://www.healthit.gov/data/quickstats/office-based-physician-electronic-health-record-adoption",
+                "https://www.healthit.gov/data/apps/office-based-physician-health-it-adoption"
+            ],
+            "keyword": [
+                "doctors",
+                "ehr adoption",
+                "health information technology",
+                "health it",
+                "interoperability",
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
+            "identifier": "9jlt3cvr-g3xs-9sva-n1js-xczfj9fxr7fh",
+            "description": "Since 2008, the Centers for Disease Control and Prevention's National Center for Health Statistics has fielded a mail survey of office-based physicians, the National Electronic Health Records Survey (NEHRS). ONC helps fund this supplement to track office-based physician adoption and the use of EHRs for health information exchange and patient engagement. Starting in 2010, the NEHRS's sample size was increased to allow for state-level estimates. The data set estimates each measure nationally and individually for each state and the District of Columbia beginning in 2010, unless otherwise noted.",
+            "title": "Office-based Physician Health IT Adoption and Use",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/nehrs.csv",
+                    "mediaType": "text/csv",
+                    "title": "nehrs.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/office-based-physician-health-it-adoption-and-use"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135198.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "cder",
+                "clinical investigator"
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
+            "identifier": "9dcfa54e-3b0c-40c8-b2fe-754820bed30f",
+            "description": "The Clinical Investigator Inspection List (CLIIL) contains names, addresses, and other pertinent information gathered from inspections of clinical investigators who have performed studies with investigational new drugs. The list contains information on inspections that have been closed since July 1977.",
+            "title": "Clinical Investigator Inspector List (CLIIL)",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM111343.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "describedBy": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/EnforcementActivitiesbyFDA/ucm073059.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P3M"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-iii-nys-1978",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "aspirations",
+                "behavior problems",
+                "career goals",
+                "community involvement",
+                "delinquent behavior",
+                "depression (psychology)",
+                "deviance",
+                "drugs",
+                "expectations",
+                "family conflict",
+                "family relations",
+                "health services utilization",
+                "life events",
+                "neighborhood conditions",
+                "parental attitudes",
+                "parents",
+                "peer influence",
+                "sexual behavior",
+                "social attitudes",
+                "social behavior",
+                "social isolation",
+                "social values",
+                "socioeconomic status",
+                "spouse abuse",
+                "substance abuse",
+                "teenage pregnancies",
+                "victimization",
+                "young adults",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537",
+            "description": "<p>Youth data for the third wave of the National Youth Survey<br />\nare contained in this data collection, which includes data for youth<br />\ninterviewed in 1979 about events and behavior of the preceding year.<br />\nThe first wave of this study was conducted in 1976 and the<br />\nsecond wave in 1977. Data were collected on the<br />\ndemographic and socioeconomic status of respondents, disruptive events<br />\nin the home, youth aspirations, expectations for future goals, social<br />\nisolation, normlessness, labeling, perceived disapproval, attitudes<br />\ntoward deviance, exposure and commitment to delinquent peers, sex<br />\nroles, attitudes toward sexual assault, interpersonal violence,<br />\npressure for substance abuse by peers, exposure to substance abuse by<br />\nparents, self-reported delinquency, and drug and alcohol use.This study has 1 Data Set.</p>",
+            "title": "National Youth Survey US:  Wave III (NYS-1978)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537",
+                    "description": "National Youth Survey US:  Wave III (NYS-1978) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nsfg/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+            "issued": "2020-10-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2017/2019",
+            "modified": "2023-12-12",
+            "references": [
+                "https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-MainText-508.pdf"
+            ],
+            "keyword": [
+                "births",
+                "cohabitation",
+                "contraception",
+                "health",
+                "infertility",
+                "marriage",
+                "pregnancy",
+                "sdoh-access-to-health-care",
+                "sdoh-employment",
+                "sdoh-food-access",
+                "sdoh-food-insecurity",
+                "sdoh-health-literacy",
+                "sdoh-higher-education",
+                "sdoh-high-school",
+                "sdoh-housing-stability",
+                "sdoh-incarceration",
+                "sdoh-language",
+                "sdoh-poverty-income",
+                "sdoh-use-of-health-care",
+                "survey"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nsfg@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ihtq-qs57",
+            "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
+            "title": "National Survey of Family Growth 2017-2019 Public-Use Files",
+            "isPartOf": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+                    "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
+                    "@type": "dcat:Distribution",
+                    "title": "National Survey of Family Growth 2017-2019 Public-Use Files"
+                }
+            ],
+            "spatial": "US",
+            "describedBy": "Nationally representative sample of women and men in the household population ages 15-49",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/ie2e-2dst",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2023-06-07",
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
+            "identifier": "5e2eb7ef-c735-5aa0-9e78-da25fa18ff2f",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_files_allDownloads",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20230426v2_ETL_DEV/files_allDownloads.csv",
+                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"featAuto\", \"update_id\": \"20230426v2_ETL_DEV\"}",
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
+            "landingPage": "https://data.cdc.gov/d/swv3-ghj7",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
+                "hepatitis",
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
+            "identifier": "https://data.cdc.gov/api/views/swv3-ghj7",
+            "description": "NNDSS - Table II. Hepatitis (viral, acute) C - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n *Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Based on the CSTE Position Statement 15-ID-03: Revision of the Case Definition of Hepatitis C for National Notification, acute hepatitis C is now reported by case classification status.",
+            "title": "NNDSS - Table II. Hepatitis (viral, acute) C",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swv3-ghj7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swv3-ghj7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swv3-ghj7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swv3-ghj7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ifsn-wqrr",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-29",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-28",
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
+            "identifier": "c657d635-87c6-4a2c-a098-7ccc85d22462",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-21-to-2023-08-27",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-08-21-2023-to-08-27-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-21-to-2023-08-27"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/igis-mx5s",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-10-19",
+            "@type": "dcat:Dataset",
+            "modified": "2022-10-25",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan id crosswalk",
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
+            "identifier": "46fdeb9e-921a-4141-a231-1bbe3dd14f61",
+            "description": "The Plan ID Crosswalk PUF (CW-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The purpose of the CW-PUF is to map QHPs and SADPs offered through the Exchanges during the previous plan year to plans that will be offered through the Exchanges in the current plan year.",
+            "title": "Plan ID Crosswalk PUF \u2013 PY2023",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/plan_id_crosswalk_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mpx5-t7tu",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-03-31",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-12-29/2023-07-29",
+            "modified": "2025-01-30",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "hhs region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "puerto rico",
+                "state",
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
+            "identifier": "https://data.cdc.gov/api/views/mpx5-t7tu",
+            "description": "This file contains COVID-19 death counts, death rates, and percent of total deaths by jurisdiction of residence. The data is grouped by different time periods including 3-month period, weekly, and total (cumulative since January 1, 2020). United States death counts and rates include the 50 states, plus the District of Columbia and New York City. New York state estimates exclude New York City. Puerto Rico is included in HHS Region 2 estimates.\n\nDeaths with confirmed or presumed COVID-19, coded to ICD\u201310 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.\n\nData during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.\n\nDeath counts should not be compared across states. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly. \n\nThe ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.\n\nRates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).\n\nRates are based on deaths occurring in the specified week/month and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly/monthly age-adjusted rates which have been adjusted to allow comparison with annual rates.  Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly/monthly) rate prevailed for a full year.\n\nSub-national death counts between 1-9 are suppressed in accordance with NCHS data confidentiality standards. Rates based on death counts less than 20 are suppressed in accordance with NCHS standards of reliability as specified in NCHS Data Presentation Standards for Proportions (available from: https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf.).",
+            "title": "Provisional COVID-19 death counts, rates, and percent of total deaths, by jurisdiction of residence",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States, Puerto Rico",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "references": [
+                "http://www.accessdata.fda.gov/scripts/cder/dissolution/index.cfm"
+            ],
+            "keyword": [
+                "cder",
+                "dissolution"
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
+            "identifier": "3f2b8dee-6c80-4230-8f8a-3f7c83920d42",
+            "description": "For a drug product that does not have a dissolution test method in the United States Pharmacopeia (USP), the FDA Dissolution Methods Database provides information on dissolution methods presently recommended by the Division of Bioequivalence, Office of Generic Drugs.",
+            "title": "Dissolution Methods Database",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P3M"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-08-04",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2020-07-04",
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
+            "identifier": "https://data.cdc.gov/api/views/sf7h-sajc",
+            "description": "Cumulative provisional counts of deaths sex, race/Hispanic origin, age group, and by select underlying causes of death. The dataset also includes provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death. Includes deaths that occurred between January 1, 2020 to July 4, 2020.",
+            "title": "AH Cumulative Provisional Death Counts by Sex, Race, and Age from 1/1/2020 to 7/4/2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/art/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-30",
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
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4yy2-qa9v",
+            "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Summary dataset provides a full snapshot of clinic services and profile, patient characteristics, and ART success rates. It is worth noting that patient medical characteristics, such as age, diagnosis, and ovarian reserve, affect ART treatment\u2019s success. Comparison of success rates across clinics may not be meaningful because of differences in patient populations and ART treatment methods. The success rates displayed in this dataset do not reflect any one patient\u2019s chance of success. Patients should consult with a doctor to understand their chance of success based on their own characteristics.",
+            "title": "2020 Final Assisted Reproductive Technology (ART) Summary",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yy2-qa9v/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yy2-qa9v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yy2-qa9v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yy2-qa9v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/4yy2-qa9v",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Assisted Reproductive Technology (ART)"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/ij3a-jt2x",
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
+            "identifier": "582424b1-9548-5ebe-9a0d-9e50031fbfaa",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2005",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588",
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2005)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2005) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588"
+                }
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/namcs/hcc/aboutnamcs.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2023-08-25",
+            "@type": "dcat:Dataset",
+            "temporal": "2021-2022",
+            "modified": "2024-03-05",
+            "keyword": [
+                "advanced practice providers",
+                "electronic health records",
+                "encounter",
+                "federally-qualified-health-center",
+                "fqhc",
+                "health center",
+                "health center component",
+                "health center encounter",
+                "namcs",
+                "physicians",
+                "research-data-center",
+                "visit characteristics",
+                "visit data"
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
+            "identifier": "https://data.cdc.gov/api/views/g795-gzp9",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) is designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. NAMCS began in 1973 as a national probability sample survey of visits to nonfederally employed office-based physicians. NCHS conducted the survey annually through 1981, again in 1985, and annually through 2021 (collection of visit data from physicians was stopped during 2020\u20132021 due to the burden placed on respondents by the COVID-19 pandemic). In 2006, a separate sample of Community Health Centers (CHCs) was added to the survey; the CHC component samples visits to both physicians and advanced practice providers (nurse practitioners, PAs [physician assistants and physician associates], and certified nurse midwives). Starting in 2012, in addition to the traditional NAMCS file, a separate data file for CHCs including physicians and advanced practice providers has been released.\n\nIn 2021, the former CHC sample of NAMCS was redesigned and launched as the NAMCS Health Center (HC) Component, collecting visit data from HCs using electronic health records, or EHR, systems of the participating health centers. The NAMCS Health Center Component contains critical data about health centers and the care they provide.",
+            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2021-2022, restricted data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
+                    "mediaType": "text/html",
+                    "description": "Link to the Standard Application Process attached."
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component has randomly selected a nationally representative sample of health centers that provide health care services to the public and have an electronic health record, or EHR, system. Eligible health centers include:  Federally Qualified Health Centers (FQHCs; section 330-funded) FQHC Look-alikes (FQHC\u2013LALs; not federally funded) Currently, Indian Health Service Centers are not eligible for the NAMCS Health Center Component.",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/yakh-mjxn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
+                "cryptosporidiosis",
+                "dengue",
+                "dengue virus infection",
+                "mmwr",
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
+            "identifier": "https://data.cdc.gov/api/views/yakh-mjxn",
+            "description": "NNDSS - Table II. Cryptosporidiosis to Dengue - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Includes data for dengue and dengue-like illness.",
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://pubmed.ncbi.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "data distribution",
+                "dataset",
+                "literature",
+                "pubmed"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bg8v-b9q4",
+            "description": "PubMed is a free resource supporting the search and retrieval of biomedical and life sciences literature with the aim of improving health\u2013both globally and personally.\n\nThe PubMed database contains citations and abstracts of biomedical literature. It does not include full text journal articles; however, links to the full text are often present when available from other sources, such as the publisher's website or PubMed Central (PMC). \n\nSee the PubMed User Guide for more information. https://pubmed.ncbi.nlm.nih.gov/help/",
+            "title": "MEDLINE/PubMed Citations",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/",
+                    "description": "NLM produces a baseline set of MEDLINE/PubMed citation records in XML format for download on an annual basis. The annual baseline is released in December of each year. The best practice is to overwrite your local data with baseline data each year. MEDLINE/PubMed data conforms to the PubMed DTD. See our Data Elements documentation for more information. https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd",
+                    "@type": "dcat:Distribution",
+                    "title": "Download - MEDLINE/PubMed - Annual Baseline"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/",
+                    "description": "Subsequent to the annual baseline release, NLM produces daily update files. These files include new, revised and deleted citations. If you are incorporating these files into a local database, load the baseline files first, then load the daily update files in numerical order. Revised or deleted citations should replace existing citations in your local database. More than one update file may become available on the same day. MEDLINE/PubMed data conforms to the PubMed DTD. See our Data Elements documentation for more information. https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd",
+                    "@type": "dcat:Distribution",
+                    "title": "Download MEDLINE/PubMed - Daily Update Files"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pubmed.ncbi.nlm.nih.gov/help/",
+                    "mediaType": "text/html",
+                    "title": "PubMed User Guide"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/bsd/pmresources.html",
+                    "mediaType": "text/html",
+                    "title": "PubMed Additional Resources"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Literature"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-14",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-05-22",
+            "keyword": [
+                "adults",
+                "covid-19 vaccination"
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
+            "identifier": "https://data.cdc.gov/api/views/brsb-akdp",
+            "description": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years \n\n\u2022 Estimated COVID-19 vaccination coverage among Medicare fee-for-service beneficiaries >65 years is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19. (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html)\n\u2003",
+            "title": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/4zxn-f9dq",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-08-15",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "healthcare personnel",
+                "healthcare workers"
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
+            "identifier": "https://data.cdc.gov/api/views/4zxn-f9dq",
+            "description": "Weekly cases among healthcare personnel, by week\n\n<b>Note:</b> Rows marked by \"missing date fields\" represent healthcare worker cases that were not associated with a date.",
+            "title": "COVID-19 Cases Among Healthcare Personnel, by week - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4zxn-f9dq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4zxn-f9dq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4zxn-f9dq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4zxn-f9dq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "theme": [
+                "Case Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-inpatient-hospital",
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
+                "hospitals & facilities",
+                "inpatient",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/1e1beaba-9b41-47ca-960a-bd47b6ea65bd/data-viewer",
+            "description": "The CMS Program Statistics -\u00a0Medicare Inpatient Hospital tables provide use and payment data for all inpatient hospitals, including short-stay hospitals, critical access hospitals, long term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, religious nonmedical health care institutions, children\u2019s hospitals, and other hospitals.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR INPT HOSP 1. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR INPT HOSP 2. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR INPT HOSP 3. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR INPT HOSP 4. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Hospital\n\tMDCR INPT HOSP 5. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR INPT HOSP 6. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment\n\tMDCR INPT HOSP 7. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR INPT HOSP 8. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Type of Entitlement and Total Days of Care\n\tMDCR INPT HOSP 9. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Location and Bedsize of Hospitals, by Medical School Affiliation, and Type of Control\n\tMDCR INPT HOSP 10.\u00a0 Special-Category Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by\u00a0Type of Hospital",
+            "title": "CMS Program Statistics - Medicare Inpatient Hospital",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/CPS%20MDCR%20INPT%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20INPT%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/CPS_MDCR_INPT_HOSP_1-10.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/CPS%20MDCR%20INPT%20HOSP%20ALL%202018.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2019-12/CPS_MDCR_INPT_HOSP_2017.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_INPT_HOSP_ALL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_INPT_HOSP_ALL_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_INPT_HOSP_ALL_1.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_INPT_HOSP_ALL_2.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2013-12-31"
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
+            "landingPage": "https://data.cdc.gov/d/8xkx-amqh",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-12-09",
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
+            "identifier": "https://data.cdc.gov/api/views/8xkx-amqh",
+            "description": "Overall US COVID-19 Vaccine administration and vaccine equity data at county level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
+            "title": "COVID-19 Vaccinations in the United States,County",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/rm6c-ns6x",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-09-23",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-08",
+            "keyword": [
+                "books",
+                "data distribution",
+                "literature",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rm6c-ns6x",
+            "description": "NLM produces bibliographic records for books, journals and other materials from NLM's collections in NLMXML, MARCXML and MARC 21 formats. These records can be searched at NLM LocatorPlus or the NLM Catalog.",
+            "title": "Catalog Record Data",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "application/xml",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catpluslease",
+                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - CatfilePlus"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfileplus",
+                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - CatfilePlus"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catplusbase",
+                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - CatfilePlus"
+                },
+                {
+                    "mediaType": "application/xml",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfilelease",
+                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - Serfile"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfile",
+                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - Serfile"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfilebase",
+                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - Serfile"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfile",
+                    "description": "Catfile contains fully cataloged bibliographic records in all formats.\n\n",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - Catfile"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfilebase",
+                    "description": "Catfile contains fully cataloged bibliographic records in all formats.\n\n",
+                    "@type": "dcat:Distribution",
+                    "title": "Download Catalog Record Data - Catfile"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://support.nlm.nih.gov/knowledgebase/article/KA-04188/en-us",
+                    "description": "MARC data are available from NLM's Z39.50 endpoint.",
+                    "@type": "dcat:Distribution",
+                    "title": "Catalog Record Data API via Z39.50 Endpoint"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/NBK25501/",
+                    "description": "NLM Catalog Record Data are available from the Entrez Programming Utilities.",
+                    "@type": "dcat:Distribution",
+                    "title": "Catalog Record DataAPI via Entrez Programming Utilities"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.nlm.nih.gov/databases/dtd/nlmcatalogrecordset_200101.dtd",
+                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
+                    "@type": "dcat:Distribution",
+                    "title": "Documentation - Data Element Documentation and DTDs"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.nlm.nih.gov/databases/dtd/nlmserials_200101.dtd",
+                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
+                    "@type": "dcat:Distribution",
+                    "title": "Documentation - Data Element Documentation and DTDs"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.nlm.nih.gov/bsd/licensee/catrecordxml_element_desc2.html",
+                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
+                    "@type": "dcat:Distribution",
+                    "title": "Documentation - Data Element Documentation and DTDs"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-23",
+            "temporal": "1988/2018",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-11",
+            "keyword": [
+                "adults",
+                "black or african american",
+                "body mass index",
+                "body weight",
+                "chronic conditions",
+                "health risk factors",
+                "health us",
+                "hispanic or latino",
+                "men",
+                "mexican",
+                "obesity",
+                "older persons",
+                "overweight",
+                "poverty",
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
+            "identifier": "https://data.cdc.gov/api/views/sqt4-6a3k",
+            "description": "Data on overweight and obesity among adults aged 20 and over in the United States, by selected characteristics, including sex, age, race, Hispanic origin, and poverty level. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Normal weight, overweight, and obesity among adults aged 20 and over, by selected characteristics: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sqt4-6a3k/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sqt4-6a3k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sqt4-6a3k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sqt4-6a3k/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/iq3g-u3cv",
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
+            "identifier": "3fcf8272-a6ca-49a4-96aa-ef0d72563984",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-02-to-2023-01-08",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-01022023-to-01082023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-02-to-2023-01-08"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-mental-health-services-survey-n-mhss-2010-0",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "mental health",
+                "mental health services",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561",
+            "description": "<p>The National Mental Health Services Survey (N-MHSS) is an annual survey designed to collect statistical information on the numbers and characteristics of all known mental health treatment facilities within the 50 States, the District of Columbia, and the U.S. territories. In every other year, beginning in 2014, the survey also collects statistical information on the numbers and demographic characteristics of persons served in these treatment facilities as of a specified survey reference date.<br />\nThe N-MHSS is the only source of national and State-level data on the mental health service delivery system reported by both publicly-operated and privately-operated specialty mental health treatment facilities, including: public psychiatric hospitals; private psychiatric hospitals, non-federal general hospitals with separate psychiatric units; U.S. Department of Veterans Affairs medical centers; residential treatment centers for children; residential treatment centers for adults; outpatient or day treatment or partial hospitalization mental health facilities; and multi-setting (non-hospital) mental health facilities.</p>\n<p>The N-MHSS complements the information collected through SAMHSA's survey of substance abuse treatment facilities, the National Survey of Substance Abuse Treatment Services (N-SSATS). Treatment facility Information from the N-MHSS is used to populate the mental health component of SAMHSA's online Behavioral Health Treatment Services Locator. <a href=\"http://findtreatment.samhsa.gov/This\">http://findtreatment.samhsa.gov/This</a> study has 1 Data Set.</p>",
+            "title": "National Mental Health Services Survey (N-MHSS-2010)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561",
+                    "description": "National Mental Health Services Survey (N-MHSS-2010) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/iqcf-c2jg",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-12-20",
+            "@type": "dcat:Dataset",
+            "modified": "2023-12-19",
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
+            "identifier": "ae0d720a-eafc-44dc-88ab-65da83917ec2",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-11-to-2023-12-17",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-12112023-to-12172023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-11-to-2023-12-17"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rksx-33p3",
+            "bureauCode": [
+                "009:15"
+            ],
+            "issued": "2021-07-29",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-03",
+            "keyword": [
+                "cares act",
+                "coronavirus",
+                "covid-19",
+                "health system",
+                "provider relief fund",
+                "uninsured"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Chief Data Officer",
+                "hasEmail": "mailto:PRFdata@hrsa.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/rksx-33p3",
+            "description": "The COVID-19 Claims Reimbursement to Health Care Providers and Facilities for Testing, Treatment, and Vaccine Administration for the Uninsured Program provides reimbursements on a rolling basis directly to eligible health care entities for claims that are attributed to the testing, treatment, and or vaccine administration of COVID-19 for uninsured individuals. The program funding information is as follow:\n\nTESTING\nThe American Rescue Plan Act (ARP) which provided $4.8 billion to reimburse providers for testing the uninsured; the Families First Coronavirus Response Act (FFCRA) Relief Fund, which includes funds received from the Public Health and Social Services Emergency Fund, as appropriated in the FFCRCA (P.L. 116-127) and the Paycheck Protection Program and Health Care Enhancement Act (P.L. 116-139) (PPPHCEA), which each appropriated $1 billion to reimburse health care entities for conducting COVID-19 testing for the uninsured.\n \nTREATMENT & VACCINATION\nThe Provider Relief Fund, which includes funds received from the Public Health and Social Services Emergency Fund, as appropriated in the Coronavirus Aid, Relief, and Economic Security (CARES) Act (P.L. 116-136), provided $100 billion in relief funds. The PPPHCEA appropriated an additional $75 billion in relief funds and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act (P.L. 116-260) appropriated another $3 billion. Within the Provider Relief Fund, a portion of the funding from these sources will be used to support healthcare-related expenses attributable to the treatment of uninsured individuals with COVID-19 and vaccination of uninsured individuals. To learn more about the program, visit: https://www.hrsa.gov/CovidUninsuredClaim\n\nThis dataset represents the list of health care entities who have agreed to the Terms and Conditions and received claims reimbursement for COVID-19 testing of uninsured individuals, vaccine administration and treatment for uninsured individuals with a COVID-19 diagnosis.\n\nFor Provider Relief Fund Data - https://data.cdc.gov/Administrative/HHS-Provider-Relief-Fund/kh8y-3es6",
+            "title": "Claims Reimbursement to Health Care Providers and Facilities for Testing, Treatment, and Vaccine Administration  of the Uninsured",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rksx-33p3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rksx-33p3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rksx-33p3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rksx-33p3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Administrative"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/isn2-adwk",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-04-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-11",
+            "keyword": [
+                "cms-64 expenditures",
+                "financial management report",
+                "national totals"
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
+            "identifier": "4011579c-33ea-5741-a763-a2558d635561",
+            "description": "This dataset reports summary state-by-state total expenditures by program for the Medicaid Program, Medicaid Administration and CHIP programs.  These state expenditures are tracked through the automated Medicaid Budget and Expenditure System/State Children's Health Insurance Program Budget and Expenditure System (MBES/CBES).\r\n\r\nFor more information, visit https://medicaid.gov/medicaid/finance/state-expenditure-reporting/expenditure-reports/index.html.",
+            "title": "Medicaid Financial Management Data \u2013 National Totals",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/medicaid-financial-management-data-national-totals.h7at-haku.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
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
+            "landingPage": "https://healthdata.gov/d/ispy-gjtf",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-16",
+            "@type": "dcat:Dataset",
+            "modified": "2023-10-24",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan id crosswalk",
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
+            "identifier": "0fa89e4e-e206-4b3d-bde5-c4d9246255c5",
+            "description": "The Plan ID Crosswalk PUF (CW-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The purpose of the CW-PUF is to map QHPs and SADPs offered through the Exchanges during the previous plan year to plans that will be offered through the Exchanges in the current plan year.",
+            "title": "Plan ID Crosswalk PUF - PY2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/plan_id_crosswalk_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/5avu-ff58",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-12",
+            "@type": "dcat:Dataset",
+            "modified": "2019-10-11",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/5avu-ff58",
+            "description": "NNDSS - Table II. Tuberculosis - 2019.  This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying WONDER data. Data on United States will exclude counts from US territories. \nFootnote: C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable. -: No reported cases. N: Not reportable. NN: Not Nationally Notifiable Cum: Cumulative year-to-date counts. Min: Minimum. Max: Maximum. \n* Case counts for reporting year 2018 and 2019 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf \n\u2020 Data for TB are displayed quarterly.",
+            "title": "NNDSS - Table II. Tuberculosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5avu-ff58/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5avu-ff58/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5avu-ff58/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5avu-ff58/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
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
+            "identifier": "4a439dda-f8d4-4461-ba4c-082abab102d4",
+            "description": "This database provides descriptions of radiation-emitting products that have been recalled under an approved corrective action plan to remove defective and noncompliant products from the market. Searches may be done by manufacturer name, performance standard, product name, description, or date range.",
+            "title": "Radiation Emitting Product Corrective Actions and Recalls",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/uniform-facility-data-set-us-ufds-1997",
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
+            "identifier": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557",
+            "description": "<p>The Uniform Facility Data Set (UFDS), formerly the National Drug and Alcohol Treatment Unit Survey or NDATUS, was designed to measure the scope and use of drug abuse treatment services in the United States. The survey collects information from each privately- and publicly-funded facility in the country that provides substance abuse treatment as well as from state-identified facilities that provide other substance abuse services. Data are collected on a number of topics including facility operation, services provided (assessment, therapy, testing, health, continuing care, programs for special groups, transitional services, community outreach, ancillary), type of treatment, facility capacity, numbers of clients, and various client characteristics. The main objective of the UFDS is to produce data that can be used to assess the nature and extent of substance abuse treatment services, to assist in the forecast of treatment resource requirements, to analyze treatment service trends, to conduct national, regional, and state-level comparative analyses of treatment services and utilization, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its on-line equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.  Additionally, the UFDS provides information that can be used to design sampling frames for other surveys of substance abuse treatment facilities.This study has 1 Data Set.</p>",
+            "title": "Uniform Facility Data Set US (UFDS-1997)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557",
+                    "description": "Uniform Facility Data Set US (UFDS-1997) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557"
+                }
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
+            "identifier": "https://data.cdc.gov/api/views/vtt8-av2v",
+            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
+            "title": "Quitline \u2013 Services Available \u2013 Hours Of Operation And Available Languages - 2010 To Present",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vtt8-av2v/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vtt8-av2v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vtt8-av2v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vtt8-av2v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Hours-Of-Operation-And/vtt8-av2v",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Quitline"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/iuk7-b344",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-12-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2025",
+                "qhp",
+                "qhp landscape instructions"
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
+            "identifier": "d7865dc4-7c70-4bee-9e88-eaf6d4c7da28",
+            "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2025 Individual Medical",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/med-ind-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/w46e-8kr3",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
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
+            "identifier": "https://data.cdc.gov/api/views/w46e-8kr3",
+            "description": "NNDSS - TABLE 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease \u2013 2021.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w46e-8kr3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w46e-8kr3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w46e-8kr3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w46e-8kr3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-outpatient-hospitals/medicare-outpatient-hospitals-by-provider-and-service",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2015-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-04",
+            "references": [
+                "https://data.cms.gov/resources/medicare-outpatient-hospitals-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "outpatient facilities"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ccbc9a44-40d4-46b4-a709-5caa59212e50/data-viewer",
+            "description": "The Medicare Outpatient Hospitals by Provider and Service dataset provides information on services for Original Medicare Part B beneficiaries by OPPS hospitals. These datasets contain information on the number of services, payments, and submitted charges organized by provider CMS Certified Number (CCN) and comprehensive Ambulatory Payment Classification (APC).",
+            "title": "Medicare Outpatient Hospitals - by Provider and Service",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ccbc9a44-40d4-46b4-a709-5caa59212e50/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/860428c0-6102-4fff-812d-57c7860613e5/MUP_OUT_RY24_P04_V10_DY22_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/456dbe68-8878-49dd-889b-bb8bf432fcbe/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/657f3480-6e15-4978-8e4d-78bfa03b7a79/MUP_OUT_RY24_P04_V10_DY21_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a7617aef-046f-4557-8a2a-54f9c9a88b57/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/62b3e7e6-674f-4f74-8c52-c1e32d3905eb/MUP_OUT_RY24_P04_V10_DY20_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8281e9f7-1874-4bd9-a183-a74bec2debd3/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/MUP_OUT_RY21_P04_V10_DY19_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f3fc4327-f66e-49e1-ba06-f2607a164406/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/MUP_OHP_R20_P04_V10_D18_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c52aa19e-38d1-40a3-b918-80add25502aa/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-06/MUP_OHP_R19_P04_V40_D17_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e5b339e2-0caa-4a01-b547-71e9eb3b4c17/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-06/MUP_OHP_R19_P04_V40_D16_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d7112a9d-aeb6-4242-a0bf-0bb07e442445/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-06/MUP_OHP_R19_P04_V40_D15_Prov_Svc.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/42381a9e-676d-4392-baf2-155559c1c26f/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Outpatient Hospitals - by Provider and Service : 2015-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-outpatient-hospitals-by-provider-and-service-data-dictionary",
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
+            "landingPage": "https://healthdata.gov/d/iwbk-66ew",
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
+            "identifier": "5e020af5-c00c-5055-8aaa-3c2f11ba3cfe",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_briefType",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/briefType.csv",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "identifier": "https://data.cdc.gov/api/views/mx2d-yjrk",
+            "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Demographic Characteristics \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023.  (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
+            "title": "Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine by Demographic Characteristics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.xml?accessType=DOWNLOAD",
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
+            "identifier": "https://data.cdc.gov/api/views/qwpv-wpc8",
+            "description": "2009. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "title": "CDC PRAMStat Data for 2009",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qwpv-wpc8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qwpv-wpc8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qwpv-wpc8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qwpv-wpc8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2009/qwpv-wpc8",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Maternal & Child Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/aq5t-7aga",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aq5t-7aga",
+            "description": "<b>(Includes MeSH 2023 and 2024 changes)</b> The MeSH 2025 Update - Add Report lists new Descriptors and Supplementary Concept Records (SCRs) that have been added to MeSH for the upcoming new release.  It also includes terms that replace deleted terms, as well as new entry combinations (new precoordinated descriptor heading that replaces an existing descriptor/subheading combination).  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
+            "title": "MeSH 2025 Update - Add Report",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aq5t-7aga/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aq5t-7aga/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aq5t-7aga/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aq5t-7aga/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/gtr/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ggb5-vr2q",
+            "description": "Genetic Testing Registry (GTR) is a free, centralized voluntary registry of comprehensive genetic test information covering clinical and research tests for Mendelian disorders and drug responses including multigenic, array-based, biochemical, cytogenetic, and molecular tests.",
+            "title": "Genetic Testing Registry (GTR)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/gtr/",
+                    "mediaType": "text/html",
+                    "title": "Genetic Test Registry (GTR) Homepage"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/iye8-2kz6",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2022-10-06",
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
+            "identifier": "5fe32037-4a6f-5c53-80e8-26414747c39c",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_files_topicSnapshot",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
+                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"prodAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "files_topicSnapshot csv file"
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
+            "landingPage": "https://data.cdc.gov/d/eg2p-49pd",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-13",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Physical Effects Research Branch (PERB), National Institute for Occupational Safety and Health (NIOSH) Health Effects Laboratory Division (HELD),",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/eg2p-49pd",
+            "description": "Working with vibrating hand tools is associated with the development of hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms, finger blanching and changes in sensory function.  Vibration plays a major role in the development of the symptoms that are characteristic of HAVS, however, the hands and fingers of worker using tools are also exposed to pressure applied as the workers grip tools.  The pressure applied by gripping a tool might also affect blood flow and sensorineural function.  Therefore, this study examined the effects of applied pressure [2 and 4 newtons (N)] on peripheral vascular and sensorineural function using a characterized rat tail model.  The tails of rats were exposed to 0, 2 or 4N of applied force for 10 days.  Blood flow (laser doppler) and sensitivity of the tail to pressure (Randall-Selitto pressure test) was measured on days 1, 5 and 10 of the exposure.  The sensitivity of the tail nerves to electrical stimulation was measured on days 2 and 9.",
+            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/eg2p-49pd/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/q78n-cpzf",
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
+                "fn": "National Center for Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/q78n-cpzf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 1 is the first round of a three-round survey. The probability sample of RANDS during COVID-19 Round 1 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from June 9, 2020 to July 6, 2020. The RANDS during COVID-19 Round 1 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "title": "NCHS Research and Development Survey (RANDS) Round 1 during COVID-19 probability sampled Restricted File",
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
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_1_technical_documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/iznq-47kj",
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
+            "identifier": "a29cf229-575a-531a-adaa-cf3dbf77defd",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_measure_allStates",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates.csv",
+                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_allStates csv file"
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
+            "landingPage": "https://mor.nlm.nih.gov/RxClass/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-09-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "classification",
+                "drugs",
+                "supplements",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4mcj-vnc6",
+            "description": "The RxClass Browser is a web application for exploring and navigating through the class hierarchies to find the RxNorm drug members associated with each class.\n\nRxClass links drug classes of several drug sources including ATC, MeSH, NDF-RT and FDA/SPL to their RxNorm drug members (ingredients, precise ingredients and multiple ingredients).\n\nRxClass allows users to search by class name or identifier to find the RxNorm drug members or, conversely, search by RxNorm drug name or identifier to find the classes that the RxNorm drug is a member of.",
+            "title": "RxClass",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://rxnav.nlm.nih.gov/RxClassAPIs.html",
+                    "mediaType": "text/html",
+                    "title": "API"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://mor.nlm.nih.gov/RxClass/#",
+                    "mediaType": "text/html",
+                    "title": "Search RxClass"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/4bc2-bbpq",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-08",
+            "@type": "dcat:Dataset",
+            "temporal": "2018-01-06/2024-02-17",
+            "modified": "2025-01-24",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "deaths",
+                "influenza",
+                "mortality",
+                "nchs",
+                "nvss",
+                "respiratory-virus-response",
+                "rsv",
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
+            "identifier": "https://data.cdc.gov/api/views/4bc2-bbpq",
+            "description": "This file contains the provisional percent of total deaths by week for COVID-19, Influenza, and Respiratory Syncytial Virus for deaths occurring among residents in the United States. Provisional data are based on non-final counts of deaths based on the flow of mortality data in National Vital Statistics System.",
+            "title": "Provisional Percent of Deaths for COVID-19, Influenza, and RSV",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bc2-bbpq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bc2-bbpq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bc2-bbpq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bc2-bbpq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2018-10-24",
+            "@type": "dcat:Dataset",
+            "modified": "2024-04-30",
+            "references": [
+                "https://chronicdata.cdc.gov/d/vtwh-8kxg"
+            ],
+            "keyword": [
+                "cigar",
+                "cigarette",
+                "combustibles",
+                "loose tobacco",
+                "non-combustibles",
+                "per capita",
+                "pipe tobacco",
+                "roll-your-own tobacco",
+                "smokeless",
+                "tobacco consumption"
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
+            "identifier": "https://data.cdc.gov/api/views/rnvb-cpxx",
+            "description": "2000 to Present. Adult Tobacco Consumption in the U.S. This dataset highlights critical trends in adult total and per capita consumption of both combustible (cigarettes, little cigars, small cigars, pipe tobacco, roll-your-own tobacco) tobacco products and smokeless (chewing tobacco and snuff) tobacco from 2000 to present. To view the CDC MMWR report, please visit https://www.cdc.gov/mmwr/volumes/65/wr/mm6548a1.htm.",
+            "title": "Adult Tobacco Consumption In The U.S., 2000-Present",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnvb-cpxx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnvb-cpxx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnvb-cpxx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnvb-cpxx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Policy/Adult-Tobacco-Consumption-In-The-U-S-2000-Present/rnvb-cpxx",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Policy"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-30",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-30",
+            "references": [
+                "https://www.cdc.gov/breastfeeding/data/nis_data/index.htm"
+            ],
+            "keyword": [
+                "breastfed",
+                "breastfeeding",
+                "child",
+                "dnpao",
+                "infants",
+                "national immunization survey",
+                "nis",
+                "nutrition"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DNPAO Public Inquiries",
+                "hasEmail": "mailto:dnpaoinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8hxn-cvik",
+            "description": "This dataset includes breastfeeding data from the National Immunization Survey (NIS). This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding. For more information about breastfeeding and NIS visit https://www.cdc.gov/breastfeeding/data/nis_data/index.htm.",
+            "title": "Nutrition, Physical Activity, and Obesity - National Immunization Survey (Breastfeeding)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-National-I/8hxn-cvik",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Nutrition",
+                "Physical Activity",
+                "and Obesity"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/hmd/ihm/index.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-24",
+            "keyword": [
+                "history of medicine",
+                "images"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/62wp-7g64",
+            "description": "Images from the History of Medicine (IHM) in NLM Digital Collections provides online access to images from the historical collections of the U.S. National Library of Medicine. IHM includes image files of a wide variety of visual media including fine art, photographs, engravings, and posters that illustrate the social and historical aspects of medicine dating from the 15th to 21st century.",
+            "title": "Images from the History of Medicine",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/hmd/ihm/index.html",
+                    "mediaType": "text/html",
+                    "title": "Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://collections.nlm.nih.gov/web_service.html",
+                    "description": "Images from the History of Medicine is accessible programmatically via the NLM Digital Collections web service.",
+                    "@type": "dcat:Distribution",
+                    "title": "API"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Images"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://dailymed.nlm.nih.gov/dailymed/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "api",
+                "drug label",
+                "drugs",
+                "supplements",
+                "united states"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n7e9-np3x",
+            "description": "DailyMed provides health information providers and the public with a standard, comprehensive, up-to-date, look-up and download resource of medication content and labeling as found in medication package inserts, also known as Structured Product Labeling (SPL).",
+            "title": "DailyMed",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dailymed.nlm.nih.gov/dailymed/index.cfm",
+                    "mediaType": "text/html",
+                    "title": "DailyMed Homepage and Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dailymed.nlm.nih.gov/dailymed/spl-resources.cfm",
+                    "mediaType": "text/html",
+                    "title": "Download DailyMed Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm",
+                    "mediaType": "text/html",
+                    "title": "Access DailyMed API"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Consumer Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/kikd-77zw",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
+                "cryptosporidiosis",
+                "dengue",
+                "dengue virus infection",
+                "mmwr",
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
+            "identifier": "https://data.cdc.gov/api/views/kikd-77zw",
+            "description": "NNDSS - Table II. Cryptosporidiosis to Dengue - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP:  Nationally notifiable but not published.  Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.   Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Includes data for dengue and dengue-like illness. Office of Management and Budget approval of the NNDSS Revision #0920-0728 on January 21, 2016, authorized CDC to receive data for these conditions. CDC is in the process of soliciting data for these conditions.",
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/cucp-zsht",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
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
+            "identifier": "https://data.cdc.gov/api/views/cucp-zsht",
+            "description": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://datatools.ahrq.gov/hcupnet",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2021-02-13",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "references": [
+                "https://datatools.ahrq.gov/hcupnet/glossary"
+            ],
+            "keyword": [
+                "claims",
+                "community health",
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
+                "quality indicators",
+                "readmissions",
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
+            "identifier": "1f692757-76c2-47d0-a39f-2ac3c0ecbd66",
+            "description": "HCUPnet is an online data tool based on data from the Healthcare Cost and Utilization Project (HCUP).\n\nThe data tool provides healthcare statistics and information for hospital inpatient and emergency department settings, as well as population-based healthcare data on counties. Users are able to query HCUP data to access detailed or summary statistics on inpatient stays and emergency department visits by patient, hospital, and encounter characteristics. Users are also able to generate tables and graphs on national and regional statistics and trends for community hospitals in the United States.",
+            "title": "HCUPnet",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://hcupnet.ahrq.gov/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "https://datatools.ahrq.gov/hcupnet/methodology"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2005",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2005)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2005) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/j5g5-dyyq",
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
+            "identifier": "a66fa666-3854-5bc3-b8f8-9367a10cb40f",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_measure_allStates_downloadLink",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates_downloadLink.csv",
+                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+            "landingPage": "https://healthdata.gov/d/j62p-6uef",
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
+            "identifier": "90b4f584-cdf9-5d81-a106-f1781f8ba706",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_topicArea_measureDisplayGroups",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/topicArea_measureDisplayGroups.csv",
+                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+            "landingPage": "https://data.cdc.gov/d/yu68-juzt",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Division of Safety Research, Protective Technology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/yu68-juzt",
+            "description": "The accommodation of worker anthropometric variability in the workplace and personal protective equipment (PPE) is key to safe and efficient completion of work tasks. Previously, the best data available was 46 years old, which has largely become outdated due to demographic changes. These data tables consist of 34 traditional semi-nude body dimensions without gear (e.g., chest depth, standing; foot breadth, horizontal, standing; hip circumference; stature; elbow rest height, sitting; and eye height, sitting) and 15 dimension measurements over clothing and with gear (e.g., abdominal extension depth, sitting; hip breadth, sitting; and should-grip length, sitting) of 756 male and 218 female Law Enforcement Officers (LEOs). For many LEOs, patrol vehicles are the workplace where they spend significant portions of their workday and PPE is vital gear to safeguard LEOs from the harm of assaults. Design improvements of vehicle console space, vehicle ingress/egress, and LEO body-worn equipment can result in reduced LEO fatigue, pain, or injury.",
+            "title": "Anthropometry of Law Enforcement Officers",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/yu68-juzt/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/j6tg-9r9f",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-03",
+            "references": [
+                "https://download.medicaid.gov/data/Keywords.csv"
+            ],
+            "keyword": [
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
+            "identifier": "0d425780-16be-4ded-8420-69def8f4ee29",
+            "description": "Division of Pharmacy Releases Index dataset. The list of keywords for this dataset can be found in Additional information table below.",
+            "title": "Division of Pharmacy Releases Index dataset",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/division-of-pharmacy-releases-07032024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2018-01-01/2018-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "references": [
+                "https://data.cms.gov/resources/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes-methodology"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medicare"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CLFS Inquires - CM",
+                "hasEmail": "mailto:CLFS_Inquiries@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/0e57f57d-0acc-4c9c-8f8c-973e3f4a3c4b/data-viewer",
+            "description": "The Medicare Clinical Laboratory Fee Schedule (CLFS) dataset provides raw data reported by any applicable laboratories that reported a volume greater than 10 tests for the data collection period. As described by the Protecting Access to Medicare Act, Applicable Laboratories must report to CMS private payor rates and associated volumes for laboratory tests on the Clinical Laboratory Fee Schedule.",
+            "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0e57f57d-0acc-4c9c-8f8c-973e3f4a3c4b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/CLFS%20Applicable%20Information%202018%20Raw%20Data%20File-updated%2012152021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1f39e9a2-5f75-4b39-831a-cff0a2096832/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes : 2018-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes-data-dictionary",
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
+            "landingPage": "https://data.cdc.gov/d/wgyw-mswy",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
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
+            "identifier": "https://data.cdc.gov/api/views/wgyw-mswy",
+            "description": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgyw-mswy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgyw-mswy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgyw-mswy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgyw-mswy/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/mv87-mh7a",
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
+            "identifier": "https://data.cdc.gov/api/views/mv87-mh7a",
+            "description": "NNDSS - TABLE 1GG.  Spotted fever rickettsiosis, Confirmed to Smallpox - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://rgd.mcw.edu/",
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
+                "fn": "LUO, JAMES",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "c6c39d59-80c6-4ed8-a97e-09752c52f9f6",
+            "description": "<p>The Rat Genome Database (RGD) is a collaborative effort between leading research institutions involved in rat genetic and genomic research to collect, consolidate, and integrate data generated from ongoing rat genetic and genomic research efforts and make these data widely available to the scientific community.</p>",
+            "title": "Rat Genome Database (RGD)",
+            "programCode": [
+                "009:003"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/krkm-t59m",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-11-17",
+            "@type": "dcat:Dataset",
+            "modified": "2015-11-17",
+            "keyword": [
+                "malaria"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Gimnig",
+                "hasEmail": "mailto:hzg1@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/krkm-t59m",
+            "description": "This data set is from 3 surveys conducted in two districts in western Kenya following the scale up of insecticide treated nets and the implementation of IRS in one of the districts.",
+            "title": "PONE-D-15-23803",
+            "programCode": [
+                "009:036"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/j83z-us86",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-02",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-01",
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
+            "identifier": "7dd8dbcf-53ca-43eb-a423-003026e24972",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-24-to-2023-07-30",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-07-24-2023-to-07-30-2023.csv.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-24-to-2023-07-30"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.ncbi.nlm.nih.gov/genbank/",
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
+                "fn": "Mizrachi, Ilene",
+                "hasEmail": "mailto:mizrachi@ncbi.nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "810d7c33-6139-4976-884f-b2c3cdb1c8e3",
+            "description": "<p>GenBank is the NIH genetic sequence database, an annotated collection of all publicly available DNA sequences. GenBank is designed to provide and encourage access within the scientific community to the most up to date and comprehensive DNA sequence information.</p>",
+            "title": "GenBank",
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
+            "landingPage": "https://data.cdc.gov/d/5pe9-px25",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
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
+            "identifier": "https://data.cdc.gov/api/views/5pe9-px25",
+            "description": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5pe9-px25/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5pe9-px25/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5pe9-px25/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5pe9-px25/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/j8fd-jyui",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-07-27",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
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
+            "identifier": "695e7a86-00c1-49b1-935a-6fef6cbf5835",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-17-to-2023-07-23",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-07-17-2023-to-07-23-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-17-to-2023-07-23"
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
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2007",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2007)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2007) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/6nbv-ifib",
+            "bureauCode": [
+                "009:032"
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
+            "identifier": "https://data.cdc.gov/api/views/6nbv-ifib",
+            "description": "This dataset provides data at the county level for the contiguous United States. It includes monthly Standardized Precipitation Evapotranspiration Index (SPEI)  data from 1895-2016 provided by the Cooperative Institute for Climate and Satellites - North Carolina. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate drought measures. Learn more about drought on the Tracking Network's website: https://ephtracking.cdc.gov/showDroughtLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
+            "title": "Standardized Precipitation Evapotranspiration Index, 1895-2016",
+            "programCode": [
+                "009:20"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/j9pn-7wwd",
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
+            "identifier": "cd577ff7-f5a3-599d-9fc9-102d5e220d7c",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_tafVersion",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/tafVersion.csv",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://data.cms.gov/provider-compliance/fee-for-service-error-rate-improper-payment/medicare-fee-for-service-comprehensive-error-rate-testing",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2011-01-01/2024-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-03",
+            "references": [
+                "https://data.cms.gov/resources/medicare-fee-for-service-comprehensive-error-rate-testing-improper-payment-data-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "medicare",
+                "original medicare"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Comprehensive Error Rate Testing (CERT) Program - OFM",
+                "hasEmail": "mailto:CERT@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6395b458-2f89-4828-8c1a-e1e16b723d48/data-viewer",
+            "description": "The Medicare Fee-for-Service (FFS) Comprehensive Error Rate Testing (CERT) dataset provides information on a random sample of FFS claims to determine if they were paid properly under Medicare coverage, coding, and payment rules. The dataset contains information on type of FFS claim, Diagnosis Related Group (DRG) and Healthcare Common Procedure Coding System (HCPCS) codes, provider type, type of bill, review decision, and error code.\n\n\u00a0\n\nPlease note, each reporting year (RY) contains claims submitted July 1 two years before the report\u00a0through June 30 one year before the report. For example, the 2024 data contains claims submitted July 1, 2022 through June 30, 2023.",
+            "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6395b458-2f89-4828-8c1a-e1e16b723d48/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/9512fdeb-578d-428e-bddb-458338517cfb/2024%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/81f4f6c8-0f55-49f1-a338-4f92a859263b/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/8e1e39c7-859f-455b-9eab-6bb3d63e516c/2023%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a3334602-31c4-45b0-95ee-988c6274032e/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/16676776-b9f0-4740-8345-5cc3f84e63db/2022%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2022-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/755391cc-6682-419d-9c95-d0905fea78d4/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2022-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/4267ffed-b89a-402a-8c70-a048b32ae642/2021%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/749f218f-0669-4925-885c-a4b40b6f0480/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/2020%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8e02cc09-8179-4aaf-a437-c6012642f9af/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Medicare_FFS_CERT_Data_2019.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6b92a8b2-efaa-49ae-8a01-1922ef1fe534/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Medicare_FFS_CERT_Data_2018.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2018-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e9d0fb3a-ca8d-4e80-8bd3-0ae336ac76e6/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2018-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Nov17%20PartAPartB%20Public%20Data_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2017-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bcdc6155-64f8-4f0d-8ae4-dd31cfd3b61e/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2017-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Nov16%20PartAPartB%20Public%20Data_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2016-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/13a30957-b6e7-4d4e-b82c-a88b581d1ac9/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2016-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Nov15%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2015-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b974bc10-e684-4972-80fa-b2280bb2f018/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2015-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Nov14%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2014-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d7e943c8-853e-4cb0-ae1d-9ba37414e451/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2014-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Nov13%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2013-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/151d88cc-4872-4567-8a65-7afbd6b8f60b/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2013-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Nov12%20PartAPartB%20Public%20Data_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2012-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e14016d4-599b-4cf9-b1d8-da6953947bb8/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2012-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/Nov11%20PartAPartB%20Public%20Data.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2011-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e171a6e4-21a9-4eed-aed5-fd6f845bdccb/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2011-02-13"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-fee-for-service-comprehensive-error-rate-testing-improper-payment-data-dictionary",
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
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "public",
+            "issued": "2015-12-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1933/2018",
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
+                "births",
+                "maternal age",
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
+            "identifier": "https://data.cdc.gov/api/views/isx2-c2ii",
+            "description": "This dataset includes percent distribution of births for females by age group in the United States since 1933.\n\nThe number of states in the reporting area differ historically. In 1915 (when the birth registration area was established), 10 states and the District of Columbia reported births; by 1933, 48 states and the District of Columbia were reporting births, with the last two states, Alaska and Hawaii, added to the registration area in 1959 and 1960, when these regions gained statehood. Reporting area information is detailed in references 1 and 2 below. Trend lines for 1909\u20131958 are based on live births adjusted for under-registration; beginning with 1959, trend lines are based on registered live births.",
+            "title": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
+            "isPartOf": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
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
+            "identifier": "650b8214-c3a4-46f6-8a10-5d182339c0d6",
+            "description": "The CDRH FOIA electronic reading room contains frequently requested information via the Freedom of Information Act from the Center for Devices and Radiological Health.",
+            "title": "CDRH FOIA Electronic Reading Room",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
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
+            "identifier": "https://data.cdc.gov/api/views/eanj-9nie",
+            "description": "Weekly COVID-19 Vaccination Coverage of Adults18 Years and Older by Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM)(https://www.cdc.gov/nis/about/index.html). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
+            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324, Overall, by Jurisdiction Among Adults 18 Years",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-10-26",
+            "@type": "dcat:Dataset",
+            "modified": "2023-12-04",
+            "references": [
+                "https://www.census.gov/programs-surveys/acs/data.html",
+                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
+            ],
+            "keyword": [
+                "acs",
+                "estimates",
+                "place",
+                "places",
+                "sdoh"
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
+            "identifier": "https://data.cdc.gov/api/views/edkk-ze78",
+            "description": "This dataset contains place-level (incorporated and census-designated places) social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service: https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
+            "title": "SDOH Measures for Place, ACS 2017-2021",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/home-infusion-therapy-providers",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-18",
+            "temporal": "2023-05-07/2025-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-07",
+            "references": [
+                "https://data.cms.gov/resources/home-infusion-therapy-providers-methodology"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "outpatient facilities",
+                "outpatient physical therapy",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data-viewer",
+            "description": "The Home Infusion Therapy Providers dataset provides information on the Providers in Medicare who specialize in Home Infusion Therapy.",
+            "title": "Home Infusion Therapy Providers",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Home Infusion Therapy Providers : 2025-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/ab9ed0b6-73d6-4023-969b-bfad85b2ddcd/Home%20Infusion%20Therapy%201.6.2025.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2025-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8596aa47-d4d4-4149-bc80-eb52e2d3a761/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2025-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/51dac38c-b579-4141-baf5-7e5aec7924fd/Home%20Infusion%20Therapy%2012.23.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e14f5b0-1bc6-4b07-952e-786711893997/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/8ba0ca11-14e1-4dcf-84df-5e589af8f62f/Home%20Infusion%20Therapy%2012.9.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-12-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b045ef18-e306-4f1d-b710-04cd335a7895/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-12-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/56a56562-678f-4b3d-b6d7-12e97c5c3d67/Home%20Infusion%20Therapy%2011.25.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-11-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/edda6a20-cae6-41b9-8594-ec90ab0edf3f/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-11-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/b24b7e90-8cc8-4091-a3c6-251a86c3e9f4/Home%20Infusion%20Therapy%2011.12.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/86c2aadc-7836-45a3-9962-bb7f31d86877/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/76a5a885-2a94-4dd2-987c-41ffaa801730/Home%20Infusion%20Therapy%2010.28.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/28835aba-de78-4e14-b76f-d9c880342b9a/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/a9a9c427-df93-4b30-9a58-e9897a661ff9/Home%20Infusion%20Therapy%2010.15.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-10-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/11bee001-3af6-49f0-86cd-2ff3e372d6c0/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-10-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/3d133010-2bbd-425c-85f8-0923efffef7d/Home%20Infusion%20Therapy%209.30.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4ef9fdd8-2543-4415-a4b4-a339c8b6ee36/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/32cb6953-750c-4f35-ad2f-0c1fe9febe4b/Home%20Infusion%20Therapy%209.16.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-09-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bb7bc7cb-86cc-405f-b379-b1783b8d4be2/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-09-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/7d90d08c-3faf-4ba7-b186-9f773a240d54/Home%20Infusion%20Therapy%209.3.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-09-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/db8830fb-0de4-4ac0-97ee-f68d8fd700eb/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-09-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/981ac67a-f5b9-4e72-a88b-2b63285d7b00/Home%20Infusion%20Therapy%208.19.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-08-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a89247df-5f9f-4b56-bdf3-14530b30de2c/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-08-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/788614b8-fc39-480f-b262-bb40acc6ac84/Home%20Infusion%20Therapy%208.5.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-08-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/18d04805-5e3a-4645-9b64-6a62d08ae5ee/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-08-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/00741270-45b8-4655-8fa4-f92f492afdde/Home%20Infusion%20Therapy%207.22.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-07-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8451233d-0bc1-4ae5-a422-1ecfbd4414c5/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-07-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/e73b7a79-077b-4de1-9673-35f6ee2145b6/Home%20Infusion%20Therapy%207.8.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-07-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/34b4d0d9-6127-44bc-9ba8-13006bcff99e/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-07-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/4d340e2d-abd5-4b4d-a2f3-1a28b44bf9b2/Home%20Infusion%20Therapy%206.24.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-06-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/49ba4df7-1f31-4b68-979d-37a08440d65c/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-06-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/3a7b7834-be2c-487b-9857-d49593da1d01/Home%20Infusion%20Therapy%206.10.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-06-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f984f522-3a5d-4fe0-ab1e-c42f8aa0107e/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-06-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/f94db978-d795-47d9-b811-9251f59f65fa/Home%20Infusion%20Therapy%205.27.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-05-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5fc05909-1f6c-4926-8002-61a0623351df/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-05-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/14f4cdd6-6b3d-49c5-8c37-bed1f19c7ee8/Home%20Infusion%20Therapy%205.15.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-05-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/71887189-9d27-48bd-a4a8-5864d667baf5/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-05-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/7e812996-009e-488f-916a-5897be832747/Home%20Infusion%20Therapy%205.6.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-05-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b65b680d-aac2-4aea-bc51-fc5a3bdd0396/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-05-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/3d81abd4-c352-4761-8672-d43ba76e6813/Home%20Infusion%20Therapy%204.22.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-04-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cd4db424-23ca-40fd-87e0-a8dfceb1b94e/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-04-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/bcb776ec-ee3e-4b41-9e93-e64b24a0e19c/Home%20Infusion%20Therapy%204.8.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-04-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b22ad616-c507-4774-b2fb-77ae14b30ed3/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-04-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/7dd8ecc0-27ff-4d3e-a7b7-6fc5a628e872/Home%20Infusion%20Therapy%203.25.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-03-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1dba13c6-07b3-4687-9aca-78ffda9ffd9c/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-03-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/a0645e94-4abe-41ce-87d6-faf616e105df/Home%20Infusion%20Therapy%203.11.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-03-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9116e170-6df0-4e14-a8dd-26acae6486eb/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-03-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/075e1ce7-a2fd-4fd6-8a0e-8396d181075c/Home%20Infusion%20Therapy%202.26.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-02-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/20d8dfe6-a7bf-4e95-901b-12db792b8998/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-02-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/750fda9a-65f3-4421-bb6a-8ff768692880/Home%20Infusion%20Therapy%202.12.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/db54201d-9c1e-4b05-bad4-766d5f1e2150/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/a49c47a3-1984-48f7-9a13-cc2e49f1ca5e/Home%20Infusion%20Therapy%201.29.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-01-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e0fc2c94-d507-48a0-9023-a2b329587f26/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-01-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/ccf2bd40-7060-4df3-b7ee-6bd5e1c172cd/Home%20Infusion%20Therapy%201.16.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-01-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ffc5c501-5afc-475a-a3b9-e92434021129/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-01-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/8c89d6f5-1975-426e-ab9e-bde671477a2d/Home%20Infusion%20Therapy%201.2.2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3665883-a1a6-4079-b776-db16825fa9de/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/b5412976-cd08-4594-aeed-1225611839d9/Home%20Infusion%20Therapy%2012.19.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-12-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee0b3463-6a97-444d-b81f-e59a8f067c16/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-12-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/04ef54c0-0b86-47fd-801b-f20e8f383d38/Home%20Infusion%20Therapy%2011.22.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-11-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/44c9c855-3308-42d2-882e-969f7d0168d3/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-11-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/70d01c6d-0761-4cae-8ef0-405e2f22d15b/Home%20Infusion%20Therapy%2010.27.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-10-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e1b91378-0377-4deb-a3cf-663eb9544673/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-10-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/68fbba81-f338-4e5e-8ee2-c9613832830a/Home%20Infusion%20Therapy%2010.12.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-10-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3aab410-1c04-42d5-ad97-a9fe9b916a73/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-10-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/3160a3e2-526e-45c8-bb92-c0f17b99ce73/Home%20Infusion%20Therapy%2009.29.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-09-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ddfb7fb3-86ba-40e1-979f-ddcbd9149677/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-09-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/bc6da7c8-f327-44e0-ae76-c336efb7351d/Home%20Infusion%20Therapy%2009.14.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-09-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d6e25ad2-598c-4ad9-9430-8eb596b1eeb3/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-09-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8c1ac232-330f-4853-9805-7417c3e81b20/Home%20Infusion%20Therapy%2008.31.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-08-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/991a98b9-64d7-4a33-ac26-7c1a1471f435/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-08-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/bf9d90fc-dca3-47bc-9d22-a239ccbda4f9/Home%20Infusion%20Therapy%2008.18.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-08-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/277b8532-670e-4f2b-bd7d-7a3921c296df/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-08-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/e3c3808b-84df-42c7-81fe-9d622cbd4199/Home%20Infusion%20Therapy%2008.04.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-08-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e8ee2dbb-d135-45ba-8feb-03cddb0b0bf4/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-08-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/e62afdc9-e5d2-4d70-bc87-d48d1739c992/Home%20Infusion%20Therapy%2007.20.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-07-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09ae777f-10cf-4790-acee-5b513482f801/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-07-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/3e4d46bf-c011-4baa-a075-1c4608db5622/Home%20Infusion%20Therapy%2007.07.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-07-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3eb706ec-7494-4608-9b03-6dc374ce3ae8/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-07-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/aec0d657-f330-498a-8383-4ce6ccb5014b/Home%20Infusion%20Therapy%2006.22.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-06-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f424a96b-1288-4089-ac11-de6a8d2a46af/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-06-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/73194870-bc08-41c5-8283-d954a812fd94/Home%20Infusion%20Therapy%2006.08.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-06-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e1f868a9-a28f-4bd8-ac70-cfa1616039e8/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-06-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/3283d350-5de4-4db2-8536-64abd6adaae3/Home%20Infusion%20Therapy%2005.25.2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Infusion Therapy Providers : 2023-05-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4c81d8d9-b534-45d3-91e8-c72c90595152/data",
+                    "mediaType": "text/html",
+                    "title": "Home Infusion Therapy Providers : 2023-05-25"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/home-infusion-therapy-providers-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P2W",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/medicare-provider-and-supplier-taxonomy-crosswalk",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2021-07-01/2025-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-17",
+            "references": [
+                "https://data.cms.gov/resources/medicare-provider-and-supplier-taxonomy-crosswalk-methodology"
+            ],
+            "keyword": [
+                "medical suppliers & equipment",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/113eb0bc-0c9a-4d91-9f93-3f6b28c0bf6b/data-viewer",
+            "description": "The Medicare Provider and Supplier Taxonomy Crosswalk dataset lists the providers and suppliers eligible to enroll in Medicare programs with the proper healthcare provider taxonomy code. This data includes the Medicare speciality codes, if available, provider/supplier type description, taxonomy code, and the taxonomy description.",
+            "title": "Medicare Provider and Supplier Taxonomy Crosswalk",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/113eb0bc-0c9a-4d91-9f93-3f6b28c0bf6b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/7b0ea92d-2f70-424e-bec4-3fd35dc9a597/Medicare_Provider_and_Supplier_Taxonomy_Crosswalk_JAN__2025.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c127e711-47ae-488a-9470-11b9055e3450/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/2019b560-c060-4499-8bb6-25ac9185e70f/Medicare_Provider_and_Supplier_Taxonomy_Crosswalk_DEC_10_2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/117b40ba-e414-4eea-b096-a9ef7f0b9573/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/a6ce71d4-84cd-4d96-9cd4-3ab6c8ee8798/Medicare_Provider_and_Supplier_Taxonomy_Crosswalk_October_2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2fd3474c-4315-4325-a2f4-99bbc5fb8c6e/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/2dfa900d-dcc3-49f3-9104-d88b9149de8e/Medicare_Provider_and_Supplier_Taxonomy_Crosswalk_July_19_2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2024-06-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/142c63b6-47e0-464b-a8bf-b8d8bf5b8eb7/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2024-06-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/0f9c6563-7b46-4a5a-b45d-260d75e375ed/Taxonomy%20Code%20List%20Dec%202023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c7a85e56-3226-4673-b582-f6a558932cbf/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/b8c64259-47c7-4912-950b-ac933989c2c0/Medicare_Provider_and_Supplier_Taxonomy_Crosswalk_September_2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/22f41f23-6653-441f-9c88-2b8fad98c662/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/8639b869-e4dd-4bea-bb67-f8de6bc870b6/Taxonomy_List.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2021-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/88bd5fb4-7b5c-4107-8131-23c485e00ef0/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2021-10-29"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-provider-and-supplier-taxonomy-crosswalk-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P6M",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-outpatient-facility",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-05-17",
+            "temporal": "2016-01-01/2021-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-05-16",
+            "references": [
+                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "outpatient facilities",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/bbcffb70-4b07-4a0b-a783-0722b89315b5/data-viewer",
+            "description": "The CMS Program Statistics \u2013 Medicare Advantage, Outpatient Facility tables provide utilization data for outpatient facilities, by Medicare Advantage beneficiaries.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\nBelow is the list of tables:\n\n\n\tMDCR OUTPATIENT MA 1. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR OUTPATIENT MA 2. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR OUTPATIENT MA 3. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Area of Residence",
+            "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202021%20FINAL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2021-05-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202020%20FINAL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2020-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202019%20FINAL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2019-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202018%20FINAL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2018-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202017%20FINAL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2017-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202016%20FINAL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2016-01-15"
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
+            "landingPage": "https://healthdata.gov/dataset/state-child-support-agencies-debt-compromise-policies",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2014-02-10",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "administrative",
+                "arrears management",
+                "case management",
+                "children's health",
+                "child support program",
+                "debt compromise",
+                "other",
+                "policy",
+                "program information",
+                "promising practices",
+                "state local child support agencies"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis.Putze",
+                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "identifier": "086ea269-2de3-4f89-b8c0-a517c9bacce2",
+            "description": "<p>Interactive Child Support Program Map - Click on State or Territory for more information regarding local policies to compromise child support debt owed to the state.</p>",
+            "title": "State Child Support Agencies With Debt Compromise Policies",
+            "programCode": [
+                "009:084"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/jcq7-czbz",
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
+            "identifier": "d8dc4c8b-3174-5aba-a777-f1ea0f4bdc7f",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_tafVersion",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/tafVersion.csv",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+                "census tracts",
+                "estimates",
+                "prevalence"
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
+            "identifier": "https://data.cdc.gov/api/views/5mtz-k78d",
+            "description": "2014, 2013. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census tract-level data in GIS-friendly format can be joined with census tract spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-Boundaries/x7zy-2xmx) in a geographic information system (GIS) to produce maps of 27 measures at the census tract level.",
+            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2016 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5mtz-k78d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5mtz-k78d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5mtz-k78d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5mtz-k78d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-level-Data-GIS-Friendly-Fo/5mtz-k78d",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/youth-risk-behavior-surveillance-system-yrbss",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2013-05-01",
+            "temporal": "1991-01-01T00:00:00-05:00/1991-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "children's health",
+                "epidemiology",
+                "health-related behaviors",
+                "national",
+                "population statistics",
+                "sexual assault",
+                "surveillance",
+                "survey",
+                "youth"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "YRBSS",
+                "hasEmail": "mailto:yrbss@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "identifier": "83a48652-f4c3-4d9c-8f04-3e59b6a50878",
+            "description": "<p>The Youth Risk Behavior Surveillance System (YRBSS) monitors 6 types of health-risk behaviors that contribute to the leading causes of death and disability among youth and adults, including: behaviors that contribute to unintentional injuries and violence; sexual behaviors that contribute to unintended pregnancy and sexually transmitted diseases (STDs), including HIV infection; alcohol and other drug use; tobacco use; unhealthy dietary behaviors; inadequate physical activity. YRBSS also measures the prevalence of obesity and asthma among youth and young adults. YRBSS includes a national school-based survey conducted by CDC and state, territorial, tribal, and local surveys conducted by state, territorial, and local education and health agencies and tribal governments.</p>",
+            "title": "Youth Risk Behavior Surveillance System (YRBSS)",
+            "programCode": [
+                "009:027"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/healthyyouth/yrbs/cdcreports.htm",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health",
+                "National"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/w54d-atna",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "brucellosis",
+                "campylobacteriosis",
+                "candida auris",
+                "clinical",
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
+            "identifier": "https://data.cdc.gov/api/views/w54d-atna",
+            "description": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Candida auris, clinical colonization/screening cases are not included in this table. These data are available on the Mycotic Diseases Branch's Tracking Candida auris page (https://www.cdc.gov/fungal/candida-auris/tracking-c-auris.html).",
+            "title": "NNDSS - TABLE 1F. Brucellosis to Candida auris, clinical",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w54d-atna/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w54d-atna/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w54d-atna/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w54d-atna/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533",
+            "description": "<p>This file includes data from the 2002 through 2011 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across one or more of the pair years, i.e., 2002-2003, 2004-2005, 2006-2007, 2008-2009, 2010-2011, or 2012-2013.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health: 2-Year R-DAS (NSDUH-2002-2003)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533",
+                    "description": "National Survey on Drug Use and Health: 2-Year R-DAS (NSDUH-2002-2003) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/4rd8-s7gn",
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
+            "identifier": "https://data.cdc.gov/api/views/4rd8-s7gn",
+            "description": "Understanding the host response to influenza A virus (IAV) infection is vital for developing intervention strategies. The primary barriers for invading respiratory pathogens are the airway epithelial cells of the respiratory tract and antimicrobial peptides produced by these cells. The antimicrobial peptide, \u03b2-defensin-1, has antiviral activity against both enveloped and non-enveloped viruses. Significant downregulation of \u03b2-defensin1 gene (DEFB1) expression was observed when human bronchial epithelial cells (HBEpCs) were exposed to IAV. HBEpCs overexpressing DEFB1 caused a significant reduction in IAV, that was confirmed by IAV matrix gene analysis and confocal microscopy. DEFB1expression after transfection with hsa-miR-186-5p and hsa-miR-340-5p provided evidence that DEFB1 expression could be modulated by these two miRNAs and hsa-miR-186-5p had a higher binding efficiency with DEFB1. Overexpression of DEFB1 in IAV infected HBEpCs led to increased NF-kB expression.  In a Polymerase Chain Reaction (PCR) array analysis of 84 transcription factors, either overexpressing DEFB1 or siRNA silencing of DEFB1 expression significantly modulated the expression of STAT3.  In addition, Ingenuity Pathway Analysis (IPA) integrated with PCR array data showed that the JAK1/STAT3 pathway was significantly altered by cells overexpressing DEFB1, suggesting that this may be one of the pathways by which defensin regulates IAV replication in HBEpCs. In conclusion, the reduction in IAV copy number in DEFB1 overexpressing cells suggests that \u03b2-defensin-1 plays a key role in regulating IAV survival through STAT3 and is a potential target for antiviral drug development.",
+            "title": "\u03b2-defensin-1 regulates influenza virus infection in human bronchial epithelial cells through the STAT3 signaling pathway",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/4rd8-s7gn/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/dataset/departmental-appeals-board-decisions-0",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1974-03-07T00:00:00-04:00/1974-03-07T00:00:00-04:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "abuse",
+                "acf",
+                "administrative",
+                "adopt",
+                "adoption",
+                "alj",
+                "antidumping",
+                "appeal",
+                "appellate",
+                "assessment",
+                "assistance",
+                "attorney fees",
+                "award",
+                "balance",
+                "beneficiary",
+                "benefit",
+                "billing",
+                "biologic",
+                "board",
+                "cancellation",
+                "charge",
+                "children",
+                "civil rights",
+                "clia",
+                "cmp",
+                "cms",
+                "code",
+                "collect",
+                "community health",
+                "community law",
+                "compliance",
+                "cost",
+                "coverage",
+                "dab",
+                "debar",
+                "debt",
+                "decision",
+                "denial",
+                "determination",
+                "device",
+                "disallowance",
+                "disapprove",
+                "discontinution",
+                "discrimination",
+                "doctor",
+                "drug",
+                "eligibility",
+                "eligible",
+                "embezzlement",
+                "enforcement",
+                "enrollee",
+                "enrollment",
+                "exclusion",
+                "expenditure",
+                "false claim",
+                "fda",
+                "fee",
+                "felony",
+                "fine",
+                "fiscal",
+                "foster care",
+                "fraud",
+                "funding",
+                "grant",
+                "head start",
+                "health care",
+                "hearing",
+                "hipaa",
+                "home health",
+                "hospice",
+                "hospital",
+                "ig",
+                "indian",
+                "induce",
+                "ineligible",
+                "insurance",
+                "invalid",
+                "judge",
+                "kickback",
+                "law",
+                "lcd",
+                "license",
+                "lobbying",
+                "marketing",
+                "medical equipment",
+                "medically necessary",
+                "medicare",
+                "misconduct",
+                "misdemeanor",
+                "misrepresent",
+                "modify",
+                "nf",
+                "non-compliance",
+                "nondisclosure",
+                "nursing facility",
+                "nursing home",
+                "obstruction",
+                "office of the interior",
+                "oi",
+                "oig",
+                "participation",
+                "patient",
+                "payment",
+                "penalty",
+                "performance standard",
+                "physician",
+                "plan",
+                "prescription",
+                "privacy",
+                "procedure",
+                "provider",
+                "qio",
+                "reasonable",
+                "recipient",
+                "reduction",
+                "repay",
+                "rescind",
+                "reverse",
+                "review",
+                "revocation",
+                "sanction",
+                "schip",
+                "security",
+                "snf",
+                "ssa",
+                "supplier",
+                "surgery",
+                "suspension",
+                "tanf",
+                "termination",
+                "theft",
+                "transaction",
+                "vaccine",
+                "violation",
+                "withold"
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
+            "identifier": "56e8ed0c-b29b-462e-aede-83b3e3c466a8",
+            "description": "<p>Decisions issued by the Chair and Board Members of the Departmental Appeals Board concerning determinations in discretionary, project grant programs, including disallowances, terminations and denials of refunding, cost allocation plan disapprovals, and rate determinations; determinations in mandatory grant programs, including disallowances of state claims under titles I, IV-A (Temporary Assistance for Needy Families), IV-D (Child Support Enforcement), IV-E (Foster Care and Adoption Assistance), X, XIV, XVI, XIX (Medicaid), and XXI (State Children's Health Insurance Program) of the Social Security Act; and appellate review of decisions of DAB Civil Remedies Division ALJs, decisions of Food and Drug Administration ALJs regarding civil money penalties, and decisions of Department of the Interior ALJs in Indian Health Service contract/compact cases.n.</p>",
+            "title": "Departmental Appeals Board Decisions",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "http://www.hhs.gov/dab/decisions/dabdecisions/index.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Community",
+                "Health",
+                "Medicare",
+                "Hospital"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/v4tm-h8pe",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-06-24",
+            "@type": "dcat:Dataset",
+            "modified": "2023-06-01",
+            "keyword": [
+                "antimicrobial resistance",
+                "carbapenem-resistant acinetobacter baumannii",
+                "carbapenem-resistant enterobacterales",
+                "enterobacter spp.",
+                "escherichia coli",
+                "haicviz",
+                "healthcare-associated infection",
+                "klebsiella spp.",
+                "surveillance"
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
+            "identifier": "https://data.cdc.gov/api/views/v4tm-h8pe",
+            "description": "<p>The healthcare-associated infection component of CDC\u2019s <a href=\"https://www.cdc.gov/ncezid/dpei/eip/index.html\" target=\"_blank\">EIP</a> engages a <a href=\"https://www.cdc.gov/ncezid/dpei/eip/eip-sites.html\" target=\"_blank\">network</a> of state health departments and their academic medical center partners to help answer critical questions about emerging HAI threats, advanced infection tracking methods, and antibiotic resistance in the United States. Information gathered through this activity will play a key role in shaping future policies and recommendations targeting HAI prevention. </p>",
+            "title": "HAICViz - MuGSI",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v4tm-h8pe/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v4tm-h8pe/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v4tm-h8pe/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v4tm-h8pe/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/7esm-uptm",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-19",
+            "keyword": [
+                "122 cities",
+                "2015",
+                "death",
+                "influenza",
+                "mortality",
+                "pneumonia"
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
+            "identifier": "https://data.cdc.gov/api/views/7esm-uptm",
+            "description": "TABLE III. Deaths in 122 U.S. cities - 2015122 Cities Mortality Reporting System \ufffd\ufffd\ufffd Each week, the vital statistics offices of 122 cities across the United States report the total number of death certificates processed and the number of those for which pneumonia or influenza was listed as the underlying or contributing cause of death by age group (Under 28 days, 28 days \ufffd\ufffd\ufffd1 year, 1-14 years, 15-24 years, 25-44 years, 45-64 years, 65-74 years, 75-84 years, and \ufffd\ufffd\ufffd 85 years).FOOTNOTE:U: Unavailable      -: No reported cases * Mortality data in this table are voluntarily reported from 122 cities in the United States, most of which have populations of 100,000 or more. A death is reported by the place of its occurrence and by the week that the death certificate was filed. Fetal deaths are not included. ** Totals include unknown ages. *** Partial counts for this city.",
+            "title": "TABLE III. Deaths in 122 U.S. cities",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/h3kf-bqpq",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/h3kf-bqpq",
+            "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/CMS-Medicare-Restricted.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-23",
+            "@type": "dcat:Dataset",
+            "temporal": "2014/2017",
+            "modified": "2024-10-11",
+            "references": [
+                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare14_18_linked_data-list_of_variables.pdf"
+            ],
+            "keyword": [
+                "linked medicare data",
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
+            "identifier": "https://data.cdc.gov/api/views/42pu-ymxu",
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the\u00a0National Hospital Care Survey (NHCS)\u00a0by augmenting it with 2014-2018 administrative data from the Centers for Medicare & Medicaid Services\u2019 (CMS) Medicare program. Linkage of NHCS data with the CMS Medicare Data provides the opportunity to conduct a vast array of studies on health care utilization and expenditures among the elderly U.S. population and persons receiving Medicare disability benefits.",
+            "title": "National Hospital Care Survey (NHCS) linked to Centers for Medicare & Medicaid (CMS) 2014-2018 Medicare Data",
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
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 12) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-linkage-methodology.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/fc5f-ixvg",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-07",
+            "keyword": [
+                "2019",
+                "arboviral diseases",
+                "babesiosis",
+                "nedss",
+                "netss",
+                "nndss",
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
+            "identifier": "https://data.cdc.gov/api/views/fc5f-ixvg",
+            "description": "NNDSS - Table 1D. Arboviral diseases, neuroinvasive and non-neuroinvasive, West Nile virus disease to Babesiosis - 2019.In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1D. Arboviral diseases, West Nile virus to Babesiosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/nnvr-zdhw",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-13",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Respiratory Health Division, Surveillance Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/nnvr-zdhw",
+            "description": "The National Study of Coal Workers\u2019 Pneumoconiosis (NSCWP) is a large, continuing epidemiologic study of the respiratory health of U.S. coal miners. By using information from the study, prevalence of coal workers\u2019 pneumoconiosis (CWP) was related to indexes of dust exposure obtained from research and compliance sampling data. Clear relationships between prevalences of both simple CWP and progressive massive fibrosis (PMF) and estimated dust exposure were seen. Additional effects independently associated with coal rank (% carbon) and age were also seen. Logistic model fitting indicated that between 2% and 12% of miners exposed to a 2-mg/m3 dust environment in bituminous coal mines would be expected to have Category 2 or greater CWP after a 40-yr working life; PMF would be expected for between 1.3% and 6.7%. The risks for anthracite miners appeared to be greater. There was a suggestion of a background level of abnormality, not associated with dust exposure, but increasing with age. Although there are certain we",
+            "title": "An Investigation Into the Relationship Between Coal Workers\u2019 Pneumoconiosis and Dust Exposure in U.S. Coal Miners",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/nnvr-zdhw/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/hget-9fst",
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
+            "identifier": "https://data.cdc.gov/api/views/hget-9fst",
+            "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 2 - New York",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/jf8m-mtc3",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-03-20",
+            "keyword": [
+                "2019",
+                "malaria",
+                "measles imported",
+                "measles indigenous",
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
+            "identifier": "https://data.cdc.gov/api/views/jf8m-mtc3",
+            "description": "NNDSS - TABLE 1V. Malaria to Measles, Imported - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \n\nNotice:  The total numbers of measles cases in Table 1v for weeks 1-51 in the 2019 data are correct but counts for imported and indigenous categories are incorrect. Measles data for week 52 (in Table 1v) were updated on 02-28-2020 to correct the classification of imported and indigenous. Please see week 52, 2019 data for the correct breakout of imported and indigenous measles cases.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\n\u00a7 Measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.",
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Imported",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/hh8a-ys2f",
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
+            "identifier": "https://data.cdc.gov/api/views/hh8a-ys2f",
+            "description": "The association between human respiratory disease transmission by respiratory droplets and aerosols is well established for several known pathogens.1 Given that the average individual spends > 90% of their day indoors, there has been intense focus on factors associated with indoor transmission. To minimize exposure risks, the Centers for Disease Control and Prevention (CDC) recommends behavioral and personal protective equipment mitigation strategies to limit COVID-19 transmission, including wearing masks, maintaining physical distances of  \u2265 1.8 m, and avoiding crowded indoor and outdoor spaces. As such, the current investigation examines the combined effect of physical distancing, universal masking, and ventilation on exposure to airborne particles generated during breathing and coughing within a controlled indoor environment. The results of this investigation quantitatively examine the contribution of the matrix of controls employed and provides guidance on respiratory disease mitigation strategies within the indoor environment.",
+            "title": "Reduction of exposure to simulated respiratory aerosols using ventilation, physical distancing, and universal masking",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/hh8a-ys2f/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/jirv-7bvn",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2014-11-07",
+            "temporal": "2015-01-01T00:00:00+00:00/2016-01-01T00:00:00+00:00",
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
+            "identifier": "4d7af295-2132-55a8-b40c-d6630061f3e8",
+            "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
+            "title": "NADAC (National Average Drug Acquisition Cost) 2015",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost.a4y5-998d.4d7af295-2132-55a8-b40c-d6630061f3e8.csv",
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
+            "landingPage": "https://healthdata.gov/d/jj4y-qp9m",
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
+            "identifier": "f48c4dc5-80d3-5528-8d79-238c124fe10d",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_states_measures",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures.csv",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-05-11",
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
+                "original medicare"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ee6fb1a5-39b9-46b3-a980-a7284551a732/data-viewer",
+            "description": "The Medicare Inpatient Hospitals by Provider dataset provides information on inpatient discharges for Original Medicare Part A beneficiaries by IPPS hospitals. It includes information on the use, payment, and hospital charges for more than 3,000 U.S. hospitals that received IPPS payments. The data are organized by hospital.",
+            "title": "Medicare Inpatient Hospitals - by Provider",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee6fb1a5-39b9-46b3-a980-a7284551a732/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/e95428bb-00a6-46e2-9be2-ffd9c6fe5186/MUP_INP_RY24_P04_V10_DY22_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cc73e77b-7367-48c9-b766-fafefe3f8ffa/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/ef80e842-4949-46e8-ab66-0c4c4310d400/MUP_INP_RY24_P04_V10_DY21_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c7e1501c-a770-4e2a-beb6-32b3525491a7/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/c2f4c3df-c7ec-4402-8064-7f7d2586ba56/MUP_INP_RY24_P04_V10_DY20_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d7b2810d-ac10-498f-8794-1c3d9f72ee96/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/1c1f6004-9fe2-43d0-907c-203322cd40e7/MUP_INP_RY24_P04_V10_DY19_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2019-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c349419e-3c6a-419e-8c74-0641b64cca12/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2019-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/7bb03a80-a0ed-4fd9-a7c8-c851c70d484b/MUP_INP_RY24_P04_V10_DY18_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2018-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8f65555-1540-44ef-9808-a64f29b15570/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2018-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/c016da49-525e-4c64-adc8-4bef70eabf32/MUP_INP_RY24_P04_V10_DY17_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2017-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/be4e1a28-8afe-40c3-8d8f-6dba7c539b64/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2017-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/16a75a1e-060b-42dd-b647-a7536eb0373c/MUP_INP_RY24_P04_V10_DY16_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2016-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f0fb93a4-3475-42de-b264-9a1e785f1ea4/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2016-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/1f667627-0c55-4237-b8e1-6545f9d43e75/MUP_INP_RY24_P04_V10_DY15_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2015-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5cae9291-4be8-4e3c-94f6-27aaf20c9ded/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2015-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/9c770459-6517-4763-ad3e-991ddf7c5d9f/MUP_INP_RY24_P04_V10_DY14_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2014-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b685142b-cc56-4ff1-98f1-06bddf2787f1/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2014-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/26990132-59b8-4de0-ba6e-811a756ff0c3/MUP_INP_RY24_P04_V10_DY13_Prv.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2013-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c5a33eaf-a076-4513-b057-4d10803deca8/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Provider : 2013-12-02"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-provider-data-dictionary",
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
+            "landingPage": "https://data.cdc.gov/d/ig4m-ub43",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-01-08",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "2014",
+                "chickenpox",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "varicella",
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
+            "identifier": "https://data.cdc.gov/api/views/ig4m-ub43",
+            "description": "NNDSS - Table II. Varicella to West Nile virus disease - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Updated weekly from reports to the Division of Vector-Borne Infectious Diseases, National Center for Zoonotic, Vector-Borne, and Enteric Diseases (ArboNet Surveillance). Data for California serogroup, eastern equine, Powassan, St. Louis, and western equine diseases are available in Table I. \ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table, except starting in 2007 for the Arboviral diseases and influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/document/SRCA_FINAL_REPORT_2006-2012_final.xlsx.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
+            "title": "NNDSS - Table II. Varicella to West Nile virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2017-12-06",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-30",
+            "keyword": [
+                "deaths",
+                "drug poisoning",
+                "mortality",
+                "national",
+                "nchs",
+                "state",
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
+            "identifier": "https://data.cdc.gov/api/views/xbxb-epbu",
+            "description": "This dataset describes drug poisoning deaths at the U.S. and state level by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning. \r\n\r\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\r\n\r\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132016 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Drug poisoning death rates may be underestimated in those instances.\r\n\r\nREFERENCES\r\n1. National Center for Health Statistics. National Vital Statistics System: Mortality data. Available from: http://www.cdc.gov/nchs/deaths.htm.\r\n\r\n2. CDC. CDC Wonder: Underlying cause of death 1999\u20132016. Available from: http://wonder.cdc.gov/wonder/help/ucd.html.",
+            "title": "NCHS - Drug Poisoning Mortality by State: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/jki3-r9ys",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-12-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "py2025",
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
+            "identifier": "c4b9735c-68d0-4f8e-9563-cba97783618e",
+            "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2025 Dental SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/den-shop-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/an65-3p9b",
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
+            "identifier": "https://data.cdc.gov/api/views/an65-3p9b",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, HHS Region 1 - Boston",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/child-coverage-vaccination.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-29",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024 & 2024-2025",
+            "modified": "2025-01-29",
+            "keyword": [
+                "flu vaccination",
+                "nis-ccm",
+                "nis-flu"
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
+            "identifier": "https://data.cdc.gov/api/views/vncy-2ds7",
+            "description": "\u2022 Weekly Cumulative Influenza Vaccination Coverage by Flu Season, Selected Demographics, and Race and Ethnicity Among 6 Months-17 Years. \n\n\u2022 Weekly Influenza vaccination coverage and parental intent for vaccination among children is calculated using data from the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html). NIS\u2013Flu is a national random-digit-dialed cellular telephone survey of households with children ages 6 months\u201317 years conducted during October-June. The respondent to a NIS\u2013Flu survey is a parent or guardian who said they were knowledgeable about the child\u2019s vaccination history. All estimates are based upon parental report of receipt of vaccination and month of that vaccination.",
+            "title": "Weekly Cumulative Influenza Vaccination Coverage by Flu Season, Selected Demographics, and Race and Ethnicity Among Children 6 Months-17 Years, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vncy-2ds7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vncy-2ds7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vncy-2ds7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vncy-2ds7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2018-10-16",
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
+            "identifier": "https://data.cdc.gov/api/views/djk3-k3zs",
+            "description": "2015, 2014. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. Because some questions are only asked every other year in the BRFSS, there are 7 measures in this 2017 release from the 2014 BRFSS that were the same as the 2016 release.",
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2017 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/sks5-7yq7",
+            "issued": "2018-06-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-07",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jarvis Sims",
+                "hasEmail": "mailto:xma4@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/sks5-7yq7",
+            "description": "A complete listing of subscription databases provided by the Stephen B. Thacker CDC Library.",
+            "title": "CDC Library Subscription Databases",
+            "programCode": [
+                "009:031"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sks5-7yq7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sks5-7yq7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sks5-7yq7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sks5-7yq7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/jmxz-6n7j",
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
+                "service use",
+                "t-msis analytic files",
+                "vaccination"
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
+            "identifier": "43d419f9-f863-4f68-b622-311a8800100d",
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of vaccinations provided to Medicaid and CHIP beneficiaries under age 19 (as of the first day of the month), by state. The following vaccinations are included: Chickenpox, DTaP, HPV, Hepatitis A, Hepatitis B, Influenza, MMR, Meningococcal, Meningococcal B, Pneumococcal conjugate, Pneumococcal polysaccharide, Polio, Rotavirus, Tdap, and all vaccinations. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating vaccination measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Vaccinations Provided to the Medicaid and CHIP Population under age 19",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/Vaccinations-Provided-to-the-MedicaidCHIP-Population-under-age-19.csv",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of vaccinations provided to Medicaid and CHIP beneficiaries under age 19 (as of the first day of the month), by state. The following vaccinations are included: Chickenpox, DTaP, HPV, Hepatitis A, Hepatitis B, Influenza, MMR, Meningococcal, Meningococcal B, Pneumococcal conjugate, Pneumococcal polysaccharide, Polio, Rotavirus, Tdap, and all vaccinations. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating vaccination measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Vaccinations Provided to the Medicaid and CHIP Population under age 19"
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
+            "landingPage": "https://data.cdc.gov/d/afja-b25e",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
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
+            "identifier": "https://data.cdc.gov/api/views/afja-b25e",
+            "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Data for H. influenzae (age <5 years for serotype b, nonserotype b, and unknown serotype) are available in Table I.",
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1992",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+                "heroin",
+                "households",
+                "inhalants",
+                "marijuana",
+                "methamphetamine",
+                "prescription drugs",
+                "sedatives",
+                "smoking",
+                "steroid use",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560",
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Data are<br />\nalso provided on treatment for drug use and on illegal activities<br />\nrelated to drug use. Questions include age at first use, as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco,<br />\nand nonmedical use of psychotherapeutics. Respondents were also asked<br />\nabout problems resulting from their use of drugs, alcohol, and<br />\ntobacco, their perceptions of the risks involved, insurance coverage,<br />\nand personal and family income sources and amounts. Demographic data<br />\ninclude gender, race, ethnicity, educational level, job status, income<br />\nlevel, household composition, and population density.This study has 1 Data Set.</p>",
+            "title": "National Household Survey on Drug Abuse (NHSDA-1992)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1992) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/jn5c-ypvd",
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
+            "identifier": "cb573493-01ed-531e-9a99-c1197f4db8e0",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_briefType",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/briefType.csv",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-online-tuberculosis-information-system-otis",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-08-03",
+            "temporal": "1993-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "age",
+                "alcohol use",
+                "case",
+                "correctional facility",
+                "drug resistant",
+                "drug susceptibility",
+                "epidemiology",
+                "ethnicity",
+                "foreign born",
+                "hiv status",
+                "homeless",
+                "incidence",
+                "injecting drug use",
+                "isoniazid",
+                "long term care facility",
+                "metropolitan area",
+                "msa",
+                "occupation",
+                "pulmonary",
+                "race",
+                "rifampin",
+                "sex",
+                "state",
+                "tb",
+                "therapy",
+                "tuberculosis",
+                "verification criteria",
+                "vital status",
+                "year"
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
+            "identifier": "9041abdb-0c6b-4398-bb69-8d7d88df4e5f",
+            "description": "<p>The Online Tuberculosis Information System (OTIS) on CDC WONDER contains information on verified tuberculosis (TB) cases reported to the Centers for Disease Control and Prevention (CDC) by state health departments, the District of Columbia and Puerto Rico since 1993. These data were extracted from the CDC national TB surveillance system. OTIS reports case counts, incidence rates, population counts, percentage of cases that completed therapy within 1 year of diagnosis, and percentage of cases tested for drug susceptibility. Data for 22 variables are included in the data set, including: age groups, race / ethnicity, sex, vital status, year reported, state, metropolitan area, several patient risk factors, directly observed therapy, disease verification criteria and multi-drug resistant TB. Each year these data are updated with an additional year of cases plus revisions to cases reported in previous years. OTIS is produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
+            "title": "CDC WONDER: Online Tuberculosis Information System (OTIS)",
+            "programCode": [
+                "009:027"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/tb.html",
+                    "mediaType": "text/html",
+                    "title": "Text"
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/tb.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/telemedicine-use.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-04-27",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-08-19/2022-07-11",
+            "modified": "2023-04-14",
+            "keyword": [
+                "covid-19",
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
+            "identifier": "https://data.cdc.gov/api/views/h7xa-837u",
+            "description": "To rapidly monitor recent changes in the use of telemedicine, the National Center for Health Statistics (NCHS) and the Health Resources and Services Administration\u2019s Maternal and Child Health Bureau (HRSA MCHB) partnered with the Census Bureau on an experimental data system called the Household Pulse Survey. This 20-minute online survey was designed to complement the ability of the federal statistical system to rapidly respond and provide relevant information about the impact of the coronavirus pandemic in the U.S.\n\nThe U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of the COVID-19 pandemic on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
+            "title": "Telemedicine Use in the Last 4 Weeks",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-07",
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
+            "identifier": "https://data.cdc.gov/api/views/hm35-qkiu",
+            "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Demographic Characteristics \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n \n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
+            "title": "Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-03-28",
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
+            "identifier": "https://data.cdc.gov/api/views/3myw-4j4q",
+            "description": "Cumulative Influenza Vaccination Coverage Age Group, Race/Ethnicity, and Jurisdiction, Adults 18 Years and Older, United States, National Immunization Survey Adult COVID Module.\n\nArchived data are available including for Figures 4B and 4C:  https://data.cdc.gov/resource/8dyx-9z99 \n\n\u2022  The National Immunization Survey-Adult COVID Module (NIS-ACM) was launched in April 2021 among adults 18 years and older. The survey was used to monitor COVID-19 vaccination uptake and confidence in vaccination among adults and included questions about influenza vaccination.",
+            "title": "Cumulative Influenza Vaccination Coverage by Race/Ethnicity and Age Group, NIS-ACM",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3myw-4j4q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3myw-4j4q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3myw-4j4q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3myw-4j4q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Approximately Monthly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/jpaz-yhdx",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "py2024",
+                "qhp",
+                "qhp landscape instructions",
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
+            "identifier": "77bae5d1-43da-4348-9679-82b7d1ce3eb8",
+            "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2024 Medical SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/med-shop-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
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
+                "brfss",
+                "census tract",
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
+            "identifier": "https://data.cdc.gov/api/views/cwsq-ngmh",
+            "description": "This dataset contains model-based census tract estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 40 measures: 12 for health outcomes, 7 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, 3 for health status, and 7 for health-related social needs. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population data, and American Community Survey 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2024 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/qvzb-qs6p",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-22",
+            "keyword": [
+                "abcs",
+                "active bacterial core surveillance",
+                "bactfacts",
+                "invasive pneumococcal disease serotypes",
+                "ipd serotype frequencies",
+                "ipd serotypes",
+                "spn serotypes",
+                "streptococcus pneumoniae serotypes"
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
+            "identifier": "https://data.cdc.gov/api/views/qvzb-qs6p",
+            "description": "CDC monitors invasive bacterial infections that cause bloodstream infections, sepsis, and meningitis in persons living in the community through Active Bacterial Core surveillance (ABCs). ABCs conducts laboratory- and population-based surveillance for invasive pneumococcal disease (IPD). ABCs serotype data are used to measure the impact of vaccine use in the United States on vaccine-type IPD. \n\nThis table reports IPD case counts in the ABCs catchment area by serotype for years 1998 through 2022. Cases are grouped into the following mutually exclusive age groups: age <2 years old, age 2\u20134 years old, age 5\u201317 years old, age 18\u201349 years old, age 50\u201364 years old, and age \u226565 years old.\n\nABCs methods and surveillance areas reporting IPD cases has changed over time. Given these changes, trends in serotype distribution by year and age group should be interpreted with caution. Additional information on ABCs methods and surveillance population is available at <a href=\"https://www.cdc.gov/abcs/methodology/index.html\">https://www.cdc.gov/abcs/methodology/index.html</a>.\n\nAnalyze and visualize data using the ABCs Bact Facts Interactive Data Dashboard at <a href=\"https://www.cdc.gov/abcs/bact-facts/data-dashboard.html?CDC_AAref_Val=https://www.cdc.gov/abcs/bact-facts-interactive-dashboard.html\">https://www.cdc.gov/abcs/bact-facts-interactive-dashboard</a>.",
+            "title": "1998-2022 Serotype Data for Invasive Pneumococcal Disease Cases by Age Group from Active Bacterial Core surveillance",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvzb-qs6p/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvzb-qs6p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvzb-qs6p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvzb-qs6p/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/x7ys-5vpn",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-17",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/x7ys-5vpn",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "Medicaid Coverage Of Cessation Treatments And Barriers To Treatments Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/x7ys-5vpn/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Cessation Coverage"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/non-federal-acute-care-hospital-health-it-adoption-and-use",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2021-12-01",
+            "references": [
+                "https://www.healthit.gov/data/apps/non-federal-acute-care-hospital-health-it-adoption-and-use",
+                "https://www.healthit.gov/data/quickstats/non-federal-acute-care-hospital-electronic-health-record-adoption"
+            ],
+            "keyword": [
+                "adoption",
+                "health care facilities",
+                "health information technology",
+                "health it",
+                "hospital",
+                "patient engagement",
+                "patient information"
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
+            "identifier": "4ace2vzk-eulv-7lnl-xxcj-kg2k8iivmu6m",
+            "description": "The adoption and use of electronic health records is a key ONC priority. This page provides data access and documentation for the non-federal acute care hospital EHR adoption and use open data. These data include measures for electronic health record (EHR) adoption, patient health information exchange, including measures of interoperable exchange, and patient engagement capabilities.",
+            "title": "Non-federal Acute Care Hospital Health IT Adoption and Use",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/aha.csv",
+                    "mediaType": "text/csv",
+                    "title": "aha.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/non-federal-acute-care-hospital-health-it-adoption-and-use"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/jrc9-essi",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-07-05",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-03",
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
+            "identifier": "325529aa-89b0-4892-913f-4515e4db1355",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-26-to-2023-07-02",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-06-26-2023-to-07-02-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-26-to-2023-07-02"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/kp49-9dp8",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-03-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-30",
+            "keyword": [
+                "business closure",
+                "business reopening",
+                "covid-19",
+                "executive order",
+                "government order",
+                "legal epidemiology",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "social distancing"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "T.J. Pierce",
+                "hasEmail": "mailto:pwc2@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/kp49-9dp8",
+            "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when bars in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data can be used to determine when bars in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly close or reopen bars found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through May 31, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
+            "title": "U.S. State and Territorial Orders Closing and Reopening Bars Issued from March 11, 2020 through May 31, 2021 by County by Day",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.beiresources.org/",
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
+                "fn": "Yao, Alison",
+                "hasEmail": "mailto:yaoal@niaid.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "1f97b8dc-27ee-4ef1-b54c-d160a7d053b6",
+            "description": "<p>BEI Resources provides reagents, tools and information for studying Category A, B, and C priority pathogens, emerging infectious disease agents, non-pathogenic microbes and other microbiological materials of relevance to the research community.</p>",
+            "title": "BEI Resource Repository",
+            "programCode": [
+                "009:028"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/hauf-e9a4",
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
+            "identifier": "https://data.cdc.gov/api/views/hauf-e9a4",
+            "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 3 - Philadelphia",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/jsqz-id25",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-03-02",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-28",
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
+            "identifier": "139ad317-b64b-4db4-b76b-3eff03fc7abd",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-21 to 2022-02-27",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://edit.data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-feb-02-21-2022-02-27-2022.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/6uy5-4d9d",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-22",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/6uy5-4d9d",
+            "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/a9xa-yrhn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
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
+            "identifier": "https://data.cdc.gov/api/views/a9xa-yrhn",
+            "description": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes data for old world hantavirus infections, such as Seoul virus infections. Prior to 2015, this condition was not nationally notifiable and data for this condition was not submitted to CDC's National Notifiable Diseases Surveillance System (NNDSS).\n\u00b6 Includes data for Andes virus infections.",
+            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://fdanj.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2019-08-22",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "api",
+                "fda",
+                "history of medicine"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/cpdk-v8cd",
+            "description": "A digital archive of the published federal notices of judgment (a summary of the final outcome of a court case) for manufacturers and products prosecuted under authority of the 1906 Pure Food and Drug Act (https://fdanj.nlm.nih.gov/)",
+            "title": "FDA Notices of Judgment Collection, 1908-1966",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/cpdk-v8cd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/cpdk-v8cd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/cpdk-v8cd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/cpdk-v8cd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Historical Curated Content"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-31",
+            "references": [
+                "https://chronicdata.cdc.gov/d/5amh-5sx3"
+            ],
+            "keyword": [
+                "adult",
+                "age",
+                "behavioral",
+                "cessation",
+                "cigarette",
+                "cigarette use",
+                "current",
+                "demographics",
+                "education",
+                "ethnicity",
+                "ever",
+                "every day",
+                "former",
+                "frequency",
+                "gender",
+                "never",
+                "office on smoking and health",
+                "osh",
+                "prevalence",
+                "quit",
+                "race",
+                "risk",
+                "smoker",
+                "smoking",
+                "smoking status",
+                "some days",
+                "state system",
+                "surveillance",
+                "survey",
+                "tobacco",
+                "tobacco use"
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
+            "identifier": "https://data.cdc.gov/api/views/fpp2-pp25",
+            "description": "1996-2010. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  BRFSS Survey Data.  The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. The data for the STATE System were extracted from the annual BRFSS surveys from participating states.  Tobacco topics included are cigarette smoking status, cigarette smoking prevalence by demographics, cigarette smoking frequency, and quit attempts.  NOTE:  these data are not to be compared with BRFSS data collected 2011 and forward, as the methodologies were changed.  Please refer to the FAQs / Methodology sections for more details.",
+            "title": "Behavioral Risk Factor Data: Tobacco Use (2010 And Prior)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Behavioral-Risk-Factor-Data-Tobacco-Use-2010-And-P/fpp2-pp25",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Survey Data"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-post-acute-care-hospice/medicare-post-acute-care-and-hospice-by-geography-provider",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-11-03",
+            "temporal": "2022-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-14",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-05/MUP_PAC_RY24_Methodology_2024_508.pdf"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "home health",
+                "hospice",
+                "hospitals & facilities",
+                "inpatient",
+                "long term care",
+                "medicare",
+                "national",
+                "original medicare",
+                "rehabilitation",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/fa8caa65-d5c3-492e-be49-835fe42c9190/data-viewer",
+            "description": "The Medicare Post-Acute Care and Hospice Provider Utilization and Payment Public Use Files (PAC PUF) contains information on demographic and clinical characteristics of beneficiaries served, professional and paraprofessional service utilization, and payment information at the provider, state, and national levels for each PAC setting (i.e. HHA, hospices, SNF, IRF, and LTCH). There are additional datasets which can be found as a downloadable report under \u2018Resources', which include information specific to the unique variables (e.g., case-mix groups) for HHAs, SNFs and IRFs.\n\nPlease note the data included may not be representative of a physician\u2019s entire practice. The data are also not intended to indicate the quality of care provided and are not risk-adjusted to account for differences in underlying severity of disease of patient populations.\u00a0\n\nMore information can be found below in the resources section.",
+            "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fa8caa65-d5c3-492e-be49-835fe42c9190/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider : 2022-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/e19ecccb-355b-479f-9fd1-2e1250822bd8/ry2024_pacpuf_main_2020_2022s.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider : 2022-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/29ee817a-da89-4743-a43e-6b8b6f11d7dc/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider : 2022-01-02"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-05/MUP_PAC_RY24_Data_Dictionary_2024_FINAL.xlsx",
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
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/nhis/teen.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2024-10-18",
+            "@type": "dcat:Dataset",
+            "temporal": "2021-2023",
+            "modified": "2024-10-18",
+            "keyword": [
+                "dhis",
+                "injury",
+                "mental health",
+                "nchs",
+                "research data center",
+                "sdoh-access-to-health-care",
+                "sdoh-crime-violence",
+                "sdoh-discrimination",
+                "sdoh-social-emotional",
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
+            "identifier": "https://data.cdc.gov/api/views/7ym9-zzt7",
+            "description": "The National Health Interview Survey (NHIS)\u2014Teen was a follow-back survey of Sample Children ages 12-17 years old (herein teen) for whom a parent completed the National Health Interview Survey (NHIS) and also provided permission for the teen to participate. NHIS\u2014Teen is a self-administered survey that teens completed themselves either on the web or paper (mailed). Recruitment for NHIS\u2014Teen occurred July 2021\u2014December 2023 during the NHIS Sample Child interview. Teens with permission received an invitation to go online and complete a questionnaire about their own health. Mailed paper questionnaires were sent to nonrespondents. Questions were included to test concordance with parent-reported responses, address time-sensitive data needs, assess public health attitudes or behaviors, and contribute to developmental work to understand differences between parent and self-reported measures of health. \n\nThe majority of NHIS\u2014Teen survey content focused on the health behaviors, social and emotional wellbeing, and healthcare experiences of teens. Detailed sociodemographic characteristics (e.g. health insurance coverage type, family income) as reported by the parent in the NHIS Sample Child interview can be linked to NHIS\u2014Teen. NHIS\u2014Teen was a pilot survey with data collection concluding in March 2024. There are currently no plans to field additional iterations.",
+            "title": "NHIS\u2014Teen Restricted Use File",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/nchs/nhis/teen.htm",
+                    "description": "The National Health Interview Survey (NHIS)\u2014Teen was a follow-back survey of Sample Children ages 12-17 years old (herein teen) for whom a parent completed the National Health Interview Survey (NHIS) and also provided permission for the teen to participate. NHIS\u2014Teen is a self-administered survey that teens completed themselves either on the web or paper (mailed). Recruitment for NHIS\u2014Teen occurred July 2021\u2014December 2023 during the NHIS Sample Child interview. Teens with permission received an invitation to go online and complete a questionnaire about their own health. Mailed paper questionnaires were sent to nonrespondents. Questions were included to test concordance with parent-reported responses, address time-sensitive data needs, assess public health attitudes or behaviors, and contribute to developmental work to understand differences between parent and self-reported measures of health.",
+                    "@type": "dcat:Distribution",
+                    "title": "NHIS\u2014Teen Restricted Use File"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2014-12-01",
+            "keyword": [
+                "american reconstruction and recovery act",
+                "arra",
+                "beacon communities program",
+                "ehr",
+                "health it",
+                "hitech",
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
+            "identifier": "5k0pnwr0-zzo9-pvru-dy7y-29vcs3fudqax",
+            "description": "The Health Information Technology for Economic and Clinical Health (HITECH) Act was passed as part of the American Recovery and Reinvestment Act (ARRA) to invest in the U.S. health IT infrastructure. The Office of the National Coordinator for Health IT (ONC) received over $2 billion of these HITECH funds, which was granted to health and community organizations across the U.S. This crosswalk provides geographic data for the service areas of two of these HITECH programs: the Health IT Regional Extension Centers (REC) Program and the Beacon Communities Program. This data can be linked to program financial and performance data to map and visualize program data. You can access the data in multiple formats below.",
+            "title": "ONC Health Information Technology for Economic and Clinical Health (HITECH) Grantee Crosswalk",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/HealthIT_Dashboard_AreaType_Crosswalk.csv",
+                    "mediaType": "text/csv",
+                    "title": "HealthIT_Dashboard_AreaType_Crosswalk.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-03",
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
+            "identifier": "https://data.cdc.gov/api/views/pakc-hru3",
+            "description": "\u2022 COVID-19 vaccination coverage and intent among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
+            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 18 Years and Older Vaccinated with Updated 2023-24 COVID-19 Vaccine",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-19",
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
+            "identifier": "https://data.cdc.gov/api/views/akmt-4qtj",
+            "description": "2006. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "title": "CDC PRAMStat Data for 2006",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2006/akmt-4qtj",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Maternal & Child Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/b6fe-yq88",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division, Chemical and Biological Monitoring Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/b6fe-yq88",
+            "description": "A method for measuring PAA vapors in air using impinger sampling and field-portable colorimetric analysis is presented. The capture efficiency of aqueous media in glass and plastic impingers was evaluated when used for PAA vapor sampling. Measurement of PAA was done using a N,N-diethyl-p-phenylenediamine (DPD) colorimetric method with a field portable spectrometer. The linearity of the DPD method was determined for PAA both in-solution and captured from vapor phase using glass or plastic impingers. The Limit of Detection (LOD) for the glass and plastic impinger (0.24 mg/m3 (0.077 mg/L) and 0.28 mg/m3 (0.091 mg/L)), respectively, and Limit of Quantitation (LOQ) (0.79 mg/m3 (0.25 mg/L) and 0.92 mg/m3 (0.30 mg/L) for the glass and plastic impingers, respectively, are below the threshold limit value (TLV) short term exposure limit (STEL) of 1.24 mg/m3 (0.4 ppm) over a 15 minute period. This impinger method allows for a low cost, easy to use, and rapid in-field measurement for occupational exposure to PAA.",
+            "title": "A Field-Portable Colorimetric Method for the Measurement of Peracetic Acid Vapors: A Comparison of Glass and Plastic Impingers",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/b6fe-yq88/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/jxgy-4c9s",
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
+            "identifier": "a8647354-7dcb-5949-9582-b40e7a985bef",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt measure_value v2.10.16 (coreset-dev0)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/measure_value.csv",
+                    "description": "CoreSEt measure_value v2.10.16 (coreset-dev0)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt measure_value v2.10.16 (coreset-dev0)"
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
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/hospital-service-area",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2015-01-01/2023-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-26",
+            "references": [
+                "https://data.cms.gov/resources/hospital-service-area-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "original medicare"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CMS EDG Data Questions - OIT",
+                "hasEmail": "mailto:CMSEDG_DataRequests_Intake@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/8708ca8b-8636-44ed-8303-724cbfaf78ad/data-viewer",
+            "description": "The Hospital Service Area data\u00a0is a summary of calendar year Medicare inpatient hospital fee-for-service and Medicare Advantage claims data. It contains number of discharges, total days of care, and total charges summarized by hospital provider number and the ZIP code of the Medicare beneficiary.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Hospital Service Area",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8708ca8b-8636-44ed-8303-724cbfaf78ad/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Hospital Service Area : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/88791b91-c9e4-448f-b961-60313b43bc40/Hospital_Service_Area_2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7f749f00-bfa9-4377-9a98-90c15cacc2f3/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/efbdf792-a370-4963-8bb6-0629214089f8/Hospital_Service_Area_2022.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/84a0a165-a570-4ffe-a230-043176c1221a/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/8c7636db-1339-4299-80e9-4c1efa80b614/Hospital_Service_Area_2021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/099b80df-be9c-4274-a974-31d4537bdc33/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/000bef33-e8b9-43bd-be62-4e029110aa8b/Hospital_Service_Area_2020.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/609f2b73-d7e0-4dd1-a8b1-f951860ad9f7/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/90262ee6-b957-4c3e-b2f0-a960b0ae0ed5/Hospital_Service_Area_2019.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2713ba99-c59e-4b25-9a3d-3661d35988da/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/fe062fa5-76e6-4cff-aa6e-e97a9eefe191/Hospital_Service_Area_2018.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/263734c7-f5fd-4df2-8436-2322c86e7191/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/401038c4-07da-42f4-b98b-a25ddab4ab5a/Hospital_Service_Area_2017.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6628dd7e-9706-4e8a-bd85-f8450308066a/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/7e1f952c-70bc-43e1-8c3b-e312f796c131/Hospital_Service_Area_2016.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c9912dd2-fac1-4929-9641-dc031422b458/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d91e8043-d137-4b3e-bac7-c13387cab29b/HSAF_2015_SUPPRESS.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Service Area : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/93a89060-c812-4955-8433-09cad35d5eb2/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Service Area : 2015-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/hospital-service-area-data-dictionary",
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
+            "landingPage": "https://healthdata.gov/d/jxyn-z54e",
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
+            "identifier": "4804ca61-bb86-564d-83ab-51fcb94f0981",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet measure_value v2.10.64 (coreset-cmsdev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-cmsdev)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet measure_value v2.10.64 (coreset-cmsdev)"
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
+            "landingPage": "https://data.cdc.gov/d/6ssd-y5qt",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-03-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-02-13",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Danielle Sharpe",
+                "hasEmail": "mailto:svi_coordinator@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/6ssd-y5qt",
+            "description": "The interactive maps are visual representations of the Social Vulnerability Index (SVI). Data were extracted from the US Census and the American Community Survey.",
+            "title": "CDC Social Vulnerability Index (SVI) Mapping Dashboard",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://svi.cdc.gov/map.html",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/jys3-jbpy",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-03-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-03-18",
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
+            "identifier": "a5c46841-e9c1-4293-bfd3-6e4948a367f2",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-11-2024-to-03-17-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-03-11-2024-to-03-17-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-11-2024-to-03-17-2024"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/life-expectancy/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2019-06-21",
+            "@type": "dcat:Dataset",
+            "temporal": "2010/2015",
+            "modified": "2022-04-01",
+            "keyword": [
+                "birth",
+                "census tract",
+                "county",
+                "life expectancy",
+                "nchs",
+                "nvss",
+                "state",
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
+            "identifier": "https://data.cdc.gov/api/views/5h56-n989",
+            "description": "This dataset includes estimates of U.S. life expectancy at birth by state and census tract for the period 2010-2015 (1). Estimates were produced for 65,662 census tracts, covering the District of Columbia (D.C.) and all states, excluding Maine and Wisconsin, representing 88.7% of all U.S. census tracts (see notes).  These estimates are the result of the collaborative project, \u201cU.S. Small-area Life Expectancy Estimates Project (USALEEP),\u201d between the National Center for Health Statistics (NCHS), the National Association for Public Health Statistics and Information Systems (NAPHSIS), and the Robert Wood Johnson Foundation (RWJF) (2).",
+            "title": "U.S. Life Expectancy at Birth by State and Census Tract - 2010-2015",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5h56-n989/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5h56-n989/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5h56-n989/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5h56-n989/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-08-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "computational biology",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jz6b-hbzb",
+            "description": "Conserved Domain Database (CDD) is a protein annotation resource that consists of a collection of well-annotated multiple sequence alignment models for ancient domains and full-length proteins.",
+            "title": "Conserved Domain Database (CDD)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml",
+                    "mediaType": "text/html",
+                    "title": "Conserved Domain Database (CCD) Homepage and Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nih.gov/pub/mmdb/cdd/",
+                    "mediaType": "text/html",
+                    "title": "Download Conserved Domain Database (CCD) Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/books/NBK25499/",
+                    "mediaType": "text/html",
+                    "title": "Access Conserved Domain Database (CCD) via E-utilities API"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm191015.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+            "identifier": "e3b58aa4-eb31-406f-a766-1a4f2da87565",
+            "description": "The Electronic Animal Drug Product Listing Directory is a directory of all animal drug products that have been listed electronically since June 1, 2009, to comply with changes enacted as part of the FDA Amendments Act of 2007.",
+            "title": "Electronic Animal Drug Product Listing Directory",
+            "programCode": [
+                "009:004"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/UCM362817.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1D"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.ncbi.nlm.nih.gov/bioproject/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-08-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-08",
+            "keyword": [
+                "api",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/25yr-g2pr",
+            "description": "The BioProject database links to data that have been or will be deposited into archival databases maintained at members of the International Nucleotide Sequence Database Consortium (INSDC, which comprises the DNA DataBank of Japan (DDBJ), the European Nucleotide Archive at European Molecular Biology Laboratory (ENA), and GenBank at the National Center for Biotechnology Information (NCBI)).",
+            "title": "BioProject",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/bioproject/",
+                    "mediaType": "text/html",
+                    "title": "BioProject Homepage and Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/bioproject/",
+                    "mediaType": "text/html",
+                    "title": "Download BioProject Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
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
+                "census tract",
+                "gis",
+                "outcomes",
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
+            "identifier": "https://data.cdc.gov/api/views/ib3w-k9rq",
+            "description": "This dataset contains model-based census tract level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census tract 2015 boundary file in a GIS system to produce maps for 27 measures at the census tract level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2020 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.hcup-us.ahrq.gov",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2022-06-07",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "references": [
+                "https://www.hcup-us.ahrq.gov/datavisualizations/HCUP_Visualization_DataTable_March2021.xlsx"
+            ],
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "inpatient trends"
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
+            "identifier": "https://healthdata.gov/api/views/k2dr-3fsc",
+            "description": "The HCUP Visualization of Inpatient Trends in COVID-19 and Other Conditions displays State-specific monthly trends in inpatient stays related to COVID-19 and other conditions, and facilitates comparisons of the number of hospital discharges, the average length of stays, and in-hospital mortality rates across patient/stay characteristics and States. This information is based on the HCUP State Inpatient Databases (SID), starting with 2018 data, plus newer annual and quarterly inpatient data, if and when available.",
+            "title": "HCUP Visualization of Inpatient Trends in COVID-19 and Other Conditions",
+            "programCode": [
+                "009:074"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.hcup-us.ahrq.gov/datavisualizations/covid-19-inpatient-trends.jsp",
+                    "mediaType": "text/html",
+                    "title": "HCUP Visualization of Inpatient Trends in COVID-19 and Other Conditions"
+                }
+            ],
+            "describedBy": "https://www.hcup-us.ahrq.gov/datavisualizations/covid-19-inpatient-trends.jsp"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ya9m-pyut",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-12-05",
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
+            "identifier": "https://data.cdc.gov/api/views/ya9m-pyut",
+            "description": "The 2011 BRFSS data reflects a change in weighting methodology (raking) and the addition of cell phone only respondents. Shifts in observed prevalence from 2010 to 2011 for BRFSS measures will likely reflect the new methods of measuring risk factors, rather than true trends in risk-factor prevalence. A break in trend lines after 2010 is used to reflect this change in methodolgy. Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements.For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm.Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
+            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 2011",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-03-24",
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
+                "united states",
+                "urbanicity",
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
+            "identifier": "https://data.cdc.gov/api/views/hkhc-f7hg",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional COVID-19 deaths by urbanicity and week. Deaths are based on the county of occurrence in the United States. Urbanicity is defined as metropolitan and non-metropolitan, based on the 2013 National Center for Health Statistics (NCHS) Urban-Rural Classification Scheme for Counties. Counties are classified as \u201cmetropolitan\u201d if they are large central metro, large fringe metro, medium metro or small metro; and \u201cnon-metropolitan\u201d if micropolitan or non-core.",
+            "title": "Provisional COVID-19 Deaths by Week and Urbanicity",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/dhcs/drug-use/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-09-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2022-08-01/2024-07-31",
+            "modified": "2024-11-25",
+            "keyword": [
+                "amphetamine",
+                "bed size",
+                "benzodiazepines",
+                "cdc",
+                "classification",
+                "cocaine",
+                "covid-19",
+                "drug overdose",
+                "electronic health records",
+                "emergency",
+                "emergency departments",
+                "federal hospitals",
+                "fentanyl",
+                "health care delivery",
+                "heroin",
+                "hospitalization",
+                "hospitals",
+                "icd-10-cm",
+                "inpatient",
+                "mental health",
+                "methadone",
+                "methylphenidate",
+                "opioid overdose",
+                "opioids",
+                "opium",
+                "patient care",
+                "substance use",
+                "tramadol"
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
+            "identifier": "https://data.cdc.gov/api/views/gypc-kpgn",
+            "description": "The National Hospital Care Survey (NHCS) collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings currently include inpatient and emergency departments (ED). From this collection, the NHCS contributes data that may inform emerging national health threats such as the current opioid public health emergency. The 2022 - 2024 NHCS are not yet fully operational so it is important to note that the data presented here are preliminary and not nationally representative.\n\nThe data are from 24 hospitals submitting inpatient and 24 hospitals submitting ED Uniform Bill (UB)-04 administrative claims from August 1, 2022\u2013July 31, 2024. Even though the data are not nationally representative, they can provide insight into the use of opioids and other overdose drugs. The NHCS data is submitted from various types of hospitals (e.g., general/acute, children\u2019s, etc.) and can show results from a variety of indicators related to drug use, such as overall drug use, comorbidities, and drug and polydrug overdose. NHCS data can also be used to report on patient conditions within the hospital over time.",
+            "title": "Drug Use Data from Selected Hospitals",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
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
+            "landingPage": "https://healthdata.gov/d/k3v5-ddgt",
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
+            "identifier": "c0b5f0c0-87d8-4a3f-b637-b114e482d329",
+            "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2025 Individual Dental",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/den-ind-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-07-08",
+            "temporal": "1980/2020",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-09",
+            "keyword": [
+                "american hospital association",
+                "community hospital beds",
+                "health us",
+                "hospital",
+                "sdoh-access-to-health-care",
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
+            "identifier": "https://data.cdc.gov/api/views/uiux-mrvg",
+            "description": "Data on community hospital beds in the United States, by state. Data are from Health, United States. SOURCE: American Hospital Association (AHA) Annual Survey of Hospitals, Hospital Statistics.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Community hospital beds, by state: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uiux-mrvg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uiux-mrvg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uiux-mrvg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uiux-mrvg/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/default.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2012-04-04",
+            "references": [
+                "http://www.accessdata.fda.gov/scripts/cder/acronyms/index.cfm"
+            ],
+            "keyword": [
+                "definitions"
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
+            "identifier": "4dc9ed1a-1287-40e5-9c14-41011aac1308",
+            "description": "The FDA Acronyms and Abbreviations database provides a quick reference to acronyms and abbreviations related to Food and Drug Administration (FDA) activities",
+            "title": "FDA Acronyms and Abbreviations",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/ucm070296.htm",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/k4gi-7y87",
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
+            "identifier": "de0dc5a3-76a0-5531-a07d-282c9404173b",
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
+            "landingPage": "https://data.cdc.gov/d/mkns-9vjv",
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
+            "identifier": "https://data.cdc.gov/api/views/mkns-9vjv",
+            "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/d3c4-tq79",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2018-06-15",
+            "@type": "dcat:Dataset",
+            "modified": "2018-11-27",
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
+            "identifier": "https://data.cdc.gov/api/views/d3c4-tq79",
+            "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2001-2005",
+            "programCode": [
+                "009:032"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/k5s7-ii8g",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-13",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-18",
+            "keyword": [
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
+            "identifier": "601a8897-1453-5282-81cd-be49d7ec7503",
+            "description": "States may rely on eligibility information from \"Express Lane\" agency programs to streamline and simplify enrollment and renewal in Medicaid and CHIP. Express Lane agencies may include Supplemental Nutrition Assistance Program (SNAP), School Lunch programs, Temporary Assistance for Needy Families, Head Start, and the Women, infant, and children's program (WIC) , among others. States can also use state income tax data to determine Medicaid and CHIP eligibility for children.",
+            "title": "Express Lane Eligibility for Medicaid and CHIP Coverage",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/express-lane-eligibility-for-medicaid-and-chip-coverage.8vcd-dnq9.csv",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-03-25",
+            "@type": "dcat:Dataset",
+            "temporal": "2015/2020",
+            "modified": "2022-04-01",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
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
+            "identifier": "https://data.cdc.gov/api/views/chcz-j2du",
+            "description": "Death counts by age and sex for years 2015-2020. Data for 2015-2019 are final. Data for 2020 are provisional.",
+            "title": "AH Deaths by Year, Sex, and Age for 2015-2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/mbsb-z5f8",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
+                "all ages",
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
+            "identifier": "https://data.cdc.gov/api/views/mbsb-z5f8",
+            "description": "NNDSS - Table II. Invasive Pneumococcal Diseases, All Ages - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years.",
+            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, All Ages",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/k65v-ain7",
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
+            "identifier": "ae4d5347-5137-5f6c-b66c-3420fa0316d8",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 1991",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData1991.csv",
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
+            "landingPage": "https://data.cdc.gov/d/ujph-mgrh",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Spokane Mining Research Division\u2014Miner Health Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ujph-mgrh",
+            "description": "The National Health Interview Survey (NHIS) is an annual cross-sectional survey that collects information on a broad range of health topics; it was developed by the National Center for Health Statistics (NCHS) and is currently administered by the U.S. Census Bureau. NHIS datasets for the years 2007\u20132018 were combined to ensure an adequate sample size to study currently working male miners. During 2007\u20132018, the NHIS included four core modules. The Family and Sample Adult core modules were used in the study. The Family core module collected health and sociodemographic information on each member of each family within the household. The Sample Adult core module collected health and industry and occupation information for the randomly chosen sample adult from each household interviewed.",
+            "title": "Health conditions among male workers in mining and other industries reliant on manual labor occupations: National Health Interview Survey, 2007\u20132018",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/ujph-mgrh/application/x-zip-compressed",
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
+            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-daily-non-nurse-staffing",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2017-01-01/2024-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-31",
+            "references": [
+                "https://data.cms.gov/resources/payroll-based-journal-methodology-0"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "skilled nursing"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nursing Home Staffing - CCSQ (PBJ Reports)",
+                "hasEmail": "mailto:nhstaffing@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/b497431a-5b57-42c0-9016-90105b51841e/data-viewer",
+            "description": "The Payroll Based Journal (PBJ) Nurse Staffing and Non-Nurse Staffing datasets provide information submitted by nursing homes including rehabilitation services on a quarterly basis. The data include the hours staff are paid to work each day, for each facility. Examples of reporting categories include Director of Nursing, Administrative Registered Nurses, Registered Nursing, Administrative Licensed Practice Nurses, Licensed Practice Nurses, Certified Nurse Aides, Certified Medication Aides, and Nurse Aides in Training. There are also other non-nurse staff categories provided in the data such as Respiratory Therapist, Occupational Therapist, and Social Worker. The datasets also include a facility\u2019s daily census calculated using the Minimum Data Set (MDS) submission.\n\nThe Payroll Based Journal (PBJ) Employee Detail Nursing Home Staffing datasets and technical information have been moved to a new location.\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Payroll Based Journal Daily Non-Nurse Staffing",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b497431a-5b57-42c0-9016-90105b51841e/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/f9a724c1-1785-494f-b34d-1b66c1a53b8c/PBJ_dailyNonnursestaffing_CY2024Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c06ad548-5cb2-4f29-8075-66efc2d195b6/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/d48c6e27-2e27-47c2-bf3c-e493a07060ee/PBJ_dailyNonnursestaffing_CY2024Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/86603f7e-6ed8-4005-a5d3-b13d2ebcf3d4/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/fd3e006f-315f-4e05-9b45-1c568dcb4bb5/PBJ_dailyNonnurseStaffing_CY2023Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/80e14392-7640-4fef-b226-309929273962/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/da7cceca-fbef-4461-8286-b8a777323344/PBJ_dailyNonnurseStaffing_CY2023Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c4e98981-5128-4aee-b175-223c743d0914/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/6548296e-1849-4968-b0e2-2a68c77288dd/PBJ_dailyNonnurseStaffing_CY2023Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e43a7c86-1ef1-411e-ba53-b3711f029d0d/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/ca6cd979-b204-4005-aed4-02c28fd134fe/PBJ_dailyNonnurseStaffing_CY2023Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/60ea3ab9-e8f7-412f-ade6-e1517569cdce/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/4ace4212-2ca4-4d4a-810f-f9ec2c48a96e/PBJ_dailyNonnursestaffing_CY2022Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/161d21ed-2f94-46da-aeb3-6bdd58d57264/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/f51658e7-a4f8-4711-ae29-98de30cfe5aa/PBJ_dailyNonnursestaffing_CY2022Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d061079d-0247-4611-acfb-39da43d13f0b/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/e32dbad4-f975-48fd-ade9-b33fa244296a/PBJ_dailyNonnursestaffing_CY2022Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a9606f6a-e021-4e7c-812a-e2fbad8963e3/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/3a3cbd82-04f9-4675-ab84-b0cad6398998/PBJ_dailyNonnursestaffing_CY2022Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4dcd0728-93e3-4f00-ade9-f458a3798cb0/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/287acfdb-6cfa-4822-8120-2ace7eeede16/PBJ_dailyNonnursestaffing_CY2021Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d805bf46-faa2-48d8-89af-1f40def16c36/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/6460c80d-40b1-4de2-98ba-a850d0a30ffa/PBJ_dailyNonnursestaffing_CY2021Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/40dbe6b5-ea42-4cbc-9e7c-79673a29beb9/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/caf942e1-3e85-49fd-a66f-dfe92b122ba7/PBJ_dailyNonnursestaffing_CY2021Q2_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5f730690-64b6-4fde-ba0d-d20d0dbdc7b1/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/pbj_daily_non-nurse_staffing_cy_2021q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/91cd6494-f576-47c6-861f-fe1f436522c9/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2021-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/pbj_daily_non-nurse_staffing_cy_2020q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5759c2e9-a132-4a6f-b544-d9f1dfa1d2d5/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/78y2-smqp.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2ab96e88-d0ea-4e53-b2ec-cd32971aa659/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/PBJ_NonNurse_Q2_2020_ca7a-55j7.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/da8a7110-b591-46d8-af39-eae3eee07623/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/3a593779-6e24-4831-a892-04bb47bf4a9a/PBJ_dailyNonnursestaffing_CY2020Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f2b3d871-c5cc-45c4-b77e-77dd2384a52e/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2020-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-10/PBJ_NonNurse_2019_Q4_aif9-utfe.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3a393de4-c907-4635-ab0d-6df2b074925c/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-10/PBJ_NonNurse_2019_Q3_5epz-i6b4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3102d802-82e2-4e98-8378-8af1adc9dd1a/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-10/PBJ_NonNurse_2019_Q2_nxdr-vqyq.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aafcfc64-b66c-48e2-a4f0-c207fb88081e/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-10/PBJ_NonNurse_2019_Q1_dp6w-452n.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d859ded6-53d8-4b65-aec5-34ee757e00d0/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2019-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-10/PBJ_NonNurse_2018_Q4_4xvm-t6kp.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6e991d59-160c-4e1d-84c4-6325cf2e4d7b/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/3518f520-9ff8-4340-8cb3-5cee41a21d08/PBJ_dailyNonnursestaffing_CY2018Q3%20%284%29.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/eec70ea6-2d4d-4bc3-8df9-14fe9a64d222/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/26f2f7a7-a24c-4206-b21a-e80cc1cea640/PBJ_dailyNonnursestaffing_CY2018Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/dddfeeba-b686-4d56-b5a1-12131d5dda9b/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/356f39a6-7527-4642-8812-bece764407ac/PBJ_dailyNonnursestaffing_CY2018Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0721c6b4-9dcd-4260-a7ce-7f285036bc9d/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2018-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/8df1a39b-714e-47b9-aa17-e23b25fb6397/PBJ_dailyNonnursestaffing_CY2017Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/71b9dc6a-3073-491f-ac67-8fac3c6b9a43/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/aa533f14-7acc-4b70-b5d0-745fb98e913d/PBJ_dailyNonnursestaffing_CY2017Q3%20%282%29.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0bf9a592-a1c6-4b63-a052-775c885e5633/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/3866a9c2-2b45-47b2-b2f3-13f159f6147f/PBJ_dailyNonnursestaffing_CY2017Q2%20%281%29.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7cf6d016-2d68-4217-8d83-0ee08dd16802/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/1e4cd29c-10e9-439b-975e-064f8fa775e9/PBJ_dailyNonnursestaffing_CY2017Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7008b7ea-6237-4596-b36b-667f4f26c58b/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-03-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-daily-non-nurse-staffing-data-dictionary",
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
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-01-16",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-01-24",
+            "keyword": [
+                "covid-19",
+                "covid-19 vaccination",
+                "immunization",
+                "nis-ccm",
+                "vaccination",
+                "vaccination coverage",
+                "vaccine confidence",
+                "vaxviews"
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
+            "identifier": "https://data.cdc.gov/api/views/s5a6-fn5p",
+            "description": "National Immunization Survey Child COVID Module (NIS-CCM): CDC is providing information on COVID-19 vaccine uptake and confidence. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
+            "title": "National Immunization Survey Child COVID Module (NIS-CCM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5a6-fn5p/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5a6-fn5p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5a6-fn5p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5a6-fn5p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "National",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Child Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/4tmr-eik2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-01-28",
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
+            "identifier": "https://data.cdc.gov/api/views/4tmr-eik2",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2014 Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/4tmr-eik2/application/vnd.ms-excel",
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
+            "landingPage": "https://learn.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-06-29",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-30",
+            "keyword": [
+                "education",
+                "training and instruction",
+                "videos"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/khy6-95gu",
+            "description": "The Learning Resources Database is a catalog of interactive tutorials, videos, online classes, finding aids, and other instructional resources on National Library of Medicine (NLM) products and services. Resources may be available for immediate use via a browser or downloadable for use in course management systems.",
+            "title": "Learning Resources Database",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/khy6-95gu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/khy6-95gu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/khy6-95gu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/khy6-95gu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Other"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/8vj7-uiam",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-05",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-05",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chemical and Biological Monitoring Branch (CBMB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8vj7-uiam",
+            "description": "Laboratory-generated environments are substantial parts of the work involved in developing and validating methods for sampling volatile organic compounds (VOCs) in workplace atmospheres. We assessed the variability of samples produced by our dynamic atmosphere generation system designed for VOC generation and sampling. The characterization of bias and variability was conducted across various atmospheres containing pure n-heptane as well as mixtures of VOCs, which were collected using coconut shell charcoal tubes. The analysis of VOCs from these charcoal tubes was evaluated to reveal the variability from multiple sources: the generation of the atmosphere, the sampling process, and the analytical procedures. This research aimed to quantify the extent of variability from these sources and to estimate the sampling variability associated with our dynamic generation system. Our findings indicated that sampling variability ranged from 2% for pure n-heptane to 12% for a component within a ten-VOC mixture. Notably, sample variability increased with lower concentration levels and in mixtures compared to single-component atmospheres. This study provides a foundational reference for future experiments focused on atmosphere sampling performance at lower concentrations and in mixed VOC environments.\n\nThe introduction above was rephrased by ChatGPT-4 (with training data up to April 2023) from the original work of: Doepke et al. (2024) Journal of Occupational and Environmental Hygiene, doi:10.1080/15459624.2024.2423749.",
+            "title": "Characterizing dynamic atmosphere generation system performance for analytical method development",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/8vj7-uiam/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "public",
+            "issued": "2015-12-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1990-01-01/2018-12-31",
+            "modified": "2022-05-09",
+            "references": [
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr51/nvsr51_12.pdf",
+                "ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/62_09/",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr63/nvsr63_04.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr62/nvsr62_09.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr64/nvsr64_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr64/nvsr64_12.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr67/nvsr67_08-508.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13-508.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-02-508.pdf"
+            ],
+            "keyword": [
+                "nchs",
+                "state teen birth trends",
+                "teen births",
+                "united states",
+                "u.s. and state trends on teen births",
+                "u.s. teen birth rate"
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
+            "identifier": "https://data.cdc.gov/api/views/y268-sna3",
+            "description": "This dataset assembles all final birth data for females aged 15\u201319, 15\u201317, and 18\u201319 for the United States and each of the 50 states.\r\n\r\nData are based on 100% of birth certificates filed in all 50 states. All the teen birth rates in this dashboard reflect the latest revisions to Census populations (i.e., the intercensal populations) and thus provide a consistent series of accurate rates for the past 25 years. The denominators of the teen birth rates for 1991\u20131999 have been revised to incorporate the results of the 2000 Census. The denominators of the teen birth rates for 2001\u20132009 have revised to incorporate the results of the 2010 Census.",
+            "title": "NCHS - U.S. and State Trends on Teen Births",
+            "isPartOf": "Teen births by state 1990 through most current data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://ephtracking.cdc.gov/DataExplorer/#/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-03-08",
+            "@type": "dcat:Dataset",
+            "temporal": "2016-2020",
+            "modified": "2024-03-08",
+            "keyword": [
+                "air pollution",
+                "air quality",
+                "asthma",
+                "environmental health",
+                "national ambient air quality standards",
+                "national environmental health tracking network",
+                "particulate matter",
+                "pm2.5"
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
+            "identifier": "https://data.cdc.gov/api/views/96sd-hxdt",
+            "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2016-2020. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information. Learn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action. By using these data, you signify your agreement to comply with the following requirements: 1. Use the data for statistical reporting and analysis only. 2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. 3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. 4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. 5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC. 6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2016 - 2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S. states",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Environmental Health & Toxicology"
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
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2006",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581",
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2006)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2006) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://ephtracking.cdc.gov/DataExplorer/#/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-09-19",
+            "@type": "dcat:Dataset",
+            "temporal": "2001-2019",
+            "modified": "2023-09-19",
+            "keyword": [
+                "air pollution",
+                "air quality",
+                "asthma",
+                "environmental health",
+                "national ambient air quality standards",
+                "national environmental health tracking network",
+                "particulate matter",
+                "pm2.5"
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
+            "identifier": "https://data.cdc.gov/api/views/dqwm-pbi7",
+            "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the county level for 2001-2019. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily County-Level PM2.5 Concentrations, 2001-2019",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S. states",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Environmental Health & Toxicology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kbtb-47jc",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2022-08-17",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2022",
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
+            "identifier": "0a973ff8-9926-49c5-91e1-ee6c9c1288e1",
+            "description": "The Service Area PUF (SA-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The SA-PUF contains issuer-level data on geographic service areas including state, county, and zip code.",
+            "title": "Service Area PUF \u2013 PY2022",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/service_area_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-07-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-15",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "city",
+                "disability",
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
+            "identifier": "https://data.cdc.gov/api/views/krqc-563j",
+            "description": "This dataset contains model-based place (incorporated and census-designated places) estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, Place Data 2023 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kdeq-n7js",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2021-12-16",
+            "@type": "dcat:Dataset",
+            "modified": "2021-12-22",
+            "keyword": [
+                "exchange puf",
+                "machine readable",
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
+            "identifier": "6044cb77-5350-4ffc-908e-5c9283da5056",
+            "description": "The Machine Readable PUF (MR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The MR-PUF contains issuer-level URL locations for machine-readable network provider and formulary information.",
+            "title": "Machine Readable PUF - PY2022",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/machine_readable_puf.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kduu-h3ai",
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
+                "hasEmail": "mailto:no-reply@data.medicaid.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "5b10a5b4-dabe-5419-99d8-043df47b8e4b",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2005",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData2005.csv",
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
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2013-11-01",
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/PostmarketSurveillance/ucm134497.htm",
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocuments/ucm268064.htm"
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
+            "identifier": "3d55fceb-5248-4475-b675-503312202d0d",
+            "description": "The 522 Postmarket Surveillance Studies Program encompasses design, tracking, oversight, and review responsibilities for studies mandated under section 522 of the Federal Food, Drug and Cosmetic Act. The program helps ensure that well-designed 522 postmarket surveillance (PS) studies are conducted effectively and efficiently and in the least burdensome manner.",
+            "title": "522 Postmarket Surveillance Studies",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss_excel.cfm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/8cyw-fici",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
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
+            "identifier": "https://data.cdc.gov/api/views/8cyw-fici",
+            "description": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/mental-health-care.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-09-23",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-08-19/2022-05-09",
+            "modified": "2023-04-14",
+            "keyword": [
+                "covid-19",
+                "mental health"
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
+            "identifier": "https://data.cdc.gov/api/views/yni7-er2q",
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
+            "title": "Mental Health Care in the Last 4 Weeks",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.xml?accessType=DOWNLOAD",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-2000",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562",
+            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 2000 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey and retained in the 2000<br />\nsurvey. Demographic data include gender, race, age, ethnicity, marital<br />\nstatus, educational level, job status, veteran status, and current<br />\nhousehold composition.This study has 1 Data Set.</p>",
+            "title": "National Household Survey on Drug Abuse (NHSDA-2000)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-2000) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/x8ni-jytx",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "junin virus",
+                "lassa virus",
+                "lujo virus",
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
+            "identifier": "https://data.cdc.gov/api/views/x8ni-jytx",
+            "description": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/uarv-cqnu",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-03-17",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "associate",
+                "host site",
+                "location",
+                "phap",
+                "program"
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
+            "identifier": "https://data.cdc.gov/api/views/uarv-cqnu",
+            "description": "The map illustrates the total number of 2013 and 2014 PHAP associates in each state and U.S. territory.",
+            "title": "2013-2014 PHAP Associates by State",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uarv-cqnu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uarv-cqnu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uarv-cqnu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/uarv-cqnu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/f3zz-zga5",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-08",
+            "temporal": "9/1/2023 - Present",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-24",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Syndromic Surveillance Program",
+                "hasEmail": "mailto:nssp@cdc.gov "
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/f3zz-zga5",
+            "description": "Respiratory illness activity is monitored using the acute respiratory illness (ARI) metric. ARI captures a broad range of diagnoses from emergency department visits for respiratory illnesses, from the common cold to severe infections like influenza, RSV and COVID-19. It captures illnesses that may not present with fever, offering a more complete picture than the previous influenza-like illness (ILI) metric.  \n\n Updated once per week on Fridays.",
+            "title": "Level of Acute Respiratory Illness (ARI) Activity by State",
+            "programCode": [
+                "009:038"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/khre-5qyk",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-12-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
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
+            "identifier": "1cec574b-9353-41cf-9c81-b7c49c482bb2",
+            "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
+            "title": "Network PUF - PY2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/network_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/3nij-2pw6",
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
+                "non-congenital",
+                "sabia virus",
+                "viral hemorrhagic fevers",
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
+            "identifier": "https://data.cdc.gov/api/views/3nij-2pw6",
+            "description": "NNDSS - TABLE 1PP. Viral hemorrhagic fevers, Sabia virus to Zika virus disease, non-congenital \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1PP. Viral hemorrhagic fevers, Sabia virus to Zika virus disease, non-congenital",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nij-2pw6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nij-2pw6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nij-2pw6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nij-2pw6/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/kia2-kqun",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-02-23",
+            "@type": "dcat:Dataset",
+            "modified": "2024-02-20",
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
+            "identifier": "0f06578a-8f49-46f9-8e42-80edf20ea395",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-12-2024-to-02-18-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-02-12-2024-to-02-18-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-12-2024-to-02-18-2024"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kizf-jt27",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-02",
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
+            "identifier": "63e60221-3cef-552a-8d1e-39baf4c2bd4b",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_measure_allStates_download",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220302_ETL_DEV_OT_SPLIT/measure_allStates_download.csv",
+                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"featAuto\", \"update_id\": \"20220302_ETL_DEV_OT_SPLIT\"}",
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
+            "landingPage": "https://data.cdc.gov/d/s5vm-cztk",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2018-07-10",
+            "@type": "dcat:Dataset",
+            "modified": "2018-11-27",
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
+                "hasEmail": "mailto:nephtrackingsupport@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/s5vm-cztk",
+            "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2001-2005",
+            "programCode": [
+                "009:032"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5vm-cztk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5vm-cztk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5vm-cztk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s5vm-cztk/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-10-26",
+            "@type": "dcat:Dataset",
+            "modified": "2023-12-04",
+            "references": [
+                "https://www.census.gov/programs-surveys/acs/data.html",
+                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
+            ],
+            "keyword": [
+                "acs",
+                "estimates",
+                "places",
+                "sdoh",
+                "zcta"
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
+            "identifier": "https://data.cdc.gov/api/views/bumh-rgsq",
+            "description": "This dataset contains ZCTA-level social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service:  https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
+            "title": "SDOH Measures for ZCTA, ACS 2017-2021",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
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
+            "identifier": "5d4b366c-07ca-4358-a783-01aa2fe59684",
+            "description": "This list includes human and pet food subject to recall in the United States since January 2009 related to peanut products distributed by Peanut Corporation of America.",
+            "title": "Peanut Product Recalls",
+            "programCode": [
+                "009:001"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "irregular"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/4wzk-pwz3",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HELD Toxicology and Molecular Biology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4wzk-pwz3",
+            "description": "Traumatic brain injury (TBI) is as a major cause of death and disability experienced by nearly 3 million people annually resulting from falls, vehicular accidents, or from being struck by or against an object. While TBIs can range in severity, the majority of injuries are considered to be mild. However, TBI of any severity has the potential to have long-lasting neurological effects including headaches, cognitive/memory impairments, mood dysfunction, and fatigue as a result of neuronal damage and neuroinflammation. The goal of the study was to evaluate the neuroinflammatory and neuronal damage outcomes associated with mild or moderate-severe TBI via the modification of an established closed-head injury model of TBI by varying the material of the projectile.  Rats that received TBI using a stainless steel projectile exhibited outcomes strongly correlated to moderate-severe TBI, such as prolonged unconsciousness, impaired neurobehavior, increased risk for hematoma and death, as well as significant neuronal degeneration and neuroinflammation throughout the cortex, hippocampus, thalamus, and cerebellum.  In contrast, rats that received TBI with an aluminum projectile exhibited characteristics more congruous with mild TBI, such as a trend for longer periods of unconscious in the absence of neurobehavioral deficits, a lack of neurodegeneration and mild neuroinflammation.  Our results indicate that different levels of behavioral, neuroinflammatory, and damage outcomes are associated with differing levels of TBI severity.",
+            "title": "A Projectile Concussive Impact Model Produces Neuroinflammation in Both Mild and Moderate-Severe Traumatic Brain Injury",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/4wzk-pwz3/application/x-zip-compressed",
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
+            "identifier": "https://data.cdc.gov/api/views/wrev-kwxu",
+            "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Patient and Cycle Characteristics dataset summarizes the types of ART services performed and the kinds of patients who received ART procedures in a specific clinic. Please note patient characteristics are presented per cycle rather than per patient. As a result, patients who had more than one ART cycle within the reporting year are represented more than once.",
+            "title": "2022 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wrev-kwxu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wrev-kwxu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wrev-kwxu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wrev-kwxu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/wrev-kwxu",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Assisted Reproductive Technology (ART)"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/km4k-2uzc",
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
+            "identifier": "10012a8e-f16e-5acd-bc7e-209cb7aa94e2",
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
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-12-16",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-08-28",
+            "keyword": [
+                "adults",
+                "covid-19 vaccination",
+                "iqvia"
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
+            "identifier": "https://data.cdc.gov/api/views/w76m-r924",
+            "description": "Weekly Cumulative Estimated Number of Updated 2023-24 COVID-19 Vaccinations Administered in Pharmacies and Physical Medical Offices, Adults 18 Years and Older, United States \n\n\u2022 Estimated number of updated COVID-19 vaccinations among adults 18 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices. \n\n\u2022 Starting in September 2023, the CDC recommended the updated 2023-2024 COVID-19 vaccine for adults ages 18 years and older.",
+            "title": "Weekly Cumulative Estimated Number of Updated 2023-24 COVID-19 Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States, Data Source(s): IQVIA Pharmacy and Physician Medical Office Claims",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w76m-r924/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w76m-r924/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w76m-r924/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w76m-r924/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States - National",
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
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2015-03-01",
+            "@type": "dcat:Dataset",
+            "temporal": "1991/2012",
+            "modified": "2023-03-27",
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/index.htm"
+            ],
+            "keyword": [
+                "genetics",
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
+                "hasEmail": "mailto:NHANESGenetics@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hdx4-e4uu",
+            "description": "DNA samples were collected in the <b>Third National Health and Nutrition Examination Survey</b> (NHANES III; 1988-1994) and in subsequent NHANES cycles (1999-2002, 2007-2008, 2009-2010, and 2011-2012). The program is a nationally representative collection of stored DNA samples and genetic data and will serve to add to the extensive amount of health, nutritional, and environmental information collected from NHANES. Resulting genetic variants are deposited into the NHANES Genetic Data Repository. These datasets are categorized as restricted data since they contain identifiable information.\n\nFor more information on the NHANES Genetic Data please visit: <a href=\"https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm\">NHANES DNA Specimens and Genetic Data Program at: https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm.</a>\nFor more information on NHANES, visit the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\">NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm.</a>",
+            "title": "National Health and Nutrition Examination Survey (NHANES) Genetic Restricted Data",
+            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Health and Nutrition Examination Survey (NHANES) Genetic Restricted Data"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "The NHANES samples were selected using a complex, stratified, multistage probability cluster sampling design.",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/vbim-akqf",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-05-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2024-21-06",
+            "modified": "2025-01-13",
+            "references": [
+                "https://github.com/CDCgov/covid_case_privacy_review/blob/master/analysis/public%2012%20utility%20summary.pdf"
+            ],
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "covid",
+                "covid19",
+                "covid-19",
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
+            "identifier": "https://data.cdc.gov/api/views/vbim-akqf",
+            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated.  \n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance public use dataset has 12 elements for all COVID-19 cases shared with CDC and includes demographics, any exposure history, disease severity indicators and outcomes, presence of any underlying medical conditions and risk behaviors, and no geographic data.\n\n<h4><b>CDC has three COVID-19 case surveillance datasets:</b></h4><ul><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">COVID-19 Case Surveillance Public Use Data with Geography</a>: Public use, patient-level dataset with clinical data (including symptoms), demographics, and county and state of residence. (19 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">COVID-19 Case Surveillance Public Use Data</a>: Public use, patient-level dataset with clinical and symptom data and demographics, with no geographic data. (12 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">COVID-19 Case Surveillance Restricted Access Detailed Data</a>: Restricted access, patient-level dataset with clinical and symptom data, demographics, and state and county of residence. Access requires a registration process and a data use agreement. (33 data elements)</li></ul>\n\nThe following apply to all three datasets:\n<ul><li>Data elements can be found on the COVID-19 case report form located at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf\">www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf</a>.</li><li>Data are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers.</li><li>Some data cells are suppressed to protect individual privacy.</li><li>The datasets will include all cases with the earliest date available in each record (date received by CDC or date related to illness/specimen collection) at least 14 days prior to the creation of the current datasets. This 14-day lag allows case reporting to be stabilized and ensures that time-dependent outcome data are accurately captured.</li><li>Datasets are updated monthly.</li><li>Datasets are created using CDC\u2019s <a href=\"https://www.cdc.gov/grants/additional-requirements/ar-25.html\">Policy on Public Health Research and Nonresearch Data Management and Access</a> and include protections designed to protect individual privacy.</li><li>For more information about data collection and reporting, please see\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html\">https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html.</a></li><li>For more information about the COVID-19 case surveillance data, please see <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\"> https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html</a><br></li></ul>\n\n<h4><b>Overview</b></h4>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and aut",
+            "title": "COVID-19 Case Surveillance Public Use Data",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vbim-akqf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vbim-akqf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vbim-akqf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vbim-akqf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "describedBy": "https://data.cdc.gov/api/views/vbim-akqf/files/0eb0e326-d1bd-42a3-a748-acc6d6663326?download=true&filename=data_dictionary_covid_cases_public.xlsx",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Case Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kp27-ns4b",
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
+            "identifier": "281a686a-e457-5570-a102-157023507ab8",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet filters v2.10.64 (coreset-prod)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
+                    "description": "CoreSet filters v2.10.64 (coreset-prod)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet filters v2.10.64 (coreset-prod)"
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
+            "landingPage": "https://healthdata.gov/d/kp7p-697u",
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
+            "identifier": "f768cec0-26a6-5a21-ba76-94e1d3387f34",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt pillar v2.10.6 (coreset-etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/pillar.csv",
+                    "description": "CoreSEt pillar v2.10.6 (coreset-etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt pillar v2.10.6 (coreset-etl-test)"
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
+            "landingPage": "https://healthdata.gov/dataset/cdc-biosense-tarrant-county-texas",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "2007-01-01T00:00:00-05:00/2007-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "chronic disease",
+                "community health",
+                "gastro-intestinal",
+                "health care access",
+                "health-related behaviors",
+                "heat related",
+                "infectious disease",
+                "injury",
+                "other",
+                "prevalence",
+                "preventive practices",
+                "surveillance",
+                "trends",
+                "upper respiratory",
+                "visualization"
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
+            "identifier": "2e3a0a06-5e2d-4cbc-8c63-0d54e10978d9",
+            "description": "<p>The Tarrant County Public Health (TCPH) and Biosense collaboration is an effort to visualize TCPH health data collected by Biosense using Google Fusion Table technology and make that visualization publicly available. The data consists of patient visits to hospital emergency departments associated with Tarrant County Public Health (TCPH)  that had the illness Gastro Intestinal, Heat Related, or Upper Respiratory divided by all emergency department visits that occurred for the same time period and in the geographic granularity for which the calculation was made.</p>",
+            "title": "CDC BioSense On-Boarding",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/nssp/biosense/onboarding.html",
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
+            "identifier": "https://data.cdc.gov/api/views/yctb-fv7w",
+            "description": "\u2022 COVID-19 vaccination coverage among children 6 months to 17 years is assessed through the National Immunization Survey providing weekly COVID-19 vaccination coverage estimates (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM) (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-ccm). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19 (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html).",
+            "title": "Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to Date with the Updated 2023-24 COVID-19 Vaccine",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National, Region, State",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Child Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kqrh-gg42",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2025-01-15",
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
+            "identifier": "b4cfe208-05cd-46a0-baef-fe0e67d2abb1",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-06-2025-to-01-12-2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-01-06-2025-to-01-12-2025.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-06-2025-to-01-12-2025"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kqx9-wkhb",
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
+            "identifier": "46ea08d0-c3cc-5ecd-b665-18e50c2854fe",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_map",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/map.csv",
+                    "description": "{\"dataset\": \"map\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-19",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-06",
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
+            "identifier": "https://data.cdc.gov/api/views/dnxe-zgxs",
+            "description": "2002.  Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "title": "CDC PRAMStat Data for 2002",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2002/dnxe-zgxs",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Maternal & Child Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/research/visible/visible_human.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "anatomy",
+                "data distribution",
+                "dataset",
+                "images",
+                "medical imaging"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ux2j-9i9a",
+            "description": "The NLM Visible Human Project\u00ae has created publicly-available complete, anatomically detailed, three-dimensional representations of a human male body and a human female body. Specifically, the VHP provides a public-domain library of cross-sectional cryosection, CT, and MRI images obtained from one male cadaver and one female cadaver. The Visible Man data set was publicly released in 1994 and the Visible Woman in 1995.\n\nhttps://www.nlm.nih.gov/research/visible/visible_human.html",
+            "title": "Visible Human Project",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Sample-Data/index.html",
+                    "description": "The Visible Human Project Sample Data contains the following sample images:\nCT scans after freezing, CT scans prior to freezing, Five slices from the Visible Female, Six slices from the Visible Male, MRI-MaleHead, MRI-MaleThorax, MRI-MaleAbdomen, MRI-MalePelvis, MRI-MaleThigh, MRI-MaleFeet.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download - Visible Human Project - Sample Data"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Male-Images/index.html",
+                    "description": "The Visible Human Male data set consists of MRI, CT, and anatomical images. Axial MRI images of the head and neck, and longitudinal sections of the rest of the body were obtained at 4mm intervals. The MRI images are 256 by 256 pixel resolution with each pixel made up of 12 bits of gray tone. The CT data consist of axial CT scans of the entire body taken at 1mm intervals at a pixel resolution of 512 by 512 with each pixel made up of 12 bits of gray tone. The approximately 7.5 megabyte axial anatomical images are 2048 pixels by 1216 pixels, with each pixel being .33mm in size, and defined by 24 bits of color. The anatomical cross-sections are at 1mm intervals to coincide with the CT images. There are 1,871 cross-sections for both CT and anatomical images. The complete male data set is approximately 15 gigabytes.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download - Visible Human Project - Male Data"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Female-Images/index.html",
+                    "description": "The Visible Human Female data set has the same characteristics as the Visible Human Male. However, the axial anatomical images were obtained at 0.33 mm intervals. Spacing in the \u201cZ\u201d dimension was reduced to 0.33mm in order to match the 0.33mm pixel sizing in the \u201cX-Y\u201d plane. As a result, developers interested in three-dimensional reconstructions are able to work with cubic voxels. There are 5,189 anatomical images in the Visible Human Female data set. The data set size is approximately 40 gigabytes.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download - Visible Human Project - Female Data"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Additional-Head-Images/index.html",
+                    "description": "Data is the head of a 72 year old male donor. The donor was preserved in formalin and the blood vessels were filled with araldite-F.  Before freezing, MRI and CAT imaging was preformed. After freezing the specimen was cryo sectioned at 0.147mm intervals and digital photographs were taken with a resolution of 1056 x 1528 pixels.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download - Visible Human Project - Additional Head Images"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Images"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/aemt-mg7g",
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
+            "identifier": "https://data.cdc.gov/api/views/aemt-mg7g",
+            "description": "<b>Note:</b> \nAfter November 1, 2024, this dataset will no longer be updated due to a transition in NHSN Hospital Respiratory Data reporting that occurred on Friday, November 1, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.\n\nDue to a recent update in voluntary NHSN Hospital Respiratory Data reporting that occurred on Wednesday, October 9, 2024, reporting levels and other data displayed on this page may fluctuate week-over-week beginning Friday, October 18, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.  Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.\u202f  \n\nThis dataset represents weekly respiratory virus-related hospitalization data and metrics aggregated to national and state/territory levels reported during two periods: 1) data for collection dates from August 1, 2020 to April 30, 2024, represent data reported by hospitals during a mandated reporting period as specified by the HHS Secretary; and 2) data for collection dates beginning May 1, 2024, represent data reported voluntarily by hospitals to CDC\u2019s National Healthcare Safety Network (NHSN). NHSN monitors national and local trends in healthcare system stress and capacity for up to approximately 6,000 hospitals in the United States. Data reported represent aggregated counts and include metrics capturing information specific to COVID-19- and influenza-related hospitalizations, hospital occupancy, and hospital capacity. Find more information about reporting to NHSN at:\u202fhttps://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.\n\n<b>Source: COVID-19 hospitalization data reported to CDC\u2019s National Healthcare Safety Network (NHSN).</b>\n<ul><li><b>Data source description (updated October 18, 2024):</b> As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or \u2018COVID-19 hospital data\u2019) are reported to HHS through CDC\u2019s National Healthcare Safety Network based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data are voluntarily reported to NHSN as of May 1, 2024 until November 1, 2024, at which time CMS will require acute care and critical access hospitals to electronically report information via NHSN about COVID-19, Influenza, and RSV, hospital bed census and capacity, and limited patient demographic information, including age. Data for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting period as specified by the HHS Secretary. Data for collection dates May 1, 2024, and onwards represent data reported voluntarily to NHSN; as such, data included represents reporting hospitals only for a given week and might not be complete or representative of all hospitals. NHSN monitors national and local trends in healthcare system stress and capacity for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Find more information about reporting to NHSN: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html. Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.\u202f </li><li><b>Data quality:</b> While CDC reviews reported data for completeness and errors and corrects those found, some reporting errors might still exist within the data. CDC and partners work with reporters to correct these errors and update the data in subse",
+            "title": "Weekly United States Hospitalization Metrics by Jurisdiction, During Mandatory Reporting Period from August 1, 2020 to April 30, 2024, and for Data Reported Voluntarily Beginning May 1, 2024, National Healthcare Safety Network (NHSN) - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
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
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-01-10",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-04-17",
+            "keyword": [
+                "nis-acm",
+                "pregnancy",
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
+            "identifier": "https://data.cdc.gov/api/views/8ame-63pc",
+            "description": "Monthly Nirsevimab Receipt and Intent Among Females Aged 18-49 Years Who Have a Baby <8 Months, Are Currently Pregnant, or Are Trying to Get Pregnant. \n\n\u2022 Using data from the National Immunization Survey-Adult COVID Module (NIS-ACM), monthly estimates of receipt and intent for baby\u2019s receipt of nirsevimab reported by females aged 18-49 years with infants under the age of 8 months, females aged 18-49 years who are currently pregnant, and females aged 18-49 years who are currently trying to get pregnant. \n\n\u2022 The NIS-ACM is an ongoing random-digit-dial cellular telephone survey of households with adults 18 years and older.",
+            "title": "Monthly Nirsevimab Receipt and Intent Among Females Aged 18-49 Years Who Have a Baby <8 Months, Are Currently Pregnant, or Are Trying to Get Pregnant, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
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
+            "landingPage": "https://smokefree.gov/",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2021-02-13",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "references": [
+                "https://smokefree.gov/about-us/smokefree"
+            ],
+            "keyword": [
+                "cancer",
+                "cessation",
+                "cigarettes",
+                "mobile",
+                "mobile health",
+                "quitting",
+                "smoking",
+                "text messaging",
+                "tobacco",
+                "tobacco control",
+                "treatments"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HealthData.Gov Team",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Cancer Institute (NCI), National Institutes of Health (NIH)"
+            },
+            "identifier": "c90f280f-7c5c-4d12-a648-a521301708c0",
+            "description": "<p>Overview: The QuitNowTXT text messaging program is designed as a resource that can be adapted to specific contexts including those outside the United States and in languages other than English. Based on evidence-based practices, this program is a smoking cessation intervention for smokers who are ready to quit smoking. Although evidence supports the use of text messaging as a platform to deliver cessation interventions, it is expected that the maximum effect of the program will be demonstrated when it is integrated into other elements of a national tobacco control strategy.  The QuitNowTXT program is designed to deliver tips, motivation, encouragement and fact-based information via unidirectional and interactive bidirectional message formats. The core of the program consists of messages sent to the user based on a scheduled quit day identified by the user. Messages are sent for up to four weeks pre-quit date and up to six weeks post quit date. Messages assessing mood, craving, and smoking status are also sent at various intervals, and the user receives messages back based on the response they have submitted. In addition, users can request assistance in dealing with craving, stress/mood, and responding to slips/relapses by texting specific key words to the QuitNow. Rotating automated messages are then returned to the user based on the keyword. Details of the program are provided below. Texting STOP to the service discontinues further texts being sent.  This option is provided every few messages as required by the United States cell phone providers.  It is not an option to remove this feature if the program is used within the US.  If a web-based registration is used, it is suggested that users provide demographic information such as age, gender, and smoking frequency (daily or almost every day, most days, only a few days a week, only on weekends, a few times a month or less) in addition to their mobile phone number and quit date. This information will be useful for assessing the reach of the program, as well as identifying possible need to develop libraries to specific groups. The use of only a mobile phone-based registration system reduces barriers for participant entry into the program but limits the collection of additional data. At bare minimum, quit date must be collected.  At sign up, participants will have the option to choose a quit date up to one month out. Text messages will start up to 14 days before their specified quit date. Users also have the option of changing their quit date at any time if desired. The program can also be modified to provide texts to users who have already quit within the last month.  One possible adaptation of the program is to include a QuitNowTXT \"light\" version. This adaptation would allow individuals who do not have unlimited text messaging capabilities but would still like to receive support to participate by controlling the number of messages they receive. In the light program, users can text any of the programmed keywords without fully opting in to the program. Program Design: The program is designed as a 14-day countdown to quit date, with subsequent six weeks of daily messages. Each day within the program is identified as either a pre-quit date (Q- # days) or a post-quit date (Q+#). If a user opts into the program fewer than 14 days before their quit date, the system will begin sending messages on that day. For example, if they opt in four days prior to their quit date, the system will send a welcome message and recognize that they are at Q-4 (or four days before their quit date), and they will receive the message that everyone else receives four days before their quit date. As the user progresses throughout the program, they will receive messages outlined in the text message library. Throughout the program, users will receive texts that cover a variety of content areas including tips, informational content, motivational messaging, and keyword responses. The frequency of messages in",
+            "title": "QuitNowTXT Text Messaging Library",
+            "programCode": [
+                "009:047"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://smokefree.gov/tools-tips/text-programs/quit-for-good/smokefreetxt",
+                    "description": "Who is this program for?\nAdults in the United States who are ready to quit smoking. This program is offered by the National Cancer Institute\u2019s Smokefree.gov.\n\n\nHow does it work?\nSign up with the form below or text QUIT to 47848.\n\nAfter you confirm your enrollment, you will receive daily text messages to support you in quitting smoking from the short code 47848 (message and data rates may apply). The program lasts for 6-8 weeks.\n\nYou can opt out at any time by texting STOP. Text HELP at any time for information on the program. ",
+                    "@type": "dcat:Distribution",
+                    "title": "SmokefreeTXT"
+                }
+            ],
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kspi-2sgr",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-01-19",
+            "@type": "dcat:Dataset",
+            "modified": "2023-12-26",
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
+            "identifier": "4a00010a-132b-4e4d-a611-543c9521280f",
+            "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
+            "title": "NADAC (National Average Drug Acquisition Cost) 2023",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost-12-27-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "NADAC (National Average Drug Acquisition Cost) 2023"
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611",
+            "description": "<p>This file includes data from the 2002 through 2013 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across all four years from 2002-2005, from 2006-2009, or from 2010-2013.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health: 4-Year R-DAS (NSDUH-2002-2005)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611",
+                    "description": "National Survey on Drug Use and Health: 4-Year R-DAS (NSDUH-2002-2005) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/cah8-bpvk",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "lujo virus",
+                "machupo virus",
+                "marburg virus",
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
+            "identifier": "https://data.cdc.gov/api/views/cah8-bpvk",
+            "description": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Lujo virus to Viral hemorrhagic fevers, Marburg virus \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents..\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Lujo virus to Viral hemorrhagic fevers, Marburg virus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/4day-mt2f",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-13",
+            "temporal": "2022-01-01/Present",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "firearm injury",
+                "homicide",
+                "mortality",
+                "nchs",
+                "suicide"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCIPC",
+                "hasEmail": "mailto:injurydashboard@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4day-mt2f",
+            "description": "This file contains death counts and death rates for drug overdose, suicide, homicide and firearm injuries by census tract of residence (additional datasets exist for other levels of geography). The data is grouped by 2 different time periods including yearly and trailing twelve months. Please see data dictionary for intents and mechanisms included in each measure. \n\n \n\nWhen there are 1-9 deaths in an area, CDC uses a Bayesian model to calculate rates. A Bayesian model is a type of statistical model often used in geographic analysis. This model can improve stability of the rates in lower population areas and protects privacy by taking into account information from neighboring areas.",
+            "title": "Mapping Injury, Overdose, and Violence - Census Tract",
+            "programCode": [
+                "009:033"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4day-mt2f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4day-mt2f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4day-mt2f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4day-mt2f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Injury & Violence"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://medpix.nlm.nih.gov/home",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "education",
+                "images",
+                "medical imaging",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vp23-ayt5",
+            "description": "MedPix is a database of patient cases integrating images and textual information. The content material is organized by disease location (organ system), pathology category, patient profiles, and by image classification and caption.  Additional information at https://medpix.nlm.nih.gov/home",
+            "title": "MedPix",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://openi.nlm.nih.gov/services#searchAPIUsingGET",
+                    "description": "MedPix can be accessed programmatically via the Open-i API.",
+                    "@type": "dcat:Distribution",
+                    "title": "API"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://openi.nlm.nih.gov/services#searchAPIUsingGET",
+                    "mediaType": "text/html",
+                    "title": "Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://cup.nlm.nih.gov/login",
+                    "description": "If you have images and interesting clinical observations you'd like to showcase in MedPix\u00ae, Open-i\u2120 or both, we would like to publish them. Please register and submit good-quality de-identified images with a brief description of the clinical course. To submit a MedPix case, please provide differential diagnoses and treatment plan based on evidence supported by references.",
+                    "@type": "dcat:Distribution",
+                    "title": "Submit Your Case Report"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Images"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kv2y-hu7s",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2021-10-25",
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
+            "identifier": "99a60727-dc56-5dc2-a72c-5b2e71078ad6",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_measure_allStates_download",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20211018_v2_ETL_DEV_OT_SPLIT/measure_allStates_download.csv",
+                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"prodAuto\", \"update_id\": \"20211018_v2_ETL_DEV_OT_SPLIT\"}",
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
+            "landingPage": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
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
+            "identifier": "99f89749-f77f-4d0f-a415-8c7b633bac1f",
+            "description": "Whereas not all recalls are announced in the media or on our Recalls press release page, all recalls montiored by FDA are included in FDA's weekly Enforcement Report once they are classified according to the level of hazard involved.",
+            "title": "Enforcement Reports",
+            "programCode": [
+                "009:008"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W"
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
+                "brfss",
+                "city",
+                "disability",
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
+            "identifier": "https://data.cdc.gov/api/views/eav7-hnsx",
+            "description": "This dataset contains model-based place (incorporated and census-designated places) estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 40 measures: 12 for health outcomes, 7 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, 3 for health status, and 7 for health-related social needs. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population data, and American Community Survey 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, Place Data 2024 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/kwct-eszz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-11-29",
+            "@type": "dcat:Dataset",
```

