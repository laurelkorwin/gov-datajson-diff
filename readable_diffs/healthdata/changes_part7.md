# Change History for healthdata.json (Part 7)

### Changes from 31606f9 to dd2190f (Part 6/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
             "description": "NNDSS - Table II. Shiga toxin to Shigellosis - 2015.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Includes E. coli O157:H7; Shiga toxin-positive, serogroup non-O157; and Shiga toxin-positive, not serogrouped.",
-            "title": "NNDSS - Table II. Shiga toxin to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73302,21 +73278,58 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n3wf-wtep",
+            "issued": "2016-01-07",
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
+            "landingPage": "https://data.cdc.gov/d/n3wf-wtep",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Shiga toxin to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-bridged-race-july-1st-estimates",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
+            "description": "<p>The Population - Bridged-Race July 1st Estimates online databases report bridged-race population estimates of the July 1st resident population of the United States, based on Census 2000 counts, for use in calculating vital rates. These estimates result from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) standards for the collection of data on race and ethnicity, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White). Many data systems, such as vital statistics, are continuing to use the 1977 OMB standards during the transition to full implementation of the 1997 OMB standards. Postcensal estimates are available for year 2000 - 2009; intercensal estimates are available for the years 1990-1999.  Obtain population counts by  Year, State, County, Race (4-categories), Ethnicity, Sex and Age (1-year or 5-year groups).   The data are released by the National Center for Health Statistics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/bridged-race-population.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "7461968e-5c85-451b-a38b-26c540c7b802",
             "issued": "2012-05-30",
-            "temporal": "1990-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "age",
                 "county",
@@ -73328,77 +73341,34 @@
                 "state",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-bridged-race-july-1st-estimates",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "7461968e-5c85-451b-a38b-26c540c7b802",
-            "description": "<p>The Population - Bridged-Race July 1st Estimates online databases report bridged-race population estimates of the July 1st resident population of the United States, based on Census 2000 counts, for use in calculating vital rates. These estimates result from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) standards for the collection of data on race and ethnicity, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White). Many data systems, such as vital statistics, are continuing to use the 1977 OMB standards during the transition to full implementation of the 1997 OMB standards. Postcensal estimates are available for year 2000 - 2009; intercensal estimates are available for the years 1990-1999.  Obtain population counts by  Year, State, County, Race (4-categories), Ethnicity, Sex and Age (1-year or 5-year groups).   The data are released by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Population - Bridged-Race July 1st Estimates",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/bridged-race-population.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1990-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Population - Bridged-Race July 1st Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "city",
-                "disability",
-                "gis",
-                "health",
-                "outcomes",
-                "place",
-                "places",
-                "prevalence",
-                "prevention",
-                "risk",
-                "status"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xx8k-iu94",
             "description": "This dataset contains model-based place (incorporated and census designated places) estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia \u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 36 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
-            "title": "PLACES: Place Data (GIS Friendly Format), 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73421,92 +73391,99 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xx8k-iu94",
+            "issued": "2024-07-15",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: Place Data (GIS Friendly Format), 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/gr95-7mnn",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "8a655f73-c702-571c-9bb0-f100c4323e5d",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "8a655f73-c702-571c-9bb0-f100c4323e5d",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/gr95-7mnn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ahrf-yqdt",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2024-10-04",
-            "@type": "dcat:Dataset",
-            "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-17",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "disease burden",
-                "hospitalizations",
-                "illnesses",
-                "outpatient visits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ahrf-yqdt",
             "description": "This dataset represents preliminary estimates of cumulative U.S. COVID-19 disease burden for the 2024-2025 period, including illnesses, outpatient visits, hospitalizations, and deaths. The weekly COVID-19-associated burden estimates are preliminary and based on continuously collected surveillance data from patients hospitalized with laboratory-confirmed severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) infections. The data come from the Coronavirus Disease 2019 (COVID-19)-Associated Hospitalization Surveillance Network (COVID-NET), a surveillance platform that captures data from hospitals that serve about 10% of the U.S. population. Each week CDC estimates a range (i.e., lower estimate and an upper estimate) of COVID-19 -associated burden that have occurred since October 1, 2024. \n\n<b>Note:</b> Data are preliminary and subject to change as more data become available. Rates for recent COVID-19-associated hospital admissions are subject to reporting delays; as new data are received each week, previous rates are updated accordingly.\n\n<b>References</b>\n<ol><li>Reed C, Chaves SS, Daily Kirley P, et al. Estimating influenza disease burden from population-based surveillance data in the United States. PLoS One. 2015;10(3):e0118369. https://doi.org/10.1371/journal.pone.0118369\u202f </li><li>Rolfes, MA, Foppa, IM, Garg, S, et al. Annual estimates of the burden of seasonal influenza in the United States: A tool for strengthening influenza surveillance and preparedness. Influenza Other Respi Viruses. 2018; 12: 132\u2013 137. https://doi.org/10.1111/irv.12486</li><li>Tokars  JI, Rolfes  MA, Foppa  IM, Reed  C.  An evaluation and update of methods for estimating the number of influenza cases averted by vaccination in the United States.   Vaccine. 2018;36(48):7331-7337. doi:10.1016/j.vaccine.2018.10.026\u202f</li><li>Collier SA, Deng L, Adam EA, Benedict KM, Beshearse EM, Blackstock AJ, Bruce BB, Derado G, Edens C, Fullerton KE, Gargano JW, Geissler AL, Hall AJ, Havelaar AH, Hill VR, Hoekstra RM, Reddy SC, Scallan E, Stokes EK, Yoder JS, Beach MJ. Estimate of Burden and Direct Healthcare Cost of Infectious Waterborne Disease in the United States. Emerg Infect Dis. 2021 Jan;27(1):140-149. doi: 10.3201/eid2701.190676. PMID: 33350905; PMCID: PMC7774540.</li><li>Reed C, Kim IK, Singleton JA,\u202f et al. Estimated influenza illnesses and hospitalizations averted by vaccination\u2013United States, 2013-14 influenza season. MMWR Morb Mortal Wkly Rep. 2014 Dec 12;63(49):1151-4. https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6349a2.htm\u202f</li><li>Reed C, Angulo FJ, Swerdlow DL, et al. Estimates of the Prevalence of Pandemic (H1N1) 2009, United States, April\u2013July 2009. Emerg Infect Dis. 2009;15(12):2004-2007. https://dx.doi.org/10.3201/eid1512.091413 \u202f</li><li>Devine O, Pham H, Gunnels B, et al. Extrapolating Sentinel Surveillance Information to Estimate National COVID-19 Hospital Admission Rates: A Bayesian Modeling Approach. Influenza and Other Respiratory Viruses. https://onlinelibrary.wiley.com/doi/10.1111/irv.70026. Volume18, Issue10. October 2024.</li><li><a ref=\"https://www.cdc.gov/covid/php/covid-net/index.html\">COVID-NET | COVID-19 | CDC\u202f</a></li><li>https://www.cdc.gov/covid/hcp/clinical-care/systematic-review-process.html\u202f </li><li><a ref=\"https://academic.oup.com/pnasnexus/article/1/3/pgac079/6604394?login=false\">Excess natural-cause deaths in California by cause and setting: March 2020 through February 2021 | PNAS Nexus | Oxford Academic (oup.com)</a></li><li>Kruschke, J. K. 2011. Doing Bayesian data analysis: a tutorial with R and BUGS. Elsevier, Amsterdam, Section 3.3.5.</li></ol>",
-            "title": "Preliminary 2024-2025 U.S. COVID-19 Burden Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73529,94 +73506,93 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/ahrf-yqdt",
+            "issued": "2024-10-04",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "disease burden",
+                "hospitalizations",
+                "illnesses",
+                "outpatient visits"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ahrf-yqdt",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "October 1, 2024 - no specified end date",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Preliminary 2024-2025 U.S. COVID-19 Burden Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/grua-wsci",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "9dcfc4fd-2d71-55fc-bd59-7b7524186c88",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure_value v2.11.18 (etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/measure_value.csv",
-                    "description": "Scorecard measure_value v2.11.18 (etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure_value v2.11.18 (etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure_value v2.11.18 (etl-test)"
                 }
             ],
+            "identifier": "9dcfc4fd-2d71-55fc-bd59-7b7524186c88",
+            "issued": "2023-04-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/grua-wsci",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard measure_value v2.11.18 (etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xv7k-8e7s",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "shiga toxin-producing e. coli",
-                "shigellosis",
-                "stec",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xv7k-8e7s",
             "description": "NNDSS - Table II. Shiga toxin to Shigellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.   Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n \r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.   Data for TB are displayed in Table IV, which appears quarterly.  \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table II to facilitate case count verification with reporting jurisdictions.\r\n\u00a7 Includes E. coli O157:H7; Shiga toxin-positive, serogroup non-O157; and Shiga toxin-positive, not serogrouped.",
-            "title": "NNDSS - Table II. Shiga toxin to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73639,49 +73615,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xv7k-8e7s",
+            "issued": "2017-01-05",
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
+            "landingPage": "https://data.cdc.gov/d/xv7k-8e7s",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Shiga toxin to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/prov-county-drug-overdose.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-01/2024-06-30",
-            "modified": "2025-01-15",
-            "keyword": [
-                "county",
-                "deaths",
-                "drug",
-                "drug overdose",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "united states",
-                "vsrr"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gb4e-yj24",
             "description": "This data visualization presents county-level provisional counts for drug overdose deaths based on a current flow of mortality data in the National Vital Statistics System. County-level provisional counts include deaths occurring within the 50 states and the District of Columbia, as of the date specified and may not include all deaths that occurred during a given time period. Provisional counts are often incomplete and causes of death may be pending investigation resulting in an underestimate relative to final counts (see Technical Notes).\n\nThe provisional data presented on the dashboard below include reported 12 month-ending provisional counts of death due to drug overdose by the decedent\u2019s county of residence and the month in which death occurred.\n\nPercentages of deaths with a cause of death pending further investigation and a note on historical completeness (e.g. if the percent completeness was under 90% after 6 months) are included to aid in interpretation of provisional data as these measures are related to the accuracy of provisional counts (see Technical Notes). Counts between 1-9 are suppressed in accordance with NCHS confidentiality standards. Provisional data presented on this page will be updated on a quarterly basis as additional records are received.\n\nTechnical Notes\n\nNature and Sources of Data\n\nProvisional drug overdose death counts are based on death records received and processed by the National Center for Health Statistics (NCHS) as of a specified cutoff date. The cutoff date is generally the first Sunday of each month. National provisional estimates include deaths occurring within the 50 states and the District of Columbia. NCHS receives the death records from the state vital registration offices through the Vital Statistics Cooperative Program (VSCP).\n\nThe timeliness of provisional mortality surveillance data in the National Vital Statistics System (NVSS) database varies by cause of death and jurisdiction in which the death occurred. The lag time (i.e., the time between when the death occurred and when the data are available for analysis) is longer for drug overdose deaths compared with other causes of death due to the time often needed to investigate these deaths (1). Thus, provisional estimates of drug overdose deaths are reported 6 months after the date of death.\n\nProvisional death counts presented in this data visualization are for \u201c12 month-ending periods,\u201d defined as the number of deaths occurring in the 12 month period ending in the month indicated. For example, the 12 month-ending period in June 2020 would include deaths occurring from July 1, 2019 through June 30, 2020. The 12 month-ending period counts include all seasons of the year and are insensitive to reporting variations by seasonality. These provisional counts of drug overdose deaths and related data quality metrics are provided for public health surveillance and monitoring of emerging trends. Provisional drug overdose death data are often incomplete, and the degree of completeness varies by jurisdiction and 12 month-ending period. Consequently, the numbers of drug overdose deaths are underestimated based on provisional data relative to final data and are subject to random variation.\n\nCause of Death Classification and Definition of Drug Deaths\n\nMortality statistics are compiled in accordance with the World Health Organizations (WHO) regulations specifying that WHO member nations classify and code causes of death with the current revision of the International Statistical Classification of Diseases and Related Health Problems (ICD). ICD provides the basic guidance used in virtually all countries to code and classify causes of death. It provides not only disease, injury, and poisoning categories but also the rules used to select the single underlying cause of death for tabulation from the several diagnoses that may be reported on a single death certificate, as well as definitions, tabulation lists, the format of the death certificate, and regul",
-            "title": "VSRR Provisional County-Level Drug Overdose Death Counts",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73704,44 +73677,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/gb4e-yj24",
+            "issued": "2021-10-05",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/prov-county-drug-overdose.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2015-01-01/2024-06-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "VSRR Provisional County-Level Drug Overdose Death Counts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "vsd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ph8r-wzxn",
             "description": "\u2022 Weekly Cumulative Doses (in Millions) of Influenza Vaccines Distributed by Season in the United States. \n\n\u2022 Archived data are available here: https://data.cdc.gov/resource/e5zk-7tx5\n\n\u2022 Influenza vaccine is produced by private manufacturers. Additional information is available at https://www.cdc.gov/flu/prevent/vaccine-supply-distribution.htm. These data are submitted to CDC by current U.S.\u2500 licensed manufacturers of influenza vaccine and a subset of influenza vaccine wholesalers and distributors that receive vaccine directly from these manufacturers. These data are not projected but approximate all influenza vaccines distributed in the United States.\n\n\u2022 Additional information is available:\u202fhttps://www.cdc.gov/flu/prevent/vaccine-supply-distribution.htm.",
-            "title": "Weekly Cumulative Doses (in Millions) of Influenza Vaccines Distributed by Season, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73764,51 +73744,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ph8r-wzxn",
+            "issued": "2024-10-01",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2024-2025",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Doses (in Millions) of Influenza Vaccines Distributed by Season, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/r9mz-pvtk",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "all ages",
-                "confirmed",
-                "invasive pneumococcal disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/r9mz-pvtk",
             "description": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\n\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73831,43 +73807,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r9mz-pvtk",
+            "issued": "2020-01-21",
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
+            "landingPage": "https://data.cdc.gov/d/r9mz-pvtk",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2011-02-01",
-            "keyword": [
-                "community health",
-                "drug",
-                "fda",
-                "label",
-                "label repository",
-                "labels fda gov"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FDA Enterprise Data Inventory",
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "c447002d-51df-46d9-a105-dda94dfd6083",
             "description": "This file contains the data elements used for searching the FDA Online Data Repository including proprietary name, active ingredients, marketing application number or regulatory citation, National Drug Code, and company name.",
-            "title": "FDA Drug Label Data",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73875,44 +73854,40 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "c447002d-51df-46d9-a105-dda94dfd6083",
+            "issued": "2021-02-25",
+            "keyword": [
+                "community health",
+                "drug",
+                "fda",
+                "label",
+                "label repository",
+                "labels fda gov"
+            ],
+            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2011-02-01",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "FDA Drug Label Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mwkk-wzmy",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "confirmed",
-                "hepatitis b",
-                "hepatitis c acute",
-                "nedss",
-                "netss",
-                "nndss",
-                "perinatal infection",
-                "probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mwkk-wzmy",
             "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73935,46 +73910,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mwkk-wzmy",
+            "issued": "2021-01-21",
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
+            "landingPage": "https://data.cdc.gov/d/mwkk-wzmy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7xvh-y5vh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-10",
-            "keyword": [
-                "covid-19",
-                "executive order",
-                "gathering bans",
-                "government order",
-                "legal epidemiology",
-                "mitigation",
-                "proclamation",
-                "public health order",
-                "social distancing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:cak8@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7xvh-y5vh",
             "description": "State and territorial executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications are collected from government websites and cataloged and coded using Microsoft Excel by one or more coders with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states and territories were subject to executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications related to  COVID-19 banning gatherings of various sizes either (1) generally, or specified that the gathering limit applied only when social distancing was not possible, or (2) even if participants practiced social distancing.\n\nThese data are derived from on the publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly ban gatherings found by the CDC, COVID-19 Community Intervention and Critical Populations Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through August 15, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded, as well as official government communications such as announcements that counties have progressed through new phases of reopening pursuant to an executive order, directive, or other executive branch action, and posted to government websites; news media reports on restrictions were excluded. Recommendations and guidance documents not included or adopted by reference in an order are not included in these data. These data do not include mandatory business closures, curfews, or requirements/recommendations for people to stay in their homes. Due to limitations of the National Environmental Public Health Tracking Network Data Explorer, these data do not include tribes or cities, nor was a distinction made between county orders that applied county-wide versus those that were limited to unincorporated areas of the county. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Gathering Bans: March 11, 2020-August 15, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73997,38 +73973,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7xvh-y5vh",
+            "issued": "2021-09-10",
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
+            "landingPage": "https://data.cdc.gov/d/7xvh-y5vh",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-09-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Policy Surveillance"
-            ]
+            ],
+            "title": "U.S. State and Territorial Gathering Bans: March 11, 2020-August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/guzr-wp6x",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2018-07-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "927f4847-2c0a-50c1-8f50-9103de7d048b",
             "description": "Number of Managed Care Programs Enrolling Certain Populations on a Mandatory or Voluntary Basis at any point in 2022",
-            "title": "Managed Care Features By Enrollment Population",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74037,25 +74022,52 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "927f4847-2c0a-50c1-8f50-9103de7d048b",
+            "issued": "2018-07-11",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/guzr-wp6x",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-10-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Managed Care Features By Enrollment Population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2020",
-            "modified": "2024-05-02",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nhcs/2020-NHCS-PUF-Tech-Doc-508.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-INPATIENT-CODEBOOK-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-ED-CODEBOOK-508.pdf",
+            "describedByType": "application/pdf",
+            "description": "As a principal source of information on health care utilization in the United States, NHCS collects inpatient and emergency department data from a nationally representative sample of U.S. hospitals sourced from administrative and electronic health records data. The 2020 NHCS is conducted by the National Center for Health Statistics (NCHS) and is a member of the National Health Care Surveys \u2013 a family of surveys which measure health care utilization across a variety of health care providers and settings.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Inpatient and emergency department datasets are available for SAS, STATA, AND R at the link below.",
+                    "downloadURL": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+                    "mediaType": "text/html",
+                    "title": "2020 NATIONAL HOSPITAL CARE SURVEY"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jdch-es95",
+            "issued": "2024-04-03",
             "keyword": [
                 "electronic health records",
                 "emergency departments",
@@ -74066,118 +74078,85 @@
                 "nhcs",
                 "united states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-02",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/jdch-es95",
-            "description": "As a principal source of information on health care utilization in the United States, NHCS collects inpatient and emergency department data from a nationally representative sample of U.S. hospitals sourced from administrative and electronic health records data. The 2020 NHCS is conducted by the National Center for Health Statistics (NCHS) and is a member of the National Health Care Surveys \u2013 a family of surveys which measure health care utilization across a variety of health care providers and settings.",
-            "title": "National Hospital Care Survey, 2020 public-use file",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
-                    "description": "Inpatient and emergency department datasets are available for SAS, STATA, AND R at the link below.",
-                    "@type": "dcat:Distribution",
-                    "title": "2020 NATIONAL HOSPITAL CARE SURVEY"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/nhcs/2020-NHCS-PUF-Tech-Doc-508.pdf"
             ],
             "spatial": "United States",
-            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-INPATIENT-CODEBOOK-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-ED-CODEBOOK-508.pdf",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey, 2020 public-use file"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/gv77-cetz",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-12",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "6e9ec91c-c298-5a59-bc0a-51f3b20f6c80",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt pillar v2.10.16 (coreset-dev0)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/pillar.csv",
-                    "description": "CoreSEt pillar v2.10.16 (coreset-dev0)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt pillar v2.10.16 (coreset-dev0)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt pillar v2.10.16 (coreset-dev0)"
                 }
             ],
+            "identifier": "6e9ec91c-c298-5a59-bc0a-51f3b20f6c80",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/gv77-cetz",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt pillar v2.10.16 (coreset-dev0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/art/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-30",
-            "keyword": [
-                "art",
-                "assisted reproductive technology",
-                "clinic",
-                "fertility",
-                "infertility",
-                "services",
-                "success rates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ARTINFO",
                 "hasEmail": "mailto:ARTINFO@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/knu9-e7pg",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/knu9-e7pg",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Patient and Cycle Characteristics dataset summarizes the types of ART services performed and the kinds of patients who received ART procedures in a specific clinic. Please note patient characteristics are presented per cycle rather than per patient. As a result, patients who had more than one ART cycle within the reporting year are represented more than once.",
-            "title": "2020 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74200,49 +74179,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/knu9-e7pg",
+            "identifier": "https://data.cdc.gov/api/views/knu9-e7pg",
+            "issued": "2023-07-18",
+            "keyword": [
+                "art",
+                "assisted reproductive technology",
+                "clinic",
+                "fertility",
+                "infertility",
+                "services",
+                "success rates"
+            ],
+            "landingPage": "https://www.cdc.gov/art/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Assisted Reproductive Technology (ART)"
-            ]
+            ],
+            "title": "2020 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-va.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-12-09",
-            "@type": "dcat:Dataset",
-            "temporal": "2015/2020",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Linked-VA-Match-File.pdf"
-            ],
-            "keyword": [
-                "linked va files",
-                "nhcs",
-                "research-data-center",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCHS Data Linkage Program",
                 "hasEmail": "mailto:DataLinkage@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vaca-65fb",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with administrative data from the Department of Veterans Affairs (VA). NHCS data have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training and veteran readiness (vocational rehabilitation), and employment benefit programs.",
-            "title": "National Hospital Care Survey (NHCS) linked to Department of Veterans Affairs Administrative Data Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 9) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS-VA-Linkage-Methods-and-Analytic-Considerations.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with administrative data from the Department of Veterans Affairs (VA). NHCS data have been linked to VA administrative data containing information on details of active-duty service in the United States uniformed services (such as branch of service and era of active-duty service) and VA benefit program utilization including VA health care, service-connected disability compensation, pension, VA guaranteed home loan program, life insurance, education, training and veteran readiness (vocational rehabilitation), and employment benefit programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74250,47 +74226,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 9) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS-VA-Linkage-Methods-and-Analytic-Considerations.pdf",
+            "identifier": "https://data.cdc.gov/api/views/vaca-65fb",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-12-09",
+            "keyword": [
+                "linked va files",
+                "nhcs",
+                "research-data-center",
+                "veterans"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-va.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Linked-VA-Match-File.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "2015/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey (NHCS) linked to Department of Veterans Affairs Administrative Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/tv5g-74as",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "hepatitis c",
-                "influenza-associated pediatric mortality",
-                "nedss",
-                "netss",
-                "nndss",
-                "perinatal infection",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tv5g-74as",
             "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Since [INSERT DATE], XXX influenza-associated pediatric deaths occurring during the 2017-18 season have been reported.",
-            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74313,46 +74290,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tv5g-74as",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/tv5g-74as",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-04",
-            "references": [
-                "https://www.census.gov/programs-surveys/acs/data.html",
-                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
-            ],
-            "keyword": [
-                "acs",
-                "county",
-                "estimates",
-                "places",
-                "sdoh"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/i6u4-y3g4",
             "description": "This dataset contains county-level social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service:  https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
-            "title": "SDOH Measures for County, ACS 2017-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74375,45 +74351,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i6u4-y3g4",
+            "issued": "2023-11-16",
+            "keyword": [
+                "acs",
+                "county",
+                "estimates",
+                "places",
+                "sdoh"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-12-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.census.gov/programs-surveys/acs/data.html",
+                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "SDOH Measures for County, ACS 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ehf4-c7tw",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "legionellosis",
-                "leptospirosis",
-                "listeriosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ehf4-c7tw",
             "description": "NNDSS - TABLE 1U. Legionellosis to Listeriosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1U. Legionellosis to Listeriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74436,21 +74413,57 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ehf4-c7tw",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/ehf4-c7tw",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1U. Legionellosis to Listeriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-bridged-race-july-1st-estimates-0",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
+            "description": "<p>The Population - Bridged-Race July 1st Estimates online databases report bridged-race population estimates of the July 1st resident population of the United States, based on Census 2000 counts, for use in calculating vital rates. These estimates result from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) standards for the collection of data on race and ethnicity, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White). Many data systems, such as vital statistics, are continuing to use the 1977 OMB standards during the transition to full implementation of the 1997 OMB standards. Postcensal estimates are available for year 2000 - 2009; intercensal estimates are available for the years 1990-1999. Obtain population counts by Year, State, County, Race (4-categories), Ethnicity, Sex and Age (1-year or 5-year groups). The data are released by the National Center for Health Statistics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/bridged-race-population.html",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "identifier": "c4c88d50-56af-4f58-bd10-6f234e2b3125",
             "issued": "2012-07-31",
-            "temporal": "1990-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "age",
                 "county",
@@ -74462,76 +74475,35 @@
                 "state",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-bridged-race-july-1st-estimates-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "c4c88d50-56af-4f58-bd10-6f234e2b3125",
-            "description": "<p>The Population - Bridged-Race July 1st Estimates online databases report bridged-race population estimates of the July 1st resident population of the United States, based on Census 2000 counts, for use in calculating vital rates. These estimates result from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) standards for the collection of data on race and ethnicity, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White). Many data systems, such as vital statistics, are continuing to use the 1977 OMB standards during the transition to full implementation of the 1997 OMB standards. Postcensal estimates are available for year 2000 - 2009; intercensal estimates are available for the years 1990-1999. Obtain population counts by Year, State, County, Race (4-categories), Ethnicity, Sex and Age (1-year or 5-year groups). The data are released by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Population - Bridged-Race July 1st Estimates",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/bridged-race-population.html",
-                    "mediaType": "text/html",
-                    "title": "Text "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1990-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Population - Bridged-Race July 1st Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "gis",
-                "health",
-                "outcomes",
-                "places",
-                "prevalence",
-                "prevention",
-                "risk",
-                "status",
-                "zcta",
-                "zip code"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9xb7-9z99",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 29 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
-            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74554,142 +74526,148 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "identifier": "https://data.cdc.gov/api/views/9xb7-9z99",
+            "issued": "2022-10-11",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2021 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/gxrm-5qet",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-06-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_prodauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "0f4dd698-2ac9-5a6c-bbd2-c7d23f4110e8",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_files_allDownloadsSSBtn",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/files_allDownloadsSSBtn.csv",
-                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/files_allDownloadsSSBtn.csv",
+                    "mediaType": "text/csv",
                     "title": "files_allDownloadsSSBtn csv file"
                 }
             ],
+            "identifier": "0f4dd698-2ac9-5a6c-bbd2-c7d23f4110e8",
+            "issued": "2022-06-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/gxrm-5qet",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "prodAuto_files_allDownloadsSSBtn"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/gyk2-ne97",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_devauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "8f77310d-ef45-5bb6-bcb0-6da9a1bdb3cd",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_fileType_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/fileType_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/fileType_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "fileType_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "8f77310d-ef45-5bb6-bcb0-6da9a1bdb3cd",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/gyk2-ne97",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "devAuto_fileType_measureDisplayGroups"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/t6u2-f84c",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-13",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-01-01/Present",
-            "modified": "2025-01-13",
-            "keyword": [
-                "deaths",
-                "drug overdose",
-                "firearm injury",
-                "homicide",
-                "mortality",
-                "nchs",
-                "suicide"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIPC",
                 "hasEmail": "mailto:injurydashboard@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/t6u2-f84c",
             "description": "This file contains death counts and death rates for drug overdose, suicide, homicide and firearm injuries at the United States national level (additional datasets exist for other levels of geography). The data is grouped by 3 different time periods including monthly, yearly, and trailing twelve months. Please see data dictionary for intents and mechanisms included in each measure.",
-            "title": "Mapping Injury, Overdose, and Violence - National",
-            "programCode": [
-                "009:033"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74712,23 +74690,71 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/t6u2-f84c",
+            "issued": "2025-01-13",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "firearm injury",
+                "homicide",
+                "mortality",
+                "nchs",
+                "suicide"
+            ],
+            "landingPage": "https://data.cdc.gov/d/t6u2-f84c",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:033"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2019-01-01/Present",
             "theme": [
                 "Injury & Violence"
-            ]
+            ],
+            "title": "Mapping Injury, Overdose, and Violence - National"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/mortality.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Provisional estimates of death rates. Estimates are presented for each of the 15 leading causes of death plus estimates for deaths attributed to drug overdose, falls (for persons aged 65 and over), human immunodeficiency virus (HIV) disease, homicide, and firearms-related deaths.",
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
+            "identifier": "https://data.cdc.gov/api/views/489q-934x",
             "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-04-01/2024-06-30",
-            "modified": "2025-01-14",
             "keyword": [
                 "age",
                 "age group",
@@ -74770,79 +74796,35 @@
                 "united states",
                 "vsrr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/489q-934x",
-            "description": "Provisional estimates of death rates. Estimates are presented for each of the 15 leading causes of death plus estimates for deaths attributed to drug overdose, falls (for persons aged 65 and over), human immunodeficiency virus (HIV) disease, homicide, and firearms-related deaths.",
-            "title": "NCHS - VSRR Quarterly provisional estimates for selected indicators of mortality",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/mortality.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-14",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/489q-934x/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2022-04-01/2024-06-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - VSRR Quarterly provisional estimates for selected indicators of mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ucum.nlm.nih.gov/ucum-lhc/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "health data standards",
-                "terminologies",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bat9-dmve",
             "description": "A JavaScript package that can be included in webpages or programs and used for validating and converting unit expressions from the Unified Code for Units of Measure (UCUM).",
-            "title": "UCUM-LHC",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74851,48 +74833,41 @@
                     "title": "UCUM-LHC - GitHub repository"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bat9-dmve",
+            "issued": "2021-06-30",
+            "keyword": [
+                "health data standards",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "landingPage": "https://ucum.nlm.nih.gov/ucum-lhc/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "UCUM-LHC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2vpi-n544",
+            "accrualPeriodicity": "Archived",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-11-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13 to 2021-11-17",
-            "modified": "2022-09-28",
-            "references": [
-                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
-            ],
-            "keyword": [
-                "administration",
-                "coronavirus",
-                "covid-19",
-                "immunization",
-                "izdl",
-                "report date",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:iisinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2vpi-n544",
             "description": "This data dictionary provides information about archived demographic trend data for people receiving COVID-19 vaccinations in the United States at the national level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities. \n\nThese data have been archived to provide historical demographic trend data for COVID-19 vaccine recipients prior to CDC converting the Vaccination Demographic Trends site to using data based on the date of vaccine administration. Previously, the Vaccination Demographic Trends site presented trend data by the date the vaccination was reported to CDC.",
-            "title": "Archive: COVID-19 Vaccination Demographic Trends by Report Date, National",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74915,40 +74890,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/2vpi-n544",
+            "issued": "2021-11-16",
+            "keyword": [
+                "administration",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "report date",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/2vpi-n544",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Archived",
+            "modified": "2022-09-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13 to 2021-11-17",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Archive: COVID-19 Vaccination Demographic Trends by Report Date, National"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/h43i-y4v2",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-07",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "151e48c4-52e7-4c42-bd9a-4a46b85365a3",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 09-30-2024-to-10-06-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74956,38 +74940,36 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "151e48c4-52e7-4c42-bd9a-4a46b85365a3",
+            "issued": "2024-10-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/h43i-y4v2",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 09-30-2024-to-10-06-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datatools.ahrq.gov",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2022-06-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "insurance",
-                "medical expenditure",
-                "meps"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MEPS Project Director",
                 "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
-            },
-            "identifier": "https://healthdata.gov/api/views/h4d7-8c39",
+            "describedBy": "https://datatools.ahrq.gov/meps-ic#table-series",
             "description": "The Medical Expenditure Panel Survey Insurance Component (MEPS-IC) is an annual survey of private employers and State and local governments. The MEPS-IC produces national and State level estimates of employer-sponsored insurance, including offered plans, costs, employee eligibility, and number of enrollees. PDF files are available for complete sets of table series on employer-based health insurance at the national, state, and metropolitan area levels. The MEPS-IC is sponsored by the Agency for Healthcare Research and Quality and is fielded by the U.S. Census Bureau.",
-            "title": "Medical Expenditure Panel Survey (MEPS) Insurance Component Complete Table Series PDFs",
-            "programCode": [
-                "009:072"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74996,96 +74978,93 @@
                     "title": "PDF Tables"
                 }
             ],
-            "describedBy": "https://datatools.ahrq.gov/meps-ic#table-series"
+            "identifier": "https://healthdata.gov/api/views/h4d7-8c39",
+            "issued": "2022-06-03",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "insurance",
+                "medical expenditure",
+                "meps"
+            ],
+            "landingPage": "https://datatools.ahrq.gov",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "title": "Medical Expenditure Panel Survey (MEPS) Insurance Component Complete Table Series PDFs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/h4eb-shcy",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "4a0b8c8d-3725-5ab7-af6e-a67025589f85",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt state v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/state.csv",
-                    "description": "CoreSEt state v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt state v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt state v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "4a0b8c8d-3725-5ab7-af6e-a67025589f85",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/h4eb-shcy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt state v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-change-of-ownership-owner-information",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-04-21",
-            "temporal": "2022-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "provider enrollment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/a4358712-e910-4eaf-8f24-5e90ba3cf8d0/data-viewer",
-            "description": "The Skilled Nursing Facility (SNF) Change of Ownership (CHOW) - Owner Information dataset provides information on individual and organizational ownership interest and managerial control associated with the buyer and seller organizations, role of the owner, association date, address of the organizational owner and other ownership details.",
-            "title": "Skilled Nursing Facility Change of Ownership - Owner Information",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Skilled Nursing Facility (SNF) Change of Ownership (CHOW) - Owner Information dataset provides information on individual and organizational ownership interest and managerial control associated with the buyer and seller organizations, role of the owner, association date, address of the organizational owner and other ownership details.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a4358712-e910-4eaf-8f24-5e90ba3cf8d0/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a4358712-e910-4eaf-8f24-5e90ba3cf8d0/data",
+                    "mediaType": "text/html",
                     "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2024-12-01"
                 },
                 {
@@ -75233,46 +75212,49 @@
                     "title": "Skilled Nursing Facility Change of Ownership - Owner Information : 2022-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a4358712-e910-4eaf-8f24-5e90ba3cf8d0/data-viewer",
+            "issued": "2022-04-21",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-change-of-ownership-owner-information",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Data_Guidance.pdf"
+            ],
+            "temporal": "2022-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Skilled Nursing Facility Change of Ownership - Owner Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK547852/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-30",
-            "keyword": [
-                "dataset",
-                "environmental health",
-                "toxicology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5fe7-gc6d",
             "description": "Provides up-to-date, accurate, and easily accessed information on the diagnosis, cause, frequency, patterns, and management of liver injury attributable to prescription and nonprescription medications, herbals and dietary supplements.",
-            "title": "LiverTox",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75287,93 +75269,88 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5fe7-gc6d",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "environmental health",
+                "toxicology"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK547852/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-09-30",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Drugs and Chemicals"
-            ]
+            ],
+            "title": "LiverTox"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/h5bv-j4am",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_prodauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "22c72566-87de-5759-90ee-350df11bc89b",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measure_allStates_downloadLink",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates_downloadLink.csv",
-                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates_downloadLink.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates_downloadLink csv file"
                 }
             ],
