# Change History for healthdata.json (Part 18)

### Changes from 761a84b to acf49f0 (Part 7/12)
**Author:** Automated

**Date:** 2025-01-31 15:36:25+00:00

**Message:** Updated data: Fri Jan 31 15:36:25 UTC 2025

```diff
+                    "downloadURL": "https://data.cdc.gov/api/views/32fd-hyzc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/32fd-hyzc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/32fd-hyzc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/32fd-hyzc",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm"
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
+            "identifier": "7138583c-afe2-4e52-843b-a0665c75714d",
+            "description": "This searchable database contains establishments (engaged in the manufacture, preparation, propagation, compounding, assembly, or processing of medical devices intended for human use and commercial distribution) and listings of medical devices in commercial distribution by both domestic and foreign manufacturers. Note: This database is updated once a week.",
+            "title": "Establishment Registration & Device Listing",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/office-based-health-care-providers-database",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2014-12-01",
+            "references": [
+                "https://www.healthit.gov/data/apps/office-based-physicians-have-demonstrated-meaningful-use-through-medicare-ehr-incentive"
+            ],
+            "keyword": [
+                "health information technology",
+                "health it",
+                "non-primary physicians",
+                "nurse practitioners",
+                "office-based physicians",
+                "physician assistants",
+                "primary care physicians",
+                "providers"
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
+            "identifier": "oerg8yyb-66a7-cry5-ljpv-0x7h9uz4xq52",
+            "description": "ONC uses the SK&amp;A Office-based Provider Database to calculate the counts of medical doctors, doctors of osteopathy, nurse practitioners, and physician assistants at the state and count level from 2011 through 2013. These counts are grouped as a total, as well as segmented by each provider type and separately as counts of primary care providers.",
+            "title": "Office-based Health Care Providers Database",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/SKA_State_County_Data_2011-2013.csv",
+                    "mediaType": "text/csv",
+                    "title": "SKA_State_County_Data_2011-2013.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/office-based-health-care-providers-database"
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
+            "identifier": "https://data.cdc.gov/api/views/7dvv-y64a",
+            "description": "2010-2011.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
+            "title": "Quitline \u2013 7-Month Follow-Up (Not Comparable Across States) \u2013 2010-2011",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-7-Month-Follow-Up-Not-Comparable-Across-S/7dvv-y64a",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Quitline"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/f4j7-krxz",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-12-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-16",
+            "keyword": [
+                "bho",
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
+            "identifier": "8e7be65b-97ba-5ecf-8394-ca8e6f63685a",
+            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Because Medicaid beneficiaries may be enrolled concurrently in more than one type of managed care program (e.g., a Comprehensive MCO and a BHO), users should not sum enrollment across all program types, since the total would count individuals more than once and, in some states, exceed the actual number of Medicaid enrollees.\t\t\t\t\t\t\t\t\r\n2. Comprehensive MCOs cover acute, primary, and specialty medical care services; they may also cover behavioral health, long-term services and supports, and other benefits in some states. Limited benefit managed care programs, including MLTSS only, BHO, Dental, Transportation, and Other cover a narrower set of services.\t\t\t\t\t\t\t\t\r\n3. The indicated territory was not able to supply data for this report. The Northern Mariana Islands reported that they have no Medicaid managed care enrollment, but they did not report total Medicaid enrollees.\r\n4. The \u201cTotal dually eligible individuals\u201d column represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including enrollees receiving full Medicaid benefits or Medicaid cost sharing.\r\n\t\t\t\t\t\r\n\"--\" indicates states that do not operate programs of a given type. 0 signifies that a state operated a program of this type in 2014, but it ended before July 1, 2014, or began after that date.",
+            "title": "Managed Care Enrollment by Program and Population (Duals)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-population-duals.2022.csv",
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
+            "landingPage": "https://data.cdc.gov/d/sumd-iwm8",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "N/A",
+            "issued": "2024-10-04",
+            "@type": "dcat:Dataset",
+            "temporal": "October 1, 2024 - no specified end date",
+            "modified": "2025-01-17",
+            "keyword": [
+                "deaths",
+                "disease burden",
+                "hospitalizations",
+                "outpatient visits",
+                "respiratory syncytial virus",
+                "rsv"
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
+            "identifier": "https://data.cdc.gov/api/views/sumd-iwm8",
+            "description": "This dataset represents preliminary estimates of cumulative U.S. RSV \u2013associated disease burden estimates for the 2024-2025 season, including outpatient visits, hospitalizations, and deaths. Real-time estimates are preliminary and based on continuously collected surveillance data from patients hospitalized with laboratory-confirmed respiratory syncytial virus (RSV) infections. The data  come from the Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET), a surveillance platform that captures data from hospitals that serve about 8% of the U.S. population. Each week CDC estimates a range (i.e., lower estimate and an upper estimate) of RSV-associated disease burden estimates that have occurred since October 1, 2024.  \n\n<b>Note:</b> Data are preliminary and subject to change as more data become available. Rates for recent RSV-associated hospital admissions are subject to reporting delays; as new data are received each week, previous rates are updated accordingly.  \n\n<b>Note:</b> Preliminary burden estimates are not inclusive of data from all RSV-NET sites. Due to model limitations, sites with small sample sizes can impact estimates in unpredictable ways and are excluded for the benefit of model stability. CDC is working to address model limitations and include data from all sites in final burden estimates.  \n\n\n<b>References</b>\n<ol><li>Reed C, Chaves SS, Daily Kirley P, et al. Estimating influenza disease burden from population-based surveillance data in the United States. PLoS One. 2015;10(3):e0118369. https://doi.org/10.1371/journal.pone.0118369\u202f </li><li>Rolfes, MA, Foppa, IM, Garg, S, et al. Annual estimates of the burden of seasonal influenza in the United States: A tool for strengthening influenza surveillance and preparedness. Influenza Other Respi Viruses. 2018; 12: 132\u2013 137. https://doi.org/10.1111/irv.12486</li><li>Tokars  JI, Rolfes  MA, Foppa  IM, Reed  C.  An evaluation and update of methods for estimating the number of influenza cases averted by vaccination in the United States.   Vaccine. 2018;36(48):7331-7337. doi:10.1016/j.vaccine.2018.10.026\u202f</li><li>Collier SA, Deng L, Adam EA, Benedict KM, Beshearse EM, Blackstock AJ, Bruce BB, Derado G, Edens C, Fullerton KE, Gargano JW, Geissler AL, Hall AJ, Havelaar AH, Hill VR, Hoekstra RM, Reddy SC, Scallan E, Stokes EK, Yoder JS, Beach MJ. Estimate of Burden and Direct Healthcare Cost of Infectious Waterborne Disease in the United States. Emerg Infect Dis. 2021 Jan;27(1):140-149. doi: 10.3201/eid2701.190676. PMID: 33350905; PMCID: PMC7774540.</li><li>Reed C, Kim IK, Singleton JA,\u202f et al. Estimated influenza illnesses and hospitalizations averted by vaccination\u2013United States, 2013-14 influenza season. MMWR Morb Mortal Wkly Rep. 2014 Dec 12;63(49):1151-4. https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6349a2.htm\u202f</li><li>Reed C, Angulo FJ, Swerdlow DL, et al. Estimates of the Prevalence of Pandemic (H1N1) 2009, United States, April\u2013July 2009. Emerg Infect Dis. 2009;15(12):2004-2007. https://dx.doi.org/10.3201/eid1512.091413 \u202f</li><li>Devine O, Pham H, Gunnels B, et al. Extrapolating Sentinel Surveillance Information to Estimate National COVID-19 Hospital Admission Rates: A Bayesian Modeling Approach. Influenza and Other Respiratory Viruses. https://onlinelibrary.wiley.com/doi/10.1111/irv.70026. Volume18, Issue10. October 2024.</li><li><a ref=\"https://www.cdc.gov/covid/php/covid-net/index.html\">COVID-NET | COVID-19 | CDC\u202f</a></li><li>https://www.cdc.gov/covid/hcp/clinical-care/systematic-review-process.html\u202f </li><li><a ref=\"https://academic.oup.com/pnasnexus/article/1/3/pgac079/6604394?login=false\">Excess natural-cause deaths in California by cause and setting: March 2020 through February 2021 | PNAS Nexus | Oxford Academic (oup.com)</a></li><li>Kruschke, J. K. 2011. Doing Bayesian data analysis: a tutorial with R and BUGS. Elsevier, Amsterdam, Section 3.3.5.</li></ol>",
+            "title": "Preliminary 2024-2025 U.S. RSV Burden Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sumd-iwm8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sumd-iwm8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sumd-iwm8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sumd-iwm8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.ncbi.nlm.nih.gov/sra",
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
+                "fn": "O&#039;Sullivan, Chris",
+                "hasEmail": "mailto:osulliva@ncbi.nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "9b502ae8-4e12-4157-9f4a-bc8de6053870",
+            "description": "<p>The Sequence Read Archive (SRA) stores raw sequencing data from the next generation of sequencing platforms including Roche 454 GS System\u00ae, Illumina Genome Analyzer\u00ae, Applied Biosystems SOLiD\u00ae System, Helicos Heliscope\u00ae, Complete Genomics\u00ae, and Pacific Biosciences SMRT\u00ae.</p>",
+            "title": "Sequence Read Archive (SRA)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/sra",
+                    "mediaType": "text/html",
+                    "title": "Sequence Read Archive (SRA)"
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
+            "landingPage": "https://www.cdc.gov/nchs/nhis/shs.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "issued": "2024-07-29",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-2023",
+            "modified": "2024-11-05",
+            "references": [
+                "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf"
+            ],
+            "keyword": [
+                "nhis",
+                "sdoh-access-to-health-care",
+                "sdoh-employment",
+                "sdoh-food-access",
+                "sdoh-food-insecurity",
+                "sdoh-higher-education",
+                "sdoh-high-school",
+                "sdoh-housing-stability",
+                "sdoh-poverty-income",
+                "sdoh-source-of-health-care",
+                "sdoh-use-of-health-care",
+                "sdoh-workplace",
+                "summary health statistics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS",
+                "hasEmail": "mailto:CDCINFO@CDC.GOV"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/pg2r-sfcx",
+            "description": "Interactive Summary Health Statistics for Adults provide annual estimates of selected health topics for adults aged 18 years and over based on final data from the National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS NHIS Adult Summary Health Statistics",
+            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pg2r-sfcx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pg2r-sfcx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pg2r-sfcx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pg2r-sfcx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "annual",
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
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-31",
+            "keyword": [
+                "gsps",
+                "gtss",
+                "osh",
+                "school personnel",
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
+            "identifier": "https://data.cdc.gov/api/views/5hns-mwci",
+            "description": "2001-2011. The GSPS was initiated in 2000 to collect information on tobacco use, knowledge and attitudes of school personnel toward tobacco, existence and effectiveness of tobacco control policies in schools, and training and materials available for implementing tobacco prevention and control interventions.",
+            "title": "Global Tobacco Surveillance System (GTSS) - Global School Personnel Survey (GSPS)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5hns-mwci/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5hns-mwci/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5hns-mwci/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5hns-mwci/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Sch/5hns-mwci",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Global Survey Data"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/i43m-djm6",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-17",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
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
+            "identifier": "https://data.cdc.gov/api/views/i43m-djm6",
+            "description": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
+            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/f77z-wtsx",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-06-01",
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
+            "identifier": "a9cfe5e9-d7d8-5b87-a7db-b45a7daf84fc",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2014",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData2014.csv",
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
+            "landingPage": "https://data.cdc.gov/d/rv55-x8ff",
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
+            "identifier": "https://data.cdc.gov/api/views/rv55-x8ff",
+            "description": "Information on radiographic evidence of coal workers\u2019 pneumoconiosis (CWP) is presented for a group of 3,194 underground bituminous coal miners and ex-miners examined between 1985 and 1988. Prevalence of CWP was related to estimated cumulative dust exposure, age, and rank of coal. On the basis of these data, miners of medium to low rank coal, who work for 40 years at the current federal dust limit of 2 mg/m3, are predicted to have a 1.4% risk of having progressive massive fibrosis on retirement. Higher prevalences are predicted for less severe categories of CWP. Miners in high rank coal areas appear to be at greater risk than those mining medium and low rank coals. Ex-miners who said that they left mining for health-related reasons had higher levels of abnormality compared to current miners.",
+            "title": "Prevalence of Pneumoconiosis and its Relationship to Dust Exposure in a Cohort of U.S. Bituminous Coal Miners and ex-Miners",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/rv55-x8ff/application/x-zip-compressed",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2001",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2001)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2001) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/association-university-centers-disabilities-aucd-network-national-information-and-reporting",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2014-06-26",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "children's health",
+                "fihet",
+                "health disparities",
+                "population statistics",
+                "social determinates of health"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Corina Miclea",
+                "hasEmail": "mailto:cmiclea@aucd.org"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "identifier": "165fd4ab-65d6-48e3-a1bb-52216d5f9660",
+            "description": "<p>A searchable, web-based tool for accessing data on AUCD training programs, projects, activities, and products.  Includes data on the University Center for Excellence in Developmental Disabilities (UCEDD) and Leadership Education in Neurodevelopmental and related Disabilities (LEND) programs.</p>",
+            "title": "The Association of University Centers on Disabilities (AUCD) Network National Information and Reporting System (NIRS)",
+            "programCode": [
+                "009:105"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-model-participants",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2025-01-05/2025-01-11",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-17",
+            "references": [
+                "https://data.cms.gov/resources/model-participants-methodology"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/44e93e18-b9b3-4650-9471-2b1b31dc588b/data-viewer",
+            "description": "The Innovation Center Model Participants dataset contains information on current CMS Innovation Center models, demonstrations, initiatives, and programs. This can include the name of the initiative, organization name, location information, address, phase of participation, social media and website URLs, Metropolitan Statistical Area, categories related to health care quality, cost, payment, and delivery, among others. Information on past participants can be found below under resources.",
+            "title": "Innovation Center Model Participants",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/44e93e18-b9b3-4650-9471-2b1b31dc588b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Innovation Center Model Participants : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/9cef2ee4-7ab0-4052-a0b8-75d95994c05f/Model_Participants_BPCIA-01-17-2025.csv",
+                    "mediaType": "text/csv",
+                    "title": "Innovation Center Model Participants : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cea81977-6fa6-44e3-876a-5116c905921c/data",
+                    "mediaType": "text/html",
+                    "title": "Innovation Center Model Participants : 2025-01-17"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/model-participants-data-dictionary",
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
+            "landingPage": "https://data.cdc.gov/d/338g-fx72",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Protective Technology Branch (PTB), Division of Safety Research (DSR)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/338g-fx72",
+            "description": "Top impacts are considered essential tests to evaluate the shock absorption performance of commonly used type I industrial helmets. Currently, there are two major test standards that are widely applied in helmet industry: ANSI/ISEA Z89.1 and EN397.  Since drop impacts are performed using different impactors and at drop heights, results obtained using different test standards are not directly comparable. The purpose of the current study is to evaluate and compare the helmet impact test results obtained using these two frequently used helmet test standards. A representative basic Type I construction helmet model was selected for the study. A total of 19 drop impact tests were performed at different drop heights and with two different impactors (3.6 kg and 5.0 kg). Group (a) contains 10 drop impacts performed using the 3.6 kg  impactor at drop heights from 0.31 m to 1.93 m. Group (b) contains 9 drop impacts performed using the 5.0 kg impactor at drop heights from 0.22 m to 1.32 m. Each of the impact trials was replicated four times. Relationships between the peak impact force and the drop height for these two test groups were analyzed and compared. When the helmets were tested with potential impact energy smaller than critical values, a consistent trend for the relationship of peak impact force as a function of the potential impact energy was obtained. Our results show that our previously proposed quantitative evaluation approach for industrial helmets\u2019 shock absorption performance can be used with either the ANSI/ISEA Z89.1 or EN395 standard to quantify industrial helmets\u2019 shock absorption performance. Furthermore, our results illustrated that the peak impact force would not be a reliable parameter to evaluate the helmets\u2019 safety margin.",
+            "title": "Testing the shock protection performance of Type I construction helmets using impactors of different masses",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/338g-fx72/application/x-zip-compressed",
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
+            "landingPage": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
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
+            "identifier": "703b0166-e4c2-4c1e-b5d7-46f5f21acb12",
+            "description": "This list includes products subject to recall in the United States since June 2009 related to products manufactured by Plainview Milk Products Cooperative.",
+            "title": "Plainview Milk Cooperative Ingredient Recall",
+            "programCode": [
+                "009:001"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "irregular"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/pending-initial-logging-and-tracking-physicians",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2023-05-21/2025-01-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-21",
+            "references": [
+                "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-methodology"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6bd6b1dd-208c-4f9c-88b8-b15fec6db548/data-viewer",
+            "description": "The Pending Initial Logging and Tracking\u00a0(L & T) Physicians dataset provides a list of pending applications that have not been processed by CMS contractors.",
+            "title": "Pending Initial Logging and Tracking Physicians",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6bd6b1dd-208c-4f9c-88b8-b15fec6db548/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/fb10c137-60ec-4328-9af5-b6fc3b55b937/PendingInitialLandTsPhysicians_20250121.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f1848255-f2d6-4e10-a269-49330b051a58/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/847c607c-9f52-4c1e-955f-e60fcdc715de/PendingInitialLandTsPhysicians_20250117.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8c432486-8c63-4bcc-84b1-0c2f06fd652a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/017d4851-1782-4a5a-ad3e-d88ad17fd474/PendingInitialLandTsPhysicians_20250113.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/075c7c2c-413e-4ca8-a5fb-45bcb5611b8f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/489ea192-6c21-4c3b-a84d-64a0d6497e78/PendingInitialLandTsPhysicians_20250109.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9621a288-4f8a-46fc-a3cc-0490380979ca/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/13a9bab1-e1bc-4998-96d2-9105749bfb53/PendingInitialLandTsPhysicians_20250106.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4bd25754-5890-46d3-af3a-cfb2744c7ed9/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/17226386-0423-415b-852e-895943e26f3b/PendingInitialLandTsPhysicians_20250102.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e16ced69-a28e-4d45-bdd1-abceea3ee484/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2025-01-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/17e30e0c-b2a3-4558-8fdd-72413f0261d2/PendingInitialLandTsPhysicians_20241230.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/890502c2-5ec3-4fc1-8c55-88470f09552c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/4c7c3e4c-a239-4b83-9873-21a7527cfd51/PendingInitialLandTsPhysicians_20241226.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1a6b2305-8922-4934-81e9-3e378f169987/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/94a021e6-b2bb-4f48-a86e-e36d4fd6f455/PendingInitialLandTsPhysicians_20241223.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/098496b6-af34-4140-9218-066c52afbce8/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/e692aa6b-c80d-4833-a2d6-345fc662e886/PendingInitialLandTsPhysicians_20241219.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c5d52e66-a695-4d19-b763-7f49ced66c33/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/495616ec-edef-41da-b299-cdb2f4caaddf/PendingInitialLandTsPhysicians_20241216.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7cf1b191-40d2-400c-ad8f-6a3af8f941d1/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/90e62e6b-20b8-4ebd-bc76-90dedec6f2b7/PendingInitialLandTsPhysicians_20241212.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e8af2e2-7183-4faa-91d5-052fad794d6e/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/0596e154-6685-4fda-b706-3cb712ccc5b4/PendingInitialLandTsPhysicians_20241209.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/92854ee4-3134-45e0-a2ab-86e9554c93f2/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/0ab1276d-f5a1-48e3-83d3-22a4e7ff7020/PendingInitialLandTsPhysicians_20241205.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e4b16cdc-264e-49e9-9f20-7eb94a71e8fc/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/971d59f3-e3da-4d4c-b1ad-ddfe3717e528/PendingInitialLandTsPhysicians_20241202.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/661c77b1-f4fa-44b9-a3c7-6ba2f9ef7666/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-12-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/93cca165-e44f-4baa-80fd-d47411e6ee70/PendingInitialLandTsPhysicians_20241129.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7ec74805-b3fa-40d0-9954-854133b5f936/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/cb480e7f-69eb-4ac9-95b0-0fc817fbb79e/PendingInitialLandTsPhysicians_20241125.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/50218736-14e7-4d8b-8603-1b387f1a4d0d/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/16c8a4d3-6147-40fc-97c5-5a81669b58b4/PendingInitialLandTsPhysicians_20241121.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aef6e89a-39e2-4cbc-9b03-453f56f3d853/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/22f1c38c-db7d-4bd9-9f13-a18e2e28d24f/PendingInitialLandTsPhysicians_20241118.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c9f2e625-acb5-40b8-a25d-f39ad01dae41/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/6c55c977-a15e-451b-89da-6608563743a2/PendingInitialLandTsPhysicians_20241114.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7f9f7449-4258-4e1b-b512-2796b026ebbe/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/46dfb68d-d19b-40f9-a0db-136d7559b726/PendingInitialLandTsPhysicians_20241112.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c0389ef0-2a81-45f3-aca3-1f05e43f4388/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/08e09f69-641d-48ab-95bc-d8406b82faa9/PendingInitialLandTsPhysicians_20241107.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9431a439-ccc2-42fd-9585-b8ff0d4c825d/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/29166ca2-c86c-4acd-b39d-faea6cc27386/PendingInitialLandTsPhysicians_20241104.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/936dd914-9f2b-4adf-ad4e-cd72a77d5f22/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/4e70813f-dcdb-443a-9bc8-194932f4c1cc/PendingInitialLandTsPhysicians_20241031.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/00b08e5f-0fc0-49f7-b3e3-340e90994e27/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/fe016887-efe1-43f4-9e81-3b4488028a0e/PendingInitialLandTsPhysicians_20241028.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/82c799d0-cd4a-4e13-a36e-5196876b6d13/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/6919a476-cf54-43f6-9fc1-6802edac5e1c/PendingInitialLandTsPhysicians_20241024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8e03b028-c341-45a1-b07a-e0bf3eeed07f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/4ae8f028-5b6a-4b3a-a4d1-39821e9dc926/PendingInitialLandTsPhysicians_20241021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f613e808-1182-49cc-8f8e-462fd0be9b36/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/9707f617-2aa2-4ffa-9739-74b7e82a38bf/PendingInitialLandTsPhysicians_20241017.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9ca7e821-f6dc-4603-bd28-6abbdc6b4866/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/63ac10ff-bfba-48fc-b840-447eb30bd3e7/PendingInitialLandTsPhysicians_20241015.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c77b3aa9-ef10-435c-a0f9-2e6555bfd365/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/09eddb5f-2668-4cc6-9218-9d86fa1bbfc7/PendingInitialLandTsPhysicians_20241010.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/dd8e643c-b69a-4a6d-a2e7-a5cbaec1e46a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/a52a39bc-5040-4380-8d68-789082b1d4da/PendingInitialLandTsPhysicians_20241007.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/addeb05c-03d6-4b75-89c4-6f9040e17be1/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/2b12b9f1-5d66-48d8-acba-66c23c418727/PendingInitialLandTsPhysicians_20241003.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1cb8a7fc-a390-4c9a-ad18-217df865df8a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/f22d0300-5595-4211-b503-988601d77f4b/PendingInitialLandTsPhysicians_20240930.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1f574fd7-63a1-4892-91dc-b82e913beb29/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/58a73794-f4dd-4dbb-a42b-2967628760fc/PendingInitialLandTsPhysicians_20240926.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5b7575e5-7762-400c-8f24-4a0bfcbb3efc/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/7a631014-9825-4caf-91f3-cad33bc6dc24/PendingInitialLandTsPhysicians_20240923.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c988ffa0-7ee3-44e9-94b7-19877f19ad9e/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/5c90dc5b-f3f8-4fcb-b3d4-4830b573b58e/PendingInitialLandTsPhysicians_20240919.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/008dd1ca-ad6c-4ac5-b532-1f2a2f83e20b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/f7eb1aef-7dbd-442a-8b2a-3af6b6e245a3/PendingInitialLandTsPhysicians_20240916.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c41e1211-5502-4d00-8096-12dd0bf4a40e/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/7438d1d7-c950-410a-9e7d-61f3faed058c/PendingInitialLandTsPhysicians_20240912.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/68120cf0-e6fc-4428-9d2e-3776bac5b7bd/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/4da760a8-762d-4c64-a377-bbb043dd2000/PendingInitialLandTsPhysicians_20240909.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/93644fea-475e-49b9-95bf-6d313bc37c31/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/8c13e7de-4559-44d5-ba7b-e6e0fccca270/PendingInitialLandTsPhysicians_20240905.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3c610b60-94ff-406e-9684-0259b67ff1c9/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/b3425b59-5598-4684-b45a-22eb4083cefe/PendingInitialLandTsPhysicians_20240903.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4aa5992d-13b8-4bb0-b92a-ebc531476b73/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-09-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/ac5b7aaf-c482-4e6f-844c-c3ecf498c999/PendingInitialLandTsPhysicians_20240829.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee78ac43-dae0-437d-a68f-80dd047ed9a6/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/5b91385d-1350-485a-a130-5ea0cf05f2ec/PendingInitialLandTsPhysicians_20240826.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7a4342a4-5030-4c38-9c9c-8256a9867073/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/6ada0074-f300-49c7-9674-2c665f59c825/PendingInitialLandTsPhysicians_20240822.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5355ddde-0f71-4284-b1df-838a9e9e9c56/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/a0c15bac-29b9-41e3-977e-84ad5a85ef62/PendingInitialLandTsPhysicians_20240819.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/236c81ea-77a3-4ce9-aff5-25c118dd65cd/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/c658d7b8-df9a-4ee7-9db6-85b9af1c5a15/PendingInitialLandTsPhysicians_20240815.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e7a736d-b2e8-4b7c-9a90-7b0666ee463d/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/06cda56a-acb0-4a5a-9b88-16bf91b309af/PendingInitialLandTsPhysicians_20240812.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/653a4d5a-3852-4721-bcc7-9904005c8906/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/378f6e0b-53fe-45e3-b11c-12e31917f507/PendingInitialLandTsPhysicians_20240808.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d81b9555-7f92-45ca-a5ef-4f89907b70f4/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/ece1de3f-9edc-4d8f-91a9-5dd571c5afb2/PendingInitialLandTsPhysicians_20240805.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c886c4b9-b570-4b42-966b-d182619ef703/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/44404d19-6f1b-4721-9efc-104ff6efb6cf/PendingInitialLandTsPhysicians_20240801.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9cde00c9-5600-4d4c-aff3-a1b3f9279317/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-08-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/e1c184e6-e4fc-42af-813f-333d7a612459/PendingInitialLandTsPhysicians_20240729.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8141f7f-8cc9-452b-a5e2-88b48af468af/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/b1076304-f08a-4cd3-a2ef-68bc35e1dea8/PendingInitialLandTsPhysicians_20240725.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/480f9b38-e472-4c1a-b3b9-b35bf14ddaff/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/c7542565-87bd-4883-9ba1-4db8680b67cf/PendingInitialLandTsPhysicians_20240722.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0219c500-dd2a-4a37-8cc7-ff816c4a7177/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/7152e3fc-8f41-4b16-af05-6681280c533b/PendingInitialLandTsPhysicians_20240718.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bf67419f-024f-45fb-a5f9-e4de02fb98c8/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/51e69131-042e-4c6c-aa45-8abe642b426a/PendingInitialLandTsPhysicians_20240715.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/36047a75-6f3d-4afe-8678-59681e91ecb7/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/2afac87f-d695-4463-9820-06d135f74b31/PendingInitialLandTsPhysicians_20240711.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ce4acf4c-73ba-4f78-98f3-e4e101182e1a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/7cb1506e-c519-49e4-9792-75e811adf00e/PendingInitialLandTsPhysicians_20240708.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3c3108d-aa72-4703-925e-41cb05c3341c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/7d447247-d3b3-41ba-a229-56283f7e9828/PendingInitialLandTsPhysicians_20240705.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2c532f03-e07b-40c2-93c9-9093d773ff05/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/c84f580e-5dc0-4e56-af09-7e536cc64cbd/PendingInitialLandTsPhysicians_20240701.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/22886d06-857b-4901-b197-239dcb9869b1/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-07-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/78fc9afc-9a5e-4658-a7f1-e24a99d01365/PendingInitialLandTsPhysicians_20240627.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/568ea272-93d5-4fc5-93a4-95fbb08f8c00/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/d148392f-a12e-464a-beb5-6e264e2d833a/PendingInitialLandTsPhysicians_20240624.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d9a007ca-420e-43ef-9923-2267b008e975/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/1c44cfe6-f212-40b0-ab1b-a565237b150d/PendingInitialLandTsPhysicians_20240620.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6b8c08d1-dc56-411b-8ada-ee9f3dcc87a4/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/7542bf30-a90b-4ceb-8047-741361dcf136/PendingInitialLandTsPhysicians_20240617.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/28b5da9f-f18d-4093-b867-710618a02e19/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/7a0fe598-c3dc-4e76-8c45-075942a0faa2/PendingInitialLandTsPhysicians_20240613.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9a4d6b64-b303-45e7-8654-6aff799396e7/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/9359a7d0-1d2e-4959-81ff-bcb30ccfd31c/PendingInitialLandTsPhysicians_20240610.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c9f3265f-a6d5-404e-b871-daffa5bf0d22/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/61c0a38e-2cd3-4219-9b63-07c555fe07cc/PendingInitialLandTsPhysicians_20240606.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8ea0d682-0600-4e8a-873d-cc58a5aae812/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/331eef49-00a2-4422-8249-b080d2e909f6/PendingInitialLandTsPhysicians_20240603.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3ba4e11a-0666-4ab2-8f68-d3481a50bd8f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-06-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/25345ba7-6456-4066-864a-5fdeda2fbbcd/PendingInitialLandTsPhysicians_20240530.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ddce660e-4775-4fa9-9fae-4b8248b59052/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/af104dca-0d96-415f-be7c-b7465d1ae556/PendingInitialLandTsPhysicians_20240528.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0fa0b977-a96b-4c55-9b29-afa2d92bc88a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/9f921542-05b7-4a73-aaa5-68a5ba1e5b59/PendingInitialLandTsPhysicians_20240523.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b656ed47-edc8-440c-8eab-34e005030e8d/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/f9b14788-7eef-4f73-bb73-01cfe0c0f400/PendingInitialLandTsPhysicians_20240520.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/95de84b0-268b-4863-b7b8-e456cd56718c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/93b805c3-5584-4f5b-a4c0-a52614851ebd/PendingInitialLandTsPhysicians_20240516.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2f205dbb-5b19-48fa-aba3-864fe62ec5d5/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/45759971-14da-43df-ac8e-c4f3958baad3/PendingInitialLandTsPhysicians_20240513.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/71ff6b23-3d04-4b58-87ca-d9dbff3e11a1/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/4bd1ec29-257c-4750-8372-bcc2a4dc928b/PendingInitialLandTsPhysicians_20240509.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/603a10e8-c200-42db-a22c-18ac2232342d/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/7bbe49a4-51eb-4620-a2ca-b715db22816b/PendingInitialLandTsPhysicians_20240506.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fe6061c9-7e74-4681-99de-1f2b1d33e4ac/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/cdd358e5-408b-4664-8f46-b1bda7dae8b6/PendingInitialLandTsPhysicians_20240502.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/68bcbb91-1a48-4c59-acf4-72df44642512/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-05-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/e0f70d7f-6c2d-4800-82aa-aa7af361194b/PendingInitialLandTsPhysicians_20240429.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/10e5fb2e-adee-42b6-b68f-ba6c3b1e77c0/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/919077d7-89c9-4aa2-97df-fd28593c0ab5/PendingInitialLandTsPhysicians_20240425.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9454a288-35e5-4e51-b7d6-65ca9205c205/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/2c02f6a4-cb8a-4888-ba31-44282c0636ac/PendingInitialLandTsPhysicians_20240422.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1e286281-9db9-4eb4-82f6-5399537903b1/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/3aa28296-528e-4e55-aa22-9e84f7208acc/PendingInitialLandTsPhysicians_20240418.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1509c354-05f4-4f93-acf9-77d1d726e0a8/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/358bab91-1803-4108-a933-b7d7b261fbe8/PendingInitialLandTsPhysicians_20240415.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c7cf9729-6d4d-4160-8fc1-a72e7c292eb5/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/7bf954c0-39a3-4b6d-92d4-80f488a017b3/PendingInitialLandTsPhysicians_20240411.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/77ea6277-c767-4169-b1cf-0d8818845d9a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/d4646a27-20e0-42a9-b6e5-c5c8558bc2a9/PendingInitialLandTsPhysicians_20240408.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6cd4da21-9e5a-460b-a273-9c4d67dc87f3/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/2a2075aa-04a7-4b66-9151-e525104d02b9/PendingInitialLandTsPhysicians_20240404.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0a54ebcb-81cf-4341-8a9f-794b403ee49a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/b4a3d63c-6576-4257-8a94-b39d4415da3d/PendingInitialLandTsPhysicians_20240401.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8ec76d6a-ff06-4d9e-8b06-247d921dbbd5/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-04-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/eba49b46-e9c1-4ea3-99d6-e9afeeb0940e/PendingInitialLandTsPhysicians_20240328.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/474e88bf-e3de-494e-ad91-c3efbf0bc7d8/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/9c1d1340-8a57-4390-985c-5e2c45cb1b78/PendingInitialLandTsPhysicians_20240325.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7eb06c0b-e161-451a-8e5f-f22563ae1d10/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f8057c0d-9b4a-4a2b-9d00-4bcb2f3d436b/PendingInitialLandTsPhysicians_20240321.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/875eda09-3381-431c-9297-706857a3800d/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/39c38e36-ab16-424c-8681-1024f2f5bd09/PendingInitialLandTsPhysicians_20240318.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c550cac3-cd24-4b66-9bb5-3dee05cb3963/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/25ab342d-1db7-443a-8556-b29610fcf24b/PendingInitialLandTsPhysicians_20240314.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7ead690f-f520-4d62-9737-d829bcf74510/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/1aa9ba7b-b08a-47af-b3c0-e5af5ec243d7/PendingInitialLandTsPhysicians_20240311.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/36f22764-e27d-484c-ae39-95398c983ee9/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/735f55b5-31fe-4f0b-a327-1b06991e18b2/PendingInitialLandTsPhysicians_20240307.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9974c85d-04d0-4aa8-9f73-4f17ffb433d5/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/621cad4b-ff78-4926-9f11-2adbcffa994f/PendingInitialLandTsPhysicians_20240304.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4be267e6-0fb2-40dc-9f0d-fd951b2198d2/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/145949d8-c29a-44d6-a331-235bae67e46f/PendingInitialLandTsPhysicians_20240229.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4b444e0c-3532-40f3-a3a0-b70e85d913ef/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/83296b15-3fd9-4bc4-bb98-48d8cfc5543f/PendingInitialLandTsPhysicians_20240226.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e0634859-bbfb-4b4e-9cae-509bddc8cfe9/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/d6ccb7a7-281b-4241-9da1-f09f0c61c1b9/PendingInitialLandTsPhysicians_20240222.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8c444507-5249-4369-8eed-397524e3ea5b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/9c7f9bd4-3a8d-4b65-9014-378fe2558e61/PendingInitialLandTsPhysicians_20240220.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/471ab8b1-c230-4fb4-a168-aa26faee6f6f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/7b476e2c-a63d-485f-9e3c-492f322fafdd/PendingInitialLandTsPhysicians_20240215.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/26ee6375-be47-49e1-9704-69898690730f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/b0cd7a79-7ce2-464b-a122-c703c36844f5/PendingInitialLandTsPhysicians_20240212.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/68cdb183-d048-41f3-8ef2-e2411d90625f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/fee35e7b-f375-40c4-b6d4-ac706bab64e4/PendingInitialLandTsPhysicians_20240208.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ad0dcc72-9cf5-4652-9f4d-38e31ba5b589/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/6e30e048-d857-40c9-8484-e60490eacfef/PendingInitialLandTsPhysicians_20240205.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aadd5de7-eedc-4659-b277-c46035dbf6d8/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/9f1381ac-15a6-44ab-baac-d47e6d14f337/PendingInitialLandTsPhysicians_20240202.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f136b3d9-eb89-43b3-aa76-6dca2f6ff3c3/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-02-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/d77c5911-a04c-442a-9761-63dc20b3e731/PendingInitialLandTsPhysicians_20240129.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8a888249-8ff2-403e-bf7b-71746bb2e168/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/777c1116-6016-4f5d-9cae-2c1837d42316/PendingInitialLandTsPhysicians_20240126.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bf95eb63-e1e8-4c15-aa87-bdfeddceeb0b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/f21a3bd6-e0b6-406d-a3d0-c31583c25226/PendingInitialLandTsPhysicians_20240122.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f34d6b5f-0ca5-4ff4-99a3-814ea9baab6f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/d4dc0f24-b15d-43dd-ba7d-367a15323e6b/PendingInitialLandTsPhysicians_20240119.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/97aed327-fb66-45e5-9265-ac2f2d2cff3b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/793ef3c7-e710-4dd7-afb9-d0a219944f15/PendingInitialLandTsPhysicians_20240115.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aa906f48-d138-4022-b22b-21bce840fec3/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/c9fd2b20-9dd7-4dda-b4d7-931f1e22b72c/PendingInitialLandTsPhysicians_20240111.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bb374999-f1d1-4727-b63b-24094206504c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/b5fa0311-5eb7-47c5-a722-c8be76c0b456/PendingInitialLandTsPhysicians_20240108.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f9c0cfee-78ed-4c4e-8b6c-e144286580ac/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/a5d46e4c-49ab-491b-bcf6-1ed36996308e/PendingInitialLandTsPhysicians_20240104.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4dd58bdf-2fa1-4673-9518-90fa09744197/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/770e47fa-cbf3-417a-a2a3-24a13812c0d5/PendingInitialLandTsPhysicians_20240102.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/84f6dea1-a3f5-429a-940b-033c65adb978/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2024-01-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/0a86c443-45f9-43a2-8434-7efab1ec7a70/PendingInitialLandTsPhysicians_20231228.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9c0307a9-83e4-4226-b866-180c3f6eec09/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/2273c000-7a5d-47ce-bf46-e3ec690b177f/PendingInitialLandTsPhysicians_20231226.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/acb02bee-7f53-4ec1-8f4a-262bb865ac7b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/9f550b04-8769-40b5-bd96-2b4ef8ad77a9/PendingInitialLandTsPhysicians_20231221.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5683542c-ee11-4f80-9e57-679dacc111ec/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/a8bc2a88-3a40-42f3-82f7-a46e2e40d689/PendingInitialLandTsPhysicians_20231218.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/32c736f7-8ddc-4989-825e-e17f7d7f3b3b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/c1e09769-b57a-40cb-8ccb-a72d60bec4b8/PendingInitialLandTsPhysicians_20231214.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/432d05f0-326f-4aad-8756-6d4fe94c5247/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/51cc8d68-4ccc-47f7-9d5e-ee7ae12dba1e/PendingInitialLandTsPhysicians_20231211.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/187ee544-68da-4ccf-bcd9-078bc81c1f2c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/91f92a93-af17-4600-89fe-aafe9ca54298/PendingInitialLandTsPhysicians_20231207.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2300e2e1-38dc-4a03-b993-9b502a3fe79c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/dfafaac2-0ccd-499d-adcd-72d555abffb7/PendingInitialLandTsPhysicians_20231204.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/736e3731-105f-448b-b004-c21bfba5518c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/9d52bd89-3b74-4f14-8d9b-f969921692fe/PendingInitialLandTsPhysicians_20231130.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/974b5435-8a37-43ae-baac-192ca1edbbaa/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/58070125-cf8b-4ad6-ab06-330a60dcba51/PendingInitialLandTsPhysicians_20231127.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ab7fb01c-5e51-4210-bb60-51bd0562f7a4/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/50f9b4f6-67a4-49cc-986d-2313b390736b/PendingInitialLandTsPhysicians_20231122.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c5d7a347-cb82-4b68-abf6-70afd34ba7ea/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/60e57f75-cefd-42de-bd88-cf0be17d07ec/PendingInitialLandTsPhysicians_20231120.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f5c8a921-fad2-4426-b595-4689c8752e03/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/6ca4d6e0-3e71-46e5-814e-9d78490c04a2/PendingInitialLandTsPhysicians_20231116.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/adbe7f57-40eb-424e-81a6-43a62262cebf/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/bd8a9790-f218-4d01-a6a1-afcfadbaf1bf/PendingInitialLandTsPhysicians_20231113.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c4cf8f72-c18a-46da-9d70-f98281d5a607/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/6c0ff54b-9aeb-4bc6-aeb8-d6e2a4d99794/PendingInitialLandTsPhysicians_20231109.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fae086d1-8ec1-43a6-b981-ffc9ce52df12/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/ae8947ed-d857-492b-a9f4-74f30d40c2c2/PendingInitialLandTsPhysicians_20231106.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8cc7f9f8-475d-428b-8d60-1297fcfe0616/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/f0fdb70f-24a7-40df-b131-89c4cdcf6c0f/PendingInitialLandTsPhysicians_20231102.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4dca697f-06ea-41c6-be1f-beb9d34ce52c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-11-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/293a38c0-2614-40a3-952e-006451f66f27/PendingInitialLandTsPhysicians_20231030.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4103f052-e182-41c2-b2e4-9440087f23e4/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/9e315434-288f-4b92-b4c4-0fa79967a838/PendingInitialLandTsPhysicians_20231026.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/897e6d28-abbf-4d81-99e8-a943dee3708c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/bafac913-b4e2-4e70-bd1f-9497b7ec8577/PendingInitialLandTsPhysicians_20231023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7ad5003d-f7c1-4dfe-be7f-6b54789dbfac/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/eb1a5d1c-9b10-4ad6-b3c4-b25c19b99d8e/PendingInitialLandTsPhysicians_20231019.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d99e288b-0f66-4cb5-8e3d-3e5201e067a3/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/0b4ccfe6-92fd-4d69-a21b-89e147dff752/PendingInitialLandTsPhysicians_20231016.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1295b87a-c3e1-469e-85c6-56a15f380a63/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/e7b48887-8e60-4ba8-8e26-a42b53d6cbae/PendingInitialLandTsPhysicians_20231012.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/14d39d94-03a2-4acd-a094-a5a8b1086502/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/f1685dcb-312e-43fe-afb6-31338d0760da/PendingInitialLandTsPhysicians_20231010.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7f529622-2eb0-47c3-9e8a-9589cb2cc643/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/ea525a29-f919-441c-a291-527611ffb651/PendingInitialLandTsPhysicians_20231005.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6aefaf4e-e79d-478d-9814-86ebe0487731/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/df2d66a3-128c-4f8d-8779-fadb5c0c0820/PendingInitialLandTsPhysicians_20231002.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/afe4f827-93d5-47e7-83d7-509adf717ab2/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-10-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/66a8f047-d441-4ccf-a7cc-a66802ce9dc7/PendingInitialLandTsPhysicians_20230928.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a72b32a8-26a9-4e6f-8687-9a73382b23d0/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/3b9c69df-5556-4eab-aeaf-7d4481d1eae6/PendingInitialLandTsPhysicians_20230925.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/14f9e6a8-4e37-4578-81af-abacd82b8997/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/ea460adb-46a3-4cea-8276-c95406aa8408/PendingInitialLandTsPhysicians_20230922.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/faf57b7f-2fbe-435f-9001-e42e773173e5/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/4743dcd7-3784-48c9-8291-5ed247cfac6d/PendingInitialLandTsPhysicians_20230918.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0ad3d32b-4e90-45a7-abae-c1e2be829a5a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/5c38bef7-a933-405f-ba77-f820007f5485/PendingInitialLandTsPhysicians_20230914.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/398bad37-e71c-408f-99df-d6d5af5fa7fc/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/57ccf451-b9f1-4f0f-857d-0183ae534dbd/PendingInitialLandTsPhysicians_20230911.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/04cf4265-8359-4f89-abe9-4a1d947ce3fd/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/d7ef80bd-b076-484b-990e-9707b8110267/PendingInitialLandTsPhysicians_20230907.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8ce2d1f-c089-4ba0-acf5-25737cbe308a/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/f9e75d06-13b0-41d8-9578-41689c27b2be/PendingInitialLandTsPhysicians_20230905.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3bd78965-26d9-492f-9cdb-8ea365f3b34b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/d19666de-f1f1-4042-87a4-a79151f1aa8c/PendingInitialLandTsPhysicians_20230831.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1da7a5e0-d94c-479d-a079-c15d69813930/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/b28a90e9-719b-40a7-9e31-000e2764f75c/PendingInitialLandTsPhysicians_20230828.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/721269c0-c61e-4928-804a-37e948db436f/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/53815ada-96c3-4331-884d-9a201c8bead8/PendingInitialLandTsPhysicians_20230824.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3d366375-9d94-4a98-a99a-52ecae532204/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/4c646a81-3e61-4e99-8a62-6bc2befd01d7/PendingInitialLandTsPhysicians_20230821.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/75ac5f20-446e-4156-89ff-86332b8affff/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/4d4130e6-97e5-42f7-b445-623e78714805/PendingInitialLandTsPhysicians_20230817.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/81527852-821c-4018-801d-fdebda6d54f5/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/f111f70c-aebe-40f3-9973-31dac45bdab0/PendingInitialLandTsPhysicians_20230814.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e5825116-2cb5-4b2b-9016-061877f138d0/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/43402219-6bcf-4ecf-9769-5289e8147983/PendingInitialLandTsPhysicians_20230810.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1ff9221e-dcad-402e-8fb6-57f4797b817e/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/1236cb9e-49e9-46ad-82f1-b368867becc6/PendingInitialLandTsPhysicians_20230807.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3d6f460-660e-4900-a10e-022c2905a2ee/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/c9a70a61-7c1f-4b74-a71c-12e1e7699c0d/PendingInitialLandTsPhysicians_20230803.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cbbed65c-ef7a-47b5-a833-40dda91592cb/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8878374b-4edd-4fb0-ae4d-b08079d3a161/PendingInitialLandTsPhysicians_20230731.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/81af36dd-a474-473c-b176-1b6ad01f1245/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/7e69ee2a-6b80-4052-9fcd-16268723c640/PendingInitialLandTsPhysicians_20230727.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9478ac58-78ea-4b40-a3bc-be296a787dcf/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/331bd12a-5843-4c23-aa8f-8d2d6efb6c93/PendingInitialLandTsPhysicians_20230724.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f75383f8-29a0-460f-b936-daaebdb15f25/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/e838df4f-f5ab-4150-b691-ba548e0389c4/PendingInitialLandTsPhysicians_20230720.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3a893cc-45a2-4b65-9051-a9af53423994/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/0b816015-808b-4f7d-a60c-723e5422485e/PendingInitialLandTsPhysicians_20230718.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e098c1e2-a0cb-4f73-9bfe-84f05ec25c64/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/13437c29-0e5c-4818-8916-5f46dc1e4b1c/PendingInitialLandTsPhysicians_20230713.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/37fba918-b475-4ec4-9177-7c25185b0015/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/22f00b6f-18a5-413b-96ea-ab524fc1f7c1/PendingInitialLandTsPhysicians_20230710.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/def28f7c-9636-4aa1-96fa-0f78efb906d4/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/3d3e67a7-1fe9-41b6-849d-b4f56285bbf3/PendingInitialLandTsPhysicians_20230706.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bdc9734c-bfd3-433e-9116-ed60357c82d5/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/e81065a9-a057-4761-8736-5467b38d06f7/PendingInitialLandTsPhysicians_20230703.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/658e91c1-8218-4d31-ac24-042c06202d5d/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/6834603d-29ef-464a-ae08-804cdc9d09b1/PendingInitialLandTsPhysicians_20230629.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cacab648-6941-443f-b1af-02e9a4acc476/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-07-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/a54a6b42-744f-42d1-9015-b425842b29e0/PendingInitialLandTsPhysicians_20230626.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6c8e9e0b-32c2-4d31-bffd-91345f90278c/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/9765803f-3a26-4e7a-9d35-56c98f8355bb/PendingInitialLandTsPhysicians_20230622.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ac7176fb-13c6-44cd-8610-4fa42d6575af/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/4f7cce5c-83eb-4a71-8ee4-6452c9fdf9ea/PendingInitialLandTsPhysicians_20230619.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/802ad7f7-c5ca-4ca0-915c-dd7b039a038b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/d98bf84f-aeba-4f17-ac11-91c13fe77c85/PendingInitialLandTsPhysicians_20230615.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b4f87204-ecba-4399-91a7-1651ed6480d3/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/d977670d-b02b-4147-ac77-b63033a68919/PendingInitialLandTsPhysicians_20230612.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4e766ee5-6598-47c6-a88d-6d08583e8137/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/56deab7c-2320-49f0-9336-357c2383bbd2/PendingInitialLandTsPhysicians_20230608.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1b83e4e9-9ec3-462c-ad1d-b414b17233cf/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/c1370b15-22af-4d3b-bea9-2b80315af978/PendingInitialLandTsPhysicians_20230605.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3dba6e32-669c-4f57-9e89-df2143c02219/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/4abaa86d-2dba-413c-9b3a-ad490748e286/PendingInitialLandTsPhysicians_20230601.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d2d588ab-017d-443b-88a6-39fb45f4239b/data",
+                    "mediaType": "text/html",
+                    "title": "Pending Initial Logging and Tracking Physicians : 2023-06-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-data-dictionary",
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
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/rdc/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-05-31",
+            "@type": "dcat:Dataset",
+            "temporal": "2010-2017",
+            "modified": "2023-03-27",
+            "references": [
+                "https://www.cdc.gov/rdc/b1datatype/dt1229.html"
+            ],
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "drug poisoning",
+                "injury",
+                "research-data-center"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Arialdi Minino Domenech",
+                "hasEmail": "mailto:aminino@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/px5t-5gtx",
+            "description": "The Drug-Involved Mortality (DIM) data are an enhancement to the National Vital Statistics System, Mortality data providing information on substances, as well as prescription (using generic names only \u2013 no trademarks) and illicit drugs mentioned on death certificates of residents of the United States and the District of Columbia. Data files were created by examining the literal text of three fields on the death certificate:  Part I-Cause of Death, Part II \u2013Significant Conditions Contributing to Death and Box 43, a verbatim description of how the injury occurred. The DIM data system does not support individual examination of \u201cliteral text\u201d and the actual variables showing free-form text are not included in these files.",
+            "title": "Drug-Involved Mortality (DIM) data available through the Research Data Center (RDC)",
+            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "description": "The Drug-Involved Mortality (DIM) data are an enhancement to the National Vital Statistics System, Mortality data providing information on substances, as well as prescription (using generic names only \u2013 no trademarks) and illicit drugs mentioned on death certificates of residents of the United States and the District of Columbia. Data files were created by examining the literal text of three fields on the death certificate:  Part I-Cause of Death, Part II \u2013Significant Conditions Contributing to Death and Box 43, a verbatim description of how the injury occurred. The DIM data system does not support individual examination of \u201cliteral text\u201d and the actual variables showing free-form text are not included in these files.",
+                    "@type": "dcat:Distribution",
+                    "title": "Drug-Involved Mortality (DIM) data available through the Research Data Center (RDC)"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "Information derived from the textual entries in key data fields from death certificates issued by jurisdictions in the U.S.",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/faqw-p9fj",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-13",
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
+            "identifier": "4b1d87f3-f0dc-4e21-98c0-9c9d98724f1c",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-06-to-2023-03-12",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-3-6-2023-to-3-12-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-06-to-2023-03-12"
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
+            "issued": "2022-04-28",
+            "@type": "dcat:Dataset",
+            "temporal": "1997-01-01/2018-12-31",
+            "modified": "2023-08-29",
+            "keyword": [
+                "african americans",
+                "age",
+                "alaskan natives",
+                "american natives",
+                "asian continental ancestry group",
+                "continental population groups",
+                "dental care",
+                "european continental ancestry group",
+                "health insurance",
+                "health us",
+                "hispanic americans",
+                "medicaid",
+                "medically uninsured",
+                "oceanic ancestry group",
+                "poverty",
+                "prescription drugs",
+                "prescriptions",
+                "schools",
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
+            "identifier": "https://data.cdc.gov/api/views/dmzy-x2ad",
+            "description": "Data on delay or nonreceipt of needed medical care, nonreceipt of needed prescription drugs, or nonreceipt of needed dental care during the past 12 months due to cost by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health Interview Survey, Family Core, Sample Child, and Sample Adult questionnaires. Data for level of difficulty are from the 2010 Quality of Life, 2011-2017 Functioning and Disability, and 2018 Sample Adult questionnaires. For more information on the National Health Interview Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
+            "title": "Delay or nonreceipt of needed medical care, prescription drugs, or dental care during the past 12 months due to cost: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/fats-pywh",
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
+            "identifier": "3380bed6-24ce-568e-982c-99951e1d7db0",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_files_topicSnapshot",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
+                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
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
+            "landingPage": "https://data.cdc.gov/d/xssa-9qw5",
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
+                "rubella",
+                "rubella congenital syndrome",
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
+            "identifier": "https://data.cdc.gov/api/views/xssa-9qw5",
+            "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/fc8e-phkt",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-03-09",
+            "@type": "dcat:Dataset",
+            "modified": "2024-03-04",
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
+            "identifier": "b5ce96db-36b4-4f1e-8db8-6fe88322360f",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-26-2024-to-03-03-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-02-26-2024-to-03-03-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-26-2024-to-03-03-2024"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/nnhs/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2024-01-16",
+            "@type": "dcat:Dataset",
+            "temporal": "2004-08-01/2004-12-31",
+            "modified": "2024-03-25",
+            "keyword": [
+                "long-term care",
+                "national nursing home survey",
+                "nursing home residents",
+                "nursing home staff",
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
+            "identifier": "https://data.cdc.gov/api/views/7ssk-h5k2",
+            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system and included a supplemental survey of nursing assistants employed by nursing homes, the National Nursing Assistant Survey (NNAS), which was sponsored by the Office of the Assistant Secretary for Planning and Evaluation (APSE). \n\nThe National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174 and the total number of nursing assistants that participated in the National Nursing Assistant Survey is 3,017.",
+            "title": "2004 National Nursing Home Survey - Restricted Facility Dataset",
+            "isPartOf": "https://www.cdc.gov/nchs/nnhs/nnhs_questionnaires.htm",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "2004 National Nursing Home Survey - Restricted Facility Dataset"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "None",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genome/viruses/retroviruses/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "dataset",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/37e3-hz3p",
+            "description": "Information about retroviruses and specialized tools for the analysis of retroviral proteins and genomes. The tools on this page aid in the identification, study and analysis of retroviral genomes and proteins. For instance, the HIV, human interaction database catalogs and organizes published data in peer-reviewed journals regarding HIV-1 and human protein interactions. Several links external to NCBI are also included  for the purposes of education, research and health-related matters. These include links to the CDC, the Retroviruses textbook and other informative sites.",
+            "title": "Retrovirus Resources",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genome/viruses/retroviruses/hiv-1/interactions/",
+                    "description": "Information about known interactions of HIV-1 proteins with proteins from human hosts. It provides annotated bibliographies of published reports of protein interactions, with links to the corresponding PubMed records and sequence data.",
+                    "@type": "dcat:Distribution",
+                    "title": "HIV-1 Human Interaction Database"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/projects/genotyping/formpage.cgi",
+                    "description": "This tool helps identify the genotype of a viral sequence. A window is slid along the query sequence and each window is compared by BLAST to each of the reference sequences for a particular virus. This approach is especially useful for the analysis of recombinant sequences",
+                    "@type": "dcat:Distribution",
+                    "title": "Retrovirus genotyping tool"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://blast.ncbi.nlm.nih.gov/Blast.cgi?ALIGNMENTS=50&ALIGNMENT_VIEW=Pairwise&AUTO_FORMAT=Semiauto&CLIENT=web&DATABASE=nr&DESCRIPTIONS=250&EQ_MENU=All+organisms&EQ_OP=AND&EQ_TEXT=txid11632%5Borgn%5D&EXPECT=10&FILTER=L&FORMAT_BLOCK_ON_RESPAGE=None&FORMAT_EQ_MENU=All+organisms&FORMAT_EQ_OP=AND&FORMAT_OBJECT=Alignment&FORMAT_TYPE=HTML&GET_SEQUENCE=on&HITLIST_SIZE=250&LAYOUT=TwoWindows&MASK_CHAR=2&MASK_COLOR=1&MYNCBI_USER=4345656082&NEW_VIEW=on&NUM_OVERVIEW=100&PAGE=Nucleotides&PROGRAM=blastn&REPEATS=repeat_9606&SEARCH_NAME=bn&SERVICE=plain&SET_DEFAULTS=Yes&SET_DEFAULTS.x=31&SET_DEFAULTS.y=11&SHOW_LINKOUT=on&SHOW_OVERVIEW=on&USER_TYPE=2&WORD_SIZE=11&dbtype=hc&END_OF_HTTPGET=Yes",
+                    "mediaType": "text/html",
+                    "title": "Retrovirus nucleotide Blast"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://blast.ncbi.nlm.nih.gov/Blast.cgi?ALIGNMENTS=250&ALIGNMENT_VIEW=Pairwise&AUTO_FORMAT=Semiauto&CDD_SEARCH=on&CLIENT=web&COMPOSITION_BASED_STATISTICS=1&DATABASE=nr&DESCRIPTIONS=500&EQ_MENU=All+organisms&EQ_OP=AND&EQ_TEXT=txid11632%5Borgn%5D&EXPECT=10&FORMAT_BLOCK_ON_RESPAGE=None&FORMAT_EQ_MENU=All+organisms&FORMAT_EQ_OP=AND&FORMAT_OBJECT=Alignment&FORMAT_TYPE=HTML&GAPCOSTS=11+1&GET_SEQUENCE=on&HITLIST_SIZE=500&I_THRESH=0.005&LAYOUT=TwoWindows&MASK_CHAR=2&MASK_COLOR=1&MATRIX_NAME=BLOSUM62&MYNCBI_USER=4345656082&NCBI_GI=on&NUM_OVERVIEW=100&PAGE=Proteins&PROGRAM=blastp&SEARCH_NAME=bp&SERVICE=plain&SET_DEFAULTS=Yes&SET_DEFAULTS.x=36&SET_DEFAULTS.y=10&SHOW_LINKOUT=on&SHOW_OVERVIEW=on&USER_TYPE=2&WORD_SIZE=3&END_OF_HTTPGET=Yes",
+                    "mediaType": "text/html",
+                    "title": "Retrovirus protein Blast"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genomes/GenomesGroup.cgi?taxid=11632",
+                    "mediaType": "text/html",
+                    "title": "Reference retrovirus genomes"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genome/?term=retroviridae",
+                    "mediaType": "text/html",
+                    "title": "Browse retrovirus genomes by species"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=11632&keep=1&lvl=6&filter=genome_filter&p=genome",
+                    "mediaType": "text/html",
+                    "title": "Retrovirus taxonomy browser"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/fcvk-9npu",
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
+            "identifier": "c57ee71b-bbf2-5406-aef4-3ac15f0554ce",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet measure v2.10.64 (coreset-dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
+                    "description": "CoreSet measure v2.10.64 (coreset-dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet measure v2.10.64 (coreset-dev)"
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
+            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "keyword": [
+                "high school",
+                "risk behavior",
+                "sexual contacts",
+                "sexual identity",
+                "sexual orientation",
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
+            "identifier": "https://data.cdc.gov/api/views/q6p7-56au",
+            "description": "2015-2017. High School Dataset \u2013 Including Sexual Orientation. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors\r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and\r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human\r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors\r\nthe prevalence of obesity and asthma and other priority health behaviors.  This dataset contains national, state, and local data from 2015 that includes two aspects of sexual orientation \u2013 sexual identity and sex of sexual contacts.  Additional information about the YRBSS can be found at www.cdc.gov/yrbss.",
+            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School \u2013  Including Sexual Orientation",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/q6p7-56au",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Youth Risk Behaviors"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/372p-dx3h",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2018-07-25",
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
+            "identifier": "https://data.cdc.gov/api/views/372p-dx3h",
+            "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2011-2014. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.",
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2011-2014",
+            "programCode": [
+                "009:032"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/372p-dx3h/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/372p-dx3h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/372p-dx3h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/372p-dx3h/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/y4ut-ybj7",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "confirmed",
+                "hepatitis b",
+                "hepatitis c acute",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
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
+            "identifier": "https://data.cdc.gov/api/views/y4ut-ybj7",
+            "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-05-08",
+            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-06",
+            "keyword": [
+                "100 diagnosis-related groups  drg",
+                "cms",
+                "health care providers",
+                "hospital referral region  hrr",
+                "inpatient",
+                "ipps",
+                "medicare",
+                "state"
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
+            "identifier": "bed9c757-f144-49eb-95ef-f8e01224a1ee",
+            "description": "<p>A provider level summary of Inpatient Prospective Payment System (IPPS) discharges, average charges and average Medicare payments for the Top 100 Diagnosis-Related Groups (DRG)</p>",
+            "title": "Inpatient Prospective Payment System (IPPS) Provider Summary for the Top 100 Diagnosis-Related Groups (DRG)",
+            "programCode": [
+                "009:078"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data",
+                    "mediaType": "application/json",
+                    "title": "API "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service/data",
+                    "mediaType": "text/html",
+                    "title": "CSV "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Community"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "temporal": "2002-11-01/2013-11-01",
+            "@type": "dcat:Dataset",
+            "modified": "2013-11-01",
+            "references": [
+                "http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm329946.htm"
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
+            "identifier": "5291f6b2-f62a-4498-a640-0639d94ec3c6",
+            "description": "This database contains a list of classified medical device recalls since November 1, 2002",
+            "title": "Recalls of Medical Devices",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-online-tuberculosis-information-system-otis-0",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1993-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "age",
+                "alcohol use",
+                "case",
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
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "identifier": "e68f8a49-eae3-41b8-8b03-0f02d0167fcf",
+            "description": "<p>The Online Tuberculosis Information System (OTIS) on CDC WONDER contains information on verified tuberculosis (TB) cases reported to the Centers for Disease Control and Prevention (CDC) by state health departments, the District of Columbia and Puerto Rico since 1993.  These data were extracted from the CDC national TB surveillance system.  OTIS reports case counts, incidence rates, population counts, percentage of cases that completed therapy within 1 year of diagnosis, and percentage of cases tested for drug susceptibility.  Data for 22 variables are included in the data set, including:  age groups, race / ethnicity, sex, vital status, year reported, state, metropolitan area, several patient risk factors, directly observed therapy, disease verification criteria and multi-drug resistant TB.   Each year these data are updated with an additional year of cases plus revisions to cases reported in previous years.   OTIS is produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
+            "title": "CDC WONDER: Online Tuberculosis Information System (OTIS)",
+            "programCode": [
+                "009:053"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/tb.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
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
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/85gd-bw4a",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/85gd-bw4a",
+            "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Update (All Fields) Report lists each individual modification made to a Descriptor or Supplementary Concept Record (SCR).  More than one field on a term can be modified during YEP, resulting in a term having multiple entries on the list.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
+            "title": "MeSH 2025 Update - Update All Fields Report",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/85gd-bw4a/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/85gd-bw4a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/85gd-bw4a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/85gd-bw4a/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-30",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-30",
+            "references": [
+                "https://www.cdc.gov/nccdphp/dnpao/index.html"
+            ],
+            "keyword": [
+                "adults",
+                "brfss",
+                "dnpao",
+                "fruit",
+                "nutrition",
+                "obesity",
+                "overweight",
+                "physical activity",
+                "vegetables",
+                "walking"
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
+            "identifier": "https://data.cdc.gov/api/views/hn4x-zwk7",
+            "description": "This dataset includes data on adult's diet, physical activity, and weight status from Behavioral Risk Factor Surveillance System. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding.",
+            "title": "Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Nutrition",
+                "Physical Activity",
+                "and Obesity"
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
+            "modified": "2024-05-13",
+            "references": [
+                "https://chronicdata.cdc.gov/d/sgg4-hiwe"
+            ],
+            "keyword": [
+                "office on smoking and health",
+                "osh",
+                "policy",
+                "state system",
+                "tobacco",
+                "tobacco settlement payments"
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
+            "identifier": "https://data.cdc.gov/api/views/ffbi-is3j",
+            "description": "1999-2024. National Association of Attorneys General (NAAG). Policy\u2014Tobacco Settlement Payments. The National Association of Attorneys General (NAAG) provides Tobacco Settlement Revenue data for 46 states participating in the Master Settlement Agreement (MSA) with the four largest tobacco companies in the United States.  Data are reported on an annual basis.  Four states (Florida, Minnesota, Mississippi, and Texas) provide the STATE System their Tobacco Settlement Revenue data independently.",
+            "title": "NAAG Tobacco Settlement Payments",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Policy/NAAG-Tobacco-Settlement-Payments/ffbi-is3j",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Policy"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/fiep-96bi",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-10-11",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-24",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2024",
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
+            "identifier": "5c232812-fc30-4dd7-8af7-015ce0073eb8",
+            "description": "The Transparency in Coverage PUF (TC-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The PUF contains data on issuer and plan-level claims, appeals, and active URL data. The PY2024 PUF contains data from PY2022 for issuers participating in the Exchanges in PY2022.",
+            "title": "Transparency in Coverage PUF - PY2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/transparency_in_coverage_PUF.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
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
+            "issued": "2021-05-14",
+            "@type": "dcat:Dataset",
+            "temporal": "1950/2019",
+            "modified": "2022-04-27",
+            "keyword": [
+                "african americans",
+                "age",
+                "alaskan natives",
+                "american natives",
+                "asian continental ancestry group",
+                "continental population groups",
+                "death",
+                "deaths",
+                "european continental ancestry group",
+                "health us",
+                "hispanic americans",
+                "injury",
+                "mental health",
+                "mortality",
+                "sex",
+                "suicide"
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
+            "identifier": "https://data.cdc.gov/api/views/9j2v-jamp",
+            "description": "Data on death rates for suicide, by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National  Vital Statistics System (NVSS); Grove RD, Hetzel AM. Vital statistics rates in the United States, 1940\u20131960. National Center for Health Statistics. 1968; numerator data from NVSS annual public-use Mortality Files; denominator data from U.S. Census Bureau national population estimates; and Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B. Deaths: Final data for 2018. National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: National Center for Health Statistics. 2021. Available from: https://www.cdc.gov/nchs/products/nvsr.htm. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
+            "title": "Death rates for suicide, by sex, race, Hispanic origin, and age: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://repository.niddk.nih.gov/home/",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-18",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Rodriguez, Rebecca",
+                "hasEmail": "mailto:niddk-crsupport@niddk.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "ad6250c9-72ec-4581-9883-45012df72b4e",
+            "description": "<p>The NIDDK Central Repository stores biosamples, genetic and other data collected in designated NIDDK-funded clinical studies. The purpose of the NIDDK Central Repository is to expand the usefulness of these studies by allowing a wider research community to access data and materials beyond the end of the study.</p>",
+            "title": "NIDDK Central Repository",
+            "programCode": [
+                "009:110"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/medicare-value-based-payment-modifier-program/value-modifier",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2013-01-01/2016-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-06",
+            "references": [
+                "https://data.cms.gov/resources/2018-value-modifier-performance-year-2016-methodology"
+            ],
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c3e8e9c3-5193-47fb-a5bb-d3ddb00e7197/data-viewer",
+            "description": "The Medicare Value-Based Payment Modifier (Value Modifier) data contains the performance results of de-identified practices that were subject to the Value Modifier, such as the practices' quality and cost tiers along with any applicable Value Modifier payment adjustment. The Value Modifier provided\u00a0for differential payment under the Medicare Physician Fee Schedule based on the quality of care furnished to Medicare beneficiaries compared to the cost of care during a performance period. Calendar Year 2015 was the first payment adjustment period under the Value Modifier based on performance in 2013. Calendar Year 2018 was the final payment adjustment period under the Value Modifier based on performance in 2016.\u00a0\n\n\u00a0\n\nThe Merit-based Incentive Payment System (MIPS) under the Quality Payment Program has replaced the Value Modifier program. The Centers for Medicare & Medicaid Services (CMS) encourages everyone to learn more about the Quality Payment Program.\u00a0",
+            "title": "Value Modifier",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3e8e9c3-5193-47fb-a5bb-d3ddb00e7197/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Value Modifier : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-07/Value_Modifier_PUF_Performance_Year_2016.csv",
+                    "mediaType": "text/csv",
+                    "title": "Value Modifier : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e7ad6745-a67a-47ee-8e8e-4cdb26965868/data",
+                    "mediaType": "text/html",
+                    "title": "Value Modifier : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-07/Value_Modifier_PUF_Performance_Year_2015.csv",
+                    "mediaType": "text/csv",
+                    "title": "Value Modifier : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/45a5e2fd-2846-480b-a5e3-de22e2fd2320/data",
+                    "mediaType": "text/html",
+                    "title": "Value Modifier : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-07/Value_Modifier_PUF_Performance_Year_2014.csv",
+                    "mediaType": "text/csv",
+                    "title": "Value Modifier : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/52d91cf6-19ec-4721-b03e-d031b5af54ed/data",
+                    "mediaType": "text/html",
+                    "title": "Value Modifier : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-07/Value_Modifier_PUF_Performance_Year_2013.csv",
+                    "mediaType": "text/csv",
+                    "title": "Value Modifier : 2013-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6abfab7c-deb8-4de0-bc99-f895f71bad57/data",
+                    "mediaType": "text/html",
+                    "title": "Value Modifier : 2013-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/value-modifier-data-dictionary",
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
+            "landingPage": "https://data.cdc.gov/d/65xe-6neq",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2016-01-07",
+            "keyword": [
+                "2015",
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
+            "identifier": "https://data.cdc.gov/api/views/65xe-6neq",
+            "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-09-14",
+            "@type": "dcat:Dataset",
+            "temporal": "2002-01-01/2018-12-31",
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
+            "identifier": "https://data.cdc.gov/api/views/3q3z-9ucr",
+            "description": "[1] The Progress by Population Group analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included subsets of the 1,111 measurable HP2020 objectives that have data available for any of six broad population characteristics: sex, race and ethnicity, educational attainment, family income, disability status, and geographic location. Progress toward meeting HP2020 targets is presented for up to 24 population groups within these characteristics, based on objective data aggregated across HP2020 topic areas. The Progress by Population Group data are also available at the individual objective level in the downloadable data set. \n[2] The final value was generally based on data available on the HP2020 website as of January 2020. For objectives that are continuing into HP2030, more recent data will be included on the HP2030 website as it becomes available: https://health.gov/healthypeople.\n[3] For more information on the HP2020 methodology for measuring progress toward target attainment and the elimination of health disparities, see: Healthy People Statistical Notes, no 27; available from: https://www.cdc.gov/nchs/data/statnt/statnt27.pdf.\n[4] Status for objectives included in the HP2020 Progress by Population Group analysis was determined using the baseline, final, and target value. The progress status categories used in HP2020 were:\n\na. Target met or exceeded\u2014One of the following applies: (i) At baseline, the target was not met or exceeded, and the most recent value was equal to or exceeded the target (the percentage of targeted change achieved was equal to or greater than 100%); (ii) The baseline and most recent values were equal to or exceeded the target (the percentage of targeted change achieved was not assessed). \n\nb. Improved\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved 10% or more of the targeted change.\n\nc. Little or no detectable change\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was not statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved less than 10% of the targeted change; (iii) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was not statistically significant; (iv) Movement was away from the baseline and target, standard errors were not available, and the objective had moved less than 10% relative to the baseline; (v) No change was observed between the baseline and the final data point.\n\nd. Got worse\u2014One of the following applies: (i) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was statistically significant; (ii) Movement was away from the baseline and target, standard errors were not available, and the objective had moved 10% or more relative to the baseline.\n\nNOTE: Measurable objectives had baseline data.\nSOURCE: National Center for Health Statistics, Healthy People 2020 Progress by Population Group database.",
+            "title": "Healthy People 2020 Final Progress by Population Group Chart and Table",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3q3z-9ucr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3q3z-9ucr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3q3z-9ucr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3q3z-9ucr/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/yviw-z6j5",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-06",
+            "temporal": "2020-01-22/2023-05-10",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
+            "keyword": [
+                "covid",
+                "covid-19",
+                "surveillance"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Surveillance Review and Response Group",
+                "hasEmail": "mailto:eocevent394@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/yviw-z6j5",
+            "description": "<b>Note:</b> \nThe cumulative case count for some counties (with small population) is higher than expected due to the inclusion of non-permanent residents in COVID-19 case counts. \n\nReporting of Aggregate Case and Death Count data was discontinued on May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\n<b>Aggregate Data Collection Process\nSince the beginning of the COVID-19 pandemic, data were reported through a robust process with the following steps:</b><ul><li>Aggregate county-level counts were obtained indirectly, via automated overnight web collection, or directly, via a data submission process.</li><li>If more than one official county data source existed, CDC used a comprehensive data selection process comparing each official county data source to retrieve the highest case and death counts, unless otherwise specified by the state.</li><li>A CDC data team reviewed counts for congruency prior to integration. CDC routinely compiled these data and post the finalized information on COVID Data Tracker.</li><li>Cases and deaths are based on date of report and not on the date of symptom onset. CDC calculates rates in this data by using population estimates provided by the US Census Bureau Population Estimates Program (2019 Vintage).</li><li>COVID-19 aggregate case and death data were organized in a time series that includes cumulative number of cases and deaths as reported by a jurisdiction on a given date.  New case and death counts were calculated as the week-to-week change in reported cumulative cases and deaths (i.e., newly reported cases and deaths = cumulative number of cases/deaths reported this week minus the cumulative total reported the week before.</li></ul>\n\nThis process was collaborative, with CDC and jurisdictions working together to ensure the accuracy of COVID-19 case and death numbers. County counts provided the most up-to-date numbers on cases and deaths by report date. Throughout data collection, CDC retrospectively updated counts to correct known data quality issues. CDC also worked with jurisdictions after the end of the public health emergency declaration to finalize county data. \n<ul><li><b>Source:</b> The weekly archived dataset is based on county-level aggregate count data</li><li><b>Confirmed/Probable Cases/Death breakdown:</b> Cumulative cases and deaths for each county are included.  Total reported cases include probable and confirmed cases.</li><li><b>Time Series Frequency:</b> The weekly archived dataset contains weekly time series data (i.e., one record per week per county)</li></ul>\n \n<b>Important note:</b> The counts reflected during a given time period in this dataset may not match the counts reflected for the same time period in the daily archived dataset noted above. Discrepancies may exist due to differences between county and state COVID-19 case surveillance and reconciliation efforts.\n\nThe surveillance case definition for COVID-19, a nationally notifiable disease, was first described in a <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-covid-19/\">position statement</a> from the Council for State and Territorial Epidemiologists, which was later <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-covid-19/\">revised</a>. However, there is some variation in how jurisdictions implement these case classifications. More information on how CDC collects COVID-19 case surveillance data can be found at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\">FAQ: COVID-19 Data and Surveillance</a>.\n\n<b>Confirmed and Probable Counts</b>\nIn this dataset, counts by jurisdiction are not displayed by confirmed or probable status. Instead, counts of confirmed and probable cases and deaths are included in the Total Cases and Total Deaths columns, when available. Not all jurisdictions report",
+            "title": "Weekly United States COVID-19 Cases and Deaths by County - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "No longer updated (dataset archived)"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/fjmx-xmbz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2022-08-17",
+            "keyword": [
+                "py2022",
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
+            "identifier": "385f17c1-f03d-4927-947d-854cfcd07c00",
+            "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2022 Medical SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/med-shop-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ahrq.gov/data/innovations/3p-rd.html",
+            "bureauCode": [
+                "009:00"
+            ],
+            "rights": "Restricted-Use Files also available",
+            "issued": "2023-09-15",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-15",
+            "keyword": [
+                "physician",
+                "physician practice"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "3P-RD help desk",
+                "hasEmail": "mailto:3P-RD@ahrq.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality"
+            },
+            "identifier": "https://healthdata.gov/api/views/fk2u-ctai",
+            "description": "The Physician and Physician Practice Research Database (3P-RD) captures characteristics of physicians and physician practices in 13 states. The database describes the supply of physician services available across selected states for data year 2019-2020.",
+            "title": "Physician and Physician Practice Research Database (3P-RD)",
+            "programCode": [
+                "009:074"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ahrq.gov/data/innovations/3p-rd.html",
+                    "description": "The Physician and Physician Practice Research Database (3P-RD) captures characteristics of physicians and physician practices in 13 states. The database describes the supply of physician services available across selected states for data year 2019-2020. AHRQ created 3P-RD as a resource to address existing data gaps in physician health services information at the state and market levels. \n\n3P-RD consists of both public use and restricted use data files. The public use file (PUF) version of 3P-RD is currently available for download. The Restricted Use File (RUF) version of 3P-RD will be available for each state. Once the data are released, a data use agreement (DUA) will be required for access to the data files.",
+                    "@type": "dcat:Distribution",
+                    "title": "Physician and Physician Practice Research Database (3P-RD)"
+                }
+            ],
+            "spatial": "13 states (AR, AZ, CA, CO, FL, MA, MD, MN, MO, MT, NY, TX, WA)",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccine-confidence",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-07-06",
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
+            "identifier": "https://data.cdc.gov/api/views/akkj-j5ru",
+            "description": "National Immunization Survey-Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent by week for the national-level view, and by month for the jurisdiction-level view.",
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Trends in Vaccination Status and Intent",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/fkfr-fp4z",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-11-27",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "keyword": [
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "medicaid",
+                "program enrollment",
+                "renewals"
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
+            "identifier": "5abea2e0-3f8e-4b49-a50d-d63d5fd9103c",
+            "description": "All states (including the District of Columbia) provide data to the Centers for Medicare & Medicaid Services (CMS) on a range of Medicaid and Children\u2019s Health Insurance Program (CHIP) eligibility and enrollment metrics. These data reflect state-reported information on Medicaid and CHIP eligibility renewals initiated and scheduled for completion during the reporting period. In addition to reporting the outcomes of renewals at the end of each reporting period, states also provide an update on renewals that were reported pending as of the end of a reporting period. For more information on these data, see Sections II and III of the <a href=\"https://www.medicaid.gov/resources-for-states/downloads/eligibility-processing-data-specs-august-2024.pdf\">Eligibility Processing Data Report specifications</a>. <br/>\r\n<b>Notes:</b><br/> Georgia reported data for individuals who continue to be eligible following a change in circumstances and were granted a new 12-month eligibility period during the reporting period, along with data on individuals due for renewal in the month.<br/>\r\nNorth Carolina reports renewal outcomes for only initiated renewals scheduled for completion in the report month, and as such, the data do not reflect renewals that should have been completed in the reporting period that the state was unable to initiate by the end of the report month.",
+            "title": "State Medicaid and CHIP Eligibility Processing Data",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/renewal-dataset-january-2025-release.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1M",
+            "theme": [
+                "Enrollment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/resp-net/dashboard/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-05-03",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-24",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "RESP-NET",
+                "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/kvib-3txy",
+            "description": "The Respiratory Virus Hospitalization Surveillance Network (RESP-NET) is a network that conducts, active, population-based surveillance for laboratory confirmed hospitalizations associated with Influenza, COVID-19, and RSV. The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. Hospitalization rates show how many people in the surveillance area are hospitalized with influenza, COVID-19, and RSV compared to the total number of people residing in that area. \n\nData will be updated weekly. Data are preliminary and subject to change as more data become available.",
+            "title": "Rates of Laboratory-Confirmed RSV, COVID-19, and Flu Hospitalizations from the RESP-NET Surveillance Systems",
+            "programCode": [
+                "009:038"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "RESP-NET Sites",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://jats.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-02-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-05",
+            "keyword": [
+                "data standards",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/77jt-4tze",
+            "description": "Journal Article Tag Suite (JATS) is an application of NISO Z39.96.2019, which defines a set of XML elements and attributes for describing the textual and graphical content of journal articles and describes three article models.",
+            "title": "Journal Article Tag Suite (JATS)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://jats.nlm.nih.gov/",
+                    "mediaType": "text/html",
+                    "title": "Journal Article Tag Suite (JATS) Homepage"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-home-health-agency",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2013-01-01/2021-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-06-12",
+            "references": [
+                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "home health",
+                "hospitals & facilities",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/b8135181-4274-4a11-a6cd-992090297ef5/data-viewer",
+            "description": "The Medicare Home Health Agency tables provide use and payment data for home health agencies. The tables include use and expenditure data from home health Part A (Hospital Insurance) and Part B (Medical Insurance) claims.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR HHA 1. \u00a0Medicare Home Health Agencies: \u00a0Utilization and\u00a0Program Payments for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR HHA 2. \u00a0Medicare Home Health Agencies: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR HHA 3. \u00a0Medicare Home Health Agencies: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR HHA 4. \u00a0Medicare Home Health Agencies: \u00a0Persons with Utilization and Total Service Visits for Original Medicare Beneficiaries, Type of Agency and Type of Service Visit\n\tMDCR HHA 5. \u00a0Medicare Home Health Agencies: \u00a0Persons with Utilization and Total Service Visits for Original Medicare Beneficiaries, by Type of Control and Type of Service Visit\n\tMDCR HHA 6. \u00a0Medicare Home Health Agencies: \u00a0Persons with Utilization, Total Service Visits, and Program Payments for Original Medicare Beneficiaries, by Number of Service Visits and Number of Episodes",
+            "title": "CMS Program Statistics - Medicare Home Health Agency",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/CPS%20MDCR%20HHA%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20HHA%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2020-02-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/CPS_MDCR_HHA_1-6.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/CPS%20MDCR%20TOTAL%20HHA%202018.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2019-12/CPS_MDCR_HHA_2017.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_HHA_ALL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_HHA_ALL_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_HHA_ALL_1.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_HHA_ALL_2.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Home Health Agency : 2013-12-31"
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-04-21",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-04/2023-07-22",
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
+                "influenza",
+                "kidney disease",
+                "mortality",
+                "natural cause",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
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
+            "identifier": "https://data.cdc.gov/api/views/muzy-jte6",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the week the deaths occurred, by state of occurrence, and by select underlying causes of death for 2020-2023.  The dataset also includes weekly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.\n\nNOTE: death counts are presented with a one week lag.",
+            "title": "Weekly Provisional Counts of Deaths by State and Select Causes, 2020-2023",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/fmc9-nsxa",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-09-13",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-12",
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
+            "identifier": "b3c30bd4-f3f9-496f-97ec-c5f9d8083ad0",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-04-to-2023-09-10",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-09-04-2023-to-09-10-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-04-to-2023-09-10"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/fmd4-iw4i",
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
+            "identifier": "9285d2b8-866e-5760-ac92-c2628ac59e2e",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2009",
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
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608",
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug-related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 22 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "title": "Drug Abuse Warning Network (DAWN-2009)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608",
+                    "description": "Drug Abuse Warning Network (DAWN-2009) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.metabolomicsworkbench.org/",
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
+                "fn": "MARUVADA, PADMA\u00a0",
+                "hasEmail": "mailto:maruvadp@mail.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "37d41112-7b13-4f93-9c6c-f6e0b12f979f",
+            "description": "<p>The Metabolomics Program's Data Repository and Coordinating Center (DRCC), housed at the San Diego Supercomputer Center (SDSC), University of California, San Diego, has developed the Metabolomics Workbench. MetWB will serve as a national and international repository for metabolomics data and metadata and will provide analysis tools and access to metabolite standards, protocols, tutorials, training, and more.</p>",
+            "title": "Metabolomics Workbench (MetWB)",
+            "programCode": [
+                "009:110"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "cder"
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
+            "identifier": "520f8f0d-b519-4ad9-8597-14d517f00987",
+            "description": "Information provided to FDA by manufacturers about current drugs in shortage, resolved shortages, and discontinuations of specific drug products.",
+            "title": "Current and Resolved Drug Shortages and Discontinuations Reported to FDA",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/g6fu-zp23",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "age <5 years",
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
+            "identifier": "https://data.cdc.gov/api/views/g6fu-zp23",
+            "description": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/keia-pvvn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
+                "anaplasma phagocytophilum",
+                "ehrlichia chaffeensis",
+                "ehrlichiosis/anaplasmosis",
+                "mmwr",
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
+            "identifier": "https://data.cdc.gov/api/views/keia-pvvn",
+            "description": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. \r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.   Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n \r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Please refer to the MMWR publication for weekly updates to the footnote for this condition.",
+            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-07-14",
+            "@type": "dcat:Dataset",
+            "temporal": "1915/2013",
+            "modified": "2022-03-30",
+            "keyword": [
+                "infant mortality rates",
+                "nchs",
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
+            "identifier": "https://data.cdc.gov/api/views/ddsk-zebd",
+            "description": "All birth data by race before 1980 are based on race of the child; starting in 1980, birth data by race are based on race of the mother. Birth data are used to calculate infant mortality rate.\r\n\r\nhttps://www.cdc.gov/nchs/data-visualization/mortality-trends/",
+            "title": "NCHS - Infant Mortality Rates, by Race: United States, 1915-2013",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/x9gk-5huc",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-27",
+            "keyword": [
+                "2022",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NNDSS Team",
+                "hasEmail": "mailto:NNDSSWeb@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/x9gk-5huc",
+            "description": "NNDSS - In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\n\nNotes:\n\n\u2022 These are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/infectious-disease/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data.\n\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page https://www.cdc.gov/nndss/infectious-disease/notice-to-data-users.html.\n\n\u2022 The list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2024 and 2025 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u2022 Please refer to the Stacks publication for weekly updates to the footnote for influenza-associated pediatric mortality.\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS Weekly Data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/52cr-rw4k",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-01-08",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "2014",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonellosis",
+                "shiga toxin-producing e. coli",
+                "shigellosis",
+                "stec",
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
+            "identifier": "https://data.cdc.gov/api/views/52cr-rw4k",
+            "description": "NNDSS - Table II. Salmonellosis to Shigellosis - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Includes E. coli O157:H7; Shiga toxin positive, serogroup non-O157; and Shiga toxin positive, not serogrouped.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
+            "title": "NNDSS - Table II. Salmonellosis to Shigellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/52cr-rw4k/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/52cr-rw4k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/52cr-rw4k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/52cr-rw4k/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://imagic.nlm.nih.gov/imagic/code/map",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-05",
+            "keyword": [
+                "health data standards",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/7bij-avxu",
+            "description": "I-MAGIC (Interactive Map-Assisted Generation of ICD Codes)  is an interactive tool to demonstrate how the SNOMED CT to ICD-10-CM map can be used to generate ICD-10-CM codes from clinical problems coded in SNOMED CT.",
+            "title": "I-MAGIC",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://imagic.nlm.nih.gov/imagic/code/map",
+                    "mediaType": "text/html",
+                    "title": " I-MAGIC Homepage and Search"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/fruh-rw7y",
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
+            "identifier": "abb567c0-42bd-5851-870e-8dad158d97e2",
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
+            "landingPage": "https://data.cdc.gov/d/n835-hpyp",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
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
+            "identifier": "https://data.cdc.gov/api/views/n835-hpyp",
+            "description": "NNDSS - Table II. Chlamydia to Coccidioidomycosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP:  Nationally notifiable but not published.  Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/d29v-yfc2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-06",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Physical Effects Research Branch, Health Effects Laboratory Division",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/d29v-yfc2",
+            "description": "Masonry work, a sub-specialty of the construction industry, consists of brick and block-laying. Masonry workers often perform these tasks daily using an elevated work platform (e.g., mast climbers). Mast climbers are elevating equipment used to replace traditional scaffolds. They have been available in the United States since the 1980s.  Mast climbers are capable of handling much greater loads of workers and materials than traditional scaffolding. They also make reaching greater heights much easier, thereby improving efficiency on construction projects. However, working on an unstable work platform at elevation can increase the risks of slips, trips and falls, including falls to a lower level. From 1990 to 2017, there were a total of 35 recorded fatalities associated with the use of mast climbers. Of the 35 fatalities, 13 were masonry workers (OSHA report).  Additionally, working on a mast climber can also create awkward working postures due to the confined nature of the workspace. Masonry work can be physically demanding. Concrete block can weigh between 9-27 kg. The rate of overexertion among masonry workers was 33.4 per 10,000 FTEs compared to the average rate of 21.5 per 10,000 FTEs in all industries (BLS data). Shoulder-assist exoskeletons present an attractive possibility to reduce MSD risks in masonry workers if the exoskeletons do not cause adverse effects to the workers\u2019 stability and balance. \n\nIn this study, we evaluated effects of three models of passive shoulder-assist exoskeletons on balance and shoulder muscle activity during a masonry task on a simulated mast climbing work platform. The balance-related parameters and shoulder muscle activities were compared when using or not using the exoskeletons. We want to evaluate the hypotheses that the exoskeletons (1) reduce shoulder muscle activity and (2) decrease the stability of the workers.",
+            "title": "Shoulder-Assist Exoskeleton Effects on Balance and Muscle Activity During a Block-laying Task on a Simulated Mast Climber",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/d29v-yfc2/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/dkyk-v5f5",
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
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli (stec)",
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
+            "identifier": "https://data.cdc.gov/api/views/dkyk-v5f5",
+            "description": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-31",
+            "keyword": [
+                "osh",
+                "sam",
+                "sammec",
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
+            "identifier": "https://data.cdc.gov/api/views/4yyu-3s69",
+            "description": "2005-2009. SAMMEC - Smoking-Attributable Mortality, Morbidity, and Economic Costs. Smoking-attributable mortality (SAM) is the number of deaths caused by cigarette smoking based on diseases for which the U.S. Surgeon General has determined that cigarette smoking is a causal factor.",
+            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Mortality (SAM)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yyu-3s69/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yyu-3s69/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yyu-3s69/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4yyu-3s69/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Health Consequences and Costs"
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
+            "identifier": "https://data.cdc.gov/api/views/k25u-mg9b",
+            "description": "2016, 2015. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census tract-level data in GIS-friendly format can be joined with census tract spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-Boundaries/x7zy-2xmx) in a geographic information system (GIS) to produce maps of 27 measures at the census tract level. There are 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, cholesterol screening) in this 2018 release from the 2015 BRFSS that were the same as the 2017 release.",
+            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2018 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/c2hx-eeis",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
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
+            "identifier": "https://data.cdc.gov/api/views/c2hx-eeis",
+            "description": "In 2003, the National Institute for Occupational Safety and Health (NIOSH) conducted a nationwide anthropometric survey of 3,997 subjects. The resulting head and face measurements were used to develop an anthropometric database detailing the face size distributions of respirator users using both traditional measurement methods and three-dimensional (3D) scanning systems. This database was used to establish fit test panels to be incorporated into NIOSH respirator certification and international standards. One of the panels developed, called the principal component analysis (PCA) panel, uses the first two principal components obtained from a set of 10 facial dimensions (age and race adjusted) and divides user population into five face-size categories. These 10 dimensions are associated with respirator fit and leakage and can predict the remaining face dimensions as well. Respirators designed to fit these panels are expected to accommodate more than 95% of the current U.S. civilian workers.\n\nFrom the 3,997 subje",
+            "title": "NIOSH Anthropometric Data and ISO Digital Headforms",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/c2hx-eeis/application/x-zip-compressed",
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
+            "issued": "2023-04-10",
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
+            "identifier": "https://data.cdc.gov/api/views/fvm6-ic5r",
+            "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
+            "title": "BEAM Dashboard - Serotypes of concern: Illnesses and Outbreaks",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/home-health-agency-cost-report",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-12-15",
+            "temporal": "2020-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-25",
+            "references": [
+                "https://data.cms.gov/resources/home-health-agency-cost-report-methodology"
+            ],
+            "keyword": [
+                "financials",
+                "home health",
+                "hospitals & facilities",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data-viewer",
+            "description": "The Home Health Agency Provider Cost Report dataset provides select measures from the home health agency annual cost report. This data includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
+            "title": "Home Health Agency Cost Report",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Home Health Agency Cost Report : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/19db07e2-b626-480a-8554-8cb2ea64f5df/CostReporthha_Final_22.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Cost Report : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1adf48d9-9ff2-4641-ac51-d827aabf791c/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Cost Report : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/e5f655dd-d6e9-466b-8669-5aec4bd2f76d/CostReporthha_Final_21.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Cost Report : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a02a324e-a8ad-4933-8bcd-e6a10ab28c8e/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Cost Report : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/2864363c-e84f-4cde-9042-f55590b750b7/CostReporthha_Final_20.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Cost Report : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2914a2e4-6d60-4b46-8806-9e9c56ca2f39/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Cost Report : 2020-12-02"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/home-health-agency-cost-report-data-dictionary",
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
+            "landingPage": "https://healthdata.gov/d/fx7n-f9pk",
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
+            "identifier": "d6a1edcf-eec9-5eef-82e2-a4d68cc940c4",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt version v2.10.22 (coreset-impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/version.csv",
+                    "description": "CoreSEt version v2.10.22 (coreset-impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt version v2.10.22 (coreset-impl)"
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
+            "landingPage": "https://data.cdc.gov/d/axgy-8qey",
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
+                "nonparalytic",
+                "poliovirus infection",
+                "psittacosis",
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
+            "identifier": "https://data.cdc.gov/api/views/axgy-8qey",
+            "description": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/e8fc-yrqd",
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
+            "identifier": "https://data.cdc.gov/api/views/e8fc-yrqd",
+            "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 1 - Boston",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2020-09-15",
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
+            "identifier": "https://data.cdc.gov/api/views/w4jm-mysj",
+            "description": "Deaths involving coronavirus disease 2019 (COVID-19) by month of death, region, age, place of death, and race and Hispanic origin: May-August 2020.",
+            "title": "AH Monthly COVID-19 Deaths, by Census Region, Age, Place, and Race and Hispanic Origin, 2020 Provisional",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w4jm-mysj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w4jm-mysj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w4jm-mysj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w4jm-mysj/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/54ys-qyzm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-03-17",
+            "@type": "dcat:Dataset",
+            "temporal": "October 3, 2021 - April 22, 2023",
+            "modified": "2023-06-01",
+            "keyword": [
+                "covid-19 bivalent boosters",
+                "covid-19 booster doses",
+                "covid-19 breakthrough",
+                "covid-19 cases",
+                "covid-19 deaths",
+                "covid-19 vaccination"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vaccine Breakthrough/Surveillance and Analytics Team",
+                "hasEmail": "mailto:vbtsurveillance@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/54ys-qyzm",
+            "description": "Data for CDC\u2019s COVID Data Tracker site on Rates of COVID-19 Cases and Deaths by Updated (Bivalent) Booster Status.\nClick 'More' for important dataset description and footnotes\n\nWebpage: https://covid.cdc.gov/covid-data-tracker/#rates-by-vaccine-status\n\nDataset and data visualization details:\n\n\nThese data were posted and archived on May 30, 2023 and reflect cases among persons with a positive specimen collection date through April 22, 2023, and deaths among persons with a positive specimen collection date through April 1, 2023. These data will no longer be updated after May 2023.\n\nVaccination status: A person vaccinated with at least a primary series had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably completing the primary series of an FDA-authorized or approved COVID-19 vaccine. An unvaccinated person had SARS-CoV-2 RNA or antigen detected on a respiratory specimen and has not been verified to have received COVID-19 vaccine. Excluded were partially vaccinated people who received at least one FDA-authorized vaccine dose but did not complete a primary series \u226514 days before collection of a specimen where SARS-CoV-2 RNA or antigen was detected. A person vaccinated with a primary series and a monovalent booster dose had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably receiving a primary series of an FDA-authorized or approved vaccine and at least one additional dose of any monovalent FDA-authorized or approved COVID-19 vaccine on or after August 13, 2021. (Note: this definition does not distinguish between vaccine recipients who are immunocompromised and are receiving an additional dose versus those who are not immunocompromised and receiving a booster dose.) A person vaccinated with a primary series and an updated (bivalent) booster dose had SARS-CoV-2 RNA or antigen detected in a respiratory specimen collected \u226514 days after verifiably receiving a primary series of an FDA-authorized or approved vaccine and an additional dose of any bivalent FDA-authorized or approved vaccine COVID-19 vaccine on or after September 1, 2022. (Note: Doses with bivalent doses reported as first or second doses are classified as vaccinated with a bivalent booster dose.) People with primary series or a monovalent booster dose were combined in the \u201cvaccinated without an updated booster\u201d category. \n\nDeaths: A COVID-19\u2013associated death occurred in a person with a documented COVID-19 diagnosis who died; health department staff reviewed to make a determination using vital records, public health investigation, or other data sources. Per the interim guidance of the Council of State and Territorial Epidemiologists (CSTE), this should include persons whose death certificate lists COVID-19 disease or SARS-CoV-2 as the underlying cause of death or as a significant condition contributing to death. Rates of COVID-19 deaths by vaccination status are primarily reported based on when the patient was tested for COVID-19. In select jurisdictions, deaths are included that are not laboratory confirmed and are reported based on alternative dates (i.e., onset date for most; or date of death or report date, where onset date is unavailable). Deaths usually occur up to 30 days after COVID-19 diagnosis.\n\nParticipating jurisdictions: Currently, these 24 health departments that regularly link their case surveillance to immunization information system data are included in these incidence rate estimates: Alabama, Arizona, Colorado, District of Columbia, Georgia, Idaho, Indiana, Kansas, Kentucky, Louisiana, Massachusetts, Michigan, Minnesota, Nebraska, New Jersey, New Mexico, New York, New York City (NY), North Carolina, Rhode Island, Tennessee, Texas, Utah, and West Virginia; 23 jurisdictions also report deaths among vaccinated and unvaccinated people. These jurisdictions represent 48% of the total U.S. population and all ten of the Health and Human Services Regions. This list will be",
+            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Updated (Bivalent) Booster Status",
+            "programCode": [
+                "009:038"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/54ys-qyzm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/54ys-qyzm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/54ys-qyzm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/54ys-qyzm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "Select US Jurisdictions",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "None - this dataset is archived as of May 2023",
+            "theme": [
+                "Public Health Surveillance"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/fztk-4izv",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2014-09-22",
+            "keyword": [
+                "drug name",
+                "feasibility",
+                "proprietary",
+                "safety"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Quinn",
+                "hasEmail": "mailto:john.quinn@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "78e2c44a-948a-4f20-a810-6f1e60cee0d1",
+            "description": "POCA is a software that produces a data set used internally to assess the  safety, and feasibility of proposed proprietary drug names.  FDA product name safety evaluators have access to an internal version of the POCA system behind the FDA firewall.   Source code to develop external non-FDA instances of POCA are available at http://www.fda.gov/Drugs/ResourcesForYou/Industry/ucm400127.htm",
+            "title": "POCA -Phonetic Orthographic Computer Algorithm",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/Drugs/ResourcesForYou/Industry/ucm400127.htm",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-medicaid.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-12-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2015/2017",
+            "modified": "2024-10-11",
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/NCHS-TMSIS-MATCH-STATUS.pdf"
+            ],
+            "keyword": [
+                "linked medicaid data",
+                "nhcs",
+                "research-data-center",
+                "t-msis"
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
+            "identifier": "https://data.cdc.gov/api/views/ay69-birh",
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with Medicaid and Children\u2019s Health Insurance Program (CHIP) claims data collected by the Centers for Medicare & Medicaid Services (CMS) Transformed Medicaid Statistical Information System (T-MSIS). Linkage of NHCS patient data with T-MSIS enrollment and claims data creates a new data resource that can support research studies focused on a wide range of patient health outcomes and the association of means-tested government insurance programs with health and health outcomes.",
+            "title": "National Hospital Care Survey (NHCS) linked to Centers for Medicare & Medicaid (CMS) Medicaid Data",
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
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 22) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-medicaid-linkage-methodology.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1998",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "alcohol",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630",
+            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npsychotherapeutics. Respondents were also asked about personal and<br />\nfamily income sources and amounts, substance abuse treatment history,<br />\nillegal activities, problems resulting from the use of drugs, need for<br />\ntreatment for drug or alcohol use, criminal record, and<br />\nneedle-sharing. Questions on mental health and access to care, which<br />\nwere introduced in the 1994-B questionnaire (see NATIONAL HOUSEHOLD<br />\nSURVEY ON DRUG ABUSE, 1994), were retained in this<br />\nadministration of the survey. Also retained was the section on<br />\nrisk/availability of drugs that was reintroduced in 1996, and sections<br />\non driving behavior and personal behavior were added (see NATIONAL<br />\nHOUSEHOLD SURVEY ON DRUG ABUSE, 1996). The 1997<br />\nquestionnaire (NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1997) introduced new items that the 1998 NHSDA continued on cigar<br />\nsmoking, people who were present when respondents used marijuana or<br />\ncocaine for the first time (if applicable), reasons for using these<br />\ntwo drugs the first time, reasons for using these two drugs in the<br />\npast year, reasons for discontinuing use of these two drugs (for<br />\nlifetime but not past-year users), and reasons respondents never used<br />\nthese two drugs. Both the 1997 and 1998 NHSDAs had a series of<br />\nquestions that were asked only of respondents aged 12 to 17. These<br />\nitems covered a variety of topics that may be associated with<br />\nsubstance use and related behaviors, such as exposure to substance<br />\nabuse prevention and education programs, gang involvement,<br />\nrelationship with parents, and substance use by friends. Demographic<br />\ndata include gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, income level, veteran status, and current household<br />\ncomposition.This study has 1 Data Set.</p>",
+            "title": "National Household Survey on Drug Abuse (NHSDA-1998)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1998) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-11-28",
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
+            "identifier": "https://data.cdc.gov/api/views/khic-yj26",
+            "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
+            "title": "BEAM Dashboard - Isolates by HHS Region",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
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
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
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
+            "identifier": "https://data.cdc.gov/api/views/equ4-92qe",
+            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
+            "title": "Quitline \u2013 Service Utilization - 2010 To Present",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Service-Utilization-2010-To-Present/equ4-92qe",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Quitline"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/g2vc-5pzi",
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
+            "identifier": "2eb2dbeb-08d4-56a3-b081-2c87d0353027",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard version v2.11.9 (prod)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/version.csv",
+                    "description": "Scorecard version v2.11.9 (prod)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard version v2.11.9 (prod)"
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
+            "landingPage": "https://www.healthit.gov/data/datasets/students-trained-through-onc-workforce-programs",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2014-06-01",
+            "references": [
+                "http://www.healthit.gov/facas/sites/faca/files/Workforce%20Evaluation%20Briefing%20for%20FACA%20Committee%2009%2010.pdf",
+                "https://www.healthit.gov/data/quickstats/hitech-workforce-development-programs"
+            ],
+            "keyword": [
+                "grantees",
+                "health information",
+                "health it",
+                "health it professionals",
+                "onc community college consortia"
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
+            "identifier": "4zpu3gv4-vo8i-wwb6-6wfi-gd6i7vzqsqo3",
+            "description": "The Office of the National Coordinator for Health Information Technology (ONC) created the Community College Consortia to Educate Health IT Professionals in Health Care Program and University-based Training Program to increase the workforce of skilled health IT specialists that can help transition health care providers to electronic health records (EHRs). The Community College Consortia Program includes 82 member community colleges representing all 50 states, and the University-based Training Program includes 9 member universities in 9 states. The member community colleges and universities received funding to rapidly create health IT academic programs, or expand existing health IT training programs that can be completed in six months or less. This data provides the number of students trained through both programs, segmented by rural and urban areas for each U.S. state. The data is through September, 2013: the duration of the program. This data is an artifact of ONC's performance measurement for the Recovery and HITECH Acts",
+            "title": "Students Trained through ONC Workforce Programs",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/workforce-programs-trained.csv",
+                    "mediaType": "text/csv",
+                    "title": "workforce-programs-trained.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/students-trained-through-onc-workforce-programs"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1993",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1993)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1993) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-10-18",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2022-10-15",
+            "modified": "2023-04-05",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "county",
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
+            "identifier": "https://data.cdc.gov/api/views/ite7-j2w7",
+            "description": "Provisional count of deaths involving COVID-19 by United States county of occurrence, by week of death.",
+            "title": "AH COVID-19 Death Counts by County and Week, 2020-present",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/wa6b-urfv",
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
+            "identifier": "https://data.cdc.gov/api/views/wa6b-urfv",
+            "description": "A new high-flow, compact aerosol concentrator, using rapid, turbulent mixing to grow aerosol particles into droplets for dry spot sample collection, has been designed and tested. The \u201cTCAC (Turbulent-mixing, Condensation Aerosol Concentrator)\u201d is composed of a saturator for generating hot vapor, a mixing section where the hot vapor mixes with the cold aerosol flow, a growth tube where condensational droplet growth primarily occurs, and a converging nozzle that focuses the droplets into a beam. The prototype concentrator utilizes an aerosol sample flow rate of 4 L min-1. The TCAC was optimized by varying the operating conditions, such as relative humidity of the aerosol flow, mixing flow ratio, vapor temperature, and impaction characteristics. The results showed that particles with a diameter \u2265 25 nm can be grown to a droplet diameter > 1400 nm with near 100 % efficiency. Complete activation and growth were observed at relative humidity \u2265 25 % of the aerosol sample flow. A consistent spot sample with a diameter of D90 = 1.4 mm (the diameter of a circle containing 90 % of the deposited particles) was obtained regardless of the aerosol particle diameter (dp = 20 \u2013 1900 nm). For fiber counting applications using phase contrast microscopy, the TCAC can reduce the sampling time, or counting uncertainty, by two to three orders of magnitude, compared to the 25-mm-filter collection. The study shows that the proposed mixing-flow scheme enables a compact spot sample collector suitable for handheld or portable applications, while still allowing for high flow rates.",
+            "title": "Compact, High-flow, Water-based, Turbulent-mixing, Condensation Aerosol Concentrator for Collection of Spot Samples",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/wa6b-urfv/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "Restricted data files can be requested through the Research Data Center. Restricted files contain sensitive protected health information.",
+            "issued": "2024-02-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2018, 2019, 2021",
+            "modified": "2024-02-20",
+            "references": [
+                "https://www.cdc.gov/nchs/data/nehrs/2018_NEHRS_Questionnaire_08092018-508.pdf",
+                "https://www.cdc.gov/nchs/data/nehrs/NEHRS2019-Questionnaire-508.pdf",
+                "https://www.cdc.gov/nchs/data/nehrs/NEHRS2020-Questionnaire-508.pdf"
+            ],
+            "keyword": [
+                "electronic health records",
+                "nchs",
+                "nehrs",
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
+            "identifier": "https://data.cdc.gov/api/views/7jqv-mu8u",
+            "description": "The National Electronic Health Records Survey (NEHRS) is an annual survey of non-federally employed, office-based physicians practicing in the United States (excluding those in the specialties of anesthesiology, radiology, and pathology). NEHRS began in 2008 and was originally designed as an annual mail supplement to the National Ambulatory Medical Care Survey (NAMCS). Since 2012, NEHRS has been administered as a survey independent of NAMCS.\nData from NEHRS can be used to produce state and national estimates of EHR adoption and capabilities, burden associated with EHRs, and progress physicians have made towards meeting the policy goals of the HITECH Act. In more recent years, survey questions have also asked about Promoting Interoperability programs, sponsored by the Centers for Medicare and Medicaid Services (CMS).",
+            "title": "National Electronic Health Records Survey, Public-use data: 2018, 2019, 2021",
+            "isPartOf": "https://www.cdc.gov/nchs/nehrs/questionnaires.htm",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NEHRS/",
+                    "description": "SAS and STATA .zip files",
+                    "@type": "dcat:Distribution",
+                    "title": "NEHRS 2018, 2019, 2021"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://www.cdc.gov/nchs/data/nehrs/2021-NEHRS-public-use-file-layout-508.pdf, https://www.cdc.gov/nchs/data/nehrs/2019-NEHRS-public-use-layout-508.pdf, https://www.cdc.gov/nchs/data/nehrs/2018-NEHRS-public-restricted-layout-508.pdf",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Future funding patterns past 2024 are uncertain however, we expect yearly or biannually is reasonable R/P1Y or R/P2Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/g4wx-we5n",
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
+            "identifier": "d4063f55-6da8-587b-8279-8ff627b2318b",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_tafVersion",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/tafVersion.csv",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://healthdata.gov/d/g58t-eidy",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "acute care",
+                "chip",
+                "dqatlas",
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
+            "identifier": "d55e5ef5-9a2e-4d6c-884e-65a40a70756b",
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of acute care services, including emergency department (ED) visits, inpatient stays, intensive care unit (ICU) stays, and ICU stays that include ventilator use, provided to Medicaid and CHIP beneficiaries, by state. Users can filter to acute care services for any reason, or acute care services for COVID-19. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating acute care services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Acute Care Services Provided to the Medicaid and CHIP Population",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/Acute-Care-Services-Provided-to-the-MedicaidCHIP-Population.csv",
+                    "description": "Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Acute Care Services Provided to the Medicaid and CHIP Population"
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2009",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631",
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2009)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2009) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/g5mg-5c44",
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
+            "identifier": "315310e1-367d-51cd-ac6d-ecf42f828960",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_files_topicSnapshot",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
+                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"featAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-19",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "gis",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "unhealthy",
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
+            "identifier": "https://data.cdc.gov/api/views/bdsk-unrd",
+            "description": "This dataset contains model-based ZIP Code tabulation Areas (ZCTA) level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 27 measures at the ZCTA level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2020 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/cr56-k9wj",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-04-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-07",
+            "keyword": [
+                "animal model",
+                "ferret",
+                "flu",
+                "influenza",
+                "in vivo",
+                "pathogenesis",
+                "risk assessment",
+                "virus"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jessica Belser",
+                "hasEmail": "mailto:jax6@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/cr56-k9wj",
+            "description": "Data from influenza A virus (IAV) infected ferrets (Mustela putorius furo) provides invaluable information towards the study of novel and emerging viruses that pose a threat to human health. This gold standard animal model can recapitulate many clinical signs of infection present in IAV-infected humans, support virus replication of human and zoonotic strains without prior adaptation, and permit evaluation of virus transmissibility by multiple modes. While ferrets have been employed in risk assessment settings for >20 years, results from this work are typically reported in discrete stand-alone publications, making aggregation of raw data from this work over time nearly impossible. Here, we describe a dataset of 728 ferrets inoculated with 126 unique IAV, conducted by a single research group (NCIRD/ID/IPB/Pathogenesis Laboratory Team) under a uniform experimental protocol. This collection of morbidity, mortality, and viral titer data represents the largest publicly available dataset to date of in vivo-generated IAV infection outcomes on a per-individual ferret level.\n\nPublished Data Descriptor for more information:\nKieran TJ, Sun X, Creager HM, Tumpey TM, Maine TR, Belser JA. 2024. An aggregated dataset of serial morbidity and titer measurements from influenza A virus-infected ferrets. Sci Data 11, 510. https://doi.org/10.1038/s41597-024-03256-6\n\nAdditional publications using and describing data:\nKieran TJ, Sun X, Maines TR, Beauchemin CAA, Belser JA. 2024. Exploring associations between viral titer measurements and disease outcomes in ferrets inoculated with 125 contemporary influenza A viruses. J Virol98:e01661-23.https://doi.org/10.1128/jvi.01661-23\n\nBelser JA, Kieran TJ, Mitchell ZA, Sun X, Mayfield K, Tumpey TM, Spengler JR, Maines TR. 2024. Key considerations to improve the normalization, interpretation and reproducibility of morbidity data in mammalian models of viral disease. Dis Model Mech; 17 (3): dmm050511. doi: https://doi.org/10.1242/dmm.050511\n\nKieran TJ, Sun X, Maines TR, Belser JA. 2024. Machine learning approaches for influenza A virus risk assessment identifies predictive correlates using ferret model in vivo data. Communications Biology 7, 927. https://doi.org/10.1038/s42003-024-06629-0",
+            "title": "An aggregated dataset of serially collected influenza A virus morbidity and titer measurements from virus-infected ferrets.",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "National Center for Immunization and Respiratory Diseases"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/nra9-vzzn",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-06",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-22/2022-10-18",
+            "modified": "2025-01-13",
+            "references": [
+                "https://data.cdc.gov/Public-Health-Surveillance/United-States-County-Level-of-Community-Transmissi/8396-v7yb"
+            ],
+            "keyword": [
+                "cases",
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
+            "identifier": "https://data.cdc.gov/api/views/nra9-vzzn",
+            "description": "On October 20, 2022, CDC began retrieving aggregate case and death data from jurisdictional and state partners weekly instead of daily. This dataset contains archived historical community transmission and related data elements by county. Although these data will continue to be publicly available, this dataset has not been updated since October 20, 2022. An archived dataset containing weekly historical community transmission data by county can also be found here: <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly COVID-19 County Level of Community Transmission Historical Changes | Data | Centers for Disease Control and Prevention (cdc.gov)</a>. \n\n<b>Related data</b>\nCDC has been providing the public with two versions of COVID-19 county-level community transmission level data: this historical dataset with the daily county-level transmission data from January 22, 2020, and a dataset with the daily values as originally posted on the COVID Data Tracker. Similar to this dataset, the <a href=\"https://data.cdc.gov/Public-Health-Surveillance/United-States-COVID-19-County-Level-of-Community-T/nra9-vzzn\">original dataset</a> with daily data as posted is archived on 10/20/2022. It will continue to be publicly available but will no longer be updated. A new dataset containing community transmission data by county as originally posted is now published weekly and can be found at: <a href=\"https://data.cdc.gov/dataset/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly COVID-19 County Level of Community Transmission as Originally Posted | Data | Centers for Disease Control and Prevention (cdc.gov)</a>.\n\nThis public use dataset has 7 data elements reflecting historical data for community transmission levels for all available counties and jurisdictions. It contains historical data for the county level of community transmission and includes updated data submitted by states and jurisdictions. Each day, the dataset was updated to include the most recent days\u2019 data and incorporate any historical changes made by jurisdictions. This dataset includes data since January 22, 2020. Transmission level is set to low, moderate, substantial, or high using the calculation rules below.\n\n<b>Methods for calculating county level of community transmission indicator</b>\nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and <a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making.\n\n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00).\n\n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests resulted over the last 7 days. \"Percentage of positive NAAT in the past 7 days\" is considered to have transmission level of Low (less than 5.00); Moderate (5.00-7.99); Substa",
+            "title": "United States COVID-19 County Level of Community Transmission Historical Changes - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nra9-vzzn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nra9-vzzn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nra9-vzzn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nra9-vzzn/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2022-04-28",
+            "@type": "dcat:Dataset",
+            "temporal": "1999/2019",
+            "modified": "2022-04-28",
+            "keyword": [
+                "african americans",
+                "age",
+                "alaskan natives",
+                "american natives",
+                "analgesics",
+                "asian continental ancestry group",
+                "continental population groups",
+                "death",
+                "drug overdose",
+                "european continental ancestry group",
+                "health us",
+                "heroin",
+                "hispanic americans",
+                "injury",
+                "methadone",
+                "mortality",
+                "opioid",
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
+            "identifier": "https://data.cdc.gov/api/views/95ax-ymtc",
+            "description": "Data on drug overdose death rates, by drug type and selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Vital Statistics System, numerator data from annual public-use Mortality Files; denominator data from U.S. Census Bureau national population estimates; and Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B. Deaths: Final data for 2018. National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: National Center for Health Statistics.2021. Available from: https://www.cdc.gov/nchs/products/nvsr.htm. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
+            "title": "Drug overdose death rates, by drug type, sex, age, race, and Hispanic origin: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/6yz5-ufy2",
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
+            "identifier": "https://data.cdc.gov/api/views/6yz5-ufy2",
+            "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/msaviewer/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6iwu-fbds",
+            "description": "An interactive Web application that enables users to visualize multiple alignments created by database search results or other software applications. The MSA Viewer allows users to upload an alignment and set a master sequence and to explore the data using features such as zooming and changing of coloration.",
+            "title": "Multiple Sequence Alignment (MSA) Viewer",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/tools/msaviewer/",
+                    "mediaType": "text/html",
+                    "title": "Multiple Sequence Alignment (MSA) Viewer"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/tools/msaviewer/embedding-api/",
+                    "description": "The NCBI Multiple Sequence (MSA) Alignment Viewer is a general purpose tool for viewing multiple alignments of biological sequences. It can be embedded in a wide variety of web pages and with a large number of options.",
+                    "@type": "dcat:Distribution",
+                    "title": "Multiple Sequence Alignment Viewer Embedding API"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/g995-q4wt",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-06-08",
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
+            "identifier": "622fd82e-d2cb-5204-9a97-ba4df56ffcc6",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_files_allDownloadsSSBtn",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/files_allDownloadsSSBtn.csv",
+                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "files_allDownloadsSSBtn csv file"
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
+            "landingPage": "https://www.healthit.gov/data/datasets/state-health-it-policy-levers-activities-catalog",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2015-12-01",
+            "references": [
+                "https://www.healthit.gov/data/apps/state-health-it-policy-levers-compendium"
+            ],
+            "keyword": [
+                "ehr",
+                "health information exchange",
+                "health information technology",
+                "health it",
+                "patient engagement",
+                "state health it policies",
+                "state hie"
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
+            "identifier": "exxucmj0-ey0t-ofmw-ehjp-yknmz432m3og",
+            "description": "The Health IT State Policy Levers Compendium was developed by the Office of National Coordinator for Health Information Technology (ONC) in coordination with states. It is intended to support state efforts to advance interoperability and can also be used in service of delivery system reform. The Compendium includes a directory of health IT policy levers and nearly 300 examples of how states have used them. The 'Activities Catalog' includes the over 300 documented examples of health IT policy levers in use by states. The catalog data includes the states using the policy lever to promote health IT and advance interoperability, the state's documented activities, and official information source for these activities.",
+            "title": "State Health IT Policy Levers Activities Catalog",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/policy-levers-activities-catalog.csv",
+                    "mediaType": "text/csv",
+                    "title": "policy-levers-activities-catalog.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/state-health-it-policy-levers-activities-catalog"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/bw3b-karf",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "chapare virus",
+                "crimean-congo hemorrhagic fever virus",
+                "ebola virus",
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
+            "identifier": "https://data.cdc.gov/api/views/bw3b-karf",
+            "description": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Chapare virus to Ebola virus \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Chapare virus to Ebola virus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-vaccine-adverse-event-reporting-system-vaers",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1990-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "adverse event",
+                "aefi",
+                "age",
+                "immunization",
+                "manufacturer",
+                "medra",
+                "month",
+                "onset",
+                "outcome",
+                "population statistics",
+                "report date",
+                "safety",
+                "sex",
+                "side effect",
+                "state",
+                "symptom",
+                "territory",
+                "vaccination date",
+                "vaccine",
+                "vaers",
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
+            "identifier": "2761a3aa-c892-4e95-bece-7902cff70133",
+            "description": "<p>The Vaccine Adverse Event Reporting System (VAERS) online database on CDC WONDER provides counts and percentages of adverse event case reports after vaccination, by symptom, vaccine product, manufacturer, onset interval, outcome category, year and month vaccinated, year and month reported, age, sex and state / territory. The Vaccine Adverse Event Reporting System is a cooperative program for vaccine safety of the Centers for Disease Control and Prevention (CDC) and the Food and Drug Administration (FDA). VAERS is a post-marketing safety surveillance program, collecting information about adverse events (possible side effects) that occur after the administration of US licensed vaccines.  Data are from the US Department of Health and Human Services (DHHS), Public Health Service (PHS), Food and Drug Administration (FDA)/ Centers for Disease Control (CDC), Vaccine Adverse Event Reporting System (VAERS).</p>",
+            "title": "CDC WONDER: Vaccine Adverse Event Reporting System (VAERS)",
+            "programCode": [
+                "009:011"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/vaers.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/vaers.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "009:20"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qzjj-q36s",
+            "issued": "2022-03-30",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-30",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kayla Janos",
+                "hasEmail": "mailto:qrw4@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/qzjj-q36s",
+            "description": "not for public use",
+            "title": "testing_cte_aspost",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qzjj-q36s/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qzjj-q36s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qzjj-q36s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qzjj-q36s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/child-coverage-vaccination.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-10-23",
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
+            "identifier": "https://data.cdc.gov/api/views/skkh-jsrk",
+            "description": "\u2022 Weekly Cumulative Percentage of Children 6 Months\u201317 Years Who Are Up to Date with COVID-19 Vaccines by Selected Demographics and by Season.\n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey\u2013Child COVID Module (NIS\u2013CCM). The NIS\u2013CCM was discontinued at the end of 2023 and questions regarding COVID-19 vaccination status and intent were added to the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html).\n\n\u2022 Please note, weekly estimates for children 6 months to 4 years and 5 to 11 years from January-June 2024 have been updated due to a mistake in age group coding.",
+            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to date with COVID-19 Vaccines by Selected Demographics and by Season, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/skkh-jsrk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/skkh-jsrk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/skkh-jsrk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/skkh-jsrk/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/valuing-invaluable-2011-update-growing-contributions-and-costs-family-caregiving",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2014-07-22",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "caregiver",
+                "caregiving",
+                "economic value",
+                "eldercare",
+                "elderly",
+                "healthcare",
+                "seniors"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Claudia Williams",
+                "hasEmail": "mailto:Claudia_H_Williams@ostp.eop.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "identifier": "f5545353-28ba-4e82-a0ca-164560d9eb2a",
+            "description": "<p>This report estimates the economic value of family caregiving at $450 billion in 2009 based on 42.1 million caregivers age 18 or older providing an average of 18.4 hours of care per week to care recipients age 18 or older, at an average value of $11.16 per hour.</p>\n<p><strong><em>This data is not collected by a government agency.  The findings and conclusions in this report are those of the author and do not necessarily represent the views of the Department of Health &amp; Human Services.</em></strong></p>",
+            "title": "Long-Term Care Calculator: Compare Costs, Types of Service in Your Area",
+            "programCode": [
+                "009:015"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/5wdd-3g8t",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/5wdd-3g8t",
+            "description": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022\tNotices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\nFootnotes:\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5wdd-3g8t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5wdd-3g8t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5wdd-3g8t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5wdd-3g8t/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/dqgu-gg5d",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-11-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-31",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Immunization Safety Office",
+                "hasEmail": "mailto:vsafe@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/dqgu-gg5d",
+            "description": "Users of the v-safe data are required to adhere to the following standards for the analysis and reporting of research data. All research results must be presented and/or published in a manner that protects the confidentiality of participants. v-safe data will not be presented and/or published in any way in which an individual can be identified. \n\nTherefore, users will:\n<ol>\n<li>Not attempt to link or permit others to link the data with individually identified records in another database.</li>\n<li>Not attempt to learn the identity of any participant in the data and will not deliberately combine these data with other CDC or non-CDC data for the purpose of matching records to identify individuals. If you should inadvertently discover the identity of any participant, you will ensure the identity of any participant is kept confidential, and will not be used in any publications and/or presentations.</li>\n<li>Not imply or state, either in written or oral form, that interpretations based on analysis of the data reflect official CDC policies or positions.</li>\n<li>Understand that sub-national analyses are not appropriate for this national sample and will not be conducted. </li>\n<li>Understand that v-safe is a voluntary self-enrollment program requiring smartphone access; therefore, information from v-safe might not be representative or generalizable to the US population.</li></ol>\nBy clicking on the weblink below to download and use these v-safe data, you signify your agreement to comply with the above-stated terms.\n\nv-safe is an active surveillance program to monitor the safety of COVID-19 vaccines during the period when the vaccines are authorized for use under Food and Drug Administration (FDA) Emergency Use Authorization (EUA) and after vaccine licensure. \n \nThese data include registrant information (deidentified), health check-in, and vaccination data collected through v-safe from 12/13/2020 to 06/30/2023. Please review the v-safe data user agreement before analyzing any v-safe data.",
+            "title": "v-safe COVID-19",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/dqgu-gg5d/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/2vtj-68zm",
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
+            "identifier": "https://data.cdc.gov/api/views/2vtj-68zm",
+            "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vtj-68zm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vtj-68zm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vtj-68zm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vtj-68zm/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/qjju-smys",
+            "bureauCode": [
+                "009:032"
+            ],
+            "issued": "2018-06-15",
+            "@type": "dcat:Dataset",
+            "modified": "2018-11-27",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter"
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
+            "identifier": "https://data.cdc.gov/api/views/qjju-smys",
+            "description": "This dataset provides modeled predictions of particulate matter (PM2.5) levels from the EPA's Downscaler model. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Data are at the county levels for 2001-2014. The dataset includes the maximum, median, mean, and population-weighted mean concentration. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
+            "title": "Daily County-Level PM2.5 Concentrations, 2001-2014",
+            "programCode": [
+                "009:20"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjju-smys/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjju-smys/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjju-smys/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjju-smys/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/gdw9-dep3",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
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
+            "identifier": "2226672d-d505-49ae-9853-1049b53722df",
+            "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
+            "title": "Network PUF - PY2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/network_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/ge4b-j6f6",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-12-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-16",
+            "keyword": [
+                "bho",
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
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "e2ce0d2f-07c5-5213-947a-31e19bc649f6",
+            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Because Medicaid beneficiaries may be enrolled concurrently in more than one type of managed care program (e.g., a Comprehensive MCO and a BHO), users should not sum enrollment across all program types, since the total would count individuals more than once and, in some states, exceed the actual number of Medicaid enrollees.\r\n\r\n2. Comprehensive MCOs cover acute, primary, and specialty medical care services; they may also cover behavioral health, long-term services and supports, and other benefits in some states. Limited benefit managed care programs, including PCCM, MLTSS only, BHO, Dental, Transportation, and Other cover a narrower set of services.\r\n\r\n3.  The \u201cTotal Medicaid Enrollees\u201d column represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including Medicaid-only and dually eligible individuals receiving full Medicaid benefits or Medicaid cost sharing.\r\n\r\n\"--\" indicates states that do not operate programs of a given type. 0 signifies that a state operated a program of this type in 2014, but it ended before July 1, 2014, or began after that date.",
+            "title": "Managed Care Enrollment by Program and Population (All)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-population-all-2022-tab2.csv",
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
+            "landingPage": "https://data.cdc.gov/d/62d6-pm5i",
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
+                "mask mandates",
+                "masks",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "social distancing"
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
+            "identifier": "https://data.cdc.gov/api/views/62d6-pm5i",
+            "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when members of the public in states and territories were subject to state and territorial executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require them to wear masks in public. \u201cMembers of the public\u201d are defined as individuals operating in a personal capacity. \u201cIn public\u201d is defined to mean either (1) anywhere outside the home or (2) both in retail businesses and in restaurants/food establishments. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level. \n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require individuals to wear masks in public found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program, and Max Gakh, Assistant Professor, School of Public Health, University of Nevada, Las Vegas from April 10, 2020 through August 15, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the dates provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not include data on counties that have opted out of their state mask mandate pursuant to state law. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
+            "title": "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through August 15, 2021 by County by Day",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/geqt-uwhp",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2025-01-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-30",
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
+            "identifier": "f7420ebf-7bd1-44de-b2a4-07c6ec9c28ac",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-23-2024-to-12-29-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-12-23-2024-to-12-29-2024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://catalog.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "books",
+                "library services",
+                "literature"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/f3sh-4v4q",
+            "description": "A MARC-based catalog, the LocatorPlus Catalog provides access to NLM bibliographic data for journals, books, audiovisuals, computer software, electronic resources and other materials.",
+            "title": "LocatorPlus",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://catalog.nlm.nih.gov/",
+                    "mediaType": "text/html",
+                    "title": "Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://support.nlm.nih.gov/knowledgebase/article/KA-04188/en-us",
+                    "description": "Retrieving NLM bibliographic records from the LocatorPlus Catalog via Z39.50",
+                    "@type": "dcat:Distribution",
+                    "title": "Alma - Z39.50 Protocol"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Literature"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2009",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2009)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2009) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/lack-socialconnection.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-21",
+            "temporal": "2024-02-05/2024-09-16",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-04",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mnaa-qctp",
+            "description": "In 2020, the National Center for Health Statistics (NCHS) partnered with the Census Bureau on an experimental data system called the Household Pulse Survey. This survey was designed to complement the ability of the federal statistical system to rapidly respond and provide relevant information about how emergent issues are impacting American households. Beginning in Phase 4.0 (on January 9, 2024), questions on social support, loneliness, and social isolation were added to the survey. These questions have been included on other nationally representative surveys. Briefly, the question on social support was included on the National Health Interview Survey (NHIS) from July 2020-December 2021 and was added to the 2024 NHIS. The question on loneliness was added to the 2024 NHIS. The questions on social isolation are adapted from the Berkman-Syme Social Network Index and were included on an earlier cycle of the National Health and Nutrition Examination Survey. For more information, please visit: https://www.cdc.gov/nchs/covid19/pulse/lack-socialconnection.htm",
+            "title": "Lack of Social Connection",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "monthly",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
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
+            "identifier": "https://data.cdc.gov/api/views/ui6g-vumy",
+            "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Services and Profiles dataset provides an overview of clinic services, the clinic\u2019s contact information, location, the medical director\u2019s name, and summary statistics.",
+            "title": "2021 Final Assisted Reproductive Technology (ART) Services and Profiles",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ui6g-vumy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ui6g-vumy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ui6g-vumy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ui6g-vumy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Se/ui6g-vumy",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Assisted Reproductive Technology (ART)"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/vuhn-dxkt",
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
+                "nonparalytic",
+                "poliovirus infection",
+                "psittacosis",
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
+            "identifier": "https://data.cdc.gov/api/views/vuhn-dxkt",
+            "description": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vuhn-dxkt/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vuhn-dxkt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vuhn-dxkt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vuhn-dxkt/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/9mw4-6adp",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-09-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-02",
+            "keyword": [
+                "asd",
+                "autism",
+                "autism prevalence",
+                "autism spectrum disorder",
+                "prevalence studies"
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
+            "identifier": "https://data.cdc.gov/api/views/9mw4-6adp",
+            "description": "This data table provides a collection of information from peer-reviewed autism prevalence studies. Information reported from each study includes the autism prevalence estimate and additional study characteristics (e.g., case ascertainment and criteria). A PubMed search was conducted to identify studies published at any time through September 2020 using the search terms: autism (title/abstract) OR autistic (title/abstract) AND prevalence (title/abstract). Data were abstracted and included if the study fulfilled the following criteria: \n\u2022\tThe study was published in English; \n\u2022\tThe study produced at least one autism prevalence estimate; and\n\u2022\tThe study was population-based (any age range) within a defined geographic area.",
+            "title": "autism prevalence studies",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "Annually",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/about_ahcd.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "issued": "2022-11-16",
+            "@type": "dcat:Dataset",
+            "temporal": "1973-1981, 1985, 1989-2019",
+            "modified": "2023-11-21",
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/"
+            ],
+            "keyword": [
+                "ambulatory-care",
+                "namcs",
+                "office-based physicians",
+                "physician office visits",
+                "physicians",
+                "visit characteristics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:Ambcare@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/bkbr-drkm",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) is a national survey designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. Findings are based on a sample of visits to non-federally employed office-based physicians who are primarily engaged in direct patient care. Physicians in the specialties (including designated sub-specialties) of anesthesiology, pathology, and radiology are excluded from the survey. The survey was conducted annually from 1973 to 1981, again in 1985, and annually since 1989. \nData collection from the physician, rather than from the patient, provides an analytic base that expands information on ambulatory care collected through other NCHS surveys. Data about the physician and their practice characteristics are collected during a survey induction interview.\nFor survey years 1973 to 1991, there are two data files: one for patient visit data and a second for drug mention data. The second file is limited to those visits with mention of medication therapy. For the 1991 data, it is possible to link information on the drug file with information on the patient visit file. Beginning with the 1992 survey year through 2011, one main data file was produced annually that contains both patient visit and drug information.",
+            "title": "National Ambulatory Medical Care Survey, Public-use file, 1973-2019",
+            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NAMCS/",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/",
+                    "description": "First link: NAMCS public-use data, 1973-1992\nSecond link: NAMCS public-use data, 1993-2016, 2018, 2019",
+                    "@type": "dcat:Distribution",
+                    "title": "NAMCS public-use data"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NAMCS/",
+                    "description": "First link: NAMCS public-use data, 1973-1992\nSecond link: NAMCS public-use data, 1993-2016, 2018, 2019",
+                    "@type": "dcat:Distribution",
+                    "title": "NAMCS public-use data"
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
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/namcs_hc.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "Public access",
+            "issued": "2024-07-24",
+            "@type": "dcat:Dataset",
+            "temporal": "2022",
+            "modified": "2024-07-24",
+            "keyword": [
+                "ambulatory-care",
+                "health center",
+                "health center component",
+                "health center encounter",
+                "namcs"
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
+            "identifier": "https://data.cdc.gov/api/views/wj2j-rzx9",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component, conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to health centers to describe patterns of utilization and provision of ambulatory care delivery in the United States. Health centers are local clinics that are community-based and provide comprehensive health care services to populations that are often vulnerable and underserved. Health centers are either federally qualified health centers (FQHCs), which receive federal funding from the Health Resources and Services Administration (HRSA), or FQHC look-alikes, which meet HRSA requirements but do not receive HRSA funding.",
+            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2022, Public-use file",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/nchs/ahcd/namcs_hc.htm",
+                    "description": "R, SAS, and STATA data files are readily available.",
+                    "@type": "dcat:Distribution",
+                    "title": "2022 NAMCS Health Center Component"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS_HC/2022/2022-NAMCS-HCC-PUF-Codebook-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS_HC/2022/2022-NAMCS-HCC-PUF-Tech-Doc-508.pdf",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
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
+            "identifier": "https://data.cdc.gov/api/views/tid6-xphm",
+            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
+            "title": "Quitline \u2013 Quitline Names and Phone Numbers",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tid6-xphm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tid6-xphm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tid6-xphm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tid6-xphm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Quitline-Names-and-Phone-Numbers/tid6-xphm",
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
+            "issued": "2021-05-12",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2020-12-31",
+            "modified": "2022-04-01",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
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
+            "identifier": "https://data.cdc.gov/api/views/75vb-d79q",
+            "description": "Provisional count of deaths involving coronavirus disease 2019 (COVID-19) by United States county of residence, from January 1, 2020 through December 31, 2020.",
+            "title": "AH County of Residence COVID-19 Deaths Counts, 2020 Provisional",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/index_2020.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-09-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2020-12-31",
+            "modified": "2022-09-01",
+            "keyword": [
+                "deaths",
+                "life expectancy",
+                "mortality",
+                "nchs",
+                "nvss",
+                "sex",
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
+            "identifier": "https://data.cdc.gov/api/views/ss2j-8ajj",
+            "description": "The dataset presents life expectancy at birth estimates based on annual complete period life tables for each of the 50 states and the District of Columbia (D.C.)\nin 2020 for the total, male and female populations.",
+            "title": "U.S. State Life Expectancy by Sex, 2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ss2j-8ajj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ss2j-8ajj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ss2j-8ajj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ss2j-8ajj/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/gk4r-hamn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-16",
+            "keyword": [
+                "business rules",
+                "exchange puf",
+                "marketplace puf",
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
+            "identifier": "ab6b8ea6-fdd8-4eb6-9fe6-7a93aca92b46",
+            "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
+            "title": "Business Rules PUF - PY2023",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/business_rules_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-06-26",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-24",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "RESP-NET",
+                "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/6jg4-xsqq",
+            "description": "The Coronavirus Disease 2019 (COVID-19) Hospitalization Surveillance Network (COVID-NET) a network that conducts active, population-based surveillance for laboratory-confirmed COVID-19-associated hospitalizations among children and adults. COVID-NET, along with the Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) and the Influenza Hospitalization Surveillance Network (FluSurv-NET), comprise the Respiratory Virus Hospitalization Surveillance Network (RESP-NET). The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. COVID-NET is CDC\u2019s source for important data on rates of hospitalizations associated with COVID-19. Hospitalization rates show how many people in the surveillance area are hospitalized with COVID-19, compared to the total number of people residing in that area. \n\nData are preliminary and subject to change as more data become available. Data will be updated weekly.",
+            "title": "Weekly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System",
+            "programCode": [
+                "009:038"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-10",
+            "references": [
+                "https://chronicdata.cdc.gov/d/5qag-uzp2"
+            ],
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "state system",
+                "tax",
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
+            "identifier": "https://data.cdc.gov/api/views/2dwv-vfam",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation-Tax. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state taxes on combustible (cigarettes, cigars, little cigars, pipe tobacco, and roll-your-own tobacco) tobacco products, non-combustible (snus, moist snuff, dry snuff, chewing tobacco) tobacco products, and tax stamps.",
+            "title": "CDC STATE System Tobacco Legislation - Tax",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2dwv-vfam/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2dwv-vfam/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2dwv-vfam/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2dwv-vfam/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Tax/2dwv-vfam",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/vqyf-z2g3",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/vqyf-z2g3",
+            "description": "NNDSS - TABLE 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\nFootnotes:\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.",
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vqyf-z2g3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vqyf-z2g3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vqyf-z2g3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vqyf-z2g3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/gngx-pf4v",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-05-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-05-07",
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
+            "identifier": "4b7403de-2d4b-5b0e-a3c3-af9e6a0152d7",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/MEASURE_VALUE.csv",
+                    "description": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)"
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
+            "landingPage": "https://data.cdc.gov/d/hrdz-jaxc",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-03-01/2023-11-24",
+            "modified": "2025-01-13",
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
+            "identifier": "https://data.cdc.gov/api/views/hrdz-jaxc",
+            "description": "<b>Note:</b>\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis table summarizes COVID-19 case and death data submitted to CDC as case reports for the line-level dataset. Case and death counts are stratified according to sex, age, and race and ethnicity at regional and national levels. Data for US territories are included in case and death counts, but not population counts. Weekly cumulative counts with five or fewer cases or deaths are not reported to protect confidentiality of patients. Records with unknown or missing sex, age, or race and ethnicity and of multiple, non-Hispanic race and ethnicity are included in case and death totals. COVID-19 case and death data are provisional and are subject to change. Visualization of COVID-19 case and death rate trends by demographic variables may be viewed on COVID Data Tracker (<a href=\"https://covid.cdc.gov/covid-data-tracker/#demographicsovertime\">https://covid.cdc.gov/covid-data-tracker/#demographicsovertime</a>).",
+            "title": "COVID-19 Weekly Cases and Deaths by Age, Race/Ethnicity, and Sex - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.xml?accessType=DOWNLOAD",
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
+                "hispanic origin",
+                "live birth rate",
+                "marital status",
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
+            "identifier": "https://data.cdc.gov/api/views/7pcd-2tnr",
+            "description": "https://www.cdc.gov/nchs/data-visualization/births-to-unmarried-women/index.htm",
+            "title": "NCHS - Pregnancy and Live Birth Rates, by Marital Status and Race and Hispanic Origin: United States, 1990-2010",
+            "isPartOf": "NCHS - Pregnancy and Live Birth Rates, by Marital Status and Race and Hispanic Origin: United States, 1990-2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/cw4r-vcr3",
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
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli (stec)",
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
+            "identifier": "https://data.cdc.gov/api/views/cw4r-vcr3",
+            "description": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2000",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2000)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2000) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/n3wf-wtep",
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
+                "shiga toxin-producing e. coli",
+                "shigellosis",
+                "stec",
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
+            "identifier": "https://data.cdc.gov/api/views/n3wf-wtep",
+            "description": "NNDSS - Table II. Shiga toxin to Shigellosis - 2015.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Includes E. coli O157:H7; Shiga toxin-positive, serogroup non-O157; and Shiga toxin-positive, not serogrouped.",
+            "title": "NNDSS - Table II. Shiga toxin to Shigellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-bridged-race-july-1st-estimates",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1990-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "age",
+                "county",
+                "ethnicity",
+                "population",
+                "population statistics",
+                "race",
+                "sex",
+                "state",
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
+            "identifier": "7461968e-5c85-451b-a38b-26c540c7b802",
+            "description": "<p>The Population - Bridged-Race July 1st Estimates online databases report bridged-race population estimates of the July 1st resident population of the United States, based on Census 2000 counts, for use in calculating vital rates. These estimates result from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) standards for the collection of data on race and ethnicity, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White). Many data systems, such as vital statistics, are continuing to use the 1977 OMB standards during the transition to full implementation of the 1997 OMB standards. Postcensal estimates are available for year 2000 - 2009; intercensal estimates are available for the years 1990-1999.  Obtain population counts by  Year, State, County, Race (4-categories), Ethnicity, Sex and Age (1-year or 5-year groups).   The data are released by the National Center for Health Statistics.</p>",
+            "title": "CDC WONDER: Population - Bridged-Race July 1st Estimates",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/bridged-race-population.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
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
+            "identifier": "https://data.cdc.gov/api/views/xx8k-iu94",
+            "description": "This dataset contains model-based place (incorporated and census designated places) estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia \u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 36 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
+            "title": "PLACES: Place Data (GIS Friendly Format), 2023 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/gr95-7mnn",
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
+            "identifier": "8a655f73-c702-571c-9bb0-f100c4323e5d",
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
+            "landingPage": "https://data.cdc.gov/d/ahrf-yqdt",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "N/A",
+            "issued": "2024-10-04",
+            "@type": "dcat:Dataset",
+            "temporal": "October 1, 2024 - no specified end date",
+            "modified": "2025-01-17",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "disease burden",
+                "hospitalizations",
+                "illnesses",
+                "outpatient visits"
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
+            "identifier": "https://data.cdc.gov/api/views/ahrf-yqdt",
+            "description": "This dataset represents preliminary estimates of cumulative U.S. COVID-19 disease burden for the 2024-2025 period, including illnesses, outpatient visits, hospitalizations, and deaths. The weekly COVID-19-associated burden estimates are preliminary and based on continuously collected surveillance data from patients hospitalized with laboratory-confirmed severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) infections. The data come from the Coronavirus Disease 2019 (COVID-19)-Associated Hospitalization Surveillance Network (COVID-NET), a surveillance platform that captures data from hospitals that serve about 10% of the U.S. population. Each week CDC estimates a range (i.e., lower estimate and an upper estimate) of COVID-19 -associated burden that have occurred since October 1, 2024. \n\n<b>Note:</b> Data are preliminary and subject to change as more data become available. Rates for recent COVID-19-associated hospital admissions are subject to reporting delays; as new data are received each week, previous rates are updated accordingly.\n\n<b>References</b>\n<ol><li>Reed C, Chaves SS, Daily Kirley P, et al. Estimating influenza disease burden from population-based surveillance data in the United States. PLoS One. 2015;10(3):e0118369. https://doi.org/10.1371/journal.pone.0118369\u202f </li><li>Rolfes, MA, Foppa, IM, Garg, S, et al. Annual estimates of the burden of seasonal influenza in the United States: A tool for strengthening influenza surveillance and preparedness. Influenza Other Respi Viruses. 2018; 12: 132\u2013 137. https://doi.org/10.1111/irv.12486</li><li>Tokars  JI, Rolfes  MA, Foppa  IM, Reed  C.  An evaluation and update of methods for estimating the number of influenza cases averted by vaccination in the United States.   Vaccine. 2018;36(48):7331-7337. doi:10.1016/j.vaccine.2018.10.026\u202f</li><li>Collier SA, Deng L, Adam EA, Benedict KM, Beshearse EM, Blackstock AJ, Bruce BB, Derado G, Edens C, Fullerton KE, Gargano JW, Geissler AL, Hall AJ, Havelaar AH, Hill VR, Hoekstra RM, Reddy SC, Scallan E, Stokes EK, Yoder JS, Beach MJ. Estimate of Burden and Direct Healthcare Cost of Infectious Waterborne Disease in the United States. Emerg Infect Dis. 2021 Jan;27(1):140-149. doi: 10.3201/eid2701.190676. PMID: 33350905; PMCID: PMC7774540.</li><li>Reed C, Kim IK, Singleton JA,\u202f et al. Estimated influenza illnesses and hospitalizations averted by vaccination\u2013United States, 2013-14 influenza season. MMWR Morb Mortal Wkly Rep. 2014 Dec 12;63(49):1151-4. https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6349a2.htm\u202f</li><li>Reed C, Angulo FJ, Swerdlow DL, et al. Estimates of the Prevalence of Pandemic (H1N1) 2009, United States, April\u2013July 2009. Emerg Infect Dis. 2009;15(12):2004-2007. https://dx.doi.org/10.3201/eid1512.091413 \u202f</li><li>Devine O, Pham H, Gunnels B, et al. Extrapolating Sentinel Surveillance Information to Estimate National COVID-19 Hospital Admission Rates: A Bayesian Modeling Approach. Influenza and Other Respiratory Viruses. https://onlinelibrary.wiley.com/doi/10.1111/irv.70026. Volume18, Issue10. October 2024.</li><li><a ref=\"https://www.cdc.gov/covid/php/covid-net/index.html\">COVID-NET | COVID-19 | CDC\u202f</a></li><li>https://www.cdc.gov/covid/hcp/clinical-care/systematic-review-process.html\u202f </li><li><a ref=\"https://academic.oup.com/pnasnexus/article/1/3/pgac079/6604394?login=false\">Excess natural-cause deaths in California by cause and setting: March 2020 through February 2021 | PNAS Nexus | Oxford Academic (oup.com)</a></li><li>Kruschke, J. K. 2011. Doing Bayesian data analysis: a tutorial with R and BUGS. Elsevier, Amsterdam, Section 3.3.5.</li></ol>",
+            "title": "Preliminary 2024-2025 U.S. COVID-19 Burden Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/grua-wsci",
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
+            "identifier": "9dcfc4fd-2d71-55fc-bd59-7b7524186c88",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard measure_value v2.11.18 (etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/measure_value.csv",
+                    "description": "Scorecard measure_value v2.11.18 (etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure_value v2.11.18 (etl-test)"
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
+            "landingPage": "https://data.cdc.gov/d/xv7k-8e7s",
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
+                "shiga toxin-producing e. coli",
+                "shigellosis",
+                "stec",
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
+            "identifier": "https://data.cdc.gov/api/views/xv7k-8e7s",
+            "description": "NNDSS - Table II. Shiga toxin to Shigellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.   Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n \r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.   Data for TB are displayed in Table IV, which appears quarterly.  \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table II to facilitate case count verification with reporting jurisdictions.\r\n\u00a7 Includes E. coli O157:H7; Shiga toxin-positive, serogroup non-O157; and Shiga toxin-positive, not serogrouped.",
+            "title": "NNDSS - Table II. Shiga toxin to Shigellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/prov-county-drug-overdose.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-10-05",
+            "@type": "dcat:Dataset",
+            "temporal": "2015-01-01/2024-06-30",
+            "modified": "2025-01-15",
+            "keyword": [
+                "county",
+                "deaths",
+                "drug",
+                "drug overdose",
+                "monthly",
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
+            "identifier": "https://data.cdc.gov/api/views/gb4e-yj24",
+            "description": "This data visualization presents county-level provisional counts for drug overdose deaths based on a current flow of mortality data in the National Vital Statistics System. County-level provisional counts include deaths occurring within the 50 states and the District of Columbia, as of the date specified and may not include all deaths that occurred during a given time period. Provisional counts are often incomplete and causes of death may be pending investigation resulting in an underestimate relative to final counts (see Technical Notes).\n\nThe provisional data presented on the dashboard below include reported 12 month-ending provisional counts of death due to drug overdose by the decedent\u2019s county of residence and the month in which death occurred.\n\nPercentages of deaths with a cause of death pending further investigation and a note on historical completeness (e.g. if the percent completeness was under 90% after 6 months) are included to aid in interpretation of provisional data as these measures are related to the accuracy of provisional counts (see Technical Notes). Counts between 1-9 are suppressed in accordance with NCHS confidentiality standards. Provisional data presented on this page will be updated on a quarterly basis as additional records are received.\n\nTechnical Notes\n\nNature and Sources of Data\n\nProvisional drug overdose death counts are based on death records received and processed by the National Center for Health Statistics (NCHS) as of a specified cutoff date. The cutoff date is generally the first Sunday of each month. National provisional estimates include deaths occurring within the 50 states and the District of Columbia. NCHS receives the death records from the state vital registration offices through the Vital Statistics Cooperative Program (VSCP).\n\nThe timeliness of provisional mortality surveillance data in the National Vital Statistics System (NVSS) database varies by cause of death and jurisdiction in which the death occurred. The lag time (i.e., the time between when the death occurred and when the data are available for analysis) is longer for drug overdose deaths compared with other causes of death due to the time often needed to investigate these deaths (1). Thus, provisional estimates of drug overdose deaths are reported 6 months after the date of death.\n\nProvisional death counts presented in this data visualization are for \u201c12 month-ending periods,\u201d defined as the number of deaths occurring in the 12 month period ending in the month indicated. For example, the 12 month-ending period in June 2020 would include deaths occurring from July 1, 2019 through June 30, 2020. The 12 month-ending period counts include all seasons of the year and are insensitive to reporting variations by seasonality. These provisional counts of drug overdose deaths and related data quality metrics are provided for public health surveillance and monitoring of emerging trends. Provisional drug overdose death data are often incomplete, and the degree of completeness varies by jurisdiction and 12 month-ending period. Consequently, the numbers of drug overdose deaths are underestimated based on provisional data relative to final data and are subject to random variation.\n\nCause of Death Classification and Definition of Drug Deaths\n\nMortality statistics are compiled in accordance with the World Health Organizations (WHO) regulations specifying that WHO member nations classify and code causes of death with the current revision of the International Statistical Classification of Diseases and Related Health Problems (ICD). ICD provides the basic guidance used in virtually all countries to code and classify causes of death. It provides not only disease, injury, and poisoning categories but also the rules used to select the single underlying cause of death for tabulation from the several diagnoses that may be reported on a single death certificate, as well as definitions, tabulation lists, the format of the death certificate, and regul",
+            "title": "VSRR Provisional County-Level Drug Overdose Death Counts",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-10-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2024-2025",
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
+            "identifier": "https://data.cdc.gov/api/views/ph8r-wzxn",
+            "description": "\u2022 Weekly Cumulative Doses (in Millions) of Influenza Vaccines Distributed by Season in the United States. \n\n\u2022 Archived data are available here: https://data.cdc.gov/resource/e5zk-7tx5\n\n\u2022 Influenza vaccine is produced by private manufacturers. Additional information is available at https://www.cdc.gov/flu/prevent/vaccine-supply-distribution.htm. These data are submitted to CDC by current U.S.\u2500 licensed manufacturers of influenza vaccine and a subset of influenza vaccine wholesalers and distributors that receive vaccine directly from these manufacturers. These data are not projected but approximate all influenza vaccines distributed in the United States.\n\n\u2022 Additional information is available:\u202fhttps://www.cdc.gov/flu/prevent/vaccine-supply-distribution.htm.",
+            "title": "Weekly Cumulative Doses (in Millions) of Influenza Vaccines Distributed by Season, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ph8r-wzxn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ph8r-wzxn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ph8r-wzxn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ph8r-wzxn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
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
+            "landingPage": "https://data.cdc.gov/d/r9mz-pvtk",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
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
+            "identifier": "https://data.cdc.gov/api/views/r9mz-pvtk",
+            "description": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\n\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r9mz-pvtk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r9mz-pvtk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r9mz-pvtk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r9mz-pvtk/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2011-02-01",
+            "keyword": [
+                "community health",
+                "drug",
+                "fda",
+                "label",
+                "label repository",
+                "labels fda gov"
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
+            "identifier": "c447002d-51df-46d9-a105-dda94dfd6083",
+            "description": "This file contains the data elements used for searching the FDA Online Data Repository including proprietary name, active ingredients, marketing application number or regulatory citation, National Drug Code, and company name.",
+            "title": "FDA Drug Label Data",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/ucm241597.zip",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mwkk-wzmy",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "confirmed",
+                "hepatitis b",
+                "hepatitis c acute",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
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
+            "identifier": "https://data.cdc.gov/api/views/mwkk-wzmy",
+            "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/7xvh-y5vh",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-09-10",
+            "@type": "dcat:Dataset",
+            "modified": "2021-09-10",
+            "keyword": [
+                "covid-19",
+                "executive order",
+                "gathering bans",
+                "government order",
+                "legal epidemiology",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "social distancing"
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
+            "identifier": "https://data.cdc.gov/api/views/7xvh-y5vh",
+            "description": "State and territorial executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications are collected from government websites and cataloged and coded using Microsoft Excel by one or more coders with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states and territories were subject to executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications related to  COVID-19 banning gatherings of various sizes either (1) generally, or specified that the gathering limit applied only when social distancing was not possible, or (2) even if participants practiced social distancing.\n\nThese data are derived from on the publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly ban gatherings found by the CDC, COVID-19 Community Intervention and Critical Populations Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through August 15, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded, as well as official government communications such as announcements that counties have progressed through new phases of reopening pursuant to an executive order, directive, or other executive branch action, and posted to government websites; news media reports on restrictions were excluded. Recommendations and guidance documents not included or adopted by reference in an order are not included in these data. These data do not include mandatory business closures, curfews, or requirements/recommendations for people to stay in their homes. Due to limitations of the National Environmental Public Health Tracking Network Data Explorer, these data do not include tribes or cities, nor was a distinction made between county orders that applied county-wide versus those that were limited to unincorporated areas of the county. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
+            "title": "U.S. State and Territorial Gathering Bans: March 11, 2020-August 15, 2021 by County by Day",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/guzr-wp6x",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2018-07-11",
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
+            "identifier": "927f4847-2c0a-50c1-8f50-9103de7d048b",
+            "description": "Number of Managed Care Programs Enrolling Certain Populations on a Mandatory or Voluntary Basis at any point in 2022",
+            "title": "Managed Care Features By Enrollment Population",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-features-by-enrollment-population.2022.csv",
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
+            "landingPage": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-04-03",
+            "@type": "dcat:Dataset",
+            "temporal": "2020",
+            "modified": "2024-05-02",
+            "references": [
+                "https://www.cdc.gov/nchs/data/nhcs/2020-NHCS-PUF-Tech-Doc-508.pdf"
+            ],
+            "keyword": [
+                "electronic health records",
+                "emergency departments",
+                "healthcare",
+                "hospital",
+                "inpatient",
+                "inpatient department",
+                "nhcs",
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
+            "identifier": "https://data.cdc.gov/api/views/jdch-es95",
+            "description": "As a principal source of information on health care utilization in the United States, NHCS collects inpatient and emergency department data from a nationally representative sample of U.S. hospitals sourced from administrative and electronic health records data. The 2020 NHCS is conducted by the National Center for Health Statistics (NCHS) and is a member of the National Health Care Surveys \u2013 a family of surveys which measure health care utilization across a variety of health care providers and settings.",
+            "title": "National Hospital Care Survey, 2020 public-use file",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+                    "description": "Inpatient and emergency department datasets are available for SAS, STATA, AND R at the link below.",
+                    "@type": "dcat:Distribution",
+                    "title": "2020 NATIONAL HOSPITAL CARE SURVEY"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-INPATIENT-CODEBOOK-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-ED-CODEBOOK-508.pdf",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/gv77-cetz",
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
+            "identifier": "6e9ec91c-c298-5a59-bc0a-51f3b20f6c80",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt pillar v2.10.16 (coreset-dev0)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/pillar.csv",
+                    "description": "CoreSEt pillar v2.10.16 (coreset-dev0)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt pillar v2.10.16 (coreset-dev0)"
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
+                "hasEmail": "mailto:ARTINFO@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/knu9-e7pg",
+            "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Patient and Cycle Characteristics dataset summarizes the types of ART services performed and the kinds of patients who received ART procedures in a specific clinic. Please note patient characteristics are presented per cycle rather than per patient. As a result, patients who had more than one ART cycle within the reporting year are represented more than once.",
+            "title": "2020 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/knu9-e7pg",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Assisted Reproductive Technology (ART)"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-va.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-12-09",
+            "@type": "dcat:Dataset",
+            "temporal": "2015/2020",
+            "modified": "2024-10-11",
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Linked-VA-Match-File.pdf"
+            ],
+            "keyword": [
+                "linked va files",
+                "nhcs",
+                "research-data-center",
+                "veterans"
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
+            "identifier": "https://data.cdc.gov/api/views/vaca-65fb",
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with administrative data from the Department of Veterans Affairs (VA). NHCS data have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training and veteran readiness (vocational rehabilitation), and employment benefit programs.",
+            "title": "National Hospital Care Survey (NHCS) linked to Department of Veterans Affairs Administrative Data Files",
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
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 9) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS-VA-Linkage-Methods-and-Analytic-Considerations.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/tv5g-74as",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
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
+            "identifier": "https://data.cdc.gov/api/views/tv5g-74as",
+            "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Since [INSERT DATE], XXX influenza-associated pediatric deaths occurring during the 2017-18 season have been reported.",
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tv5g-74as/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tv5g-74as/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tv5g-74as/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tv5g-74as/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2023-11-16",
+            "@type": "dcat:Dataset",
+            "modified": "2023-12-04",
+            "references": [
+                "https://www.census.gov/programs-surveys/acs/data.html",
+                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
+            ],
+            "keyword": [
+                "acs",
+                "county",
+                "estimates",
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
+            "identifier": "https://data.cdc.gov/api/views/i6u4-y3g4",
+            "description": "This dataset contains county-level social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service:  https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
+            "title": "SDOH Measures for County, ACS 2017-2021",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/ehf4-c7tw",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "legionellosis",
+                "leptospirosis",
+                "listeriosis",
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
+            "identifier": "https://data.cdc.gov/api/views/ehf4-c7tw",
+            "description": "NNDSS - TABLE 1U. Legionellosis to Listeriosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1U. Legionellosis to Listeriosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-bridged-race-july-1st-estimates-0",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-07-31",
+            "temporal": "1990-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "age",
+                "county",
+                "ethnicity",
+                "population",
+                "population statistics",
+                "race",
+                "sex",
+                "state",
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
+            "identifier": "c4c88d50-56af-4f58-bd10-6f234e2b3125",
+            "description": "<p>The Population - Bridged-Race July 1st Estimates online databases report bridged-race population estimates of the July 1st resident population of the United States, based on Census 2000 counts, for use in calculating vital rates. These estimates result from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) standards for the collection of data on race and ethnicity, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White). Many data systems, such as vital statistics, are continuing to use the 1977 OMB standards during the transition to full implementation of the 1997 OMB standards. Postcensal estimates are available for year 2000 - 2009; intercensal estimates are available for the years 1990-1999. Obtain population counts by Year, State, County, Race (4-categories), Ethnicity, Sex and Age (1-year or 5-year groups). The data are released by the National Center for Health Statistics.</p>",
+            "title": "CDC WONDER: Population - Bridged-Race July 1st Estimates",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/bridged-race-population.html",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
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
+            "identifier": "https://data.cdc.gov/api/views/9xb7-9z99",
+            "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 29 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2021 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/gxrm-5qet",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-06-08",
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
+            "identifier": "0f4dd698-2ac9-5a6c-bbd2-c7d23f4110e8",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_files_allDownloadsSSBtn",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/files_allDownloadsSSBtn.csv",
+                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "files_allDownloadsSSBtn csv file"
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
+            "landingPage": "https://healthdata.gov/d/gyk2-ne97",
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
+            "identifier": "8f77310d-ef45-5bb6-bcb0-6da9a1bdb3cd",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_fileType_measureDisplayGroups",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/fileType_measureDisplayGroups.csv",
+                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://data.cdc.gov/d/t6u2-f84c",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-13",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-01-01/Present",
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
+            "identifier": "https://data.cdc.gov/api/views/t6u2-f84c",
+            "description": "This file contains death counts and death rates for drug overdose, suicide, homicide and firearm injuries at the United States national level (additional datasets exist for other levels of geography). The data is grouped by 3 different time periods including monthly, yearly, and trailing twelve months. Please see data dictionary for intents and mechanisms included in each measure.",
+            "title": "Mapping Injury, Overdose, and Violence - National",
+            "programCode": [
+                "009:033"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t6u2-f84c/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t6u2-f84c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t6u2-f84c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t6u2-f84c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Injury & Violence"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/mortality.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2016-08-04",
+            "@type": "dcat:Dataset",
+            "temporal": "2022-04-01/2024-06-30",
+            "modified": "2025-01-14",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "alzheimer disease",
+                "cancer",
+                "causes of death",
+                "cerebrovascular disease",
+                "chronic liver disease",
+                "chronic lower respiratory disease",
+                "cirrhosis",
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "diabetes",
+                "diseases of heart",
+                "drug overdose",
+                "falls",
+                "firearm injury",
+                "hiv disease",
+                "homicide",
+                "hypertensive disease",
+                "influenza",
+                "kidney disease",
+                "mortality",
+                "nchs",
+                "nvss",
+                "parkinson disease",
+                "pneumonia",
+                "pneumonitis due to solids and liquids",
+                "provisional",
+                "quarterly",
+                "septicemia",
+                "sex",
+                "state",
+                "suicide",
+                "unintentional injuries",
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
+            "identifier": "https://data.cdc.gov/api/views/489q-934x",
+            "description": "Provisional estimates of death rates. Estimates are presented for each of the 15 leading causes of death plus estimates for deaths attributed to drug overdose, falls (for persons aged 65 and over), human immunodeficiency virus (HIV) disease, homicide, and firearms-related deaths.",
+            "title": "NCHS - VSRR Quarterly provisional estimates for selected indicators of mortality",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://ucum.nlm.nih.gov/ucum-lhc/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "health data standards",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bat9-dmve",
+            "description": "A JavaScript package that can be included in webpages or programs and used for validating and converting unit expressions from the Unified Code for Units of Measure (UCUM).",
+            "title": "UCUM-LHC",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://github.com/lhncbc/ucum-lhc",
+                    "mediaType": "text/html",
+                    "title": "UCUM-LHC - GitHub repository"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Other"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/2vpi-n544",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-11-16",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-12-13 to 2021-11-17",
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
+            "identifier": "https://data.cdc.gov/api/views/2vpi-n544",
+            "description": "This data dictionary provides information about archived demographic trend data for people receiving COVID-19 vaccinations in the United States at the national level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities. \n\nThese data have been archived to provide historical demographic trend data for COVID-19 vaccine recipients prior to CDC converting the Vaccination Demographic Trends site to using data based on the date of vaccine administration. Previously, the Vaccination Demographic Trends site presented trend data by the date the vaccination was reported to CDC.",
+            "title": "Archive: COVID-19 Vaccination Demographic Trends by Report Date, National",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vpi-n544/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vpi-n544/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vpi-n544/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2vpi-n544/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/h43i-y4v2",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-10-09",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-07",
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
+            "identifier": "151e48c4-52e7-4c42-bd9a-4a46b85365a3",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 09-30-2024-to-10-06-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-09-30-2024-to-10-06-2024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
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
+                "insurance",
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
+            "identifier": "https://healthdata.gov/api/views/h4d7-8c39",
+            "description": "The Medical Expenditure Panel Survey Insurance Component (MEPS-IC) is an annual survey of private employers and State and local governments. The MEPS-IC produces national and State level estimates of employer-sponsored insurance, including offered plans, costs, employee eligibility, and number of enrollees. PDF files are available for complete sets of table series on employer-based health insurance at the national, state, and metropolitan area levels. The MEPS-IC is sponsored by the Agency for Healthcare Research and Quality and is fielded by the U.S. Census Bureau.",
+            "title": "Medical Expenditure Panel Survey (MEPS) Insurance Component Complete Table Series PDFs",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datatools.ahrq.gov/meps-ic#table-series",
+                    "mediaType": "text/html",
+                    "title": "PDF Tables"
+                }
+            ],
+            "describedBy": "https://datatools.ahrq.gov/meps-ic#table-series"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/h4eb-shcy",
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
+            "identifier": "4a0b8c8d-3725-5ab7-af6e-a67025589f85",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-change-of-ownership-owner-information",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-04-21",
+            "temporal": "2022-01-01/2024-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Data_Guidance.pdf"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a4358712-e910-4eaf-8f24-5e90ba3cf8d0/data-viewer",
+            "description": "The Skilled Nursing Facility (SNF) Change of Ownership (CHOW) - Owner Information dataset provides information on individual and organizational ownership interest and managerial control associated with the buyer and seller organizations, role of the owner, association date, address of the organizational owner and other ownership details.",
+            "title": "Skilled Nursing Facility Change of Ownership - Owner Information",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a4358712-e910-4eaf-8f24-5e90ba3cf8d0/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/ba5a5dd5-f2b1-4047-a80a-9da9ec038312/SNF_CHOW_Owners_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/79e884c7-5be0-4059-9fa9-c778d34c44e0/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/f2c814e7-ea11-4d0c-bf2a-68323d82f463/SNF_CHOW_Owners_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4edc8f10-17c4-4b70-95d3-755f6bb15cd0/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/40e75ec2-892f-4ee0-a934-a86b6a3e2ff4/SNF_CHOW_Owners_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f33b46ed-2036-47e3-8344-9dc64ddcbbd1/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/78b5c3e8-0b6e-4bb3-863b-7f20f3c9ca64/SNF_CHOW_Owners_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f6c042b5-006b-4262-b227-5c50d45fa816/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/b8ab7f74-e0bf-4bf6-90ac-85171d6e7eae/SNF_CHOW_Owners_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e7bbb52e-f3da-4757-b85c-c6f71abe0173/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/6f787cc2-e652-4102-90aa-584b70292bad/SNF_CHOW_Owners_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/77a52242-f510-4ff4-b61f-c511b771e8da/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/2982689d-f31d-4878-99e4-1efa09b5aab3/SNF_CHOW_Owners_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a1a1e421-d4ff-4a70-9330-f56cb237be45/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/23fbec12-05d8-44b1-9d62-5da8d341f8df/SNF_CHOW_Owners_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c1e36fcf-2d2d-41d4-8e38-1cac3e19cd6f/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/461ff47b-e5c4-47f2-a4b6-2f390d0ba82b/SNF_CHOW_Owners_2022.12.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b13761c2-e721-4458-b6aa-e10b3b1ff403/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/54c3f2ba-6500-4c17-b138-9c9ea3ae25e5/SNF_CHOW_Owners_2022.09.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/436bd59f-f19a-4141-bffc-5fb3f6a147b4/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/9d06bed9-4373-47b9-88f1-b58cda627ce7/Study_01.032.02_2022.07.01_PPEF_SNF_CHOW_Owners_Extract.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0abd00a5-bfad-4975-a5a9-ccbfa5001422/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/9310c3ef-c246-4b27-8eb3-f422fe9156cf/SNF_CHOW_Owners_2022Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b972eccc-46ac-4727-9b0e-13a04aef80eb/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-03-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Owners_Data_Dictionary.pdf",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK547852/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-30",
+            "keyword": [
+                "dataset",
+                "environmental health",
+                "toxicology"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5fe7-gc6d",
+            "description": "Provides up-to-date, accurate, and easily accessed information on the diagnosis, cause, frequency, patterns, and management of liver injury attributable to prescription and nonprescription medications, herbals and dietary supplements.",
+            "title": "LiverTox",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pub/litarch/29/31/",
+                    "mediaType": "text/html",
+                    "title": "Download LiverTox Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/NBK547852/",
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
+            "landingPage": "https://healthdata.gov/d/h5bv-j4am",
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
+            "identifier": "22c72566-87de-5759-90ee-350df11bc89b",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_measure_allStates_downloadLink",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates_downloadLink.csv",
+                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://data.cdc.gov/d/rnah-xd9n",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/rnah-xd9n",
+            "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Please refer to the CDC WONDER publication for weekly updates to the footnote for this condition.\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnah-xd9n/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnah-xd9n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnah-xd9n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rnah-xd9n/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "bioethics",
+                "biomedical research",
+                "books",
+                "clinical medicine",
+                "community health",
+                "dataset",
+                "dentistry",
+                "ethics medical",
+                "literature",
+                "medicine",
+                "nursing"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vc2v-qdpk",
+            "description": "PubMed comprises more than 26 million citations for biomedical literature from MEDLINE, life science journals, and online books. Citations may include links to full-text content from PubMed Central and publisher web sites.",
+            "title": "PubMed",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/books/NBK25497/",
+                    "description": "The Entrez Programming Utilities (E-utilities) are a set of nine server-side programs that provide a stable interface into the Entrez query and database system at the National Center for Biotechnology Information (NCBI).",
+                    "@type": "dcat:Distribution",
+                    "title": "E-utilities API"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pubmed.ncbi.nlm.nih.gov/help/#download-pubmed-data",
+                    "mediaType": "text/html",
+                    "title": "Download MEDLINE/PubMed Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pubmed.ncbi.nlm.nih.gov/",
+                    "mediaType": "text/html",
+                    "title": "Search PubMed - Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://pubmed.ncbi.nlm.nih.gov/clinical/",
+                    "description": "This tool uses predefined filters to help you quickly refine PubMed searches on clinical or disease-specific topics. To use this tool, enter your search terms in the search bar and select filters before searching.  The tool include a COVID-19-specific filter.",
+                    "@type": "dcat:Distribution",
+                    "title": "PubMed Clinical Queries"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.nlm.nih.gov/psd/special_queries.html",
+                    "description": "Clinical Queries (Clinical Study Categories and COVID-19), Healthy People 2020, and Health Services Research (HSR) Queries, as well as other topics.",
+                    "@type": "dcat:Distribution",
+                    "title": "Topic-Specific PubMed Queries"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://learn.nlm.nih.gov/documentation/training-packets/T0042010P/",
+                    "description": "Quick tours, tutorials, class recordings, handouts, and API instructions",
+                    "@type": "dcat:Distribution",
+                    "title": "PubMed Online Training"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Literature"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/innovation-center-model-summary-information",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2025-01-01/2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-17",
+            "references": [
+                "https://data.cms.gov/resources/model-summary-information-methodology"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data-viewer",
+            "description": "The Innovation Center Model Summary Information dataset contains various data points related to CMS Innovation Center models, demonstrations, programs, and initiatives. This can includes name, start and end date, statutory or regulatory authority, keywords, stage of implementation, participants, beneficiaries and physicians impacted, and categories related to health care quality, cost, payment, and delivery.\u00a0",
+            "title": "Innovation Center Model Summary Information",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Innovation Center Model Summary Information : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/46af39a2-3a14-497e-aa4b-d7480bed3497/WDDSE-Model-Summary-BPCIA-01-17-25.csv",
+                    "mediaType": "text/csv",
+                    "title": "Innovation Center Model Summary Information : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/038a8dcf-6552-4766-a954-18a275412bb6/data",
+                    "mediaType": "text/html",
+                    "title": "Innovation Center Model Summary Information : 2025-01-17"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/model-summary-information-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1M",
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
+                "city",
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
+            "identifier": "https://data.cdc.gov/api/views/epbn-9bv3",
+            "description": "This dataset contains model-based place (incorporated and census-designated places) level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at   www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, Place Data 2022 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "temporal": "2004-01-01/2012-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2004-01-01",
+            "keyword": [
+                "adverse event",
+                "human drugs"
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
+            "identifier": "b454bed2-730a-4e06-becb-0f599f2ad62a",
+            "description": "The Adverse Event Reporting System (AERS) is a computerized information database designed to support the FDA's post-marketing safety surveillance program for all approved drug and therapeutic biologic products. The FDA uses AERS to monitor for new adverse events and medication errors that might occur with these marketed products. Reporting of adverse events from the point of care is voluntary in the United States. FDA receives some adverse event and medication error reports directly from health care professionals (such as physicians, pharmacists, nurses and others) and consumers (such as patients, family members, lawyers and others). Healthcare professionals and consumers may also report these events to the products' manufacturers. If a manufacturer receives an adverse event report, it is required to send the report to FDA as specified by regulations.  The files listed on this page contain raw data extracted from the AERS database for the indicated time ranges and are not cumulative. Users of these files need to be familiar with creation of relational databases using applications such as ORACLE, Microsoft Office Access, MySQL and IBM DB2 or the use of ASCII files with SAS analytic tools. A simple search of AERS data cannot be performed with these files by persons who are not familiar with creation of relational databases.",
+            "title": "Adverse Event Reporting System (AERS)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/h62y-qtec",
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
+            "identifier": "672d5f6a-b8a7-4ebe-87f6-67db641e192d",
+            "description": "The Rate PUF (Rate-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Rate-PUF contains plan-level data on rates based on an eligible subscriber\u2019s age, tobacco use, and geographic location; and family-tier rates.",
+            "title": "Rate PUF \u2013 PY2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/Rate_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1996",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1996)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1996) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/2kh7-g39q",
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
+            "identifier": "https://data.cdc.gov/api/views/2kh7-g39q",
+            "description": "Three-dimensional (3D) printing is increasingly being used in manufacturing settings, homes and schools.  Fused deposition modeling (FDM) 3D printers are the most widely used systems with standard thermoplastics such as acrylonitrile butadiene styrene (ABS), polylactic acid and polycarbonate (PC) commonly used in the manufacturing processes.  Heating of the thermoplastic generates and releases particulates and fumes.  Emission constituents frequently measured include aldehydes, benzene, toluene, ethylbenzene, and xylenes.  Inhalation of the emitted particulates and/or the fumes, that contain bisphenol A (BPA)  may pose health problems to users of these systems as well as bystanders.\n\nThe goal of the current study was to examine the effects of inhalation of PC-emissions generated during 3D-printing.  PC-emissions can include bisphenol A (BPA). Bisphenols are known endocrine and metabolic disruptors (i.e., they interfere with actions of steroid and thyroid hormones) and have been shown to have significant effects on a number of physiological systems including the endocrine and cardiovascular systems.  Because steroid hormones have major effects on cardiovascular function, it is possible that inhalation of PC particulate and/or BPA impact cardiovascular function.\n\nTo begin to understand how inhalation of PC-emissions generated during 3D printing might affect the cardiovascular system, the current study examined the effects of inhaling PC-emissions after 1, 4, 8, 15 and 30d of exposure, on peripheral vascular responses to vaso-modulating agents, on cardiac morphology and on the expression of proteins and transcripts that are markers of inflammation, oxidative stress and cardiovascular dysfunction.",
+            "title": "Exposure to emissions generated by 3-dimensional printing with polycarbonate affects vascular morphology and expression of markers of oxidative stress and vascular dysfunction in cardiac tissue",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/2kh7-g39q/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/cov19_landing_2024.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2015-01-04/2020-01-03",
+            "modified": "2024-09-24",
+            "keyword": [
+                "all causes",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
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
+            "identifier": "https://data.cdc.gov/api/views/9cpv-whbv",
+            "description": "This dataset includes the number of deaths from all causes by week in which the death occurred and by jurisdiction, from 2015 to 2019, United States and Puerto Rico.",
+            "title": "Weekly counts of deaths from all causes by jurisdiction,  2015-2019",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States, Puerto Rico",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P4Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/h6e5-7hzs",
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
+            "identifier": "0a339472-900f-526b-b339-f5d7d407a906",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_measure_allStates",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates.csv",
+                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://data.cdc.gov/d/chmz-4uae",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
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
+            "identifier": "https://data.cdc.gov/api/views/chmz-4uae",
+            "description": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes data for old world hantavirus infections, such as Seoul virus infections. Prior to 2015, this condition was not nationally notifiable and data for this condition was not submitted to CDC's National Notifiable Diseases Surveillance System (NNDSS).\n\u00b6 Includes data for Andes virus infections.",
+            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/h8pb-fabb",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2024",
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
+            "identifier": "2cfb30f4-7c65-42bd-bc4c-a3fbcf1cb2cd",
+            "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2024 Individual Medical",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/individual_market_medical.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/gap/phegeni",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-07-01",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-30",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/53jk-taha",
+            "description": "Supports finding human phenotype/genotype relationships with queries by phenotype, chromosome location, gene, and SNP identifiers. Currently includes information from dbGaP, the National Human Genome Research Institute (NHGRI) genome-wide association study (GWAS) Catalog, and Genotype - Tissue Expression (GTeX).",
+            "title": "Phenotype-Genotype Integrator (PheGenI)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/gap/phegeni",
+                    "mediaType": "text/html",
+                    "title": "Phenotype-Genotype Integrator (PheGenI) - Query Interface"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rqg5-mkef",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-10-17",
+            "@type": "dcat:Dataset",
+            "modified": "2017-09-13",
+            "keyword": [
+                "death rate",
+                "motor vehicle"
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
+            "identifier": "https://data.cdc.gov/api/views/rqg5-mkef",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, All States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rqg5-mkef/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rqg5-mkef/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rqg5-mkef/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rqg5-mkef/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "geospatial"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/jz7r-jrma",
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
+                "tetanus",
+                "varicella",
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
+            "identifier": "https://data.cdc.gov/api/views/jz7r-jrma",
+            "description": "NNDSS - Table II. Tetanus to Varicella - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
+            "title": "NNDSS - Table II. Tetanus to Varicella",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/harf-86yj",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-01-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-11",
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
+            "identifier": "e02d3bb0-600d-5451-945f-978a8a511770",
+            "description": "During a public health emergency in the Families First Coronavirus Response Act (FFCRA), a new optional Medicaid eligibility group was added called COVID-19 testing eligibility group. States reported these expenditures under sections 6004 and 6008 through the Medicaid Budget and Expenditure System (MBES) on the Form CMS-64. The data in these reports constitute summary level preliminary expenditure information related to these FFCRA provisions for each state\r\n\r\nNotes:\r\n1. The Families First Coronavirus Response Act (FFCRA), enacted on March 18, 2020, provided a temporary FMAP increase to states and territories meeting certain qualifications and added a new optional \t\t\t\t\t\r\n    Medicaid eligibility group for uninsured individuals during a public health emergency in section 1902(a)(10)(A)(ii)(XXIII) of the Act, referred to as the \u201cCOVID - 19 Testing Group.\u201d\t\t\t\t\t\r\n2. FFCRA Section 6008 provides a temporary 6.2 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning January 1, 2020 and lasting through \t\t\t\t\t\r\n    the end of the quarter in which the public health emergency (PHE) declared by the Secretary for COVID-19 ends, including any extensions.\t\t\t\t\t\r\n3. FFCRA Section 6004 provides a 100 percent match rate for individuals eligible under the new optional Medicaid eligibility group in section 1902(a)(10)(A)(ii)(XXIII) of the Act, beginning no earlier than \t\t\t\t\t\r\n    March 18, 2020 and lasting through the end of the PHE for COVID-19.\t\t\t\t\t\r\n4. States that have reported \u201c0\u201d either have no expenditures for that reporting category or have not yet reported expenditures for that category.\t\t\t\t\t\r\n5. This report is a cumulative summary report that includes current and prior period adjustment expenditures that apply to this quarter\t\r\n6. For the Quarter ending 03/31/2020: Delaware has Negative Total Computable Expenditures and Total Federal Share Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\r\n7. For the Quarter ending 09/30/2020: Colorado has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\t\t\r\n8. For the Quarter ending 03/31/2021: California has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period. This corrected FY 2020 Q4 expenditures for Treatment services that are not allowed for Section 6004 100% FMAP match.\r\n9. For the Quarter ending 03/31/2021: Utah has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\r\n10. For the Quarter ending 12/31/2022: California has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\r\n11. For the Quarter ending 12/31/2022: Connecticut has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\r\n12. For the Quarter ending 09/30/2023: Connecticut has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\t\t\r\n13. For the Quarter ending 09/30/2023: Illinois has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\t\t\r\n14. For the Quarter ending 09/30/2023: Minnesota has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid",
+            "title": "Medicaid CMS-64 FFCRA Increased FMAP Expenditure",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/Medicaid-CMS-64-FFCRA-Increased-FMAP-Expenditure-10182024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/research/coronavirus/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "dataset",
+                "literature"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/8nrp-jhfw",
+            "description": "LitCovid is a curated literature hub for tracking up-to-date scientific information about the 2019 novel Coronavirus. The articles are updated daily and are further categorized by different research topics (e.g. Long Covid) and geographic locations for improved access.",
+            "title": "LitCovid",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pub/lu/LitCovid/",
+                    "description": "See README.txt for descriptions of datasets.  In addition to exports of LitCovid, datasets which are automatically annotated or contain articles are available.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download LitCovid Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Literature"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/wgvr-7mvz",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-12",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "community mitigation",
+                "coronavirus",
+                "covid-19",
+                "school closure"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nicole Zviedrite",
+                "hasEmail": "mailto:jmu6@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/wgvr-7mvz",
+            "description": "Unplanned public K-12 school district and individual school closures due to COVID-19 in the United States from February 18\u2013June 30, 2020.",
+            "title": "COVID-19-associated school closures, United States, February 18\u2013June 30, 2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgvr-7mvz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgvr-7mvz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgvr-7mvz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wgvr-7mvz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/hbyh-kqh6",
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
+            "identifier": "2f2451fb-e5fe-4235-892b-755fe273903e",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-09-to-2023-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-01092023-to-01152023_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-09-to-2023-01-15"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/9x7v-wy9u",
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
+            "identifier": "https://data.cdc.gov/api/views/9x7v-wy9u",
+            "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-clinic-group-practice-reassignment",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2022-01-01/2025-01-31",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e1f1fa9a-d6b4-417e-948a-c72dead8a41c/data-viewer",
+            "description": "The Revalidation Clinic Group Practice Reassignment dataset provides information between the physician and the group practice they reassign their billing to. It also includes individual employer association counts and the revalidation dates for the individual physician as well as the clinic group practice.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Revalidation Clinic Group Practice Reassignment",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e1f1fa9a-d6b4-417e-948a-c72dead8a41c/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/cf3fa088-72f9-4115-a5c7-9b587116b3b7/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a30bd9d4-1ad1-4bb1-b9d4-d31507095f47/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/6bc8fe73-5568-44a2-b79f-35376e224093/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09ba1e0e-2000-469f-ae3e-d6acb406a4bd/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/ac809489-97fd-473e-b871-6bf46049375c/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/96fca71e-4ab9-44ca-978e-9821dad2366d/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/22812ccd-463f-43a7-85df-79a7c9d0d380/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0943cf59-6f41-4736-8e88-7c9f0a801954/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/74ac2b19-7bba-4c12-8390-29f272188a7a/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/df40e019-20dc-4a6f-96ae-8369a8c2da65/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/8be3d480-edfc-44cd-ae0c-b7e1e3ea5690/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6e3d82b3-9ad0-4e1b-bb3e-e2579aebcb89/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/0ac4636c-c741-4a3e-a84a-dbff50ec6f6a/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0766a480-5ae0-4d1a-8166-4de1b0c565e7/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/78017b80-bf62-4417-92f5-d3223c975a4e/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9e37c9d5-f0ae-404d-8d89-22f10b717d6e/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/246880eb-3969-49d9-bcc8-f6c7fc3a1611/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b28fa07b-50f8-4520-af1b-43a1be2fffb8/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/2f69c02d-b3e7-4c30-9086-d5f2aa1a6864/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6e251069-79c3-4bcf-972c-ec6efd319558/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/ff527070-50f4-4e78-8e7d-c9d395f0f854/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9f242c09-6eef-405a-9692-b4c3a7f5a7e6/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/a5d10b97-dd12-461c-8a80-e73e9305431b/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6042e10e-a361-40ac-9838-8ede1dd2e473/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/999e3435-02f8-4b95-8405-7f6029d0af8d/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/190a977e-8175-4f8e-84b9-f3ee5aa54c6f/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/6d5e524e-ce51-4f57-8c31-6470fd13f075/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d5d244c1-79b3-46dc-83e6-91b9166a2263/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/622f8bd7-1d46-4951-a5a0-0d007004197a/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3ddc2e3-901c-4549-8d6b-21db3a95a998/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/768ac791-e4dd-4f29-b408-af611405184f/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b5d6013d-fdf3-4948-94ff-50171dc69028/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/ddc12875-3f2e-4942-9fe8-ba12501eb36c/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/35b1631c-1557-44c4-ada0-d9d6cfdf286f/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/61486e4c-8a3b-4b31-bf4a-d60128fce4e4/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d55ce5bf-91ee-4618-b4ce-59cda693e866/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/22b5e384-f5ea-4510-ad6a-8190a0383786/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0c55ef7b-098a-47ce-9897-9efcf6f4f4d6/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/9da6dfc1-b356-4d52-b50f-4e694849f2e4/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9389f6ad-5551-4da8-8d83-59f0234c1791/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/ed85664c-65e1-4624-8c0e-260aed9f42af/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/306e9308-ebdb-47cd-adea-e72b6fb44fa5/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/29fde050-7f32-4c3c-a312-fb18388e21e2/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-04-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7062cc70-6490-4600-b292-858ca575358c/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-04-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/e3ed9628-98cd-49df-bd59-07f7ed8e394d/revalidation_clinic_group_practice_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-02-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3c16d900-64cd-4874-91bc-04a164e94789/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-02-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/dd7a9ebf-3195-4555-8755-fa56b9a6052d/revalidation_clinic_group_practice_reassignment_pa_xref%20Dec%202021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/713e0294-e793-42b5-8c63-5f5723fe7ad1/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Clinic Group Practice Reassignment : 2022-01-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/revalidation-clinic-group-practice-reassignment-data-dictionary",
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
+            "issued": "2020-05-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2023-07-29",
+            "modified": "2023-09-27",
+            "keyword": [
+                "age",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "influenza",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "sex",
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
+            "identifier": "https://data.cdc.gov/api/views/9bhg-hcku",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by sex, age group, and jurisdiction of occurrence.",
+            "title": "Provisional COVID-19 Deaths by Sex and Age",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/hdhv-rcwe",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2019-04-18",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-03",
+            "keyword": [
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chris Vaughn",
+                "hasEmail": "mailto:no-reply@data.medicaid.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "8f39b637-9bb1-5894-9062-2c4f2ad70fba",
+            "description": "Provides program names, program features, population enrolled, benefits covered, quality assurance and improvement, performance incentives, provider value-based purchasing, participating plans, regions served and program notes.",
+            "title": "2017 Managed Care Programs by State",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/2017-managed-care-programs-by-state.hc9x-7kex.csv",
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
+                "brfss",
+                "county",
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
+            "identifier": "https://data.cdc.gov/api/views/dv4u-3x3q",
+            "description": "This dataset contains model-based county-level estimates for the PLACES project 2020 release. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 27 measures: 5 chronic disease-related unhealthy behaviors, 13 health outcomes, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2018 or 2017 county population data, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, County Data 2020 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/sixg-saap",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/sixg-saap",
+            "description": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sixg-saap/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sixg-saap/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sixg-saap/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sixg-saap/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2019-04-29",
+            "@type": "dcat:Dataset",
+            "modified": "2023-04-20",
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
+            "identifier": "https://data.cdc.gov/api/views/rpvx-m2md",
+            "description": "This dataset describes drug poisoning deaths at the U.S. and state level by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning. \n\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\n\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\n\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Drug poisoning death rates may be underestimated in those instances.\n\nREFERENCES\n1. National Center for Health Statistics. National Vital Statistics System: Mortality data. Available from: http://www.cdc.gov/nchs/deaths.htm.\n\n2. CDC. CDC Wonder: Underlying cause of death 1999\u20132016. Available from: http://wonder.cdc.gov/wonder/help/ucd.html.",
+            "title": "NCHS - Drug Poisoning Mortality by County: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rpvx-m2md/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rpvx-m2md/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rpvx-m2md/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rpvx-m2md/rows.xml?accessType=DOWNLOAD",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2015",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and<br />\n    correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual estimates. Information is provided on the use<br />\n    of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as<br />\n    lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco,<br />\n    and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment<br />\n    history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic<br />\n    criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were<br />\n    also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting<br />\n    from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2015 survey, including questions asked<br />\n    only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug<br />\n    use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes<br />\n    toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on<br />\n    mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking.<br />\n    Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to<br />\n    measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a<br />\n    split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems.<br />\n    Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race,<br />\n    age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2015)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2015) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/hhqs-3zft",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2014-12-31",
+            "keyword": [
+                "faers"
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
+            "identifier": "901A022F-A9B2-4B0A-9A33-0F3D353DF3FD",
+            "description": "Public access  allowing for public search of the FDA Adverse Events Database",
+            "title": "Public Search for Adverse Events (FOIA)",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/ucm082193",
+                    "mediaType": "application/xml",
+                    "description": "Public access  allowing for public search of the FDA Adverse Events Database"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.ncbi.nlm.nih.gov/clinvar/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-08-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4jy8-nv98",
+            "description": "ClinVar aggregates information about genomic variation and its relationship to human health.",
+            "title": "ClinVar",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/clinvar/",
+                    "mediaType": "text/html",
+                    "title": "ClinVar Homepage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/",
+                    "mediaType": "text/html",
+                    "title": "Download ClinVar Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/5iuf-feyd",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-04-21",
+            "@type": "dcat:Dataset",
+            "temporal": "August 1, 2011 to June 30, 2019",
+            "modified": "2022-04-21",
+            "keyword": [
+                "community mitigation",
+                "emergency preparedness",
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
+            "identifier": "https://data.cdc.gov/api/views/5iuf-feyd",
+            "description": "Prolonged unplanned public K-12 school district and individual school closures in the United States from August 1, 2011 \u2013 June 30, 2019. Prolonged unplanned school closure is defined as a school closure lasting \u22655 school days, excluding any scheduled days off.",
+            "title": "Prolonged Unplanned School Closures: USA, 2011-2019",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5iuf-feyd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5iuf-feyd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5iuf-feyd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5iuf-feyd/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/pwn4-m3yp",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-10-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-22/2023-05-10",
+            "modified": "2025-01-13",
+            "keyword": [
+                "aggregate",
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "death"
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
+            "identifier": "https://data.cdc.gov/api/views/pwn4-m3yp",
+            "description": "Reporting of new Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. This dataset will receive a final update on June 1, 2023, to reconcile historical data through May 10, 2023, and will remain publicly available.\n\n<b>Aggregate Data Collection Process </b>\nSince the start of the COVID-19 pandemic, data have been gathered through a robust process with the following steps: \n<ul><li>A CDC data team reviews and validates the information obtained from jurisdictions\u2019 state and local websites via an overnight data review process.</li>\n<li>If more than one official county data source exists, CDC uses a comprehensive data selection process comparing each official county data source, and takes the highest case and death counts respectively, unless otherwise specified by the state. </li>\n<li>CDC compiles these data and posts the finalized information on COVID Data Tracker. </li>\n<li>County level data is aggregated to obtain state and territory specific totals.</li>\n</ul>This process is collaborative, with CDC and jurisdictions working together to ensure the accuracy of COVID-19 case and death numbers. County counts provide the most up-to-date numbers on cases and deaths by report date. CDC may retrospectively update counts to correct data quality issues. \n\n<b>Methodology Changes </b>\nSeveral differences exist between the current, weekly-updated dataset and the archived version: \n<ul><li><b>Source:</b>\u202fThe current Weekly-Updated Version is based on county-level aggregate count data, while the Archived Version is based on State-level aggregate count data. </li>\n<li><b>Confirmed/Probable Cases/Death breakdown:\u202f</b> While the probable cases and deaths are included in the total case and total death counts in both versions (if applicable), they were reported separately from the confirmed cases and deaths by jurisdiction in the Archived Version.\u202f In the current Weekly-Updated Version, the counts by jurisdiction are not reported by confirmed or probable status (See Confirmed and Probable Counts section for more detail).</li>\n<li><b>Time Series Frequency:</b> The current Weekly-Updated Version contains weekly time series data (i.e., one record per week per jurisdiction), while the Archived Version contains daily time series data (i.e., one record per day per jurisdiction). </li>\n<li><b>Update Frequency:</b>\u202fThe current Weekly-Updated Version is updated weekly, while the Archived Version was updated twice daily up to October 20, 2022. </li></ul>\n<b>Important note:</b> The counts reflected during a given time period in this dataset may not match the counts reflected for the same time period in the archived dataset noted above. Discrepancies may exist due to differences between county and state COVID-19 case surveillance and reconciliation efforts. \n\n<b>Confirmed and Probable Counts </b>\nIn this dataset, counts by jurisdiction are not displayed by confirmed or probable status. Instead, confirmed and probable cases and deaths are included in the Total Cases and Total Deaths columns, when available. Not all jurisdictions report probable cases and deaths to CDC.* Confirmed and probable case definition criteria are described here: \n\n<a href=\"https://cdn.ymaws.com/www.cste.org/resource/resmgr/ps/ps2022/22-ID-01_COVID19.pdf\">Council of State and Territorial Epidemiologists (ymaws.com).</a>\n\n<b>Deaths</b>\nCDC reports death data on other sections of the website: <a href=\"https://covid.cdc.gov/covid-data-tracker/#datatracker-home\"> CDC COVID Data Tracker: Home</a>, <a href=\"https://covid.cdc.gov/covid-data-tracker/?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fcases-updates%2Fcases-in-us.html#cases_casesper100klast7days\">CDC COVID Data Tracker: Cases, Deaths, and Testing</a>, and <a href=\"https://www.cdc.gov/nchs/nvss/covid-19.htm\">NCHS Provisional Death Counts</a>. Information presented on the COVID Data Tracker pages is based on the same source (to",
+            "title": "Weekly United States COVID-19 Cases and Deaths by State - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwn4-m3yp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwn4-m3yp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwn4-m3yp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwn4-m3yp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "theme": [
+                "Case Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mr4u-abm2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/mr4u-abm2",
+            "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 years, Confirmed to Legionellosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/medicaid-fraud-control-units-mfcu-annual-spending-and-performance-statistics",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-03-25",
+            "temporal": "2006-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "medicaid",
+                "office-of-inspector-general-department-of-health-human-services"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OIG public affairs",
+                "hasEmail": "mailto:public.affairs@oig.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Inspector General, Department of Health & Human Services"
+            },
+            "identifier": "e02ee78f-98b2-4a10-b057-07c73edb954c",
+            "description": "<p>To inform HHS, States, Congress, and the public about the results and accomplishments of the State Medicaid Fraud Control Units.</p>",
+            "title": "Medicaid Fraud Control Units (MFCU) Annual Spending and Performance Statistics",
+            "programCode": [
+                "009:076"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ci7c-73kg",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2023-04-26",
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "ensemble",
+                "forecast",
+                "model"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Forecasting and Outbreak Analytics",
+                "hasEmail": "mailto:cfadata@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ci7c-73kg",
+            "description": "This dataset contains forecasted weekly numbers of reported COVID-19 incident cases, incident deaths, and cumulative deaths in the United States, previously reported on COVID Data Tracker (https://covid.cdc.gov/covid-data-tracker/#datatracker-home). These forecasts were generated using mathematical models by CDC partners in the COVID-19 Forecast Hub (https://covid19forecasthub.org/doc/ensemble/). A CDC ensemble model was produced every week using the submitted models from that week at the national, and state/territory level. \n\n\nThis dataset is intended to mirror the observed and forecasted data, previously available for download on the CDC\u2019s COVID Data Tracker.  Mortality forecasts for both new and cumulative reported COVID-19 deaths were produced at the state and territory level and national level. Forecasts of new reported COVID-19 cases were produced at the county, state/territory, and national level. Please note that this dataset is not complete for every model, date, location or combination thereof. Specifically, county level submissions for COVID-19 incident cases were accepted, but not required, and are missing or incomplete for many models and dates.  State and territory-level forecasts are more complete, but not all models submitted forecasts for all locations, dates, and targets (new reported deaths, new reported cases, and cumulative reported deaths).  Forecasts for COVID-19 incident cases were discontinued in February 2022. Forecasts for COVID-19 cumulative and incident deaths were discontinued in March 2023.",
+            "title": "CDC COVID-19 Cases and Deaths Ensemble Forecast Archive",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "National",
+            "license": "http://creativecommons.org/licenses/by/4.0/legalcode",
+            "accrualPeriodicity": "Archive",
+            "theme": [
+                "Models"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/qcw5-4m9q",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "See data use agreement for additional information.",
+            "issued": "2021-05-24",
+            "@type": "dcat:Dataset",
+            "temporal": "2013/2017",
+            "modified": "2025-01-29",
+            "references": [
+                "https://clinicaltrials.gov/ct2/show/NCT01965470?cond=HIV&cntry=BW&draw=2&rank=14"
+            ],
+            "keyword": [
+                "bcpp",
+                "botswana",
+                "combination hiv prevention",
+                "hiv",
+                "hiv incidence",
+                "hiv testing",
+                "pepfar",
+                "randomized control trial"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Gene Ussery",
+                "hasEmail": "mailto:gua1@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/qcw5-4m9q",
+            "description": "The Botswana Combination Prevention Project (BCPP) was a research project conducted by the Botswana Ministry of Health (MOH), Harvard School of Public Health/Botswana Harvard AIDS Institute Partnership (BHP), and the U.S. Centers for Disease Control and Prevention (CDC). BCPP was a community randomized trial that examined the impact of prevention interventions on HIV incidence in 15 intervention and 15 control communities. The interventions included extensive HIV testing, linkage to care, and universal treatment services. To reduce HIV incidence in the intervention communities, the UNAIDS 90-90-90 goals were used: 90% of HIV-positive persons know their status; 90% of persons who know status are to be on ART; 90% of persons on ART are to be virally suppressed. The BCPP study is composed of 2 interlocking protocols: Evaluation Protocol and Intervention Protocol. The Evaluation Protocol of the BCPP evaluated the primary endpoint (HIV incidence), as well as some key related secondary endpoints. This protocol focused on the Baseline Household Survey; the HIV Incidence Cohort; and an End of Study Survey. The Intervention Protocol of the BCPP implemented the combination prevention (CP) intervention package in CPCs and measures the uptake of these interventions (expanded HIV testing and counselling, strengthened male circumcision, and expanded HIV Care and Treatment).",
+            "title": "Botswana Combination Prevention Project (BCPP) - Public Release Data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/qcw5-4m9q/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "spatial": "Botswana",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Global Health"
+            ],
+            "language": [
+                "English"
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
+            "modified": "2010-10-01",
+            "keyword": [
+                "h1n1",
+                "health",
+                "influenza",
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
+            "identifier": "9cc0d11d-dbcd-41a7-8947-02774d10ce2e",
+            "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
+            "title": "Fraudulent 2009 H1N1 Influenza Products Widget",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/hk4x-6nkd",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-11-03",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-28",
+            "keyword": [
+                "cms-64",
+                "expansion population",
+                "expenditures",
+                "mbes",
+                "medicaid",
+                "new adult group",
+                "viii group"
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
+            "identifier": "00505e90-f8ac-5921-b12f-5e23ba7ffcf3",
+            "description": "This dataset reports summary level expenditure data associated with the new adult group established under the Affordable Care Act. These state expenditures are reported through the federal Medicaid Budget and Expenditure System (MBES).\r\n\r\nNotes:\r\n1. \u201cVIII GROUP\u201d is also known as the \u201cNew Adult Group.\u201d\r\n2. The VIII Group is only applicable for states that have expanded their Medicaid programs by adopting the VIII Group. VIII Group expenditure information\r\nfor the states that have not expanded their Medicaid program is noted as \u201cN/A.\u201d\r\n3. States that have reported \u201c0\u201d either have no expenditures for that reporting category or have not yet reported expenditures for that category.\r\n4. MCHIP expenditures are not included in the All Medical Assistance Expenditures.",
+            "title": "Medicaid CMS-64 New Adult Group Expenditures",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/medicaid-cms-64-new-adult-group-expenditures-dataset10282024.csv",
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
+            "landingPage": "https://data.cdc.gov/d/kh8y-3es6",
+            "bureauCode": [
+                "009:15"
+            ],
+            "issued": "2020-05-06",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-17",
+            "keyword": [
+                "cares act",
+                "health system",
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
+            "identifier": "https://data.cdc.gov/api/views/kh8y-3es6",
+            "description": "HHS is providing support to healthcare providers fighting the coronavirus disease 2019 (COVID-19) pandemic through the bipartisan Coronavirus Aid, Relief, & Economic Security (CARES) Act; the Paycheck Protection Program and Health Care Enhancement Act (PPPHCEA); and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act, which provide a total of $178 billion for relief funds to hospitals and other healthcare providers on the front lines of the COVID-19 response. This funding supports healthcare-related expenses or lost revenue attributable to COVID-19 and ensures uninsured Americans can get treatment for COVID-19. HHS is distributing this Provider Relief Fund (PRF) money and these payments do not need to be repaid.\n\nThe Department allocated $50 billion in PRF payments for general distribution to Medicare facilities and providers impacted by COVID-19, based on eligible providers' net reimbursement. HHS has made other PRF distributions to a wide array of health care providers and more information on those distributions can be found here: https://www.hhs.gov/coronavirus/cares-act-provider-relief-fund/data/index.html",
+            "title": "HHS Provider Relief Fund",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/cz39-ahbn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
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
+            "identifier": "https://data.cdc.gov/api/views/cz39-ahbn",
+            "description": "NNDSS - Table 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1A.  Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/hmsq-tdap",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-03-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-03-26",
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
+            "identifier": "9ddd26da-ac32-47e9-88fd-3e4d4e747c90",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-18-2024-to-03-24-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-03-18-2024-to-03-24-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-18-2024-to-03-24-2024"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225440.htm",
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
+                "milk",
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
+            "identifier": "5d970911-f35f-4514-9ddf-b20bc32790ff",
+            "description": "Contains data for the FDA Plainview Milk Cooperative Ingredient Recall since June 2009.",
+            "title": "FDA Plainview Milk Cooperative Ingredient Recall",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/uvv3-fqwr",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-09-22",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/uvv3-fqwr",
+            "description": "The Chemical Carcinogenesis Research Information System (CCRIS) database contains chemical records with carcinogenicity, mutagenicity, tumor promotion, and tumor inhibition test results. It was developed by the National Cancer Institute (NCI). Data are derived from studies cited in primary journals, current awareness tools, NCI reports, and other sources. Test results have been reviewed by experts in carcinogenesis and mutagenesis. CCRIS provides historical information from the years 1985 - 2011. It is no longer updated.",
+            "title": "Chemical Carcinogenesis Research Information System (CCRIS)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/ccrislease/",
+                    "description": "Download over 9,000 chemical records.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download CCRIS Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/sample/ccris/",
+                    "mediaType": "text/html",
+                    "title": "Download Sample CCRIS Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/ccrislease/ccris-docs.txt",
+                    "mediaType": "text/html",
+                    "title": "CCRIS Documentation"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
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
+            "identifier": "https://data.cdc.gov/api/views/6vp6-wxuq",
+            "description": "This is the complete dataset for the 500 Cities project 2019 release. This dataset includes 2017, 2016 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2017, 2016), Census Bureau 2010 census population data, and American Community Survey (ACS) 2013-2017, 2012-2016 estimates. Because some questions are only asked every other year in the BRFSS, there are 7 measures (all teeth lost, dental visits, mammograms, pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) from the 2016 BRFSS that are the same in the 2019 release as the previous 2018 release. More information about the methodology can be found at www.cdc.gov/500cities.",
+            "title": "500 Cities: Local Data for Better Health, 2019 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2017-relea/6vp6-wxuq",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "alcohol",
+                "cocaine",
+                "crack cocaine",
+                "demographic characteristics",
+                "drug abuse",
+                "drug use",
+                "hallucinogens",
+                "heroin",
+                "homeless persons",
+                "inhalants",
+                "marijuana",
+                "sedatives",
+                "smoking",
+                "stimulants",
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
+            "identifier": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
+            "description": "<p>The DC Metropolitan Area Drug Study (DC<em>MADS) was<br />\nconducted in 1991, and included special analyses of homeless and<br />\ntransient populations and of women delivering live births in the DC<br />\nhospitals. DC</em>MADS was undertaken to assess the full extent of the<br />\ndrug problem in one metropolitan area. The study was comprised of 16<br />\nseparate studies that focused on different sub-groups, many of which<br />\nare typically not included or are under-represented in household<br />\nsurveys.The DC<em>MADS: Household and Non-household Populations<br />\nexamines the prevalence of tobacco, alcohol, and drug use among<br />\nmembers of household and non-household populations aged 12 and older<br />\nin the District of Columbia Metropolitan Statistical Area (DC<br />\nMSA). The study also examines the characteristics of three<br />\ndrug-abusing sub-groups: crack-cocaine, heroin, and needle users. The<br />\nhousehold sample was drawn from the 1991 National Household Survey on<br />\nDrug Abuse (NHSDA). The non-household sample was drawn from the<br />\nDC</em>MADS Institutionalized and Homeless and Transient Population<br />\nStudies. Data include demographics, needle use, needle-sharing, and<br />\nuse of tobacco, alcohol, cocaine, crack, inhalants, marijuana, hallucinogens, heroin, sedatives, stimulants, psychotherapeutics (non-medical use), tranquilizers, and analgesics.This study has 1 Data Set.</p>",
+            "title": "Washington  DC  Metropolitan Area Drug Study Household and Non-Household Populations (DC-MADSH-1991)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
+                    "description": "Washington  DC  Metropolitan Area Drug Study Household and Non-Household Populations (DC-MADSH-1991) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ur6f-kidn",
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
+            "identifier": "https://data.cdc.gov/api/views/ur6f-kidn",
+            "description": "Thermal spray coating involves spraying a product that is melted by extremely high temperatures and then applied under pressure under pressure onto a surface. Large amounts of a complex metal aerosol (e.g., Fe, Cr, Ni, Zn) are formed during the process, presenting a potentially serious risk to the operator. Information about the health effects associated with exposure to these aerosols is lacking. Even less is known about the chemical and physical properties of these aerosols. The goal was to develop and test an automated thermal spray coating aerosol generator and inhalation exposure system that would simulate workplace exposures. An electric arc wire- thermal spray coating aerosol generator and exposure system was designed and separated into two areas: (A) an enclosed room where the spray coating occurs; (B) an exposure chamber with different measurement devices and controllers. The physicochemical properties of aerosols generated during electric arc wire- thermal spray coating using five different consumable wires were examined. The generated particles regardless of composition were poorly soluble, complex metal oxides and mostly arranged as chain-like agglomerates and similar in size distribution as determined by MOUDI and ELPI. To allow for continuous, sequential spray coating during a 4-hr exposure period, a motor rotated the metal pipe to be coated in a circular and up-and-down direction. In a pilot animal study, male Sprague-Dawley rats were exposed to aerosols (25 mg/m3 x 4 hr/d x 9 d) generated from electric arc wire- thermal spray coating using a stainless-steel PMET720 consumable wire. The targeted exposure chamber concentration was achieved and maintained during a 4-hr period. At 1 d after exposure, lung injury and inflammation were significantly elevated in the group exposed to the thermal spray coating aerosol compared to the air control group. A thermal spray coating inhalation system was designed and constructed that will generate continuous metal spray coating aerosols at a targeted concentration for extended periods of time without interruption for future animal exposure studies.",
+            "title": "Development of a thermal spray coating aerosol generator and inhalation exposure system",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/ur6f-kidn/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/hq8u-zp5z",
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
+            "identifier": "13793c80-067b-5cf9-a0aa-751c387a10d4",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard measure v2.12.1-test (local)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/measure.csv",
+                    "description": "Scorecard measure v2.12.1-test (local)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure v2.12.1-test (local)"
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
+            "landingPage": "https://healthdata.gov/d/hqzz-856g",
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
+            "identifier": "d12a6469-b3df-5b52-a980-f7613823e8a3",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet measure_value v2.10.64 (coreset-dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet measure_value v2.10.64 (coreset-dev)"
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
+            "landingPage": "https://data.cdc.gov/d/rdmq-nq56",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-12-18",
+            "@type": "dcat:Dataset",
+            "temporal": "2022-10-01/2023-01-27",
+            "modified": "2025-01-24",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "ed",
+                "emergency department",
+                "flu",
+                "influenza",
+                "national syndromic surveillance program",
+                "ncird",
+                "nssp",
+                "ophdst",
+                "respiratory syncytial virus",
+                "respiratory-virus-response",
+                "rsv",
+                "rvr"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Syndromic Surveillance Program",
+                "hasEmail": "mailto:nssp@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/rdmq-nq56",
+            "description": "NSSP Emergency Department (ED) Visit Trajectories by State and Sub-State Regions- COVID-19, Flu, RSV, Combined. This dataset provides the percentage of emergency department patient visits for the specified pathogen of all ED patient visits for the specified geographic part of the country that were observed for the given week from data submitted to the National Syndromic Surveillance Program (NSSP). In addition, the trend over time is characterized as increasing, decreasing or no change, with exceptions for when there are no data available, the data are too sparse, or there are not enough data to compute a trend. These data are to provide awareness of how the weekly trend is changing for the given geographic region.\u202f \n\nNote that the reported sub-state trends are from Health Service Areas (HSA) and the data reported from the health care facilities located within the given HSA. Health Service Areas are regions of one or more counties that align to patterns of care seeking. The HSA level data are reported for each county in the HSA. \n\nMore information on HSAs is available <a href=\"https://seer.cancer.gov/seerstat/variables/countyattribs/hsa.html\"><b>here</b></a>.\n\nFor the emergency department time series, trajectory classifications reported on for sub-state (HSA) emergency department time series, trajectory classifications are based on approximations of the first derivative (slope) of trends that are smoothed using generalized additive models (GAMs). To determine time intervals in which the slope is sufficiently changing (i.e., rate of change distinguishable from 0), 95% confidence intervals for the slope approximations are calculated and assessed. Weeks with a 95% confidence interval not containing 0 are classified as increasing if the slope estimate is positive and decreasing if the slope estimate is negative. Weeks with a 95% confidence interval containing 0 are classified as stable. In the scenario that an HSA's time series is determined to be too sparse (i.e., many weeks with percentages of 0%), a model is not fit, and the HSA is classified as \u201csparse\u201d.  \n\nFor additional information, please see: <a href=\"https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide\"><b>Companion Guide: NSSP Emergency Department Data on Respiratory Illness</b></a>\n\nUpdated once per week on Fridays.\u202f",
+            "title": "NSSP Emergency Department Visit Trajectories by State and Sub State Regions- COVID-19, Flu, RSV, Combined\u202f\u202f",
+            "programCode": [
+                "009:037"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rdmq-nq56/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rdmq-nq56/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rdmq-nq56/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rdmq-nq56/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/fj6i-3v3k",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "confirmed",
+                "hepatitis b",
+                "hepatitis c acute",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
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
+            "identifier": "https://data.cdc.gov/api/views/fj6i-3v3k",
+            "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/hrcu-si9w",
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
+                "perinatal care",
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
+            "identifier": "ed67e610-aed3-4bed-842f-e6044511dd64",
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of perinatal care, including prenatal visits, prenatal bundled payments, postpartum visits, and postpartum bundled payments, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating perinatal care measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas  for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Perinatal Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/Perinatal-Care-Services-Provided-to-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of perinatal care, including prenatal visits, prenatal bundled payments, postpartum visits, and postpartum bundled payments, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating perinatal care measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas  for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Perinatal Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44"
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
+            "landingPage": "https://data.cdc.gov/d/en3s-hzsr",
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
+            "identifier": "https://data.cdc.gov/api/views/en3s-hzsr",
+            "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul>  <li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\n                Find details about surveillance population, case determination, surveillance evaluation, and more.  </li>                    <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>  \n                 Get official interpretations from reports and publications created from ABCs data.        </li> </ul>",
+            "title": "Active Bacterial Core surveillance (ABCs) Streptococcus pneumoniae",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-employee-detail-nursing-home-staffing",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-07-27",
+            "temporal": "2020-04-01/2024-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-31",
+            "references": [
+                "https://data.cms.gov/resources/payroll-based-journal-employee-detail-nursing-home-staffing-methodology"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/d65b8be0-946e-410b-ab06-01829628d5a1/data-viewer",
+            "description": "The Payroll Based Journal (PBJ) Employee Detail Nursing Home Staffing dataset provides information submitted by nursing homes including rehabilitation services on a quarterly basis. The data include a system generated employee identification number, work date, job type and employment status, and hours worked for each nursing home employee.\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Payroll Based Journal Employee Detail Nursing Home Staffing",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d65b8be0-946e-410b-ab06-01829628d5a1/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/a284dec3-92da-4de4-a1a2-3c91e15c43e7/PBJ_employeedetail_CY2024Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d99a572e-e50e-46e4-9be2-0eddb5963701/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/de75a2ea-6ec2-4166-9f6b-6ac3ffd009b4/PBJ_employeedetail_CY2024Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee686e84-d778-48bf-b78a-1cec8a36923a/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/b84e5743-bd7b-4870-bc5d-90926e0f8553/PBJ_employeedetail_CY2023Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/86f6f9ad-2cb2-447c-b460-cf4f819fea7c/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/009f82da-932f-4daf-82dc-25f33b655a45/PBJ_employeedetail_CY2023Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f3fd4a00-c808-4e34-9464-68a50be7c69c/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/227f42ad-b125-475d-abf1-6ecf3c53e086/PBJ_employeedetail_CY2023Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c9fecee7-46b8-4ae6-98a6-c90a6ca8e745/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/0ff00eb9-e032-49ab-9f19-5f6e0977321f/PBJ_employeedetail_CY2023Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/700daa22-b84d-46b4-8495-a43512a5fec2/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/PBJ_employeedetail_CY2022Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/91c55823-f84a-4b68-b770-9f594f9e776f/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/PBJ_employeedetail_CY2022Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a6fb781f-0503-4e4f-8cd6-9afbcbd77156/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/1457ac40-92cb-4155-830b-e6819c0e70c9/PBJ_employeedetail_CY2022Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ecb5f45a-1620-4db6-bd07-53a8b58835a3/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/d1804d50-aea7-4573-bd63-1b7c47b82d12/PBJ_employeedetail_CY2022Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/de95ae4c-73b5-4824-80d2-5ae1558f9249/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2022-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/87d0cbf1-a0c8-4058-aa9e-70e8e982db9e/PBJ_employeedetail_CY2021Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/24e7953e-ed2a-4931-a272-a4c0995c4865/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/5aff92dc-fa72-47dd-b438-a5b4791666db/PBJ_employeedetail_CY2021Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee4d7788-1cf7-44da-b419-d126d9138bec/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/3abaf7b3-5dea-41bc-bc3f-99f0406531d9/PBJ_employeedetail_CY2021Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2a017680-ef59-4fbf-beeb-8b2d69266c3f/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/b432a28e-bdc6-4020-9b5c-72c6625bc302/PBJ_employeedetail_CY2021Q1_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/942d7734-4401-4372-a5be-3c9d32996f14/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2021-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/67d9a38e-8ef4-43ba-8785-f344d2e1d66e/PBJ_employeedetail_CY2020Q4_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2020-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3b8ff726-23e5-493f-8fac-a3c8e759af69/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2020-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/0d9eec4f-2fc4-4af1-8cc9-de66d182f66b/PBJ_employeedetail_CY2020Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2020-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2a10d692-a0bf-48c3-aa2d-98283c26588d/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2020-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/f61b8bd0-c4d4-4d18-835f-c1a57c723659/PBJ_employeedetail_CY2020Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2020-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0309f7d8-d639-49eb-9c22-2acd8f571879/data",
+                    "mediaType": "text/html",
+                    "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2020-06-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-employee-detail-nursing-home-staffing-data-dictionary",
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
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/vtwh-v35w",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vtwh-v35w",
+            "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Registry Number Update Report lists changes to Registry Numbers on a Descriptor or Supplementary Concept Record (SCR).  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
+            "title": "MeSH 2025 Update - Registry Number Update Report",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vtwh-v35w/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vtwh-v35w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vtwh-v35w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vtwh-v35w/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/irpc-yf8f",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenza",
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
+            "identifier": "https://data.cdc.gov/api/views/irpc-yf8f",
+            "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Data for Haemophilus influenzae (age <5 for serotype b, nontypeable, non-b serotype, and unknown serotype) are available in Table I.",
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/w79a-dgrh",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
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
+            "identifier": "https://data.cdc.gov/api/views/w79a-dgrh",
+            "description": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w79a-dgrh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w79a-dgrh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w79a-dgrh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w79a-dgrh/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2013",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626",
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.</p>\n<p>Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.<br />\nThis study has 1 Data Set.</p>",
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2013)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2013) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#trends",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-06",
+            "@type": "dcat:Dataset",
+            "temporal": "Data from 2020-03-14 to present (posted starting 2023-06-06)",
+            "modified": "2025-01-30",
+            "references": [
+                "https://covid.cdc.gov/covid-data-tracker/"
+            ],
+            "keyword": [
+                "covid19",
+                "nrevss",
+                "test"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Virologic Unit, Surveillance and Analytics Team",
+                "hasEmail": "mailto:nrevss@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/gvsb-yw6g",
+            "description": "More than 450 public health and clinical laboratories located throughout the United States participate in surveillance for severe acute respiratory virus coronavirus type 2 (SARS-CoV-2), the virus that causes COVID-19, through CDC's National Respiratory and Enteric Virus Surveillance System (NREVSS). The dataset contains a weekly summary of aggregate counts of the total SARS-CoV-2 tests and SARS-CoV-2 detections reported to NREVSS since March 14, 2020. These data are reported weekly on a voluntary basis. Clinical laboratories do not report demographic data through NREVSS. Testing practices may vary regionally, and the number of participating laboratories may change from year to year. Results can be changed for up to 2 years after the initial reporting week. However, discrepancies may be noted and updated at the discretion of the data stewards and key stakeholders.\n\nWhile NREVSS strives to present the most precise estimates of respiratory viral trends with reporting burden minimized for participating laboratories, there are several inherent limitations to this surveillance system.\n\nNREVSS does not collect patient-specific data or demographic information. Multiple samples may be collected from a single patient, so NREVSS results do not necessarily reflect the number of patients tested, nor do they directly reflect hospitalizations or deaths related to COVID-19.\n\nParticipating laboratories vary in size, testing capabilities, and areas served. Some institutions may receive and test samples from sites across a given state or even from multiple states. Without direct knowledge of the population base, NREVSS cannot be used to determine the prevalence or incidence of infection.\n\nFor more information on NREVSS and COVID-19 surveillance please visit: https://www.cdc.gov/surveillance/nrevss. These data appear starting May 25, 2023 on the CDC COVID Data Tracker at the following URLs: https://covid.cdc.gov/covid-data-tracker/#trends ; https://covid.cdc.gov/covid-data-tracker/#cases.   \n\nNREVSS data are reported at the national and HHS regional levels. The ten (10) U.S. Department of HHS regions are defined here: https://www.hhs.gov/about/agencies/iea/regional-offices/index.html. \n\nThe data represent SARS-CoV-2 Nucleic Acid Amplification Test (NAAT) results, which include reverse transcriptase-polymerase chain reaction (RT-PCR) tests from a voluntary, sentinel network of participating laboratories in the United States, including clinical, public health and commercial laboratories (https://www.cdc.gov/surveillance/nrevss/labs/index.html). \n\nThese data exclude antigen, antibody, and at-home test results. \n\nAll data are provisional and subject to change. Reporting is less complete for the past 1 week, and more complete (>90%) for the period 2 weeks earlier. \n\nThere are data from all states across the 10 HHS regions. Because the data are from a sentinel network of laboratories, however, results may vary geographically. The data do not include all test results within a jurisdiction and therefore do not reflect all SARS-CoV-2 NAATs administered in the United States. \n\nPercent positivity is one of the surveillance metrics used to monitor COVID-19 transmission over time and by area. Percent positivity is calculated by dividing the number of positive NAATs by the total number of NAATs administered, then multiplying by 100 [(# of positive NAAT tests / total NAAT tests) x 100].\n\nThe data represent laboratory tests performed, not individual (deduplicated) results in people. In the table and upon hovering on the map, the total test counts in the data reflect the latest data reported from NREVSS laboratories and may not match the data presented by various jurisdictions.\n\nOn May 11, 2023, CDC discontinued utilizing the COVID electronic laboratory reporting (CELR) platform as the primary laboratory source of COVID-19 results. These data are archived at health.data.gov.\n\nFor more information about NREVSS, please see: https://www.cdc.gov/surveillance/nrevss/",
+            "title": "Percent Positivity of COVID-19 Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/medlineplus-connect-electronic-health-record-ehr-systems-web-application",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "biomedical research",
+                "connect",
+                "ehr",
+                "ehrs",
+                "electronic health records",
+                "electronic medical records",
+                "emr",
+                "emrs",
+                "health",
+                "health services",
+                "icd-9",
+                "infobutton",
+                "loinc",
+                "medicine",
+                "medlineplus",
+                "ndc",
+                "patient education",
+                "patient health records",
+                "phr",
+                "phrs",
+                "rxnorm",
+                "snowmed ct",
+                "wellness"
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
+            "identifier": "f15aa02b-4129-4abc-b1f4-d74896ac7c5a",
+            "description": "<p>A Web application that allows patient portals and electronic health record (EHR) systems to use existing code sets to link to relevant, authoritative health information from MedlinePlus.gov.  Matches ICD-9-CM or SNOMED CT codes to related MedlinePlus consumer health information, LOINC codes to information on lab tests, and also matches NDC, RXCUI or text strings to patient medication information.</p>",
+            "title": "MedlinePlus Connect for Electronic Health Record (EHR) Systems - Web Application",
+            "programCode": [
+                "009:046"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nlm.nih.gov/medlineplus/connect/application.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool"
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
+            "landingPage": "https://data.cdc.gov/d/azpx-5hzx",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
```