+            "identifier": "22c72566-87de-5759-90ee-350df11bc89b",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/h5bv-j4am",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
-            "theme": [
-                "Uncategorized"
-            ]
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
             },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rnah-xd9n",
-            "bureauCode": [
-                "009:20"
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "hepatitis c",
-                "influenza-associated pediatric mortality",
-                "nedss",
-                "netss",
-                "nndss",
-                "perinatal infection",
-                "wonder"
+            "theme": [
+                "Uncategorized"
+            ],
+            "title": "prodAuto_measure_allStates_downloadLink"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rnah-xd9n",
             "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Please refer to the CDC WONDER publication for weekly updates to the footnote for this condition.\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75396,55 +75373,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rnah-xd9n",
+            "issued": "2022-01-14",
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
+            "landingPage": "https://data.cdc.gov/d/rnah-xd9n",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pubmed.ncbi.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "bioethics",
-                "biomedical research",
-                "books",
-                "clinical medicine",
-                "community health",
-                "dataset",
-                "dentistry",
-                "ethics medical",
-                "literature",
-                "medicine",
-                "nursing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vc2v-qdpk",
             "description": "PubMed comprises more than 26 million citations for biomedical literature from MEDLINE, life science journals, and online books. Citations may include links to full-text content from PubMed Central and publisher web sites.",
-            "title": "PubMed",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.ncbi.nlm.nih.gov/books/NBK25497/",
-                    "description": "The Entrez Programming Utilities (E-utilities) are a set of nine server-side programs that provide a stable interface into the Entrez query and database system at the National Center for Biotechnology Information (NCBI).",
                     "@type": "dcat:Distribution",
+                    "description": "The Entrez Programming Utilities (E-utilities) are a set of nine server-side programs that provide a stable interface into the Entrez query and database system at the National Center for Biotechnology Information (NCBI).",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/books/NBK25497/",
+                    "mediaType": "text/html",
                     "title": "E-utilities API"
                 },
                 {
@@ -75460,75 +75433,79 @@
                     "title": "Search PubMed - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubmed.ncbi.nlm.nih.gov/clinical/",
-                    "description": "This tool uses predefined filters to help you quickly refine PubMed searches on clinical or disease-specific topics. To use this tool, enter your search terms in the search bar and select filters before searching.  The tool include a COVID-19-specific filter.",
                     "@type": "dcat:Distribution",
+                    "description": "This tool uses predefined filters to help you quickly refine PubMed searches on clinical or disease-specific topics. To use this tool, enter your search terms in the search bar and select filters before searching.  The tool include a COVID-19-specific filter.",
+                    "downloadURL": "https://pubmed.ncbi.nlm.nih.gov/clinical/",
+                    "mediaType": "text/html",
                     "title": "PubMed Clinical Queries"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nlm.nih.gov/psd/special_queries.html",
-                    "description": "Clinical Queries (Clinical Study Categories and COVID-19), Healthy People 2020, and Health Services Research (HSR) Queries, as well as other topics.",
                     "@type": "dcat:Distribution",
+                    "description": "Clinical Queries (Clinical Study Categories and COVID-19), Healthy People 2020, and Health Services Research (HSR) Queries, as well as other topics.",
+                    "downloadURL": "https://www.nlm.nih.gov/psd/special_queries.html",
+                    "mediaType": "text/html",
                     "title": "Topic-Specific PubMed Queries"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://learn.nlm.nih.gov/documentation/training-packets/T0042010P/",
-                    "description": "Quick tours, tutorials, class recordings, handouts, and API instructions",
                     "@type": "dcat:Distribution",
+                    "description": "Quick tours, tutorials, class recordings, handouts, and API instructions",
+                    "downloadURL": "https://learn.nlm.nih.gov/documentation/training-packets/T0042010P/",
+                    "mediaType": "text/html",
                     "title": "PubMed Online Training"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vc2v-qdpk",
+            "issued": "2012-05-30",
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
+            "landingPage": "https://pubmed.ncbi.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Literature"
-            ]
+            ],
+            "title": "PubMed"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/innovation-center-model-summary-information",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2025-01-01/2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "references": [
-                "https://data.cms.gov/resources/model-summary-information-methodology"
-            ],
-            "keyword": [
-                "children's health insurance program",
-                "medicare",
-                "medicare advantage",
-                "medicare prescription drug",
-                "original medicare",
-                "payment models",
-                "value-based care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Innovation Center - CMMI",
                 "hasEmail": "mailto:cmmi-dataset-support@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/model-summary-information-data-dictionary",
             "description": "The Innovation Center Model Summary Information dataset contains various data points related to CMS Innovation Center models, demonstrations, programs, and initiatives. This can includes name, start and end date, statutory or regulatory authority, keywords, stage of implementation, participants, beneficiaries and physicians impacted, and categories related to health care quality, cost, payment, and delivery.\u00a0",
-            "title": "Innovation Center Model Summary Information",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data",
+                    "mediaType": "text/html",
                     "title": "Innovation Center Model Summary Information : 2025-01-17"
                 },
                 {
@@ -75544,58 +75521,53 @@
                     "title": "Innovation Center Model Summary Information : 2025-01-17"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/model-summary-information-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/0d753f51-c3de-43cd-95d2-550a23b8606a/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "children's health insurance program",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/innovation-center-model-summary-information",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/model-summary-information-methodology"
+            ],
+            "temporal": "2025-01-01/2025-01-31",
             "theme": [
                 "Medicare",
                 "Children's Health Insurance Program"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Innovation Center Model Summary Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "brfss",
-                "city",
-                "health",
-                "outcomes",
-                "place",
-                "places",
-                "prevalence",
-                "prevention",
-                "risk",
-                "status"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/epbn-9bv3",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
             "description": "This dataset contains model-based place (incorporated and census-designated places) level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at   www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Place Data 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75618,41 +75590,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "identifier": "https://data.cdc.gov/api/views/epbn-9bv3",
+            "issued": "2023-06-15",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: Local Data for Better Health, Place Data 2022 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "temporal": "2004-01-01/2012-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2004-01-01",
-            "keyword": [
-                "adverse event",
-                "human drugs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FDA Enterprise Data Inventory",
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "b454bed2-730a-4e06-becb-0f599f2ad62a",
             "description": "The Adverse Event Reporting System (AERS) is a computerized information database designed to support the FDA's post-marketing safety surveillance program for all approved drug and therapeutic biologic products. The FDA uses AERS to monitor for new adverse events and medication errors that might occur with these marketed products. Reporting of adverse events from the point of care is voluntary in the United States. FDA receives some adverse event and medication error reports directly from health care professionals (such as physicians, pharmacists, nurses and others) and consumers (such as patients, family members, lawyers and others). Healthcare professionals and consumers may also report these events to the products' manufacturers. If a manufacturer receives an adverse event report, it is required to send the report to FDA as specified by regulations.  The files listed on this page contain raw data extracted from the AERS database for the indicated time ranges and are not cumulative. Users of these files need to be familiar with creation of relational databases using applications such as ORACLE, Microsoft Office Access, MySQL and IBM DB2 or the use of ASCII files with SAS analytic tools. A simple search of AERS data cannot be performed with these files by persons who are not familiar with creation of relational databases.",
-            "title": "Adverse Event Reporting System (AERS)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75660,38 +75642,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "b454bed2-730a-4e06-becb-0f599f2ad62a",
+            "issued": "2021-02-25",
+            "keyword": [
+                "adverse event",
+                "human drugs"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2004-01-01",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "temporal": "2004-01-01/2012-12-31",
+            "title": "Adverse Event Reporting System (AERS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/h62y-qtec",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "py2025",
-                "rate"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "672d5f6a-b8a7-4ebe-87f6-67db641e192d",
             "description": "The Rate PUF (Rate-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Rate-PUF contains plan-level data on rates based on an eligible subscriber\u2019s age, tobacco use, and geographic location; and family-tier rates.",
-            "title": "Rate PUF \u2013 PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75699,17 +75681,48 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "672d5f6a-b8a7-4ebe-87f6-67db641e192d",
+            "issued": "2024-12-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2025",
+                "rate"
+            ],
+            "landingPage": "https://healthdata.gov/d/h62y-qtec",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Rate PUF \u2013 PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1996",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1996) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -75722,55 +75735,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1996",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1996)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1996) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1996-nid13551"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1996)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2kh7-g39q",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch (PERB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2kh7-g39q",
             "description": "Three-dimensional (3D) printing is increasingly being used in manufacturing settings, homes and schools.  Fused deposition modeling (FDM) 3D printers are the most widely used systems with standard thermoplastics such as acrylonitrile butadiene styrene (ABS), polylactic acid and polycarbonate (PC) commonly used in the manufacturing processes.  Heating of the thermoplastic generates and releases particulates and fumes.  Emission constituents frequently measured include aldehydes, benzene, toluene, ethylbenzene, and xylenes.  Inhalation of the emitted particulates and/or the fumes, that contain bisphenol A (BPA)  may pose health problems to users of these systems as well as bystanders.\n\nThe goal of the current study was to examine the effects of inhalation of PC-emissions generated during 3D-printing.  PC-emissions can include bisphenol A (BPA). Bisphenols are known endocrine and metabolic disruptors (i.e., they interfere with actions of steroid and thyroid hormones) and have been shown to have significant effects on a number of physiological systems including the endocrine and cardiovascular systems.  Because steroid hormones have major effects on cardiovascular function, it is possible that inhalation of PC particulate and/or BPA impact cardiovascular function.\n\nTo begin to understand how inhalation of PC-emissions generated during 3D printing might affect the cardiovascular system, the current study examined the effects of inhaling PC-emissions after 1, 4, 8, 15 and 30d of exposure, on peripheral vascular responses to vaso-modulating agents, on cardiac morphology and on the expression of proteins and transcripts that are markers of inflammation, oxidative stress and cardiovascular dysfunction.",
-            "title": "Exposure to emissions generated by 3-dimensional printing with polycarbonate affects vascular morphology and expression of markers of oxidative stress and vascular dysfunction in cardiac tissue",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75778,47 +75765,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2kh7-g39q",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/2kh7-g39q",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Exposure to emissions generated by 3-dimensional printing with polycarbonate affects vascular morphology and expression of markers of oxidative stress and vascular dysfunction in cardiac tissue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/cov19_landing_2024.htm",
+            "accrualPeriodicity": "R/P4Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-04/2020-01-03",
-            "modified": "2024-09-24",
-            "keyword": [
-                "all causes",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "puerto rico",
-                "state",
-                "united states",
-                "weekly"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9cpv-whbv",
             "description": "This dataset includes the number of deaths from all causes by week in which the death occurred and by jurisdiction, from 2015 to 2019, United States and Puerto Rico.",
-            "title": "Weekly counts of deaths from all causes by jurisdiction,  2015-2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75841,96 +75817,96 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/9cpv-whbv",
+            "issued": "2024-09-20",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/cov19_landing_2024.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P4Y",
+            "modified": "2024-09-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2015-01-04/2020-01-03",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Weekly counts of deaths from all causes by jurisdiction,  2015-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/h6e5-7hzs",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_prodauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "0a339472-900f-526b-b339-f5d7d407a906",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measure_allStates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates.csv",
-                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates csv file"
                 }
             ],
+            "identifier": "0a339472-900f-526b-b339-f5d7d407a906",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/h6e5-7hzs",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "prodAuto_measure_allStates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/chmz-4uae",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "hansen's disease",
-                "hantavirus infection",
-                "hantavirus pulmonary syndrome",
-                "nedss",
-                "netss",
-                "nndss",
-                "non-hantavirus pulmonary syndrome",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/chmz-4uae",
             "description": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes data for old world hantavirus infections, such as Seoul virus infections. Prior to 2015, this condition was not nationally notifiable and data for this condition was not submitted to CDC's National Notifiable Diseases Surveillance System (NNDSS).\n\u00b6 Includes data for Andes virus infections.",
-            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75953,42 +75929,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/chmz-4uae",
+            "issued": "2021-01-21",
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
+            "landingPage": "https://data.cdc.gov/d/chmz-4uae",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/h8pb-fabb",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "individual",
-                "individual market medical",
-                "py2024",
-                "qhp",
-                "qhp landscape"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "2cfb30f4-7c65-42bd-bc4c-a3fbcf1cb2cd",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2024 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75996,37 +75977,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "2cfb30f4-7c65-42bd-bc4c-a3fbcf1cb2cd",
+            "issued": "2024-08-06",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2024",
+                "qhp",
+                "qhp landscape"
+            ],
+            "landingPage": "https://healthdata.gov/d/h8pb-fabb",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2024 Individual Medical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/gap/phegeni",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-30",
-            "keyword": [
-                "genetics",
-                "genomics",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/53jk-taha",
             "description": "Supports finding human phenotype/genotype relationships with queries by phenotype, chromosome location, gene, and SNP identifiers. Currently includes information from dbGaP, the National Human Genome Research Institute (NHGRI) genome-wide association study (GWAS) Catalog, and Genotype - Tissue Expression (GTeX).",
-            "title": "Phenotype-Genotype Integrator (PheGenI)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76035,39 +76017,40 @@
                     "title": "Phenotype-Genotype Integrator (PheGenI) - Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/53jk-taha",
+            "issued": "2021-07-01",
+            "keyword": [
+                "genetics",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/gap/phegeni",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-09-30",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "Phenotype-Genotype Integrator (PheGenI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rqg5-mkef",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-13",
-            "keyword": [
-                "death rate",
-                "motor vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rqg5-mkef",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, All States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76090,45 +76073,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rqg5-mkef",
+            "issued": "2016-10-17",
+            "keyword": [
+                "death rate",
+                "motor vehicle"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rqg5-mkef",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-09-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, All States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jz7r-jrma",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "tetanus",
-                "varicella",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jz7r-jrma",
             "description": "NNDSS - Table II. Tetanus to Varicella - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Tetanus to Varicella",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76151,38 +76128,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jz7r-jrma",
+            "issued": "2018-01-04",
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
+            "landingPage": "https://data.cdc.gov/d/jz7r-jrma",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Tetanus to Varicella"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/harf-86yj",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-01-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-11",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "e02d3bb0-600d-5451-945f-978a8a511770",
             "description": "During a public health emergency in the Families First Coronavirus Response Act (FFCRA), a new optional Medicaid eligibility group was added called COVID-19 testing eligibility group. States reported these expenditures under sections 6004 and 6008 through the Medicaid Budget and Expenditure System (MBES) on the Form CMS-64. The data in these reports constitute summary level preliminary expenditure information related to these FFCRA provisions for each state\r\n\r\nNotes:\r\n1. The Families First Coronavirus Response Act (FFCRA), enacted on March 18, 2020, provided a temporary FMAP increase to states and territories meeting certain qualifications and added a new optional \t\t\t\t\t\r\n    Medicaid eligibility group for uninsured individuals during a public health emergency in section 1902(a)(10)(A)(ii)(XXIII) of the Act, referred to as the \u201cCOVID - 19 Testing Group.\u201d\t\t\t\t\t\r\n2. FFCRA Section 6008 provides a temporary 6.2 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning January 1, 2020 and lasting through \t\t\t\t\t\r\n    the end of the quarter in which the public health emergency (PHE) declared by the Secretary for COVID-19 ends, including any extensions.\t\t\t\t\t\r\n3. FFCRA Section 6004 provides a 100 percent match rate for individuals eligible under the new optional Medicaid eligibility group in section 1902(a)(10)(A)(ii)(XXIII) of the Act, beginning no earlier than \t\t\t\t\t\r\n    March 18, 2020 and lasting through the end of the PHE for COVID-19.\t\t\t\t\t\r\n4. States that have reported \u201c0\u201d either have no expenditures for that reporting category or have not yet reported expenditures for that category.\t\t\t\t\t\r\n5. This report is a cumulative summary report that includes current and prior period adjustment expenditures that apply to this quarter\t\r\n6. For the Quarter ending 03/31/2020: Delaware has Negative Total Computable Expenditures and Total Federal Share Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\r\n7. For the Quarter ending 09/30/2020: Colorado has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\t\t\r\n8. For the Quarter ending 03/31/2021: California has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period. This corrected FY 2020 Q4 expenditures for Treatment services that are not allowed for Section 6004 100% FMAP match.\r\n9. For the Quarter ending 03/31/2021: Utah has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\r\n10. For the Quarter ending 12/31/2022: California has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\r\n11. For the Quarter ending 12/31/2022: Connecticut has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\r\n12. For the Quarter ending 09/30/2023: Connecticut has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\t\t\r\n13. For the Quarter ending 09/30/2023: Illinois has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid 19 Expenditures due to the reporting of prior period adjustments during this period.\t\t\t\t\t\t\r\n14. For the Quarter ending 09/30/2023: Minnesota has Negative Total Computable Section 6004 Covid 19 Expenditures and Total Federal Share Section 6004 Covid",
-            "title": "Medicaid CMS-64 FFCRA Increased FMAP Expenditure",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76190,81 +76175,77 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "e02d3bb0-600d-5451-945f-978a8a511770",
+            "issued": "2021-01-15",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/harf-86yj",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-12-11",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Medicaid CMS-64 FFCRA Increased FMAP Expenditure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/research/coronavirus/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "literature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/8nrp-jhfw",
             "description": "LitCovid is a curated literature hub for tracking up-to-date scientific information about the 2019 novel Coronavirus. The articles are updated daily and are further categorized by different research topics (e.g. Long Covid) and geographic locations for improved access.",
-            "title": "LitCovid",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pub/lu/LitCovid/",
-                    "description": "See README.txt for descriptions of datasets.  In addition to exports of LitCovid, datasets which are automatically annotated or contain articles are available.",
                     "@type": "dcat:Distribution",
+                    "description": "See README.txt for descriptions of datasets.  In addition to exports of LitCovid, datasets which are automatically annotated or contain articles are available.",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pub/lu/LitCovid/",
+                    "mediaType": "text/html",
                     "title": "Download LitCovid Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/8nrp-jhfw",
+            "issued": "2021-08-27",
+            "keyword": [
+                "dataset",
+                "literature"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/research/coronavirus/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Literature"
-            ]
+            ],
+            "title": "LitCovid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wgvr-7mvz",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "community mitigation",
-                "coronavirus",
-                "covid-19",
-                "school closure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nicole Zviedrite",
                 "hasEmail": "mailto:jmu6@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wgvr-7mvz",
             "description": "Unplanned public K-12 school district and individual school closures due to COVID-19 in the United States from February 18\u2013June 30, 2020.",
-            "title": "COVID-19-associated school closures, United States, February 18\u2013June 30, 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76287,38 +76268,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wgvr-7mvz",
+            "issued": "2022-01-12",
+            "keyword": [
+                "community mitigation",
+                "coronavirus",
+                "covid-19",
+                "school closure"
+            ],
+            "landingPage": "https://data.cdc.gov/d/wgvr-7mvz",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "COVID-19-associated school closures, United States, February 18\u2013June 30, 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hbyh-kqh6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-02-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-07",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "2f2451fb-e5fe-4235-892b-755fe273903e",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-09-to-2023-01-15",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76327,43 +76312,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-09-to-2023-01-15"
                 }
             ],
+            "identifier": "2f2451fb-e5fe-4235-892b-755fe273903e",
+            "issued": "2023-02-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/hbyh-kqh6",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-02-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-09-to-2023-01-15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9x7v-wy9u",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "nedss",
-                "netss",
-                "nndss",
-                "tetanus",
-                "toxic shock syndrome (other than streptococcal)",
-                "trichinellosis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9x7v-wy9u",
             "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76386,51 +76363,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9x7v-wy9u",
+            "issued": "2021-01-21",
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
+            "landingPage": "https://data.cdc.gov/d/9x7v-wy9u",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-clinic-group-practice-reassignment",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "references": [
-                "https://data.cms.gov/resources/additional-information-on-revalidation"
-            ],
-            "keyword": [
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "provider enrollment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/e1f1fa9a-d6b4-417e-948a-c72dead8a41c/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/revalidation-clinic-group-practice-reassignment-data-dictionary",
             "description": "The Revalidation Clinic Group Practice Reassignment dataset provides information between the physician and the group practice they reassign their billing to. It also includes individual employer association counts and the revalidation dates for the individual physician as well as the clinic group practice.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Revalidation Clinic Group Practice Reassignment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e1f1fa9a-d6b4-417e-948a-c72dead8a41c/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e1f1fa9a-d6b4-417e-948a-c72dead8a41c/data",
+                    "mediaType": "text/html",
                     "title": "Revalidation Clinic Group Practice Reassignment : 2025-01-01"
                 },
                 {
@@ -76722,61 +76702,49 @@
                     "title": "Revalidation Clinic Group Practice Reassignment : 2022-01-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/revalidation-clinic-group-practice-reassignment-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e1f1fa9a-d6b4-417e-948a-c72dead8a41c/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-clinic-group-practice-reassignment",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-02",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/additional-information-on-revalidation"
+            ],
+            "temporal": "2022-01-01/2025-01-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Revalidation Clinic Group Practice Reassignment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2023-07-29",
-            "modified": "2023-09-27",
-            "keyword": [
-                "age",
-                "age group",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "influenza",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "pneumonia",
-                "provisional",
-                "puerto rico",
-                "sex",
-                "state",
-                "united states",
-                "yearly"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9bhg-hcku",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by sex, age group, and jurisdiction of occurrence.",
-            "title": "Provisional COVID-19 Deaths by Sex and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76799,40 +76767,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/9bhg-hcku",
+            "issued": "2020-05-01",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2020-01-01/2023-07-29",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Deaths by Sex and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hdhv-rcwe",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2019-04-18",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-03",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Vaughn",
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "8f39b637-9bb1-5894-9062-2c4f2ad70fba",
             "description": "Provides program names, program features, population enrolled, benefits covered, quality assurance and improvement, performance incentives, provider value-based purchasing, participating plans, regions served and program notes.",
-            "title": "2017 Managed Care Programs by State",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76841,49 +76826,39 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "8f39b637-9bb1-5894-9062-2c4f2ad70fba",
+            "issued": "2019-04-18",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/hdhv-rcwe",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2019-05-03",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Enrollment"
-            ]
+            ],
+            "title": "2017 Managed Care Programs by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "brfss",
-                "county",
-                "outcomes",
-                "places",
-                "prevalence",
-                "prevention",
-                "unhealthy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dv4u-3x3q",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
             "description": "This dataset contains model-based county-level estimates for the PLACES project 2020 release. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 27 measures: 5 chronic disease-related unhealthy behaviors, 13 health outcomes, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2018 or 2017 county population data, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, County Data 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76906,46 +76881,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "identifier": "https://data.cdc.gov/api/views/dv4u-3x3q",
+            "issued": "2021-09-29",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: Local Data for Better Health, County Data 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/sixg-saap",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "anaplasma phagocytophilum infection",
-                "ehrlichia chaffeensis infection",
-                "ehrlichiosis and anaplasmosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/sixg-saap",
             "description": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76968,44 +76945,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/sixg-saap",
+            "issued": "2022-01-14",
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
+            "landingPage": "https://data.cdc.gov/d/sixg-saap",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2019-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-20",
-            "keyword": [
-                "deaths",
-                "drug poisoning",
-                "mortality",
-                "national",
-                "nchs",
-                "state",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rpvx-m2md",
             "description": "This dataset describes drug poisoning deaths at the U.S. and state level by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning. \n\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\n\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\n\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Drug poisoning death rates may be underestimated in those instances.\n\nREFERENCES\n1. National Center for Health Statistics. National Vital Statistics System: Mortality data. Available from: http://www.cdc.gov/nchs/deaths.htm.\n\n2. CDC. CDC Wonder: Underlying cause of death 1999\u20132016. Available from: http://wonder.cdc.gov/wonder/help/ucd.html.",
-            "title": "NCHS - Drug Poisoning Mortality by County: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77028,21 +77006,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/rpvx-m2md",
+            "issued": "2019-04-29",
+            "keyword": [
+                "deaths",
+                "drug poisoning",
+                "mortality",
+                "national",
+                "nchs",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Drug Poisoning Mortality by County: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2015",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and<br />\n    correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual estimates. Information is provided on the use<br />\n    of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as<br />\n    lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco,<br />\n    and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment<br />\n    history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic<br />\n    criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were<br />\n    also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting<br />\n    from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2015 survey, including questions asked<br />\n    only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug<br />\n    use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes<br />\n    toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on<br />\n    mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking.<br />\n    Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to<br />\n    measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a<br />\n    split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems.<br />\n    Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race,<br />\n    age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2015) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -77083,96 +77096,66 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2015",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and<br />\n    correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual estimates. Information is provided on the use<br />\n    of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as<br />\n    lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco,<br />\n    and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment<br />\n    history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic<br />\n    criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were<br />\n    also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting<br />\n    from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2015 survey, including questions asked<br />\n    only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug<br />\n    use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes<br />\n    toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on<br />\n    mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking.<br />\n    Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to<br />\n    measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a<br />\n    split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems.<br />\n    Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race,<br />\n    age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2015)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2015) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2015-nid16893"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2015)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hhqs-3zft",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-31",
-            "keyword": [
-                "faers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FDA Enterprise Data Inventory",
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "901A022F-A9B2-4B0A-9A33-0F3D353DF3FD",
             "description": "Public access  allowing for public search of the FDA Adverse Events Database",
-            "title": "Public Search for Adverse Events (FOIA)",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Public access  allowing for public search of the FDA Adverse Events Database",
                     "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/ucm082193",
-                    "mediaType": "application/xml",
-                    "description": "Public access  allowing for public search of the FDA Adverse Events Database"
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "901A022F-A9B2-4B0A-9A33-0F3D353DF3FD",
+            "issued": "2021-02-25",
+            "keyword": [
+                "faers"
+            ],
+            "landingPage": "https://healthdata.gov/d/hhqs-3zft",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2014-12-31",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Public Search for Adverse Events (FOIA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/clinvar/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "dataset",
-                "genomics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4jy8-nv98",
             "description": "ClinVar aggregates information about genomic variation and its relationship to human health.",
-            "title": "ClinVar",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77187,42 +77170,39 @@
                     "title": "Download ClinVar Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4jy8-nv98",
+            "issued": "2016-08-08",
+            "keyword": [
+                "dataset",
+                "genomics"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/clinvar/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "ClinVar"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5iuf-feyd",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-04-21",
-            "@type": "dcat:Dataset",
-            "temporal": "August 1, 2011 to June 30, 2019",
-            "modified": "2022-04-21",
-            "keyword": [
-                "community mitigation",
-                "emergency preparedness",
-                "pandemic preparedness",
-                "school closure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nicole Zviedrite",
                 "hasEmail": "mailto:nzviedrite@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5iuf-feyd",
             "description": "Prolonged unplanned public K-12 school district and individual school closures in the United States from August 1, 2011 \u2013 June 30, 2019. Prolonged unplanned school closure is defined as a school closure lasting \u22655 school days, excluding any scheduled days off.",
-            "title": "Prolonged Unplanned School Closures: USA, 2011-2019",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77245,44 +77225,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, 50 States and D.C.",
+            "identifier": "https://data.cdc.gov/api/views/5iuf-feyd",
+            "issued": "2022-04-21",
+            "keyword": [
+                "community mitigation",
+                "emergency preparedness",
+                "pandemic preparedness",
+                "school closure"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5iuf-feyd",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-21",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, 50 States and D.C.",
+            "temporal": "August 1, 2011 to June 30, 2019",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Prolonged Unplanned School Closures: USA, 2011-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pwn4-m3yp",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-10-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-22/2023-05-10",
-            "modified": "2025-01-13",
-            "keyword": [
-                "aggregate",
-                "cases",
-                "coronavirus",
-                "covid-19",
-                "death"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pwn4-m3yp",
             "description": "Reporting of new Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. This dataset will receive a final update on June 1, 2023, to reconcile historical data through May 10, 2023, and will remain publicly available.\n\n<b>Aggregate Data Collection Process </b>\nSince the start of the COVID-19 pandemic, data have been gathered through a robust process with the following steps: \n<ul><li>A CDC data team reviews and validates the information obtained from jurisdictions\u2019 state and local websites via an overnight data review process.</li>\n<li>If more than one official county data source exists, CDC uses a comprehensive data selection process comparing each official county data source, and takes the highest case and death counts respectively, unless otherwise specified by the state. </li>\n<li>CDC compiles these data and posts the finalized information on COVID Data Tracker. </li>\n<li>County level data is aggregated to obtain state and territory specific totals.</li>\n</ul>This process is collaborative, with CDC and jurisdictions working together to ensure the accuracy of COVID-19 case and death numbers. County counts provide the most up-to-date numbers on cases and deaths by report date. CDC may retrospectively update counts to correct data quality issues. \n\n<b>Methodology Changes </b>\nSeveral differences exist between the current, weekly-updated dataset and the archived version: \n<ul><li><b>Source:</b>\u202fThe current Weekly-Updated Version is based on county-level aggregate count data, while the Archived Version is based on State-level aggregate count data. </li>\n<li><b>Confirmed/Probable Cases/Death breakdown:\u202f</b> While the probable cases and deaths are included in the total case and total death counts in both versions (if applicable), they were reported separately from the confirmed cases and deaths by jurisdiction in the Archived Version.\u202f In the current Weekly-Updated Version, the counts by jurisdiction are not reported by confirmed or probable status (See Confirmed and Probable Counts section for more detail).</li>\n<li><b>Time Series Frequency:</b> The current Weekly-Updated Version contains weekly time series data (i.e., one record per week per jurisdiction), while the Archived Version contains daily time series data (i.e., one record per day per jurisdiction). </li>\n<li><b>Update Frequency:</b>\u202fThe current Weekly-Updated Version is updated weekly, while the Archived Version was updated twice daily up to October 20, 2022. </li></ul>\n<b>Important note:</b> The counts reflected during a given time period in this dataset may not match the counts reflected for the same time period in the archived dataset noted above. Discrepancies may exist due to differences between county and state COVID-19 case surveillance and reconciliation efforts. \n\n<b>Confirmed and Probable Counts </b>\nIn this dataset, counts by jurisdiction are not displayed by confirmed or probable status. Instead, confirmed and probable cases and deaths are included in the Total Cases and Total Deaths columns, when available. Not all jurisdictions report probable cases and deaths to CDC.* Confirmed and probable case definition criteria are described here: \n\n<a href=\"https://cdn.ymaws.com/www.cste.org/resource/resmgr/ps/ps2022/22-ID-01_COVID19.pdf\">Council of State and Territorial Epidemiologists (ymaws.com).</a>\n\n<b>Deaths</b>\nCDC reports death data on other sections of the website: <a href=\"https://covid.cdc.gov/covid-data-tracker/#datatracker-home\"> CDC COVID Data Tracker: Home</a>, <a href=\"https://covid.cdc.gov/covid-data-tracker/?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fcases-updates%2Fcases-in-us.html#cases_casesper100klast7days\">CDC COVID Data Tracker: Cases, Deaths, and Testing</a>, and <a href=\"https://www.cdc.gov/nchs/nvss/covid-19.htm\">NCHS Provisional Death Counts</a>. Information presented on the COVID Data Tracker pages is based on the same source (to",
-            "title": "Weekly United States COVID-19 Cases and Deaths by State - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77305,49 +77285,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/pwn4-m3yp",
+            "issued": "2022-10-20",
+            "keyword": [
+                "aggregate",
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "death"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pwn4-m3yp",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2020-01-22/2023-05-10",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "Weekly United States COVID-19 Cases and Deaths by State - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mr4u-abm2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "age<5 years",
-                "confirmed",
-                "invasive pneumococcal disease",
-                "legionellosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mr4u-abm2",
             "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 years, Confirmed to Legionellosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77370,76 +77345,80 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mr4u-abm2",
+            "issued": "2022-01-14",
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
+            "landingPage": "https://data.cdc.gov/d/mr4u-abm2",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/medicaid-fraud-control-units-mfcu-annual-spending-and-performance-statistics",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-03-25",
-            "temporal": "2006-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "medicaid",
-                "office-of-inspector-general-department-of-health-human-services"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OIG public affairs",
                 "hasEmail": "mailto:public.affairs@oig.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Inspector General, Department of Health & Human Services"
-            },
-            "identifier": "e02ee78f-98b2-4a10-b057-07c73edb954c",
+            "dataQuality": true,
             "description": "<p>To inform HHS, States, Congress, and the public about the results and accomplishments of the State Medicaid Fraud Control Units.</p>",
-            "title": "Medicaid Fraud Control Units (MFCU) Annual Spending and Performance Statistics",
+            "identifier": "e02ee78f-98b2-4a10-b057-07c73edb954c",
+            "issued": "2013-03-25",
+            "keyword": [
+                "medicaid",
+                "office-of-inspector-general-department-of-health-human-services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/medicaid-fraud-control-units-mfcu-annual-spending-and-performance-statistics",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:076"
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Inspector General, Department of Health & Human Services"
+            },
+            "temporal": "2006-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
+            "title": "Medicaid Fraud Control Units (MFCU) Annual Spending and Performance Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ci7c-73kg",
+            "accrualPeriodicity": "Archive",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-26",
-            "keyword": [
-                "cases",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "ensemble",
-                "forecast",
-                "model"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Forecasting and Outbreak Analytics",
                 "hasEmail": "mailto:cfadata@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ci7c-73kg",
             "description": "This dataset contains forecasted weekly numbers of reported COVID-19 incident cases, incident deaths, and cumulative deaths in the United States, previously reported on COVID Data Tracker (https://covid.cdc.gov/covid-data-tracker/#datatracker-home). These forecasts were generated using mathematical models by CDC partners in the COVID-19 Forecast Hub (https://covid19forecasthub.org/doc/ensemble/). A CDC ensemble model was produced every week using the submitted models from that week at the national, and state/territory level. \n\n\nThis dataset is intended to mirror the observed and forecasted data, previously available for download on the CDC\u2019s COVID Data Tracker.  Mortality forecasts for both new and cumulative reported COVID-19 deaths were produced at the state and territory level and national level. Forecasts of new reported COVID-19 cases were produced at the county, state/territory, and national level. Please note that this dataset is not complete for every model, date, location or combination thereof. Specifically, county level submissions for COVID-19 incident cases were accepted, but not required, and are missing or incomplete for many models and dates.  State and territory-level forecasts are more complete, but not all models submitted forecasts for all locations, dates, and targets (new reported deaths, new reported cases, and cumulative reported deaths).  Forecasts for COVID-19 incident cases were discontinued in February 2022. Forecasts for COVID-19 cumulative and incident deaths were discontinued in March 2023.",
-            "title": "CDC COVID-19 Cases and Deaths Ensemble Forecast Archive",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77462,27 +77441,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "National",
+            "identifier": "https://data.cdc.gov/api/views/ci7c-73kg",
+            "issued": "2023-04-26",
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "ensemble",
+                "forecast",
+                "model"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ci7c-73kg",
             "license": "http://creativecommons.org/licenses/by/4.0/legalcode",
-            "accrualPeriodicity": "Archive",
+            "modified": "2023-04-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "National",
             "theme": [
                 "Models"
-            ]
+            ],
+            "title": "CDC COVID-19 Cases and Deaths Ensemble Forecast Archive"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qcw5-4m9q",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "See data use agreement for additional information.",
-            "issued": "2021-05-24",
-            "@type": "dcat:Dataset",
-            "temporal": "2013/2017",
-            "modified": "2025-01-29",
-            "references": [
-                "https://clinicaltrials.gov/ct2/show/NCT01965470?cond=HIV&cntry=BW&draw=2&rank=14"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Gene Ussery",
+                "hasEmail": "mailto:gua1@cdc.gov"
+            },
+            "description": "The Botswana Combination Prevention Project (BCPP) was a research project conducted by the Botswana Ministry of Health (MOH), Harvard School of Public Health/Botswana Harvard AIDS Institute Partnership (BHP), and the U.S. Centers for Disease Control and Prevention (CDC). BCPP was a community randomized trial that examined the impact of prevention interventions on HIV incidence in 15 intervention and 15 control communities. The interventions included extensive HIV testing, linkage to care, and universal treatment services. To reduce HIV incidence in the intervention communities, the UNAIDS 90-90-90 goals were used: 90% of HIV-positive persons know their status; 90% of persons who know status are to be on ART; 90% of persons on ART are to be virally suppressed. The BCPP study is composed of 2 interlocking protocols: Evaluation Protocol and Intervention Protocol. The Evaluation Protocol of the BCPP evaluated the primary endpoint (HIV incidence), as well as some key related secondary endpoints. This protocol focused on the Baseline Household Survey; the HIV Incidence Cohort; and an End of Study Survey. The Intervention Protocol of the BCPP implemented the combination prevention (CP) intervention package in CPCs and measures the uptake of these interventions (expanded HIV testing and counselling, strengthened male circumcision, and expanded HIV Care and Treatment).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/qcw5-4m9q/application/zip",
+                    "mediaType": "application/zip"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qcw5-4m9q",
+            "issued": "2021-05-24",
             "keyword": [
                 "bcpp",
                 "botswana",
@@ -77493,47 +77499,51 @@
                 "pepfar",
                 "randomized control trial"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Gene Ussery",
-                "hasEmail": "mailto:gua1@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/qcw5-4m9q",
+            "language": [
+                "English"
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/qcw5-4m9q",
-            "description": "The Botswana Combination Prevention Project (BCPP) was a research project conducted by the Botswana Ministry of Health (MOH), Harvard School of Public Health/Botswana Harvard AIDS Institute Partnership (BHP), and the U.S. Centers for Disease Control and Prevention (CDC). BCPP was a community randomized trial that examined the impact of prevention interventions on HIV incidence in 15 intervention and 15 control communities. The interventions included extensive HIV testing, linkage to care, and universal treatment services. To reduce HIV incidence in the intervention communities, the UNAIDS 90-90-90 goals were used: 90% of HIV-positive persons know their status; 90% of persons who know status are to be on ART; 90% of persons on ART are to be virally suppressed. The BCPP study is composed of 2 interlocking protocols: Evaluation Protocol and Intervention Protocol. The Evaluation Protocol of the BCPP evaluated the primary endpoint (HIV incidence), as well as some key related secondary endpoints. This protocol focused on the Baseline Household Survey; the HIV Incidence Cohort; and an End of Study Survey. The Intervention Protocol of the BCPP implemented the combination prevention (CP) intervention package in CPCs and measures the uptake of these interventions (expanded HIV testing and counselling, strengthened male circumcision, and expanded HIV Care and Treatment).",
-            "title": "Botswana Combination Prevention Project (BCPP) - Public Release Data",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/qcw5-4m9q/application/zip",
-                    "mediaType": "application/zip"
-                }
+            "references": [
+                "https://clinicaltrials.gov/ct2/show/NCT01965470?cond=HIV&cntry=BW&draw=2&rank=14"
             ],
+            "rights": "See data use agreement for additional information.",
             "spatial": "Botswana",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2013/2017",
             "theme": [
                 "Global Health"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Botswana Combination Prevention Project (BCPP) - Public Release Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "9cc0d11d-dbcd-41a7-8947-02774d10ce2e",
             "issued": "2021-02-25",
-            "temporal": "2009-01-01/2009-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "h1n1",
                 "health",
@@ -77543,63 +77553,32 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "9cc0d11d-dbcd-41a7-8947-02774d10ce2e",
-            "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
-            "title": "Fraudulent 2009 H1N1 Influenza Products Widget",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "temporal": "2009-01-01/2009-12-31",
+            "title": "Fraudulent 2009 H1N1 Influenza Products Widget"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hk4x-6nkd",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-11-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-28",
-            "keyword": [
-                "cms-64",
-                "expansion population",
-                "expenditures",
-                "mbes",
-                "medicaid",
-                "new adult group",
-                "viii group"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "00505e90-f8ac-5921-b12f-5e23ba7ffcf3",
             "description": "This dataset reports summary level expenditure data associated with the new adult group established under the Affordable Care Act. These state expenditures are reported through the federal Medicaid Budget and Expenditure System (MBES).\r\n\r\nNotes:\r\n1. \u201cVIII GROUP\u201d is also known as the \u201cNew Adult Group.\u201d\r\n2. The VIII Group is only applicable for states that have expanded their Medicaid programs by adopting the VIII Group. VIII Group expenditure information\r\nfor the states that have not expanded their Medicaid program is noted as \u201cN/A.\u201d\r\n3. States that have reported \u201c0\u201d either have no expenditures for that reporting category or have not yet reported expenditures for that category.\r\n4. MCHIP expenditures are not included in the All Medical Assistance Expenditures.",
-            "title": "Medicaid CMS-64 New Adult Group Expenditures",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77608,41 +77587,45 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "00505e90-f8ac-5921-b12f-5e23ba7ffcf3",
+            "issued": "2017-11-03",
+            "keyword": [
+                "cms-64",
+                "expansion population",
+                "expenditures",
+                "mbes",
+                "medicaid",
+                "new adult group",
+                "viii group"
+            ],
+            "landingPage": "https://healthdata.gov/d/hk4x-6nkd",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-10-28",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Medicaid CMS-64 New Adult Group Expenditures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kh8y-3es6",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2020-05-06",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "cares act",
-                "health system",
-                "provider relief fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HRSA Chief Data Officer",
                 "hasEmail": "mailto:PRFdata@hrsa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kh8y-3es6",
             "description": "HHS is providing support to healthcare providers fighting the coronavirus disease 2019 (COVID-19) pandemic through the bipartisan Coronavirus Aid, Relief, & Economic Security (CARES) Act; the Paycheck Protection Program and Health Care Enhancement Act (PPPHCEA); and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act, which provide a total of $178 billion for relief funds to hospitals and other healthcare providers on the front lines of the COVID-19 response. This funding supports healthcare-related expenses or lost revenue attributable to COVID-19 and ensures uninsured Americans can get treatment for COVID-19. HHS is distributing this Provider Relief Fund (PRF) money and these payments do not need to be repaid.\n\nThe Department allocated $50 billion in PRF payments for general distribution to Medicare facilities and providers impacted by COVID-19, based on eligible providers' net reimbursement. HHS has made other PRF distributions to a wide array of health care providers and more information on those distributions can be found here: https://www.hhs.gov/coronavirus/cares-act-provider-relief-fund/data/index.html",
-            "title": "HHS Provider Relief Fund",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77665,49 +77648,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/kh8y-3es6",
+            "issued": "2020-05-06",
+            "keyword": [
+                "cares act",
+                "health system",
+                "provider relief fund"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kh8y-3es6",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "HHS Provider Relief Fund"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cz39-ahbn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "anthrax",
-                "arboviral diseases",
-                "chikungunya virus disease",
-                "eastern equine encephalitis virus disease",
-                "nedss",
-                "netss",
-                "neuroinvasive and non-neuroinvasive",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cz39-ahbn",
             "description": "NNDSS - Table 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1A.  Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77730,38 +77705,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cz39-ahbn",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/cz39-ahbn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1A.  Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hmsq-tdap",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-26",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "9ddd26da-ac32-47e9-88fd-3e4d4e747c90",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-18-2024-to-03-24-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77770,18 +77755,44 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-18-2024-to-03-24-2024"
                 }
             ],
+            "identifier": "9ddd26da-ac32-47e9-88fd-3e4d4e747c90",
+            "issued": "2024-03-27",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/hmsq-tdap",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-03-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-18-2024-to-03-24-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225440.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for the FDA Plainview Milk Cooperative Ingredient Recall since June 2009.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "5d970911-f35f-4514-9ddf-b20bc32790ff",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "community health",
                 "food",
@@ -77792,63 +77803,36 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225440.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "5d970911-f35f-4514-9ddf-b20bc32790ff",
-            "description": "Contains data for the FDA Plainview Milk Cooperative Ingredient Recall since June 2009.",
-            "title": "FDA Plainview Milk Cooperative Ingredient Recall",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xls",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Plainview Milk Cooperative Ingredient Recall"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/uvv3-fqwr",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "data distribution"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/uvv3-fqwr",
             "description": "The Chemical Carcinogenesis Research Information System (CCRIS) database contains chemical records with carcinogenicity, mutagenicity, tumor promotion, and tumor inhibition test results. It was developed by the National Cancer Institute (NCI). Data are derived from studies cited in primary journals, current awareness tools, NCI reports, and other sources. Test results have been reviewed by experts in carcinogenesis and mutagenesis. CCRIS provides historical information from the years 1985 - 2011. It is no longer updated.",
-            "title": "Chemical Carcinogenesis Research Information System (CCRIS)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/ccrislease/",
-                    "description": "Download over 9,000 chemical records.",
                     "@type": "dcat:Distribution",
+                    "description": "Download over 9,000 chemical records.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/ccrislease/",
+                    "mediaType": "text/html",
                     "title": "Download CCRIS Data"
                 },
                 {
@@ -77864,53 +77848,39 @@
                     "title": "CCRIS Documentation"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/uvv3-fqwr",
+            "issued": "2020-09-22",
+            "keyword": [
+                "data distribution"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/uvv3-fqwr",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Drugs and Chemicals"
-            ]
+            ],
+            "title": "Chemical Carcinogenesis Research Information System (CCRIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://academic.oup.com/aje/article/179/8/1025/109078",
-                "https://academic.oup.com/aje/article/182/2/127/93984",
-                "https://www.cdc.gov/pcd/issues/2017/17_0281.htm",
-                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
-            ],
-            "keyword": [
-                "500cities",
-                "behaviors",
-                "brfss",
-                "census",
-                "cities",
-                "outcomes",
-                "prevalence",
-                "prevention",
-                "tracts",
-                "unhealthy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "500 Cities Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6vp6-wxuq",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2017-relea/6vp6-wxuq",
             "description": "This is the complete dataset for the 500 Cities project 2019 release. This dataset includes 2017, 2016 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2017, 2016), Census Bureau 2010 census population data, and American Community Survey (ACS) 2013-2017, 2012-2016 estimates. Because some questions are only asked every other year in the BRFSS, there are 7 measures (all teeth lost, dental visits, mammograms, pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) from the 2016 BRFSS that are the same in the 2019 release as the previous 2018 release. More information about the methodology can be found at www.cdc.gov/500cities.",
-            "title": "500 Cities: Local Data for Better Health, 2019 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77933,21 +77903,64 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2017-relea/6vp6-wxuq",
+            "identifier": "https://data.cdc.gov/api/views/6vp6-wxuq",
+            "issued": "2023-07-18",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://academic.oup.com/aje/article/179/8/1025/109078",
+                "https://academic.oup.com/aje/article/182/2/127/93984",
+                "https://www.cdc.gov/pcd/issues/2017/17_0281.htm",
+                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "500 Cities: Local Data for Better Health, 2019 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The DC Metropolitan Area Drug Study (DC<em>MADS) was<br />\nconducted in 1991, and included special analyses of homeless and<br />\ntransient populations and of women delivering live births in the DC<br />\nhospitals. DC</em>MADS was undertaken to assess the full extent of the<br />\ndrug problem in one metropolitan area. The study was comprised of 16<br />\nseparate studies that focused on different sub-groups, many of which<br />\nare typically not included or are under-represented in household<br />\nsurveys.The DC<em>MADS: Household and Non-household Populations<br />\nexamines the prevalence of tobacco, alcohol, and drug use among<br />\nmembers of household and non-household populations aged 12 and older<br />\nin the District of Columbia Metropolitan Statistical Area (DC<br />\nMSA). The study also examines the characteristics of three<br />\ndrug-abusing sub-groups: crack-cocaine, heroin, and needle users. The<br />\nhousehold sample was drawn from the 1991 National Household Survey on<br />\nDrug Abuse (NHSDA). The non-household sample was drawn from the<br />\nDC</em>MADS Institutionalized and Homeless and Transient Population<br />\nStudies. Data include demographics, needle use, needle-sharing, and<br />\nuse of tobacco, alcohol, cocaine, crack, inhalants, marijuana, hallucinogens, heroin, sedatives, stimulants, psychotherapeutics (non-medical use), tranquilizers, and analgesics.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Washington  DC  Metropolitan Area Drug Study Household and Non-Household Populations (DC-MADSH-1991) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol",
                 "cocaine",
@@ -77965,55 +77978,29 @@
                 "stimulants",
                 "tranquilizers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
-            "description": "<p>The DC Metropolitan Area Drug Study (DC<em>MADS) was<br />\nconducted in 1991, and included special analyses of homeless and<br />\ntransient populations and of women delivering live births in the DC<br />\nhospitals. DC</em>MADS was undertaken to assess the full extent of the<br />\ndrug problem in one metropolitan area. The study was comprised of 16<br />\nseparate studies that focused on different sub-groups, many of which<br />\nare typically not included or are under-represented in household<br />\nsurveys.The DC<em>MADS: Household and Non-household Populations<br />\nexamines the prevalence of tobacco, alcohol, and drug use among<br />\nmembers of household and non-household populations aged 12 and older<br />\nin the District of Columbia Metropolitan Statistical Area (DC<br />\nMSA). The study also examines the characteristics of three<br />\ndrug-abusing sub-groups: crack-cocaine, heroin, and needle users. The<br />\nhousehold sample was drawn from the 1991 National Household Survey on<br />\nDrug Abuse (NHSDA). The non-household sample was drawn from the<br />\nDC</em>MADS Institutionalized and Homeless and Transient Population<br />\nStudies. Data include demographics, needle use, needle-sharing, and<br />\nuse of tobacco, alcohol, cocaine, crack, inhalants, marijuana, hallucinogens, heroin, sedatives, stimulants, psychotherapeutics (non-medical use), tranquilizers, and analgesics.This study has 1 Data Set.</p>",
-            "title": "Washington  DC  Metropolitan Area Drug Study Household and Non-Household Populations (DC-MADSH-1991)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh",
-                    "description": "Washington  DC  Metropolitan Area Drug Study Household and Non-Household Populations (DC-MADSH-1991) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-household-and-non-household-populations-dc-madsh"
-                }
-            ]
+            "title": "Washington  DC  Metropolitan Area Drug Study Household and Non-Household Populations (DC-MADSH-1991)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ur6f-kidn",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Pathology and Physiology Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ur6f-kidn",
             "description": "Thermal spray coating involves spraying a product that is melted by extremely high temperatures and then applied under pressure under pressure onto a surface. Large amounts of a complex metal aerosol (e.g., Fe, Cr, Ni, Zn) are formed during the process, presenting a potentially serious risk to the operator. Information about the health effects associated with exposure to these aerosols is lacking. Even less is known about the chemical and physical properties of these aerosols. The goal was to develop and test an automated thermal spray coating aerosol generator and inhalation exposure system that would simulate workplace exposures. An electric arc wire- thermal spray coating aerosol generator and exposure system was designed and separated into two areas: (A) an enclosed room where the spray coating occurs; (B) an exposure chamber with different measurement devices and controllers. The physicochemical properties of aerosols generated during electric arc wire- thermal spray coating using five different consumable wires were examined. The generated particles regardless of composition were poorly soluble, complex metal oxides and mostly arranged as chain-like agglomerates and similar in size distribution as determined by MOUDI and ELPI. To allow for continuous, sequential spray coating during a 4-hr exposure period, a motor rotated the metal pipe to be coated in a circular and up-and-down direction. In a pilot animal study, male Sprague-Dawley rats were exposed to aerosols (25 mg/m3 x 4 hr/d x 9 d) generated from electric arc wire- thermal spray coating using a stainless-steel PMET720 consumable wire. The targeted exposure chamber concentration was achieved and maintained during a 4-hr period. At 1 d after exposure, lung injury and inflammation were significantly elevated in the group exposed to the thermal spray coating aerosol compared to the air control group. A thermal spray coating inhalation system was designed and constructed that will generate continuous metal spray coating aerosols at a targeted concentration for extended periods of time without interruption for future animal exposure studies.",
-            "title": "Development of a thermal spray coating aerosol generator and inhalation exposure system",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78021,144 +78008,128 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ur6f-kidn",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/ur6f-kidn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Development of a thermal spray coating aerosol generator and inhalation exposure system"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hq8u-zp5z",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-30",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "13793c80-067b-5cf9-a0aa-751c387a10d4",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure v2.12.1-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/measure.csv",
-                    "description": "Scorecard measure v2.12.1-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure v2.12.1-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure v2.12.1-test (local)"
                 }
             ],
+            "identifier": "13793c80-067b-5cf9-a0aa-751c387a10d4",
+            "issued": "2023-08-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/hq8u-zp5z",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-30",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard measure v2.12.1-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hqzz-856g",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-06",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "d12a6469-b3df-5b52-a980-f7613823e8a3",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure_value v2.10.64 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
-                    "description": "CoreSet measure_value v2.10.64 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure_value v2.10.64 (coreset-dev)"
                 }
             ],
+            "identifier": "d12a6469-b3df-5b52-a980-f7613823e8a3",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/hqzz-856g",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSet measure_value v2.10.64 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rdmq-nq56",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-10-01/2023-01-27",
-            "modified": "2025-01-24",
-            "keyword": [
-                "coronavirus",
-                "covid19",
-                "ed",
-                "emergency department",
-                "flu",
-                "influenza",
-                "national syndromic surveillance program",
-                "ncird",
-                "nssp",
-                "ophdst",
-                "respiratory syncytial virus",
-                "respiratory-virus-response",
-                "rsv",
-                "rvr"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Syndromic Surveillance Program",
                 "hasEmail": "mailto:nssp@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rdmq-nq56",
             "description": "NSSP Emergency Department (ED) Visit Trajectories by State and Sub-State Regions- COVID-19, Flu, RSV, Combined. This dataset provides the percentage of emergency department patient visits for the specified pathogen of all ED patient visits for the specified geographic part of the country that were observed for the given week from data submitted to the National Syndromic Surveillance Program (NSSP). In addition, the trend over time is characterized as increasing, decreasing or no change, with exceptions for when there are no data available, the data are too sparse, or there are not enough data to compute a trend. These data are to provide awareness of how the weekly trend is changing for the given geographic region.\u202f \n\nNote that the reported sub-state trends are from Health Service Areas (HSA) and the data reported from the health care facilities located within the given HSA. Health Service Areas are regions of one or more counties that align to patterns of care seeking. The HSA level data are reported for each county in the HSA. \n\nMore information on HSAs is available <a href=\"https://seer.cancer.gov/seerstat/variables/countyattribs/hsa.html\"><b>here</b></a>.\n\nFor the emergency department time series, trajectory classifications reported on for sub-state (HSA) emergency department time series, trajectory classifications are based on approximations of the first derivative (slope) of trends that are smoothed using generalized additive models (GAMs). To determine time intervals in which the slope is sufficiently changing (i.e., rate of change distinguishable from 0), 95% confidence intervals for the slope approximations are calculated and assessed. Weeks with a 95% confidence interval not containing 0 are classified as increasing if the slope estimate is positive and decreasing if the slope estimate is negative. Weeks with a 95% confidence interval containing 0 are classified as stable. In the scenario that an HSA's time series is determined to be too sparse (i.e., many weeks with percentages of 0%), a model is not fit, and the HSA is classified as \u201csparse\u201d.  \n\nFor additional information, please see: <a href=\"https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide\"><b>Companion Guide: NSSP Emergency Department Data on Respiratory Illness</b></a>\n\nUpdated once per week on Fridays.\u202f",
-            "title": "NSSP Emergency Department Visit Trajectories by State and Sub State Regions- COVID-19, Flu, RSV, Combined\u202f\u202f",
-            "programCode": [
-                "009:037"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78181,49 +78152,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/rdmq-nq56",
+            "issued": "2023-12-18",
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
+            "landingPage": "https://data.cdc.gov/d/rdmq-nq56",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:037"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "2022-10-01/2023-01-27",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "NSSP Emergency Department Visit Trajectories by State and Sub State Regions- COVID-19, Flu, RSV, Combined\u202f\u202f"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fj6i-3v3k",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "confirmed",
-                "hepatitis b",
-                "hepatitis c acute",
-                "nedss",
-                "netss",
-                "nndss",
-                "perinatal infection",
-                "probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fj6i-3v3k",
             "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78246,85 +78221,93 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fj6i-3v3k",
+            "issued": "2022-01-14",
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
+            "landingPage": "https://data.cdc.gov/d/fj6i-3v3k",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hrcu-si9w",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "chip",
-                "dq atlas",
-                "medicaid",
-                "perinatal care",
-                "t-msis analytic files"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "ed67e610-aed3-4bed-842f-e6044511dd64",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of perinatal care, including prenatal visits, prenatal bundled payments, postpartum visits, and postpartum bundled payments, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating perinatal care measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas  for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Perinatal Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Perinatal-Care-Services-Provided-to-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of perinatal care, including prenatal visits, prenatal bundled payments, postpartum visits, and postpartum bundled payments, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating perinatal care measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas  for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of perinatal care, including prenatal visits, prenatal bundled payments, postpartum visits, and postpartum bundled payments, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating perinatal care measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas  for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Perinatal-Care-Services-Provided-to-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
+                    "mediaType": "text/csv",
                     "title": "Perinatal Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44"
                 }
             ],
+            "identifier": "ed67e610-aed3-4bed-842f-e6044511dd64",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "perinatal care",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/hrcu-si9w",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-01-05",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Perinatal Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/en3s-hzsr",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
-                "abcs",
-                "bactfacts"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Active Bacterial Core surveillance",
                 "hasEmail": "mailto:abcs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/en3s-hzsr",
             "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul>  <li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\n                Find details about surveillance population, case determination, surveillance evaluation, and more.  </li>                    <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>  \n                 Get official interpretations from reports and publications created from ABCs data.        </li> </ul>",
-            "title": "Active Bacterial Core surveillance (ABCs) Streptococcus pneumoniae",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78347,52 +78330,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/en3s-hzsr",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/en3s-hzsr",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Active Bacterial Core surveillance (ABCs) Streptococcus pneumoniae"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-employee-detail-nursing-home-staffing",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-07-27",
-            "temporal": "2020-04-01/2024-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "references": [
-                "https://data.cms.gov/resources/payroll-based-journal-employee-detail-nursing-home-staffing-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "hospitals & facilities",
-                "medicare",
-                "original medicare",
-                "skilled nursing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nursing Home Staffing - CCSQ (PBJ Reports)",
                 "hasEmail": "mailto:nhstaffing@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/d65b8be0-946e-410b-ab06-01829628d5a1/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-employee-detail-nursing-home-staffing-data-dictionary",
             "description": "The Payroll Based Journal (PBJ) Employee Detail Nursing Home Staffing dataset provides information submitted by nursing homes including rehabilitation services on a quarterly basis. The data include a system generated employee identification number, work date, job type and employment status, and hours worked for each nursing home employee.\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Payroll Based Journal Employee Detail Nursing Home Staffing",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d65b8be0-946e-410b-ab06-01829628d5a1/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d65b8be0-946e-410b-ab06-01829628d5a1/data",
+                    "mediaType": "text/html",
                     "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2024-04-01"
                 },
                 {
@@ -78600,47 +78579,49 @@
                     "title": "Payroll Based Journal Employee Detail Nursing Home Staffing : 2020-06-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-employee-detail-nursing-home-staffing-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/d65b8be0-946e-410b-ab06-01829628d5a1/data-viewer",
+            "issued": "2023-07-27",
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-employee-detail-nursing-home-staffing",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-10-31",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/payroll-based-journal-employee-detail-nursing-home-staffing-methodology"
+            ],
+            "temporal": "2020-04-01/2024-06-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Payroll Based Journal Employee Detail Nursing Home Staffing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/vtwh-v35w",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2023-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "api",
-                "mesh",
-                "mesh 2023 update",
-                "terminologies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vtwh-v35w",
             "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Registry Number Update Report lists changes to Registry Numbers on a Descriptor or Supplementary Concept Record (SCR).  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Registry Number Update Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78663,46 +78644,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vtwh-v35w",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/vtwh-v35w",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-16",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Terminology"
-            ]
+            ],
+            "title": "MeSH 2025 Update - Registry Number Update Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/irpc-yf8f",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "giardiasis",
-                "gonorrhea",
-                "haemophilus influenza",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/irpc-yf8f",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Data for Haemophilus influenzae (age <5 for serotype b, nontypeable, non-b serotype, and unknown serotype) are available in Table I.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78725,45 +78701,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/irpc-yf8f",
+            "issued": "2018-01-04",
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
+            "landingPage": "https://data.cdc.gov/d/irpc-yf8f",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/w79a-dgrh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "hemolytic uremic syndrome post-diarrheal",
-                "hepatitis (viral acute) type a",
-                "hepatitis (viral acute) type b",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/w79a-dgrh",
             "description": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78786,20 +78763,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w79a-dgrh",
+            "issued": "2021-01-21",
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
+            "landingPage": "https://data.cdc.gov/d/w79a-dgrh",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2013",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.</p>\n<p>Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.<br />\nThis study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2013) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -78812,64 +78825,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2013",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.</p>\n<p>Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.<br />\nThis study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2013)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2013) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2013-nid13626"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2013)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#trends",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-06",
-            "@type": "dcat:Dataset",
-            "temporal": "Data from 2020-03-14 to present (posted starting 2023-06-06)",
-            "modified": "2025-01-30",
-            "references": [
-                "https://covid.cdc.gov/covid-data-tracker/"
-            ],
-            "keyword": [
-                "covid19",
-                "nrevss",
-                "test"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Virologic Unit, Surveillance and Analytics Team",
                 "hasEmail": "mailto:nrevss@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gvsb-yw6g",
             "description": "More than 450 public health and clinical laboratories located throughout the United States participate in surveillance for severe acute respiratory virus coronavirus type 2 (SARS-CoV-2), the virus that causes COVID-19, through CDC's National Respiratory and Enteric Virus Surveillance System (NREVSS). The dataset contains a weekly summary of aggregate counts of the total SARS-CoV-2 tests and SARS-CoV-2 detections reported to NREVSS since March 14, 2020. These data are reported weekly on a voluntary basis. Clinical laboratories do not report demographic data through NREVSS. Testing practices may vary regionally, and the number of participating laboratories may change from year to year. Results can be changed for up to 2 years after the initial reporting week. However, discrepancies may be noted and updated at the discretion of the data stewards and key stakeholders.\n\nWhile NREVSS strives to present the most precise estimates of respiratory viral trends with reporting burden minimized for participating laboratories, there are several inherent limitations to this surveillance system.\n\nNREVSS does not collect patient-specific data or demographic information. Multiple samples may be collected from a single patient, so NREVSS results do not necessarily reflect the number of patients tested, nor do they directly reflect hospitalizations or deaths related to COVID-19.\n\nParticipating laboratories vary in size, testing capabilities, and areas served. Some institutions may receive and test samples from sites across a given state or even from multiple states. Without direct knowledge of the population base, NREVSS cannot be used to determine the prevalence or incidence of infection.\n\nFor more information on NREVSS and COVID-19 surveillance please visit: https://www.cdc.gov/surveillance/nrevss. These data appear starting May 25, 2023 on the CDC COVID Data Tracker at the following URLs: https://covid.cdc.gov/covid-data-tracker/#trends ; https://covid.cdc.gov/covid-data-tracker/#cases.   \n\nNREVSS data are reported at the national and HHS regional levels. The ten (10) U.S. Department of HHS regions are defined here: https://www.hhs.gov/about/agencies/iea/regional-offices/index.html. \n\nThe data represent SARS-CoV-2 Nucleic Acid Amplification Test (NAAT) results, which include reverse transcriptase-polymerase chain reaction (RT-PCR) tests from a voluntary, sentinel network of participating laboratories in the United States, including clinical, public health and commercial laboratories (https://www.cdc.gov/surveillance/nrevss/labs/index.html). \n\nThese data exclude antigen, antibody, and at-home test results. \n\nAll data are provisional and subject to change. Reporting is less complete for the past 1 week, and more complete (>90%) for the period 2 weeks earlier. \n\nThere are data from all states across the 10 HHS regions. Because the data are from a sentinel network of laboratories, however, results may vary geographically. The data do not include all test results within a jurisdiction and therefore do not reflect all SARS-CoV-2 NAATs administered in the United States. \n\nPercent positivity is one of the surveillance metrics used to monitor COVID-19 transmission over time and by area. Percent positivity is calculated by dividing the number of positive NAATs by the total number of NAATs administered, then multiplying by 100 [(# of positive NAAT tests / total NAAT tests) x 100].\n\nThe data represent laboratory tests performed, not individual (deduplicated) results in people. In the table and upon hovering on the map, the total test counts in the data reflect the latest data reported from NREVSS laboratories and may not match the data presented by various jurisdictions.\n\nOn May 11, 2023, CDC discontinued utilizing the COVID electronic laboratory reporting (CELR) platform as the primary laboratory source of COVID-19 results. These data are archived at health.data.gov.\n\nFor more information about NREVSS, please see: https://www.cdc.gov/surveillance/nrevss/",
-            "title": "Percent Positivity of COVID-19 Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78892,26 +78871,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/gvsb-yw6g",
+            "issued": "2023-06-06",
+            "keyword": [
+                "covid19",
+                "nrevss",
+                "test"
+            ],
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#trends",
+            "language": [
+                "English"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://covid.cdc.gov/covid-data-tracker/"
+            ],
+            "spatial": "US",
+            "temporal": "Data from 2020-03-14 to present (posted starting 2023-06-06)",
             "theme": [
                 "Laboratory Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Percent Positivity of COVID-19 Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/medlineplus-connect-electronic-health-record-ehr-systems-web-application",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>A Web application that allows patient portals and electronic health record (EHR) systems to use existing code sets to link to relevant, authoritative health information from MedlinePlus.gov.  Matches ICD-9-CM or SNOMED CT codes to related MedlinePlus consumer health information, LOINC codes to information on lab tests, and also matches NDC, RXCUI or text strings to patient medication information.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nlm.nih.gov/medlineplus/connect/application.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool"
+                }
+            ],
+            "identifier": "f15aa02b-4129-4abc-b1f4-d74896ac7c5a",
             "issued": "2012-05-30",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "biomedical research",
                 "connect",
@@ -78937,70 +78949,34 @@
                 "snowmed ct",
                 "wellness"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/medlineplus-connect-electronic-health-record-ehr-systems-web-application",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Institutes of Health (NIH)"
             },
-            "identifier": "f15aa02b-4129-4abc-b1f4-d74896ac7c5a",
-            "description": "<p>A Web application that allows patient portals and electronic health record (EHR) systems to use existing code sets to link to relevant, authoritative health information from MedlinePlus.gov.  Matches ICD-9-CM or SNOMED CT codes to related MedlinePlus consumer health information, LOINC codes to information on lab tests, and also matches NDC, RXCUI or text strings to patient medication information.</p>",
-            "title": "MedlinePlus Connect for Electronic Health Record (EHR) Systems - Web Application",
-            "programCode": [
-                "009:046"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nlm.nih.gov/medlineplus/connect/application.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "MedlinePlus Connect for Electronic Health Record (EHR) Systems - Web Application"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/azpx-5hzx",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "hansen's disease",
-                "hantavirus infection",
-                "hantavirus pulmonary syndrome",
-                "nedss",
-                "netss",
-                "nndss",
-                "non-hantavirus pulmonary syndrome",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/azpx-5hzx",
             "description": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79023,40 +78999,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/azpx-5hzx",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/azpx-5hzx",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hwwg-9k4v",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-06-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
-            "keyword": [
-                "drug utilization",
-                "medicaid reimbursements",
-                "pharmacy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "1db0f12c-e4d6-5a70-8c1b-5af9635999be",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2010",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79064,40 +79047,42 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "1db0f12c-e4d6-5a70-8c1b-5af9635999be",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/hwwg-9k4v",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-06-11",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "State Drug Utilization"
-            ]
+            ],
+            "title": "State Drug Utilization Data 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "accrualPeriodicity": "NA",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-07",
-            "temporal": "1999-2018",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-17",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/visualization/"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:CDCINFO@CDC.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/iqm3-hbev",
+            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "description": "List of footnotes, notes, and source information for NHANES Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHANES Datasets.",
-            "title": "DQS NHANES Footnotes",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79120,49 +79105,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "identifier": "https://data.cdc.gov/api/views/iqm3-hbev",
+            "issued": "2024-02-07",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "NA",
+            "modified": "2024-09-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/visualization/"
+            ],
+            "spatial": "United States",
+            "temporal": "1999-2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS NHANES Footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ntaa-dtex",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-17",
-            "references": [
-                "https://chronicdata.cdc.gov/d/x7ys-5vpn"
-            ],
-            "keyword": [
-                "american lung association",
-                "cessation coverage",
-                "comprehensive medicaid coverage",
-                "medicaid coverage of cessation treatment",
-                "office on smoking and health",
-                "osh"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ntaa-dtex",
+            "describedBy": "https://chronicdata.cdc.gov/Cessation-Coverage-/Medicaid-Coverage-Of-Cessation-Treatments-And-Barr/ntaa-dtex",
             "description": "2008-2024. American Lung Association. Cessation Coverage.  Medicaid data compiled by the Centers for Disease Control and Prevention\u2019s Office on Smoking and Health were obtained from the State Tobacco Cessation Coverage Database, developed and administered by the American Lung Association.  Data from 2008-2012 are reported on an annual basis; beginning in 2013 data are reported on a quarterly basis.  Data include state-level information on Medicaid coverage of approved medications by the Food and Drug Administration (FDA) for tobacco cessation treatment; types of counseling recommended by the Public Health Service (PHS) and barriers to accessing cessation treatment. Note: Section 2502 of the Patient Protection and Affordable Care Act requires all state Medicaid programs to cover all FDA-approved tobacco cessation medications as of January 1, 2014. However, states are currently in the process of modifying their coverage to come into compliance with this requirement. Data in the STATE System on Medicaid coverage of tobacco cessation medications reflect evidence of coverage that is found in documentable sources, and may not yet reflect medications covered under this requirement.",
-            "title": "Medicaid Coverage Of Cessation Treatments And Barriers To Treatments",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79185,36 +79162,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Cessation-Coverage-/Medicaid-Coverage-Of-Cessation-Treatments-And-Barr/ntaa-dtex",
+            "identifier": "https://data.cdc.gov/api/views/ntaa-dtex",
+            "issued": "2023-07-18",
+            "keyword": [
+                "american lung association",
+                "cessation coverage",
+                "comprehensive medicaid coverage",
+                "medicaid coverage of cessation treatment",
+                "office on smoking and health",
+                "osh"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ntaa-dtex",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/x7ys-5vpn"
+            ],
             "theme": [
                 "Cessation Coverage"
-            ]
+            ],
+            "title": "Medicaid Coverage Of Cessation Treatments And Barriers To Treatments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n7uz-829a",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Allergy and Clinical Immunology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/n7uz-829a",
             "description": "SARS-CoV-2 is a highly infectious respiratory virus that is primarily transmitted by respiratory aerosols and droplets emitted during activities such as talking, breathing, and coughing.  Because symptomatic and asymptomatic individuals with COVID-19 can exhibit a high viral load of SARS-CoV-2 in their respiratory fluids, the CDC recommends that people wear a face mask that covers the nose and mouth to reduce community transmission during the COVID-19 pandemic. Wearing a face mask to protect others from potentially infectious droplets, called source control, has been shown to be a highly effective infection control strategy to limit the spread of COVID-19.  The presence of mask face seal leaks enables respiratory aerosols to escape out rather than pass through the filtering materials of the mask, consequently reducing the benefits of wearing a face mask for source control.  As such, the current investigation examines various modifications that improve the fit of a medical or cloth face mask and reduce the amounts of expelled aerosols during simulated coughs and exhalations.",
-            "title": "Face mask fit modifications that improve source control performance dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79222,39 +79209,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n7uz-829a",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/n7uz-829a",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Face mask fit modifications that improve source control performance dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hyc2-qtk4",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-11",
-            "keyword": [
-                "amp",
-                "average manufacturer price"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "91d4309d-3ca8-5a1e-8f78-79984027392d",
             "description": "Drugs that have been reported under the Medicaid Drug Rebate Program along with an indication of whether or not the required Average Manufacturer Price (AMP) was reported for each drug. All drugs are identified in the file by the 11-digit National Drug Code, product name, labeler name, and reported (R) or not reported (NR).",
-            "title": "Drug AMP Reporting - Monthly",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79262,53 +79246,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "91d4309d-3ca8-5a1e-8f78-79984027392d",
+            "issued": "2017-03-21",
+            "keyword": [
+                "amp",
+                "average manufacturer price"
+            ],
+            "landingPage": "https://healthdata.gov/d/hyc2-qtk4",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-09-11",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "Drug AMP Reporting - Monthly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "disability",
-                "gis",
-                "health",
-                "outcomes",
-                "places",
-                "prevalence",
-                "prevention",
-                "risk",
-                "status",
-                "zcta",
-                "zip code"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/c7b2-4ecy",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 36 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
-            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79331,41 +79302,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "identifier": "https://data.cdc.gov/api/views/c7b2-4ecy",
+            "issued": "2024-07-15",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/sutils/static/prosplign/prosplign.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "protein",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/dz4r-nx2x",
             "description": "A utility for computing alignment of proteins to genomic nucleotide sequence based on a variation of the Needleman Wunsch global alignment algorithm and specifically accounts for introns and splice signals.",
-            "title": "ProSplign",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79374,92 +79356,86 @@
                     "title": "ProSplign - Download"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/dz4r-nx2x",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/sutils/static/prosplign/prosplign.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "ProSplign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/hzsh-xp8k",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "75ff3421-7f51-5d22-af3c-83c71affd5eb",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure.csv",
-                    "description": "CoreSEt measure v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "75ff3421-7f51-5d22-af3c-83c71affd5eb",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/hzsh-xp8k",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt measure v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ydsy-yh5w",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
-                "invasive pneumococcal disease",
-                "legionellosis",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "pneumococcal",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ydsy-yh5w",
             "description": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years. Since 2010, case notifications for this condition were consolidated under one event code for Invasive pneumococcal disease.",
-            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79482,51 +79458,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ydsy-yh5w",
+            "issued": "2016-01-07",
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
+            "landingPage": "https://data.cdc.gov/d/ydsy-yh5w",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/aging/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-29",
-            "references": [
-                "https://www.cdc.gov/aging/index.html"
-            ],
-            "keyword": [
-                "aging",
-                "alcohol",
-                "caregiver",
-                "cognitive health",
-                "falls",
-                "fruits and vegetables",
-                "obesity",
-                "overall health",
-                "screenings",
-                "smoking",
-                "vaccines"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DPH Public Inquiries",
                 "hasEmail": "mailto:PublicInquiriesDPH@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hfr9-rurv",
+            "describedBy": "https://chronicdata.cdc.gov/Healthy-Aging/Alzheimer-s-Disease-and-Healthy-Aging-Data/hfr9-rurv",
             "description": "2015-2022. This data set contains data from BRFSS.",
-            "title": "Alzheimer's Disease and Healthy Aging Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79549,52 +79521,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Healthy-Aging/Alzheimer-s-Disease-and-Healthy-Aging-Data/hfr9-rurv",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "identifier": "https://data.cdc.gov/api/views/hfr9-rurv",
+            "issued": "2024-04-29",
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
+            "landingPage": "https://www.cdc.gov/aging/index.html",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-04-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/aging/index.html"
+            ],
             "theme": [
                 "Healthy Aging"
-            ]
+            ],
+            "title": "Alzheimer's Disease and Healthy Aging Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-04-28",
-            "temporal": "2020-01-01/2020-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-03",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "county",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "quarterly",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ypxr-mz8e",
             "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by United States county of residence and age group, for 2020 by quarter.",
-            "title": "AH Provisional COVID-19 Deaths by Quarter, County and Age for 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79617,45 +79589,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ypxr-mz8e",
+            "issued": "2021-04-28",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Quarter, County and Age for 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/respvaxview/about/index.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "covid-19 vaccination",
-                "nis-acm",
-                "rsv vaccination",
-                "vaccination",
-                "vaccination coverage",
-                "vaccine confidence"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/si7g-c2bs",
             "description": "\u2022 National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on the updated 2024-25 COVID-19 vaccine, the 2024-25 seasonal flu vaccine, and the RSV vaccine uptake and confidence. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics. \n\n\u2022 The data start in September 2024.\n\n\u2022 The archived data can be found here: \n- 2023-24 season: https://data.cdc.gov/Vaccinations/National-Immunization-Survey-Adult-COVID-Module-NI/uc4z-hbsd/about_data\n- Before October 2023:  \nhttps://data.cdc.gov/Vaccinations/National-Immunization-Survey-Adult-COVID-Module-NI/udsf-9v7b/about_data",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): RespVaxView| Data | Centers for Disease Control and Prevention (cdc.gov)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79678,58 +79657,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/si7g-c2bs",
+            "issued": "2024-11-20",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis-acm",
+                "rsv vaccination",
+                "vaccination",
+                "vaccination coverage",
+                "vaccine confidence"
+            ],
+            "landingPage": "https://www.cdc.gov/respvaxview/about/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): RespVaxView| Data | Centers for Disease Control and Prevention (cdc.gov)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-inpatient-hospitals-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "original medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicare Provider Data - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-provider-and-service-data-dictionary-0",
             "description": "The Medicare Inpatient Hospitals by Provider and Service dataset provides information on inpatient discharges for Original Medicare Part A beneficiaries by IPPS\u00a0hospitals. It includes information on the use, payment, and hospital charges for more than 3,000 U.S. hospitals that received IPPS payments.\u00a0The data are organized by hospital and Medicare Severity Diagnosis Related Group (DRG).\n\n\u00a0\n\nHospitals determine what they will charge for items and services provided to patients, and these charges are the amount the hospital bills for an item or service. The Total Payment Amount includes the DRG amount, claim per diem amount, beneficiary primary payer claim payment amount, beneficiary Part A (Hospital Insurance)\u00a0coinsurance amount, beneficiary deductible amount, beneficiary blood deductible amount and diagnosis related group outlier amount.",
-            "title": "Medicare Inpatient Hospitals - by Provider and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Inpatient Hospitals - by Provider and Service : 2022-12-01"
                 },
                 {
@@ -79853,41 +79831,50 @@
                     "title": "Medicare Inpatient Hospitals - by Provider and Service : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-provider-and-service-data-dictionary-0",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/690ddc6c-2767-4618-b277-420ffb2bf27c/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-inpatient-hospitals-methodology"
+            ],
+            "temporal": "2013-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Inpatient Hospitals - by Provider and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bucw-etpd",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bucw-etpd",
             "description": "Over-exposure of the hand-arm system to intense vibration and force over time may cause degeneration of the vascular, neurological, and musculoskeletal systems in the fingers. A novel animal model using rat tails has been developed to understand the health effects on human fingers exposed to vibration and force when operating powered hand tools or workpieces. The biodynamic responses, such as vibration stress, strain, and power absorption density, of the rat tails can be used to help evaluate the health effects related to vibration and force and to establish a dose-effect relationship. While the biodynamic responses of cadaver rat tails have been investigated, the objective of the current study was to determine whether the biodynamic responses of living rat tails are different from those of cadaver rat tails, and whether the biodynamic responses of both living and cadaver tails change with exposure duration. To make direct comparisons, the responses of both cadaver and living rat tails were examined on four different testing stations. The transfer function of each tail under a given contact force (2 N) was measured at each frequency in the one-third octave bands from 20 to 1000 Hz, and used to calculate the mechanical system parameters of the tails. The transfer function was also measured at different exposure durations to determine the time dependency of the response. The biodynamic responses of both cadaver and living rat tails, and the modeling results and time dependency are presented in a manuscript of this study (Warren et al., 2024), the original datasets measured in each trial of the tests are documented in this data description.",
-            "title": "Rat-Tail Models for Studying Hand-Arm Vibration Syndrome:  A Comparison between Living and Cadaver Rat Tails",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79895,42 +79882,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bucw-etpd",
+            "issued": "2024-12-02",
+            "landingPage": "https://data.cdc.gov/d/bucw-etpd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-02",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Rat-Tail Models for Studying Hand-Arm Vibration Syndrome:  A Comparison between Living and Cadaver Rat Tails"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/dhcs/ed-visits/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-01",
-            "temporal": "2016/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-25",
-            "keyword": [
-                "emergency department",
-                "national hospital ambulatory medical care survey",
-                "primary diagnosis",
-                "reason for visit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:ambcare@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ycxr-emue",
             "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS), conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to emergency departments to describe patterns of utilization and provision of ambulatory care delivery in the United States. Data are collected from nonfederal, general, and short-stay hospitals from all 50 U.S. states and the District of Columbia, and are used to develop nationally representative estimates. \n\nThe data include counts and rates of emergency department visits from 2016-2022 for the 10 leading primary diagnoses and reasons for visit, stratified by selected patient and hospital characteristics. Rankings for the 10 leading categories were identified using weighted data from 2022 and were then assessed in prior years.",
-            "title": "Estimates of Emergency Department Visits in the United States from 2016-2022",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79953,24 +79934,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ycxr-emue",
+            "issued": "2022-06-01",
+            "keyword": [
+                "emergency department",
+                "national hospital ambulatory medical care survey",
+                "primary diagnosis",
+                "reason for visit"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/dhcs/ed-visits/index.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2024-07-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2016/2022",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Estimates of Emergency Department Visits in the United States from 2016-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://seer.cancer.gov/",
             "bureauCode": [
                 "009:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Cancer Institute (NCI)",
+                "hasEmail": "mailto:NCIinfo@nih.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>SEER Limited-Use cancer incidence data with associated population data. Geographic areas available are county and SEER registry.  The Surveillance, Epidemiology, and End Results (SEER) Program of the National Cancer Institute collects and distributes high quality, comprehensive cancer data from a number of population-based cancer registries. Data include patient demographics, primary tumor site, morphology, stage at diagnosis, first course of treatment, and follow-up for vital status. The SEER Program is the only comprehensive source of population-based information in the United States that includes stage of cancer at the time of diagnosis and survival rates within each stage.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://seer.cancer.gov/canques/incidence.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "68efde71-93b1-440d-b7d1-1847114d16ad",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alaska",
                 "aleukemic",
@@ -80066,46 +80079,46 @@
                 "vagina",
                 "vulva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Cancer Institute (NCI)",
-                "hasEmail": "mailto:NCIinfo@nih.gov"
-            },
+            "landingPage": "https://seer.cancer.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:047"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Cancer Institute (NCI), National Institutes of Health (NIH)"
             },
-            "identifier": "68efde71-93b1-440d-b7d1-1847114d16ad",
-            "description": "<p>SEER Limited-Use cancer incidence data with associated population data. Geographic areas available are county and SEER registry.  The Surveillance, Epidemiology, and End Results (SEER) Program of the National Cancer Institute collects and distributes high quality, comprehensive cancer data from a number of population-based cancer registries. Data include patient demographics, primary tumor site, morphology, stage at diagnosis, first course of treatment, and follow-up for vital status. The SEER Program is the only comprehensive source of population-based information in the United States that includes stage of cancer at the time of diagnosis and survival rates within each stage.</p>",
-            "title": "Cancer Incidence - Surveillance, Epidemiology, and End Results (SEER) Registries Limited-Use",
-            "programCode": [
-                "009:047"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://seer.cancer.gov/canques/incidence.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Cancer Incidence - Surveillance, Epidemiology, and End Results (SEER) Registries Limited-Use"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/b2qj-y9ew",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS7-technical-documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, and questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, along with questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/b2qj-y9ew",
             "issued": "2023-06-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2022",
-            "modified": "2023-06-06",
             "keyword": [
                 "chronic health conditions",
                 "disability",
@@ -80125,68 +80138,37 @@
                 "traumatic brain injury",
                 "vaccination"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/b2qj-y9ew",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-06-06",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/b2qj-y9ew",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, and questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, along with questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-                    "@type": "dcat:Distribution",
-                    "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS7-technical-documentation.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/state-snapshots",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "health care quality",
-                "nhqr",
-                "quality measurement",
-                "state health care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
-            },
-            "identifier": "234049e8-dd71-4b9d-8dc2-ab56471b9011",
+            "dataQuality": true,
             "description": "<p>The State Snapshots provide graphical representations of State-specific health care quality information, including strengths, weaknesses, and opportunities for improvement. The goal is to help State officials and their public- and private-sector partners better understand health care quality and disparities in their State. State-level information used to create the State Snapshots is based on data collected for the National Healthcare Quality Report (NHQR). The State Snapshots include summary measures of quality of care and States' performances relative to all States, the region, and best performing States by overall health care quality, types of care (preventive, acute, and chronic), settings of care (hospitals, ambulatory care, nursing home, and home health), and clinical conditions (cancer, diabetes, heart disease, maternal and child health, and respiratory diseases). Special focus areas on diabetes, asthma, Healthy People 2010, clinical preventive services, disparities, payer, and variation over time are also featured. The Agency for Healthcare Research and Quality (AHRQ) has released the State Snapshots each year in conjunction with the 2004 NHQR through the 2009 NHQR.</p>",
-            "title": "State Snapshots",
-            "programCode": [
-                "009:072"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80195,49 +80177,43 @@
                     "title": "Query Tool "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "234049e8-dd71-4b9d-8dc2-ab56471b9011",
+            "issued": "2012-05-30",
+            "keyword": [
+                "health care quality",
+                "nhqr",
+                "quality measurement",
+                "state health care"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/state-snapshots",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
             "theme": [
                 "Health",
                 "Quality",
                 "State"
-            ]
+            ],
+            "title": "State Snapshots"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yqwx-bvu7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "invasive pneumococcal disease",
-                "legionellosis",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "pneumococcal",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yqwx-bvu7",
             "description": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years.",
-            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80260,42 +80236,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yqwx-bvu7",
+            "issued": "2017-01-05",
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
+            "landingPage": "https://data.cdc.gov/d/yqwx-bvu7",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "keyword": [
-                "middle school",
-                "risk behavior",
-                "survey",
-                "youth online",
-                "yrbs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DASH Public Inquiries",
                 "hasEmail": "mailto:nccddashinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/k5bc-k3g8",
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/k5bc-k3g8",
             "description": "1991-2017. Middle School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): Middle School",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80318,36 +80299,42 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/k5bc-k3g8",
+            "identifier": "https://data.cdc.gov/api/views/k5bc-k3g8",
+            "issued": "2023-07-19",
+            "keyword": [
+                "middle school",
+                "risk behavior",
+                "survey",
+                "youth online",
+                "yrbs"
+            ],
+            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Youth Risk Behaviors"
-            ]
+            ],
+            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): Middle School"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/uhs4-vv7g",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-09",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allergy and Clinical Immunology Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/uhs4-vv7g",
             "description": "Nickel is one of the most common contact allergens worldwide. Despite this prevalence, many of the underlying immunological mechanisms responsible for nickel allergy remain unclear. This knowledge gap is partially attributable to the inherent resistance of laboratory rodents (mice and rats) to dermal sensitization with nickel salts. The fundamental goal of this study was to assess the potential utility of the novel humanized Toll-like receptor-4 (hTLR-4) mouse model for use in future in vivo studies of nickel allergy. Accordingly, hTLR-4 positive and negative mice of both sexes were first incorporated into a Local Lymph Node Assay (LLNA) to evaluate dermal sensitization following topical exposure to soluble nickel salts (NiSO4). The ensuing immune responses were then characterized further by incorporating female and male hTLR-4 positive mice into a non-radioactive endpoint-based assay. Utilizing the same exposure scheme as in the LLNA, mice were euthanized following exposure and the auricular lymph nodes, spleen, and blood were collected to assess various immunological parameters associated with allergy and ACD.",
-            "title": "Assessment of dermal sensitization by nickel salts in a novel humanized TLR-4 mouse model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80355,47 +80342,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uhs4-vv7g",
+            "issued": "2024-12-09",
+            "landingPage": "https://data.cdc.gov/d/uhs4-vv7g",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-09",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Assessment of dermal sensitization by nickel salts in a novel humanized TLR-4 mouse model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hatw-7gqy",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "all serogroups",
-                "meningococcal disease (neisseria meningitidis)",
-                "mmwr",
-                "mumps",
-                "nedss",
-                "netss",
-                "nndss",
-                "pertussis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hatw-7gqy",
             "description": "NNDSS - Table II. Meningococcal to Pertussis - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Data for meningococcal disease, invasive caused by serogroups ACWY, serogroup B, other serogroups, and unknown serogroups are available in Table I.",
-            "title": "NNDSS - Table II. Meningococcal to Pertussis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80418,46 +80393,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hatw-7gqy",
+            "issued": "2018-01-04",
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
+            "landingPage": "https://data.cdc.gov/d/hatw-7gqy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Meningococcal to Pertussis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7xhe-mv2e",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "imported",
-                "indigenous",
-                "malaria",
-                "measles",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7xhe-mv2e",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNotice:  Measles data for weeks 1-4 (in Table 1v) were updated on 02-28-2020 to correct the classification of imported and indigenous. For all weeks, measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80480,39 +80456,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7xhe-mv2e",
+            "issued": "2020-01-21",
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
+            "landingPage": "https://data.cdc.gov/d/7xhe-mv2e",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/VAST/vast.shtml",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "protein",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/w6ya-ncpm",
             "description": "A computer algorithm that identifies similar protein 3-dimensional structures. Structure neighbors for every structure in MMDB are pre-computed and accessible via links on the MMDB Structure Summary pages.",
-            "title": "Vector Alignment Search Tool (VAST)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80521,41 +80504,40 @@
                     "title": "Vector Alignment Search Tool (VAST)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/w6ya-ncpm",
+            "issued": "2021-07-01",
+            "keyword": [
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/VAST/vast.shtml",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "Vector Alignment Search Tool (VAST)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "references": [
-                "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135509.htm"
-            ],
-            "keyword": [
-                "cdrh"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "7e7f6062-5270-4e09-81c9-ff22261232ac",
+            "describedBy": "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135508.htm",
             "description": "This database contains product names and associated information developed by the Center for all products, both medical and non-medical, which emit radiation. It includes a three letter product code, a descriptor for radiation type, applicable performance standard(s), and a definition for the code.",
-            "title": "Radiation-emitting Electronic Product Codes",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80563,42 +80545,39 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135508.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "7e7f6062-5270-4e09-81c9-ff22261232ac",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135509.htm"
+            ],
+            "title": "Radiation-emitting Electronic Product Codes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/seuz-s2cv",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "coronavirus",
-                "covid19",
-                "ncird",
-                "ncird-corvd",
-                "ncird-id",
-                "respiratory-virus-response",
-                "rsv"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREVSS",
                 "hasEmail": "mailto:Nrevss@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/seuz-s2cv",
             "description": "Percent of tests positive for a pathogen is one of the surveillance metrics used to monitor respiratory pathogen transmission over time. The percent of tests positive is calculated by dividing the number of positive tests by the total number of tests administered, then multiplying by 100 [(# of positive tests/total tests) x 100]. These data include percent of tests positive values for the detection of severe acute respiratory virus coronavirus type 2 (SARS-CoV-2), the virus that causes COVID-19 and Respiratory syncytial virus (RSV) reported to the National Respiratory and Enteric Virus Surveillance System (NREVSS), a sentinel network of laboratories located through the US, includes clinical, public health and commercial laboratories; additional information available at: https://www.cdc.gov/surveillance/nrevss/index.html. Influenza results include clinical laboratory test results from NREVSS and U.S. World Health Organization collaborating laboratories; more details about influenza virologic surveillance are available here:\u202fhttps://www.cdc.gov/flu/weekly/overview.html. \n\nData represent calculations based on laboratory tests performed, not individual people tested. RSV and COVID-19 are limited to nucleic acid amplification tests (NAATs), also listed as polymerase chain reaction tests (PCR). Participating laboratories report weekly to CDC the total number of RSV tests performed that week and the number of those tests that were positive. The RSV trend graphs display the national average of the weekly % test positivity for the current, previous, and following weeks in accordance with the recommendations for assessing RSV trends by percent (https://academic.oup.com/jid/article/216/3/345/3860464). \n\nAll data are provisional and subject to change.",
-            "title": "Percent of Tests Positive for Viral Respiratory Pathogens",
-            "programCode": [
-                "009:037"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80621,22 +80600,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/seuz-s2cv",
+            "issued": "2023-11-08",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "ncird",
+                "ncird-corvd",
+                "ncird-id",
+                "respiratory-virus-response",
+                "rsv"
+            ],
+            "landingPage": "https://data.cdc.gov/d/seuz-s2cv",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:037"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Percent of Tests Positive for Viral Respiratory Pathogens"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/uniform-facility-data-set-us-ufds-1998",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Uniform Facility Data Set (UFDS) was designed to measure the scope and use of drug abuse treatment services in the United States. The survey collects information from each privately- and publicly-funded facility in the country that provides substance abuse treatment as well as from state-identified facilities that provide other substance abuse services. Data are collected on a number of topics including facility operation, services provided (assessment, therapy, testing, health, continuing care, special programs, transitional services, community outreach, ancillary), type of treatment, numbers of clients, and various client characteristics. The main objective of the UFDS is to produce data that can be used to assess the nature and extent of substance abuse treatment services, to assist in the forecast of treatment resource requirements, to analyze treatment service trends, to conduct national, regional, and state-level comparative analyses of treatment services and utilization, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its on-line equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov/.This\">http://findtreatment.samhsa.gov/.This</a> study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Uniform Facility Data Set  US (UFDS-1998) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -80649,59 +80662,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/uniform-facility-data-set-us-ufds-1998",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632",
-            "description": "<p>The Uniform Facility Data Set (UFDS) was designed to measure the scope and use of drug abuse treatment services in the United States. The survey collects information from each privately- and publicly-funded facility in the country that provides substance abuse treatment as well as from state-identified facilities that provide other substance abuse services. Data are collected on a number of topics including facility operation, services provided (assessment, therapy, testing, health, continuing care, special programs, transitional services, community outreach, ancillary), type of treatment, numbers of clients, and various client characteristics. The main objective of the UFDS is to produce data that can be used to assess the nature and extent of substance abuse treatment services, to assist in the forecast of treatment resource requirements, to analyze treatment service trends, to conduct national, regional, and state-level comparative analyses of treatment services and utilization, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its on-line equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov/.This\">http://findtreatment.samhsa.gov/.This</a> study has 1 Data Set.</p>",
-            "title": "Uniform Facility Data Set  US (UFDS-1998)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632",
-                    "description": "Uniform Facility Data Set  US (UFDS-1998) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1998-nid13632"
-                }
-            ]
+            "title": "Uniform Facility Data Set  US (UFDS-1998)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b58h-s9zx",
+            "accrualPeriodicity": "Never",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2020-07-20",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-25",
-            "keyword": [
-                "covid-19",
-                "provider relief fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HRSA Chief Data Officer",
                 "hasEmail": "mailto:PRFdata@hrsa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b58h-s9zx",
             "description": "The bipartisan CARES Act; the Paycheck Protection Program and Health Care Enhancement Act (PPPHCEA); and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act provided $178 billion in relief funds to hospitals and other healthcare providers on the front lines of the coronavirus response. The Department of Health and Human Services through the Health Resources and Services Administration is distributing two rounds of payments to hospitals in High Impact areas for positive COVID-19 admissions. In the first round of the High Impact Allocation, $12 billion was distributed to nearly 400 hospitals who provided inpatient care for 100 or more COVID-19 patients through April 10, 2020. $2 billion of these payments was distributed to these hospitals based on their Medicare disproportionate share and uncompensated care payments. In the second round of funding, $10 billion will be distributed to hospitals having over 161 COVID-19 admissions between January 1 and June 10, 2020.",
-            "title": "Provider Relief Fund COVID-19 High-Impact Payments",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80724,22 +80708,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/b58h-s9zx",
+            "issued": "2020-07-20",
+            "keyword": [
+                "covid-19",
+                "provider relief fund"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b58h-s9zx",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Never",
+            "modified": "2021-01-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "Provider Relief Fund COVID-19 High-Impact Payments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "This feed describes all new items that are being recalled by the FDA.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
+                    "mediaType": "application/rss+xml"
+                }
+            ],
+            "identifier": "e9412021-e775-4c64-9c04-98d6f666786f",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2004-01-01",
             "keyword": [
                 "community health",
                 "foods",
@@ -80749,74 +80760,40 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2004-01-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "e9412021-e775-4c64-9c04-98d6f666786f",
-            "description": "This feed describes all new items that are being recalled by the FDA.",
-            "title": "Food and Drug Administration--Recalls",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
-                    "mediaType": "application/rss+xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "Food and Drug Administration--Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/skilled-nursing-facility-cost-report",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2011-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-25",
-            "references": [
-                "https://data.cms.gov/resources/skilled-nursing-facility-cost-report-methodology"
-            ],
-            "keyword": [
-                "financials",
-                "health care use & payments",
-                "hospitals & facilities",
-                "medicare",
-                "original medicare",
-                "skilled nursing",
-                "value-based care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PDAG Data Products - OEDA",
                 "hasEmail": "mailto:PDAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/a69d3df7-3f66-4a0d-b5b8-0d66049bd565/data-viewer",
-            "description": "The Skilled Nursing Facility (SNF) Cost Report dataset is a public use file that provides select measures from the skilled nursing facility\u00a0annual cost report. This data includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
-            "title": "Skilled Nursing Facility Cost Report",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-12/Skilled%20Nursing%20Facility%20Cost%20Report%20Data%20Dictionary_508.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Skilled Nursing Facility (SNF) Cost Report dataset is a public use file that provides select measures from the skilled nursing facility\u00a0annual cost report. This data includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a69d3df7-3f66-4a0d-b5b8-0d66049bd565/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a69d3df7-3f66-4a0d-b5b8-0d66049bd565/data",
+                    "mediaType": "text/html",
                     "title": "Skilled Nursing Facility Cost Report : 2022-12-02"
                 },
                 {
@@ -80964,46 +80941,52 @@
                     "title": "Skilled Nursing Facility Cost Report : 2011-12-02"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-12/Skilled%20Nursing%20Facility%20Cost%20Report%20Data%20Dictionary_508.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a69d3df7-3f66-4a0d-b5b8-0d66049bd565/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "financials",
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "skilled nursing",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/skilled-nursing-facility-cost-report",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/skilled-nursing-facility-cost-report-methodology"
+            ],
+            "temporal": "2011-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Skilled Nursing Facility Cost Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-15/2022-05-06",
-            "modified": "2023-01-12",
-            "keyword": [
-                "covid-19",
-                "physicians"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kk8c-wtm4",
             "description": "The National Ambulatory Medical Care Survey (NAMCS), conducted by the National Center for Health Statistics (NCHS), collects data on visits to physician offices to describe patterns of ambulatory care delivery in the United States. As part of NAMCS, the Physician Induction Interview collects information about practice characteristics at physician offices. Partway through the 2020 NAMCS, NCHS added questions to the Physician Induction Interview to assess physician experiences related to COVID-19 in office-based settings.\n\nThe data include nationally representative estimates of experiences related to COVID-19 among office-based physicians in the United States, including: shortages of personal protective equipment (PPE) in the past 3 months; the ability to test for COVID-19 in the past 3 months; providers testing positive for COVID-19 in the past 3 months; turning away COVID-19 patients in the past 3 months; and telemedicine or telehealth technology use before and after March 2020.  Estimates were derived from interviews with physicians in periods 3 and 4 of 2020 NAMCS and periods 1 through 4 of 2021 NAMCS, which occurred between December 15, 2020 and May 6, 2022.  The data are considered preliminary, and the results may change with the final data release.",
-            "title": "Physician Experiences Related to COVID-19 from the National Ambulatory Medical Care Survey",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81026,45 +81009,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/kk8c-wtm4",
+            "issued": "2021-10-18",
+            "keyword": [
+                "covid-19",
+                "physicians"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2020-12-15/2022-05-06",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Physician Experiences Related to COVID-19 from the National Ambulatory Medical Care Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/tsa/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "genomics",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/fj8w-mvxu",
             "description": "TSA is an archive of computationally assembled transcript sequences from primary data such as ESTs and Next Generation Sequencing Technologies. The overlapping sequence reads from a complete transcriptome are assembled into transcripts by computational methods instead of by traditional cloning and sequencing of cloned cDNAs. The primary sequence data used in the assemblies must have been experimentally determined by the same submitter. TSA sequence records differ from GenBank records because there are no physical counterparts to the assemblies.",
-            "title": "Transcriptome Shotgun Assembly (TSA) Sequence Database and Submissions",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81079,57 +81061,48 @@
                     "title": "Download TSA"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://submit.ncbi.nlm.nih.gov/subs/tsa/",
-                    "description": "Submission details can be found in the TSA submission guide. https://www.ncbi.nlm.nih.gov/genbank/tsaguide",
                     "@type": "dcat:Distribution",
+                    "description": "Submission details can be found in the TSA submission guide. https://www.ncbi.nlm.nih.gov/genbank/tsaguide",
+                    "downloadURL": "https://submit.ncbi.nlm.nih.gov/subs/tsa/",
+                    "mediaType": "text/html",
                     "title": "TSA Submission Portal"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/fj8w-mvxu",
+            "issued": "2021-08-26",
+            "keyword": [
+                "dataset",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/tsa/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "Transcriptome Shotgun Assembly (TSA) Sequence Database and Submissions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7dk4-g6vg",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2023-07-06",
-            "@type": "dcat:Dataset",
-            "temporal": "8/1/2020 - 5/3/2024",
-            "modified": "2025-01-17",
-            "references": [
-                "CDT aggregate hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-state CDT Hospitalizations Landing Page: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-landing NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
-            ],
-            "keyword": [
-                "admissions",
-                "coronavirus",
-                "covid-19",
-                "hospital capacity",
-                "hospitalizations",
-                "hospital occupancy",
-                "icu beds",
-                "inpatient beds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7dk4-g6vg",
-            "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\nThis dataset represents weekly COVID-19 hospitalization data and metrics aggregated to national, state/territory, and regional levels. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS).</li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.</li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files.</li><li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n\n<b>Metric details:</b><ul><li><b>Time Period:</b> timeseries data will update weekly on Mondays as soon as they are reviewed and verified, usually before 8 pm ET. Updates will occur the following day when reporting coincides with a federal holiday. Note: Weekly updates might be delayed due to delays in reporting. All data are provisional. Because these provisional counts are subject to change, including updates to data reported previously, adjustments can occur. Data may be updated since original publication due to delays in reporting (to account for data received after a given Thursday publication) or data quality corrections.</li><li><b>New COVID-19 Hospital Admissions (count):</b> Number of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>New COVID-19 Hospital Admissions (7-Day Average):</b> 7-day average of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>Cumulative COVID-19 Hospital Admissions:</b> Cumulative total number of admissions of patients with labo",
-            "title": "Weekly United States COVID-19 Hospitalization Metrics by Jurisdiction \u2013 ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\nThis dataset represents weekly COVID-19 hospitalization data and metrics aggregated to national, state/territory, and regional levels. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS).</li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.</li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files.</li><li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n\n<b>Metric details:</b><ul><li><b>Time Period:</b> timeseries data will update weekly on Mondays as soon as they are reviewed and verified, usually before 8 pm ET. Updates will occur the following day when reporting coincides with a federal holiday. Note: Weekly updates might be delayed due to delays in reporting. All data are provisional. Because these provisional counts are subject to change, including updates to data reported previously, adjustments can occur. Data may be updated since original publication due to delays in reporting (to account for data received after a given Thursday publication) or data quality corrections.</li><li><b>New COVID-19 Hospital Admissions (count):</b> Number of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>New COVID-19 Hospital Admissions (7-Day Average):</b> 7-day average of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>Cumulative COVID-19 Hospital Admissions:</b> Cumulative total number of admissions of patients with labo",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81152,42 +81125,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/7dk4-g6vg",
+            "issued": "2023-07-06",
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
+            "landingPage": "https://data.cdc.gov/d/7dk4-g6vg",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "CDT aggregate hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-state CDT Hospitalizations Landing Page: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-landing NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "8/1/2020 - 5/3/2024",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly United States COVID-19 Hospitalization Metrics by Jurisdiction \u2013 ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ia8m-ebiw",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-06-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
-            "keyword": [
-                "drug utilization",
-                "medicaid reimbursements",
-                "pharmacy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "992936b2-2a72-5df6-a734-a56a8631b87a",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2012",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81195,45 +81178,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "992936b2-2a72-5df6-a734-a56a8631b87a",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/ia8m-ebiw",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-06-11",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "State Drug Utilization"
-            ]
+            ],
+            "title": "State Drug Utilization Data 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/uw7a-a5t8",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "nedss",
-                "netss",
-                "nndss",
-                "smallpox",
-                "streptococcal toxic shock syndrome",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/uw7a-a5t8",
             "description": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81256,44 +81234,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uw7a-a5t8",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "smallpox",
+                "streptococcal toxic shock syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/uw7a-a5t8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/tfu6-pjxh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "nedss",
-                "netss",
-                "nndss",
-                "tuberculosis",
-                "tularemia",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tfu6-pjxh",
             "description": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81316,53 +81294,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tfu6-pjxh",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "tuberculosis",
+                "tularemia",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/tfu6-pjxh",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-change-of-ownership-owner-information",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-04-21",
-            "temporal": "2022-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "provider enrollment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/60625dc8-b621-45f0-9423-077fd133b13e/data-viewer",
-            "description": "The Hospital Change of Ownership (CHOW) - Owner Information dataset provides information on individual and organizational ownership interest and managerial control associated with the buyer and seller organizations, role of the owner, association date, address of the organizational owner and other ownership details.",
-            "title": "Hospital Change of Ownership - Owner Information",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Hospital Change of Ownership (CHOW) - Owner Information dataset provides information on individual and organizational ownership interest and managerial control associated with the buyer and seller organizations, role of the owner, association date, address of the organizational owner and other ownership details.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/60625dc8-b621-45f0-9423-077fd133b13e/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/60625dc8-b621-45f0-9423-077fd133b13e/data",
+                    "mediaType": "text/html",
                     "title": "Hospital Change of Ownership - Owner Information : 2024-12-01"
                 },
                 {
@@ -81510,49 +81489,49 @@
                     "title": "Hospital Change of Ownership - Owner Information : 2022-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/60625dc8-b621-45f0-9423-077fd133b13e/data-viewer",
+            "issued": "2022-04-21",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-change-of-ownership-owner-information",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Data_Guidance.pdf"
+            ],
+            "temporal": "2022-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hospital Change of Ownership - Owner Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ttj2-zsyk",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "nedss",
-                "netss",
-                "nndss",
-                "vibriosis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ttj2-zsyk",
             "description": "NNDSS - Table II.  Vibriosis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Vibriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81575,54 +81554,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ttj2-zsyk",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "vibriosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ttj2-zsyk",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-01-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Vibriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/advance-investment-payment-spend-plan",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-01-30",
-            "temporal": "2024-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-29",
-            "references": [
-                "https://data.cms.gov/resources/advance-investment-payment-spend-plan-methodology"
-            ],
-            "keyword": [
-                "accountable care organizations",
-                "coordinated care",
-                "financials",
-                "medicare",
-                "original medicare",
-                "payment models",
-                "value-based care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shared Savings Program - CM",
                 "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/advance-investment-payment-spend-plan-data-dictionary",
             "description": "The Advance Investment Payment Spend Plan data provides payment use, spending category, projected and actual spending of advanced investments payments by Accountable Care Organizations (ACOs).",
-            "title": "Advance Investment Payment Spend Plan",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data",
+                    "mediaType": "text/html",
                     "title": "Advance Investment Payment Spend Plan : 2024-01-02"
                 },
                 {
@@ -81638,46 +81615,51 @@
                     "title": "Advance Investment Payment Spend Plan : 2024-01-02"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/advance-investment-payment-spend-plan-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data-viewer",
+            "issued": "2024-01-30",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "financials",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/advance-investment-payment-spend-plan",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-01-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/advance-investment-payment-spend-plan-methodology"
+            ],
+            "temporal": "2024-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Advance Investment Payment Spend Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x66v-w5ka",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-05-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-04",
-            "keyword": [
-                "centers for disease control and prevention",
-                "environmental health",
-                "foodborne"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "The National Environmental Assessment Reporting System (NEARS)",
                 "hasEmail": "mailto:nears@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x66v-w5ka",
             "description": "This study examined relationships between foodborne outbreak investigation characteristics, such as the epidemiological methods used, and the success of the investigation, as determined by whether the investigation identified an outbreak agent (i.e., pathogen), food item, and contributing factor. This study used data from the Centers for Disease Control and Prevention\u2019s (CDC) National Outbreak Reporting System (NORS) and National Environmental Assessment Reporting System (NEARS) to identify outbreak investigation characteristics associated with outbreak investigation success. We identified investigation characteristics that increase the probability of successful outbreak investigations: a robust epidemiology investigation method; a thorough environmental assessment, as measured by number of visits to complete the assessment; and the collection of clinical samples. This research highlights the importance of a comprehensive outbreak investigation, which includes epidemiology, environmental health, and laboratory personnel working together to solve the outbreak.",
-            "title": "Characteristics Associated with Successful Foodborne Outbreak Investigations, NEARS 2014 - 2016",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81700,43 +81682,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x66v-w5ka",
+            "issued": "2023-05-04",
+            "keyword": [
+                "centers for disease control and prevention",
+                "environmental health",
+                "foodborne"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x66v-w5ka",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-05-04",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Foodborne",
                 "Waterborne",
                 "and Related Diseases"
-            ]
+            ],
+            "title": "Characteristics Associated with Successful Foodborne Outbreak Investigations, NEARS 2014 - 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cde.nlm.nih.gov/home",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
-            "keyword": [
-                "dataset",
-                "health data standards",
-                "medical informatics",
-                "terminologies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/divb-gtqn",
             "description": "The NIH Common Data Elements (CDE) Repository has been designed to provide access to structured human and machine-readable definitions of data elements that have been recommended or required by NIH Institutes and Centers and other organizations for use in research and for other purposes. Visit the NIH CDE Resource Portal for contextual information about the repository.",
-            "title": "NIH Common Data Elements Repository",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81751,20 +81732,52 @@
                     "title": "Search Forms and Download Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/divb-gtqn",
+            "issued": "2016-08-04",
+            "keyword": [
+                "dataset",
+                "health data standards",
+                "medical informatics",
+                "terminologies"
+            ],
+            "landingPage": "https://cde.nlm.nih.gov/home",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-24",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "NIH Common Data Elements Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment.  Data are collected on topics including facility operation, services offered (assessment and pre-treatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.  N-SSATS was titled the Uniform Facility Data Set (UFDS) in 1997 and 1998. Data from these years along with N-SSATS 2000 and  N-SSATS 2002 to N-SSATS 2011 are included in this concatenated dataset.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-1997-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -81777,58 +81790,29 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment.  Data are collected on topics including facility operation, services offered (assessment and pre-treatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.  N-SSATS was titled the Uniform Facility Data Set (UFDS) in 1997 and 1998. Data from these years along with N-SSATS 2000 and  N-SSATS 2002 to N-SSATS 2011 are included in this concatenated dataset.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-1997-2011)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-1997-2011) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-1997-2011-nid13597"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-1997-2011)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/icfy-anwh",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-11-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "743f9f04-4473-41e2-9da2-9a89db65ee55",
             "description": "The MLR Summary Reports provide plan-specific MLRs for Medicaid managed care programs. The MLR summary report data include MLRs for MCOs, PIHPs, and PAHPs submitted by states under 42 CFR \u00a7 438.74.",
-            "title": "MLR Summary Reports",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81837,71 +81821,72 @@
                     "title": "MLR Summary Reports"
                 }
             ],
+            "identifier": "743f9f04-4473-41e2-9da2-9a89db65ee55",
+            "issued": "2024-11-01",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/icfy-anwh",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "MLR Summary Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/office-refugee-resettlement-orr-overseas-refugee-arrival-data-fy-2000",
             "bureauCode": [
                 "001:05"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jennifer Schmalz",
+                "hasEmail": "mailto:jennifer.schmalz@acf.hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Office of Refugee Resettlement (ORR) Overseas Refugee Arrival Data FY 2000 sorted by country of origin and state of initial resettlement in the United States.</p>",
+            "identifier": "cf157d3d-72fa-4d8d-8f7c-4a0d0bc5e7b5",
             "issued": "2013-12-13",
-            "temporal": "2000-01-01T00:00:00-05:00/2000-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administration-for-children-and-families-department-of-health-human-services",
                 "administrative",
                 "population statistics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jennifer Schmalz",
-                "hasEmail": "mailto:jennifer.schmalz@acf.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/office-refugee-resettlement-orr-overseas-refugee-arrival-data-fy-2000",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "cf157d3d-72fa-4d8d-8f7c-4a0d0bc5e7b5",
-            "description": "<p>Office of Refugee Resettlement (ORR) Overseas Refugee Arrival Data FY 2000 sorted by country of origin and state of initial resettlement in the United States.</p>",
-            "title": "OFFICE OF REFUGEE RESETTLEMENT",
-            "programCode": [
-                "009:086"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "temporal": "2000-01-01T00:00:00-05:00/2000-01-01T00:00:00-05:00",
+            "title": "OFFICE OF REFUGEE RESETTLEMENT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Safety/MedWatch/SafetyInformation/SafetyAlertsforHumanMedicalProducts/default.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "definitions"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "2003711a-3d1c-4a0c-9928-09de5c42e2cf",
             "description": "MedWatch alerts provide timely new safety information on human drugs, medical devices, vaccines and other biologics, dietary supplements, and cosmetics. The alerts contain actionable information that may impact both treatment and diagnostic choices for healthcare professional and patient.",
-            "title": "MedWatch Safety Alerts for Human Medical Products",
-            "programCode": [
-                "009:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81909,45 +81894,36 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "2003711a-3d1c-4a0c-9928-09de5c42e2cf",
+            "issued": "2021-02-25",
+            "keyword": [
+                "definitions"
+            ],
+            "landingPage": "http://www.fda.gov/Safety/MedWatch/SafetyInformation/SafetyAlertsforHumanMedicalProducts/default.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "MedWatch Safety Alerts for Human Medical Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/office-based-physician-health-it-adoption-and-use",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/office-based-physician-electronic-health-record-adoption",
-                "https://www.healthit.gov/data/apps/office-based-physician-health-it-adoption"
-            ],
-            "keyword": [
-                "doctors",
-                "ehr adoption",
-                "health information technology",
-                "health it",
-                "interoperability",
-                "physicians"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ONC Request",
                 "hasEmail": "mailto:onc.request@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the National Coordinator for Health Information Technology"
-            },
-            "identifier": "9jlt3cvr-g3xs-9sva-n1js-xczfj9fxr7fh",
+            "describedBy": "https://www.healthit.gov/data/datasets/office-based-physician-health-it-adoption-and-use",
             "description": "Since 2008, the Centers for Disease Control and Prevention's National Center for Health Statistics has fielded a mail survey of office-based physicians, the National Electronic Health Records Survey (NEHRS). ONC helps fund this supplement to track office-based physician adoption and the use of EHRs for health information exchange and patient engagement. Starting in 2010, the NEHRS's sample size was increased to allow for state-level estimates. The data set estimates each measure nationally and individually for each state and the District of Columbia beginning in 2010, unless otherwise noted.",
-            "title": "Office-based Physician Health IT Adoption and Use",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81956,36 +81932,45 @@
                     "title": "nehrs.csv"
                 }
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/office-based-physician-health-it-adoption-and-use"
+            "identifier": "9jlt3cvr-g3xs-9sva-n1js-xczfj9fxr7fh",
+            "issued": "2023-10-03",
+            "keyword": [
+                "doctors",
+                "ehr adoption",
+                "health information technology",
+                "health it",
+                "interoperability",
+                "physicians"
+            ],
+            "landingPage": "https://www.healthit.gov/data/datasets/office-based-physician-health-it-adoption-and-use",
+            "modified": "2021-12-01",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "references": [
+                "https://www.healthit.gov/data/quickstats/office-based-physician-electronic-health-record-adoption",
+                "https://www.healthit.gov/data/apps/office-based-physician-health-it-adoption"
+            ],
+            "title": "Office-based Physician Health IT Adoption and Use"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135198.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "cder",
-                "clinical investigator"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "9dcfa54e-3b0c-40c8-b2fe-754820bed30f",
+            "describedBy": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/EnforcementActivitiesbyFDA/ucm073059.htm",
             "description": "The Clinical Investigator Inspection List (CLIIL) contains names, addresses, and other pertinent information gathered from inspections of clinical investigators who have performed studies with investigational new drugs. The list contains information on inspections that have been closed since July 1977.",
-            "title": "Clinical Investigator Inspector List (CLIIL)",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81993,19 +81978,47 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/EnforcementActivitiesbyFDA/ucm073059.htm",
+            "identifier": "9dcfa54e-3b0c-40c8-b2fe-754820bed30f",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "clinical investigator"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135198.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P3M"
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Clinical Investigator Inspector List (CLIIL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-iii-nys-1978",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>Youth data for the third wave of the National Youth Survey<br />\nare contained in this data collection, which includes data for youth<br />\ninterviewed in 1979 about events and behavior of the preceding year.<br />\nThe first wave of this study was conducted in 1976 and the<br />\nsecond wave in 1977. Data were collected on the<br />\ndemographic and socioeconomic status of respondents, disruptive events<br />\nin the home, youth aspirations, expectations for future goals, social<br />\nisolation, normlessness, labeling, perceived disapproval, attitudes<br />\ntoward deviance, exposure and commitment to delinquent peers, sex<br />\nroles, attitudes toward sexual assault, interpersonal violence,<br />\npressure for substance abuse by peers, exposure to substance abuse by<br />\nparents, self-reported delinquency, and drug and alcohol use.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Youth Survey US:  Wave III (NYS-1978) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "aspirations",
                 "behavior problems",
@@ -82037,45 +82050,43 @@
                 "young adults",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-iii-nys-1978",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537",
-            "description": "<p>Youth data for the third wave of the National Youth Survey<br />\nare contained in this data collection, which includes data for youth<br />\ninterviewed in 1979 about events and behavior of the preceding year.<br />\nThe first wave of this study was conducted in 1976 and the<br />\nsecond wave in 1977. Data were collected on the<br />\ndemographic and socioeconomic status of respondents, disruptive events<br />\nin the home, youth aspirations, expectations for future goals, social<br />\nisolation, normlessness, labeling, perceived disapproval, attitudes<br />\ntoward deviance, exposure and commitment to delinquent peers, sex<br />\nroles, attitudes toward sexual assault, interpersonal violence,<br />\npressure for substance abuse by peers, exposure to substance abuse by<br />\nparents, self-reported delinquency, and drug and alcohol use.This study has 1 Data Set.</p>",
-            "title": "National Youth Survey US:  Wave III (NYS-1978)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537",
-                    "description": "National Youth Survey US:  Wave III (NYS-1978) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iii-nys-1978-nid13537"
-                }
-            ]
+            "title": "National Youth Survey US:  Wave III (NYS-1978)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nsfg/index.htm",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
-            "issued": "2020-10-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2017/2019",
-            "modified": "2023-12-12",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-MainText-508.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nsfg@cdc.gov"
+            },
+            "describedBy": "Nationally representative sample of women and men in the household population ages 15-49",
+            "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
+                    "downloadURL": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+                    "mediaType": "text/html",
+                    "title": "National Survey of Family Growth 2017-2019 Public-Use Files"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ihtq-qs57",
+            "isPartOf": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+            "issued": "2020-10-20",
             "keyword": [
                 "births",
                 "cohabitation",
@@ -82098,121 +82109,87 @@
                 "sdoh-use-of-health-care",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:nsfg@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nsfg/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-12-12",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/ihtq-qs57",
-            "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
-            "title": "National Survey of Family Growth 2017-2019 Public-Use Files",
-            "isPartOf": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
-                    "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
-                    "@type": "dcat:Distribution",
-                    "title": "National Survey of Family Growth 2017-2019 Public-Use Files"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-MainText-508.pdf"
             ],
+            "rights": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
             "spatial": "US",
-            "describedBy": "Nationally representative sample of women and men in the household population ages 15-49",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Irregular",
+            "temporal": "2017/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Survey of Family Growth 2017-2019 Public-Use Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ie2e-2dst",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-07",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_featauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "5e2eb7ef-c735-5aa0-9e78-da25fa18ff2f",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_files_allDownloads",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20230426v2_ETL_DEV/files_allDownloads.csv",
-                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"featAuto\", \"update_id\": \"20230426v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"featAuto\", \"update_id\": \"20230426v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20230426v2_ETL_DEV/files_allDownloads.csv",
+                    "mediaType": "text/csv",
                     "title": "files_allDownloads csv file"
                 }
             ],
+            "identifier": "5e2eb7ef-c735-5aa0-9e78-da25fa18ff2f",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ie2e-2dst",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2023-06-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "featAuto_files_allDownloads"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/swv3-ghj7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "hepatitis",
-                "hepatitis (viral acute) type c",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/swv3-ghj7",
             "description": "NNDSS - Table II. Hepatitis (viral, acute) C - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n *Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Based on the CSTE Position Statement 15-ID-03: Revision of the Case Definition of Hepatitis C for National Notification, acute hepatitis C is now reported by case classification status.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute) C",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82235,38 +82212,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/swv3-ghj7",
+            "issued": "2018-01-04",
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
+            "landingPage": "https://data.cdc.gov/d/swv3-ghj7",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Hepatitis (viral, acute) C"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ifsn-wqrr",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-28",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "c657d635-87c6-4a2c-a098-7ccc85d22462",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-21-to-2023-08-27",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82275,39 +82260,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-21-to-2023-08-27"
                 }
             ],
+            "identifier": "c657d635-87c6-4a2c-a098-7ccc85d22462",
+            "issued": "2023-08-29",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ifsn-wqrr",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-08-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-21-to-2023-08-27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/igis-mx5s",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-10-19",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-25",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "plan id crosswalk",
-                "py2023"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "46fdeb9e-921a-4141-a231-1bbe3dd14f61",
             "description": "The Plan ID Crosswalk PUF (CW-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The purpose of the CW-PUF is to map QHPs and SADPs offered through the Exchanges during the previous plan year to plans that will be offered through the Exchanges in the current plan year.",
-            "title": "Plan ID Crosswalk PUF \u2013 PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82315,46 +82297,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "46fdeb9e-921a-4141-a231-1bbe3dd14f61",
+            "issued": "2022-10-19",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan id crosswalk",
+                "py2023"
+            ],
+            "landingPage": "https://healthdata.gov/d/igis-mx5s",
+            "modified": "2022-10-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan ID Crosswalk PUF \u2013 PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mpx5-t7tu",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-03-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-12-29/2023-07-29",
-            "modified": "2025-01-30",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "death rate",
-                "deaths",
-                "hhs region",
-                "mortality",
-                "nchs",
-                "nvss",
-                "puerto rico",
-                "state",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mpx5-t7tu",
             "description": "This file contains COVID-19 death counts, death rates, and percent of total deaths by jurisdiction of residence. The data is grouped by different time periods including 3-month period, weekly, and total (cumulative since January 1, 2020). United States death counts and rates include the 50 states, plus the District of Columbia and New York City. New York state estimates exclude New York City. Puerto Rico is included in HHS Region 2 estimates.\n\nDeaths with confirmed or presumed COVID-19, coded to ICD\u201310 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.\n\nData during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.\n\nDeath counts should not be compared across states. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly. \n\nThe ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.\n\nRates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).\n\nRates are based on deaths occurring in the specified week/month and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly/monthly age-adjusted rates which have been adjusted to allow comparison with annual rates.  Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly/monthly) rate prevailed for a full year.\n\nSub-national death counts between 1-9 are suppressed in accordance with NCHS data confidentiality standards. Rates based on death counts less than 20 are suppressed in accordance with NCHS standards of reliability as specified in NCHS Data Presentation Standards for Proportions (available from: https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf.).",
-            "title": "Provisional COVID-19 death counts, rates, and percent of total deaths, by jurisdiction of residence",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82377,44 +82351,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/mpx5-t7tu",
+            "issued": "2023-03-31",
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
+            "landingPage": "https://data.cdc.gov/d/mpx5-t7tu",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2019-12-29/2023-07-29",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 death counts, rates, and percent of total deaths, by jurisdiction of residence"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "references": [
-                "http://www.accessdata.fda.gov/scripts/cder/dissolution/index.cfm"
-            ],
-            "keyword": [
-                "cder",
-                "dissolution"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "3f2b8dee-6c80-4230-8f8a-3f7c83920d42",
             "description": "For a drug product that does not have a dissolution test method in the United States Pharmacopeia (USP), the FDA Dissolution Methods Database provides information on dissolution methods presently recommended by the Division of Bioequivalence, Office of Generic Drugs.",
-            "title": "Dissolution Methods Database",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82422,19 +82403,64 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "3f2b8dee-6c80-4230-8f8a-3f7c83920d42",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "dissolution"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P3M"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.accessdata.fda.gov/scripts/cder/dissolution/index.cfm"
+            ],
+            "title": "Dissolution Methods Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Cumulative provisional counts of deaths sex, race/Hispanic origin, age group, and by select underlying causes of death. The dataset also includes provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death. Includes deaths that occurred between January 1, 2020 to July 4, 2020.",
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
+            "identifier": "https://data.cdc.gov/api/views/sf7h-sajc",
             "issued": "2020-08-04",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2020-07-04",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -82465,83 +82491,36 @@
                 "united states",
                 "weekly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/sf7h-sajc",
-            "description": "Cumulative provisional counts of deaths sex, race/Hispanic origin, age group, and by select underlying causes of death. The dataset also includes provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death. Includes deaths that occurred between January 1, 2020 to July 4, 2020.",
-            "title": "AH Cumulative Provisional Death Counts by Sex, Race, and Age from 1/1/2020 to 7/4/2020",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sf7h-sajc/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2020-01-01/2020-07-04",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Cumulative Provisional Death Counts by Sex, Race, and Age from 1/1/2020 to 7/4/2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/art/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-30",
-            "keyword": [
-                "art",
-                "assisted reproductive technology",
-                "clinic",
-                "fertility",
-                "infertility",
-                "services",
-                "success rates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ARTINFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4yy2-qa9v",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/4yy2-qa9v",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Summary dataset provides a full snapshot of clinic services and profile, patient characteristics, and ART success rates. It is worth noting that patient medical characteristics, such as age, diagnosis, and ovarian reserve, affect ART treatment\u2019s success. Comparison of success rates across clinics may not be meaningful because of differences in patient populations and ART treatment methods. The success rates displayed in this dataset do not reflect any one patient\u2019s chance of success. Patients should consult with a doctor to understand their chance of success based on their own characteristics.",
-            "title": "2020 Final Assisted Reproductive Technology (ART) Summary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82564,67 +82543,101 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/4yy2-qa9v",
+            "identifier": "https://data.cdc.gov/api/views/4yy2-qa9v",
+            "issued": "2023-07-18",
+            "keyword": [
+                "art",
+                "assisted reproductive technology",
+                "clinic",
+                "fertility",
+                "infertility",
+                "services",
+                "success rates"
+            ],
+            "landingPage": "https://www.cdc.gov/art/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Assisted Reproductive Technology (ART)"
-            ]
+            ],
+            "title": "2020 Final Assisted Reproductive Technology (ART) Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ij3a-jt2x",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "582424b1-9548-5ebe-9a0d-9e50031fbfaa",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "582424b1-9548-5ebe-9a0d-9e50031fbfaa",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ij3a-jt2x",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2005",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2005) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -82637,42 +82650,41 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2005",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2005)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2005) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2005-nid13588"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2005)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/namcs/hcc/aboutnamcs.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component has randomly selected a nationally representative sample of health centers that provide health care services to the public and have an electronic health record, or EHR, system. Eligible health centers include:  Federally Qualified Health Centers (FQHCs; section 330-funded) FQHC Look-alikes (FQHC\u2013LALs; not federally funded) Currently, Indian Health Service Centers are not eligible for the NAMCS Health Center Component.",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) is designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. NAMCS began in 1973 as a national probability sample survey of visits to nonfederally employed office-based physicians. NCHS conducted the survey annually through 1981, again in 1985, and annually through 2021 (collection of visit data from physicians was stopped during 2020\u20132021 due to the burden placed on respondents by the COVID-19 pandemic). In 2006, a separate sample of Community Health Centers (CHCs) was added to the survey; the CHC component samples visits to both physicians and advanced practice providers (nurse practitioners, PAs [physician assistants and physician associates], and certified nurse midwives). Starting in 2012, in addition to the traditional NAMCS file, a separate data file for CHCs including physicians and advanced practice providers has been released.\n\nIn 2021, the former CHC sample of NAMCS was redesigned and launched as the NAMCS Health Center (HC) Component, collecting visit data from HCs using electronic health records, or EHR, systems of the participating health centers. The NAMCS Health Center Component contains critical data about health centers and the care they provide.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Link to the Standard Application Process attached.",
+                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/g795-gzp9",
             "issued": "2023-08-25",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-2022",
-            "modified": "2024-03-05",
             "keyword": [
                 "advanced practice providers",
                 "electronic health records",
@@ -82688,73 +82700,36 @@
                 "visit characteristics",
                 "visit data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/namcs/hcc/aboutnamcs.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-03-05",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/g795-gzp9",
-            "description": "The National Ambulatory Medical Care Survey (NAMCS) is designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. NAMCS began in 1973 as a national probability sample survey of visits to nonfederally employed office-based physicians. NCHS conducted the survey annually through 1981, again in 1985, and annually through 2021 (collection of visit data from physicians was stopped during 2020\u20132021 due to the burden placed on respondents by the COVID-19 pandemic). In 2006, a separate sample of Community Health Centers (CHCs) was added to the survey; the CHC component samples visits to both physicians and advanced practice providers (nurse practitioners, PAs [physician assistants and physician associates], and certified nurse midwives). Starting in 2012, in addition to the traditional NAMCS file, a separate data file for CHCs including physicians and advanced practice providers has been released.\n\nIn 2021, the former CHC sample of NAMCS was redesigned and launched as the NAMCS Health Center (HC) Component, collecting visit data from HCs using electronic health records, or EHR, systems of the participating health centers. The NAMCS Health Center Component contains critical data about health centers and the care they provide.",
-            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2021-2022, restricted data",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
-                    "mediaType": "text/html",
-                    "description": "Link to the Standard Application Process attached."
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component has randomly selected a nationally representative sample of health centers that provide health care services to the public and have an electronic health record, or EHR, system. Eligible health centers include:  Federally Qualified Health Centers (FQHCs; section 330-funded) FQHC Look-alikes (FQHC\u2013LALs; not federally funded) Currently, Indian Health Service Centers are not eligible for the NAMCS Health Center Component.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2021-2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2021-2022, restricted data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yakh-mjxn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "cryptosporidiosis",
-                "dengue",
-                "dengue virus infection",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "severe dengue",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yakh-mjxn",
             "description": "NNDSS - Table II. Cryptosporidiosis to Dengue - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Includes data for dengue and dengue-like illness.",
-            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82777,55 +82752,60 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yakh-mjxn",
+            "issued": "2018-01-04",
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
+            "landingPage": "https://data.cdc.gov/d/yakh-mjxn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pubmed.ncbi.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "data distribution",
-                "dataset",
-                "literature",
-                "pubmed"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bg8v-b9q4",
             "description": "PubMed is a free resource supporting the search and retrieval of biomedical and life sciences literature with the aim of improving health\u2013both globally and personally.\n\nThe PubMed database contains citations and abstracts of biomedical literature. It does not include full text journal articles; however, links to the full text are often present when available from other sources, such as the publisher's website or PubMed Central (PMC). \n\nSee the PubMed User Guide for more information. https://pubmed.ncbi.nlm.nih.gov/help/",
-            "title": "MEDLINE/PubMed Citations",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/",
-                    "description": "NLM produces a baseline set of MEDLINE/PubMed citation records in XML format for download on an annual basis. The annual baseline is released in December of each year. The best practice is to overwrite your local data with baseline data each year. MEDLINE/PubMed data conforms to the PubMed DTD. See our Data Elements documentation for more information. https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd",
                     "@type": "dcat:Distribution",
+                    "description": "NLM produces a baseline set of MEDLINE/PubMed citation records in XML format for download on an annual basis. The annual baseline is released in December of each year. The best practice is to overwrite your local data with baseline data each year. MEDLINE/PubMed data conforms to the PubMed DTD. See our Data Elements documentation for more information. https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/",
+                    "mediaType": "text/html",
                     "title": "Download - MEDLINE/PubMed - Annual Baseline"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/",
-                    "description": "Subsequent to the annual baseline release, NLM produces daily update files. These files include new, revised and deleted citations. If you are incorporating these files into a local database, load the baseline files first, then load the daily update files in numerical order. Revised or deleted citations should replace existing citations in your local database. More than one update file may become available on the same day. MEDLINE/PubMed data conforms to the PubMed DTD. See our Data Elements documentation for more information. https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd",
                     "@type": "dcat:Distribution",
+                    "description": "Subsequent to the annual baseline release, NLM produces daily update files. These files include new, revised and deleted citations. If you are incorporating these files into a local database, load the baseline files first, then load the daily update files in numerical order. Revised or deleted citations should replace existing citations in your local database. More than one update file may become available on the same day. MEDLINE/PubMed data conforms to the PubMed DTD. See our Data Elements documentation for more information. https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/",
+                    "mediaType": "text/html",
                     "title": "Download MEDLINE/PubMed - Daily Update Files"
                 },
                 {
@@ -82841,40 +82821,43 @@
                     "title": "PubMed Additional Resources"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bg8v-b9q4",
+            "issued": "2020-08-06",
+            "keyword": [
+                "api",
+                "data distribution",
+                "dataset",
+                "literature",
+                "pubmed"
+            ],
+            "landingPage": "https://pubmed.ncbi.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Literature"
-            ]
+            ],
+            "title": "MEDLINE/PubMed Citations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-05-22",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/brsb-akdp",
             "description": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years \n\n\u2022 Estimated COVID-19 vaccination coverage among Medicare fee-for-service beneficiaries >65 years is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19. (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html)\n\u2003",
-            "title": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82897,47 +82880,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/brsb-akdp",
+            "issued": "2024-02-14",
+            "keyword": [
+                "adults",
+                "covid-19 vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-05-22",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4zxn-f9dq",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-08-15",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "cases",
-                "coronavirus",
-                "covid-19",
-                "healthcare personnel",
-                "healthcare workers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4zxn-f9dq",
             "description": "Weekly cases among healthcare personnel, by week\n\n<b>Note:</b> Rows marked by \"missing date fields\" represent healthcare worker cases that were not associated with a date.",
-            "title": "COVID-19 Cases Among Healthcare Personnel, by week - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82960,51 +82941,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/4zxn-f9dq",
+            "issued": "2023-08-15",
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "healthcare personnel",
+                "healthcare workers"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4zxn-f9dq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "COVID-19 Cases Among Healthcare Personnel, by week - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-inpatient-hospital",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-06",
-            "references": [
-                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "national",
-                "original medicare",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/1e1beaba-9b41-47ca-960a-bd47b6ea65bd/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Inpatient Hospital tables provide use and payment data for all inpatient hospitals, including short-stay hospitals, critical access hospitals, long term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, religious nonmedical health care institutions, children\u2019s hospitals, and other hospitals.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR INPT HOSP 1. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR INPT HOSP 2. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR INPT HOSP 3. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR INPT HOSP 4. \u00a0All Medicare Inpatient Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Hospital\n\tMDCR INPT HOSP 5. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR INPT HOSP 6. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment\n\tMDCR INPT HOSP 7. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR INPT HOSP 8. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Type of Entitlement and Total Days of Care\n\tMDCR INPT HOSP 9. \u00a0Medicare IPPS Short Stay Hospitals: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Location and Bedsize of Hospitals, by Medical School Affiliation, and Type of Control\n\tMDCR INPT HOSP 10.\u00a0 Special-Category Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by\u00a0Type of Hospital",
-            "title": "CMS Program Statistics - Medicare Inpatient Hospital",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83061,54 +83037,53 @@
                     "title": "CMS Program Statistics - Medicare Inpatient Hospital : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/1e1beaba-9b41-47ca-960a-bd47b6ea65bd/data-viewer",
+            "issued": "2021-12-22",
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
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-inpatient-hospital",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-03-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
+            ],
+            "temporal": "2013-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS Program Statistics - Medicare Inpatient Hospital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8xkx-amqh",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-12-09",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13/2023-05-12",
-            "modified": "2023-05-12",
-            "references": [
-                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
-            ],
-            "keyword": [
-                "administration",
-                "age",
-                "coronavirus",
-                "covid-19",
-                "immunization",
-                "izdl",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:iisinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8xkx-amqh",
             "description": "Overall US COVID-19 Vaccine administration and vaccine equity data at county level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
-            "title": "COVID-19 Vaccinations in the United States,County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83131,184 +83106,178 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/8xkx-amqh",
+            "issued": "2022-12-09",
+            "keyword": [
+                "administration",
+                "age",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8xkx-amqh",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2023-05-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13/2023-05-12",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "COVID-19 Vaccinations in the United States,County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/rm6c-ns6x",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-08",
-            "keyword": [
-                "books",
-                "data distribution",
-                "literature",
-                "reference"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rm6c-ns6x",
             "description": "NLM produces bibliographic records for books, journals and other materials from NLM's collections in NLMXML, MARCXML and MARC 21 formats. These records can be searched at NLM LocatorPlus or the NLM Catalog.",
-            "title": "Catalog Record Data",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catpluslease",
-                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
                     "@type": "dcat:Distribution",
+                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catpluslease",
+                    "mediaType": "application/xml",
                     "title": "Download Catalog Record Data - CatfilePlus"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfileplus",
-                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
                     "@type": "dcat:Distribution",
+                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfileplus",
+                    "mediaType": "text/html",
                     "title": "Download Catalog Record Data - CatfilePlus"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catplusbase",
-                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
                     "@type": "dcat:Distribution",
+                    "description": "CatfilePlus includes cataloging records created by NLM in all formats and all monograph and monograph chapter records created by contributing collaborative partners in the fields of history of medicine, health technology assessment, space, bioethics, and population studies.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catplusbase",
+                    "mediaType": "text/html",
                     "title": "Download Catalog Record Data - CatfilePlus"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfilelease",
-                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
                     "@type": "dcat:Distribution",
+                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfilelease",
+                    "mediaType": "application/xml",
                     "title": "Download Catalog Record Data - Serfile"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfile",
-                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
                     "@type": "dcat:Distribution",
+                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfile",
+                    "mediaType": "text/html",
                     "title": "Download Catalog Record Data - Serfile"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfilebase",
-                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
                     "@type": "dcat:Distribution",
+                    "description": "Serfile contains all fully cataloged serial bibliographic records in the NLM database.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/serfilebase",
+                    "mediaType": "text/html",
                     "title": "Download Catalog Record Data - Serfile"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfile",
-                    "description": "Catfile contains fully cataloged bibliographic records in all formats.\n\n",
                     "@type": "dcat:Distribution",
+                    "description": "Catfile contains fully cataloged bibliographic records in all formats.\n\n",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfile",
+                    "mediaType": "text/html",
                     "title": "Download Catalog Record Data - Catfile"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfilebase",
-                    "description": "Catfile contains fully cataloged bibliographic records in all formats.\n\n",
                     "@type": "dcat:Distribution",
+                    "description": "Catfile contains fully cataloged bibliographic records in all formats.\n\n",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/catfilebase",
+                    "mediaType": "text/html",
                     "title": "Download Catalog Record Data - Catfile"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://support.nlm.nih.gov/knowledgebase/article/KA-04188/en-us",
-                    "description": "MARC data are available from NLM's Z39.50 endpoint.",
                     "@type": "dcat:Distribution",
+                    "description": "MARC data are available from NLM's Z39.50 endpoint.",
+                    "downloadURL": "https://support.nlm.nih.gov/knowledgebase/article/KA-04188/en-us",
+                    "mediaType": "text/html",
                     "title": "Catalog Record Data API via Z39.50 Endpoint"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/NBK25501/",
-                    "description": "NLM Catalog Record Data are available from the Entrez Programming Utilities.",
                     "@type": "dcat:Distribution",
+                    "description": "NLM Catalog Record Data are available from the Entrez Programming Utilities.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/NBK25501/",
+                    "mediaType": "text/html",
                     "title": "Catalog Record DataAPI via Entrez Programming Utilities"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nlm.nih.gov/databases/dtd/nlmcatalogrecordset_200101.dtd",
-                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
                     "@type": "dcat:Distribution",
+                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
+                    "downloadURL": "https://www.nlm.nih.gov/databases/dtd/nlmcatalogrecordset_200101.dtd",
+                    "mediaType": "text/html",
                     "title": "Documentation - Data Element Documentation and DTDs"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nlm.nih.gov/databases/dtd/nlmserials_200101.dtd",
-                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
                     "@type": "dcat:Distribution",
+                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
+                    "downloadURL": "https://www.nlm.nih.gov/databases/dtd/nlmserials_200101.dtd",
+                    "mediaType": "text/html",
                     "title": "Documentation - Data Element Documentation and DTDs"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nlm.nih.gov/bsd/licensee/catrecordxml_element_desc2.html",
-                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
                     "@type": "dcat:Distribution",
+                    "description": "Data Element Documentation as well as DTDs for the NLM Catalog Record Set and NLM Serials.",
+                    "downloadURL": "https://www.nlm.nih.gov/bsd/licensee/catrecordxml_element_desc2.html",
+                    "mediaType": "text/html",
                     "title": "Documentation - Data Element Documentation and DTDs"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rm6c-ns6x",
+            "issued": "2020-09-23",
+            "keyword": [
+                "books",
+                "data distribution",
+                "literature",
+                "reference"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/rm6c-ns6x",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-08",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Research"
-            ]
+            ],
+            "title": "Catalog Record Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-23",
-            "temporal": "1988/2018",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-11",
-            "keyword": [
-                "adults",
-                "black or african american",
-                "body mass index",
-                "body weight",
-                "chronic conditions",
-                "health risk factors",
-                "health us",
-                "hispanic or latino",
-                "men",
-                "mexican",
-                "obesity",
-                "older persons",
-                "overweight",
-                "poverty",
-                "white",
-                "women"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/sqt4-6a3k",
             "description": "Data on overweight and obesity among adults aged 20 and over in the United States, by selected characteristics, including sex, age, race, Hispanic origin, and poverty level. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Normal weight, overweight, and obesity among adults aged 20 and over, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83331,39 +83300,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/sqt4-6a3k",
+            "issued": "2024-02-23",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1988/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Normal weight, overweight, and obesity among adults aged 20 and over, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/iq3g-u3cv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-02-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-07",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "3fcf8272-a6ca-49a4-96aa-ef0d72563984",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-02-to-2023-01-08",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83372,76 +83357,76 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-02-to-2023-01-08"
                 }
             ],
+            "identifier": "3fcf8272-a6ca-49a4-96aa-ef0d72563984",
+            "issued": "2023-02-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/iq3g-u3cv",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-02-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-02-to-2023-01-08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-mental-health-services-survey-n-mhss-2010-0",
-            "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "mental health",
-                "mental health services",
-                "treatment facilities",
-                "treatment programs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
                 "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Substance Abuse & Mental Health Services Administration"
-            },
-            "identifier": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561",
             "description": "<p>The National Mental Health Services Survey (N-MHSS) is an annual survey designed to collect statistical information on the numbers and characteristics of all known mental health treatment facilities within the 50 States, the District of Columbia, and the U.S. territories. In every other year, beginning in 2014, the survey also collects statistical information on the numbers and demographic characteristics of persons served in these treatment facilities as of a specified survey reference date.<br />\nThe N-MHSS is the only source of national and State-level data on the mental health service delivery system reported by both publicly-operated and privately-operated specialty mental health treatment facilities, including: public psychiatric hospitals; private psychiatric hospitals, non-federal general hospitals with separate psychiatric units; U.S. Department of Veterans Affairs medical centers; residential treatment centers for children; residential treatment centers for adults; outpatient or day treatment or partial hospitalization mental health facilities; and multi-setting (non-hospital) mental health facilities.</p>\n<p>The N-MHSS complements the information collected through SAMHSA's survey of substance abuse treatment facilities, the National Survey of Substance Abuse Treatment Services (N-SSATS). Treatment facility Information from the N-MHSS is used to populate the mental health component of SAMHSA's online Behavioral Health Treatment Services Locator. <a href=\"http://findtreatment.samhsa.gov/This\">http://findtreatment.samhsa.gov/This</a> study has 1 Data Set.</p>",
-            "title": "National Mental Health Services Survey (N-MHSS-2010)",
-            "programCode": [
-                "009:030"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561",
-                    "description": "National Mental Health Services Survey (N-MHSS-2010) \n",
                     "@type": "dcat:Distribution",
+                    "description": "National Mental Health Services Survey (N-MHSS-2010) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561",
+                    "mediaType": "text/html",
                     "title": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561"
                 }
-            ]
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-mental-health-services-survey-n-mhss-2010-nid13561",
+            "issued": "2016-05-23",
+            "keyword": [
+                "mental health",
+                "mental health services",
+                "treatment facilities",
+                "treatment programs"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-mental-health-services-survey-n-mhss-2010-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "title": "National Mental Health Services Survey (N-MHSS-2010)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/iqcf-c2jg",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-12-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-19",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "ae0d720a-eafc-44dc-88ab-65da83917ec2",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-11-to-2023-12-17",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83450,41 +83435,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-11-to-2023-12-17"
                 }
             ],
+            "identifier": "ae0d720a-eafc-44dc-88ab-65da83917ec2",
+            "issued": "2023-12-20",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/iqcf-c2jg",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-12-19",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-11-to-2023-12-17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rksx-33p3",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2021-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-03",
-            "keyword": [
-                "cares act",
-                "coronavirus",
-                "covid-19",
-                "health system",
-                "provider relief fund",
-                "uninsured"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HRSA Chief Data Officer",
                 "hasEmail": "mailto:PRFdata@hrsa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rksx-33p3",
             "description": "The COVID-19 Claims Reimbursement to Health Care Providers and Facilities for Testing, Treatment, and Vaccine Administration for the Uninsured Program provides reimbursements on a rolling basis directly to eligible health care entities for claims that are attributed to the testing, treatment, and or vaccine administration of COVID-19 for uninsured individuals. The program funding information is as follow:\n\nTESTING\nThe American Rescue Plan Act (ARP) which provided $4.8 billion to reimburse providers for testing the uninsured; the Families First Coronavirus Response Act (FFCRA) Relief Fund, which includes funds received from the Public Health and Social Services Emergency Fund, as appropriated in the FFCRCA (P.L. 116-127) and the Paycheck Protection Program and Health Care Enhancement Act (P.L. 116-139) (PPPHCEA), which each appropriated $1 billion to reimburse health care entities for conducting COVID-19 testing for the uninsured.\n \nTREATMENT & VACCINATION\nThe Provider Relief Fund, which includes funds received from the Public Health and Social Services Emergency Fund, as appropriated in the Coronavirus Aid, Relief, and Economic Security (CARES) Act (P.L. 116-136), provided $100 billion in relief funds. The PPPHCEA appropriated an additional $75 billion in relief funds and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act (P.L. 116-260) appropriated another $3 billion. Within the Provider Relief Fund, a portion of the funding from these sources will be used to support healthcare-related expenses attributable to the treatment of uninsured individuals with COVID-19 and vaccination of uninsured individuals. To learn more about the program, visit: https://www.hrsa.gov/CovidUninsuredClaim\n\nThis dataset represents the list of health care entities who have agreed to the Terms and Conditions and received claims reimbursement for COVID-19 testing of uninsured individuals, vaccine administration and treatment for uninsured individuals with a COVID-19 diagnosis.\n\nFor Provider Relief Fund Data - https://data.cdc.gov/Administrative/HHS-Provider-Relief-Fund/kh8y-3es6",
-            "title": "Claims Reimbursement to Health Care Providers and Facilities for Testing, Treatment, and Vaccine Administration  of the Uninsured",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83507,42 +83487,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/rksx-33p3",
+            "issued": "2021-07-29",
+            "keyword": [
+                "cares act",
+                "coronavirus",
+                "covid-19",
+                "health system",
+                "provider relief fund",
+                "uninsured"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rksx-33p3",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2022-03-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "Claims Reimbursement to Health Care Providers and Facilities for Testing, Treatment, and Vaccine Administration  of the Uninsured"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/isn2-adwk",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-04-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-11",
-            "keyword": [
-                "cms-64 expenditures",
-                "financial management report",
-                "national totals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "4011579c-33ea-5741-a763-a2558d635561",
             "description": "This dataset reports summary state-by-state total expenditures by program for the Medicaid Program, Medicaid Administration and CHIP programs.  These state expenditures are tracked through the automated Medicaid Budget and Expenditure System/State Children's Health Insurance Program Budget and Expenditure System (MBES/CBES).\r\n\r\nFor more information, visit https://medicaid.gov/medicaid/finance/state-expenditure-reporting/expenditure-reports/index.html.",
-            "title": "Medicaid Financial Management Data \u2013 National Totals",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83551,42 +83534,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "4011579c-33ea-5741-a763-a2558d635561",
+            "issued": "2018-04-10",
+            "keyword": [
+                "cms-64 expenditures",
+                "financial management report",
+                "national totals"
+            ],
+            "landingPage": "https://healthdata.gov/d/isn2-adwk",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-12-11",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Medicaid Financial Management Data \u2013 National Totals"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ispy-gjtf",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "plan id crosswalk",
-                "py2024"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "0fa89e4e-e206-4b3d-bde5-c4d9246255c5",
             "description": "The Plan ID Crosswalk PUF (CW-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The purpose of the CW-PUF is to map QHPs and SADPs offered through the Exchanges during the previous plan year to plans that will be offered through the Exchanges in the current plan year.",
-            "title": "Plan ID Crosswalk PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83594,32 +83576,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "0fa89e4e-e206-4b3d-bde5-c4d9246255c5",
+            "issued": "2023-10-16",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan id crosswalk",
+                "py2024"
+            ],
+            "landingPage": "https://healthdata.gov/d/ispy-gjtf",
+            "modified": "2023-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan ID Crosswalk PUF - PY2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5avu-ff58",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-12",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-11",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5avu-ff58",
             "description": "NNDSS - Table II. Tuberculosis - 2019.  This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying WONDER data. Data on United States will exclude counts from US territories. \nFootnote: C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable. -: No reported cases. N: Not reportable. NN: Not Nationally Notifiable Cum: Cumulative year-to-date counts. Min: Minimum. Max: Maximum. \n* Case counts for reporting year 2018 and 2019 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf \n\u2020 Data for TB are displayed quarterly.",
-            "title": "NNDSS - Table II. Tuberculosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83642,38 +83629,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5avu-ff58",
+            "issued": "2019-04-12",
+            "landingPage": "https://data.cdc.gov/d/5avu-ff58",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-10-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Tuberculosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "keyword": [
-                "cdrh"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "4a439dda-f8d4-4461-ba4c-082abab102d4",
             "description": "This database provides descriptions of radiation-emitting products that have been recalled under an approved corrective action plan to remove defective and noncompliant products from the market. Searches may be done by manufacturer name, performance standard, product name, description, or date range.",
-            "title": "Radiation Emitting Product Corrective Actions and Recalls",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83681,17 +83665,46 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "4a439dda-f8d4-4461-ba4c-082abab102d4",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Radiation Emitting Product Corrective Actions and Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/uniform-facility-data-set-us-ufds-1997",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Uniform Facility Data Set (UFDS), formerly the National Drug and Alcohol Treatment Unit Survey or NDATUS, was designed to measure the scope and use of drug abuse treatment services in the United States. The survey collects information from each privately- and publicly-funded facility in the country that provides substance abuse treatment as well as from state-identified facilities that provide other substance abuse services. Data are collected on a number of topics including facility operation, services provided (assessment, therapy, testing, health, continuing care, programs for special groups, transitional services, community outreach, ancillary), type of treatment, facility capacity, numbers of clients, and various client characteristics. The main objective of the UFDS is to produce data that can be used to assess the nature and extent of substance abuse treatment services, to assist in the forecast of treatment resource requirements, to analyze treatment service trends, to conduct national, regional, and state-level comparative analyses of treatment services and utilization, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its on-line equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.  Additionally, the UFDS provides information that can be used to design sampling frames for other surveys of substance abuse treatment facilities.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Uniform Facility Data Set US (UFDS-1997) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -83704,72 +83717,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Substance Abuse & Mental Health Services Administration"
-            },
-            "identifier": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557",
-            "description": "<p>The Uniform Facility Data Set (UFDS), formerly the National Drug and Alcohol Treatment Unit Survey or NDATUS, was designed to measure the scope and use of drug abuse treatment services in the United States. The survey collects information from each privately- and publicly-funded facility in the country that provides substance abuse treatment as well as from state-identified facilities that provide other substance abuse services. Data are collected on a number of topics including facility operation, services provided (assessment, therapy, testing, health, continuing care, programs for special groups, transitional services, community outreach, ancillary), type of treatment, facility capacity, numbers of clients, and various client characteristics. The main objective of the UFDS is to produce data that can be used to assess the nature and extent of substance abuse treatment services, to assist in the forecast of treatment resource requirements, to analyze treatment service trends, to conduct national, regional, and state-level comparative analyses of treatment services and utilization, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its on-line equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.  Additionally, the UFDS provides information that can be used to design sampling frames for other surveys of substance abuse treatment facilities.This study has 1 Data Set.</p>",
-            "title": "Uniform Facility Data Set US (UFDS-1997)",
+            "landingPage": "https://healthdata.gov/dataset/uniform-facility-data-set-us-ufds-1997",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:030"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557",
-                    "description": "Uniform Facility Data Set US (UFDS-1997) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/uniform-facility-data-set-us-ufds-1997-nid13557"
-                }
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "title": "Uniform Facility Data Set US (UFDS-1997)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
-            ],
-            "keyword": [
-                "callers",
-                "cessation",
-                "intervention",
-                "national quitline data warehouse",
-                "nqdw",
-                "office on smoking and health",
-                "osh",
-                "quit",
-                "quitline",
-                "quit-now",
-                "services",
-                "state system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSHData Support",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vtt8-av2v",
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Hours-Of-Operation-And/vtt8-av2v",
             "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
-            "title": "Quitline \u2013 Services Available \u2013 Hours Of Operation And Available Languages - 2010 To Present",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83792,43 +83763,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Hours-Of-Operation-And/vtt8-av2v",
+            "identifier": "https://data.cdc.gov/api/views/vtt8-av2v",
+            "issued": "2023-07-18",
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
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
+            ],
             "theme": [
                 "Quitline"
-            ]
+            ],
+            "title": "Quitline \u2013 Services Available \u2013 Hours Of Operation And Available Languages - 2010 To Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/iuk7-b344",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "individual",
-                "individual market medical",
-                "py2025",
-                "qhp",
-                "qhp landscape instructions"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "d7865dc4-7c70-4bee-9e88-eaf6d4c7da28",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2025 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83836,43 +83817,38 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "d7865dc4-7c70-4bee-9e88-eaf6d4c7da28",
+            "issued": "2024-12-10",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2025",
+                "qhp",
+                "qhp landscape instructions"
+            ],
+            "landingPage": "https://healthdata.gov/d/iuk7-b344",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2025 Individual Medical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/w46e-8kr3",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "arboviral diseases",
-                "jamestown canyon virus disease",
-                "la crosse virus disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "powassan virus disease",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/w46e-8kr3",
             "description": "NNDSS - TABLE 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease \u2013 2021.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83895,53 +83871,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w46e-8kr3",
+            "issued": "2021-01-21",
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
+            "landingPage": "https://data.cdc.gov/d/w46e-8kr3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-outpatient-hospitals/medicare-outpatient-hospitals-by-provider-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2015-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-outpatient-hospitals-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospitals & facilities",
-                "medicare",
-                "original medicare",
-                "outpatient facilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicare Provider Data - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/ccbc9a44-40d4-46b4-a709-5caa59212e50/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-outpatient-hospitals-by-provider-and-service-data-dictionary",
             "description": "The Medicare Outpatient Hospitals by Provider and Service dataset provides information on services for Original Medicare Part B beneficiaries by OPPS hospitals. These datasets contain information on the number of services, payments, and submitted charges organized by provider CMS Certified Number (CCN) and comprehensive Ambulatory Payment Classification (APC).",
-            "title": "Medicare Outpatient Hospitals - by Provider and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ccbc9a44-40d4-46b4-a709-5caa59212e50/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ccbc9a44-40d4-46b4-a709-5caa59212e50/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Outpatient Hospitals - by Provider and Service : 2022-12-01"
                 },
                 {
@@ -84041,96 +84019,99 @@
                     "title": "Medicare Outpatient Hospitals - by Provider and Service : 2015-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-outpatient-hospitals-by-provider-and-service-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ccbc9a44-40d4-46b4-a709-5caa59212e50/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "outpatient facilities"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-outpatient-hospitals/medicare-outpatient-hospitals-by-provider-and-service",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-outpatient-hospitals-methodology"
+            ],
+            "temporal": "2015-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Outpatient Hospitals - by Provider and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/iwbk-66ew",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_devauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "5e020af5-c00c-5055-8aaa-3c2f11ba3cfe",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_briefType",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/briefType.csv",
-                    "description": "{\"dataset\": \"briefType\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/briefType.csv",
+                    "mediaType": "text/csv",
                     "title": "briefType csv file"
                 }
             ],
+            "identifier": "5e020af5-c00c-5055-8aaa-3c2f11ba3cfe",
+            "issued": "2024-07-17",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/iwbk-66ew",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "devAuto_briefType"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "nis-acm",
-                "older adults",
-                "rsv",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mx2d-yjrk",
             "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Demographic Characteristics \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023.  (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "title": "Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine by Demographic Characteristics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84153,65 +84134,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/mx2d-yjrk",
+            "issued": "2023-11-07",
+            "keyword": [
+                "nis-acm",
+                "older adults",
+                "rsv",
+                "vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-08-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine by Demographic Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/prams/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
-            "references": [
-                "https://www.cdc.gov/prams/index.htm",
-                "https://www.cdc.gov/prams/pramstat/index.html"
-            ],
-            "keyword": [
-                "abuse",
-                "alcohol use",
-                "breastfeeding",
-                "contraception",
-                "infant health",
-                "medicaid",
-                "mental health",
-                "morbidity",
-                "obesity",
-                "preconception health",
-                "pregnancy history",
-                "prenatal care",
-                "reproductive health",
-                "sleep behavior",
-                "smoke exposure",
-                "stress",
-                "tobacco use",
-                "unintended pregnancy",
-                "wic"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DRH Public Inquiries",
                 "hasEmail": "mailto:PRAMSProposals@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qwpv-wpc8",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2009/qwpv-wpc8",
             "description": "2009. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2009",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84234,42 +84197,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2009/qwpv-wpc8",
+            "identifier": "https://data.cdc.gov/api/views/qwpv-wpc8",
+            "issued": "2023-07-18",
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
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
+            ],
             "theme": [
                 "Maternal & Child Health"
-            ]
+            ],
+            "title": "CDC PRAMStat Data for 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/aq5t-7aga",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2023-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "api",
-                "mesh",
-                "mesh 2023 update",
-                "terminologies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aq5t-7aga",
             "description": "<b>(Includes MeSH 2023 and 2024 changes)</b> The MeSH 2025 Update - Add Report lists new Descriptors and Supplementary Concept Records (SCRs) that have been added to MeSH for the upcoming new release.  It also includes terms that replace deleted terms, as well as new entry combinations (new precoordinated descriptor heading that replaces an existing descriptor/subheading combination).  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Add Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84292,40 +84273,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aq5t-7aga",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/aq5t-7aga",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-16",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Terminology"
-            ]
+            ],
+            "title": "MeSH 2025 Update - Add Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/gtr/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "genetics",
-                "genomics",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ggb5-vr2q",
             "description": "Genetic Testing Registry (GTR) is a free, centralized voluntary registry of comprehensive genetic test information covering clinical and research tests for Mendelian disorders and drug responses including multigenic, array-based, biochemical, cytogenetic, and molecular tests.",
-            "title": "Genetic Testing Registry (GTR)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84334,83 +84316,88 @@
                     "title": "Genetic Test Registry (GTR) Homepage"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ggb5-vr2q",
+            "issued": "2021-06-30",
+            "keyword": [
+                "genetics",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/gtr/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "Genetic Testing Registry (GTR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/iye8-2kz6",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-06",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_prodauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "5fe32037-4a6f-5c53-80e8-26414747c39c",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_files_topicSnapshot",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
-                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"prodAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"prodAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
+                    "mediaType": "text/csv",
                     "title": "files_topicSnapshot csv file"
                 }
             ],
+            "identifier": "5fe32037-4a6f-5c53-80e8-26414747c39c",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/iye8-2kz6",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2022-10-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "prodAuto_files_topicSnapshot"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/eg2p-49pd",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch (PERB), National Institute for Occupational Safety and Health (NIOSH) Health Effects Laboratory Division (HELD),",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/eg2p-49pd",
             "description": "Working with vibrating hand tools is associated with the development of hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms, finger blanching and changes in sensory function.  Vibration plays a major role in the development of the symptoms that are characteristic of HAVS, however, the hands and fingers of worker using tools are also exposed to pressure applied as the workers grip tools.  The pressure applied by gripping a tool might also affect blood flow and sensorineural function.  Therefore, this study examined the effects of applied pressure [2 and 4 newtons (N)] on peripheral vascular and sensorineural function using a characterized rat tail model.  The tails of rats were exposed to 0, 2 or 4N of applied force for 10 days.  Blood flow (laser doppler) and sensitivity of the tail to pressure (Randall-Selitto pressure test) was measured on days 1, 5 and 10 of the exposure.  The sensitivity of the tail nerves to electrical stimulation was measured on days 2 and 9.",
-            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84418,46 +84405,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/eg2p-49pd",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/eg2p-49pd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/q78n-cpzf",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2020",
-            "modified": "2023-04-24",
-            "keyword": [
-                "anxiety",
-                "covid-19",
-                "depression",
-                "missed healthcare",
-                "research-data-center",
-                "telemedicine"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/q78n-cpzf",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 1 is the first round of a three-round survey. The probability sample of RANDS during COVID-19 Round 1 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from June 9, 2020 to July 6, 2020. The RANDS during COVID-19 Round 1 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 1 during COVID-19 probability sampled Restricted File",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_1_technical_documentation.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 1 is the first round of a three-round survey. The probability sample of RANDS during COVID-19 Round 1 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from June 9, 2020 to July 6, 2020. The RANDS during COVID-19 Round 1 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84465,92 +84443,94 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_1_technical_documentation.pdf",
+            "identifier": "https://data.cdc.gov/api/views/q78n-cpzf",
+            "issued": "2022-06-15",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression",
+                "missed healthcare",
+                "research-data-center",
+                "telemedicine"
+            ],
+            "landingPage": "https://data.cdc.gov/d/q78n-cpzf",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 1 during COVID-19 probability sampled Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/iznq-47kj",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_devauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "a29cf229-575a-531a-adaa-cf3dbf77defd",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measure_allStates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates.csv",
-                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates csv file"
                 }
             ],
+            "identifier": "a29cf229-575a-531a-adaa-cf3dbf77defd",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/iznq-47kj",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "devAuto_measure_allStates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://mor.nlm.nih.gov/RxClass/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "classification",
-                "drugs",
-                "supplements",
-                "terminologies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4mcj-vnc6",
             "description": "The RxClass Browser is a web application for exploring and navigating through the class hierarchies to find the RxNorm drug members associated with each class.\n\nRxClass links drug classes of several drug sources including ATC, MeSH, NDF-RT and FDA/SPL to their RxNorm drug members (ingredients, precise ingredients and multiple ingredients).\n\nRxClass allows users to search by class name or identifier to find the RxNorm drug members or, conversely, search by RxNorm drug name or identifier to find the classes that the RxNorm drug is a member of.",
-            "title": "RxClass",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84565,49 +84545,43 @@
                     "title": "Search RxClass"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4mcj-vnc6",
+            "issued": "2016-09-06",
+            "keyword": [
+                "api",
+                "classification",
+                "drugs",
+                "supplements",
+                "terminologies"
+            ],
+            "landingPage": "https://mor.nlm.nih.gov/RxClass/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Drugs and Chemicals"
-            ]
+            ],
+            "title": "RxClass"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4bc2-bbpq",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-01-06/2024-02-17",
-            "modified": "2025-01-24",
-            "keyword": [
-                "coronavirus",
-                "covid19",
-                "deaths",
-                "influenza",
-                "mortality",
-                "nchs",
-                "nvss",
-                "respiratory-virus-response",
-                "rsv",
-                "united states",
-                "weekly"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4bc2-bbpq",
             "description": "This file contains the provisional percent of total deaths by week for COVID-19, Influenza, and Respiratory Syncytial Virus for deaths occurring among residents in the United States. Provisional data are based on non-final counts of deaths based on the flow of mortality data in National Vital Statistics System.",
-            "title": "Provisional Percent of Deaths for COVID-19, Influenza, and RSV",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84630,52 +84604,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/4bc2-bbpq",
+            "issued": "2024-11-08",
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
+            "landingPage": "https://data.cdc.gov/d/4bc2-bbpq",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2018-01-06/2024-02-17",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional Percent of Deaths for COVID-19, Influenza, and RSV"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-30",
-            "references": [
-                "https://chronicdata.cdc.gov/d/vtwh-8kxg"
-            ],
-            "keyword": [
-                "cigar",
-                "cigarette",
-                "combustibles",
-                "loose tobacco",
-                "non-combustibles",
-                "per capita",
-                "pipe tobacco",
-                "roll-your-own tobacco",
-                "smokeless",
-                "tobacco consumption"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSHData Support",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rnvb-cpxx",
+            "describedBy": "https://chronicdata.cdc.gov/Policy/Adult-Tobacco-Consumption-In-The-U-S-2000-Present/rnvb-cpxx",
             "description": "2000 to Present. Adult Tobacco Consumption in the U.S. This dataset highlights critical trends in adult total and per capita consumption of both combustible (cigarettes, little cigars, small cigars, pipe tobacco, roll-your-own tobacco) tobacco products and smokeless (chewing tobacco and snuff) tobacco from 2000 to present. To view the CDC MMWR report, please visit https://www.cdc.gov/mmwr/volumes/65/wr/mm6548a1.htm.",
-            "title": "Adult Tobacco Consumption In The U.S., 2000-Present",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84698,49 +84671,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Policy/Adult-Tobacco-Consumption-In-The-U-S-2000-Present/rnvb-cpxx",
+            "identifier": "https://data.cdc.gov/api/views/rnvb-cpxx",
+            "issued": "2018-10-24",
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
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2024-04-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/vtwh-8kxg"
+            ],
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "Adult Tobacco Consumption In The U.S., 2000-Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "references": [
-                "https://www.cdc.gov/breastfeeding/data/nis_data/index.htm"
-            ],
-            "keyword": [
-                "breastfed",
-                "breastfeeding",
-                "child",
-                "dnpao",
-                "infants",
-                "national immunization survey",
-                "nis",
-                "nutrition"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DNPAO Public Inquiries",
                 "hasEmail": "mailto:dnpaoinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8hxn-cvik",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-National-I/8hxn-cvik",
             "description": "This dataset includes breastfeeding data from the National Immunization Survey (NIS). This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding. For more information about breastfeeding and NIS visit https://www.cdc.gov/breastfeeding/data/nis_data/index.htm.",
-            "title": "Nutrition, Physical Activity, and Obesity - National Immunization Survey (Breastfeeding)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84763,42 +84738,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-National-I/8hxn-cvik",
+            "identifier": "https://data.cdc.gov/api/views/8hxn-cvik",
+            "issued": "2025-01-30",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/breastfeeding/data/nis_data/index.htm"
+            ],
             "theme": [
                 "Nutrition",
                 "Physical Activity",
                 "and Obesity"
-            ]
+            ],
+            "title": "Nutrition, Physical Activity, and Obesity - National Immunization Survey (Breastfeeding)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/hmd/ihm/index.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
-            "keyword": [
-                "history of medicine",
-                "images"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/62wp-7g64",
             "description": "Images from the History of Medicine (IHM) in NLM Digital Collections provides online access to images from the historical collections of the U.S. National Library of Medicine. IHM includes image files of a wide variety of visual media including fine art, photographs, engravings, and posters that illustrate the social and historical aspects of medicine dating from the 15th to 21st century.",
-            "title": "Images from the History of Medicine",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84807,49 +84790,46 @@
                     "title": "Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://collections.nlm.nih.gov/web_service.html",
-                    "description": "Images from the History of Medicine is accessible programmatically via the NLM Digital Collections web service.",
                     "@type": "dcat:Distribution",
+                    "description": "Images from the History of Medicine is accessible programmatically via the NLM Digital Collections web service.",
+                    "downloadURL": "https://collections.nlm.nih.gov/web_service.html",
+                    "mediaType": "text/html",
                     "title": "API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/62wp-7g64",
+            "issued": "2021-06-30",
+            "keyword": [
+                "history of medicine",
+                "images"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/hmd/ihm/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-24",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Images"
-            ]
+            ],
+            "title": "Images from the History of Medicine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://dailymed.nlm.nih.gov/dailymed/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "api",
-                "drug label",
-                "drugs",
-                "supplements",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n7e9-np3x",
             "description": "DailyMed provides health information providers and the public with a standard, comprehensive, up-to-date, look-up and download resource of medication content and labeling as found in medication package inserts, also known as Structured Product Labeling (SPL).",
-            "title": "DailyMed",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84870,47 +84850,42 @@
                     "title": "Access DailyMed API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n7e9-np3x",
+            "issued": "2012-05-30",
+            "keyword": [
+                "api",
+                "drug label",
+                "drugs",
+                "supplements",
+                "united states"
+            ],
+            "landingPage": "https://dailymed.nlm.nih.gov/dailymed/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Consumer Health"
-            ]
+            ],
+            "title": "DailyMed"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kikd-77zw",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "cryptosporidiosis",
-                "dengue",
-                "dengue virus infection",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "severe dengue",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kikd-77zw",
             "description": "NNDSS - Table II. Cryptosporidiosis to Dengue - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP:  Nationally notifiable but not published.  Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.   Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Includes data for dengue and dengue-like illness. Office of Management and Budget approval of the NNDSS Revision #0920-0728 on January 21, 2016, authorized CDC to receive data for these conditions. CDC is in the process of soliciting data for these conditions.",
-            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84933,45 +84908,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kikd-77zw",
+            "issued": "2017-01-05",
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
+            "landingPage": "https://data.cdc.gov/d/kikd-77zw",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cucp-zsht",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "ehrlichia ewingii infection",
-                "ehrlichiosis and anaplasmosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "undetermined",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cucp-zsht",
             "description": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84994,23 +84971,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cucp-zsht",
+            "issued": "2019-01-03",
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
+            "landingPage": "https://data.cdc.gov/d/cucp-zsht",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-01-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datatools.ahrq.gov/hcupnet",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "references": [
-                "https://datatools.ahrq.gov/hcupnet/glossary"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://datatools.ahrq.gov/hcupnet/methodology",
+            "description": "HCUPnet is an online data tool based on data from the Healthcare Cost and Utilization Project (HCUP).\n\nThe data tool provides healthcare statistics and information for hospital inpatient and emergency department settings, as well as population-based healthcare data on counties. Users are able to query HCUP data to access detailed or summary statistics on inpatient stays and emergency department visits by patient, hospital, and encounter characteristics. Users are also able to generate tables and graphs on national and regional statistics and trends for community hospitals in the United States.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://hcupnet.ahrq.gov/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
             ],
+            "identifier": "1f692757-76c2-47d0-a39f-2ac3c0ecbd66",
+            "issued": "2021-02-13",
             "keyword": [
                 "claims",
                 "community health",
@@ -85029,40 +85039,43 @@
                 "readmissions",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://datatools.ahrq.gov/hcupnet",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "1f692757-76c2-47d0-a39f-2ac3c0ecbd66",
-            "description": "HCUPnet is an online data tool based on data from the Healthcare Cost and Utilization Project (HCUP).\n\nThe data tool provides healthcare statistics and information for hospital inpatient and emergency department settings, as well as population-based healthcare data on counties. Users are able to query HCUP data to access detailed or summary statistics on inpatient stays and emergency department visits by patient, hospital, and encounter characteristics. Users are also able to generate tables and graphs on national and regional statistics and trends for community hospitals in the United States.",
-            "title": "HCUPnet",
-            "programCode": [
-                "009:072"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://hcupnet.ahrq.gov/",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
+            "references": [
+                "https://datatools.ahrq.gov/hcupnet/glossary"
             ],
-            "describedBy": "https://datatools.ahrq.gov/hcupnet/methodology"
+            "title": "HCUPnet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2005",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2005) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -85075,151 +85088,125 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2005",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2005)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2005) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2005-nid13556"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2005)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/j5g5-dyyq",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_implauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "a66fa666-3854-5bc3-b8f8-9367a10cb40f",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_measure_allStates_downloadLink",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates_downloadLink.csv",
-                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates_downloadLink.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates_downloadLink csv file"
                 }
             ],
+            "identifier": "a66fa666-3854-5bc3-b8f8-9367a10cb40f",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/j5g5-dyyq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "implAuto_measure_allStates_downloadLink"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/j62p-6uef",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_implauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "90b4f584-cdf9-5d81-a106-f1781f8ba706",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_topicArea_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/topicArea_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/topicArea_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "topicArea_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "90b4f584-cdf9-5d81-a106-f1781f8ba706",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/j62p-6uef",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "implAuto_topicArea_measureDisplayGroups"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yu68-juzt",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Safety Research, Protective Technology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yu68-juzt",
             "description": "The accommodation of worker anthropometric variability in the workplace and personal protective equipment (PPE) is key to safe and efficient completion of work tasks. Previously, the best data available was 46 years old, which has largely become outdated due to demographic changes. These data tables consist of 34 traditional semi-nude body dimensions without gear (e.g., chest depth, standing; foot breadth, horizontal, standing; hip circumference; stature; elbow rest height, sitting; and eye height, sitting) and 15 dimension measurements over clothing and with gear (e.g., abdominal extension depth, sitting; hip breadth, sitting; and should-grip length, sitting) of 756 male and 218 female Law Enforcement Officers (LEOs). For many LEOs, patrol vehicles are the workplace where they spend significant portions of their workday and PPE is vital gear to safeguard LEOs from the harm of assaults. Design improvements of vehicle console space, vehicle ingress/egress, and LEO body-worn equipment can result in reduced LEO fatigue, pain, or injury.",
-            "title": "Anthropometry of Law Enforcement Officers",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85227,41 +85214,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yu68-juzt",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/yu68-juzt",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Anthropometry of Law Enforcement Officers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/j6tg-9r9f",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-03",
-            "references": [
-                "https://download.medicaid.gov/data/Keywords.csv"
-            ],
-            "keyword": [
-                "pharmacy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "0d425780-16be-4ded-8420-69def8f4ee29",
             "description": "Division of Pharmacy Releases Index dataset. The list of keywords for this dataset can be found in Additional information table below.",
-            "title": "Division of Pharmacy Releases Index dataset",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85269,47 +85251,47 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "0d425780-16be-4ded-8420-69def8f4ee29",
+            "issued": "2021-10-26",
+            "keyword": [
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/j6tg-9r9f",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-07-03",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://download.medicaid.gov/data/Keywords.csv"
+            ],
+            "title": "Division of Pharmacy Releases Index dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2018-01-01/2018-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "references": [
-                "https://data.cms.gov/resources/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes-methodology"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CLFS Inquires - CM",
                 "hasEmail": "mailto:CLFS_Inquiries@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/0e57f57d-0acc-4c9c-8f8c-973e3f4a3c4b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes-data-dictionary",
             "description": "The Medicare Clinical Laboratory Fee Schedule (CLFS) dataset provides raw data reported by any applicable laboratories that reported a volume greater than 10 tests for the data collection period. As described by the Protecting Access to Medicare Act, Applicable Laboratories must report to CMS private payor rates and associated volumes for laboratory tests on the Clinical Laboratory Fee Schedule.",
-            "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0e57f57d-0acc-4c9c-8f8c-973e3f4a3c4b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0e57f57d-0acc-4c9c-8f8c-973e3f4a3c4b/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes : 2018-12-31"
                 },
                 {
@@ -85325,53 +85307,46 @@
                     "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes : 2018-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/0e57f57d-0acc-4c9c-8f8c-973e3f4a3c4b/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-01-05",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-clinical-laboratory-fee-schedule-private-payer-rates-and-volumes-methodology"
+            ],
+            "temporal": "2018-01-01/2018-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Clinical Laboratory Fee Schedule Private Payer Rates and Volumes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wgyw-mswy",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "acute",
-                "by type) a",
-                "by type) b",
-                "hemolytic uremic syndrome post-diarrheal",
-                "hepatitis (viral",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wgyw-mswy",
             "description": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85394,45 +85369,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wgyw-mswy",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/wgyw-mswy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mv87-mh7a",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "nedss",
-                "netss",
-                "nndss",
-                "smallpox",
-                "spotted fever rickettsiosis confirmed",
-                "spotted fever rickettsiosis probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mv87-mh7a",
             "description": "NNDSS - TABLE 1GG.  Spotted fever rickettsiosis, Confirmed to Smallpox - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85455,71 +85432,78 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mv87-mh7a",
+            "issued": "2019-04-23",
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
+            "landingPage": "https://data.cdc.gov/d/mv87-mh7a",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://rgd.mcw.edu/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LUO, JAMES",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "c6c39d59-80c6-4ed8-a97e-09752c52f9f6",
+            "dataQuality": true,
             "description": "<p>The Rat Genome Database (RGD) is a collaborative effort between leading research institutions involved in rat genetic and genomic research to collect, consolidate, and integrate data generated from ongoing rat genetic and genomic research efforts and make these data widely available to the scientific community.</p>",
-            "title": "Rat Genome Database (RGD)",
+            "identifier": "c6c39d59-80c6-4ed8-a97e-09752c52f9f6",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://rgd.mcw.edu/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:003"
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Rat Genome Database (RGD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/krkm-t59m",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2015-11-17",
-            "keyword": [
-                "malaria"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Gimnig",
                 "hasEmail": "mailto:hzg1@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/krkm-t59m",
             "description": "This data set is from 3 surveys conducted in two districts in western Kenya following the scale up of insecticide treated nets and the implementation of IRS in one of the districts.",
-            "title": "PONE-D-15-23803",
-            "programCode": [
-                "009:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85542,35 +85526,36 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/krkm-t59m",
+            "issued": "2015-11-17",
+            "keyword": [
+                "malaria"
+            ],
+            "landingPage": "https://data.cdc.gov/d/krkm-t59m",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-11-17",
+            "programCode": [
+                "009:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "PONE-D-15-23803"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/j83z-us86",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-02",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-01",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "7dd8dbcf-53ca-43eb-a423-003026e24972",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-24-to-2023-07-30",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85579,76 +85564,68 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-24-to-2023-07-30"
                 }
             ],
+            "identifier": "7dd8dbcf-53ca-43eb-a423-003026e24972",
+            "issued": "2023-08-02",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/j83z-us86",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-08-01",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-24-to-2023-07-30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/genbank/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mizrachi, Ilene",
                 "hasEmail": "mailto:mizrachi@ncbi.nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "810d7c33-6139-4976-884f-b2c3cdb1c8e3",
+            "dataQuality": true,
             "description": "<p>GenBank is the NIH genetic sequence database, an annotated collection of all publicly available DNA sequences. GenBank is designed to provide and encourage access within the scientific community to the most up to date and comprehensive DNA sequence information.</p>",
-            "title": "GenBank",
+            "identifier": "810d7c33-6139-4976-884f-b2c3cdb1c8e3",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/genbank/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:041"
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "GenBank"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5pe9-px25",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "anaplasma phagocytophilum infection",
-                "ehrlichia chaffeensis infection",
-                "ehrlichiosis and anaplasmosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5pe9-px25",
             "description": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85671,38 +85648,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5pe9-px25",
+            "issued": "2019-01-03",
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
+            "landingPage": "https://data.cdc.gov/d/5pe9-px25",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-01-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/j8fd-jyui",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "695e7a86-00c1-49b1-935a-6fef6cbf5835",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-17-to-2023-07-23",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85711,18 +85696,46 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-17-to-2023-07-23"
                 }
             ],
+            "identifier": "695e7a86-00c1-49b1-935a-6fef6cbf5835",
+            "issued": "2023-07-27",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/j8fd-jyui",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-17-to-2023-07-23"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2007",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2007) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -85735,59 +85748,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2007",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2007)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2007) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2007-nid13547"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2007)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6nbv-ifib",
             "bureauCode": [
                 "009:032"
             ],
-            "issued": "2018-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
-            "keyword": [
-                "drought",
-                "environmental health"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:nephtrackingsupport@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6nbv-ifib",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes monthly Standardized Precipitation Evapotranspiration Index (SPEI)  data from 1895-2016 provided by the Cooperative Institute for Climate and Satellites - North Carolina. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate drought measures. Learn more about drought on the Tracking Network's website: https://ephtracking.cdc.gov/showDroughtLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Standardized Precipitation Evapotranspiration Index, 1895-2016",
-            "programCode": [
-                "009:20"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85810,98 +85793,96 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6nbv-ifib",
+            "issued": "2018-07-26",
+            "keyword": [
+                "drought",
+                "environmental health"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6nbv-ifib",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-11-27",
+            "programCode": [
+                "009:20"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Standardized Precipitation Evapotranspiration Index, 1895-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/j9pn-7wwd",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_prodauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "cd577ff7-f5a3-599d-9fc9-102d5e220d7c",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_tafVersion",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/tafVersion.csv",
-                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/tafVersion.csv",
+                    "mediaType": "text/csv",
                     "title": "tafVersion csv file"
                 }
             ],
+            "identifier": "cd577ff7-f5a3-599d-9fc9-102d5e220d7c",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/j9pn-7wwd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "prodAuto_tafVersion"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-compliance/fee-for-service-error-rate-improper-payment/medicare-fee-for-service-comprehensive-error-rate-testing",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2011-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-03",
-            "references": [
-                "https://data.cms.gov/resources/medicare-fee-for-service-comprehensive-error-rate-testing-improper-payment-data-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "medicare",
-                "original medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Comprehensive Error Rate Testing (CERT) Program - OFM",
                 "hasEmail": "mailto:CERT@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6395b458-2f89-4828-8c1a-e1e16b723d48/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-fee-for-service-comprehensive-error-rate-testing-improper-payment-data-dictionary",
             "description": "The Medicare Fee-for-Service (FFS) Comprehensive Error Rate Testing (CERT) dataset provides information on a random sample of FFS claims to determine if they were paid properly under Medicare coverage, coding, and payment rules. The dataset contains information on type of FFS claim, Diagnosis Related Group (DRG) and Healthcare Common Procedure Coding System (HCPCS) codes, provider type, type of bill, review decision, and error code.\n\n\u00a0\n\nPlease note, each reporting year (RY) contains claims submitted July 1 two years before the report\u00a0through June 30 one year before the report. For example, the 2024 data contains claims submitted July 1, 2022 through June 30, 2023.",
-            "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6395b458-2f89-4828-8c1a-e1e16b723d48/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6395b458-2f89-4828-8c1a-e1e16b723d48/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2024-01-01"
                 },
                 {
@@ -86073,58 +86054,48 @@
                     "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing : 2011-02-13"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-fee-for-service-comprehensive-error-rate-testing-improper-payment-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6395b458-2f89-4828-8c1a-e1e16b723d48/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/provider-compliance/fee-for-service-error-rate-improper-payment/medicare-fee-for-service-comprehensive-error-rate-testing",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-12-03",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-fee-for-service-comprehensive-error-rate-testing-improper-payment-data-methodology"
+            ],
+            "temporal": "2011-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Fee-for-Service Comprehensive Error Rate Testing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "public",
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1933/2018",
-            "modified": "2022-03-29",
-            "references": [
-                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
-                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
-                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
-                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
-            ],
-            "keyword": [
-                "births",
-                "maternal age",
-                "nchs",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:births@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/isx2-c2ii",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes percent distribution of births for females by age group in the United States since 1933.\n\nThe number of states in the reporting area differ historically. In 1915 (when the birth registration area was established), 10 states and the District of Columbia reported births; by 1933, 48 states and the District of Columbia were reporting births, with the last two states, Alaska and Hawaii, added to the registration area in 1959 and 1960, when these regions gained statehood. Reporting area information is detailed in references 1 and 2 below. Trend lines for 1909\u20131958 are based on live births adjusted for under-registration; beginning with 1959, trend lines are based on registered live births.",
-            "title": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
-            "isPartOf": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86147,43 +86118,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/isx2-c2ii",
+            "isPartOf": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "births",
+                "maternal age",
+                "nchs",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
+                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
+                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
+            ],
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1933/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Percent Distribution of Births for Females by Age Group: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "keyword": [
-                "cdrh"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "650b8214-c3a4-46f6-8a10-5d182339c0d6",
             "description": "The CDRH FOIA electronic reading room contains frequently requested information via the Freedom of Information Act from the Center for Devices and Radiological Health.",
-            "title": "CDRH FOIA Electronic Reading Room",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86191,41 +86175,36 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "650b8214-c3a4-46f6-8a10-5d182339c0d6",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "CDRH FOIA Electronic Reading Room"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "covid-19 vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "vsd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/eanj-9nie",
             "description": "Weekly COVID-19 Vaccination Coverage of Adults18 Years and Older by Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM)(https://www.cdc.gov/nis/about/index.html). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
-            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324, Overall, by Jurisdiction Among Adults 18 Years",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86248,51 +86227,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/eanj-9nie",
+            "issued": "2024-09-26",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324, Overall, by Jurisdiction Among Adults 18 Years"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-10-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-04",
-            "references": [
-                "https://www.census.gov/programs-surveys/acs/data.html",
-                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
-            ],
-            "keyword": [
-                "acs",
-                "estimates",
-                "place",
-                "places",
-                "sdoh"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/edkk-ze78",
             "description": "This dataset contains place-level (incorporated and census-designated places) social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service: https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
-            "title": "SDOH Measures for Place, ACS 2017-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86315,56 +86291,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/edkk-ze78",
+            "issued": "2023-10-26",
+            "keyword": [
+                "acs",
+                "estimates",
+                "place",
+                "places",
+                "sdoh"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-12-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.census.gov/programs-surveys/acs/data.html",
+                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "SDOH Measures for Place, ACS 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/home-infusion-therapy-providers",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-18",
-            "temporal": "2023-05-07/2025-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "references": [
-                "https://data.cms.gov/resources/home-infusion-therapy-providers-methodology"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "outpatient facilities",
-                "outpatient physical therapy",
-                "provider enrollment",
-                "states & territories",
-                "zip code"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/home-infusion-therapy-providers-data-dictionary",
             "description": "The Home Infusion Therapy Providers dataset provides information on the Providers in Medicare who specialize in Home Infusion Therapy.",
-            "title": "Home Infusion Therapy Providers",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data",
+                    "mediaType": "text/html",
                     "title": "Home Infusion Therapy Providers : 2025-01-07"
                 },
                 {
@@ -86872,58 +86847,62 @@
                     "title": "Home Infusion Therapy Providers : 2023-05-25"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/home-infusion-therapy-providers-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data-viewer",
+            "issued": "2023-03-18",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/home-infusion-therapy-providers",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P2W",
+            "modified": "2025-01-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/home-infusion-therapy-providers-methodology"
+            ],
+            "temporal": "2023-05-07/2025-01-04",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Home Infusion Therapy Providers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/medicare-provider-and-supplier-taxonomy-crosswalk",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2021-07-01/2025-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "references": [
-                "https://data.cms.gov/resources/medicare-provider-and-supplier-taxonomy-crosswalk-methodology"
-            ],
-            "keyword": [
-                "medical suppliers & equipment",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "provider enrollment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/113eb0bc-0c9a-4d91-9f93-3f6b28c0bf6b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-provider-and-supplier-taxonomy-crosswalk-data-dictionary",
             "description": "The Medicare Provider and Supplier Taxonomy Crosswalk dataset lists the providers and suppliers eligible to enroll in Medicare programs with the proper healthcare provider taxonomy code. This data includes the Medicare speciality codes, if available, provider/supplier type description, taxonomy code, and the taxonomy description.",
-            "title": "Medicare Provider and Supplier Taxonomy Crosswalk",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/113eb0bc-0c9a-4d91-9f93-3f6b28c0bf6b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/113eb0bc-0c9a-4d91-9f93-3f6b28c0bf6b/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2025-01-01"
                 },
                 {
@@ -87011,55 +86990,52 @@
                     "title": "Medicare Provider and Supplier Taxonomy Crosswalk : 2021-10-29"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-provider-and-supplier-taxonomy-crosswalk-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/113eb0bc-0c9a-4d91-9f93-3f6b28c0bf6b/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medical suppliers & equipment",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/medicare-provider-and-supplier-taxonomy-crosswalk",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P6M",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-provider-and-supplier-taxonomy-crosswalk-methodology"
+            ],
+            "temporal": "2021-07-01/2025-06-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Provider and Supplier Taxonomy Crosswalk"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-outpatient-facility",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-05-17",
-            "temporal": "2016-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-16",
-            "references": [
-                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
-                "national",
-                "outpatient facilities",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/bbcffb70-4b07-4a0b-a783-0722b89315b5/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics \u2013 Medicare Advantage, Outpatient Facility tables provide utilization data for outpatient facilities, by Medicare Advantage beneficiaries.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\nBelow is the list of tables:\n\n\n\tMDCR OUTPATIENT MA 1. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR OUTPATIENT MA 2. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR OUTPATIENT MA 3. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Area of Residence",
-            "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87098,26 +87074,55 @@
                     "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2016-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/bbcffb70-4b07-4a0b-a783-0722b89315b5/data-viewer",
+            "issued": "2024-05-17",
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
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-outpatient-facility",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
+            ],
+            "temporal": "2016-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/state-child-support-agencies-debt-compromise-policies",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis.Putze",
+                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Interactive Child Support Program Map - Click on State or Territory for more information regarding local policies to compromise child support debt owed to the state.</p>",
+            "identifier": "086ea269-2de3-4f89-b8c0-a517c9bacce2",
             "issued": "2014-02-10",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administrative",
                 "arrears management",
@@ -87131,111 +87136,82 @@
                 "promising practices",
                 "state local child support agencies"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dennis.Putze",
-                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/state-child-support-agencies-debt-compromise-policies",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:084"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "086ea269-2de3-4f89-b8c0-a517c9bacce2",
-            "description": "<p>Interactive Child Support Program Map - Click on State or Territory for more information regarding local policies to compromise child support debt owed to the state.</p>",
-            "title": "State Child Support Agencies With Debt Compromise Policies",
-            "programCode": [
-                "009:084"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "State Child Support Agencies With Debt Compromise Policies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jcq7-czbz",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_featauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "d8dc4c8b-3174-5aba-a777-f1ea0f4bdc7f",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_tafVersion",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/tafVersion.csv",
-                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/tafVersion.csv",
+                    "mediaType": "text/csv",
                     "title": "tafVersion csv file"
                 }
             ],
+            "identifier": "d8dc4c8b-3174-5aba-a777-f1ea0f4bdc7f",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/jcq7-czbz",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "featAuto_tafVersion"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "references": [
-                "https://academic.oup.com/aje/article/179/8/1025/109078",
-                "https://academic.oup.com/aje/article/182/2/127/93984",
-                "https://www.cdc.gov/pcd/issues/2017/pdf/17_0281.pdf",
-                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
-            ],
-            "keyword": [
-                "500 cities",
-                "census tracts",
-                "estimates",
-                "prevalence"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "500 Cities Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5mtz-k78d",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-level-Data-GIS-Friendly-Fo/5mtz-k78d",
             "description": "2014, 2013. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census tract-level data in GIS-friendly format can be joined with census tract spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-Boundaries/x7zy-2xmx) in a geographic information system (GIS) to produce maps of 27 measures at the census tract level.",
-            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2016 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87258,22 +87234,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-level-Data-GIS-Friendly-Fo/5mtz-k78d",
+            "identifier": "https://data.cdc.gov/api/views/5mtz-k78d",
+            "issued": "2023-07-18",
+            "keyword": [
+                "500 cities",
+                "census tracts",
+                "estimates",
+                "prevalence"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://academic.oup.com/aje/article/179/8/1025/109078",
+                "https://academic.oup.com/aje/article/182/2/127/93984",
+                "https://www.cdc.gov/pcd/issues/2017/pdf/17_0281.pdf",
+                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2016 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/youth-risk-behavior-surveillance-system-yrbss",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "YRBSS",
+                "hasEmail": "mailto:yrbss@cdc.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Youth Risk Behavior Surveillance System (YRBSS) monitors 6 types of health-risk behaviors that contribute to the leading causes of death and disability among youth and adults, including: behaviors that contribute to unintentional injuries and violence; sexual behaviors that contribute to unintended pregnancy and sexually transmitted diseases (STDs), including HIV infection; alcohol and other drug use; tobacco use; unhealthy dietary behaviors; inadequate physical activity. YRBSS also measures the prevalence of obesity and asthma among youth and young adults. YRBSS includes a national school-based survey conducted by CDC and state, territorial, tribal, and local surveys conducted by state, territorial, and local education and health agencies and tribal governments.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/healthyyouth/yrbs/cdcreports.htm",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "identifier": "83a48652-f4c3-4d9c-8f04-3e59b6a50878",
             "issued": "2013-05-01",
-            "temporal": "1991-01-01T00:00:00-05:00/1991-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "children's health",
                 "epidemiology",
@@ -87285,71 +87297,35 @@
                 "survey",
                 "youth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "YRBSS",
-                "hasEmail": "mailto:yrbss@cdc.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/youth-risk-behavior-surveillance-system-yrbss",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "83a48652-f4c3-4d9c-8f04-3e59b6a50878",
-            "description": "<p>The Youth Risk Behavior Surveillance System (YRBSS) monitors 6 types of health-risk behaviors that contribute to the leading causes of death and disability among youth and adults, including: behaviors that contribute to unintentional injuries and violence; sexual behaviors that contribute to unintended pregnancy and sexually transmitted diseases (STDs), including HIV infection; alcohol and other drug use; tobacco use; unhealthy dietary behaviors; inadequate physical activity. YRBSS also measures the prevalence of obesity and asthma among youth and young adults. YRBSS includes a national school-based survey conducted by CDC and state, territorial, tribal, and local surveys conducted by state, territorial, and local education and health agencies and tribal governments.</p>",
-            "title": "Youth Risk Behavior Surveillance System (YRBSS)",
-            "programCode": [
-                "009:027"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cdc.gov/healthyyouth/yrbs/cdcreports.htm",
-                    "mediaType": "text/html",
-                    "title": "Text "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1991-01-01T00:00:00-05:00/1991-01-01T00:00:00-05:00",
             "theme": [
                 "Health",
                 "National"
-            ]
+            ],
+            "title": "Youth Risk Behavior Surveillance System (YRBSS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/w54d-atna",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "brucellosis",
-                "campylobacteriosis",
-                "candida auris",
-                "clinical",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/w54d-atna",
             "description": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Candida auris, clinical colonization/screening cases are not included in this table. These data are available on the Mycotic Diseases Branch's Tracking Candida auris page (https://www.cdc.gov/fungal/candida-auris/tracking-c-auris.html).",
-            "title": "NNDSS - TABLE 1F. Brucellosis to Candida auris, clinical",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87372,20 +87348,57 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w54d-atna",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/w54d-atna",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1F. Brucellosis to Candida auris, clinical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This file includes data from the 2002 through 2011 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across one or more of the pair years, i.e., 2002-2003, 2004-2005, 2006-2007, 2008-2009, 2010-2011, or 2012-2013.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health: 2-Year R-DAS (NSDUH-2002-2003) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -87426,55 +87439,29 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533",
-            "description": "<p>This file includes data from the 2002 through 2011 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across one or more of the pair years, i.e., 2002-2003, 2004-2005, 2006-2007, 2008-2009, 2010-2011, or 2012-2013.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health: 2-Year R-DAS (NSDUH-2002-2003)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533",
-                    "description": "National Survey on Drug Use and Health: 2-Year R-DAS (NSDUH-2002-2003) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-2-year-r-das-nsduh-2002-2003-nid13533"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health: 2-Year R-DAS (NSDUH-2002-2003)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4rd8-s7gn",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Allergy and Clinical Immunology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4rd8-s7gn",
             "description": "Understanding the host response to influenza A virus (IAV) infection is vital for developing intervention strategies. The primary barriers for invading respiratory pathogens are the airway epithelial cells of the respiratory tract and antimicrobial peptides produced by these cells. The antimicrobial peptide, \u03b2-defensin-1, has antiviral activity against both enveloped and non-enveloped viruses. Significant downregulation of \u03b2-defensin1 gene (DEFB1) expression was observed when human bronchial epithelial cells (HBEpCs) were exposed to IAV. HBEpCs overexpressing DEFB1 caused a significant reduction in IAV, that was confirmed by IAV matrix gene analysis and confocal microscopy. DEFB1expression after transfection with hsa-miR-186-5p and hsa-miR-340-5p provided evidence that DEFB1 expression could be modulated by these two miRNAs and hsa-miR-186-5p had a higher binding efficiency with DEFB1. Overexpression of DEFB1 in IAV infected HBEpCs led to increased NF-kB expression.  In a Polymerase Chain Reaction (PCR) array analysis of 84 transcription factors, either overexpressing DEFB1 or siRNA silencing of DEFB1 expression significantly modulated the expression of STAT3.  In addition, Ingenuity Pathway Analysis (IPA) integrated with PCR array data showed that the JAK1/STAT3 pathway was significantly altered by cells overexpressing DEFB1, suggesting that this may be one of the pathways by which defensin regulates IAV replication in HBEpCs. In conclusion, the reduction in IAV copy number in DEFB1 overexpressing cells suggests that \u03b2-defensin-1 plays a key role in regulating IAV survival through STAT3 and is a potential target for antiviral drug development.",
-            "title": "\u03b2-defensin-1 regulates influenza virus infection in human bronchial epithelial cells through the STAT3 signaling pathway",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87482,21 +87469,47 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4rd8-s7gn",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/4rd8-s7gn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "\u03b2-defensin-1 regulates influenza virus infection in human bronchial epithelial cells through the STAT3 signaling pathway"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/departmental-appeals-board-decisions-0",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.hhs.gov/dab/decisions/dabdecisions/index.html",
+            "description": "<p>Decisions issued by the Chair and Board Members of the Departmental Appeals Board concerning determinations in discretionary, project grant programs, including disallowances, terminations and denials of refunding, cost allocation plan disapprovals, and rate determinations; determinations in mandatory grant programs, including disallowances of state claims under titles I, IV-A (Temporary Assistance for Needy Families), IV-D (Child Support Enforcement), IV-E (Foster Care and Adoption Assistance), X, XIV, XVI, XIX (Medicaid), and XXI (State Children's Health Insurance Program) of the Social Security Act; and appellate review of decisions of DAB Civil Remedies Division ALJs, decisions of Food and Drug Administration ALJs regarding civil money penalties, and decisions of Department of the Interior ALJs in Indian Health Service contract/compact cases.n.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "56e8ed0c-b29b-462e-aede-83b3e3c466a8",
             "issued": "2012-05-30",
-            "temporal": "1974-03-07T00:00:00-04:00/1974-03-07T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "abuse",
                 "acf",
@@ -87634,74 +87647,37 @@
                 "violation",
                 "withold"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/departmental-appeals-board-decisions-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "56e8ed0c-b29b-462e-aede-83b3e3c466a8",
-            "description": "<p>Decisions issued by the Chair and Board Members of the Departmental Appeals Board concerning determinations in discretionary, project grant programs, including disallowances, terminations and denials of refunding, cost allocation plan disapprovals, and rate determinations; determinations in mandatory grant programs, including disallowances of state claims under titles I, IV-A (Temporary Assistance for Needy Families), IV-D (Child Support Enforcement), IV-E (Foster Care and Adoption Assistance), X, XIV, XVI, XIX (Medicaid), and XXI (State Children's Health Insurance Program) of the Social Security Act; and appellate review of decisions of DAB Civil Remedies Division ALJs, decisions of Food and Drug Administration ALJs regarding civil money penalties, and decisions of Department of the Interior ALJs in Indian Health Service contract/compact cases.n.</p>",
-            "title": "Departmental Appeals Board Decisions",
-            "programCode": [
-                "009:072"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://www.hhs.gov/dab/decisions/dabdecisions/index.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1974-03-07T00:00:00-04:00/1974-03-07T00:00:00-04:00",
             "theme": [
                 "Community",
                 "Health",
                 "Medicare",
                 "Hospital"
-            ]
+            ],
+            "title": "Departmental Appeals Board Decisions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v4tm-h8pe",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-01",
-            "keyword": [
-                "antimicrobial resistance",
-                "carbapenem-resistant acinetobacter baumannii",
-                "carbapenem-resistant enterobacterales",
-                "enterobacter spp.",
-                "escherichia coli",
-                "haicviz",
-                "healthcare-associated infection",
-                "klebsiella spp.",
-                "surveillance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HAIC",
                 "hasEmail": "mailto:erib@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/v4tm-h8pe",
             "description": "<p>The healthcare-associated infection component of CDC\u2019s <a href=\"https://www.cdc.gov/ncezid/dpei/eip/index.html\" target=\"_blank\">EIP</a> engages a <a href=\"https://www.cdc.gov/ncezid/dpei/eip/eip-sites.html\" target=\"_blank\">network</a> of state health departments and their academic medical center partners to help answer critical questions about emerging HAI threats, advanced infection tracking methods, and antibiotic resistance in the United States. Information gathered through this activity will play a key role in shaping future policies and recommendations targeting HAI prevention. </p>",
-            "title": "HAICViz - MuGSI",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87724,43 +87700,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/v4tm-h8pe",
+            "issued": "2021-06-24",
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
+            "landingPage": "https://data.cdc.gov/d/v4tm-h8pe",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-06-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "HAICViz - MuGSI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7esm-uptm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-19",
-            "keyword": [
-                "122 cities",
-                "2015",
-                "death",
-                "influenza",
-                "mortality",
-                "pneumonia"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7esm-uptm",
             "description": "TABLE III. Deaths in 122 U.S. cities - 2015122 Cities Mortality Reporting System \ufffd\ufffd\ufffd Each week, the vital statistics offices of 122 cities across the United States report the total number of death certificates processed and the number of those for which pneumonia or influenza was listed as the underlying or contributing cause of death by age group (Under 28 days, 28 days \ufffd\ufffd\ufffd1 year, 1-14 years, 15-24 years, 25-44 years, 45-64 years, 65-74 years, 75-84 years, and \ufffd\ufffd\ufffd 85 years).FOOTNOTE:U: Unavailable      -: No reported cases * Mortality data in this table are voluntarily reported from 122 cities in the United States, most of which have populations of 100,000 or more. A death is reported by the place of its occurrence and by the week that the death certificate was filed. Fetal deaths are not included. ** Totals include unknown ages. *** Partial counts for this city.",
-            "title": "TABLE III. Deaths in 122 U.S. cities",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87783,42 +87762,40 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/7esm-uptm",
+            "issued": "2016-01-07",
+            "keyword": [
+                "122 cities",
+                "2015",
+                "death",
+                "influenza",
+                "mortality",
+                "pneumonia"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7esm-uptm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "TABLE III. Deaths in 122 U.S. cities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h3kf-bqpq",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
-                "chancroid",
-                "chlamydia trachomatis infection",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/h3kf-bqpq",
             "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87841,95 +87818,95 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h3kf-bqpq",
+            "issued": "2022-01-14",
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
+            "landingPage": "https://data.cdc.gov/d/h3kf-bqpq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/CMS-Medicare-Restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2014/2017",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare14_18_linked_data-list_of_variables.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 12) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-linkage-methodology.pdf",
+            "describedByType": "application/pdf",
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the\u00a0National Hospital Care Survey (NHCS)\u00a0by augmenting it with 2014-2018 administrative data from the Centers for Medicare & Medicaid Services\u2019 (CMS) Medicare program. Linkage of NHCS data with the CMS Medicare Data provides the opportunity to conduct a vast array of studies on health care utilization and expenditures among the elderly U.S. population and persons receiving Medicare disability benefits.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/42pu-ymxu",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-23",
             "keyword": [
                 "linked medicare data",
                 "nhcs",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/CMS-Medicare-Restricted.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/42pu-ymxu",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the\u00a0National Hospital Care Survey (NHCS)\u00a0by augmenting it with 2014-2018 administrative data from the Centers for Medicare & Medicaid Services\u2019 (CMS) Medicare program. Linkage of NHCS data with the CMS Medicare Data provides the opportunity to conduct a vast array of studies on health care utilization and expenditures among the elderly U.S. population and persons receiving Medicare disability benefits.",
-            "title": "National Hospital Care Survey (NHCS) linked to Centers for Medicare & Medicaid (CMS) 2014-2018 Medicare Data",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare14_18_linked_data-list_of_variables.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 12) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-linkage-methodology.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2014/2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey (NHCS) linked to Centers for Medicare & Medicaid (CMS) 2014-2018 Medicare Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fc5f-ixvg",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-07",
-            "keyword": [
-                "2019",
-                "arboviral diseases",
-                "babesiosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "west nile virus disease",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
```

