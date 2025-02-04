# Change History for epa.json (Part 23)

### Changes from 31606f9 to dd2190f (Part 13/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "As described in the README.md file, the GitHub repository EoL4Chem are Python scripts written to track chemical waste flows and identify recycling, energy recovery, treatment & disposal facilities (RETDFs) located across the United States of America, using publicly-available databases. EoL4Chem uses the U.S. Environmental Protection Agency (EPA)'s Chemical Data Reporting (CDR) to gather information about potential post-recycling scenarios for recycled chemicals (e.g., fuel or fuel agent). EoL4Chem integrates the PAU4Chem repository, which transforms data for performing chemical flow analysis for pollution abatement units (PAUs) or on-site end-of-life (EoL) operations (e.g., distillation). Also, EoL4Chem incorporates the physical properties (e.g., boiling point) from another repository that retrieves the properties using web scraping and automatization. These properties support chemical flow analysis performance.\nAlso, it describes the Python libraries required for running the code, how to use it, the obtained outputs files after running the Python script (all manuscript figures, e.g., file name Sankey_1.pdf\tis the Sankey diagram shown in Figure 4A), and the corresponding Disclaimer.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Gerardo Ruiz-Mercado",
+                "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
+            },
+            "description": "As described in the README.md file, the GitHub repository EoL4Chem are Python scripts written to track chemical waste flows and identify recycling, energy recovery, treatment & disposal facilities (RETDFs) located across the United States of America, using publicly-available databases. EoL4Chem uses the U.S. Environmental Protection Agency (EPA)'s Chemical Data Reporting (CDR) to gather information about potential post-recycling scenarios for recycled chemicals (e.g., fuel or fuel agent). EoL4Chem integrates the PAU4Chem repository, which transforms data for performing chemical flow analysis for pollution abatement units (PAUs) or on-site end-of-life (EoL) operations (e.g., distillation). Also, EoL4Chem incorporates the physical properties (e.g., boiling point) from another repository that retrieves the properties using web scraping and automatization. These properties support chemical flow analysis performance.\nAlso, it describes the Python libraries required for running the code, how to use it, the obtained outputs files after running the Python script (all manuscript figures, e.g., file name Sankey_1.pdf\tis the Sankey diagram shown in Figure 4A), and the corresponding Disclaimer.",
+            "distribution": [
+                {
+                    "accessURL": "https://github.com/gruizmer/EoL4Chem",
+                    "title": "https://github.com/gruizmer/EoL4Chem"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520621",
             "keyword": [
@@ -128350,18 +128353,11 @@
                 "chemical manufacturing",
                 "Life Cycle Environmental Assessment"
             ],
-            "contactPoint": {
-                "fn": "Gerardo Ruiz-Mercado",
-                "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://github.com/gruizmer/EoL4Chem",
-                    "accessURL": "https://github.com/gruizmer/EoL4Chem"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-30",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -128370,20 +128366,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Datasets for manuscript \"A data engineering approach for chemical flow analysis and circular economy\""
         },
         {
-            "title": "Bioavailability, Bioaccessibility and speciation data.",
-            "description": "Bioavailability, Bioaccessibility and speciation data. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Karen Bradham bradham.karen@epa.gov or Tyler Sowers sowers.tyler@epa.gov. Format: The data were generated using EPA and HUD samples.  All of the soil and dust samples were provided to CEMM for research and methods development based on the agreement that the specific sample identifiers would not be released.  The samples identifications for the HUD samples are considered PII and the EPA Regional soils samples are not identified because some of these locations may be in litigation.  ",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Karen Bradham",
+                "hasEmail": "mailto:bradham.karen@epa.gov"
+            },
+            "description": "Bioavailability, Bioaccessibility and speciation data. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Karen Bradham bradham.karen@epa.gov or Tyler Sowers sowers.tyler@epa.gov. Format: The data were generated using EPA and HUD samples.  All of the soil and dust samples were provided to CEMM for research and methods development based on the agreement that the specific sample identifiers would not be released.  The samples identifications for the HUD samples are considered PII and the EPA Regional soils samples are not identified because some of these locations may be in litigation.  ",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1519319",
             "keyword": [
                 "lead",
@@ -128391,13 +128389,11 @@
                 "bioavailability",
                 "Dust"
             ],
-            "contactPoint": {
-                "fn": "Karen Bradham",
-                "hasEmail": "mailto:bradham.karen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-01",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -128406,19 +128402,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Bioavailability, Bioaccessibility and speciation data."
         },
         {
-            "title": "Data used in Figures and Tables in this Research Effort",
-            "description": "The data set represents data collected during the pilot study. \n\nThis dataset is associated with the following publication:\nLytle, D., D. Williams, C. Muhlen, E. Riddick, and M. Pham. The Removal of Ammonia, Arsenic, Iron and Manganese by Biological Treatment from a Small Iowa Drinking Water System.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 6(11): 3142-3156, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Darren Lytle",
+                "hasEmail": "mailto:lytle.darren@epa.gov"
+            },
+            "description": "The data set represents data collected during the pilot study. \n\nThis dataset is associated with the following publication:\nLytle, D., D. Williams, C. Muhlen, E. Riddick, and M. Pham. The Removal of Ammonia, Arsenic, Iron and Manganese by Biological Treatment from a Small Iowa Drinking Water System.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 6(11): 3142-3156, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504163/Gilbert%20Iowa%20SKIDs%20Pilot%20_Science%20Hub%20data%20set.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Gilbert Iowa SKIDs Pilot _Science Hub data set.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504163",
             "keyword": [
@@ -128429,20 +128433,10 @@
                 "biological treatment",
                 "drinking water"
             ],
-            "contactPoint": {
-                "fn": "Darren Lytle",
-                "hasEmail": "mailto:lytle.darren@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Gilbert Iowa SKIDs Pilot _Science Hub data set.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504163/Gilbert%20Iowa%20SKIDs%20Pilot%20_Science%20Hub%20data%20set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-28",
-            "references": [
-                "https://doi.org/10.1039/d0ew00361a"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128452,91 +128446,91 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d0ew00361a"
+            ],
+            "rights": null,
+            "title": "Data used in Figures and Tables in this Research Effort"
         },
         {
-            "title": "Characterization results",
-            "description": "Characterization data set. \n\nThis dataset is associated with the following publication:\nAl-Anazi, A., W. Abdelraheem, K. Scheckel, M. Nadagouda, K. Shea, and D.D.  Dionysiou. Novel Franklinite-like Synthetic Zinc-Ferrite Redox Nanomaterial: synthesis and evaluation for Degradation of Diclofenac in Water.   APPLIED CATALYSIS B: ENVIRONMENTAL. Elsevier Science Ltd, New York, NY, USA, 275: 119098, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1506071",
-            "keyword": [
-                "Zinc ferrite",
-                "Diclofenac (DCF)",
-                "Advanced oxidation and reduction",
-                "reaction byproducts"
-            ],
             "contactPoint": {
                 "fn": "Mallikarjuna Nadagouda",
                 "hasEmail": "mailto:nadagouda.mallikarjuna@epa.gov"
             },
+            "description": "Characterization data set. \n\nThis dataset is associated with the following publication:\nAl-Anazi, A., W. Abdelraheem, K. Scheckel, M. Nadagouda, K. Shea, and D.D.  Dionysiou. Novel Franklinite-like Synthetic Zinc-Ferrite Redox Nanomaterial: synthesis and evaluation for Degradation of Diclofenac in Water.   APPLIED CATALYSIS B: ENVIRONMENTAL. Elsevier Science Ltd, New York, NY, USA, 275: 119098, (2020).",
             "distribution": [
                 {
-                    "title": "Copy of MALLIK.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Copy%20of%20MALLIK.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of MALLIK.xlsx"
                 },
                 {
-                    "title": "Manuscript-11-20-19.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Manuscript-11-20-19.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Manuscript-11-20-19.docx"
                 },
                 {
-                    "title": "Graphical Abstract-11-20-19.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Graphical%20Abstract-11-20-19.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Graphical Abstract-11-20-19.docx"
                 },
                 {
-                    "title": "Highlights.doc",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Highlights.doc",
-                    "mediaType": "application/msword"
+                    "mediaType": "application/msword",
+                    "title": "Highlights.doc"
                 },
                 {
-                    "title": "Supplementary Information.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Supplementary%20Information.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary Information.docx"
                 },
                 {
-                    "title": "Zn10.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Zn10.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Zn10.xls"
                 },
                 {
-                    "title": "Zn07.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Zn07.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Zn07.xls"
                 },
                 {
-                    "title": "Zn03star.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Zn03star.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Zn03star.xls"
                 },
                 {
-                    "title": "Zn03.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Zn03.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Zn03.xls"
                 },
                 {
-                    "title": "Zn01.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Zn01.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Zn01.xls"
                 },
                 {
-                    "title": "Zn 0.3 Star.XLS",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506071/Zn%200.3%20Star.XLS",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Zn 0.3 Star.XLS"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1506071",
+            "keyword": [
+                "Zinc ferrite",
+                "Diclofenac (DCF)",
+                "Advanced oxidation and reduction",
+                "reaction byproducts"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-19",
-            "references": [
-                "https://doi.org/10.1016/j.apcatb.2020.119098"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128546,70 +128540,70 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apcatb.2020.119098"
+            ],
+            "rights": null,
+            "title": "Characterization results"
         },
         {
-            "title": "Characterization Data-XPS-XRD",
-            "description": "Characterization data such as XRD and XPS. \n\nThis dataset is associated with the following publication:\nDesai, I., M. Nadagouda, M. Elovitz, M. Mills, and B. Boulanger. Synthesis and Characterization of Magnetic Manganese Ferrites.   Materials Science for Energy Technologies. Elsevier B.V., Amsterdam,  NETHERLANDS, 2(2): 150-160, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520718",
-            "keyword": [
-                ":  Synthesis",
-                "Magnetic particles",
-                "water treatment"
-            ],
             "contactPoint": {
                 "fn": "Mallikarjuna Nadagouda",
                 "hasEmail": "mailto:nadagouda.mallikarjuna@epa.gov"
             },
+            "description": "Characterization data such as XRD and XPS. \n\nThis dataset is associated with the following publication:\nDesai, I., M. Nadagouda, M. Elovitz, M. Mills, and B. Boulanger. Synthesis and Characterization of Magnetic Manganese Ferrites.   Materials Science for Energy Technologies. Elsevier B.V., Amsterdam,  NETHERLANDS, 2(2): 150-160, (2019).",
             "distribution": [
                 {
-                    "title": "XPS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520718/XPS.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "XPS.zip"
                 },
                 {
-                    "title": "20PVA.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520718/20PVA.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "20PVA.zip"
                 },
                 {
-                    "title": "15PVA.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520718/15PVA.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "15PVA.zip"
                 },
                 {
-                    "title": "10PVA.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520718/10PVA.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "10PVA.zip"
                 },
                 {
-                    "title": "3.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520718/3.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "3.zip"
                 },
                 {
-                    "title": "2.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520718/2.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "2.zip"
                 },
                 {
-                    "title": "1.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520718/1.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "1.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520718",
+            "keyword": [
+                ":  Synthesis",
+                "Magnetic particles",
+                "water treatment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-20",
-            "references": [
-                "https://doi.org/10.1016/j.mset.2019.01.009"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128619,42 +128613,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.mset.2019.01.009"
+            ],
+            "rights": null,
+            "title": "Characterization Data-XPS-XRD"
         },
         {
-            "title": "Dataset for ORD-033294: Mining a human transcriptome database for chemical modulators of NRF2",
-            "description": "Gene Expression Omnibus and ArrayExpress archived study numbers of microarray data used in the study. \n\nThis dataset is associated with the following publication:\nRooney, J., B. Chorley, S. Hiemstra, S. Wink, X. Wang, D. Bell, B. van de Water, and J. Corton. Mining a human transcriptome database for chemical modulators of Nrf2 (PLOS ONE).   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 15(9): e0239367, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504297",
-            "keyword": [
-                "Nrf2",
-                "oxidative stress",
-                "microarray",
-                "toxicogenomics",
-                "High throughput screening"
-            ],
             "contactPoint": {
                 "fn": "Jon Corton",
                 "hasEmail": "mailto:corton.chris@epa.gov"
             },
+            "description": "Gene Expression Omnibus and ArrayExpress archived study numbers of microarray data used in the study. \n\nThis dataset is associated with the following publication:\nRooney, J., B. Chorley, S. Hiemstra, S. Wink, X. Wang, D. Bell, B. van de Water, and J. Corton. Mining a human transcriptome database for chemical modulators of Nrf2 (PLOS ONE).   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 15(9): e0239367, (2020).",
             "distribution": [
                 {
-                    "title": "Data submission for A-83c0.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504297/Data%20submission%20for%20A-83c0.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-83c0.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504297",
+            "keyword": [
+                "Nrf2",
+                "oxidative stress",
+                "microarray",
+                "toxicogenomics",
+                "High throughput screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-10",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0239367"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128664,51 +128658,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0239367"
+            ],
+            "rights": null,
+            "title": "Dataset for ORD-033294: Mining a human transcriptome database for chemical modulators of NRF2"
         },
         {
-            "title": "R2PIER monitoring data",
-            "description": "These data include the 1-minute monitoring values at the R2PIER site, the daily averaged data supporting comparison of the R2PIER and nearby New Jersey Elizabeth Lab site, and the 5 minute shipping data. \n\nThis dataset is associated with the following publication:\nHagler, G., D. Birkett, R. Henry, and R. Peltier. Three years of high time-resolution air pollution monitoring in the complex multi-source harbor of New York and New Jersey.   AEROSOL AND AIR QUALITY RESEARCH. Chinese Association for Aerosol Research in Taiwan,   TAIWAN, PROVINCE OF CHINA, 21(2): NA, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1517799",
-            "keyword": [
-                "ports",
-                "near-source",
-                "air quality monitoring",
-                "Inverse Modeling"
-            ],
             "contactPoint": {
                 "fn": "Gayle Hagler",
                 "hasEmail": "mailto:hagler.gayle@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517799/documents/DataDictionary-README.txt",
+            "describedByType": "text/plain",
+            "description": "These data include the 1-minute monitoring values at the R2PIER site, the daily averaged data supporting comparison of the R2PIER and nearby New Jersey Elizabeth Lab site, and the 5 minute shipping data. \n\nThis dataset is associated with the following publication:\nHagler, G., D. Birkett, R. Henry, and R. Peltier. Three years of high time-resolution air pollution monitoring in the complex multi-source harbor of New York and New Jersey.   AEROSOL AND AIR QUALITY RESEARCH. Chinese Association for Aerosol Research in Taiwan,   TAIWAN, PROVINCE OF CHINA, 21(2): NA, (2020).",
             "distribution": [
                 {
-                    "title": "R2PIER-NJ-Comparison.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517799/R2PIER-NJ-Comparison.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "R2PIER-NJ-Comparison.csv"
                 },
                 {
-                    "title": "Shipping-data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517799/Shipping-data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Shipping-data.csv"
                 },
                 {
-                    "title": "R2PIER-1min-data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517799/R2PIER-1min-data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "R2PIER-1min-data.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517799",
+            "keyword": [
+                "ports",
+                "near-source",
+                "air quality monitoring",
+                "Inverse Modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-02-13",
-            "references": [
-                "https://doi.org/10.4209/aaqr.2020.02.0069"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128719,42 +128715,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517799/documents/DataDictionary-README.txt",
-            "describedByType": "text/plain"
+            "references": [
+                "https://doi.org/10.4209/aaqr.2020.02.0069"
+            ],
+            "rights": null,
+            "title": "R2PIER monitoring data"
         },
         {
-            "title": "Sarajevo PM2.5 Data from MetOne BAM-1020",
-            "description": "This is an hourly time series of PM2.5 concentration, temperature, and relative humidity measured by a MetOne BAM-1020 in Sarajevo, Bosnia and Herzegovina. \n\nThis dataset is associated with the following publication:\nHagler, G., T. Hanley, R. Vanderpool, B. Hassett-Sipple, M. Smith, J. Wilbur, T. Wilbur, T. Oliver, D. Shand, V. Vidacek, C. D'Angelo, and R. Allen. PM2.5 Temporal Trends and Instrument Performance Assessment Over 2018-2019 in Sarajevo, BiH Jan 2020. In Proceedings, UIPS Conference 2020, Sarajevo, NA, BOSNIA, 01/31/2021 - 01/31/2021. Association of Consulting Engineers Bosnia and Herzegovina, Sarajevo,  BOSNIA, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1518365",
-            "keyword": [
-                "pm2.5",
-                "Bosnia",
-                "Sarajevo",
-                "fine particles",
-                "FEM"
-            ],
             "contactPoint": {
                 "fn": "Gayle Hagler",
                 "hasEmail": "mailto:hagler.gayle@epa.gov"
             },
+            "description": "This is an hourly time series of PM2.5 concentration, temperature, and relative humidity measured by a MetOne BAM-1020 in Sarajevo, Bosnia and Herzegovina. \n\nThis dataset is associated with the following publication:\nHagler, G., T. Hanley, R. Vanderpool, B. Hassett-Sipple, M. Smith, J. Wilbur, T. Wilbur, T. Oliver, D. Shand, V. Vidacek, C. D'Angelo, and R. Allen. PM2.5 Temporal Trends and Instrument Performance Assessment Over 2018-2019 in Sarajevo, BiH Jan 2020. In Proceedings, UIPS Conference 2020, Sarajevo, NA, BOSNIA, 01/31/2021 - 01/31/2021. Association of Consulting Engineers Bosnia and Herzegovina, Sarajevo,  BOSNIA, (2020).",
             "distribution": [
                 {
-                    "title": "Sarajevo-confproc-data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518365/Sarajevo-confproc-data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Sarajevo-confproc-data.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518365",
+            "keyword": [
+                "pm2.5",
+                "Bosnia",
+                "Sarajevo",
+                "fine particles",
+                "FEM"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-14",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -128763,19 +128759,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Sarajevo PM2.5 Data from MetOne BAM-1020"
         },
         {
-            "title": "NRSA Data 2008,2009, 2013, 2014",
-            "description": "Rivers and Streams data for the National Aquatic Resource Surveys. \n\nThis dataset is associated with the following publication:\nHerlihy, A., J. Sifneos, R. Hughes, D. Peck, and R. Mitchell. The Relation of Lotic Fish and Benthic Macroinvertebrate Condition Indices to Environmental Factors Across the Conterminous USA.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 112: 105958, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Steven Paulsen",
+                "hasEmail": "mailto:paulsen.steve@epa.gov"
+            },
+            "description": "Rivers and Streams data for the National Aquatic Resource Surveys. \n\nThis dataset is associated with the following publication:\nHerlihy, A., J. Sifneos, R. Hughes, D. Peck, and R. Mitchell. The Relation of Lotic Fish and Benthic Macroinvertebrate Condition Indices to Environmental Factors Across the Conterminous USA.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 112: 105958, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504126",
             "keyword": [
@@ -128786,19 +128789,10 @@
                 "lakes and reservoirs",
                 "wetlands"
             ],
-            "contactPoint": {
-                "fn": "Steven Paulsen",
-                "hasEmail": "mailto:paulsen.steve@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2009-12-31",
-            "references": [
-                "https://doi.org/10.1016/j.ecolind.2019.105958"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128808,41 +128802,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolind.2019.105958"
+            ],
+            "rights": null,
+            "title": "NRSA Data 2008,2009, 2013, 2014"
         },
         {
-            "title": "Seepage Flux Article Data 8/7/2014 - 8/19/2014",
-            "description": "The dataset includes measurements of sediment temperature, along with local climate and hydrologic conditions, which can be used to assess performance of different one-dimensional models for estimating the magnitude and direction of seepage flux between groundwater and surface water.  The dataset includes continuous records of groundwater and surface water elevations, sediment temperature, and local climate data during the dates of 7 August 2014 through 19 August 2014.  Measurements of thermal conductivity for sediment cores in three locations within the monitored surface water body are also included. \n\nThis dataset is associated with the following publication:\nFord, R.G., B.K. Lien, S.D. Acree, and R.R. Ross. Spreadsheet Tools for Quantifying Seepage Flux Across the GW\u2010SW Interface.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 57(1): 01-11, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1520049",
-            "keyword": [
-                "seepage flux",
-                "sediment temperature",
-                "calculation tool",
-                "site characterization"
-            ],
             "contactPoint": {
                 "fn": "Robert Ford",
                 "hasEmail": "mailto:ford.robert@epa.gov"
             },
+            "description": "The dataset includes measurements of sediment temperature, along with local climate and hydrologic conditions, which can be used to assess performance of different one-dimensional models for estimating the magnitude and direction of seepage flux between groundwater and surface water.  The dataset includes continuous records of groundwater and surface water elevations, sediment temperature, and local climate data during the dates of 7 August 2014 through 19 August 2014.  Measurements of thermal conductivity for sediment cores in three locations within the monitored surface water body are also included. \n\nThis dataset is associated with the following publication:\nFord, R.G., B.K. Lien, S.D. Acree, and R.R. Ross. Spreadsheet Tools for Quantifying Seepage Flux Across the GW\u2010SW Interface.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 57(1): 01-11, (2021).",
             "distribution": [
                 {
-                    "title": "Seepage_Flux_Article_Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520049/Seepage_Flux_Article_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Seepage_Flux_Article_Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520049",
+            "keyword": [
+                "seepage flux",
+                "sediment temperature",
+                "calculation tool",
+                "site characterization"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-05-23",
-            "references": [
-                "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2019WR026232"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128852,56 +128846,56 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2019WR026232"
+            ],
+            "rights": null,
+            "title": "Seepage Flux Article Data 8/7/2014 - 8/19/2014"
         },
         {
-            "title": "Data for \"The contribution of wildland fire emissions to nitrogen and sulfur deposition in the contiguous U.S.: Implications for tree growth and survival in the Northwest\"",
-            "description": "Data files for Koplitz et al., \"The contribution of wildland emissions to deposition in the U.S.: implications for tree growth and survival in the Northwest\", Environmental Research Letters, in press, 2021, doi:10.1088/1748-9326/abd26e. \n\nThis dataset is associated with the following publication:\nKoplitz, S., C. Nolte, R. Sabo, C. Clark, K. Horn, R.Q. Thomas, and T. Newcomer-Johnson. The contribution of wildland fire emissions to deposition in the U S: implications for tree growth and survival in the Northwest.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 16(2): 024028, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1517565",
-            "keyword": [
-                "air quality",
-                "CMAQ",
-                "WRF",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christopher Nolte",
                 "hasEmail": "mailto:nolte.chris@epa.gov"
             },
+            "description": "Data files for Koplitz et al., \"The contribution of wildland emissions to deposition in the U.S.: implications for tree growth and survival in the Northwest\", Environmental Research Letters, in press, 2021, doi:10.1088/1748-9326/abd26e. \n\nThis dataset is associated with the following publication:\nKoplitz, S., C. Nolte, R. Sabo, C. Clark, K. Horn, R.Q. Thomas, and T. Newcomer-Johnson. The contribution of wildland fire emissions to deposition in the U S: implications for tree growth and survival in the Northwest.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 16(2): 024028, (2021).",
             "distribution": [
                 {
-                    "title": "FIA_data_stats_effects.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517565/FIA_data_stats_effects.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FIA_data_stats_effects.csv"
                 },
                 {
-                    "title": "FIA_data_full.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517565/FIA_data_full.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FIA_data_full.csv"
                 },
                 {
-                    "title": "deposition.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517565/deposition.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "deposition.csv"
                 },
                 {
-                    "title": "README.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517565/README.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "README.txt"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517565",
+            "keyword": [
+                "air quality",
+                "CMAQ",
+                "WRF",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-07",
-            "references": [
-                "https://doi.org/10.1088/1748-9326/abd26e"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128911,42 +128905,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1748-9326/abd26e"
+            ],
+            "rights": null,
+            "title": "Data for \"The contribution of wildland fire emissions to nitrogen and sulfur deposition in the contiguous U.S.: Implications for tree growth and survival in the Northwest\""
         },
         {
-            "title": "Fate of Cerium Dioxide Nanoparticles in Soil Monitored by Single Particle ICP-MS",
-            "description": "Data set is based on an analytical method for the extraction, detection, and characterization of engineered nanoparticles in the soil. \n\nThis dataset is associated with the following publication:\nLiu, W., H. Shi, K. Liu, X. Liu, E. Sahle-Demessie, and C. Stephan. A Sensitive Single Particle-ICP-MS Method for CeO2 Nanoparticles Analysis in Soil during Aging Process.   JOURNAL OF AGRICULTURAL AND FOOD CHEMISTRY. American Chemical Society, Washington, DC, USA, 69(3): 1115-1122, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1502547",
-            "keyword": [
-                "Single particle (SP)- ICP-MS",
-                "CeO2 nanoparticles",
-                "Tetrasodium pyrophosphate",
-                "soil",
-                "Extraction"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502547/documents/Data%20Dictionary_MWCNT_PlolymerComposite.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Data set is based on an analytical method for the extraction, detection, and characterization of engineered nanoparticles in the soil. \n\nThis dataset is associated with the following publication:\nLiu, W., H. Shi, K. Liu, X. Liu, E. Sahle-Demessie, and C. Stephan. A Sensitive Single Particle-ICP-MS Method for CeO2 Nanoparticles Analysis in Soil during Aging Process.   JOURNAL OF AGRICULTURAL AND FOOD CHEMISTRY. American Chemical Society, Washington, DC, USA, 69(3): 1115-1122, (2021).",
             "distribution": [
                 {
-                    "title": "G-STD-0010591-JA-15-1 (002).docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502547/G-STD-0010591-JA-15-1%20%28002%29.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "G-STD-0010591-JA-15-1 (002).docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502547",
+            "keyword": [
+                "Single particle (SP)- ICP-MS",
+                "CeO2 nanoparticles",
+                "Tetrasodium pyrophosphate",
+                "soil",
+                "Extraction"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-03",
-            "references": [
-                "https://pubs.acs.org/doi/10.1021/acs.jafc.0c06343"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -128957,20 +128953,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502547/documents/Data%20Dictionary_MWCNT_PlolymerComposite.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://pubs.acs.org/doi/10.1021/acs.jafc.0c06343"
+            ],
+            "rights": null,
+            "title": "Fate of Cerium Dioxide Nanoparticles in Soil Monitored by Single Particle ICP-MS"
         },
         {
-            "title": "Datasets for manuscript: Valuing Economic Impact Reductions of Nutrient Pollution from Livestock Waste",
-            "description": "https://github.com/zavalab/JuliaBox/tree/master/HiddenImpacts \nThis folder provides supporting codes for the paper \"Valuing Economic Impact Reductions of Nutrient Pollution from Livestock Waste\".\n* The folder \"sensitivity_analysis\" contains the code and data files for different values of the economic impact/value of service (vos).\n* The folder \"GIS_data\" contains the code and data files used to generate the maps of the Upper Yahara watershed region presented in the paper. \n* In each case, we have three Julia scripts: \"market_model.jl\", \"market_Run.jl\", and \"market_print.jl\". One should run \"market_Run.jl\" first, this script will automatically read the \"market_model.jl\" script, establish the model, and solve the model. Then, the \"market_print.jl\" should be run in order to print out all the result files.\n* If a sensitivity analysis on the VOS needs to be conducted (similar to the paper), one can change the lambda value in line 26 in \"market_model.jl\".\n* We recommend use Julia 0.6.4 and Gurobi 8.1 to run all code files for sensitivity analysis. \n\nThis dataset is associated with the following publication:\nSampat, A.M., A. Hicks, G. Ruiz-Mercado, and V.M. Zavala. Valuing economic impact reductions of nutrient pollution from livestock waste.   Resources, Conservation and Recycling. Elsevier Science BV, Amsterdam,  NETHERLANDS, 164: 105199, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Gerardo Ruiz-Mercado",
+                "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
+            },
+            "description": "https://github.com/zavalab/JuliaBox/tree/master/HiddenImpacts \nThis folder provides supporting codes for the paper \"Valuing Economic Impact Reductions of Nutrient Pollution from Livestock Waste\".\n* The folder \"sensitivity_analysis\" contains the code and data files for different values of the economic impact/value of service (vos).\n* The folder \"GIS_data\" contains the code and data files used to generate the maps of the Upper Yahara watershed region presented in the paper. \n* In each case, we have three Julia scripts: \"market_model.jl\", \"market_Run.jl\", and \"market_print.jl\". One should run \"market_Run.jl\" first, this script will automatically read the \"market_model.jl\" script, establish the model, and solve the model. Then, the \"market_print.jl\" should be run in order to print out all the result files.\n* If a sensitivity analysis on the VOS needs to be conducted (similar to the paper), one can change the lambda value in line 26 in \"market_model.jl\".\n* We recommend use Julia 0.6.4 and Gurobi 8.1 to run all code files for sensitivity analysis. \n\nThis dataset is associated with the following publication:\nSampat, A.M., A. Hicks, G. Ruiz-Mercado, and V.M. Zavala. Valuing economic impact reductions of nutrient pollution from livestock waste.   Resources, Conservation and Recycling. Elsevier Science BV, Amsterdam,  NETHERLANDS, 164: 105199, (2021).",
+            "distribution": [
+                {
+                    "accessURL": "https://github.com/zavalab/JuliaBox/tree/master/SC_HABs",
+                    "title": "https://github.com/zavalab/JuliaBox/tree/master/SC_HABs"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518420",
             "keyword": [
@@ -128985,19 +128988,10 @@
                 "Harmful Algal Bloom (HAB)",
                 "energy recovery"
             ],
-            "contactPoint": {
-                "fn": "Gerardo Ruiz-Mercado",
-                "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://github.com/zavalab/JuliaBox/tree/master/SC_HABs",
-                    "accessURL": "https://github.com/zavalab/JuliaBox/tree/master/SC_HABs"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-09",
-            "references": [
-                "https://doi.org/10.1016/j.resconrec.2020.105199"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129007,19 +129001,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.resconrec.2020.105199"
+            ],
+            "rights": null,
+            "title": "Datasets for manuscript: Valuing Economic Impact Reductions of Nutrient Pollution from Livestock Waste"
         },
         {
-            "title": "High-throughput Toxicogenomic Screening of Chemicals in the Environment Using Metabolically Competent, Human-derived Hepatic Cell Cultures ",
-            "description": "Gene expression data from the Fluidigm qRT-PCR arrays was analyzed in R (v3.6.1; R Foundation for Statistical Computing, 2019). Prior to processing through the tcpl package, each qRT-PCR primer set was annotated as an individual assay endpoint (aeid) for analyses. For each plate, well types were designated for test compound wells (t), positive controls (c), (that is phenobarbital) and neutral controls (n, DMSO). Fold-change in the number of amplification cycles needed to pass the background threshold (Ct) for 96 transcripts to (ftp://newftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA, file LTEA_Level2_20191119.zip) were normalized to the geometric mean of three housekeeping genes (ACTB, GAPDH, POLR2A) to generate \u0394Ct values (cval). Prior to calculating the response values (rval), or \u0394\u0394Ct, for each transcript (n = 96) per well, the baseline value (bval), the plate-wise median of the neutral control wells, was generated for each plate (the normalization process is described in detail in supplemental file SupFile4-DeltaCTCalculation.docx). The bval was subtracted from the cval to yield the rval or log2 Fold Change per transcript. \n\nGene expression data from the Fluidigm qRT-PCR arrays was analyzed in R (v3.6.1; R Foundation for Statistical Computing, 2019). Prior to processing through the tcpl package, each qRT-PCR primer set was annotated as an individual assay endpoint (aeid) for analyses. For each plate, well types were designated for test compound wells (t), positive controls (c), (that is phenobarbital) and neutral controls (n, DMSO). Fold-change in the number of amplification cycles needed to pass the background threshold (Ct) for 96 transcripts to (ftp://newftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA, file LTEA_Level5_20191119.zip) were normalized to the geometric mean of three housekeeping genes (ACTB, GAPDH, POLR2A) to generate \u0394Ct values (cval). Prior to calculating the response values (rval), or \u0394\u0394Ct, for each transcript (n = 96) per well, the baseline value (bval), the plate-wise median of the neutral control wells, was generated for each plate (the normalization process is described in detail in supplemental file SupFile4-DeltaCTCalculation.docx). The bval was subtracted from the cval to yield the rval or log2 Fold Change per transcript.\n\nSupplemental File LTEA_Inucyte_Images.zip is comprised of 20,493 images totaling more than 15 gigabytes. Cell morphology images were acquired for each well/plate with an Essen IncuCyte\u2122 FLR automated phase-contrast microscope located inside a tissue culture incubator. Six 96-well culture plates were loaded into the instrument and imaged for an elapsed time (~24 minutes). The IncuCyte\u2122 software was used for image capturing and export of images in JPEG format. \n\nThis dataset is associated with the following publication:\nFranzosa, J., J. Bonzo, J. Jack, N.C. Baker, P. Kothiya, R. Witek, P. Hurban, S. Siferd, S. Hester, I. Shah, S. Ferguson, K. Houck, and J. Wambaugh. High-throughput toxicogenomic screening of chemicals in the environment using metabolically competent hepatic cell cultures.   npj Systems Biology and Applications. Springer Nature Group, New York, NY,  7: Article 7, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Wambaugh",
+                "hasEmail": "mailto:wambaugh.john@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/chemical-research/exploring-toxcast-data-overview-tcpl-r-package",
+            "description": "Gene expression data from the Fluidigm qRT-PCR arrays was analyzed in R (v3.6.1; R Foundation for Statistical Computing, 2019). Prior to processing through the tcpl package, each qRT-PCR primer set was annotated as an individual assay endpoint (aeid) for analyses. For each plate, well types were designated for test compound wells (t), positive controls (c), (that is phenobarbital) and neutral controls (n, DMSO). Fold-change in the number of amplification cycles needed to pass the background threshold (Ct) for 96 transcripts to (ftp://newftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA, file LTEA_Level2_20191119.zip) were normalized to the geometric mean of three housekeeping genes (ACTB, GAPDH, POLR2A) to generate \u0394Ct values (cval). Prior to calculating the response values (rval), or \u0394\u0394Ct, for each transcript (n = 96) per well, the baseline value (bval), the plate-wise median of the neutral control wells, was generated for each plate (the normalization process is described in detail in supplemental file SupFile4-DeltaCTCalculation.docx). The bval was subtracted from the cval to yield the rval or log2 Fold Change per transcript. \n\nGene expression data from the Fluidigm qRT-PCR arrays was analyzed in R (v3.6.1; R Foundation for Statistical Computing, 2019). Prior to processing through the tcpl package, each qRT-PCR primer set was annotated as an individual assay endpoint (aeid) for analyses. For each plate, well types were designated for test compound wells (t), positive controls (c), (that is phenobarbital) and neutral controls (n, DMSO). Fold-change in the number of amplification cycles needed to pass the background threshold (Ct) for 96 transcripts to (ftp://newftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA, file LTEA_Level5_20191119.zip) were normalized to the geometric mean of three housekeeping genes (ACTB, GAPDH, POLR2A) to generate \u0394Ct values (cval). Prior to calculating the response values (rval), or \u0394\u0394Ct, for each transcript (n = 96) per well, the baseline value (bval), the plate-wise median of the neutral control wells, was generated for each plate (the normalization process is described in detail in supplemental file SupFile4-DeltaCTCalculation.docx). The bval was subtracted from the cval to yield the rval or log2 Fold Change per transcript.\n\nSupplemental File LTEA_Inucyte_Images.zip is comprised of 20,493 images totaling more than 15 gigabytes. Cell morphology images were acquired for each well/plate with an Essen IncuCyte\u2122 FLR automated phase-contrast microscope located inside a tissue culture incubator. Six 96-well culture plates were loaded into the instrument and imaged for an elapsed time (~24 minutes). The IncuCyte\u2122 software was used for image capturing and export of images in JPEG format. \n\nThis dataset is associated with the following publication:\nFranzosa, J., J. Bonzo, J. Jack, N.C. Baker, P. Kothiya, R. Witek, P. Hurban, S. Siferd, S. Hester, I. Shah, S. Ferguson, K. Houck, and J. Wambaugh. High-throughput toxicogenomic screening of chemicals in the environment using metabolically competent hepatic cell cultures.   npj Systems Biology and Applications. Springer Nature Group, New York, NY,  7: Article 7, (2021).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA",
+                    "title": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518725",
             "keyword": [
@@ -129037,19 +129041,10 @@
                 "high-throughput screening",
                 "in vitro high-throughput screening"
             ],
-            "contactPoint": {
-                "fn": "John Wambaugh",
-                "hasEmail": "mailto:wambaugh.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/CCED_Publication_Data/Wambaugh/ToxCast_LTEA"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-19",
-            "references": [
-                "https://doi.org/10.1038/s41540-020-00166-2"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129060,39 +129055,38 @@
                     }
                 }
             },
-            "describedBy": "https://www.epa.gov/chemical-research/exploring-toxcast-data-overview-tcpl-r-package"
+            "references": [
+                "https://doi.org/10.1038/s41540-020-00166-2"
+            ],
+            "rights": null,
+            "title": "High-throughput Toxicogenomic Screening of Chemicals in the Environment Using Metabolically Competent, Human-derived Hepatic Cell Cultures "
         },
         {
-            "title": " Indophenol Method Temperature Dependence: Impact on monochloramine, free ammonia, and free chlorine measurement",
-            "description": "Data is for the manuscript figures. \n\nThis dataset is associated with the following publication:\nWaters, T., M. Alexander, and D. Wahman. Temperature impact on monochloramine, free ammonia, and free chlorine indophenol methods.   Water Practice & Technology. IWA Publishing, London,  UK, 16(1): 135-145, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1517618",
-            "keyword": [
-                "nitrification",
-                "chloramine"
-            ],
             "contactPoint": {
                 "fn": "David Wahman",
                 "hasEmail": "mailto:wahman.david@epa.gov"
             },
+            "description": "Data is for the manuscript figures. \n\nThis dataset is associated with the following publication:\nWaters, T., M. Alexander, and D. Wahman. Temperature impact on monochloramine, free ammonia, and free chlorine indophenol methods.   Water Practice & Technology. IWA Publishing, London,  UK, 16(1): 135-145, (2021).",
             "distribution": [
                 {
-                    "title": "Indophenol Method Temperature Dependence Impact on monochloramine free ammonia and free chlorine.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517618/Indophenol%20Method%20Temperature%20Dependence%20Impact%20on%20monochloramine%20free%20ammonia%20and%20free%20chlorine.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Indophenol Method Temperature Dependence Impact on monochloramine free ammonia and free chlorine.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517618",
+            "keyword": [
+                "nitrification",
+                "chloramine"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-23",
-            "references": [
-                "https://doi.org/10.2166/wpt.2020.104"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129102,41 +129096,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2166/wpt.2020.104"
+            ],
+            "rights": null,
+            "title": " Indophenol Method Temperature Dependence: Impact on monochloramine, free ammonia, and free chlorine measurement"
         },
         {
-            "title": "How to Support the Application of Multiple Criteria Decision Analysis?  Let us Start with a Taxonomy",
-            "description": "Decision making is a complex task that involves a multitude of perspectives, constraints, and variables. Multiple Criteria Decision Analysis (MCDA) is a process that has been used for several decades to support decision making. It includes a series of steps that systematically help Decision Maker(s) (DM(s)) and stakeholders in structuring a decision problem, identifying their preferences and building a decision recommendation consistent with those preferences. Over the last decades, many studies have demonstrated the conduct of the MCDA process and how to select an MCDA method. Until now, there has not been a review of these studies, nor a proposal of a unified and comprehensive high-level representation of the MCDA process characteristics (i.e., features), which is the goal of this paper. We introduce a review of the research that defines how to conduct the MCDA process, compares MCDA methods and presents Decision Support Systems (DSSs) to recommend a relevant MCDA method or a subset of methods. We then synthesize this research into a taxonomy of 10 characteristics of the MCDA process, grouped into three main phases, (i) problem formulation, (ii) construction of the decision recommendation and (iii) qualitative features and technical support. Each of these phases includes a subset of the 10 characteristics that help the analyst implementing the MCDA process, while also being aware of the implication of these choices at each step. By showing how decision making can be split into manageable and justifiable steps, we reduce the risk of overwhelming the analyst, as well as the DMs/stakeholders during the MCDA process. Additionally, we show how the DSSs for MCDA method recommendation can be grouped into three main clusters, such that a traceable and categorizable development of such systems can be enhanced. \n\nThis dataset is associated with the following publication:\nCinelli, M., M. Kadzi\u0144ski, M. Gonzalez, and R. S\u0142owi\u0144ski. How to support the application of multiple criteria decision analysis? Let us start with a comprehensive taxonomy.   ACS Omega. American Chemical Society, Washington, DC, USA, 96: 102261, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1504539",
-            "keyword": [
-                "Decision analysis",
-                "emerging technology",
-                "Environmental remediation",
-                "multi-criteria decision analysis"
-            ],
             "contactPoint": {
                 "fn": "Michael Gonzalez",
                 "hasEmail": "mailto:gonzalez.michael@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1504539/documents/Appendix%20B%20-%20Data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Decision making is a complex task that involves a multitude of perspectives, constraints, and variables. Multiple Criteria Decision Analysis (MCDA) is a process that has been used for several decades to support decision making. It includes a series of steps that systematically help Decision Maker(s) (DM(s)) and stakeholders in structuring a decision problem, identifying their preferences and building a decision recommendation consistent with those preferences. Over the last decades, many studies have demonstrated the conduct of the MCDA process and how to select an MCDA method. Until now, there has not been a review of these studies, nor a proposal of a unified and comprehensive high-level representation of the MCDA process characteristics (i.e., features), which is the goal of this paper. We introduce a review of the research that defines how to conduct the MCDA process, compares MCDA methods and presents Decision Support Systems (DSSs) to recommend a relevant MCDA method or a subset of methods. We then synthesize this research into a taxonomy of 10 characteristics of the MCDA process, grouped into three main phases, (i) problem formulation, (ii) construction of the decision recommendation and (iii) qualitative features and technical support. Each of these phases includes a subset of the 10 characteristics that help the analyst implementing the MCDA process, while also being aware of the implication of these choices at each step. By showing how decision making can be split into manageable and justifiable steps, we reduce the risk of overwhelming the analyst, as well as the DMs/stakeholders during the MCDA process. Additionally, we show how the DSSs for MCDA method recommendation can be grouped into three main clusters, such that a traceable and categorizable development of such systems can be enhanced. \n\nThis dataset is associated with the following publication:\nCinelli, M., M. Kadzi\u0144ski, M. Gonzalez, and R. S\u0142owi\u0144ski. How to support the application of multiple criteria decision analysis? Let us start with a comprehensive taxonomy.   ACS Omega. American Chemical Society, Washington, DC, USA, 96: 102261, (2020).",
             "distribution": [
                 {
-                    "title": "Appendix A - Compiled data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504539/Appendix%20A%20-%20Compiled%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Appendix A - Compiled data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504539",
+            "keyword": [
+                "Decision analysis",
+                "emerging technology",
+                "Environmental remediation",
+                "multi-criteria decision analysis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-10-03",
-            "references": [
-                "https://doi.org/10.1016/j.omega.2020.102306"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129147,20 +129143,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1504539/documents/Appendix%20B%20-%20Data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.omega.2020.102306"
+            ],
+            "rights": null,
+            "title": "How to Support the Application of Multiple Criteria Decision Analysis?  Let us Start with a Taxonomy"
         },
         {
-            "title": "Contrasting radical activity",
-            "description": "Reaction intermediates formed during the ultra-violet (UV) activation of hydrogen peroxide (H2O2) (UV-AHP) and persulfate (S2O82-) (UV-APS) include hydroxyl (\u2022OH) and sulfate radicals (SO4\u2022-), respectively. These radicals, used in oxidation treatment systems to degrade a broad spectrum of environmental contaminants, may also react with non-target chemical species (scavengers) that limit treatment efficiency. UV-AHP and UV-APS treatment systems were amended with solid phase alumina to assess scavenging by solid surfaces. The relative rates of reaction between the target compound, rhodamine B dye (RhB), and aqueous and solid phase scavengers was used to assess treatment performance. The overall rate of reaction and rate of radical scavenging was greater for \u2022OH than SO4\u2022-. Scavenging by dissolved constituents was dominated by the oxidant used (H2O2, S2O82-); and the rate of radical scavenging by alumina was greater than the rate of RhB oxidation in all cases. Treatment efficiency was lower in the UV-AHP than in the UV-APS treatment system and was attributed to greater aqueous and solid phase scavenging rates. The cost of commercially available H2O2 ($0.031 mol-1) and PS ($0.24 mol-1) was used in conjunction with the overall treatment efficiency to assess specific cost of treatment. The specific cost to treat the probe compound with UV-AHP was greater than UV-APS and was attributed to the much lower treatment efficiency with UV-AHP. The much-desired high reaction rate constants between \u2022OH and environmental contaminants, relative to SO4\u2022-, comes at the cost of greater combined scavenging rates, and consequently lower treatment efficiency. \n\nThis dataset is associated with the following publication:\nRusevova Crincoli, K., and S.G. Huling. Contrasting hydrogen peroxide- and persulfate-driven oxidation systems: Impact of radical scavenging on treatment efficiency and cost.   Chemical Engineering Journal. Elsevier BV, AMSTERDAM,  NETHERLANDS, 404: 1-6, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Scott Huling",
+                "hasEmail": "mailto:huling.scott@epa.gov"
+            },
+            "description": "Reaction intermediates formed during the ultra-violet (UV) activation of hydrogen peroxide (H2O2) (UV-AHP) and persulfate (S2O82-) (UV-APS) include hydroxyl (\u2022OH) and sulfate radicals (SO4\u2022-), respectively. These radicals, used in oxidation treatment systems to degrade a broad spectrum of environmental contaminants, may also react with non-target chemical species (scavengers) that limit treatment efficiency. UV-AHP and UV-APS treatment systems were amended with solid phase alumina to assess scavenging by solid surfaces. The relative rates of reaction between the target compound, rhodamine B dye (RhB), and aqueous and solid phase scavengers was used to assess treatment performance. The overall rate of reaction and rate of radical scavenging was greater for \u2022OH than SO4\u2022-. Scavenging by dissolved constituents was dominated by the oxidant used (H2O2, S2O82-); and the rate of radical scavenging by alumina was greater than the rate of RhB oxidation in all cases. Treatment efficiency was lower in the UV-AHP than in the UV-APS treatment system and was attributed to greater aqueous and solid phase scavenging rates. The cost of commercially available H2O2 ($0.031 mol-1) and PS ($0.24 mol-1) was used in conjunction with the overall treatment efficiency to assess specific cost of treatment. The specific cost to treat the probe compound with UV-AHP was greater than UV-APS and was attributed to the much lower treatment efficiency with UV-AHP. The much-desired high reaction rate constants between \u2022OH and environmental contaminants, relative to SO4\u2022-, comes at the cost of greater combined scavenging rates, and consequently lower treatment efficiency. \n\nThis dataset is associated with the following publication:\nRusevova Crincoli, K., and S.G. Huling. Contrasting hydrogen peroxide- and persulfate-driven oxidation systems: Impact of radical scavenging on treatment efficiency and cost.   Chemical Engineering Journal. Elsevier BV, AMSTERDAM,  NETHERLANDS, 404: 1-6, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518483/Science%20Hub_data%20set%20message.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science Hub_data set message.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518483",
             "keyword": [
@@ -129171,20 +129175,10 @@
                 "treatment efficiency",
                 "Mineral Surfaces"
             ],
-            "contactPoint": {
-                "fn": "Scott Huling",
-                "hasEmail": "mailto:huling.scott@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Science Hub_data set message.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518483/Science%20Hub_data%20set%20message.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-26",
-            "references": [
-                "https://doi.org/10.1016/j.cej.2020.126404"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129194,42 +129188,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.cej.2020.126404"
+            ],
+            "rights": null,
+            "title": "Contrasting radical activity"
         },
         {
-            "title": "GAC Oxidation",
-            "description": "Raw materials, activation methods, and post-activation treatment used in manufacturing granular activated carbon (GAC) results in a spectrum of physicochemical characteristics that potentially impact the adsorption oxidation treatment process. A comprehensive study is lacking that assesses the effect of GAC characteristics on adsorption oxidation treatment of contaminant-spent GAC. Consequently, it is inherently assumed the treatment process is GAC-independent. Here, GACs (n=31) were characterized and used in the hydrogen peroxide (H2O2)-based adsorption oxidation treatment of 2-chlorophenol (2CP)-spent GAC. The GACs exhibited a range in surface area, pore volume distribution, metals content, surface functionality, and H2O2 reaction. Chloride recovery, the treatment metric for 2CP oxidation, indicated a wide range in oxidation (0-49.2%) where bituminous- and wood-based GAC performed best. A selected subset of GACs (n=12), amended with iron, methyl tert-butyl ether, and H2O2, exhibited a range in oxidative treatment (1.1-57.9%). Correlations were established between GAC surface functionality, H2O2 reactivity, adsorption, and contaminant oxidation indicating multiple parameters play a collective and compounding role. The order of GACs successfully used in the treatment process is bituminous-based coal > wood > coconut > peat. Results showed adsorption oxidation treatment is GAC-dependent, and therefore, GAC selection is a key factor in the success of this technology. \n\nThis dataset is associated with the following publication:\nRusevova Crincoli, K., P.K. Jones, and S.G. Huling. Fenton-driven oxidation of contaminant-spent granular activated carbon (GAC): GAC selection and implications.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 734: 1-9, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1518530",
-            "keyword": [
-                "granular activated carbon",
-                "advanced oxidation",
-                "adsorption",
-                "MTBE",
-                "2-chlorophenol"
-            ],
             "contactPoint": {
                 "fn": "Scott Huling",
                 "hasEmail": "mailto:huling.scott@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1518530/documents/GAC%20Oxidation_Data%20Dictionary%20for%20SDMP.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Raw materials, activation methods, and post-activation treatment used in manufacturing granular activated carbon (GAC) results in a spectrum of physicochemical characteristics that potentially impact the adsorption oxidation treatment process. A comprehensive study is lacking that assesses the effect of GAC characteristics on adsorption oxidation treatment of contaminant-spent GAC. Consequently, it is inherently assumed the treatment process is GAC-independent. Here, GACs (n=31) were characterized and used in the hydrogen peroxide (H2O2)-based adsorption oxidation treatment of 2-chlorophenol (2CP)-spent GAC. The GACs exhibited a range in surface area, pore volume distribution, metals content, surface functionality, and H2O2 reaction. Chloride recovery, the treatment metric for 2CP oxidation, indicated a wide range in oxidation (0-49.2%) where bituminous- and wood-based GAC performed best. A selected subset of GACs (n=12), amended with iron, methyl tert-butyl ether, and H2O2, exhibited a range in oxidative treatment (1.1-57.9%). Correlations were established between GAC surface functionality, H2O2 reactivity, adsorption, and contaminant oxidation indicating multiple parameters play a collective and compounding role. The order of GACs successfully used in the treatment process is bituminous-based coal > wood > coconut > peat. Results showed adsorption oxidation treatment is GAC-dependent, and therefore, GAC selection is a key factor in the success of this technology. \n\nThis dataset is associated with the following publication:\nRusevova Crincoli, K., P.K. Jones, and S.G. Huling. Fenton-driven oxidation of contaminant-spent granular activated carbon (GAC): GAC selection and implications.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 734: 1-9, (2020).",
             "distribution": [
                 {
-                    "title": "GAC Oxidation_Sci Hub Data Set Vers 2.0.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518530/GAC%20Oxidation_Sci%20Hub%20Data%20Set%20Vers%202.0.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GAC Oxidation_Sci Hub Data Set Vers 2.0.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518530",
+            "keyword": [
+                "granular activated carbon",
+                "advanced oxidation",
+                "adsorption",
+                "MTBE",
+                "2-chlorophenol"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-14",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2020.139435"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129240,41 +129236,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1518530/documents/GAC%20Oxidation_Data%20Dictionary%20for%20SDMP.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2020.139435"
+            ],
+            "rights": null,
+            "title": "GAC Oxidation"
         },
         {
-            "title": "Nitrous Oxide Formation and Dissolved Oxygen Consumption from Dichloramine Hydrolysis: Evidence of Nitrosation Stemming from Nitroxyl in Chloramination",
-            "description": "The dataset is the contact information for the corresponding author to obtain data associated with the manuscript. \n\nThis dataset is associated with the following publication:\nPham, H., D. Wahman, and J. Fairey. Updated Reaction Pathway for Dichloramine Decomposition: Formation of Reactive Nitrogen Species and N-Nitrosodimethylamine.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(3): 1740-1749, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1518479",
-            "keyword": [
-                "NDMA",
-                "nitrification",
-                "chloramine"
-            ],
             "contactPoint": {
                 "fn": "David Wahman",
                 "hasEmail": "mailto:wahman.david@epa.gov"
             },
+            "description": "The dataset is the contact information for the corresponding author to obtain data associated with the manuscript. \n\nThis dataset is associated with the following publication:\nPham, H., D. Wahman, and J. Fairey. Updated Reaction Pathway for Dichloramine Decomposition: Formation of Reactive Nitrogen Species and N-Nitrosodimethylamine.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(3): 1740-1749, (2021).",
             "distribution": [
                 {
-                    "title": "Manuscript Data Contact Information.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518479/Manuscript%20Data%20Contact%20Information.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Manuscript Data Contact Information.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518479",
+            "keyword": [
+                "NDMA",
+                "nitrification",
+                "chloramine"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-25",
-            "references": [
-                "https://doi.org/10.1021/acs.est.0c06456"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129284,19 +129278,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.0c06456"
+            ],
+            "rights": null,
+            "title": "Nitrous Oxide Formation and Dissolved Oxygen Consumption from Dichloramine Hydrolysis: Evidence of Nitrosation Stemming from Nitroxyl in Chloramination"
         },
         {
-            "title": "Datasets for manuscript \"Data engineering for tracking chemicals and releases at industrial end-of-life activities\"",
-            "description": "The GitHub repository contains a Python code (MC_Case_Study.py) to support and replicate the case study results shown in the manuscript entitled Data engineering for tracking chemicals and releases at industrial end-of-life activities. Also, it indicates the free-available Python libraries that are required for running the code \"MC_Case_Study.py.\" The dataset \"EoL_database_for_MC.csv\" contains all data to execute the Python code and obtain \"Figure 6: 6-level Sankey diagram for the case study\", \"Figure 7: Box plot for the case study\", and \"Figure 8: Histogram for the case study.\" A Table describing the data name entry and data type for the dataset \"EoL_database_for_MC.csv\" is shown. Also, this dataset information and Python code are provided in the manuscript Supporting Info file (see supporting documents). \n\nThis dataset is associated with the following publication:\nHernandez-Betancur, J.D., G.J. Ruiz-Mercado, J.P. Abraham, M. Martin, W.W. Ingwersen, and R.L. Smith. Data engineering for tracking chemicals and releases at industrial end-of-life activities.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 405: 124270, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Gerardo Ruiz-Mercado",
+                "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
+            },
+            "description": "The GitHub repository contains a Python code (MC_Case_Study.py) to support and replicate the case study results shown in the manuscript entitled Data engineering for tracking chemicals and releases at industrial end-of-life activities. Also, it indicates the free-available Python libraries that are required for running the code \"MC_Case_Study.py.\" The dataset \"EoL_database_for_MC.csv\" contains all data to execute the Python code and obtain \"Figure 6: 6-level Sankey diagram for the case study\", \"Figure 7: Box plot for the case study\", and \"Figure 8: Histogram for the case study.\" A Table describing the data name entry and data type for the dataset \"EoL_database_for_MC.csv\" is shown. Also, this dataset information and Python code are provided in the manuscript Supporting Info file (see supporting documents). \n\nThis dataset is associated with the following publication:\nHernandez-Betancur, J.D., G.J. Ruiz-Mercado, J.P. Abraham, M. Martin, W.W. Ingwersen, and R.L. Smith. Data engineering for tracking chemicals and releases at industrial end-of-life activities.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 405: 124270, (2021).",
+            "distribution": [
+                {
+                    "accessURL": "https://github.com/gruizmer/MC_Case_Study",
+                    "title": "https://github.com/gruizmer/MC_Case_Study"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518810",
             "keyword": [
@@ -129311,20 +129314,10 @@
                 "chemical manufacturing",
                 "Life Cycle Environmental Assessment"
             ],
-            "contactPoint": {
-                "fn": "Gerardo Ruiz-Mercado",
-                "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://github.com/gruizmer/MC_Case_Study",
-                    "accessURL": "https://github.com/gruizmer/MC_Case_Study"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-11",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2020.124270",
-                "https://pasteur.epa.gov/uploads/10.23719/1518810/documents/Updated_SI_chemicals_EoL_06-09-20_after_363review_-_QAClean.docx"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129334,19 +129327,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2020.124270",
+                "https://pasteur.epa.gov/uploads/10.23719/1518810/documents/Updated_SI_chemicals_EoL_06-09-20_after_363review_-_QAClean.docx"
+            ],
+            "rights": null,
+            "title": "Datasets for manuscript \"Data engineering for tracking chemicals and releases at industrial end-of-life activities\""
         },
         {
-            "title": "Dow UAS NOx Stack Boiler Emissions",
-            "description": "Read Me file with Journal title page.\nData dictionary.\nFigure/Table data (CEM data, flight data, emission factor data)",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Brian Gullett",
+                "hasEmail": "mailto:gullett.brian@epa.gov"
+            },
+            "description": "Read Me file with Journal title page.\nData dictionary.\nFigure/Table data (CEM data, flight data, emission factor data)",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520733/Data%20Table%20Science%20Hub%20Feb%203%202020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Table Science Hub Feb 3 2020.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520733",
             "keyword": [
@@ -129357,19 +129361,11 @@
                 "drone",
                 "continuous emission monitoring"
             ],
-            "contactPoint": {
-                "fn": "Brian Gullett",
-                "hasEmail": "mailto:gullett.brian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data Table Science Hub Feb 3 2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520733/Data%20Table%20Science%20Hub%20Feb%203%202020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-20",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -129378,42 +129374,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Dow UAS NOx Stack Boiler Emissions"
         },
         {
-            "title": "Dietary niche and growth rate of the nonnative tubenose goby (Proterorhinus semilunaris) in the Lake Superior basin, 2018",
-            "description": "Biological characters of age-0 tubenose goby captured in the St. Louis River, MN-WI, during 2018:\nDiet items by season with associated selection metrics\nLengths\nWeights (fresh, ethanol-preserved)\nSex\nAge (days)\nCatch data\n\nBiological characters of tadpole madtom captured in the St. Louis River, MN-WI, during 2018:\nDiet items by season with associated selection metrics. \n\nThis dataset is associated with the following publication:\nDawson, B., G. Peterson, T. Hrabik, and J. Hoffman. Dietary niche and growth rate of the nonnative tubenose goby (Proterorhinus semilunaris) in the Lake Superior basin.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 46(5): 1358-1368, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520467",
-            "keyword": [
-                "invasive species",
-                "competition",
-                "Gompertz",
-                "wetlands",
-                "Great Lakes."
-            ],
             "contactPoint": {
                 "fn": "Joel Hoffman",
                 "hasEmail": "mailto:hoffman.joel@epa.gov"
             },
+            "description": "Biological characters of age-0 tubenose goby captured in the St. Louis River, MN-WI, during 2018:\nDiet items by season with associated selection metrics\nLengths\nWeights (fresh, ethanol-preserved)\nSex\nAge (days)\nCatch data\n\nBiological characters of tadpole madtom captured in the St. Louis River, MN-WI, during 2018:\nDiet items by season with associated selection metrics. \n\nThis dataset is associated with the following publication:\nDawson, B., G. Peterson, T. Hrabik, and J. Hoffman. Dietary niche and growth rate of the nonnative tubenose goby (Proterorhinus semilunaris) in the Lake Superior basin.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 46(5): 1358-1368, (2020).",
             "distribution": [
                 {
-                    "title": "HoffmanJoel_A-69pm_Dataset_20191216.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520467/HoffmanJoel_A-69pm_Dataset_20191216.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HoffmanJoel_A-69pm_Dataset_20191216.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520467",
+            "keyword": [
+                "invasive species",
+                "competition",
+                "Gompertz",
+                "wetlands",
+                "Great Lakes."
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-12-16",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2020.07.014"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129423,20 +129417,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2020.07.014"
+            ],
+            "rights": null,
+            "title": "Dietary niche and growth rate of the nonnative tubenose goby (Proterorhinus semilunaris) in the Lake Superior basin, 2018"
         },
         {
-            "title": "Associations between cumulative environmental quality and ten selected birth defects in Texas",
-            "description": "The Texas Birth Defects Registry (TBDR) of the Texas Department of State Health Services (TDSHS) is an active surveillance system that maintains information on infants with structural and chromosomal birth defects born to mothers residing in Texas at the time of birth (Texas Department of State Health Services, 2019). TBDR staff review medical records to identify and abstract relevant case information, which then undergoes extensive quality checks (Texas Department of State Health Services, 2019). All diagnoses are made prenatally or within one year after delivery (Texas Department of State Health Services, 2019). Data on cases was obtained from the TBDR. Information on live births for the denominators and on covariates for cases and denominators was obtained from the Texas Department of State Health Services Center for Health Statistics. This research was approved by the Texas Department of State Health Services Institutional Review Board and US EPA Human Subjects Review.\n\nThe Environmental Quality Index (EQI) estimates overall county-level environmental quality for the entire US for 2006-2010. The construction of the EQI is described elsewhere (United States Environmental Protection Agency, 2020). Briefly, the national data was compiled to represent simultaneous, cumulative environmental quality across each of the five domains: air (43 variables) representing criteria and hazardous air pollutants; water (51 variables), representing overall water quality, general water contamination, recreational water quality, drinking water quality, atmospheric deposition, drought, and chemical contamination; land (18 variables), representing agriculture, pesticides, contaminants, facilities, and radon; built (15 variables), representing roads, highway/road safety, public transit behavior, business environment, and subsidized housing environment; and sociodemographic (12 variables), representing socioeconomics and crime. The variables in each domain specific index were reduced using principal component analysis (PCA), with the first component retained as that domain\u2019s index value. The domain specific indices were valence corrected to ensure that the directionality of the variables was consistent with higher values suggesting poorer environmental quality. The domain specific indices were then processed through a second PCA and the first index retained as the overall EQI. The overall and domain specific EQI indices are publicly available through the US EPA (United States Environmental Protection Agency: https://edg.epa.gov/data/Public/ORD/NHEERL/EQI). This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Human health data are not available publicly. EQI data are available at: https://edg.epa.gov/data/Public/ORD/NHEERL/EQI. Format: Data are stored as csv files. \n\nThis dataset is associated with the following publication:\nKrajewski, A., K. Rappazzo, P. Langlois, L. Messer, and D. Lobdell. Associations between cumulative environmental quality and ten selected birth defects in Texas.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA, 113(2): 161-172, (2020).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
+            "contactPoint": {
+                "fn": "Danelle Lobdell",
+                "hasEmail": "mailto:lobdell.danelle@epa.gov"
+            },
+            "description": "The Texas Birth Defects Registry (TBDR) of the Texas Department of State Health Services (TDSHS) is an active surveillance system that maintains information on infants with structural and chromosomal birth defects born to mothers residing in Texas at the time of birth (Texas Department of State Health Services, 2019). TBDR staff review medical records to identify and abstract relevant case information, which then undergoes extensive quality checks (Texas Department of State Health Services, 2019). All diagnoses are made prenatally or within one year after delivery (Texas Department of State Health Services, 2019). Data on cases was obtained from the TBDR. Information on live births for the denominators and on covariates for cases and denominators was obtained from the Texas Department of State Health Services Center for Health Statistics. This research was approved by the Texas Department of State Health Services Institutional Review Board and US EPA Human Subjects Review.\n\nThe Environmental Quality Index (EQI) estimates overall county-level environmental quality for the entire US for 2006-2010. The construction of the EQI is described elsewhere (United States Environmental Protection Agency, 2020). Briefly, the national data was compiled to represent simultaneous, cumulative environmental quality across each of the five domains: air (43 variables) representing criteria and hazardous air pollutants; water (51 variables), representing overall water quality, general water contamination, recreational water quality, drinking water quality, atmospheric deposition, drought, and chemical contamination; land (18 variables), representing agriculture, pesticides, contaminants, facilities, and radon; built (15 variables), representing roads, highway/road safety, public transit behavior, business environment, and subsidized housing environment; and sociodemographic (12 variables), representing socioeconomics and crime. The variables in each domain specific index were reduced using principal component analysis (PCA), with the first component retained as that domain\u2019s index value. The domain specific indices were valence corrected to ensure that the directionality of the variables was consistent with higher values suggesting poorer environmental quality. The domain specific indices were then processed through a second PCA and the first index retained as the overall EQI. The overall and domain specific EQI indices are publicly available through the US EPA (United States Environmental Protection Agency: https://edg.epa.gov/data/Public/ORD/NHEERL/EQI). This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Human health data are not available publicly. EQI data are available at: https://edg.epa.gov/data/Public/ORD/NHEERL/EQI. Format: Data are stored as csv files. \n\nThis dataset is associated with the following publication:\nKrajewski, A., K. Rappazzo, P. Langlois, L. Messer, and D. Lobdell. Associations between cumulative environmental quality and ten selected birth defects in Texas.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA, 113(2): 161-172, (2020).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1518475",
             "keyword": [
                 "environmental quality",
@@ -129446,14 +129444,10 @@
                 "sociodemographic quality",
                 "land quality"
             ],
-            "contactPoint": {
-                "fn": "Danelle Lobdell",
-                "hasEmail": "mailto:lobdell.danelle@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-02",
-            "references": [
-                "https://doi.org/10.1002/bdr2.1788"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129463,41 +129457,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/bdr2.1788"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Associations between cumulative environmental quality and ten selected birth defects in Texas"
         },
         {
-            "title": "Assessing reproductive effects of aromatase inhibition on fishes with group-synchronous oocyte development using western mosquitofish (Gambusia affinis) as a model",
-            "description": "Predictive models and frameworks for linking inhibition of the enzyme aromatase, as measured in non-animal high throughput screening assays, to adverse effects on reproduction in fish have been established. However, those models were established using data from several fish species commonly reared in the laboratory that employ a particular reproductive strategy involving asynchronous oocyte development and repeat spawning. Many fish species employ synchronous oocyte development and spawn annually. This product was intended to help address the question of whether the current approaches for predicting impacts of aromatase inhibitors are applicable to fish with a synchronous/annual spawning reproduction strategy. The study establishes the mosquitofish as a viable laboratory model with synchronous oocyte development and provides preliminary evidence that exposure to aromatase inhibitors during a critical period of the reproductive cycle can lead to adverse effects on fish reproduction. \n\nThis dataset provides all the data used to generate the tables and figures presented in Doering et al. \"Assessing reproductive effects of aromatase inhibition on fishes with group-synchronous oocyte development using Western Mosquitofish (Gambusia affinis) as a model.\"  Data are organized as separate tabs in an Excel spreadsheet with a cover sheet, followed by a separate tab for each Figure and Table from the manuscript.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520452",
-            "keyword": [
-                "adverse outcome pathway",
-                "ecotoxicology",
-                "endocrine disruption",
-                "screening and prioritization",
-                "aquatic ecosystems"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Predictive models and frameworks for linking inhibition of the enzyme aromatase, as measured in non-animal high throughput screening assays, to adverse effects on reproduction in fish have been established. However, those models were established using data from several fish species commonly reared in the laboratory that employ a particular reproductive strategy involving asynchronous oocyte development and repeat spawning. Many fish species employ synchronous oocyte development and spawn annually. This product was intended to help address the question of whether the current approaches for predicting impacts of aromatase inhibitors are applicable to fish with a synchronous/annual spawning reproduction strategy. The study establishes the mosquitofish as a viable laboratory model with synchronous oocyte development and provides preliminary evidence that exposure to aromatase inhibitors during a critical period of the reproductive cycle can lead to adverse effects on fish reproduction. \n\nThis dataset provides all the data used to generate the tables and figures presented in Doering et al. \"Assessing reproductive effects of aromatase inhibition on fishes with group-synchronous oocyte development using Western Mosquitofish (Gambusia affinis) as a model.\"  Data are organized as separate tabs in an Excel spreadsheet with a cover sheet, followed by a separate tab for each Figure and Table from the manuscript.",
             "distribution": [
                 {
-                    "title": "Doering et al mosquitofish ScienceHub File_v2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520452/Doering%20et%20al%20mosquitofish%20ScienceHub%20File_v2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Doering et al mosquitofish ScienceHub File_v2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520452",
+            "keyword": [
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "endocrine disruption",
+                "screening and prioritization",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-28",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -129506,19 +129502,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Assessing reproductive effects of aromatase inhibition on fishes with group-synchronous oocyte development using western mosquitofish (Gambusia affinis) as a model"
         },
         {
-            "title": "Dataset for ORD-033364: Identification of Novel Activators of the Metal Responsive Transcription Factor (MTF-1) Using a Gene Expression Biomarker in a Microarray Compendium",
-            "description": "The microarray experiments examined in the study. \n\nThis dataset is associated with the following publication:\nJackson, A., J. Liu, B. Vallanat, C. Jones, M. Nelms, G. Patlewicz, and J. Corton. Identification of Novel Activators of the Metal Responsive Transcription Factor (MTF-1) Using a Gene Expression Biomarker in a Microarray Compendium.   Metallomics. Royal Society of Chemistry, London,  UK, 12(9): 1400-1415, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jon Corton",
+                "hasEmail": "mailto:corton.chris@epa.gov"
+            },
+            "description": "The microarray experiments examined in the study. \n\nThis dataset is associated with the following publication:\nJackson, A., J. Liu, B. Vallanat, C. Jones, M. Nelms, G. Patlewicz, and J. Corton. Identification of Novel Activators of the Metal Responsive Transcription Factor (MTF-1) Using a Gene Expression Biomarker in a Microarray Compendium.   Metallomics. Royal Society of Chemistry, London,  UK, 12(9): 1400-1415, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504417/Data%20submission%20for%20A-893g.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-893g.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504417",
             "keyword": [
@@ -129530,20 +129534,10 @@
                 "oxidative stress",
                 "Nrf2"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data submission for A-893g.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504417/Data%20submission%20for%20A-893g.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-11",
-            "references": [
-                "https://doi.org/10.1039/d0mt00071j"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129553,19 +129547,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d0mt00071j"
+            ],
+            "rights": null,
+            "title": "Dataset for ORD-033364: Identification of Novel Activators of the Metal Responsive Transcription Factor (MTF-1) Using a Gene Expression Biomarker in a Microarray Compendium"
         },
         {
-            "title": "Dataset for ORD-033373: Gene Expression Thresholds Are Predictive of Rat Liver Tumorigens in Short-Term Assays",
-            "description": "The microarray experiments used in the study. \n\nThis dataset is associated with the following publication:\nHill, T., J. Rooney, J. Abedini, H. El-Masri, C. Wood, and J. Corton. Gene Expression Thresholds Derived From Short-term Exposures Identify Rat Liver Tumorigens.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  177(1): 41-59, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jon Corton",
+                "hasEmail": "mailto:corton.chris@epa.gov"
+            },
+            "description": "The microarray experiments used in the study. \n\nThis dataset is associated with the following publication:\nHill, T., J. Rooney, J. Abedini, H. El-Masri, C. Wood, and J. Corton. Gene Expression Thresholds Derived From Short-term Exposures Identify Rat Liver Tumorigens.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  177(1): 41-59, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504426/Data%20submission%20for%20A-xsk0.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-xsk0.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504426",
             "keyword": [
@@ -129576,20 +129580,10 @@
                 "molecular initiating event",
                 "adverse outcome pathway"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data submission for A-xsk0.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504426/Data%20submission%20for%20A-xsk0.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-09",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfaa102"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129599,39 +129593,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfaa102"
+            ],
+            "rights": null,
+            "title": "Dataset for ORD-033373: Gene Expression Thresholds Are Predictive of Rat Liver Tumorigens in Short-Term Assays"
         },
         {
-            "title": "RECAP dataset: Subject, exposure, and health endpoint (blood, lipids, cardiac, and lung) data",
-            "description": "This dataset contains deidentified subject level data from the study titled: Responses to Exposure to Low Levels of Concentrated Ambient Particles in Healthy Young Adults (RECAP). Subject, exposure, and health endpoint data are included in the dataset. Health endpoint data includes inflammatory, heart rate variability and cardiac repolarization, lung function, blood chemistry, and lipids measures. \n\nThis dataset is associated with the following publication:\nWyatt, L., R. Devlin, A. Rappold, and M. Case. Low levels of fine particulate matter increase vascular damage and reduce pulmonary function in young healthy adults.   Particle and Fibre Toxicology. BioMed Central Ltd, London,  UK, 17(1): 58, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1518774",
-            "keyword": [
-                "controlled human exposure",
-                "particulate matter air pollution"
-            ],
             "contactPoint": {
                 "fn": "Lauren Wyatt",
                 "hasEmail": "mailto:wyatt.lauren@epa.gov"
             },
+            "description": "This dataset contains deidentified subject level data from the study titled: Responses to Exposure to Low Levels of Concentrated Ambient Particles in Healthy Young Adults (RECAP). Subject, exposure, and health endpoint data are included in the dataset. Health endpoint data includes inflammatory, heart rate variability and cardiac repolarization, lung function, blood chemistry, and lipids measures. \n\nThis dataset is associated with the following publication:\nWyatt, L., R. Devlin, A. Rappold, and M. Case. Low levels of fine particulate matter increase vascular damage and reduce pulmonary function in young healthy adults.   Particle and Fibre Toxicology. BioMed Central Ltd, London,  UK, 17(1): 58, (2020).",
             "distribution": [
                 {
-                    "title": "ScienceHub_RECAP_deidentified.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518774/ScienceHub_RECAP_deidentified.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHub_RECAP_deidentified.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518774",
+            "keyword": [
+                "controlled human exposure",
+                "particulate matter air pollution"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-05-21",
-            "references": [
-                "https://doi.org/10.1186/s12989-020-00389-5"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129641,41 +129635,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12989-020-00389-5"
+            ],
+            "rights": null,
+            "title": "RECAP dataset: Subject, exposure, and health endpoint (blood, lipids, cardiac, and lung) data"
         },
         {
-            "title": "ConleyJustin_A-b5mz_Dataset_20201021",
-            "description": "This dataset is limited to the human counting values of multinucleated germ cells in treatment-blinded images of rat fetal testes conducted by EPA researcher Justin Conley for comparison by collaborators at Brown University to germ cell counts made using an automated method created by the collaborators. \n\nThis dataset is associated with the following publication:\nBell, S., A. Zsom, J. Conley, and D. Spade. Automated identification of multinucleated germ cells with U-Net.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 15(7): e0229967, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520770",
-            "keyword": [
-                "Phthalates",
-                "male reproductive development",
-                "testis pathology",
-                "automated high throughput methods"
-            ],
             "contactPoint": {
                 "fn": "Justin Conley",
                 "hasEmail": "mailto:conley.justin@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520770/documents/ConleyJustin_A-b5mz_Dataset_Dictionary_20201021.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This dataset is limited to the human counting values of multinucleated germ cells in treatment-blinded images of rat fetal testes conducted by EPA researcher Justin Conley for comparison by collaborators at Brown University to germ cell counts made using an automated method created by the collaborators. \n\nThis dataset is associated with the following publication:\nBell, S., A. Zsom, J. Conley, and D. Spade. Automated identification of multinucleated germ cells with U-Net.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 15(7): e0229967, (2020).",
             "distribution": [
                 {
-                    "title": "ConleyJustin_A-b5mz_Dataset_20201021.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520770/ConleyJustin_A-b5mz_Dataset_20201021.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ConleyJustin_A-b5mz_Dataset_20201021.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520770",
+            "keyword": [
+                "Phthalates",
+                "male reproductive development",
+                "testis pathology",
+                "automated high throughput methods"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-09",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0229967"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129686,43 +129682,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520770/documents/ConleyJustin_A-b5mz_Dataset_Dictionary_20201021.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0229967"
+            ],
+            "rights": null,
+            "title": "ConleyJustin_A-b5mz_Dataset_20201021"
         },
         {
-            "title": "EPIC/MODIS LAI Comparison Data",
-            "description": "This zip file contains the underlying data used to create all tables and figures within the manuscript. \n\nThis dataset is associated with the following publication:\nIiames, J., E. Cooter, D. Pilant, and Y. Shao. Comparison of EPIC-simulated and MODIS-derived Leaf Area Index (LAI) across multiple spatial scales.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 12(17): 2764, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1517788",
-            "keyword": [
-                "MODIS",
-                "LAI",
-                "leaf area index",
-                "EPIC",
-                "Environmental Policy Integrate Climate"
-            ],
             "contactPoint": {
                 "fn": "John Iiames",
                 "hasEmail": "mailto:iiames.john@epa.gov"
             },
+            "description": "This zip file contains the underlying data used to create all tables and figures within the manuscript. \n\nThis dataset is associated with the following publication:\nIiames, J., E. Cooter, D. Pilant, and Y. Shao. Comparison of EPIC-simulated and MODIS-derived Leaf Area Index (LAI) across multiple spatial scales.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 12(17): 2764, (2020).",
             "distribution": [
                 {
-                    "title": "Data_Figures.Tables.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517788/Data_Figures.Tables.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Data_Figures.Tables.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517788",
+            "keyword": [
+                "MODIS",
+                "LAI",
+                "leaf area index",
+                "EPIC",
+                "Environmental Policy Integrate Climate"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-20",
-            "references": [
-                "https://doi.org/10.3390/rs12172764"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129732,43 +129726,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/rs12172764"
+            ],
+            "rights": null,
+            "title": "EPIC/MODIS LAI Comparison Data"
         },
         {
-            "title": "Comparative toxicity of microcystin congeners in mice exposed by the oral route",
-            "description": "Physical and serum chemistry effects in mice due to a single oral dose of ten microcystin congeners at a variety of dose levels to determine health effects and a no observable effect level. \n\nThis dataset is associated with the following publications:\nChernoff, N. Comparative toxicology of microcystin congeners. U.S. Environmental Protection Agency, Washington, DC, USA.\nChernoff, N., D. Hill, J. Schmid, J. Lang, T. Le, A. Farthing, and H. Huang. The comparative toxicity of ten microcystin congeners administered orally to mice: Clinical effects and organ toxicity..   Toxins. MDPI AG, Basel,  SWITZERLAND, 12(6): 403, (2020).\nChernoff, N., D. Hill, J. Schmid, J. Lang, A. Farthing, and H. Huang. Dose-response study of microcystin congeners MCLR, MCLA, MCLY, MCRR, and MCYR administered orally to mice.   Toxins. MDPI AG, Basel,  SWITZERLAND, 13(2): 86, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519315",
-            "keyword": [
-                "cyanobacterial toxin",
-                "microcystins",
-                "toxicology",
-                "in vivo data",
-                "NOAEL"
-            ],
             "contactPoint": {
                 "fn": "Neil Chernoff",
                 "hasEmail": "mailto:chernoff.neil@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519315/documents/Data%20dictionary%20for%20MC%20Congener%20PO%20metadata.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Physical and serum chemistry effects in mice due to a single oral dose of ten microcystin congeners at a variety of dose levels to determine health effects and a no observable effect level. \n\nThis dataset is associated with the following publications:\nChernoff, N. Comparative toxicology of microcystin congeners. U.S. Environmental Protection Agency, Washington, DC, USA.\nChernoff, N., D. Hill, J. Schmid, J. Lang, T. Le, A. Farthing, and H. Huang. The comparative toxicity of ten microcystin congeners administered orally to mice: Clinical effects and organ toxicity..   Toxins. MDPI AG, Basel,  SWITZERLAND, 12(6): 403, (2020).\nChernoff, N., D. Hill, J. Schmid, J. Lang, A. Farthing, and H. Huang. Dose-response study of microcystin congeners MCLR, MCLA, MCLY, MCRR, and MCYR administered orally to mice.   Toxins. MDPI AG, Basel,  SWITZERLAND, 13(2): 86, (2021).",
             "distribution": [
                 {
-                    "title": "MC Congener PO Metadata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519315/MC%20Congener%20PO%20Metadata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MC Congener PO Metadata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519315",
+            "keyword": [
+                "cyanobacterial toxin",
+                "microcystins",
+                "toxicology",
+                "in vivo data",
+                "NOAEL"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-02-20",
-            "references": [
-                "https://doi.org/10.3390/toxins12060403",
-                "https://doi.org/10.3390/toxins13020086"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129779,48 +129774,47 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519315/documents/Data%20dictionary%20for%20MC%20Congener%20PO%20metadata.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.3390/toxins12060403",
+                "https://doi.org/10.3390/toxins13020086"
+            ],
+            "rights": null,
+            "title": "Comparative toxicity of microcystin congeners in mice exposed by the oral route"
         },
         {
-            "title": "Final Prenatal Dataset",
-            "description": "Full data tables presented in the Supplemental Information in Excel format. \n\nThis dataset is associated with the following publication:\nNilsen, F., J. Frank, and N. Tulve. A systematic review and meta-analysis investigating the relationship between exposures to chemical and non-chemical stressors during prenatal development and childhood externalizing behaviors.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 17(7): 2361, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1520131",
-            "keyword": [
-                "children",
-                "gestational",
-                "mental health",
-                "cortisol",
-                "psychosocial",
-                "well-being"
-            ],
             "contactPoint": {
                 "fn": "Nicolle Tulve",
                 "hasEmail": "mailto:tulve.nicolle@epa.gov"
             },
+            "description": "Full data tables presented in the Supplemental Information in Excel format. \n\nThis dataset is associated with the following publication:\nNilsen, F., J. Frank, and N. Tulve. A systematic review and meta-analysis investigating the relationship between exposures to chemical and non-chemical stressors during prenatal development and childhood externalizing behaviors.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 17(7): 2361, (2020).",
             "distribution": [
                 {
-                    "title": "https://www.mdpi.com/1660-4601/17/7/2361",
-                    "accessURL": "https://www.mdpi.com/1660-4601/17/7/2361"
+                    "accessURL": "https://www.mdpi.com/1660-4601/17/7/2361",
+                    "title": "https://www.mdpi.com/1660-4601/17/7/2361"
                 },
                 {
-                    "title": "Final Prenatal Exposure Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520131/Final%20Prenatal%20Exposure%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Final Prenatal Exposure Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520131",
+            "keyword": [
+                "children",
+                "gestational",
+                "mental health",
+                "cortisol",
+                "psychosocial",
+                "well-being"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-19",
-            "references": [
-                "https://doi.org/10.3390/ijerph17072361"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129830,45 +129824,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ijerph17072361"
+            ],
+            "rights": null,
+            "title": "Final Prenatal Dataset"
         },
         {
-            "title": "SMPSS GI Assessment",
-            "description": "Green infrastructure (GI) is widely recognized for reducing risk of flooding, improving water quality, and harvesting stormwater for potential future use.  GI can be an important part of a strategy used in urban planning to enhance sustainable development and urban resilience.  However, existing literature lacks a comprehensive assessment framework to evaluate GI performance in terms of promoting ecosystem functions and services for social-ecological system resilience.  We propose a scenario-based planning support system to assess the capacity of urban resilience by using a robust indicator set consisting of quantitative and qualitative measurements.  Green Infrastructure in Urban Resilience Planning Support System (GIUR-PSS) supports decision-making for GI planning through scenario comparisons with the urban resilience capacity index.  To demonstrate GIUR-PSS, we developed five scenarios for the Congress Run sub-watershed (Mill Creek watershed, Ohio, USA) to test common types of GI (rain barrels, rain gardens, detention basins, porous pavement, and open space).  Results show the open space scenario achieves the overall highest performance (GI Urban Resilience Index = 4.27/5).  To implement the open space scenario in our urban demonstration site, suitable vacant lots could be converted to greenspace (e.g., forest, detention basins, and low-impact recreation areas). GIUR-PSS is easy to replicate, customize, and apply to cities of different sizes to assess environmental, economic, and social benefits provided by different types of GI installations.\n\nAdditional data described in the manuscript are available through identified data sources indicated therein. \n\nThis dataset is associated with the following publication:\nFu, X., M. Hopton, and X. Wang. Assessment of green infrastructure performance through an urban resilience lens.   JOURNAL OF CLEANER PRODUCTION. Elsevier Science Ltd, New York, NY, USA, 289: 125146, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519010",
-            "keyword": [
-                "Green Infrastructure",
-                "scenario planning",
-                "stormwater management"
-            ],
             "contactPoint": {
                 "fn": "Matthew Hopton",
                 "hasEmail": "mailto:hopton.matthew@epa.gov"
             },
+            "description": "Green infrastructure (GI) is widely recognized for reducing risk of flooding, improving water quality, and harvesting stormwater for potential future use.  GI can be an important part of a strategy used in urban planning to enhance sustainable development and urban resilience.  However, existing literature lacks a comprehensive assessment framework to evaluate GI performance in terms of promoting ecosystem functions and services for social-ecological system resilience.  We propose a scenario-based planning support system to assess the capacity of urban resilience by using a robust indicator set consisting of quantitative and qualitative measurements.  Green Infrastructure in Urban Resilience Planning Support System (GIUR-PSS) supports decision-making for GI planning through scenario comparisons with the urban resilience capacity index.  To demonstrate GIUR-PSS, we developed five scenarios for the Congress Run sub-watershed (Mill Creek watershed, Ohio, USA) to test common types of GI (rain barrels, rain gardens, detention basins, porous pavement, and open space).  Results show the open space scenario achieves the overall highest performance (GI Urban Resilience Index = 4.27/5).  To implement the open space scenario in our urban demonstration site, suitable vacant lots could be converted to greenspace (e.g., forest, detention basins, and low-impact recreation areas). GIUR-PSS is easy to replicate, customize, and apply to cities of different sizes to assess environmental, economic, and social benefits provided by different types of GI installations.\n\nAdditional data described in the manuscript are available through identified data sources indicated therein. \n\nThis dataset is associated with the following publication:\nFu, X., M. Hopton, and X. Wang. Assessment of green infrastructure performance through an urban resilience lens.   JOURNAL OF CLEANER PRODUCTION. Elsevier Science Ltd, New York, NY, USA, 289: 125146, (2021).",
             "distribution": [
                 {
-                    "title": "F-B-indicators survey results v5 anon.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519010/F-B-indicators%20survey%20results%20v5%20anon.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "F-B-indicators survey results v5 anon.xlsx"
                 },
                 {
-                    "title": "FuzzyMembership.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519010/FuzzyMembership.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FuzzyMembership.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519010",
+            "keyword": [
+                "Green Infrastructure",
+                "scenario planning",
+                "stormwater management"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-12-31",
-            "references": [
-                "https://doi.org/10.1016/j.jclepro.2020.125146"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129878,45 +129872,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jclepro.2020.125146"
+            ],
+            "rights": null,
+            "title": "SMPSS GI Assessment"
         },
         {
-            "title": "Placenta ScienceHub Data (version 1)",
-            "description": "Data relative to the paper entitled \" Ozone-induced fetal growth restriction in rats is associated with sexually dimorphic placental and fetal metabolic adaptation.\". \n\nThis dataset is associated with the following publication:\nMiller, C., J. Dye, A. Henriquez, E. Stewart, K. Lavrich, G. Carswell, H. Ren, D. Freeborn, S. Snow, M.C. Schladweiler, J. Richards, P.R. Kodavanti, A. Fisher, B. Chorley, and U. Kodavanti. Ozone-induced fetal growth restriction in rats is associated with sexually dimorphic placental and fetal metabolic adaptation..   Molecular Metabolism. Elsevier B.V., Amsterdam,  NETHERLANDS, 20(42): 101094, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1520047",
-            "keyword": [
-                "Ozone",
-                "intrauterine growth restriction",
-                "children's health",
-                "Metabolism"
-            ],
             "contactPoint": {
                 "fn": "Urmila Kodavanti",
                 "hasEmail": "mailto:kodavanti.urmila@epa.gov"
             },
+            "description": "Data relative to the paper entitled \" Ozone-induced fetal growth restriction in rats is associated with sexually dimorphic placental and fetal metabolic adaptation.\". \n\nThis dataset is associated with the following publication:\nMiller, C., J. Dye, A. Henriquez, E. Stewart, K. Lavrich, G. Carswell, H. Ren, D. Freeborn, S. Snow, M.C. Schladweiler, J. Richards, P.R. Kodavanti, A. Fisher, B. Chorley, and U. Kodavanti. Ozone-induced fetal growth restriction in rats is associated with sexually dimorphic placental and fetal metabolic adaptation..   Molecular Metabolism. Elsevier B.V., Amsterdam,  NETHERLANDS, 20(42): 101094, (2020).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156859",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156859"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156859",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156859"
                 },
                 {
-                    "title": "Placenta ScienceHub Data (version 1).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520047/Placenta%20ScienceHub%20Data%20%28version%201%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Placenta ScienceHub Data (version 1).xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520047",
+            "keyword": [
+                "Ozone",
+                "intrauterine growth restriction",
+                "children's health",
+                "Metabolism"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-05",
-            "references": [
-                "https://doi.org/10.1016/j.molmet.2020.101094"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129926,42 +129920,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.molmet.2020.101094"
+            ],
+            "rights": null,
+            "title": "Placenta ScienceHub Data (version 1)"
         },
         {
-            "title": "Diet-O3-MS data",
-            "description": "Dataset for a study examining the cardiovascular effects from acute ozone exposure in rats fed with fish oil or olive oil diets. \n\nThis dataset is associated with the following publication:\nTong, H., S. Snow, M.C. Schladweiler, G. Carswell, B. Chorley, and U. Kodavanti. Fish Oil and Olive Oil-Enriched Diets Alleviate Acute Ozone-induced Cardiovascular Effects in Rats.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 409: 115296, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1520161",
-            "keyword": [
-                "diet",
-                "Ozone",
-                "fish oil",
-                "olive oil",
-                "cardiovascular effects"
-            ],
             "contactPoint": {
                 "fn": "Haiyan Tong",
                 "hasEmail": "mailto:tong.haiyan@epa.gov"
             },
+            "description": "Dataset for a study examining the cardiovascular effects from acute ozone exposure in rats fed with fish oil or olive oil diets. \n\nThis dataset is associated with the following publication:\nTong, H., S. Snow, M.C. Schladweiler, G. Carswell, B. Chorley, and U. Kodavanti. Fish Oil and Olive Oil-Enriched Diets Alleviate Acute Ozone-induced Cardiovascular Effects in Rats.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 409: 115296, (2020).",
             "distribution": [
                 {
-                    "title": "Diet-O3-MS data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520161/Diet-O3-MS%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Diet-O3-MS data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520161",
+            "keyword": [
+                "diet",
+                "Ozone",
+                "fish oil",
+                "olive oil",
+                "cardiovascular effects"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-27",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2020.115296"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -129971,60 +129965,70 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2020.115296"
+            ],
+            "rights": null,
+            "title": "Diet-O3-MS data"
         },
         {
-            "title": "Clean Air Status and Trends Network (CASTNET) Hourly Ozone Concentrations",
-            "description": "Ground-level ozone is measured at CASTNET sites following the guidelines in 40 Code of Federal Regulations (CFR) Parts 50 and 58. Continuous measurements are averaged to hourly concentrations. Data are reported to AirNow and EPA's Air Quality System (AQS) database routinely. There are more than 80 CASTNET sites reporting hourly ozone concentrations throughout the United States. Site location information is included with this dataset. The QAPP and associated SOPs can be found on the CASTNET website: www.epa.gov/castnet/documents-reports. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520792",
-            "keyword": [
-                "Clean Air Status and Trends Network (CASTNET)",
-                "air quality",
-                "ozone concentrations",
-                "national ambient air quality standards"
-            ],
             "contactPoint": {
                 "fn": "Melissa Puchalski",
                 "hasEmail": "mailto:puchalski.melissa@epa.gov"
             },
+            "description": "Ground-level ozone is measured at CASTNET sites following the guidelines in 40 Code of Federal Regulations (CFR) Parts 50 and 58. Continuous measurements are averaged to hourly concentrations. Data are reported to AirNow and EPA's Air Quality System (AQS) database routinely. There are more than 80 CASTNET sites reporting hourly ozone concentrations throughout the United States. Site location information is included with this dataset. The QAPP and associated SOPs can be found on the CASTNET website: www.epa.gov/castnet/documents-reports. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/ozone.zip",
-                    "accessURL": "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/ozone.zip"
+                    "accessURL": "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/ozone.zip",
+                    "title": "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/ozone.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520792",
+            "keyword": [
+                "Clean Air Status and Trends Network (CASTNET)",
+                "air quality",
+                "ozone concentrations",
+                "national ambient air quality standards"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-15",
-            "references": [
-                "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/site.zip",
-                "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/gas_calibration_web.zip"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. Environmental Protection Agency",
                 "subOrganizationOf": {
                     "name": "U.S. Government"
                 }
-            }
+            },
+            "references": [
+                "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/site.zip",
+                "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/gas_calibration_web.zip"
+            ],
+            "rights": null,
+            "title": "Clean Air Status and Trends Network (CASTNET) Hourly Ozone Concentrations"
         },
         {
-            "title": "MagnusonMatthew_A-0zpn_dataset_20210203.xlsx",
-            "description": "Data corresponding to graphs in the conference proceedings.\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Matthew Magnuson",
+                "hasEmail": "mailto:magnuson.matthew@epa.gov"
+            },
+            "description": "Data corresponding to graphs in the conference proceedings.\n",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520756/MagnusonMatthew_A-0zpn_dataset_20210203.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MagnusonMatthew_A-0zpn_dataset_20210203.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520756",
             "keyword": [
@@ -130035,19 +130039,11 @@
                 "cesium",
                 "radiological"
             ],
-            "contactPoint": {
-                "fn": "Matthew Magnuson",
-                "hasEmail": "mailto:magnuson.matthew@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MagnusonMatthew_A-0zpn_dataset_20210203.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520756/MagnusonMatthew_A-0zpn_dataset_20210203.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-05",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -130056,42 +130052,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "MagnusonMatthew_A-0zpn_dataset_20210203.xlsx"
         },
         {
-            "title": "Dry Dep Report Summary - 20190909 - NI42 (GOM Four Corners Data After Emissions Reductions)",
-            "description": "Smooth-edge surrogate surface passive sampling was again employed to measure Gaseous Oxidized Mercury (GOM) dry deposition during contiguous two-week integrated time periods from August 1, 2017-August 1, 2019.  Dry deposition of GOM was monitored at six sites in the Four Corners area. \n\nThis dataset is associated with the following publication:\nSather, M., S. Mukerjee, L. Smith, J. Mathew, C. Jackson, and M. Flournoy. Gaseous Oxidized Mercury Dry Deposition Measurements in the Four Corners Area, U.S.A., after Large Power Plant Mercury Emission Reductions.   Atmospheric Pollution Research. Turkish National Committee for Air Pollution Research and Control, Izmir,  TURKEY, 12(1): 148-158, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1518678",
-            "keyword": [
-                "air pollution",
-                "Arid Area",
-                "Gaseous Oxidized Mercury",
-                "Dry Deposition",
-                "Surrogate Surface Passive Sampling"
-            ],
             "contactPoint": {
                 "fn": "Shaibal Mukerjee",
                 "hasEmail": "mailto:mukerjee.shaibal@epa.gov"
             },
+            "description": "Smooth-edge surrogate surface passive sampling was again employed to measure Gaseous Oxidized Mercury (GOM) dry deposition during contiguous two-week integrated time periods from August 1, 2017-August 1, 2019.  Dry deposition of GOM was monitored at six sites in the Four Corners area. \n\nThis dataset is associated with the following publication:\nSather, M., S. Mukerjee, L. Smith, J. Mathew, C. Jackson, and M. Flournoy. Gaseous Oxidized Mercury Dry Deposition Measurements in the Four Corners Area, U.S.A., after Large Power Plant Mercury Emission Reductions.   Atmospheric Pollution Research. Turkish National Committee for Air Pollution Research and Control, Izmir,  TURKEY, 12(1): 148-158, (2021).",
             "distribution": [
                 {
-                    "title": "Dry Dep Report Summary - 20190909 - NI42.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518678/Dry%20Dep%20Report%20Summary%20-%2020190909%20-%20NI42.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Dry Dep Report Summary - 20190909 - NI42.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518678",
+            "keyword": [
+                "air pollution",
+                "Arid Area",
+                "Gaseous Oxidized Mercury",
+                "Dry Deposition",
+                "Surrogate Surface Passive Sampling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-09",
-            "references": [
-                "https://doi.org/10.1016/j.apr.2020.08.030"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130101,48 +130095,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apr.2020.08.030"
+            ],
+            "rights": null,
+            "title": "Dry Dep Report Summary - 20190909 - NI42 (GOM Four Corners Data After Emissions Reductions)"
         },
         {
-            "title": "Final_Wildland_Fire_Sensor_Challenge_Public_Data",
-            "description": "Wildland Fire Sensor Challenge Solver sensor system measurements and EPA reference method measurements (PM2.5, carbon monoxide, carbon dioxide, ozone) from Phase I EPA research chamber (Chapel Hill, NC) and Phase II U.S. Forest Service (Missoula, MT) combustion chamber testing. \n\nThis dataset is associated with the following publication:\nLandis, M., R. Long, J.D. Krug, M. Colon, R. Vanderpool, A. Habel, and S. Urbanski. The U.S. EPA Wildland Fire Sensor Challenge: Performance and Evaluation of Solver Submitted Multi-Pollutant Sensor Systems.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 247: NA, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1519318",
-            "keyword": [
-                "wildland fire smoke",
-                "sensor performance",
-                "particulate matter",
-                "carbon monoxide",
-                "carbon dioxide",
-                "Ozone"
-            ],
             "contactPoint": {
                 "fn": "Matthew Landis",
                 "hasEmail": "mailto:landis.matthew@epa.gov"
             },
+            "description": "Wildland Fire Sensor Challenge Solver sensor system measurements and EPA reference method measurements (PM2.5, carbon monoxide, carbon dioxide, ozone) from Phase I EPA research chamber (Chapel Hill, NC) and Phase II U.S. Forest Service (Missoula, MT) combustion chamber testing. \n\nThis dataset is associated with the following publication:\nLandis, M., R. Long, J.D. Krug, M. Colon, R. Vanderpool, A. Habel, and S. Urbanski. The U.S. EPA Wildland Fire Sensor Challenge: Performance and Evaluation of Solver Submitted Multi-Pollutant Sensor Systems.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 247: NA, (2021).",
             "distribution": [
                 {
-                    "title": "Final_phase_II_public_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519318/Final_phase_II_public_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Final_phase_II_public_data.xlsx"
                 },
                 {
-                    "title": "Final_phase_I_public_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519318/Final_phase_I_public_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Final_phase_I_public_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519318",
+            "keyword": [
+                "wildland fire smoke",
+                "sensor performance",
+                "particulate matter",
+                "carbon monoxide",
+                "carbon dioxide",
+                "Ozone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-02",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2020.118165"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130152,19 +130146,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2020.118165"
+            ],
+            "rights": null,
+            "title": "Final_Wildland_Fire_Sensor_Challenge_Public_Data"
         },
         {
-            "title": "Augustine, S. (2019). Data for Boquer\u00f3n Beach, Puerto Rico immunoconversion study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1503882",
-            "description": "Augustine, S. (2019). Data for Boquer\u00f3n Beach, Puerto Rico immunoconversion study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1503882\n\nAugustine, S. (2018). Data for Boquer\u00f3n Beach, PR immunoprevalence study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1390125. \n\nThis dataset is associated with the following publication:\nAugustine, S., T. Eason, K. Simmons, S. Griffin, C. Curioso, M. Ramudit, E. Sams, K. Oshima, A. Dufour, and T. Wade. Rapid Salivary IgG Antibody Screening for Hepatitis A.   JOURNAL OF CLINICAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 58(10): e00358-20, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Swinburne Augustine",
+                "hasEmail": "mailto:augustine.swinburne@epa.gov"
+            },
+            "describedBy": "https://sciencehub.epa.gov/sciencehub/distribution/3921/download",
+            "description": "Augustine, S. (2019). Data for Boquer\u00f3n Beach, Puerto Rico immunoconversion study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1503882\n\nAugustine, S. (2018). Data for Boquer\u00f3n Beach, PR immunoprevalence study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1390125. \n\nThis dataset is associated with the following publication:\nAugustine, S., T. Eason, K. Simmons, S. Griffin, C. Curioso, M. Ramudit, E. Sams, K. Oshima, A. Dufour, and T. Wade. Rapid Salivary IgG Antibody Screening for Hepatitis A.   JOURNAL OF CLINICAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 58(10): e00358-20, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.23719/1503882",
+                    "title": "https://doi.org/10.23719/1503882"
+                },
+                {
+                    "accessURL": "https://doi.org/10.23719/1503882",
+                    "title": "https://doi.org/10.23719/1503882"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520768/Journal%20of%20Clinical%20Microbiology-2020-Augustine-JCM.00358-20.full.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Journal of Clinical Microbiology-2020-Augustine-JCM.00358-20.full.pdf"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520768",
             "keyword": [
@@ -130183,28 +130196,10 @@
                 "cytokines",
                 "chemokines"
             ],
-            "contactPoint": {
-                "fn": "Swinburne Augustine",
-                "hasEmail": "mailto:augustine.swinburne@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.23719/1503882",
-                    "accessURL": "https://doi.org/10.23719/1503882"
-                },
-                {
-                    "title": "https://doi.org/10.23719/1503882",
-                    "accessURL": "https://doi.org/10.23719/1503882"
-                },
-                {
-                    "title": "Journal of Clinical Microbiology-2020-Augustine-JCM.00358-20.full.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520768/Journal%20of%20Clinical%20Microbiology-2020-Augustine-JCM.00358-20.full.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-09",
-            "references": [
-                "https://doi.org/10.1128/jcm.00358-20"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130215,19 +130210,33 @@
                     }
                 }
             },
-            "describedBy": "https://sciencehub.epa.gov/sciencehub/distribution/3921/download"
+            "references": [
+                "https://doi.org/10.1128/jcm.00358-20"
+            ],
+            "rights": null,
+            "title": "Augustine, S. (2019). Data for Boquer\u00f3n Beach, Puerto Rico immunoconversion study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1503882"
         },
         {
-            "title": "Augustine, S. (2018). Data for Boquer\u00f3n Beach, PR immunoprevalence study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1390125 ",
-            "description": "Augustine, S. (2018). Data for Boquer\u00f3n Beach, PR immunoprevalence study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1390125. \n\nThis dataset is associated with the following publications:\nAugustine, S., K. Simmons, T. Eason, C. Curioso, S. Griffin, T. Wade, A. Dufour, S. Fout, A. Grimm, K. Oshima, E. Sams, M. See, and L. Wymer. Immunoprevalence to Six Waterborne Pathogens in Beachgoers at Boquer\u00f3n Beach, Puerto Rico: Application of a Microsphere-Based Salivary Antibody Multiplex Immunoassay.   Frontiers in Public Health. Frontiers, Lausanne,  SWITZERLAND, 5(84): 1-11, (2017).\nAugustine, S., T. Eason, K. Simmons, S. Griffin, C. Curioso, M. Ramudit, E. Sams, K. Oshima, A. Dufour, and T. Wade. Rapid Salivary IgG Antibody Screening for Hepatitis A.   JOURNAL OF CLINICAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 58(10): e00358-20, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Swinburne Augustine",
+                "hasEmail": "mailto:augustine.swinburne@epa.gov"
+            },
+            "describedBy": "https://sciencehub.epa.gov/sciencehub/distribution/864/download",
+            "description": "Augustine, S. (2018). Data for Boquer\u00f3n Beach, PR immunoprevalence study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1390125. \n\nThis dataset is associated with the following publications:\nAugustine, S., K. Simmons, T. Eason, C. Curioso, S. Griffin, T. Wade, A. Dufour, S. Fout, A. Grimm, K. Oshima, E. Sams, M. See, and L. Wymer. Immunoprevalence to Six Waterborne Pathogens in Beachgoers at Boquer\u00f3n Beach, Puerto Rico: Application of a Microsphere-Based Salivary Antibody Multiplex Immunoassay.   Frontiers in Public Health. Frontiers, Lausanne,  SWITZERLAND, 5(84): 1-11, (2017).\nAugustine, S., T. Eason, K. Simmons, S. Griffin, C. Curioso, M. Ramudit, E. Sams, K. Oshima, A. Dufour, and T. Wade. Rapid Salivary IgG Antibody Screening for Hepatitis A.   JOURNAL OF CLINICAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 58(10): e00358-20, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.23719/1390125",
+                    "title": "https://doi.org/10.23719/1390125"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/2999/05-01-2017%20Frontiers%20article%20published.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "05-01-2017 Frontiers article published.pdf"
+                }
             ],
             "identifier": "A-3bkd-2999",
             "keyword": [
@@ -130246,25 +130255,10 @@
                 "cytokines",
                 "chemokines"
             ],
-            "contactPoint": {
-                "fn": "Swinburne Augustine",
-                "hasEmail": "mailto:augustine.swinburne@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.23719/1390125",
-                    "accessURL": "https://doi.org/10.23719/1390125"
-                },
-                {
-                    "title": "05-01-2017 Frontiers article published.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/2999/05-01-2017%20Frontiers%20article%20published.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-09",
-            "references": [
-                "https://doi.org/10.3389/fpubh.2017.00084",
-                "https://doi.org/10.1128/jcm.00358-20"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130275,19 +130269,29 @@
                     }
                 }
             },
-            "describedBy": "https://sciencehub.epa.gov/sciencehub/distribution/864/download"
+            "references": [
+                "https://doi.org/10.3389/fpubh.2017.00084",
+                "https://doi.org/10.1128/jcm.00358-20"
+            ],
+            "rights": null,
+            "title": "Augustine, S. (2018). Data for Boquer\u00f3n Beach, PR immunoprevalence study [Data set]. U.S. EPA Office of Research and Development (ORD). https://doi.org/10.23719/1390125 "
         },
         {
-            "title": "NaHRSI Scored Results",
-            "description": "Domains, Indicators and Metrics of NaHRSI and CRSI. \n\nThis dataset is associated with the following publication:\nSummers, K., L. Harwell, K. Buck, L. Smith, J. Harvey, D. Vivian, J. Bousquin, M. McLaughlin, and S. Hafner. Development of a Climate Resilience Screening Index (CRSI): An Assessment of Resilience to Acute Meteorological Events and Selected Natural Hazards. U.S. Environmental Protection Agency, Washington, DC, USA, 2017.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "James Summers",
+                "hasEmail": "mailto:summers.kevin@epa.gov"
+            },
+            "description": "Domains, Indicators and Metrics of NaHRSI and CRSI. \n\nThis dataset is associated with the following publication:\nSummers, K., L. Harwell, K. Buck, L. Smith, J. Harvey, D. Vivian, J. Bousquin, M. McLaughlin, and S. Hafner. Development of a Climate Resilience Screening Index (CRSI): An Assessment of Resilience to Acute Meteorological Events and Selected Natural Hazards. U.S. Environmental Protection Agency, Washington, DC, USA, 2017.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503667/Summers_etal_GeoHealth2_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Summers_etal_GeoHealth2_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503667",
             "keyword": [
@@ -130298,20 +130302,10 @@
                 "Vulnerability",
                 "natural hazards."
             ],
-            "contactPoint": {
-                "fn": "James Summers",
-                "hasEmail": "mailto:summers.kevin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Summers_etal_GeoHealth2_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503667/Summers_etal_GeoHealth2_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-28",
-            "references": [
-                "https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P100SSN6.txt"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130321,42 +130315,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P100SSN6.txt"
+            ],
+            "rights": null,
+            "title": "NaHRSI Scored Results"
         },
         {
-            "title": "Connecting Channels 2014 - 2015 Water Quality Data - 8/15/2018",
-            "description": "These results include water chemistry data collected in the St. Marys River and Huron-Erie Corridor in 2014 - 2016. \n\nThis dataset is associated with the following publication:\nWick, M., T. Angradi, M. Pawlowski, D. Bolgrien, J. Launspach, J. Kiddon, and M. Nord. A synoptic assessment of water quality in two Great Lakes connecting channels.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 45(5): 901-911, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1502555",
-            "keyword": [
-                "Laurentian Great Lakes",
-                "St. Marys River",
-                "Huron-Erie Corridor",
-                "water quality",
-                "ecosystem assessment"
-            ],
             "contactPoint": {
                 "fn": "Molly Wick",
                 "hasEmail": "mailto:wick.molly@epa.gov"
             },
+            "description": "These results include water chemistry data collected in the St. Marys River and Huron-Erie Corridor in 2014 - 2016. \n\nThis dataset is associated with the following publication:\nWick, M., T. Angradi, M. Pawlowski, D. Bolgrien, J. Launspach, J. Kiddon, and M. Nord. A synoptic assessment of water quality in two Great Lakes connecting channels.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 45(5): 901-911, (2019).",
             "distribution": [
                 {
-                    "title": "ConnectingChannelsWQdata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502555/ConnectingChannelsWQdata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ConnectingChannelsWQdata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502555",
+            "keyword": [
+                "Laurentian Great Lakes",
+                "St. Marys River",
+                "Huron-Erie Corridor",
+                "water quality",
+                "ecosystem assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-08-15",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2019.08.001"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130366,40 +130360,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2019.08.001"
+            ],
+            "rights": null,
+            "title": "Connecting Channels 2014 - 2015 Water Quality Data - 8/15/2018"
         },
         {
-            "title": "The Alginate Immobilization of Metabolic Enzymes (AIME) Platform Retrofits an Estrogen Receptor Transactivation Assay with Metabolic Competence",
-            "description": "The objective of this study was to develop an approach to retrofit existing HTS assays with hepatic metabolism. The Alginate Immobilization of Metabolic Enzymes (AIME) platform encapsulates hepatic S9 fractions in alginate microspheres attached to 96-well peg lids. Functional characterization across a panel of reference substrates for phase I cytochrome P450 enzymes revealed substrate depletion with expected metabolite accumulation. Performance of the AIME method in the VM7Luc estrogen receptor (ER) transactivation assay was evaluated across 15 reference chemicals and 48 test chemicals that yield metabolites previously identified as ER active or inactive. \n\nThis dataset is associated with the following publication:\nDeisenroth, C., D. DeGroot, T. Zurlinden, A. Eicher, J. McCord, M. Lee, P. Carmichael, and R. Thomas. The Alginate Immobilization of Metabolic Enzymes Platform Retrofits an Estrogen Receptor Transactivation Assay with Metabolic Competence.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  178(2): 281-301, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1518903",
-            "keyword": [
-                "high-throughput screening",
-                "xenobiotic metabolism",
-                "estrogen receptor",
-                "endocrine toxicology"
-            ],
             "contactPoint": {
                 "fn": "Chad Deisenroth",
                 "hasEmail": "mailto:deisenroth.chad@epa.gov"
             },
+            "description": "The objective of this study was to develop an approach to retrofit existing HTS assays with hepatic metabolism. The Alginate Immobilization of Metabolic Enzymes (AIME) platform encapsulates hepatic S9 fractions in alginate microspheres attached to 96-well peg lids. Functional characterization across a panel of reference substrates for phase I cytochrome P450 enzymes revealed substrate depletion with expected metabolite accumulation. Performance of the AIME method in the VM7Luc estrogen receptor (ER) transactivation assay was evaluated across 15 reference chemicals and 48 test chemicals that yield metabolites previously identified as ER active or inactive. \n\nThis dataset is associated with the following publication:\nDeisenroth, C., D. DeGroot, T. Zurlinden, A. Eicher, J. McCord, M. Lee, P. Carmichael, and R. Thomas. The Alginate Immobilization of Metabolic Enzymes Platform Retrofits an Estrogen Receptor Transactivation Assay with Metabolic Competence.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  178(2): 281-301, (2020).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.5061/dryad.r2280gbb7",
-                    "accessURL": "https://doi.org/10.5061/dryad.r2280gbb7"
+                    "accessURL": "https://doi.org/10.5061/dryad.r2280gbb7",
+                    "title": "https://doi.org/10.5061/dryad.r2280gbb7"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518903",
+            "keyword": [
+                "high-throughput screening",
+                "xenobiotic metabolism",
+                "estrogen receptor",
+                "endocrine toxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-08-24",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfaa147"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130409,41 +130403,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfaa147"
+            ],
+            "rights": null,
+            "title": "The Alginate Immobilization of Metabolic Enzymes (AIME) Platform Retrofits an Estrogen Receptor Transactivation Assay with Metabolic Competence"
         },
         {
-            "title": "TREE BOX PERFORMANCE IN EXFILTRATING STORMWATER RUNOFF",
-            "description": "This study determines the exfiltration rates in six tree boxes and analyzes their performance over time. The study site is in Louisville, KY, where we monitored the performance of six tree boxes and other stormwater control measures (SCMs).  Each tree box is 1.5 m wide, 1.5 m long, and 1.8 m deep.  Street and parking lot runoff enters tree boxes though a curb cut. A 46-cm diameter shaft was drilled at the bottom of each tree box to reach the underlying permeable soil layer.  A pressure transducer installed at the bottom of the shaft measured the water level depth and water temperature. From the water level data, the exfiltration rate of six tree boxes was calculated for 121 rain events.  For each rain event the exfiltration rate was calculated at different water levels inside the shaft. The effects of water level inside the shaft, temperature, and age on the exfiltration rate were analyzed. Exfiltration rate increased with water level and exfiltration rate in first year is significantly larger than second year. Overall in second year the decrease in geometric mean exfiltration rate was largest for moderate depth. The exfiltration rate of the tree boxes is significantly larger for warmer rain events and significantly smaller for cooler rain events. This paper highlights the use of continuous two years\u2019 water level monitoring data to quantify the potential for local recharge via exfiltration, and the effect of different parameter on the exfiltration rate of six tree boxes. \n\nThis dataset is associated with the following publication:\nAhmed, F., and M. Borst. TREE BOX PERFORMANCE IN EXFILTRATING STORMWATER RUNOFF.   WATER ENVIRONMENT RESEARCH. Water Environment Federation, Alexandria, VA, USA, 92(1): 106-114, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407665",
-            "keyword": [
-                "Exfiltration",
-                "Pressure transducer",
-                "Seasonal effect",
-                "Stormwater control measure"
-            ],
             "contactPoint": {
                 "fn": "Michael Borst",
                 "hasEmail": "mailto:borst.mike@epa.gov"
             },
+            "description": "This study determines the exfiltration rates in six tree boxes and analyzes their performance over time. The study site is in Louisville, KY, where we monitored the performance of six tree boxes and other stormwater control measures (SCMs).  Each tree box is 1.5 m wide, 1.5 m long, and 1.8 m deep.  Street and parking lot runoff enters tree boxes though a curb cut. A 46-cm diameter shaft was drilled at the bottom of each tree box to reach the underlying permeable soil layer.  A pressure transducer installed at the bottom of the shaft measured the water level depth and water temperature. From the water level data, the exfiltration rate of six tree boxes was calculated for 121 rain events.  For each rain event the exfiltration rate was calculated at different water levels inside the shaft. The effects of water level inside the shaft, temperature, and age on the exfiltration rate were analyzed. Exfiltration rate increased with water level and exfiltration rate in first year is significantly larger than second year. Overall in second year the decrease in geometric mean exfiltration rate was largest for moderate depth. The exfiltration rate of the tree boxes is significantly larger for warmer rain events and significantly smaller for cooler rain events. This paper highlights the use of continuous two years\u2019 water level monitoring data to quantify the potential for local recharge via exfiltration, and the effect of different parameter on the exfiltration rate of six tree boxes. \n\nThis dataset is associated with the following publication:\nAhmed, F., and M. Borst. TREE BOX PERFORMANCE IN EXFILTRATING STORMWATER RUNOFF.   WATER ENVIRONMENT RESEARCH. Water Environment Federation, Alexandria, VA, USA, 92(1): 106-114, (2020).",
             "distribution": [
                 {
-                    "title": "Raw data for all tree boxes.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407665/Raw%20data%20for%20all%20tree%20boxes.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Raw data for all tree boxes.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407665",
+            "keyword": [
+                "Exfiltration",
+                "Pressure transducer",
+                "Seasonal effect",
+                "Stormwater control measure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-05-31",
-            "references": [
-                "https://doi.org/10.1002/wer.1189"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130453,19 +130447,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/wer.1189"
+            ],
+            "rights": null,
+            "title": "TREE BOX PERFORMANCE IN EXFILTRATING STORMWATER RUNOFF"
         },
         {
-            "title": "Web-based Tool of The Non-potable Environmental and Economic Water Reuse Calculator (NEWR) ",
-            "description": "The methods and resource of the dataset",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Xin Ma",
+                "hasEmail": "mailto:ma.cissy@epa.gov"
+            },
+            "description": "The methods and resource of the dataset",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/water-research/onsite-non-potable-water-reuse-research",
+                    "title": "https://www.epa.gov/water-research/onsite-non-potable-water-reuse-research"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520873",
             "keyword": [
@@ -130478,18 +130481,11 @@
                 "Life Cycle Cost",
                 "greywater reuse"
             ],
-            "contactPoint": {
-                "fn": "Xin Ma",
-                "hasEmail": "mailto:ma.cissy@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/water-research/onsite-non-potable-water-reuse-research",
-                    "accessURL": "https://www.epa.gov/water-research/onsite-non-potable-water-reuse-research"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-19",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -130498,19 +130494,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Web-based Tool of The Non-potable Environmental and Economic Water Reuse Calculator (NEWR) "
         },
         {
-            "title": "THI dataset for ScienceHubJSerrano",
-            "description": "Thiacloprid (THI) is a neonicotinoid insecticide of interest to the USEPA due to its low absorption by crops, greater distribution into the surrounding areas, and potential for adverse effect to terrestrial and aquatic organisms. Prior to this report, there was very limited information addressing the ex vivo metabolism of THI by fish species and the metabolic pathways regulating its potential adverse effects. The in vitro and ex vivo biotransformation pathway of THI is defined by the formation of three primary metabolites (TM1, TM2 and TM3) via separate paths differentiated by reductive decyanation, reductive dechlorination with hydration and dealkylation processes, respectively. Kinetic rates were calculated for the rat microsomal decyanation of THI into TM1 (Km=299.2 \u00b5M and Vmax=5.3 pmol/min/mg), and for the dealkylation of THI into TM3 (Km=368.9 \u00b5M \u00b5M and Vmax=3.95 pmol/min/mg). Formation confirmation and identity inference of THI metabolites in absence of standards was achieved by LC-UV and High Resolution-MS strategies. It was concluded that the in vitro and ex vivo metabolic products of THI are conserved both across species (rat and RBT) and levels of biological organization (microsomes and liver slices), as previously reported for the neonicotinoid insecticides Imidacloprid and Acetamiprid. \n\nThis dataset is associated with the following publication:\nSerrano, J., R. Kolanczyk, B. Blackwell, B. Sheedy, and M. Tapper. In vitro metabolism assessment of thiacloprid in rainbow trout and rat by LC-UV and high resolution-mass spectrometry.   XENOBIOTICA. Taylor & Francis, Inc., Philadelphia, PA, USA, 51(5): 536-548, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Jose Serrano",
+                "hasEmail": "mailto:serrano.jose@epa.gov"
+            },
+            "description": "Thiacloprid (THI) is a neonicotinoid insecticide of interest to the USEPA due to its low absorption by crops, greater distribution into the surrounding areas, and potential for adverse effect to terrestrial and aquatic organisms. Prior to this report, there was very limited information addressing the ex vivo metabolism of THI by fish species and the metabolic pathways regulating its potential adverse effects. The in vitro and ex vivo biotransformation pathway of THI is defined by the formation of three primary metabolites (TM1, TM2 and TM3) via separate paths differentiated by reductive decyanation, reductive dechlorination with hydration and dealkylation processes, respectively. Kinetic rates were calculated for the rat microsomal decyanation of THI into TM1 (Km=299.2 \u00b5M and Vmax=5.3 pmol/min/mg), and for the dealkylation of THI into TM3 (Km=368.9 \u00b5M \u00b5M and Vmax=3.95 pmol/min/mg). Formation confirmation and identity inference of THI metabolites in absence of standards was achieved by LC-UV and High Resolution-MS strategies. It was concluded that the in vitro and ex vivo metabolic products of THI are conserved both across species (rat and RBT) and levels of biological organization (microsomes and liver slices), as previously reported for the neonicotinoid insecticides Imidacloprid and Acetamiprid. \n\nThis dataset is associated with the following publication:\nSerrano, J., R. Kolanczyk, B. Blackwell, B. Sheedy, and M. Tapper. In vitro metabolism assessment of thiacloprid in rainbow trout and rat by LC-UV and high resolution-mass spectrometry.   XENOBIOTICA. Taylor & Francis, Inc., Philadelphia, PA, USA, 51(5): 536-548, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518527/THI%20dataset%20for%20ScienceHubJSerrano.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "THI dataset for ScienceHubJSerrano.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518527",
             "keyword": [
@@ -130523,20 +130527,10 @@
                 "Rat",
                 "HPLC-HR MS"
             ],
-            "contactPoint": {
-                "fn": "Jose Serrano",
-                "hasEmail": "mailto:serrano.jose@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "THI dataset for ScienceHubJSerrano.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518527/THI%20dataset%20for%20ScienceHubJSerrano.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-24",
-            "references": [
-                "https://doi.org/10.1080/00498254.2020.1840658"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130546,19 +130540,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/00498254.2020.1840658"
+            ],
+            "rights": null,
+            "title": "THI dataset for ScienceHubJSerrano"
         },
         {
-            "title": "Data Mining Applied to Life Cycle Inventory Modeling for Cumene and Sodium Hydroxide Manufacturing, Version 1, 09/2018",
-            "description": "This file contains the life cycle inventories (LCIs) developed for an associated journal article. Potential users of the data are referred to the journal article for a full description of the modeling methodology. LCIs were developed for cumene and sodium hydroxide manufacturing using data mining with metadata-based data preprocessing. The inventory data were collected from US EPA's 2012 Chemical Data Reporting database, 2011 National Emissions Inventory, 2011 Toxics Release Inventory, 2011 Electronic Greenhouse Gas Reporting Tool, 2011 Discharge Monitoring Report, and the 2011 Biennial Report generated from the RCRAinfo hazardous waste tracking system. \n\nThe U.S. average cumene gate-to-gate inventories are provided without (baseline) and with process allocation applied using metadata-based filtering. In 2011, there were 8 facilities reporting public production volumes of cumene in the U.S., totaling to 2,609,309,687 kilograms of cumene produced that year.\n\nThe U.S. average sodium hydroxide gate-to-gate inventories are also provided without (baseline) and with process allocation applied using metadata-based filtering. In 2011, there were 24 facilities reporting public production volumes of sodium hydroxide in the U.S., totaling to 3,878,021,614 kilograms of sodium hydroxide produced that year. Process allocation was only conducted for the top 12 facilities producing sodium hydroxide, which represents 97% of the public production of sodium hydroxide.\n\nThe data have not been compiled in the formal Federal Commons LCI Template to avoid users interpreting the template to mean the data have been fully reviewed according to LCA standards and can be directly applied to all types of assessments and decision needs without additional review by industry and potential stakeholders. \n\nThis dataset is associated with the following publication:\nMeyer, D.E., S. Cashman, and A. Gaglione. Improving the reliability of chemical manufacturing life cycle inventory constructed using secondary data.   JOURNAL OF INDUSTRIAL ECOLOGY. Berkeley Electronic Press, Berkeley, CA, USA, 25(1): 20-35, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "David Meyer",
+                "hasEmail": "mailto:meyer.david@epa.gov"
+            },
+            "description": "This file contains the life cycle inventories (LCIs) developed for an associated journal article. Potential users of the data are referred to the journal article for a full description of the modeling methodology. LCIs were developed for cumene and sodium hydroxide manufacturing using data mining with metadata-based data preprocessing. The inventory data were collected from US EPA's 2012 Chemical Data Reporting database, 2011 National Emissions Inventory, 2011 Toxics Release Inventory, 2011 Electronic Greenhouse Gas Reporting Tool, 2011 Discharge Monitoring Report, and the 2011 Biennial Report generated from the RCRAinfo hazardous waste tracking system. \n\nThe U.S. average cumene gate-to-gate inventories are provided without (baseline) and with process allocation applied using metadata-based filtering. In 2011, there were 8 facilities reporting public production volumes of cumene in the U.S., totaling to 2,609,309,687 kilograms of cumene produced that year.\n\nThe U.S. average sodium hydroxide gate-to-gate inventories are also provided without (baseline) and with process allocation applied using metadata-based filtering. In 2011, there were 24 facilities reporting public production volumes of sodium hydroxide in the U.S., totaling to 3,878,021,614 kilograms of sodium hydroxide produced that year. Process allocation was only conducted for the top 12 facilities producing sodium hydroxide, which represents 97% of the public production of sodium hydroxide.\n\nThe data have not been compiled in the formal Federal Commons LCI Template to avoid users interpreting the template to mean the data have been fully reviewed according to LCA standards and can be directly applied to all types of assessments and decision needs without additional review by industry and potential stakeholders. \n\nThis dataset is associated with the following publication:\nMeyer, D.E., S. Cashman, and A. Gaglione. Improving the reliability of chemical manufacturing life cycle inventory constructed using secondary data.   JOURNAL OF INDUSTRIAL ECOLOGY. Berkeley Electronic Press, Berkeley, CA, USA, 25(1): 20-35, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503030/MeyerEtAl_DataMining_CaseStudyInventories.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MeyerEtAl_DataMining_CaseStudyInventories.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503030",
             "keyword": [
@@ -130570,20 +130574,10 @@
                 "data mining",
                 "chemical manufacturing"
             ],
-            "contactPoint": {
-                "fn": "David Meyer",
-                "hasEmail": "mailto:meyer.david@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MeyerEtAl_DataMining_CaseStudyInventories.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503030/MeyerEtAl_DataMining_CaseStudyInventories.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-19",
-            "references": [
-                "https://doi.org/10.1111/jiec.13044"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130593,20 +130587,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/jiec.13044"
+            ],
+            "rights": null,
+            "title": "Data Mining Applied to Life Cycle Inventory Modeling for Cumene and Sodium Hydroxide Manufacturing, Version 1, 09/2018"
         },
         {
-            "title": "NOAA Data",
-            "description": "Data owner is Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. This dataset is not publicly accessible because: Data is property of NOAA. It can be accessed through the following means: Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. Format: Data is raster format and table format. \n\nThis dataset is associated with the following publication:\nMishra, S., R. Stumpf, B. Schaeffer, J. Werdell, K. Loftin, and A. Meredith. Evaluation of a satellite-based cyanobacteria bloom detection algorithm using field-measured microcystin data.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 774: 145462, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Blake Schaeffer",
+                "hasEmail": "mailto:schaeffer.blake@epa.gov"
+            },
+            "description": "Data owner is Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. This dataset is not publicly accessible because: Data is property of NOAA. It can be accessed through the following means: Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. Format: Data is raster format and table format. \n\nThis dataset is associated with the following publication:\nMishra, S., R. Stumpf, B. Schaeffer, J. Werdell, K. Loftin, and A. Meredith. Evaluation of a satellite-based cyanobacteria bloom detection algorithm using field-measured microcystin data.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 774: 145462, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1519418",
             "keyword": [
                 "satellite",
@@ -130616,14 +130614,10 @@
                 "water quality",
                 "health"
             ],
-            "contactPoint": {
-                "fn": "Blake Schaeffer",
-                "hasEmail": "mailto:schaeffer.blake@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-09-01",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2021.145462"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130633,42 +130627,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2021.145462"
+            ],
+            "rights": null,
+            "title": "NOAA Data"
         },
         {
-            "title": "Brumfield et al 20xx_Data Set",
-            "description": "Log10 fecal score ratios for eligible microbial source tracking qPCR assays. \n\nThis dataset is associated with the following publication:\nBrumfield, K.D., J.A. Cotruvo, O. Shanks, M. Sivaganesan, J. Hey, N.A. Hasan, A. Huq, R.R. Colwell, and M.B. Leddy. Metagenomic Sequencing and Quantitative Real-Time PCR for Fecal Pollution Assessment in an Urban Watershed.   Frontiers in Water. Frontiers, Lausanne,  SWITZERLAND, 3: 626849, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1519140",
-            "keyword": [
-                "metagenomics",
-                "fecal indicator bacteria",
-                "Microbial Source Tracking",
-                "qPCR",
-                "stormwater"
-            ],
             "contactPoint": {
                 "fn": "Orin Shanks",
                 "hasEmail": "mailto:shanks.orin@epa.gov"
             },
+            "description": "Log10 fecal score ratios for eligible microbial source tracking qPCR assays. \n\nThis dataset is associated with the following publication:\nBrumfield, K.D., J.A. Cotruvo, O. Shanks, M. Sivaganesan, J. Hey, N.A. Hasan, A. Huq, R.R. Colwell, and M.B. Leddy. Metagenomic Sequencing and Quantitative Real-Time PCR for Fecal Pollution Assessment in an Urban Watershed.   Frontiers in Water. Frontiers, Lausanne,  SWITZERLAND, 3: 626849, (2021).",
             "distribution": [
                 {
-                    "title": "Brumfield et al 20xx_Data Set.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519140/Brumfield%20et%20al%2020xx_Data%20Set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Brumfield et al 20xx_Data Set.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519140",
+            "keyword": [
+                "metagenomics",
+                "fecal indicator bacteria",
+                "Microbial Source Tracking",
+                "qPCR",
+                "stormwater"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-25",
-            "references": [
-                "https://doi.org/10.3389/frwa.2021.626849"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130678,19 +130672,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/frwa.2021.626849"
+            ],
+            "rights": null,
+            "title": "Brumfield et al 20xx_Data Set"
         },
         {
-            "title": "The Tox21 10K Compound Library: Part 1 - Collaborative chemistry advancing toxicology",
-            "description": "Table S1: Tox21 IDs mapped to NCGC IDs, PubChem IDs, and DSSTox IDs, and indicating NCATS, NTP and EPA partner library associations (date stamped February 24, 2020). Table S2: DSSTox TOX21SL list of substance IDs and structure formula, molecular weight, SMILES, InChI, and QSAR-ready SMILES (downloaded January 24, 2020). Table S3: DSSTox TOX21SL DTXSID overlaps with EPA CompTox Dashboard lists (downloaded January 24, 2020). Table S4: Predicted physicochemical properties and toxicities generated from OPERA, T.E.S.T, CORINA, and Derek Nexus models. Table S5: ToxPrint (V2.0_r711) fingerprint file for the TOX21SL chemical list. Table S6: Chemotype enrichment workflow results generated from binarized activity hit calls for ToxCast and Tox21 assay end points (aeids) obtained from EPA\u2019s public ToxCast database, invitroDBv2. Table S7: Tox21 binarized assay hit call matrix for stereo and salt pairs, extracted from EPA\u2019s public ToxCast database, invitroDBv3. \n\nThis dataset is associated with the following publication:\nRichard, A., R. Huang, S. Waidyanatha, P. Shinn, B.J. Collins, I. Thillainadarajah, C. Grulke, A. Williams, R. Lougee, R. Judson, K. Houck, M.A. Shobair, C. Yang, J.F. Rathman, A. Yasgar, S.C. Fitzpatrick, A. Simeonov, R. Thomas, K.M. Crofton, R.S. Paules, J.R. Bucher, C.P. Austin, R.J. Kavlock, and R.R. Tice. The Tox21 10K Compound Library: Collaborative Chemistry Advancing Toxicology.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 34(2): 189-216, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Grace Patlewicz",
+                "hasEmail": "mailto:patlewicz.grace@epa.gov"
+            },
+            "description": "Table S1: Tox21 IDs mapped to NCGC IDs, PubChem IDs, and DSSTox IDs, and indicating NCATS, NTP and EPA partner library associations (date stamped February 24, 2020). Table S2: DSSTox TOX21SL list of substance IDs and structure formula, molecular weight, SMILES, InChI, and QSAR-ready SMILES (downloaded January 24, 2020). Table S3: DSSTox TOX21SL DTXSID overlaps with EPA CompTox Dashboard lists (downloaded January 24, 2020). Table S4: Predicted physicochemical properties and toxicities generated from OPERA, T.E.S.T, CORINA, and Derek Nexus models. Table S5: ToxPrint (V2.0_r711) fingerprint file for the TOX21SL chemical list. Table S6: Chemotype enrichment workflow results generated from binarized activity hit calls for ToxCast and Tox21 assay end points (aeids) obtained from EPA\u2019s public ToxCast database, invitroDBv2. Table S7: Tox21 binarized assay hit call matrix for stereo and salt pairs, extracted from EPA\u2019s public ToxCast database, invitroDBv3. \n\nThis dataset is associated with the following publication:\nRichard, A., R. Huang, S. Waidyanatha, P. Shinn, B.J. Collins, I. Thillainadarajah, C. Grulke, A. Williams, R. Lougee, R. Judson, K. Houck, M.A. Shobair, C. Yang, J.F. Rathman, A. Yasgar, S.C. Fitzpatrick, A. Simeonov, R. Thomas, K.M. Crofton, R.S. Paules, J.R. Bucher, C.P. Austin, R.J. Kavlock, and R.R. Tice. The Tox21 10K Compound Library: Collaborative Chemistry Advancing Toxicology.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 34(2): 189-216, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519349/SupportingInformation_TablesS1-S7_rev.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SupportingInformation_TablesS1-S7_rev.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1519349",
             "keyword": [
@@ -130709,20 +130713,10 @@
                 "curated data",
                 "Models"
             ],
-            "contactPoint": {
-                "fn": "Grace Patlewicz",
-                "hasEmail": "mailto:patlewicz.grace@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SupportingInformation_TablesS1-S7_rev.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519349/SupportingInformation_TablesS1-S7_rev.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-13",
-            "references": [
-                "https://doi.org/10.1021/acs.chemrestox.0c00264"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130732,50 +130726,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.chemrestox.0c00264"
+            ],
+            "rights": null,
+            "title": "The Tox21 10K Compound Library: Part 1 - Collaborative chemistry advancing toxicology"
         },
         {
-            "title": "Data contributed by EPA/ORD/CEMM/AESMD to the manuscript \"Four decades of United States mobile source pollutants: spatial-temporal trends assessed by ground-based monitors, air quality models, and satellites\"",
-            "description": "Files containing daily average NO, NO2, CO, and EC concentrations simulated by WRF/CMAQ at 36 km resolution for the time period 1990 \u2013 2010. These data were contributed by EPA/ORD/CEMM/AESMD researchers to the manuscript \u201cFour decades of United States mobile source pollutants: spatial-temporal trends assessed by ground-based monitors, air quality models, and satellites\u201d. Portions of this dataset are inaccessible because: Data files have now been uploaded. They can be accessed through the following means: Data files have now been uploaded. Format: Data files have now been uploaded. \n\nThis dataset is associated with the following publication:\nHenneman, L., H. Shen, C. Hogrefe, A. Russell, and C. Zigler. Four Decades of United States Mobile Source Pollutants: Spatial\u2013Temporal Trends Assessed by Ground-Based Monitors, Air Quality Models, and Satellites.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(2): 882-892, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520084",
-            "keyword": [
-                "traffic-related air pollution",
-                "CMAQ",
-                "remote sensing",
-                "Air quality trends"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520084/documents/HogrefeChristian_A-98sx_Data_Dictionary_20201223.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Files containing daily average NO, NO2, CO, and EC concentrations simulated by WRF/CMAQ at 36 km resolution for the time period 1990 \u2013 2010. These data were contributed by EPA/ORD/CEMM/AESMD researchers to the manuscript \u201cFour decades of United States mobile source pollutants: spatial-temporal trends assessed by ground-based monitors, air quality models, and satellites\u201d. Portions of this dataset are inaccessible because: Data files have now been uploaded. They can be accessed through the following means: Data files have now been uploaded. Format: Data files have now been uploaded. \n\nThis dataset is associated with the following publication:\nHenneman, L., H. Shen, C. Hogrefe, A. Russell, and C. Zigler. Four Decades of United States Mobile Source Pollutants: Spatial\u2013Temporal Trends Assessed by Ground-Based Monitors, Air Quality Models, and Satellites.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(2): 882-892, (2021).",
             "distribution": [
                 {
-                    "title": "https://drive.google.com/drive/folders/1icGCTT8kFhEzbzIBWtwufeXoJRAHOPWT",
-                    "accessURL": "https://drive.google.com/drive/folders/1icGCTT8kFhEzbzIBWtwufeXoJRAHOPWT"
+                    "accessURL": "https://drive.google.com/drive/folders/1icGCTT8kFhEzbzIBWtwufeXoJRAHOPWT",
+                    "title": "https://drive.google.com/drive/folders/1icGCTT8kFhEzbzIBWtwufeXoJRAHOPWT"
                 },
                 {
-                    "title": "hr2day_dailyavg_doe36km_2000_2010.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520084/hr2day_dailyavg_doe36km_2000_2010.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "hr2day_dailyavg_doe36km_2000_2010.zip"
                 },
                 {
-                    "title": "hr2day_dailyavg_doe36km_1990_1999.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520084/hr2day_dailyavg_doe36km_1990_1999.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "hr2day_dailyavg_doe36km_1990_1999.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520084",
+            "keyword": [
+                "traffic-related air pollution",
+                "CMAQ",
+                "remote sensing",
+                "Air quality trends"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-30",
-            "references": [
-                "https://doi.org/10.1021/acs.est.0c07128"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130786,48 +130782,46 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520084/documents/HogrefeChristian_A-98sx_Data_Dictionary_20201223.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/acs.est.0c07128"
+            ],
+            "rights": null,
+            "title": "Data contributed by EPA/ORD/CEMM/AESMD to the manuscript \"Four decades of United States mobile source pollutants: spatial-temporal trends assessed by ground-based monitors, air quality models, and satellites\""
         },
         {
-            "title": "Evaluation of quantitative structure property relationship algorithms for predicting plasma protein binding in humans-UW-QSPR-Supplementary data",
-            "description": "Observed fup data obtained from the literature; SMILES structures obtained from Pubchem SDF files. \n\nThis dataset is associated with the following publication:\nYun, Y.E., R. Tornero-Velez, T. Purucker, D. Chang, and A.N. Edginton. Evaluation of Quantitative Structure Property Relationship algorithms for predicting plasma protein binding in humans.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 17: 100142, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520781",
-            "keyword": [
-                "PubChem",
-                "cheminformatics",
-                "QSPR",
-                "plasma protein binding",
-                "Environmentally Relevant"
-            ],
             "contactPoint": {
                 "fn": "Rogelio Tornero-Velez",
                 "hasEmail": "mailto:tornero-velez.rogelio@epa.gov"
             },
+            "description": "Observed fup data obtained from the literature; SMILES structures obtained from Pubchem SDF files. \n\nThis dataset is associated with the following publication:\nYun, Y.E., R. Tornero-Velez, T. Purucker, D. Chang, and A.N. Edginton. Evaluation of Quantitative Structure Property Relationship algorithms for predicting plasma protein binding in humans.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 17: 100142, (2021).",
             "distribution": [
                 {
-                    "title": "Supplement Data 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520781/Supplement%20Data%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplement Data 2.xlsx"
                 },
                 {
-                    "title": "Supplement Data 1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520781/Supplement%20Data%201.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplement Data 1.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520781",
+            "keyword": [
+                "PubChem",
+                "cheminformatics",
+                "QSPR",
+                "plasma protein binding",
+                "Environmentally Relevant"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-27",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2020.100142"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130837,39 +130831,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2020.100142"
+            ],
+            "rights": null,
+            "title": "Evaluation of quantitative structure property relationship algorithms for predicting plasma protein binding in humans-UW-QSPR-Supplementary data"
         },
         {
-            "title": "The Residential Population Generator (RPGen): A tool to parameterize residential, demographic, and physiological data to model intraindividual exposure, dose, and risk",
-            "description": "This repository contains scripts, input files, and some example output files for the Residential Population Generator, an R-based tool to generate synthetic human residental populations to use in making estimates of near-field chemical exposures. This tool is most readily adapted for using in the workflow for CHEM, the Combined Human Exposure Model, avaialable in two other GitHub repositories in the HumanExposure project, including ProductUseScheduler and source2dose. CHEM is currently best suited to estimating exposure to product use. Outputs from RPGen are translated into ProductUseScheduler, which with subsequent outputs used in source2dose. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520861",
-            "keyword": [
-                "PBPK models",
-                "exposure and dose models",
-                "new approach methodologies",
-                "computational toxicology"
-            ],
             "contactPoint": {
                 "fn": "Daniel Vallero",
                 "hasEmail": "mailto:vallero.daniel@epa.gov"
             },
+            "description": "This repository contains scripts, input files, and some example output files for the Residential Population Generator, an R-based tool to generate synthetic human residental populations to use in making estimates of near-field chemical exposures. This tool is most readily adapted for using in the workflow for CHEM, the Combined Human Exposure Model, avaialable in two other GitHub repositories in the HumanExposure project, including ProductUseScheduler and source2dose. CHEM is currently best suited to estimating exposure to product use. Outputs from RPGen are translated into ProductUseScheduler, which with subsequent outputs used in source2dose. ",
             "distribution": [
                 {
-                    "title": "https://github.com/HumanExposure/RPGen",
-                    "accessURL": "https://github.com/HumanExposure/RPGen"
+                    "accessURL": "https://github.com/HumanExposure/RPGen",
+                    "title": "https://github.com/HumanExposure/RPGen"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520861",
+            "keyword": [
+                "PBPK models",
+                "exposure and dose models",
+                "new approach methodologies",
+                "computational toxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-01-08",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -130878,20 +130874,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "The Residential Population Generator (RPGen): A tool to parameterize residential, demographic, and physiological data to model intraindividual exposure, dose, and risk"
         },
         {
-            "title": "Water temperature trends",
-            "description": "Water temperature trends. This dataset is not publicly accessible because: Data is the property of HydroShare. It can be accessed through the following means: https://www.hydroshare.org/. Format: CUASHI HydroShare. \n\nThis dataset is associated with the following publication:\nKelleher, C., H. Golden, and S. Archfield. Monthly River Temperature Trends Across the US Confound Annual Changes.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 16(10): 104006, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Heather Golden",
+                "hasEmail": "mailto:golden.heather@epa.gov"
+            },
+            "description": "Water temperature trends. This dataset is not publicly accessible because: Data is the property of HydroShare. It can be accessed through the following means: https://www.hydroshare.org/. Format: CUASHI HydroShare. \n\nThis dataset is associated with the following publication:\nKelleher, C., H. Golden, and S. Archfield. Monthly River Temperature Trends Across the US Confound Annual Changes.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 16(10): 104006, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520773",
             "keyword": [
                 "stream temperature",
@@ -130901,14 +130899,10 @@
                 "water quality",
                 "river temperature"
             ],
-            "contactPoint": {
-                "fn": "Heather Golden",
-                "hasEmail": "mailto:golden.heather@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-02-10",
-            "references": [
-                "https://doi.org/10.1088/1748-9326/ac2289"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130918,20 +130912,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1748-9326/ac2289"
+            ],
+            "rights": null,
+            "title": "Water temperature trends"
         },
         {
-            "title": "Dataset for Ebullition dominates methane fluxes from the water surface across different ecohydrological patches in a temperate freshwater marsh",
-            "description": "Dataset for Ebullition dominates methane fluxes from the water surface across different ecohydrological patches in a temperate freshwater marsh. This dataset is not publicly accessible because: Data is property of Ohio State University. It can be accessed through the following means: Jorge A. Villa, School of Geosciences. University of Louisiana at Lafayette, Lafayette, LA, 70504, USA. Format: Data will be made available at National estuarine research Centralized Data Management Office (http://cdmo.baruch.sc.edu/get/landing.cfm) and the ESS-DiVE  repository. \n\nThis dataset is associated with the following publication:\nVilla, J.A., Y. Ju, T. Yazbeck, S. Waldo, K.C. Wrighton, and G. Bohrer. Ebullition dominates methane fluxes from the water surface across different ecohydrological patches in a temperate freshwater marsh at the end of the growing season.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 767: 144498, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Jake Beaulieu",
+                "hasEmail": "mailto:beaulieu.jake@epa.gov"
+            },
+            "description": "Dataset for Ebullition dominates methane fluxes from the water surface across different ecohydrological patches in a temperate freshwater marsh. This dataset is not publicly accessible because: Data is property of Ohio State University. It can be accessed through the following means: Jorge A. Villa, School of Geosciences. University of Louisiana at Lafayette, Lafayette, LA, 70504, USA. Format: Data will be made available at National estuarine research Centralized Data Management Office (http://cdmo.baruch.sc.edu/get/landing.cfm) and the ESS-DiVE  repository. \n\nThis dataset is associated with the following publication:\nVilla, J.A., Y. Ju, T. Yazbeck, S. Waldo, K.C. Wrighton, and G. Bohrer. Ebullition dominates methane fluxes from the water surface across different ecohydrological patches in a temperate freshwater marsh at the end of the growing season.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 767: 144498, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1519408",
             "keyword": [
                 "wetland",
@@ -130939,14 +130937,10 @@
                 "GRTS",
                 "ebullition"
             ],
-            "contactPoint": {
-                "fn": "Jake Beaulieu",
-                "hasEmail": "mailto:beaulieu.jake@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-09-21",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2020.144498"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -130956,19 +130950,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2020.144498"
+            ],
+            "rights": null,
+            "title": "Dataset for Ebullition dominates methane fluxes from the water surface across different ecohydrological patches in a temperate freshwater marsh"
         },
         {
-            "title": "A cross-platform approach to characterize and screen potential neurovascular unit toxicants",
-            "description": "Development of the neurovascular unit (NVU) is a complex, multistage process that requires orchestrated cell signaling mechanisms across several cell types and ultimately results in the formation of the blood-brain barrier. Typical high-throughput screening (HTS) assays investigate single biochemical or single cell responses following chemical insult. As the NVU comprises multiple cell types interacting at various stages of development, a methodology for combining high-throughput results across pertinent cell-based assays is needed to investigate potential chemical-induced disruption to the development of this complex cell system. To this end, we developed a novel method for screening putative NVU disruptors across diverse assay platforms to predict chemical perturbation of the developing NVU. Here, HTS assay results measuring chemical-induced perturbations to cellular key events across angiogenic and neurogenic outcomes were combined to create a cell-based prioritization of NVU hazard. Using activity from each biological outcome, chemicals were grouped into similar modes of action and used to train a logistic regression literature model. This model utilizes the chemical-specific pairwise mutual information score for PubMed MeSH annotations to represent how often a chemical was shown to produce a specific outcome in the published literature space. Taken together, this study presents a methodology to investigate NVU developmental hazard using cell-based HTS assays and literature evidence to prioritize screening of putative NVU disruptors. The results from these screening efforts demonstrate how chemicals that represent a range of putative vascular disrupting compound (pVDC) scores based on angiogenic endpoints can also produce effects on neurogenic outcomes such as neurite outgrowth, neuroprogenitor/neural crest migration, representing an additional method for understanding the range of possible modes of action for disruption of the developing NVU. \n\nThis dataset is associated with the following publication:\nZurlinden, T., K. Saili, N. Baker, T. Toimela, T. Heinonen, and T. Knudsen. A cross-platform approach to characterize and screen potential neurovascular unit toxicants.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 96(September 2020): 300-315, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Thomas Knudsen",
+                "hasEmail": "mailto:knudsen.thomas@epa.gov"
+            },
+            "description": "Development of the neurovascular unit (NVU) is a complex, multistage process that requires orchestrated cell signaling mechanisms across several cell types and ultimately results in the formation of the blood-brain barrier. Typical high-throughput screening (HTS) assays investigate single biochemical or single cell responses following chemical insult. As the NVU comprises multiple cell types interacting at various stages of development, a methodology for combining high-throughput results across pertinent cell-based assays is needed to investigate potential chemical-induced disruption to the development of this complex cell system. To this end, we developed a novel method for screening putative NVU disruptors across diverse assay platforms to predict chemical perturbation of the developing NVU. Here, HTS assay results measuring chemical-induced perturbations to cellular key events across angiogenic and neurogenic outcomes were combined to create a cell-based prioritization of NVU hazard. Using activity from each biological outcome, chemicals were grouped into similar modes of action and used to train a logistic regression literature model. This model utilizes the chemical-specific pairwise mutual information score for PubMed MeSH annotations to represent how often a chemical was shown to produce a specific outcome in the published literature space. Taken together, this study presents a methodology to investigate NVU developmental hazard using cell-based HTS assays and literature evidence to prioritize screening of putative NVU disruptors. The results from these screening efforts demonstrate how chemicals that represent a range of putative vascular disrupting compound (pVDC) scores based on angiogenic endpoints can also produce effects on neurogenic outcomes such as neurite outgrowth, neuroprogenitor/neural crest migration, representing an additional method for understanding the range of possible modes of action for disruption of the developing NVU. \n\nThis dataset is associated with the following publication:\nZurlinden, T., K. Saili, N. Baker, T. Toimela, T. Heinonen, and T. Knudsen. A cross-platform approach to characterize and screen potential neurovascular unit toxicants.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 96(September 2020): 300-315, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518764/SupplWorkbook.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SupplWorkbook.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518764",
             "keyword": [
@@ -130980,20 +130984,10 @@
                 "virtual tissues",
                 "tipping points"
             ],
-            "contactPoint": {
-                "fn": "Thomas Knudsen",
-                "hasEmail": "mailto:knudsen.thomas@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SupplWorkbook.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518764/SupplWorkbook.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-01",
-            "references": [
-                "https://doi.org/10.1016/j.reprotox.2020.06.010"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131003,39 +130997,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.reprotox.2020.06.010"
+            ],
+            "rights": null,
+            "title": "A cross-platform approach to characterize and screen potential neurovascular unit toxicants"
         },
         {
-            "title": "Respirometric Screening and Characterization of Mitochondrial Toxicants Within the ToxCast Phase I and II Chemical Libraries",
-            "description": "These are the raw data files for TOXSCI manuscript 19-0578 entitled, \u201cRespirometric Screening and Characterization of Mitochondrial Toxicants Within the ToxCast Phase I and II Chemical Libraries\u201d:\nDescription from readme.txt file:\n\n1) sc_seahorse.lvl0.merged.data.csv- contains all mapped raw OCR data from tier 1 single-concentration RSA screening of 1,042 Toxcast Phase I and II chemicals\n\n2) mc_seahorse.lvl0.merged.data.csv- contains all mapped raw OCR data from tier 2 multi-concentration RSA screening of 249 actives from tier 1\n\n3) EFA.lvl0.merged.data.csv- contains all mapped raw OCR data from tier 3 EFA screening of 149 putative electron transport chain inhibitors\n\n4) mc5_mc6_ncct_mito_nov2019.csv- level 5 and 6 outputs from ToxCast pipeline (tcpl) analysis\n\n5) RawMC3_ToxCast_by_aeid.csv- level 3 tcpl outputs for all mitochondrial ToxCast assays\n\n6) RawMC5_ToxCast_by_aeid.csv- level 5 tcpl outputs for all mitochondrial ToxCast assays\n\n7) ref.set.chems.csv- sixty reference chemicals used to compared assay performance\n\n8) study_code.R- R script used to analyze data and generate figures and tables. \n\nThis dataset is associated with the following publication:\nHallinger, D., H. Lindsay, K. Friedman, D. Suarez, and S. Simmons. Respirometric Screening and Characterization of Mitochondrial Toxicants Within the ToxCast Phase I and II Chemical Libraries.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  176(1): 175-192, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504436",
-            "keyword": [
-                "ToxCast",
-                "High throughput screening"
-            ],
             "contactPoint": {
                 "fn": "Steven Simmons",
                 "hasEmail": "mailto:simmons.steve@epa.gov"
             },
+            "description": "These are the raw data files for TOXSCI manuscript 19-0578 entitled, \u201cRespirometric Screening and Characterization of Mitochondrial Toxicants Within the ToxCast Phase I and II Chemical Libraries\u201d:\nDescription from readme.txt file:\n\n1) sc_seahorse.lvl0.merged.data.csv- contains all mapped raw OCR data from tier 1 single-concentration RSA screening of 1,042 Toxcast Phase I and II chemicals\n\n2) mc_seahorse.lvl0.merged.data.csv- contains all mapped raw OCR data from tier 2 multi-concentration RSA screening of 249 actives from tier 1\n\n3) EFA.lvl0.merged.data.csv- contains all mapped raw OCR data from tier 3 EFA screening of 149 putative electron transport chain inhibitors\n\n4) mc5_mc6_ncct_mito_nov2019.csv- level 5 and 6 outputs from ToxCast pipeline (tcpl) analysis\n\n5) RawMC3_ToxCast_by_aeid.csv- level 3 tcpl outputs for all mitochondrial ToxCast assays\n\n6) RawMC5_ToxCast_by_aeid.csv- level 5 tcpl outputs for all mitochondrial ToxCast assays\n\n7) ref.set.chems.csv- sixty reference chemicals used to compared assay performance\n\n8) study_code.R- R script used to analyze data and generate figures and tables. \n\nThis dataset is associated with the following publication:\nHallinger, D., H. Lindsay, K. Friedman, D. Suarez, and S. Simmons. Respirometric Screening and Characterization of Mitochondrial Toxicants Within the ToxCast Phase I and II Chemical Libraries.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  176(1): 175-192, (2020).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.5061/dryad.zkh189367",
-                    "accessURL": "https://doi.org/10.5061/dryad.zkh189367"
+                    "accessURL": "https://doi.org/10.5061/dryad.zkh189367",
+                    "title": "https://doi.org/10.5061/dryad.zkh189367"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504436",
+            "keyword": [
+                "ToxCast",
+                "High throughput screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-31",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfaa059",
-                "https://doi.org/10.23645/epacomptox.12123735"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131045,80 +131038,80 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfaa059",
+                "https://doi.org/10.23645/epacomptox.12123735"
+            ],
+            "rights": null,
+            "title": "Respirometric Screening and Characterization of Mitochondrial Toxicants Within the ToxCast Phase I and II Chemical Libraries"
         },
         {
-            "title": "Biochar 4 Crops",
-            "description": "Raw data files for study of the effects of biochar on growth and elemental content of four crops: carrot, lettuce, soybean and sweetcorn.  Plus additional files on biochar and soil characteristics. \n\nThis dataset is associated with the following publications:\nOlszyk, D., T. Shiroyama, J.M. Novak, K.B. Cantrell, G. Sigua, D.W. Watts, and M. Johnson. Biochar affects growth and shoot nitrogen in four crops for two soils.   Agrosystems, Geosciences & Environment. John Wiley & Sons, Inc., Hoboken, NJ, USA,  e20067, (2020).\nOlszyk, D.M., T. Shiroyama, J.M. Novak, K.B. Cantrell, G. Sigua, D.W. Watts, and M.G. Johnson. Biochar Affects Essential Elements of Carrot Taproots and Lettuce Leaves.   HORTSCIENCE. American Society for Horticultural Science,    55(2): 261-271, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1503192",
-            "keyword": [
-                "carrot",
-                "lettuce",
-                "soybean",
-                "sweet corn",
-                "feedstock",
-                "pyrolysis temperature",
-                "plant growth",
-                "plant nutrients",
-                "biochar",
-                "soil",
-                "plants",
-                "remediation"
-            ],
             "contactPoint": {
                 "fn": "Mark Johnson",
                 "hasEmail": "mailto:johnson.markg@epa.gov"
             },
+            "description": "Raw data files for study of the effects of biochar on growth and elemental content of four crops: carrot, lettuce, soybean and sweetcorn.  Plus additional files on biochar and soil characteristics. \n\nThis dataset is associated with the following publications:\nOlszyk, D., T. Shiroyama, J.M. Novak, K.B. Cantrell, G. Sigua, D.W. Watts, and M. Johnson. Biochar affects growth and shoot nitrogen in four crops for two soils.   Agrosystems, Geosciences & Environment. John Wiley & Sons, Inc., Hoboken, NJ, USA,  e20067, (2020).\nOlszyk, D.M., T. Shiroyama, J.M. Novak, K.B. Cantrell, G. Sigua, D.W. Watts, and M.G. Johnson. Biochar Affects Essential Elements of Carrot Taproots and Lettuce Leaves.   HORTSCIENCE. American Society for Horticultural Science,    55(2): 261-271, (2020).",
             "distribution": [
                 {
-                    "title": "Corn SH Revised 012920.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503192/Corn%20SH%20Revised%20012920.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Corn SH Revised 012920.xls"
                 },
                 {
-                    "title": "Soybean SH Revised 012920.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503192/Soybean%20SH%20Revised%20012920.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Soybean SH Revised 012920.xls"
                 },
                 {
-                    "title": "Biochar Germination Study Biochar pH EC P.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503192/Biochar%20Germination%20Study%20Biochar%20pH%20EC%20P.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biochar Germination Study Biochar pH EC P.xlsx"
                 },
                 {
-                    "title": "Soil Elements Coxville Norfolk for SH 012920.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503192/Soil%20Elements%20Coxville%20Norfolk%20for%20SH%20012920.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Soil Elements Coxville Norfolk for SH 012920.xlsx"
                 },
                 {
-                    "title": "Carrot SH Revised 012920.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503192/Carrot%20SH%20Revised%20012920.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Carrot SH Revised 012920.xls"
                 },
                 {
-                    "title": "Lettuce SH 012920.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503192/Lettuce%20SH%20012920.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Lettuce SH 012920.xls"
                 },
                 {
-                    "title": "Biochar Chemical Analysis SH Unit Change 012920.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503192/Biochar%20Chemical%20Analysis%20SH%20Unit%20Change%20012920.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biochar Chemical Analysis SH Unit Change 012920.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503192",
+            "keyword": [
+                "carrot",
+                "lettuce",
+                "soybean",
+                "sweet corn",
+                "feedstock",
+                "pyrolysis temperature",
+                "plant growth",
+                "plant nutrients",
+                "biochar",
+                "soil",
+                "plants",
+                "remediation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-29",
-            "references": [
-                "https://doi.org/10.1002/agg2.20067",
-                "https://doi.org/10.21273/hortsci14421-19"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131128,20 +131121,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/agg2.20067",
+                "https://doi.org/10.21273/hortsci14421-19"
+            ],
+            "rights": null,
+            "title": "Biochar 4 Crops"
         },
         {
-            "title": "Impact of wildfire on particulate matter in the southeastern United States in November 2016",
-            "description": "a study about wild fire in the US in 2016. This dataset is not publicly accessible because: too large to be uploaded. It can be accessed through the following means: please contact David Wong at wong.david-c@epa.gov. Format: newftp.epa.gov/EPADataCommons/ORD/CEMM-AESMD/DavidWong/July2020. \n\nThis dataset is associated with the following publication:\nGuan, S., D. Wong, Y. Gao, T. Zhang, and G. Pouliot. Impact of wildfire on particulate matter in the southeastern United States in November 2016.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 724(1): 138354, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Cheung Wong",
+                "hasEmail": "mailto:wong.david-c@epa.gov"
+            },
+            "description": "a study about wild fire in the US in 2016. This dataset is not publicly accessible because: too large to be uploaded. It can be accessed through the following means: please contact David Wong at wong.david-c@epa.gov. Format: newftp.epa.gov/EPADataCommons/ORD/CEMM-AESMD/DavidWong/July2020. \n\nThis dataset is associated with the following publication:\nGuan, S., D. Wong, Y. Gao, T. Zhang, and G. Pouliot. Impact of wildfire on particulate matter in the southeastern United States in November 2016.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 724(1): 138354, (2020).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1518723",
             "keyword": [
                 "wildfire",
@@ -131149,14 +131147,10 @@
                 "Southeastern USA",
                 "Aerosol direct effects"
             ],
-            "contactPoint": {
-                "fn": "Cheung Wong",
-                "hasEmail": "mailto:wong.david-c@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-03",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2020.138354"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131166,20 +131160,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2020.138354"
+            ],
+            "rights": null,
+            "title": "Impact of wildfire on particulate matter in the southeastern United States in November 2016"
         },
         {
-            "title": "Fates of Nanoparticles in Simulated Gastric Fluid Studied using Single-Particle-Inductively Coupled Plasma-Mass Spectrometry",
-            "description": "This study adds to the growing knowledge of the fates of ENPs under conditions that simulate the human stomach. The fates of different nanoparticles after exposure to a simulated human digestion system is highly relevant to understand the impact of ENPs overall as they become more integrated into daily life, potentially resulting in increased exposures. Various factors such as species, size, the concentration of ingested ENPs, and body temperature on the fates of nanoparticles in the human digestion system proved to be varied and complex. This research highlights the need for a better understanding of nanomaterials' properties in the digestive system under other physiologically relevant conditions. This work contributes to an improved understanding of the fates of ENPs in gastric fluid, which gives insights into the gastrointestinal uptake of these ENPs before they enter into the blood circulation and organ systems. It is especially crucial for nanoparticles not completely solubilized in the digestive system's physiological contact time because these ENPs will enter into the other body systems and potentially circulate through the body as particulates. Using this study framework, sequentially studying in other tissues, especially for those ENPs not dissolved in SGF, including Ag-NPs, Au-NPs, and CeO\u00ac2\u2013NPs, would be valuable to evaluate the potential risk of ENPs to human health. This dataset is not publicly accessible because: The research continued, additional papers could be published from this data set. It can be accessed through the following means: Data will be placed in EPA file server. Format: Data is on spreadsheet, which includes dissolution rate of engineered nanoparticles of different particle size in simulated gastric fluid. \n\nThis dataset is associated with the following publication:\nHe, X., H. Zhang, H. Shi, W. Liu, and E. Sahle-Demessie. Fates of Au, Ag, ZnO, and CeO2 Nanoparticles in Simulated Gastric Fluid Studied using Single-Particle-Inductively Coupled Plasma-Mass Spectrometry.   JOURNAL OF THE AMERICAN SOCIETY FOR MASS SPECTROMETRY. Elsevier Science Ltd, New York, NY, USA, 31(10): 2180-2190, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Endalkac Sahle-Demessie",
+                "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520892/documents/Data%20Dictionary_FateEngineeredNanoparticlee.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This study adds to the growing knowledge of the fates of ENPs under conditions that simulate the human stomach. The fates of different nanoparticles after exposure to a simulated human digestion system is highly relevant to understand the impact of ENPs overall as they become more integrated into daily life, potentially resulting in increased exposures. Various factors such as species, size, the concentration of ingested ENPs, and body temperature on the fates of nanoparticles in the human digestion system proved to be varied and complex. This research highlights the need for a better understanding of nanomaterials' properties in the digestive system under other physiologically relevant conditions. This work contributes to an improved understanding of the fates of ENPs in gastric fluid, which gives insights into the gastrointestinal uptake of these ENPs before they enter into the blood circulation and organ systems. It is especially crucial for nanoparticles not completely solubilized in the digestive system's physiological contact time because these ENPs will enter into the other body systems and potentially circulate through the body as particulates. Using this study framework, sequentially studying in other tissues, especially for those ENPs not dissolved in SGF, including Ag-NPs, Au-NPs, and CeO\u00ac2\u2013NPs, would be valuable to evaluate the potential risk of ENPs to human health. This dataset is not publicly accessible because: The research continued, additional papers could be published from this data set. It can be accessed through the following means: Data will be placed in EPA file server. Format: Data is on spreadsheet, which includes dissolution rate of engineered nanoparticles of different particle size in simulated gastric fluid. \n\nThis dataset is associated with the following publication:\nHe, X., H. Zhang, H. Shi, W. Liu, and E. Sahle-Demessie. Fates of Au, Ag, ZnO, and CeO2 Nanoparticles in Simulated Gastric Fluid Studied using Single-Particle-Inductively Coupled Plasma-Mass Spectrometry.   JOURNAL OF THE AMERICAN SOCIETY FOR MASS SPECTROMETRY. Elsevier Science Ltd, New York, NY, USA, 31(10): 2180-2190, (2020).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520892",
             "keyword": [
                 "Nanoparticles",
@@ -131187,14 +131187,10 @@
                 "simulated gastric fluid (SGF)",
                 "ingestion exposure"
             ],
-            "contactPoint": {
-                "fn": "Endalkac Sahle-Demessie",
-                "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-07-21",
-            "references": [
-                "https://doi.org/10.1021/jasms.0c00278"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131205,21 +131201,23 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520892/documents/Data%20Dictionary_FateEngineeredNanoparticlee.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/jasms.0c00278"
+            ],
+            "rights": null,
+            "title": "Fates of Nanoparticles in Simulated Gastric Fluid Studied using Single-Particle-Inductively Coupled Plasma-Mass Spectrometry"
         },
         {
-            "title": "Laboratory Data From Ghana Water Testing for E-coli",
-            "description": "There is no dataset uploaded. Data is from a non-EPA source. This dataset is not publicly accessible because: Data is with Lakhdar Boukerrou of the Florida International University, FIU and the Ghana Water Company Limited. It can be accessed through the following means: Email :Lakhdar Boukerrou <lboukerr@fiu.edu> and mark ayertey <markayertey@yahoo.com>. Format: Detection rate for e-coli performed @the Ghana lab",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Julius Enriquez",
+                "hasEmail": "mailto:enriquez.julius@epa.gov"
+            },
+            "description": "There is no dataset uploaded. Data is from a non-EPA source. This dataset is not publicly accessible because: Data is with Lakhdar Boukerrou of the Florida International University, FIU and the Ghana Water Company Limited. It can be accessed through the following means: Email :Lakhdar Boukerrou <lboukerr@fiu.edu> and mark ayertey <markayertey@yahoo.com>. Format: Detection rate for e-coli performed @the Ghana lab",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520515",
             "keyword": [
                 "drinking water quality",
@@ -131230,13 +131228,11 @@
                 "West Africa",
                 "Ghana"
             ],
-            "contactPoint": {
-                "fn": "Julius Enriquez",
-                "hasEmail": "mailto:enriquez.julius@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-11-23",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -131245,42 +131241,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Laboratory Data From Ghana Water Testing for E-coli"
         },
         {
-            "title": "Monoassociation with bacterial isolates reveals the role of colonization, community complexity and abundance on locomotor behavior in larval zebrafish",
-            "description": "Across taxa, animals with depleted intestinal microbiomes show disrupted behavioral phenotypes. Axenic (i.e., microbe-free) mice, zebrafish, and fruit flies exhibit increased locomotor behavior, or hyperactivity. The mechanism through which bacteria interact with host cells to trigger normal neurobehavioral development in larval zebrafish is unknown. Here, we monoassociated zebrafish with either one of six different zebrafish-associated bacteria, mixtures of these host-associates, or with an environmental bacterial isolate. We found that while the axenic cohort was hyperactive, monoassociation with three different host-associated bacterial species, as well as with the mixtures, resulted in control-like locomotor behavior. Monoassociation with one host-associate and the environmental isolate resulted in the hyperactive phenotype characteristic of axenic larvae, while monoassociation with two other host-associated bacteria partially blocked this phenotype. Furthermore, we found an intriguing inverse relationship between the total concentration of bacteria per larvae and locomotor behavior. These data support a growing body of evidence that individual species of bacteria can have different effects on host behavior, potentially related to their success at intestinal colonization. Specific to the zebrafish model, our results suggest that differences in the composition of microbes in fish facilities could have profound effects on the outcomes of behavioral and pharmacological studies. \n\nThis dataset is associated with the following publication:\nWeitekamp, C., A. Kvasnicka, S. Keely, N. Brinkman, X. Howey, S. Gaballah, D. Phelps, T. Catron, T. Zurlinden, E. Wheaton, and T. Tal. Monoassociation with bacterial isolates reveals the role of colonization, community complexity and abundance on locomotor behavior in larval zebrafish.   Animal Microbiome. BioMed Central Ltd, London,  UK, 3(12): 1-13, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1518372",
-            "keyword": [
-                "zebrafish",
-                "germ-free",
-                "microbiome",
-                "hyperactivity",
-                "locomotor behavior"
-            ],
             "contactPoint": {
                 "fn": "Chelsea Weitekamp",
                 "hasEmail": "mailto:weitekamp.chelsea@epa.gov"
             },
+            "description": "Across taxa, animals with depleted intestinal microbiomes show disrupted behavioral phenotypes. Axenic (i.e., microbe-free) mice, zebrafish, and fruit flies exhibit increased locomotor behavior, or hyperactivity. The mechanism through which bacteria interact with host cells to trigger normal neurobehavioral development in larval zebrafish is unknown. Here, we monoassociated zebrafish with either one of six different zebrafish-associated bacteria, mixtures of these host-associates, or with an environmental bacterial isolate. We found that while the axenic cohort was hyperactive, monoassociation with three different host-associated bacterial species, as well as with the mixtures, resulted in control-like locomotor behavior. Monoassociation with one host-associate and the environmental isolate resulted in the hyperactive phenotype characteristic of axenic larvae, while monoassociation with two other host-associated bacteria partially blocked this phenotype. Furthermore, we found an intriguing inverse relationship between the total concentration of bacteria per larvae and locomotor behavior. These data support a growing body of evidence that individual species of bacteria can have different effects on host behavior, potentially related to their success at intestinal colonization. Specific to the zebrafish model, our results suggest that differences in the composition of microbes in fish facilities could have profound effects on the outcomes of behavioral and pharmacological studies. \n\nThis dataset is associated with the following publication:\nWeitekamp, C., A. Kvasnicka, S. Keely, N. Brinkman, X. Howey, S. Gaballah, D. Phelps, T. Catron, T. Zurlinden, E. Wheaton, and T. Tal. Monoassociation with bacterial isolates reveals the role of colonization, community complexity and abundance on locomotor behavior in larval zebrafish.   Animal Microbiome. BioMed Central Ltd, London,  UK, 3(12): 1-13, (2021).",
             "distribution": [
                 {
-                    "title": "Monoassociation dataset_20200228.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518372/Monoassociation%20dataset_20200228.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Monoassociation dataset_20200228.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518372",
+            "keyword": [
+                "zebrafish",
+                "germ-free",
+                "microbiome",
+                "hyperactivity",
+                "locomotor behavior"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-02-28",
-            "references": [
-                "https://doi.org/10.1186/s42523-020-00069-x"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131290,19 +131284,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s42523-020-00069-x"
+            ],
+            "rights": null,
+            "title": "Monoassociation with bacterial isolates reveals the role of colonization, community complexity and abundance on locomotor behavior in larval zebrafish"
         },
         {
-            "title": "PHOSPHORUS INVENTORY FOR THE CONTERMINOUS UNITED STATES (2002-2012), updated legacy V2",
-            "description": "This dataset contains estimates of phosphorus inputs and outputs for all HUC-8 subbasins across the contiguous United States for the years 2002, 2007, and 2012 as well as estimates of legacy P surplus.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Robert Sabo",
+                "hasEmail": "mailto:sabo.robert@epa.gov"
+            },
+            "description": "This dataset contains estimates of phosphorus inputs and outputs for all HUC-8 subbasins across the contiguous United States for the years 2002, 2007, and 2012 as well as estimates of legacy P surplus.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520860/Master_Inventory_Final_v2.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Master_Inventory_Final_v2.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520860",
             "keyword": [
@@ -131313,19 +131317,11 @@
                 "nonpoint source pollution",
                 "Point source"
             ],
-            "contactPoint": {
-                "fn": "Robert Sabo",
-                "hasEmail": "mailto:sabo.robert@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Master_Inventory_Final_v2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520860/Master_Inventory_Final_v2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-11",
-            "references": null,
+            "programCode": [
+                "020:097"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -131334,20 +131330,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "PHOSPHORUS INVENTORY FOR THE CONTERMINOUS UNITED STATES (2002-2012), updated legacy V2"
         },
         {
-            "title": "Questionnaire data and results of serum tests, SAFE/NIEHS study",
-            "description": "The dataset includes personally identifying data from questionnaires (demographic, socioeconomic, behavioral and health data) as well as results of laboratory tests of serum samples for biomarkers of health and antibody responses to pathogens. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: See above. Format: The questionnaire survey and biomarker test data are saved in SAS and Excel databases. \n\nThis dataset is associated with the following publications:\nStyles, J., R. Converse, S. Griffin, T. Wade, E. Klein, L. Nylander-French, J. Stewart, E. Sams, E. Hudgens, and A. Egorov. Human cytomegalovirus infections are associated with elevated biomarkers of vascular injury.   Frontiers in Cellular and Infection Microbiology. Frontiers, Lausanne,  SWITZERLAND, 10: 334, (2020).\nEgorov, A., R. Converse, S. Griffin, J. Styles, E. Sams, E. Hudgens, and T. Wade. Latent Toxoplasma gondii infections are associated with elevated biomarkers of inflammation and vascular injury.   BMC Infectious Diseases. BioMed Central Ltd, London,  UK, 21: 188, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
+            "contactPoint": {
+                "fn": "Andrey Egorov",
+                "hasEmail": "mailto:egorov.andrey@epa.gov"
+            },
+            "description": "The dataset includes personally identifying data from questionnaires (demographic, socioeconomic, behavioral and health data) as well as results of laboratory tests of serum samples for biomarkers of health and antibody responses to pathogens. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: See above. Format: The questionnaire survey and biomarker test data are saved in SAS and Excel databases. \n\nThis dataset is associated with the following publications:\nStyles, J., R. Converse, S. Griffin, T. Wade, E. Klein, L. Nylander-French, J. Stewart, E. Sams, E. Hudgens, and A. Egorov. Human cytomegalovirus infections are associated with elevated biomarkers of vascular injury.   Frontiers in Cellular and Infection Microbiology. Frontiers, Lausanne,  SWITZERLAND, 10: 334, (2020).\nEgorov, A., R. Converse, S. Griffin, J. Styles, E. Sams, E. Hudgens, and T. Wade. Latent Toxoplasma gondii infections are associated with elevated biomarkers of inflammation and vascular injury.   BMC Infectious Diseases. BioMed Central Ltd, London,  UK, 21: 188, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1505444",
             "keyword": [
                 "Toxoplasma gondii",
@@ -131355,15 +131353,10 @@
                 "vegetated land cover",
                 "biomarkers"
             ],
-            "contactPoint": {
-                "fn": "Andrey Egorov",
-                "hasEmail": "mailto:egorov.andrey@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-10-25",
-            "references": [
-                "https://doi.org/10.3389/fcimb.2020.00334",
-                "https://doi.org/10.1186/s12879-021-05882-6"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131373,20 +131366,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fcimb.2020.00334",
+                "https://doi.org/10.1186/s12879-021-05882-6"
+            ],
+            "rights": null,
+            "title": "Questionnaire data and results of serum tests, SAFE/NIEHS study"
         },
         {
-            "title": "sea fog study data",
-            "description": "The data includes the input for the WRF-CMAQ coupled model and the model output. This dataset is not publicly accessible because: This study was conduct at the University of Houston. It can be accessed through the following means: Please contact Prof. Yunsoo Choi (ychoi23@central.uh.edu) at the Department of Earth and Atmospheric Sciences, University of Houston to obtain the data. Format: input and output data are in netCDF format. \n\nThis dataset is associated with the following publication:\nJung, J., Y. Choi, D. Wong, D. Nelson, and S. Lee. Journal Of Geophysical Research -Atmospheres, Role of sea fog over the Yellow Sea on air quality with the direct effect of aerosols.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 126(5): e2020JD033498, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Cheung Wong",
+                "hasEmail": "mailto:wong.david-c@epa.gov"
+            },
+            "description": "The data includes the input for the WRF-CMAQ coupled model and the model output. This dataset is not publicly accessible because: This study was conduct at the University of Houston. It can be accessed through the following means: Please contact Prof. Yunsoo Choi (ychoi23@central.uh.edu) at the Department of Earth and Atmospheric Sciences, University of Houston to obtain the data. Format: input and output data are in netCDF format. \n\nThis dataset is associated with the following publication:\nJung, J., Y. Choi, D. Wong, D. Nelson, and S. Lee. Journal Of Geophysical Research -Atmospheres, Role of sea fog over the Yellow Sea on air quality with the direct effect of aerosols.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 126(5): e2020JD033498, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1519343",
             "keyword": [
                 "sea fog",
@@ -131395,14 +131393,10 @@
                 "PM25",
                 "direct aerosol effect"
             ],
-            "contactPoint": {
-                "fn": "Cheung Wong",
-                "hasEmail": "mailto:wong.david-c@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-09-10",
-            "references": [
-                "https://doi.org/10.1029/2020jd033498"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131412,51 +131406,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2020jd033498"
+            ],
+            "rights": null,
+            "title": "sea fog study data"
         },
         {
-            "title": "Urinary miRNAs measured in rat studies associated with nephron-specific chemical toxicity",
-            "description": "Urine samples were derived from a variety of archived industry-led studies, outlined in the dataset. The purpose was to measure a targeted set of miRNA targets that were represented in the Thermo Fisher TLDA A and TLDA B card sets in Figure 2. These case studies were selected due to probable nephrotoxicity, associated with published or internal records. These clinical markers and histopath evidence was included in Table 1 associated dataset. Given specific nephron toxicity, this experiment would determine miRNA candidates that may be specific toxicity biomarkers. This analysis set up the Venn Analysis in Figure 3, which specified candidates for nephron-specific analyses. \n\nThis dataset is associated with the following publication:\nChorley, B., H. Ellinger-Ziegelbauer, M. Tackett, F. Simutis, A. Harrill, J. McDuffie, E. Atabakhsh, R. Nassirpour, L. Whiteley, J. L\u00e9onard, G. Carswell, E. Harpur, C. Chen, and J. Gautier. Urinary miRNA Biomarkers of Drug-Induced Kidney Injury and Their Site Specificity Within the Nephron.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  180(1): 1-16, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1518921",
-            "keyword": [
-                "microRNAs",
-                "biomarkers",
-                "kidney injury",
-                "safety assessment"
-            ],
             "contactPoint": {
                 "fn": "Brian Chorley",
                 "hasEmail": "mailto:chorley.brian@epa.gov"
             },
+            "description": "Urine samples were derived from a variety of archived industry-led studies, outlined in the dataset. The purpose was to measure a targeted set of miRNA targets that were represented in the Thermo Fisher TLDA A and TLDA B card sets in Figure 2. These case studies were selected due to probable nephrotoxicity, associated with published or internal records. These clinical markers and histopath evidence was included in Table 1 associated dataset. Given specific nephron toxicity, this experiment would determine miRNA candidates that may be specific toxicity biomarkers. This analysis set up the Venn Analysis in Figure 3, which specified candidates for nephron-specific analyses. \n\nThis dataset is associated with the following publication:\nChorley, B., H. Ellinger-Ziegelbauer, M. Tackett, F. Simutis, A. Harrill, J. McDuffie, E. Atabakhsh, R. Nassirpour, L. Whiteley, J. L\u00e9onard, G. Carswell, E. Harpur, C. Chen, and J. Gautier. Urinary miRNA Biomarkers of Drug-Induced Kidney Injury and Their Site Specificity Within the Nephron.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  180(1): 1-16, (2021).",
             "distribution": [
                 {
-                    "title": "Data associated with Fig 2 and Table 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518921/Data%20associated%20with%20Fig%202%20and%20Table%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Fig 2 and Table 2.xlsx"
                 },
                 {
-                    "title": "Data associated with Table 1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518921/Data%20associated%20with%20Table%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Table 1.xlsx"
                 },
                 {
-                    "title": "Data associated with Fig 3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518921/Data%20associated%20with%20Fig%203.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Fig 3.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518921",
+            "keyword": [
+                "microRNAs",
+                "biomarkers",
+                "kidney injury",
+                "safety assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-23",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfaa181"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131466,65 +131460,65 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfaa181"
+            ],
+            "rights": null,
+            "title": "Urinary miRNAs measured in rat studies associated with nephron-specific chemical toxicity"
         },
         {
-            "title": "Measuring microRNAs in LCM-isolated nephron segments to determine region-specific expression",
-            "description": "To determine nephron specificity of microRNA expression that may be associated as toxicity biomarker seen in the urine, laser-capture microdissection (LCM) was performed on the 4 major segment of the nephron in control rat samples. These samples were sent to Bayer for candidate digital drop PCR measurements, NIEHS for smallRNA-seq measurements, and Abcam for FirePlex measurements. smallRNA-seq  measurements were used as global assessment of miRNA expression in these segments. FirePlex and ddPCR were used as medium to low number candidate assessments, respectively, of miRNA candidates, based on seq and urine data. \"Data associated with Fig 4\" summarizes the ddPCR findings. \"Data Associated with Figure 5\" and \"Data Associated with Figure 6\" summarize the smallRNA-seq findings. \"Data Associated with Figure 7\" summarize the FirePlex findings. \"Data associated with Figure 8_9\" summarize the correlations of these measurements. The cumlmination of these data determine nephron-specific and enriched expression of miRNAs, that are potential candidates of toxicity markers that could leak into the urine upon chemical exposure. \n\nThis dataset is associated with the following publication:\nChorley, B., H. Ellinger-Ziegelbauer, M. Tackett, F. Simutis, A. Harrill, J. McDuffie, E. Atabakhsh, R. Nassirpour, L. Whiteley, J. L\u00e9onard, G. Carswell, E. Harpur, C. Chen, and J. Gautier. Urinary miRNA Biomarkers of Drug-Induced Kidney Injury and Their Site Specificity Within the Nephron.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  180(1): 1-16, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1519009",
-            "keyword": [
-                "RNA-Seq",
-                "FirePlex",
-                "ddPCR",
-                "LCM",
-                "microRNAs",
-                "biomarkers",
-                "kidney injury",
-                "safety assessment"
-            ],
             "contactPoint": {
                 "fn": "Brian Chorley",
                 "hasEmail": "mailto:chorley.brian@epa.gov"
             },
+            "description": "To determine nephron specificity of microRNA expression that may be associated as toxicity biomarker seen in the urine, laser-capture microdissection (LCM) was performed on the 4 major segment of the nephron in control rat samples. These samples were sent to Bayer for candidate digital drop PCR measurements, NIEHS for smallRNA-seq measurements, and Abcam for FirePlex measurements. smallRNA-seq  measurements were used as global assessment of miRNA expression in these segments. FirePlex and ddPCR were used as medium to low number candidate assessments, respectively, of miRNA candidates, based on seq and urine data. \"Data associated with Fig 4\" summarizes the ddPCR findings. \"Data Associated with Figure 5\" and \"Data Associated with Figure 6\" summarize the smallRNA-seq findings. \"Data Associated with Figure 7\" summarize the FirePlex findings. \"Data associated with Figure 8_9\" summarize the correlations of these measurements. The cumlmination of these data determine nephron-specific and enriched expression of miRNAs, that are potential candidates of toxicity markers that could leak into the urine upon chemical exposure. \n\nThis dataset is associated with the following publication:\nChorley, B., H. Ellinger-Ziegelbauer, M. Tackett, F. Simutis, A. Harrill, J. McDuffie, E. Atabakhsh, R. Nassirpour, L. Whiteley, J. L\u00e9onard, G. Carswell, E. Harpur, C. Chen, and J. Gautier. Urinary miRNA Biomarkers of Drug-Induced Kidney Injury and Their Site Specificity Within the Nephron.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  180(1): 1-16, (2021).",
             "distribution": [
                 {
-                    "title": "Data associated with Figure 4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519009/Data%20associated%20with%20Figure%204.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Figure 4.xlsx"
                 },
                 {
-                    "title": "Data associated with Figure 5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519009/Data%20associated%20with%20Figure%205.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Figure 5.xlsx"
                 },
                 {
-                    "title": "Data associated with Figure 6.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519009/Data%20associated%20with%20Figure%206.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Figure 6.xlsx"
                 },
                 {
-                    "title": "Data associated with Figure 8_9.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519009/Data%20associated%20with%20Figure%208_9.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Figure 8_9.xlsx"
                 },
                 {
-                    "title": "Data associated with Figure 7.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519009/Data%20associated%20with%20Figure%207.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data associated with Figure 7.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519009",
+            "keyword": [
+                "RNA-Seq",
+                "FirePlex",
+                "ddPCR",
+                "LCM",
+                "microRNAs",
+                "biomarkers",
+                "kidney injury",
+                "safety assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-25",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfaa181"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131534,19 +131528,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfaa181"
+            ],
+            "rights": null,
+            "title": "Measuring microRNAs in LCM-isolated nephron segments to determine region-specific expression"
         },
         {
-            "title": "RICEWQ_AnnAGNPS_Manuscript_Data ",
-            "description": "RICEWQ_AnnAGNPS_Manuscript_Data. \n\nThis dataset is associated with the following publication:\nWang, R., R. Bingner, Y. Yuan, M. Locke, G. Herring, D. Denton, and M. Zhang. Evaluation of thiobencarb runoff from rice farming practices in a California watershed using an integrated RiceWQ-AnnAGNPS system.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 767: 144898, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Yongping Yuan",
+                "hasEmail": "mailto:yuan.yongping@epa.gov"
+            },
+            "description": "RICEWQ_AnnAGNPS_Manuscript_Data. \n\nThis dataset is associated with the following publication:\nWang, R., R. Bingner, Y. Yuan, M. Locke, G. Herring, D. Denton, and M. Zhang. Evaluation of thiobencarb runoff from rice farming practices in a California watershed using an integrated RiceWQ-AnnAGNPS system.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 767: 144898, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519268/RICEWQ_AnnAGNPS_Manuscript_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "RICEWQ_AnnAGNPS_Manuscript_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1519268",
             "keyword": [
@@ -131557,20 +131561,10 @@
                 "thiobencarb",
                 "model integration"
             ],
-            "contactPoint": {
-                "fn": "Yongping Yuan",
-                "hasEmail": "mailto:yuan.yongping@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "RICEWQ_AnnAGNPS_Manuscript_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519268/RICEWQ_AnnAGNPS_Manuscript_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-08-13",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2020.144898"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131580,40 +131574,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2020.144898"
+            ],
+            "rights": null,
+            "title": "RICEWQ_AnnAGNPS_Manuscript_Data "
         },
         {
-            "title": "A state-of-the-science review of polychlorinated biphenyl exposures at background levels: relative contributions of exposure routes",
-            "description": "Data set resulting from a targeted literature review of PCB concentrations in environmental media, as well as of total PCB dietary intake. Table S1 shows all studies that underwent full-text review (Figure 1). Table S2 shows all included studies and resulting PCB exposure estimates (used to generate Figures 2-4). Table S3 provides the data and analysis used to examine the effect of congener number on diet studies. \n\nThis dataset is associated with the following publication:\nWeitekamp, C., L. Phillips, L. Carlson, N. DeLuca, E. Hubal, and G. Lehmann. A state-of-the-science review of polychlorinated biphenyl exposures at background levels: relative contributions of exposure routes.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM, NETHERLANDS, 776: 1-8, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1519261",
-            "keyword": [
-                "Polychlorinated biphenyls (PCBs)",
-                "dietary exposure",
-                "air pollution exposure"
-            ],
             "contactPoint": {
                 "fn": "Chelsea Weitekamp",
                 "hasEmail": "mailto:weitekamp.chelsea@epa.gov"
             },
+            "description": "Data set resulting from a targeted literature review of PCB concentrations in environmental media, as well as of total PCB dietary intake. Table S1 shows all studies that underwent full-text review (Figure 1). Table S2 shows all included studies and resulting PCB exposure estimates (used to generate Figures 2-4). Table S3 provides the data and analysis used to examine the effect of congener number on diet studies. \n\nThis dataset is associated with the following publication:\nWeitekamp, C., L. Phillips, L. Carlson, N. DeLuca, E. Hubal, and G. Lehmann. A state-of-the-science review of polychlorinated biphenyl exposures at background levels: relative contributions of exposure routes.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM, NETHERLANDS, 776: 1-8, (2021).",
             "distribution": [
                 {
-                    "title": "mmc1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519261/mmc1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "mmc1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519261",
+            "keyword": [
+                "Polychlorinated biphenyls (PCBs)",
+                "dietary exposure",
+                "air pollution exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-18",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2021.145912"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131623,34 +131617,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2021.145912"
+            ],
+            "rights": null,
+            "title": "A state-of-the-science review of polychlorinated biphenyl exposures at background levels: relative contributions of exposure routes"
         },
         {
-            "title": "CATHGEN Traffic-related air pollution, vascular disease, and epigenetic aging",
-            "description": "The data contains location information, DNA methylation (transformed into epigenetic aging biomakers), dates of examination, demographics, disease diagnoses, and traffic-related air pollution exposures. It is stored as a series of data frames suitable for use in the R programming language. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: This data can be accessed by contacting Dr. Cavin Ward-Caviness and describing your needs for the analysis, completing the necessary ethics trainings, and gaining approval on the appropriate IRB applications as well as by the CATHGEN Steering Committee. Format: The data contains location information, DNA methylation (transformed into epigenetic aging biomakers), dates of examination, demographics, disease diagnoses, and traffic-related air pollution exposures. It is stored as a series of data frames suitable for use in the R programming language. \n\nThis dataset is associated with the following publication:\nWard-Caviness, C., A. Russell, A. Weaver, E. Slawsky, R. Dhingra, L. Coulter Kwee, R. Jiang, L. Neas, D. Diaz-Sanchez, R. Devlin, W. Cascio, E. Hauser, S. Shah, W. Kraus, and K. Olden. Accelerated epigenetic age as a biomarker of cardiovascular sensitivity to traffic-related air pollution.   Aging. Impact Journals, LLC, Orchard Park, NY, USA, 12(23): 24141-24155, (2020).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Radhika Dhingra",
+                "hasEmail": "mailto:dhingra.radhika@epa.gov"
+            },
+            "description": "The data contains location information, DNA methylation (transformed into epigenetic aging biomakers), dates of examination, demographics, disease diagnoses, and traffic-related air pollution exposures. It is stored as a series of data frames suitable for use in the R programming language. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: This data can be accessed by contacting Dr. Cavin Ward-Caviness and describing your needs for the analysis, completing the necessary ethics trainings, and gaining approval on the appropriate IRB applications as well as by the CATHGEN Steering Committee. Format: The data contains location information, DNA methylation (transformed into epigenetic aging biomakers), dates of examination, demographics, disease diagnoses, and traffic-related air pollution exposures. It is stored as a series of data frames suitable for use in the R programming language. \n\nThis dataset is associated with the following publication:\nWard-Caviness, C., A. Russell, A. Weaver, E. Slawsky, R. Dhingra, L. Coulter Kwee, R. Jiang, L. Neas, D. Diaz-Sanchez, R. Devlin, W. Cascio, E. Hauser, S. Shah, W. Kraus, and K. Olden. Accelerated epigenetic age as a biomarker of cardiovascular sensitivity to traffic-related air pollution.   Aging. Impact Journals, LLC, Orchard Park, NY, USA, 12(23): 24141-24155, (2020).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520772",
             "keyword": [
                 "air quality",
                 "DNA methylation",
                 "850k platform"
             ],
-            "contactPoint": {
-                "fn": "Radhika Dhingra",
-                "hasEmail": "mailto:dhingra.radhika@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-12-01",
-            "references": [
-                "https://doi.org/10.18632/aging.202341"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131660,40 +131654,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.18632/aging.202341"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "CATHGEN Traffic-related air pollution, vascular disease, and epigenetic aging"
         },
         {
-            "title": "Final Transcripts for River Metrics",
-            "description": "Plain text of focus group transcripts. \n\nThis dataset is associated with the following publication:\nWeber , M., and P. Ringold. River metrics by the public, for the public.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 14(5): e0214986, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503856",
-            "keyword": [
-                "focus groups",
-                "streams",
-                "Ecosystem Goods and Services",
-                "final ecosystem goods and services"
-            ],
             "contactPoint": {
                 "fn": "Paul Ringold",
                 "hasEmail": "mailto:ringold.paul@epa.gov"
             },
+            "description": "Plain text of focus group transcripts. \n\nThis dataset is associated with the following publication:\nWeber , M., and P. Ringold. River metrics by the public, for the public.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 14(5): e0214986, (2019).",
             "distribution": [
                 {
-                    "title": "https://osf.io/7w59g/",
-                    "accessURL": "https://osf.io/7w59g/"
+                    "accessURL": "https://osf.io/7w59g/",
+                    "title": "https://osf.io/7w59g/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503856",
+            "keyword": [
+                "focus groups",
+                "streams",
+                "Ecosystem Goods and Services",
+                "final ecosystem goods and services"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-11",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0214986"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131703,41 +131697,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0214986"
+            ],
+            "rights": null,
+            "title": "Final Transcripts for River Metrics"
         },
         {
-            "title": "Quantitative structure activity relationships (QSARs) and machine learning models for abiotic reduction of organic compounds by an aqueous Fe(II) complex",
-            "description": "Due to the increasing diversity of organic contaminants discharged into anoxic water environments, reactivity prediction is necessary for chemical persistence evaluation for water treatment and risk assessment purposes. Almost all quantitative structure activity relationships (QSARs) that describe rates of contaminant transformation apply only to narrowly-defined, relatively homogenous families of reactants (e.g., dechlorination of alkyl halides). In this work, we develop predictive models for abiotic reduction of 60 organic compounds with diverse reducible functional groups, including nitroaromatic compounds (NACs), aliphatic nitro-compounds (ANCs), aromatic N-oxides (ANOs), isoxazoles (ISXs), polyhalogenated alkanes (PHAs), sulfoxides and sulfones (SOs), and others. Rate constants for their reduction were measured using a model reductant system, Fe(II)-tiron. Qualitatively, the rates followed the order NACs > ANOs \uf0bb ISXs \uf0bb PHAs > ANCs > SOs. To develop QSARs, both conventional chemical descriptor-based and machine learning (ML)-based approaches were investigated. Conventional univariate QSARs based on a molecular descriptor ELUMO (energy of the lowest-unoccupied molecular orbital) gave good correlations within classes. Multivariate QSARs combining ELUMO with Abraham descriptors for physico-chemical properties gave slightly improved correlations within classes for NCs and NACs, but little improvement in correlation within other classes or among classes. The ML model obtained covers reduction rates for all classes of compounds and all of the conditions studied with the prediction accuracy similar to those of the conventional QSARs for individual classes (r2 = 0.41-0.98 for univariate QSARs, 0.71-0.94 for multivariate QSARs, and 0.83 for the ML model). Both approaches required a scheme for a priori classification of the compounds for model training. This work offers two alternative modelling approaches to comprehensive abiotic reactivity prediction for persistence evaluation of organic compounds in anoxic water environments. \n\nThis dataset is associated with the following publication:\nGao, Y., S. Zhong, T. Torralba-Sanchez, P. Tratnyek, E. Weber, Y. Chen, and H. Zhang. Quantitative structure activity relationships (QSARs) and machine learning models for abiotic reduction of organic compounds by an aqueous Fe(II) complex.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 192: 116843, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520719",
-            "keyword": [
-                "Chemical Transformation Simulator",
-                "QSARs",
-                "machine learning",
-                "abiotic reduction"
-            ],
             "contactPoint": {
                 "fn": "Eric Weber",
                 "hasEmail": "mailto:weber.eric@epa.gov"
             },
+            "description": "Due to the increasing diversity of organic contaminants discharged into anoxic water environments, reactivity prediction is necessary for chemical persistence evaluation for water treatment and risk assessment purposes. Almost all quantitative structure activity relationships (QSARs) that describe rates of contaminant transformation apply only to narrowly-defined, relatively homogenous families of reactants (e.g., dechlorination of alkyl halides). In this work, we develop predictive models for abiotic reduction of 60 organic compounds with diverse reducible functional groups, including nitroaromatic compounds (NACs), aliphatic nitro-compounds (ANCs), aromatic N-oxides (ANOs), isoxazoles (ISXs), polyhalogenated alkanes (PHAs), sulfoxides and sulfones (SOs), and others. Rate constants for their reduction were measured using a model reductant system, Fe(II)-tiron. Qualitatively, the rates followed the order NACs > ANOs \uf0bb ISXs \uf0bb PHAs > ANCs > SOs. To develop QSARs, both conventional chemical descriptor-based and machine learning (ML)-based approaches were investigated. Conventional univariate QSARs based on a molecular descriptor ELUMO (energy of the lowest-unoccupied molecular orbital) gave good correlations within classes. Multivariate QSARs combining ELUMO with Abraham descriptors for physico-chemical properties gave slightly improved correlations within classes for NCs and NACs, but little improvement in correlation within other classes or among classes. The ML model obtained covers reduction rates for all classes of compounds and all of the conditions studied with the prediction accuracy similar to those of the conventional QSARs for individual classes (r2 = 0.41-0.98 for univariate QSARs, 0.71-0.94 for multivariate QSARs, and 0.83 for the ML model). Both approaches required a scheme for a priori classification of the compounds for model training. This work offers two alternative modelling approaches to comprehensive abiotic reactivity prediction for persistence evaluation of organic compounds in anoxic water environments. \n\nThis dataset is associated with the following publication:\nGao, Y., S. Zhong, T. Torralba-Sanchez, P. Tratnyek, E. Weber, Y. Chen, and H. Zhang. Quantitative structure activity relationships (QSARs) and machine learning models for abiotic reduction of organic compounds by an aqueous Fe(II) complex.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 192: 116843, (2021).",
             "distribution": [
                 {
-                    "title": "Gao_et_al_ReductionRateConstants.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520719/Gao_et_al_ReductionRateConstants.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Gao_et_al_ReductionRateConstants.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520719",
+            "keyword": [
+                "Chemical Transformation Simulator",
+                "QSARs",
+                "machine learning",
+                "abiotic reduction"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-01",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2021.116843"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131747,42 +131741,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2021.116843"
+            ],
+            "rights": null,
+            "title": "Quantitative structure activity relationships (QSARs) and machine learning models for abiotic reduction of organic compounds by an aqueous Fe(II) complex"
         },
         {
-            "title": "Estimates of burrowing shrimp densities and habitat area in Yaquina estuary, Oregon, in 2002",
-            "description": "Estimates of the abundance and habitat area for two species of burrowing shrimps in Yaquina Bay estuary, Oregon. \n\nThis dataset is associated with the following publication:\nDumbauld, B., L. McCoy, T. DeWitt , and J. Chapman. Estimating long-term trends in populations of two ecosystem engineering burrowing shrimps in Pacific Northwest (USA) estuaries.   HYDROBIOLOGIA. Springer, New York, NY, USA, 848(5): 993-1013, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520875",
-            "keyword": [
-                "estuary",
-                "estuarine ecosystem",
-                "nutrient cycling",
-                "carbon cycling",
-                "benthic invertebrates"
-            ],
             "contactPoint": {
                 "fn": "Theodore Dewitt",
                 "hasEmail": "mailto:dewitt.ted@epa.gov"
             },
+            "description": "Estimates of the abundance and habitat area for two species of burrowing shrimps in Yaquina Bay estuary, Oregon. \n\nThis dataset is associated with the following publication:\nDumbauld, B., L. McCoy, T. DeWitt , and J. Chapman. Estimating long-term trends in populations of two ecosystem engineering burrowing shrimps in Pacific Northwest (USA) estuaries.   HYDROBIOLOGIA. Springer, New York, NY, USA, 848(5): 993-1013, (2021).",
             "distribution": [
                 {
-                    "title": "DeWittTheodore data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520875/DeWittTheodore%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DeWittTheodore data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520875",
+            "keyword": [
+                "estuary",
+                "estuarine ecosystem",
+                "nutrient cycling",
+                "carbon cycling",
+                "benthic invertebrates"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-19",
-            "references": [
-                "https://doi.org/10.1007/s10750-021-04544-7"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131792,42 +131786,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10750-021-04544-7"
+            ],
+            "rights": null,
+            "title": "Estimates of burrowing shrimp densities and habitat area in Yaquina estuary, Oregon, in 2002"
         },
         {
-            "title": "Pacific Northwest Salt Marsh Hydrology Model Dataset",
-            "description": "This spreadsheet contains the measured and simulated data used in the manuscript 'A Simple, Dynamic, Hydrological Model for Mesotidal Salt Marshes' by D.E. Marois and H.A. Stecher published in Estuarine, Coastal and Shelf Science, Vol 233 (https://doi.org/10.1016/j.ecss.2019.106486). \n\nThis dataset is associated with the following publication:\nMarois, D., and J. Stecher. A simple, dynamic, hydrological model for mesotidal salt marshes.   ESTUARINE, COASTAL AND SHELF SCIENCE. Elsevier Science Ltd, New York, NY, USA, 233: 106486, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1502521",
-            "keyword": [
-                "salt marshes",
-                "hydrology model",
-                "sea level rise",
-                "Pacific Northwest",
-                "Estuaries"
-            ],
             "contactPoint": {
                 "fn": "Darryl Marois",
                 "hasEmail": "mailto:marois.darryl@epa.gov"
             },
+            "description": "This spreadsheet contains the measured and simulated data used in the manuscript 'A Simple, Dynamic, Hydrological Model for Mesotidal Salt Marshes' by D.E. Marois and H.A. Stecher published in Estuarine, Coastal and Shelf Science, Vol 233 (https://doi.org/10.1016/j.ecss.2019.106486). \n\nThis dataset is associated with the following publication:\nMarois, D., and J. Stecher. A simple, dynamic, hydrological model for mesotidal salt marshes.   ESTUARINE, COASTAL AND SHELF SCIENCE. Elsevier Science Ltd, New York, NY, USA, 233: 106486, (2020).",
             "distribution": [
                 {
-                    "title": "Winant MS Data for SchiHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502521/Winant%20MS%20Data%20for%20SchiHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Winant MS Data for SchiHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502521",
+            "keyword": [
+                "salt marshes",
+                "hydrology model",
+                "sea level rise",
+                "Pacific Northwest",
+                "Estuaries"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-02",
-            "references": [
-                "https://doi.org/10.1016/j.ecss.2019.106486"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131837,19 +131831,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecss.2019.106486"
+            ],
+            "rights": null,
+            "title": "Pacific Northwest Salt Marsh Hydrology Model Dataset"
         },
         {
-            "title": "KodavantiP-Acute_HSAB_AOP_Neurotox_Science Hub Data 090319",
-            "description": "Neurotox data on in silico predicted chemicals to cause protein adducts in peripheral neurons.  Includes cytotoxicity (LDH release), changes in neuron network architecture using high content imaging and neurophysiology via microelectrode arrays. \n\nThis dataset is associated with the following publication:\nJohnstone, A., C. Mack, M. Valdez, T. Shafer, D. Herr, P. Kodavanti, and R. Lo Pachin. Acute In Vitro Effects on Embryonic Rat Dorsal Root Ganglion (DRG) Cultures by In Silico Predicted Neurotoxic Chemicals: Evaluations on Cytotoxicity, Neurite Length, and Neurophysiology..   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 69(104989): 1, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Prasada Kodavanti",
+                "hasEmail": "mailto:kodavanti.prasada@epa.gov"
+            },
+            "description": "Neurotox data on in silico predicted chemicals to cause protein adducts in peripheral neurons.  Includes cytotoxicity (LDH release), changes in neuron network architecture using high content imaging and neurophysiology via microelectrode arrays. \n\nThis dataset is associated with the following publication:\nJohnstone, A., C. Mack, M. Valdez, T. Shafer, D. Herr, P. Kodavanti, and R. Lo Pachin. Acute In Vitro Effects on Embryonic Rat Dorsal Root Ganglion (DRG) Cultures by In Silico Predicted Neurotoxic Chemicals: Evaluations on Cytotoxicity, Neurite Length, and Neurophysiology..   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 69(104989): 1, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504280/KodavantiP_Acute_HSAB_AOP_Neurotox_Science%20Hub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "KodavantiP_Acute_HSAB_AOP_Neurotox_Science Hub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504280",
             "keyword": [
@@ -131861,20 +131865,10 @@
                 "Neuropathy",
                 "cytotoxicity"
             ],
-            "contactPoint": {
-                "fn": "Prasada Kodavanti",
-                "hasEmail": "mailto:kodavanti.prasada@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "KodavantiP_Acute_HSAB_AOP_Neurotox_Science Hub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504280/KodavantiP_Acute_HSAB_AOP_Neurotox_Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-07",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2020.104989"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131884,19 +131878,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2020.104989"
+            ],
+            "rights": null,
+            "title": "KodavantiP-Acute_HSAB_AOP_Neurotox_Science Hub Data 090319"
         },
         {
-            "title": "Selecting a Minimal set of Androgen Receptor Assays for Screening Chemicals",
-            "description": "Screening certain environmental chemicals for their ability to interact with endocrine targets, including the androgen receptor (AR), is an important global concern. We previously developed a model using a battery of eleven in vitro AR assays to predict in vivo AR activity. Here we describe a revised mathematical modelling approach that also incorporates data from newly available assays and demonstrate that subsets of assays can provide close to the same level of predictivity. These subset models are evaluated against the full model using 1820 chemicals, as well as in vitro and in vivo reference chemicals from the literature. \n\nThis dataset is associated with the following publication:\nJudson, R., K. Houck, K. Friedman, J. Brown, P. Browne, P. Johnston, D. Close, K. Mansouri, and N. Kleinstreuer. Selecting a Minimal set of Androgen Receptor Assays for Screening Chemicals.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 117(November 2020): 104764, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Keith Houck",
+                "hasEmail": "mailto:houck.keith@epa.gov"
+            },
+            "description": "Screening certain environmental chemicals for their ability to interact with endocrine targets, including the androgen receptor (AR), is an important global concern. We previously developed a model using a battery of eleven in vitro AR assays to predict in vivo AR activity. Here we describe a revised mathematical modelling approach that also incorporates data from newly available assays and demonstrate that subsets of assays can provide close to the same level of predictivity. These subset models are evaluated against the full model using 1820 chemicals, as well as in vitro and in vivo reference chemicals from the literature. \n\nThis dataset is associated with the following publication:\nJudson, R., K. Houck, K. Friedman, J. Brown, P. Browne, P. Johnston, D. Close, K. Mansouri, and N. Kleinstreuer. Selecting a Minimal set of Androgen Receptor Assays for Screening Chemicals.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 117(November 2020): 104764, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/STAFF/rjudson/publications/Judson%20AR%202019/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/STAFF/rjudson/publications/Judson%20AR%202019/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504530",
             "keyword": [
@@ -131908,19 +131911,10 @@
                 "High throughput screening",
                 "high throughput toxicology"
             ],
-            "contactPoint": {
-                "fn": "Keith Houck",
-                "hasEmail": "mailto:houck.keith@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/STAFF/rjudson/publications/Judson%20AR%202019/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/STAFF/rjudson/publications/Judson%20AR%202019/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-18",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2020.104764"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -131930,20 +131924,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2020.104764"
+            ],
+            "rights": null,
+            "title": "Selecting a Minimal set of Androgen Receptor Assays for Screening Chemicals"
         },
         {
-            "title": "National Birth Defect Prevention Study Protocol for Public Access and Data Sharing",
-            "description": "Protocol for requesting public access to these data via CDC. This dataset is not publicly accessible because: These data include PII, including residential data and birth date. It can be accessed through the following means: These data may be accessed by following the National Birth Defects Prevention Study (NBDPS) Protocol for Public Access and Data Sharing. Format: The data are maintained in Analytic Files by CDC",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
+            "contactPoint": {
+                "fn": "Thomas Luben",
+                "hasEmail": "mailto:luben.tom@epa.gov"
+            },
+            "description": "Protocol for requesting public access to these data via CDC. This dataset is not publicly accessible because: These data include PII, including residential data and birth date. It can be accessed through the following means: These data may be accessed by following the National Birth Defects Prevention Study (NBDPS) Protocol for Public Access and Data Sharing. Format: The data are maintained in Analytic Files by CDC",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1518896",
             "keyword": [
                 "air quality",
@@ -131951,13 +131949,11 @@
                 "Fine Particulate Matter",
                 "Birth Data"
             ],
-            "contactPoint": {
-                "fn": "Thomas Luben",
-                "hasEmail": "mailto:luben.tom@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2014-06-11",
-            "references": null,
+            "programCode": [
+                "020:062"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -131966,20 +131962,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "National Birth Defect Prevention Study Protocol for Public Access and Data Sharing"
         },
         {
-            "title": "Toxoplasma gondii, greenspaces and biomarkers of allostatic load",
-            "description": "Residential greenness, biomarkers of chronic stress and allostatic load, demographic and health characteristics, and Toxoplasma gondii serostatus data on 300 individuals. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: See above. Format: Data are stored in SAS and MS Excel. \n\nThis dataset is associated with the following publication:\nEgorov, A., R. Converse, S. Griffin, J. Styles, E. Klein, E. Sams, E. Hudgens, and T. Wade. Environmental risk factors for Toxoplasma Gondii infections and the impact of latent infections on allostatic load in residents of\nCentral North Carolina.   BMC Infectious Diseases. BioMed Central Ltd, London,  UK, 18(1): 142, (2018).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
+            "contactPoint": {
+                "fn": "Andrey Egorov",
+                "hasEmail": "mailto:egorov.andrey@epa.gov"
+            },
+            "description": "Residential greenness, biomarkers of chronic stress and allostatic load, demographic and health characteristics, and Toxoplasma gondii serostatus data on 300 individuals. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: See above. Format: Data are stored in SAS and MS Excel. \n\nThis dataset is associated with the following publication:\nEgorov, A., R. Converse, S. Griffin, J. Styles, E. Klein, E. Sams, E. Hudgens, and T. Wade. Environmental risk factors for Toxoplasma Gondii infections and the impact of latent infections on allostatic load in residents of\nCentral North Carolina.   BMC Infectious Diseases. BioMed Central Ltd, London,  UK, 18(1): 142, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1419835",
             "keyword": [
                 "Toxoplasma gondii",
@@ -131987,14 +131985,10 @@
                 "allostatic load",
                 "biomarkers"
             ],
-            "contactPoint": {
-                "fn": "Andrey Egorov",
-                "hasEmail": "mailto:egorov.andrey@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-01-22",
-            "references": [
-                "https://doi.org/10.1186/s12879-018-3343-y"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132004,19 +131998,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12879-018-3343-y"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Toxoplasma gondii, greenspaces and biomarkers of allostatic load"
         },
         {
-            "title": "VT_Irene_highflow_data",
-            "description": "The data are species counts by location, as well as other environmental variables for each stream location sampled. \n\nThis dataset is associated with the following publication:\nStamp, J., A. Moore, S. Fiske, J. Gerritsen, B. Bierwagen, and A. Hamilton. Effects of Extreme High Flow Events on Macroinvertebrate Communities in Vermont Streams.   River Research and Applications. John Wiley & Sons Incorporated, New York, NY, USA, 36(9): 1891-1902, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Britta Bierwagen",
+                "hasEmail": "mailto:bierwagen.britta@epa.gov"
+            },
+            "description": "The data are species counts by location, as well as other environmental variables for each stream location sampled. \n\nThis dataset is associated with the following publication:\nStamp, J., A. Moore, S. Fiske, J. Gerritsen, B. Bierwagen, and A. Hamilton. Effects of Extreme High Flow Events on Macroinvertebrate Communities in Vermont Streams.   River Research and Applications. John Wiley & Sons Incorporated, New York, NY, USA, 36(9): 1891-1902, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502467/VT_Irene_20180628.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "VT_Irene_20180628.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502467",
             "keyword": [
@@ -132032,20 +132036,10 @@
                 "pebble counts",
                 "Vermont"
             ],
-            "contactPoint": {
-                "fn": "Britta Bierwagen",
-                "hasEmail": "mailto:bierwagen.britta@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "VT_Irene_20180628.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502467/VT_Irene_20180628.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-27",
-            "references": [
-                "https://doi.org/10.1002/rra.3713"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132055,40 +132049,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/rra.3713"
+            ],
+            "rights": null,
+            "title": "VT_Irene_highflow_data"
         },
         {
-            "title": "Link to supplemental material including all the data needed to replicate the analysis.",
-            "description": "This is a link to the supplemental material from the manuscript that includes all of the data and R code needed to replicate the analysis. \n\nThis dataset is associated with the following publication:\nCoffman, E., R. Burnett, and J. Sacks. Quantitative Characterization of Uncertainty in the Concentration Response Relationship between Long-Term PM2.5 Exposure and\nMortality at Low Concentrations.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 54(16): 10191-10200, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1520934",
-            "keyword": [
-                "particulate matter",
-                "mortality",
-                "Uncertainty",
-                "concentration-response"
-            ],
             "contactPoint": {
                 "fn": "Evan Coffman",
                 "hasEmail": "mailto:coffman.evan@epa.gov"
             },
+            "description": "This is a link to the supplemental material from the manuscript that includes all of the data and R code needed to replicate the analysis. \n\nThis dataset is associated with the following publication:\nCoffman, E., R. Burnett, and J. Sacks. Quantitative Characterization of Uncertainty in the Concentration Response Relationship between Long-Term PM2.5 Exposure and\nMortality at Low Concentrations.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 54(16): 10191-10200, (2020).",
             "distribution": [
                 {
-                    "title": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.0c02770/suppl_file/es0c02770_si_001.pdf",
-                    "accessURL": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.0c02770/suppl_file/es0c02770_si_001.pdf"
+                    "accessURL": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.0c02770/suppl_file/es0c02770_si_001.pdf",
+                    "title": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.0c02770/suppl_file/es0c02770_si_001.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520934",
+            "keyword": [
+                "particulate matter",
+                "mortality",
+                "Uncertainty",
+                "concentration-response"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-07-23",
-            "references": [
-                "https://doi.org/10.1021/acs.est.0c02770"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132098,68 +132092,68 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.0c02770"
+            ],
+            "rights": null,
+            "title": "Link to supplemental material including all the data needed to replicate the analysis."
         },
         {
-            "title": "Iron homeostasis with physically active Figure 1A",
-            "description": "Impact of repeated physical activity on iron and zinc concentrations the plasma, liver, lung, heart, and skeletal muscle. \n\nThis dataset is associated with the following publication:\nGhio, A., J. Soukup, C. Ghio, J. Richards, M. Schladweiler, S. Snow, and U. Kodavanti. Iron and Zinc homeostasis in female rats with physically active and sedentary lifestyles.   BioMetals. Springer International Publishing AG, Cham (ZG),  SWITZERLAND, 34(1): 97-105, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503731",
-            "keyword": [
-                "Exercise",
-                "iron",
-                "zinc",
-                "ferritins",
-                "liver",
-                "muscle"
-            ],
             "contactPoint": {
                 "fn": "Andrew Ghio",
                 "hasEmail": "mailto:ghio.andy@epa.gov"
             },
+            "description": "Impact of repeated physical activity on iron and zinc concentrations the plasma, liver, lung, heart, and skeletal muscle. \n\nThis dataset is associated with the following publication:\nGhio, A., J. Soukup, C. Ghio, J. Richards, M. Schladweiler, S. Snow, and U. Kodavanti. Iron and Zinc homeostasis in female rats with physically active and sedentary lifestyles.   BioMetals. Springer International Publishing AG, Cham (ZG),  SWITZERLAND, 34(1): 97-105, (2021).",
             "distribution": [
                 {
-                    "title": "exercise and iron figure 2D.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503731/exercise%20and%20iron%20figure%202D.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "exercise and iron figure 2D.xlsx"
                 },
                 {
-                    "title": "exercise and iron figure 2B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503731/exercise%20and%20iron%20figure%202B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "exercise and iron figure 2B.xlsx"
                 },
                 {
-                    "title": "exercise and iron figure 2A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503731/exercise%20and%20iron%20figure%202A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "exercise and iron figure 2A.xlsx"
                 },
                 {
-                    "title": "exercise and iron figure 1B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503731/exercise%20and%20iron%20figure%201B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "exercise and iron figure 1B.xlsx"
                 },
                 {
-                    "title": "exercise and iron figure 2C.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503731/exercise%20and%20iron%20figure%202C.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "exercise and iron figure 2C.xlsx"
                 },
                 {
-                    "title": "exercise and iron figure 1A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503731/exercise%20and%20iron%20figure%201A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "exercise and iron figure 1A.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503731",
+            "keyword": [
+                "Exercise",
+                "iron",
+                "zinc",
+                "ferritins",
+                "liver",
+                "muscle"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-23",
-            "references": [
-                "https://doi.org/10.1007/s10534-020-00266-w"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132169,40 +132163,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10534-020-00266-w"
+            ],
+            "rights": null,
+            "title": "Iron homeostasis with physically active Figure 1A"
         },
         {
-            "title": "Simultaneous determination of a suite of endogenous steroids by LC-APPI-MS: Application to the identification of endocrine disruptors in aquatic toxicology",
-            "description": "A liquid chromatogrpahy mass spectrometry (LC-MS) method was developed for the analysis of 13 endogenous steroids. The method was validated using both fish plasma and fish holding water. The method was applied to the assessment of endocrine disruption by analyzing plasma of fathead minnows exposed to fadrozole, and by analyzing holding water from Japanese medaka exposed to fadrozole. \n\nThis dataset is associated with the following publication:\nBlackwell, B., and G. Ankley. Simultaneous determination of a suite of endogenous steroids by LC-APPI-MS: Application to the identification of endocrine disruptors in aquatic toxicology.   Journal of Chromatography B. Elsevier Science Ltd, New York, NY, USA, 1163: 122513, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1519296",
-            "keyword": [
-                "steroids",
-                "endocrine disrupting chemicals",
-                "liquid chromatography-mass spectrometry"
-            ],
             "contactPoint": {
                 "fn": "Brett Blackwell",
                 "hasEmail": "mailto:blackwell.brett@epa.gov"
             },
+            "description": "A liquid chromatogrpahy mass spectrometry (LC-MS) method was developed for the analysis of 13 endogenous steroids. The method was validated using both fish plasma and fish holding water. The method was applied to the assessment of endocrine disruption by analyzing plasma of fathead minnows exposed to fadrozole, and by analyzing holding water from Japanese medaka exposed to fadrozole. \n\nThis dataset is associated with the following publication:\nBlackwell, B., and G. Ankley. Simultaneous determination of a suite of endogenous steroids by LC-APPI-MS: Application to the identification of endocrine disruptors in aquatic toxicology.   Journal of Chromatography B. Elsevier Science Ltd, New York, NY, USA, 1163: 122513, (2021).",
             "distribution": [
                 {
-                    "title": "SciHub_steroids APPI.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519296/SciHub_steroids%20APPI.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub_steroids APPI.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519296",
+            "keyword": [
+                "steroids",
+                "endocrine disrupting chemicals",
+                "liquid chromatography-mass spectrometry"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-01",
-            "references": [
-                "https://doi.org/10.1016/j.jchromb.2020.122513"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132212,42 +132206,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jchromb.2020.122513"
+            ],
+            "rights": null,
+            "title": "Simultaneous determination of a suite of endogenous steroids by LC-APPI-MS: Application to the identification of endocrine disruptors in aquatic toxicology"
         },
         {
-            "title": "Human Iodotyrosine Deiodinase Inhibition Assay: Screening of ToxCast Phase 1_v2, Phase 2, and e1k Chemical Libraries",
-            "description": "The excel spreadsheet contains the resultant data from an assay for chemical inhibition of human Iodotyrosine Deiodinase (IYD) enzyme activity screened against the ToxCast Phase 1_v2, Phase 2, and e1k chemical libraries, as well as a few additional target chemicals from ToxCast Phase 3 library or used in assay development. Over 1,800 chemicals were tested in total. This data set includes the list of chemicals tested and the median, minimum, and maximum inhibition produced by each chemical when screened at target high concentration of 200 \u00b5M. 154 chemicals were further tested in concentration response, and the median, minimum, and maximum inhibition produced at each concentration for those chemicals are included. A model inhibitor (3-Nitro-L-Tyrosine) was included on each plate as a positive control, with concentration response data for those curves also included in the data set. \n\nThis dataset is associated with the following publication:\nOlker, J., J. Korte, J. Denny, J. Haselman, P. Hartig, M. Cardon, M. Hornung, and S. Degitz. In Vitro Screening for Chemical Inhibition of the Iodide Recycling Enzyme, Iodotyrosine Deiodinase.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY,  71: 105073, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1518772",
-            "keyword": [
-                "iodotyrosine deiodinase",
-                "endocrine",
-                "thyroid hormone",
-                "Chemical Screening",
-                "In vitro assay"
-            ],
             "contactPoint": {
                 "fn": "Jennifer Olker",
                 "hasEmail": "mailto:olker.jennifer@epa.gov"
             },
+            "description": "The excel spreadsheet contains the resultant data from an assay for chemical inhibition of human Iodotyrosine Deiodinase (IYD) enzyme activity screened against the ToxCast Phase 1_v2, Phase 2, and e1k chemical libraries, as well as a few additional target chemicals from ToxCast Phase 3 library or used in assay development. Over 1,800 chemicals were tested in total. This data set includes the list of chemicals tested and the median, minimum, and maximum inhibition produced by each chemical when screened at target high concentration of 200 \u00b5M. 154 chemicals were further tested in concentration response, and the median, minimum, and maximum inhibition produced at each concentration for those chemicals are included. A model inhibitor (3-Nitro-L-Tyrosine) was included on each plate as a positive control, with concentration response data for those curves also included in the data set. \n\nThis dataset is associated with the following publication:\nOlker, J., J. Korte, J. Denny, J. Haselman, P. Hartig, M. Cardon, M. Hornung, and S. Degitz. In Vitro Screening for Chemical Inhibition of the Iodide Recycling Enzyme, Iodotyrosine Deiodinase.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY,  71: 105073, (2021).",
             "distribution": [
                 {
-                    "title": "Olker_et_al_IYD_in vitro screening_200610.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518772/Olker_et_al_IYD_in%20vitro%20screening_200610.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Olker_et_al_IYD_in vitro screening_200610.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518772",
+            "keyword": [
+                "iodotyrosine deiodinase",
+                "endocrine",
+                "thyroid hormone",
+                "Chemical Screening",
+                "In vitro assay"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-10",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2020.105073"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132257,19 +132251,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2020.105073"
+            ],
+            "rights": null,
+            "title": "Human Iodotyrosine Deiodinase Inhibition Assay: Screening of ToxCast Phase 1_v2, Phase 2, and e1k Chemical Libraries"
         },
         {
-            "title": "Cormier, S.M., 2017. Dataset for: A Field-based Model of the Relationship Between Extirpation of Salt-intolerant Benthic Invertebrates and Background Conductivity. USEPA Environmental Dataset Gateway.  https://doi.org/10.23719/1371707",
-            "description": "Data sets and individual XCD results used to develop the field-based benchmarks are available at the U.S. EPA Environmental Dataset Gateway (https://doi.org/10.23719/1371707) (Cormier, 2017). Data are contained in three zip files. The folder \u201cBiological.zip\u201d contains occurrences of benthic invertebrate genera in 24 state data sets.  This paper uses only the data from West Virginia ecoregions 69 and 70. The folder \u201cEnvironmental.zip\u201d contains environmental data sorted into 24 data sets. The folder \u201cmodel.zip\u201d contains the calculated XC95 values, probability of observation plots as generalized additive models, and the cumulative frequency distribution for benthic invertebrate genera from WV69 and 70 plus data sets used to develop other models not discussed in this paper. \n\nA spreadsheet for calculating XC95 values and XCD05 is described in Cormier et al. (2018c). The tools, data sets, example calculations, and example outputs are available online at https://wiley.figshare.com/ieam and https://github.com/smcormier/Biological-Extirpation-Analysis-Tools-BEAT/releases/tag/v.1.0.2. Alternatively, calculation of XC95, GAM plots, XCD05 can be calculated using batch R-code. Similarly, the R-code and data sets are available on GitHub (https://github.com/leppott/XC95).\n\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Susan Cormier",
+                "hasEmail": "mailto:cormier.susan@epa.gov"
+            },
+            "description": "Data sets and individual XCD results used to develop the field-based benchmarks are available at the U.S. EPA Environmental Dataset Gateway (https://doi.org/10.23719/1371707) (Cormier, 2017). Data are contained in three zip files. The folder \u201cBiological.zip\u201d contains occurrences of benthic invertebrate genera in 24 state data sets.  This paper uses only the data from West Virginia ecoregions 69 and 70. The folder \u201cEnvironmental.zip\u201d contains environmental data sorted into 24 data sets. The folder \u201cmodel.zip\u201d contains the calculated XC95 values, probability of observation plots as generalized additive models, and the cumulative frequency distribution for benthic invertebrate genera from WV69 and 70 plus data sets used to develop other models not discussed in this paper. \n\nA spreadsheet for calculating XC95 values and XCD05 is described in Cormier et al. (2018c). The tools, data sets, example calculations, and example outputs are available online at https://wiley.figshare.com/ieam and https://github.com/smcormier/Biological-Extirpation-Analysis-Tools-BEAT/releases/tag/v.1.0.2. Alternatively, calculation of XC95, GAM plots, XCD05 can be calculated using batch R-code. Similarly, the R-code and data sets are available on GitHub (https://github.com/leppott/XC95).\n\n",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.23719/1371707",
+                    "title": "https://doi.org/10.23719/1371707"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518682",
             "keyword": [
@@ -132279,18 +132282,11 @@
                 "permutation",
                 "field based"
             ],
-            "contactPoint": {
-                "fn": "Susan Cormier",
-                "hasEmail": "mailto:cormier.susan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.23719/1371707",
-                    "accessURL": "https://doi.org/10.23719/1371707"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-20",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -132299,41 +132295,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Cormier, S.M., 2017. Dataset for: A Field-based Model of the Relationship Between Extirpation of Salt-intolerant Benthic Invertebrates and Background Conductivity. USEPA Environmental Dataset Gateway.  https://doi.org/10.23719/1371707"
         },
         {
-            "title": "De Facto  Water Reuse: Bioassay suite approach delivers depth and breadth in endocrine active compound detection",
-            "description": "Although endocrine disrupting compounds have been detected in wastewater and surface waters worldwide using a variety of in vitro effects-based screening tools, e.g. bioassays, few have examined potential attenuation of environmental contaminants by both natural (sorption, degradation, etc.) and anthropogenic (water treatment practices) processes. This study used several bioassays and quantitative chemical analyses to assess residence-time weighted samples at six sites along a river in the northeastern United States beginning upstream from a wastewater treatment plant outfall and proceeding downstream along the stream reach to a drinking water treatment plant. Known steroidal estrogens were quantified and changes in signaling pathway molecular initiating events (activation of estrogen, androgen, glucocorticoid, peroxisome proliferator-activated, pregnane X receptor, and aryl hydrocarbon receptor signaling networks) were identified in water extracts. In initial multi-endpoint assays geographic and receptor-specific endocrine activity patterns in transcription factor signatures and nuclear receptor activation were discovered. In subsequent single endpoint receptor-specific bioassays, estrogen (16 of 18 samples; 0.01 to 28\u202fng estradiol equivalents [E2Eqs]/L) glucocorticoid (3 of 18 samples; 1.8 to 21\u202fng dexamethasone equivalents [DexEqs]/L), and androgen (2 of 18 samples; 0.95 to 2.1\u202fng dihydrotestosterone equivalents [DHTEqs]/L) receptor transcriptional activation occurred above respective assay method detection limits (0.04\u202fng E2Eqs/L, 1.2\u202fng DexEqs/L, and 0.77\u202fng DHTEqs/L) in multiple sampling events. Estrogen activity, the most often detected, correlated well with measured concentrations of known steroidal estrogens (r2\u202f=\u202f0.890). Overall, activity indicative of multiple types of endocrine active compounds was highest in wastewater effluent samples, while activity downstream was progressively lower, and negligible in unfinished treated drinking water. Not only was estrogenic and glucocorticoid activity confirmed in the effluent by utilizing multiple methods concurrently, but other activated signaling networks that historically received less attention (i.e. peroxisome proliferator-activated receptor) were also detected. \n\nThis dataset is associated with the following publication:\nMedlock Kakaley, E., B. Blackwell, M. Cardon, J. Conley, N. Evans, D. Feifarek, E. Furlong, S. Glassmeyer, L. Gray, P. Hartig, D. Kolpin, M. Mills, L. Rosenblum, D. Villeneuve, and V. Wilson. De Facto Water Reuse: Bioassay suite approach delivers depth and breadth in endocrine active compound detection.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 699(134297): 1, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503441",
-            "keyword": [
-                "source water",
-                "wastewater",
-                "drinking water",
-                "de facto reuse"
-            ],
             "contactPoint": {
                 "fn": "Susan Glassmeyer",
                 "hasEmail": "mailto:glassmeyer.susan@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1503441/documents/Data%20Dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Although endocrine disrupting compounds have been detected in wastewater and surface waters worldwide using a variety of in vitro effects-based screening tools, e.g. bioassays, few have examined potential attenuation of environmental contaminants by both natural (sorption, degradation, etc.) and anthropogenic (water treatment practices) processes. This study used several bioassays and quantitative chemical analyses to assess residence-time weighted samples at six sites along a river in the northeastern United States beginning upstream from a wastewater treatment plant outfall and proceeding downstream along the stream reach to a drinking water treatment plant. Known steroidal estrogens were quantified and changes in signaling pathway molecular initiating events (activation of estrogen, androgen, glucocorticoid, peroxisome proliferator-activated, pregnane X receptor, and aryl hydrocarbon receptor signaling networks) were identified in water extracts. In initial multi-endpoint assays geographic and receptor-specific endocrine activity patterns in transcription factor signatures and nuclear receptor activation were discovered. In subsequent single endpoint receptor-specific bioassays, estrogen (16 of 18 samples; 0.01 to 28\u202fng estradiol equivalents [E2Eqs]/L) glucocorticoid (3 of 18 samples; 1.8 to 21\u202fng dexamethasone equivalents [DexEqs]/L), and androgen (2 of 18 samples; 0.95 to 2.1\u202fng dihydrotestosterone equivalents [DHTEqs]/L) receptor transcriptional activation occurred above respective assay method detection limits (0.04\u202fng E2Eqs/L, 1.2\u202fng DexEqs/L, and 0.77\u202fng DHTEqs/L) in multiple sampling events. Estrogen activity, the most often detected, correlated well with measured concentrations of known steroidal estrogens (r2\u202f=\u202f0.890). Overall, activity indicative of multiple types of endocrine active compounds was highest in wastewater effluent samples, while activity downstream was progressively lower, and negligible in unfinished treated drinking water. Not only was estrogenic and glucocorticoid activity confirmed in the effluent by utilizing multiple methods concurrently, but other activated signaling networks that historically received less attention (i.e. peroxisome proliferator-activated receptor) were also detected. \n\nThis dataset is associated with the following publication:\nMedlock Kakaley, E., B. Blackwell, M. Cardon, J. Conley, N. Evans, D. Feifarek, E. Furlong, S. Glassmeyer, L. Gray, P. Hartig, D. Kolpin, M. Mills, L. Rosenblum, D. Villeneuve, and V. Wilson. De Facto Water Reuse: Bioassay suite approach delivers depth and breadth in endocrine active compound detection.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 699(134297): 1, (2020).",
             "distribution": [
                 {
-                    "title": "De Facto Water Reuse Bioassay Manuscript Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503441/De%20Facto%20Water%20Reuse%20Bioassay%20Manuscript%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "De Facto Water Reuse Bioassay Manuscript Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503441",
+            "keyword": [
+                "source water",
+                "wastewater",
+                "drinking water",
+                "de facto reuse"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-28",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2019.134297"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132344,56 +132340,54 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1503441/documents/Data%20Dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2019.134297"
+            ],
+            "rights": null,
+            "title": "De Facto  Water Reuse: Bioassay suite approach delivers depth and breadth in endocrine active compound detection"
         },
         {
-            "title": "Genome Sequence Data Set02",
-            "description": "The Whole Genome Shotgun project has been deposited in DDBJ/ENA/GenBank under the BioProject PRJNA487286 with the following accession numbers CP061840 (chromosome) and CP061841 (plasmid). The raw sequence reads have been submitted to the NCBI SRA under the accession numbers SRR13076822 and SRR13076823. \n\nThis dataset is associated with the following publication:\nGomez-Alvarez, V., L. Boczek, I. Raffenberg, and R. Revetta. Closed Genome and Plasmid Sequences of Legionella pneumophila AW-13-4, Isolated from a Hot Water Loop System of a Large Occupational Building.   Microbiology Resource Announcements. American Society for Microbiology, Washington, DC, USA, 10(1): e01276-20, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520777",
-            "keyword": [
-                "legionella",
-                "buildings",
-                "waterbiome",
-                "Microbial Analysis",
-                "Premise Plumbing",
-                "drinking water",
-                "Drinking water distribution system"
-            ],
             "contactPoint": {
                 "fn": "Vicente Gomez-Alvarez",
                 "hasEmail": "mailto:gomez-alvarez.vicente@epa.gov"
             },
+            "description": "The Whole Genome Shotgun project has been deposited in DDBJ/ENA/GenBank under the BioProject PRJNA487286 with the following accession numbers CP061840 (chromosome) and CP061841 (plasmid). The raw sequence reads have been submitted to the NCBI SRA under the accession numbers SRR13076822 and SRR13076823. \n\nThis dataset is associated with the following publication:\nGomez-Alvarez, V., L. Boczek, I. Raffenberg, and R. Revetta. Closed Genome and Plasmid Sequences of Legionella pneumophila AW-13-4, Isolated from a Hot Water Loop System of a Large Occupational Building.   Microbiology Resource Announcements. American Society for Microbiology, Washington, DC, USA, 10(1): e01276-20, (2021).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/nuccore/CP061840.1/",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/nuccore/CP061840.1/"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/nuccore/CP061840.1/",
+                    "title": "https://www.ncbi.nlm.nih.gov/nuccore/CP061840.1/"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/nuccore/CP061841",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/nuccore/CP061841"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/nuccore/CP061841",
+                    "title": "https://www.ncbi.nlm.nih.gov/nuccore/CP061841"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/sra/SRR13076822",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/sra/SRR13076822"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/sra/SRR13076822",
+                    "title": "https://www.ncbi.nlm.nih.gov/sra/SRR13076822"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/sra/?term=SRR13076823",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/sra/?term=SRR13076823"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/sra/?term=SRR13076823",
+                    "title": "https://www.ncbi.nlm.nih.gov/sra/?term=SRR13076823"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520777",
+            "keyword": [
+                "legionella",
+                "buildings",
+                "waterbiome",
+                "Microbial Analysis",
+                "Premise Plumbing",
+                "drinking water",
+                "Drinking water distribution system"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-21",
-            "references": [
-                "https://doi.org/10.1128/mra.01276-20"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132403,20 +132397,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1128/mra.01276-20"
+            ],
+            "rights": null,
+            "title": "Genome Sequence Data Set02"
         },
         {
-            "title": "Burrow Geometry and Hazards: Case Histories of GPR for Mapping Animal Burrows",
-            "description": "The data are GPR records. This dataset is not publicly accessible because: lead author has the data. It can be accessed through the following means: via the lead author. Format: Data were no EPA-generated and are with the lead author from Kutztown University, PA. \n\nThis dataset is associated with the following publication:\nSherrod, L., W. Sauck, E. Simpson, D. Werkema, and J. Swiontek. Case Histories of GPR for Animal Burrows Mapping and Geometry.   JOURNAL OF ENVIRONMENTAL AND ENGINEERING GEOPHYSICS. Environmental and Engineering Geophysical Society, Denver, CO, USA, 24(1): 1-17, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
+            "contactPoint": {
+                "fn": "Douglas Werkema",
+                "hasEmail": "mailto:werkema.d@epa.gov"
+            },
+            "description": "The data are GPR records. This dataset is not publicly accessible because: lead author has the data. It can be accessed through the following means: via the lead author. Format: Data were no EPA-generated and are with the lead author from Kutztown University, PA. \n\nThis dataset is associated with the following publication:\nSherrod, L., W. Sauck, E. Simpson, D. Werkema, and J. Swiontek. Case Histories of GPR for Animal Burrows Mapping and Geometry.   JOURNAL OF ENVIRONMENTAL AND ENGINEERING GEOPHYSICS. Environmental and Engineering Geophysical Society, Denver, CO, USA, 24(1): 1-17, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1519287",
             "keyword": [
                 "animal burrows",
@@ -132424,14 +132422,10 @@
                 "geophysics",
                 "Geometry and Hazards"
             ],
-            "contactPoint": {
-                "fn": "Douglas Werkema",
-                "hasEmail": "mailto:werkema.d@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2015-07-20",
-            "references": [
-                "https://www.researchgate.net/publication/333035253_Case_Histories_of_GPR_for_Animal_Burrows_Mapping_and_Geometry"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132441,20 +132435,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.researchgate.net/publication/333035253_Case_Histories_of_GPR_for_Animal_Burrows_Mapping_and_Geometry"
+            ],
+            "rights": null,
+            "title": "Burrow Geometry and Hazards: Case Histories of GPR for Mapping Animal Burrows"
         },
         {
-            "title": "Fractured Rock Geophysics Method Selection Tool Software",
-            "description": "This software was developed in collaboration with the USGS. This dataset is not publicly accessible because: Because there is no data. It can be accessed through the following means: NA. Format: No dataset.  This product is software. \n\nThis dataset is associated with the following publication:\nDay-Lewis, F., L. Slater, J. Robinson, C. Johnson, N. Terry, and D. Werkema. An overview of geophysical technologies appropriate for characterization and monitoring at fractured-rock sites.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 204(2): 709-720, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Douglas Werkema",
+                "hasEmail": "mailto:werkema.d@epa.gov"
+            },
+            "description": "This software was developed in collaboration with the USGS. This dataset is not publicly accessible because: Because there is no data. It can be accessed through the following means: NA. Format: No dataset.  This product is software. \n\nThis dataset is associated with the following publication:\nDay-Lewis, F., L. Slater, J. Robinson, C. Johnson, N. Terry, and D. Werkema. An overview of geophysical technologies appropriate for characterization and monitoring at fractured-rock sites.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 204(2): 709-720, (2017).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520967",
             "keyword": [
                 "geophysics",
@@ -132463,14 +132461,10 @@
                 "field methods",
                 "characterization"
             ],
-            "contactPoint": {
-                "fn": "Douglas Werkema",
-                "hasEmail": "mailto:werkema.d@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2017-04-11",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2017.04.033"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132480,20 +132474,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2017.04.033"
+            ],
+            "rights": null,
+            "title": "Fractured Rock Geophysics Method Selection Tool Software"
         },
         {
-            "title": "Case Histories of GPR for Animal Burrows Mapping and Geometry",
-            "description": "Geophysical ground penetrating radar data. This dataset is not publicly accessible because: The data is controlled by Kutztown University (PA). It can be accessed through the following means: The first author, Laura Sherrod, can be contactec for access to the data. Format: Geophysical ground penetrating radar data. \n\nThis dataset is associated with the following publication:\nSherrod, L., W. Sauck, E. Simpson, D. Werkema, and J. Swiontek. Case Histories of GPR for Animal Burrows Mapping and Geometry.   JOURNAL OF ENVIRONMENTAL AND ENGINEERING GEOPHYSICS. Environmental and Engineering Geophysical Society, Denver, CO, USA, 24(1): 1-17, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
+            "contactPoint": {
+                "fn": "Douglas Werkema",
+                "hasEmail": "mailto:werkema.d@epa.gov"
+            },
+            "description": "Geophysical ground penetrating radar data. This dataset is not publicly accessible because: The data is controlled by Kutztown University (PA). It can be accessed through the following means: The first author, Laura Sherrod, can be contactec for access to the data. Format: Geophysical ground penetrating radar data. \n\nThis dataset is associated with the following publication:\nSherrod, L., W. Sauck, E. Simpson, D. Werkema, and J. Swiontek. Case Histories of GPR for Animal Burrows Mapping and Geometry.   JOURNAL OF ENVIRONMENTAL AND ENGINEERING GEOPHYSICS. Environmental and Engineering Geophysical Society, Denver, CO, USA, 24(1): 1-17, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520554",
             "keyword": [
                 "animal burrows",
@@ -132501,14 +132499,10 @@
                 "geophysics",
                 "hazards"
             ],
-            "contactPoint": {
-                "fn": "Douglas Werkema",
-                "hasEmail": "mailto:werkema.d@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2016-08-01",
-            "references": [
-                "https://www.researchgate.net/publication/333035253_Case_Histories_of_GPR_for_Animal_Burrows_Mapping_and_Geometry"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132518,38 +132512,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.researchgate.net/publication/333035253_Case_Histories_of_GPR_for_Animal_Burrows_Mapping_and_Geometry"
+            ],
+            "rights": null,
+            "title": "Case Histories of GPR for Animal Burrows Mapping and Geometry"
         },
         {
-            "title": "Geophysical and hydrological data for Fredericktown, MO proposed landfill site characterization",
-            "description": "Geophysical and hydrological data. \n\nThis dataset is associated with the following publication:\nJohnson, C., K. Pappas, E. White, D. Werkema, N. Terry, R. Ford, S. Phillips, K. Limes, and J. Lane Jr. Geophysical Assessment of a Proposed Landfill Site in Fredericktown, Missouri..   FastTIMES. Environmental and Engineering Geophysical Society, Denver, CO, USA, 25(2): 98-106, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1518912",
-            "keyword": [
-                "geophysics",
-                "characterization"
-            ],
             "contactPoint": {
                 "fn": "Douglas Werkema",
                 "hasEmail": "mailto:werkema.d@epa.gov"
             },
+            "description": "Geophysical and hydrological data. \n\nThis dataset is associated with the following publication:\nJohnson, C., K. Pappas, E. White, D. Werkema, N. Terry, R. Ford, S. Phillips, K. Limes, and J. Lane Jr. Geophysical Assessment of a Proposed Landfill Site in Fredericktown, Missouri..   FastTIMES. Environmental and Engineering Geophysical Society, Denver, CO, USA, 25(2): 98-106, (2020).",
             "distribution": [
                 {
-                    "title": "https://www.sciencebase.gov/catalog/item/5cb75adfe4b0c3b0065d7c03",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/5cb75adfe4b0c3b0065d7c03"
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/5cb75adfe4b0c3b0065d7c03",
+                    "title": "https://www.sciencebase.gov/catalog/item/5cb75adfe4b0c3b0065d7c03"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518912",
+            "keyword": [
+                "geophysics",
+                "characterization"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-06-03",
-            "references": [
-                "https://app.box.com/s/vz5nz4ykrs4fgtjosop0nnbprm1ot51h"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132559,41 +132553,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://app.box.com/s/vz5nz4ykrs4fgtjosop0nnbprm1ot51h"
+            ],
+            "rights": null,
+            "title": "Geophysical and hydrological data for Fredericktown, MO proposed landfill site characterization"
         },
         {
-            "title": "Dataset for ORD-033374: A Gene Expression Biomarker Identifies Chemical Modulators of the Estrogen Receptor \u03b1 (ER\u03b1) in a MCF-7 Microarray Compendium",
-            "description": "Microarray experiments examined in the study. \n\nThis dataset is associated with the following publication:\nRooney, J., N. Ryan, J. Liu, R. Houtman, R.  van Beuningen, J. Hsieh, G. Chang, S. Chen, and J. Corton. A Gene Expression Biomarker Identifies Chemical Modulators of Estrogen Receptor \u03b1 in an MCF-7 Microarray Compendium.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 34(2): 313-329, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504425",
-            "keyword": [
-                "endocrine disruption transcript profiling",
-                "toxicogenomics",
-                "estrogen receptor",
-                "biomarker"
-            ],
             "contactPoint": {
                 "fn": "Jon Corton",
                 "hasEmail": "mailto:corton.chris@epa.gov"
             },
+            "description": "Microarray experiments examined in the study. \n\nThis dataset is associated with the following publication:\nRooney, J., N. Ryan, J. Liu, R. Houtman, R.  van Beuningen, J. Hsieh, G. Chang, S. Chen, and J. Corton. A Gene Expression Biomarker Identifies Chemical Modulators of Estrogen Receptor \u03b1 in an MCF-7 Microarray Compendium.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 34(2): 313-329, (2021).",
             "distribution": [
                 {
-                    "title": "Data submission for A-d25m.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504425/Data%20submission%20for%20A-d25m.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-d25m.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504425",
+            "keyword": [
+                "endocrine disruption transcript profiling",
+                "toxicogenomics",
+                "estrogen receptor",
+                "biomarker"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-09",
-            "references": [
-                "https://doi.org/10.1021/acs.chemrestox.0c00243"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132603,42 +132597,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.chemrestox.0c00243"
+            ],
+            "rights": null,
+            "title": "Dataset for ORD-033374: A Gene Expression Biomarker Identifies Chemical Modulators of the Estrogen Receptor \u03b1 (ER\u03b1) in a MCF-7 Microarray Compendium"
         },
         {
-            "title": "Table 4 Sb XANES LCF results",
-            "description": "The dataset is a table of linear combination fitting results of antimony speciation showing the percent distribution of antimony species. \n\nThis dataset is associated with the following publication:\nDiquattro, S., P. Castaldi, S. Ritch, A.L. Juhasz, G. Brunetti, K.G. Scheckel, G. Garau, E. Lombi, G. Garaua, and E. Lombib. Insights into the fate of antimony (Sb) in contaminated soils: Ageing influence on Sb mobility, bioavailability, bioaccessibility and speciation.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 770: 145354, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520050",
-            "keyword": [
-                "Antimony",
-                "Ageing",
-                "Bioaccessibility Soil",
-                "bioavailability",
-                "synchrotron speciation"
-            ],
             "contactPoint": {
                 "fn": "Kirk Scheckel",
                 "hasEmail": "mailto:scheckel.kirk@epa.gov"
             },
+            "description": "The dataset is a table of linear combination fitting results of antimony speciation showing the percent distribution of antimony species. \n\nThis dataset is associated with the following publication:\nDiquattro, S., P. Castaldi, S. Ritch, A.L. Juhasz, G. Brunetti, K.G. Scheckel, G. Garau, E. Lombi, G. Garaua, and E. Lombib. Insights into the fate of antimony (Sb) in contaminated soils: Ageing influence on Sb mobility, bioavailability, bioaccessibility and speciation.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 770: 145354, (2021).",
             "distribution": [
                 {
-                    "title": "Table 4.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520050/Table%204.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table 4.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520050",
+            "keyword": [
+                "Antimony",
+                "Ageing",
+                "Bioaccessibility Soil",
+                "bioavailability",
+                "synchrotron speciation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-17",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2021.145354"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132648,47 +132642,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2021.145354"
+            ],
+            "rights": null,
+            "title": "Table 4 Sb XANES LCF results"
         },
         {
-            "title": "datasets for journal article_adapting urban BMPs for resilience",
-            "description": "The two excel files contain data for the results discussed and presented in the paper's figures and tables from the SUSTAIN modeling runs for the 5 sites included in this study. \n\nThis dataset is associated with the following publication:\nJob, S., M. Harris, S. Julius, J.B. Butcher, and J.T. Kennedy. Adapting urban best management practices for resilience to long-term environmental changes.   WATER ENVIRONMENT RESEARCH. Water Environment Federation, Alexandria, VA, USA, 92(12): 2178-2192, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500867",
-            "keyword": [
-                "stormwater",
-                "climate change",
-                "resilience",
-                "best management practices",
-                "adaptation"
-            ],
             "contactPoint": {
                 "fn": "Susan Julius",
                 "hasEmail": "mailto:julius.susan@epa.gov"
             },
+            "description": "The two excel files contain data for the results discussed and presented in the paper's figures and tables from the SUSTAIN modeling runs for the 5 sites included in this study. \n\nThis dataset is associated with the following publication:\nJob, S., M. Harris, S. Julius, J.B. Butcher, and J.T. Kennedy. Adapting urban best management practices for resilience to long-term environmental changes.   WATER ENVIRONMENT RESEARCH. Water Environment Federation, Alexandria, VA, USA, 92(12): 2178-2192, (2020).",
             "distribution": [
                 {
-                    "title": "Adapting_Urban_BMPs_datasources1_508.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500867/Adapting_Urban_BMPs_datasources1_508.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Adapting_Urban_BMPs_datasources1_508.xlsx"
                 },
                 {
-                    "title": "Adapting_Urban_BMPs_datasources2_508.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500867/Adapting_Urban_BMPs_datasources2_508.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Adapting_Urban_BMPs_datasources2_508.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500867",
+            "keyword": [
+                "stormwater",
+                "climate change",
+                "resilience",
+                "best management practices",
+                "adaptation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-24",
-            "references": [
-                "https://doi.org/10.1002/wer.1302"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132698,48 +132692,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/wer.1302"
+            ],
+            "rights": null,
+            "title": "datasets for journal article_adapting urban BMPs for resilience"
         },
         {
-            "title": "Stream water isotope data from the Snoqualmie River Basin 2017-2018, and related watershed information",
-            "description": "Water stable isotope data (both hydrogen and oxygen isotopes of H2O) from the Snoqualmie River Basin from 2017-2018.  This data was paired with USGS gauge data so includes watershed characteristics at the gaging stations near where water isotopes were collected.  Water isotopes were collected throughout the basin to cover the range of elevation and stream sizes.  Water isotopes were collected 5 times at all locations, and approximately twice monthly at the main stem of the Snoqualmie and larger tributaries. \n\nThis dataset is associated with the following publication:\nMcGill, L., J.R. Brooks, and A. Steel. Spatial and temporal dynamics of water sources in a mountain river basin inferred through \u03b42H and \u03b418O of water.   Hydrological Processes. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 35(3): e14063, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1520140",
-            "keyword": [
-                "water resources",
-                "river flow",
-                "stable isotopes",
-                "water supply",
-                "geology",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Jacqueline Brooks",
                 "hasEmail": "mailto:brooks.reneej@epa.gov"
             },
+            "description": "Water stable isotope data (both hydrogen and oxygen isotopes of H2O) from the Snoqualmie River Basin from 2017-2018.  This data was paired with USGS gauge data so includes watershed characteristics at the gaging stations near where water isotopes were collected.  Water isotopes were collected throughout the basin to cover the range of elevation and stream sizes.  Water isotopes were collected 5 times at all locations, and approximately twice monthly at the main stem of the Snoqualmie and larger tributaries. \n\nThis dataset is associated with the following publication:\nMcGill, L., J.R. Brooks, and A. Steel. Spatial and temporal dynamics of water sources in a mountain river basin inferred through \u03b42H and \u03b418O of water.   Hydrological Processes. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 35(3): e14063, (2021).",
             "distribution": [
                 {
-                    "title": "EPA_Snoqualmie_isotope_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520140/EPA_Snoqualmie_isotope_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA_Snoqualmie_isotope_data.xlsx"
                 },
                 {
-                    "title": "EPA_Snoqualmie_geology_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520140/EPA_Snoqualmie_geology_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA_Snoqualmie_geology_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520140",
+            "keyword": [
+                "water resources",
+                "river flow",
+                "stable isotopes",
+                "water supply",
+                "geology",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-20",
-            "references": [
-                "https://doi.org/10.1002/hyp.14063"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132749,52 +132743,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/hyp.14063"
+            ],
+            "rights": null,
+            "title": "Stream water isotope data from the Snoqualmie River Basin 2017-2018, and related watershed information"
         },
         {
-            "title": "DeMarini et al., 2021 Mutagenicity Data Set - I-THMs",
-            "description": "Mutagenicity data for iodinated trihalomethane compounds. \n\nThis dataset is associated with the following publication:\nDeMarini, D., S. Warren, W. Smith, S. Richardson, and H. Liberatore. Inability of GSTT1 to Activate Iodinated Halomethanes to Mutagens in Salmonella.   ENVIRONMENTAL AND MOLECULAR MUTAGENESIS. John Wiley & Sons, Inc, Hoboken, NJ, USA, 62(3): 168-176, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520910",
-            "keyword": [
-                "Mutagenicity",
-                "GSTT1",
-                "Disinfection by-products",
-                "drinking water",
-                "DBPs"
-            ],
             "contactPoint": {
                 "fn": "Hannah Liberatore",
                 "hasEmail": "mailto:liberatore.hannah@epa.gov"
             },
+            "description": "Mutagenicity data for iodinated trihalomethane compounds. \n\nThis dataset is associated with the following publication:\nDeMarini, D., S. Warren, W. Smith, S. Richardson, and H. Liberatore. Inability of GSTT1 to Activate Iodinated Halomethanes to Mutagens in Salmonella.   ENVIRONMENTAL AND MOLECULAR MUTAGENESIS. John Wiley & Sons, Inc, Hoboken, NJ, USA, 62(3): 168-176, (2021).",
             "distribution": [
                 {
-                    "title": "Table3_1-11-2020.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520910/Table3_1-11-2020.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table3_1-11-2020.docx"
                 },
                 {
-                    "title": "Table2_1-11-2020.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520910/Table2_1-11-2020.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table2_1-11-2020.docx"
                 },
                 {
-                    "title": "Table1_1-11-2020.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520910/Table1_1-11-2020.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table1_1-11-2020.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520910",
+            "keyword": [
+                "Mutagenicity",
+                "GSTT1",
+                "Disinfection by-products",
+                "drinking water",
+                "DBPs"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-11",
-            "references": [
-                "https://doi.org/10.1002/em.22423"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132804,19 +132798,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/em.22423"
+            ],
+            "rights": null,
+            "title": "DeMarini et al., 2021 Mutagenicity Data Set - I-THMs"
         },
         {
-            "title": "Role of solution chemistry in the retention and release of graphene oxide nanomaterials in uncoated and iron oxide-coated sand (Journal Article: Science of the Total Environment; 579: 776-785)",
-            "description": "Laboratory experimental data include: 1) transport and retention of graphene oxide nanomaterials (GONMs) in packed-columns under different KCl and CaCl2 concentrations in pure sand and iron oxide-coated sands; 2) average hydrodynamic size of GONMs using dynamic light scattering (DLS); and 3) zeta potentials of GONMs.\n\nOther data include: Derjaguin-Landau-Verwey-Overbeek (DLVO) interaction energy using surface element integration (SEI) technique. \n\nThis dataset is associated with the following publication:\nWang, D., C. Shen, Y. Jin, C. Su, L. Chu, and D. Zhou. Role of solution chemistry on the deposition and release of graphene oxide nanoparticles in uncoated and iron oxide-coated sand.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 579: 776-785, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Chunming Su",
+                "hasEmail": "mailto:su.chunming@epa.gov"
+            },
+            "description": "Laboratory experimental data include: 1) transport and retention of graphene oxide nanomaterials (GONMs) in packed-columns under different KCl and CaCl2 concentrations in pure sand and iron oxide-coated sands; 2) average hydrodynamic size of GONMs using dynamic light scattering (DLS); and 3) zeta potentials of GONMs.\n\nOther data include: Derjaguin-Landau-Verwey-Overbeek (DLVO) interaction energy using surface element integration (SEI) technique. \n\nThis dataset is associated with the following publication:\nWang, D., C. Shen, Y. Jin, C. Su, L. Chu, and D. Zhou. Role of solution chemistry on the deposition and release of graphene oxide nanoparticles in uncoated and iron oxide-coated sand.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 579: 776-785, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407601/STE%20paper%20Data_EPA_Updated%20on%2008102017.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "STE paper Data_EPA_Updated on 08102017.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407601",
             "keyword": [
@@ -132830,20 +132834,10 @@
                 "Retention",
                 "Release"
             ],
-            "contactPoint": {
-                "fn": "Chunming Su",
-                "hasEmail": "mailto:su.chunming@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "STE paper Data_EPA_Updated on 08102017.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407601/STE%20paper%20Data_EPA_Updated%20on%2008102017.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2017-08-10",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.11.029"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132853,54 +132847,54 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.11.029"
+            ],
+            "rights": null,
+            "title": "Role of solution chemistry in the retention and release of graphene oxide nanomaterials in uncoated and iron oxide-coated sand (Journal Article: Science of the Total Environment; 579: 776-785)"
         },
         {
-            "title": "Bioavailability and speciation data",
-            "description": "The files in the dataset include tables of Pb bioavailability data from mice studies, of Pb x-ray absorption near-edge structure spectroscopy data, and of Pb speciation results of diets and excreted Pb. \n\nThis dataset is associated with the following publication:\nKarna, R.R., M.P. Noerpel, C. Nelson, B. Elek, K. Herbin-Davis, G. Diamond , K. Bradham, D.J. Thomas, and K.G. Scheckel. Bioavailable soil Pb minimized by in situ transformation to plumbojarosite.   PNAS  (PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES). National Academy of Sciences, WASHINGTON, DC, USA, 118(3): 01-06, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1519345",
-            "keyword": [
-                "lead bioavailability",
-                "lead contaminated soil",
-                "lead immobilzation",
-                "plumbojarosite",
-                "synchrotron speciation",
-                "in-vitro bioaccessibilty",
-                "soil remediation"
-            ],
             "contactPoint": {
                 "fn": "Kirk Scheckel",
                 "hasEmail": "mailto:scheckel.kirk@epa.gov"
             },
+            "description": "The files in the dataset include tables of Pb bioavailability data from mice studies, of Pb x-ray absorption near-edge structure spectroscopy data, and of Pb speciation results of diets and excreted Pb. \n\nThis dataset is associated with the following publication:\nKarna, R.R., M.P. Noerpel, C. Nelson, B. Elek, K. Herbin-Davis, G. Diamond , K. Bradham, D.J. Thomas, and K.G. Scheckel. Bioavailable soil Pb minimized by in situ transformation to plumbojarosite.   PNAS  (PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES). National Academy of Sciences, WASHINGTON, DC, USA, 118(3): 01-06, (2021).",
             "distribution": [
                 {
-                    "title": "Data summary for Figs 2 & 3 Rainju et al 09102020.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519345/Data%20summary%20for%20Figs%202%20%26%203%20Rainju%20et%20al%2009102020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data summary for Figs 2 & 3 Rainju et al 09102020.xlsx"
                 },
                 {
-                    "title": "Figure 1_ Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519345/Figure%201_%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1_ Data.xlsx"
                 },
                 {
-                    "title": "Tables1and2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519345/Tables1and2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tables1and2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519345",
+            "keyword": [
+                "lead bioavailability",
+                "lead contaminated soil",
+                "lead immobilzation",
+                "plumbojarosite",
+                "synchrotron speciation",
+                "in-vitro bioaccessibilty",
+                "soil remediation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-09",
-            "references": [
-                "https://doi.org/10.1073/pnas.2020315117"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132910,20 +132904,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1073/pnas.2020315117"
+            ],
+            "rights": null,
+            "title": "Bioavailability and speciation data"
         },
         {
-            "title": "Patient records of  pulmonary isolation of Nontuberculous Mycobacteria (NTM) ",
-            "description": "Dataset includes patient records of pulmonary isolation of Nontuberculous Mycobacteria (NTM) from North Carolina State Laboratory of Public Health for the years 2006-2010. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: access is restricted because it contains PII. Format: csv. \n\nThis dataset is associated with the following publication:\nDeflorio-Barker, S., A. Egorov, G. Smith, M.S. Murphy, J. Stout, A. Ghio, E. Hudgens, K. Messier, J. Maillard, and E. Hilborn. Environmental risk factors associated with pulmonary isolation of nontuberculous mycobacteria, a population-based study in the southeastern United States.  Scott Sheridan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 763: 144552, (2021).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Stephanie Deflorio-Barker",
+                "hasEmail": "mailto:deflorio-barker.stephanie@epa.gov"
+            },
+            "description": "Dataset includes patient records of pulmonary isolation of Nontuberculous Mycobacteria (NTM) from North Carolina State Laboratory of Public Health for the years 2006-2010. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: access is restricted because it contains PII. Format: csv. \n\nThis dataset is associated with the following publication:\nDeflorio-Barker, S., A. Egorov, G. Smith, M.S. Murphy, J. Stout, A. Ghio, E. Hudgens, K. Messier, J. Maillard, and E. Hilborn. Environmental risk factors associated with pulmonary isolation of nontuberculous mycobacteria, a population-based study in the southeastern United States.  Scott Sheridan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 763: 144552, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520963",
             "keyword": [
                 "Nontuberculous Mycobacteria (NTM)",
@@ -132933,14 +132931,10 @@
                 "hydric soil",
                 "drinking water"
             ],
-            "contactPoint": {
-                "fn": "Stephanie Deflorio-Barker",
-                "hasEmail": "mailto:deflorio-barker.stephanie@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-29",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2020.144552"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132950,20 +132944,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2020.144552"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Patient records of  pulmonary isolation of Nontuberculous Mycobacteria (NTM) "
         },
         {
-            "title": "patient records of  pulmonary isolation of Nontuberculous Mycobacteria (NTM) at the block level",
-            "description": "This dataset contains patient records of  pulmonary isolation of Nontuberculous Mycobacteria (NTM) from North Carolina State Laboratory of Public Health, local soil data from the Soil Survey Geographic Database (SSURGO, Natural Resources Conservation Service, United States Department of Agriculture), land use data from the 2011 National Land Cover Database (NLCD), paved and dirt road data from the 2010 Navteq street dataset, and census-block level characteristics from the U.S. Census. The data is aggregated at the census-block level. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Access is restricted because it contains PII. Format: sas7bdat. \n\nThis dataset is associated with the following publication:\nDeflorio-Barker, S., A. Egorov, G. Smith, M.S. Murphy, J. Stout, A. Ghio, E. Hudgens, K. Messier, J. Maillard, and E. Hilborn. Environmental risk factors associated with pulmonary isolation of nontuberculous mycobacteria, a population-based study in the southeastern United States.  Scott Sheridan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 763: 144552, (2021).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Stephanie Deflorio-Barker",
+                "hasEmail": "mailto:deflorio-barker.stephanie@epa.gov"
+            },
+            "description": "This dataset contains patient records of  pulmonary isolation of Nontuberculous Mycobacteria (NTM) from North Carolina State Laboratory of Public Health, local soil data from the Soil Survey Geographic Database (SSURGO, Natural Resources Conservation Service, United States Department of Agriculture), land use data from the 2011 National Land Cover Database (NLCD), paved and dirt road data from the 2010 Navteq street dataset, and census-block level characteristics from the U.S. Census. The data is aggregated at the census-block level. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Access is restricted because it contains PII. Format: sas7bdat. \n\nThis dataset is associated with the following publication:\nDeflorio-Barker, S., A. Egorov, G. Smith, M.S. Murphy, J. Stout, A. Ghio, E. Hudgens, K. Messier, J. Maillard, and E. Hilborn. Environmental risk factors associated with pulmonary isolation of nontuberculous mycobacteria, a population-based study in the southeastern United States.  Scott Sheridan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 763: 144552, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520964",
             "keyword": [
                 "Nontuberculous Mycobacteria (NTM)",
@@ -132973,14 +132971,10 @@
                 "hydric soil",
                 "drinking water"
             ],
-            "contactPoint": {
-                "fn": "Stephanie Deflorio-Barker",
-                "hasEmail": "mailto:deflorio-barker.stephanie@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-25",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2020.144552"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -132990,170 +132984,170 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2020.144552"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "patient records of  pulmonary isolation of Nontuberculous Mycobacteria (NTM) at the block level"
         },
         {
-            "title": "Mobile source air quality data used as inputs to generate health effect incidence. PM and ozone health effect incidence for 17 mobile source sectors in 2011 and 2025; baseline mortality incidence in 2011 and 2025; and mortality percentage maps",
-            "description": "Mobile source-related PM and Ozone air quality concentration data used as inputs to BenMAP-CE to generate the attributable health burden of 17 different mobile sector categories. Also included are the attributable health impact results for the same mobile sectors, baseline mortality burden, and maps that display the spatial distribution of mobile sector mortality health burden as a percentage of total mortality. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520969",
-            "keyword": [
-                "transportation",
-                "particulate matter",
-                "Ozone",
-                "health burden",
-                "air quality",
-                "Mobile sources"
-            ],
             "contactPoint": {
                 "fn": "Kenneth Davidson",
                 "hasEmail": "mailto:davidson.ken@epa.gov"
             },
+            "description": "Mobile source-related PM and Ozone air quality concentration data used as inputs to BenMAP-CE to generate the attributable health burden of 17 different mobile sector categories. Also included are the attributable health impact results for the same mobile sectors, baseline mortality burden, and maps that display the spatial distribution of mobile sector mortality health burden as a percentage of total mortality. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "Mobile BPT Incidence.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520969/Mobile%20BPT%20Incidence.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Mobile BPT Incidence.zip"
                 },
                 {
-                    "title": "BenMAP inputs_updated.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520969/BenMAP%20inputs_updated.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "BenMAP inputs_updated.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520969",
+            "keyword": [
+                "transportation",
+                "particulate matter",
+                "Ozone",
+                "health burden",
+                "air quality",
+                "Mobile sources"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-23",
-            "references": [
-                "https://dx.doi.org/10.1088/1748-9326/ab83a8"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. Environmental Protection Agency",
                 "subOrganizationOf": {
                     "name": "U.S. Government"
                 }
-            }
+            },
+            "references": [
+                "https://dx.doi.org/10.1088/1748-9326/ab83a8"
+            ],
+            "rights": null,
+            "title": "Mobile source air quality data used as inputs to generate health effect incidence. PM and ozone health effect incidence for 17 mobile source sectors in 2011 and 2025; baseline mortality incidence in 2011 and 2025; and mortality percentage maps"
         },
         {
-            "title": "Oxidative degradation of pharmaceuticals and endocrine disrupting compounds in water",
-            "description": "The dataset includes: \n\nTEM micrographs of rGO-Ag0/Fe3O4 NH.\n\nXRD patterns, FT-IR spectra, and UV-Vis absorption spectra of rGO, AgNP, and rGO-Ag0/Fe3O4 NH.\n\nX-ray photoelectron spectra of rGO and rGO-Ag0/Fe3O4 NH.\n\nConcentrations of phenol, acetaminophen, ibuprofen, naproxen, BPA, E2, and EE2 as a function of time in graphs. \n\nThis dataset is associated with the following publication:\nPark, C.M., J. Heo, D. Wang, C. Su, and Y. Yoon. Heterogeneous activation of persulfate by reduced graphene oxide\u2013elemental silver/magnetite nanohybrids for the oxidative degradation of pharmaceuticals and endocrine disrupting compounds in water.   APPLIED CATALYSIS B: ENVIRONMENTAL. Elsevier Science Ltd, New York, NY, USA, 225: 91-99, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1521026",
-            "keyword": [
-                "graphene oxide",
-                "nanocomposites",
-                "pharmaceuticals",
-                "endocrine disrupting compounds",
-                "advanced oxidation"
-            ],
             "contactPoint": {
                 "fn": "Chunming Su",
                 "hasEmail": "mailto:su.chunming@epa.gov"
             },
+            "description": "The dataset includes: \n\nTEM micrographs of rGO-Ag0/Fe3O4 NH.\n\nXRD patterns, FT-IR spectra, and UV-Vis absorption spectra of rGO, AgNP, and rGO-Ag0/Fe3O4 NH.\n\nX-ray photoelectron spectra of rGO and rGO-Ag0/Fe3O4 NH.\n\nConcentrations of phenol, acetaminophen, ibuprofen, naproxen, BPA, E2, and EE2 as a function of time in graphs. \n\nThis dataset is associated with the following publication:\nPark, C.M., J. Heo, D. Wang, C. Su, and Y. Yoon. Heterogeneous activation of persulfate by reduced graphene oxide\u2013elemental silver/magnetite nanohybrids for the oxidative degradation of pharmaceuticals and endocrine disrupting compounds in water.   APPLIED CATALYSIS B: ENVIRONMENTAL. Elsevier Science Ltd, New York, NY, USA, 225: 91-99, (2018).",
             "distribution": [
                 {
-                    "title": "4. Conc. of pollutants vs time in graphs.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/4.%20Conc.%20of%20pollutants%20vs%20time%20in%20graphs.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "4. Conc. of pollutants vs time in graphs.pdf"
                 },
                 {
-                    "title": "3-8. XPS for rGO-Ag0_Fe3O4 NH Fe2p.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-8.%20XPS%20for%20rGO-Ag0_Fe3O4%20NH%20Fe2p.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-8. XPS for rGO-Ag0_Fe3O4 NH Fe2p.pdf"
                 },
                 {
-                    "title": "3-7. XPS for rGO-Ag0_Fe3O4 NH Ag3d.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-7.%20XPS%20for%20rGO-Ag0_Fe3O4%20NH%20Ag3d.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-7. XPS for rGO-Ag0_Fe3O4 NH Ag3d.pdf"
                 },
                 {
-                    "title": "3-6. XPS for rGO-Ag0_Fe3O4 NH O1s.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-6.%20XPS%20for%20rGO-Ag0_Fe3O4%20NH%20O1s.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-6. XPS for rGO-Ag0_Fe3O4 NH O1s.pdf"
                 },
                 {
-                    "title": "3-5. XPS for rGO-Ag0_Fe3O4 NH C1s.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-5.%20XPS%20for%20rGO-Ag0_Fe3O4%20NH%20C1s.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-5. XPS for rGO-Ag0_Fe3O4 NH C1s.pdf"
                 },
                 {
-                    "title": "3-4. XPS for rGO-Ag0_Fe3O4 NH wide.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-4.%20XPS%20for%20rGO-Ag0_Fe3O4%20NH%20wide.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-4. XPS for rGO-Ag0_Fe3O4 NH wide.pdf"
                 },
                 {
-                    "title": "3-3. XPS for rGO O1s.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-3.%20XPS%20for%20rGO%20O1s.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-3. XPS for rGO O1s.pdf"
                 },
                 {
-                    "title": "3-2. XPS for rGO C1s.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-2.%20XPS%20for%20rGO%20C1s.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-2. XPS for rGO C1s.pdf"
                 },
                 {
-                    "title": "3-1. XPS for rGO wide.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/3-1.%20XPS%20for%20rGO%20wide.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "3-1. XPS for rGO wide.pdf"
                 },
                 {
-                    "title": "2-7. UV-Vis for rGO-Ag0_Fe3O4 NH.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/2-7.%20UV-Vis%20for%20rGO-Ag0_Fe3O4%20NH.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "2-7. UV-Vis for rGO-Ag0_Fe3O4 NH.pdf"
                 },
                 {
-                    "title": "2-6. UV-Vis for AgNP.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/2-6.%20UV-Vis%20for%20AgNP.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "2-6. UV-Vis for AgNP.pdf"
                 },
                 {
-                    "title": "2-5. UV-Vis for rGO.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/2-5.%20UV-Vis%20for%20rGO.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "2-5. UV-Vis for rGO.pdf"
                 },
                 {
-                    "title": "2-4. FTIR for rGO-Ag0_Fe3O4 NH.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/2-4.%20FTIR%20for%20rGO-Ag0_Fe3O4%20NH.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "2-4. FTIR for rGO-Ag0_Fe3O4 NH.pdf"
                 },
                 {
-                    "title": "2-3. FTIR for rGO.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/2-3.%20FTIR%20for%20rGO.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "2-3. FTIR for rGO.pdf"
                 },
                 {
-                    "title": "2-2. XRD for rGO-Ag0_Fe3O4 NH.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/2-2.%20XRD%20for%20rGO-Ag0_Fe3O4%20NH.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "2-2. XRD for rGO-Ag0_Fe3O4 NH.pdf"
                 },
                 {
-                    "title": "2-1. XRD for rGO.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/2-1.%20XRD%20for%20rGO.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "2-1. XRD for rGO.pdf"
                 },
                 {
-                    "title": "1. TEM for rGO-Ag0_Fe3O4 NH.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521026/1.%20TEM%20for%20rGO-Ag0_Fe3O4%20NH.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "1. TEM for rGO-Ag0_Fe3O4 NH.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521026",
+            "keyword": [
+                "graphene oxide",
+                "nanocomposites",
+                "pharmaceuticals",
+                "endocrine disrupting compounds",
+                "advanced oxidation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-03-15",
-            "references": [
-                "https://doi.org/10.1016/j.apcatb.2017.11.058"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133163,19 +133157,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apcatb.2017.11.058"
+            ],
+            "rights": null,
+            "title": "Oxidative degradation of pharmaceuticals and endocrine disrupting compounds in water"
         },
         {
-            "title": "SWAT Model Data Illinois River Watershed",
-            "description": "Data used in the manuscript submission that describes the use of support vector machine calibration of a SWAT model of the Illinois River Watershed",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Kenneth Forshay",
+                "hasEmail": "mailto:forshay.ken@epa.gov"
+            },
+            "description": "Data used in the manuscript submission that describes the use of support vector machine calibration of a SWAT model of the Illinois River Watershed",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520734/Data_Submitting_to_PlosOne.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Data_Submitting_to_PlosOne.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520734",
             "keyword": [
@@ -133187,19 +133191,11 @@
                 "Illinois River Basin",
                 "Support Vector Machine"
             ],
-            "contactPoint": {
-                "fn": "Kenneth Forshay",
-                "hasEmail": "mailto:forshay.ken@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data_Submitting_to_PlosOne.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520734/Data_Submitting_to_PlosOne.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-01",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -133208,41 +133204,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "SWAT Model Data Illinois River Watershed"
         },
         {
-            "title": "FRTL-5 RAIU of 5-AT",
-            "description": "Iodide uptake following a two-hour incubation with concentrations of 5-ATcompared to control iodide uptake in FRTL thyroid follicular cells. \n\nThis dataset is associated with the following publication:\nAdams, V., M. Bazar, E. Reinke, A. Buckalew, and W. Eck. In vitro and in vivo effects of 5-Aminotetrazole (5-AT)- an energetic compound.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 111(104573): 1, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1521086",
-            "keyword": [
-                "thyroid",
-                "Sodium Iodide Symporter",
-                "endocrine disruption",
-                "5-aminotetrazole"
-            ],
             "contactPoint": {
                 "fn": "Angela Buckalew",
                 "hasEmail": "mailto:buckalew.angela@epa.gov"
             },
+            "description": "Iodide uptake following a two-hour incubation with concentrations of 5-ATcompared to control iodide uptake in FRTL thyroid follicular cells. \n\nThis dataset is associated with the following publication:\nAdams, V., M. Bazar, E. Reinke, A. Buckalew, and W. Eck. In vitro and in vivo effects of 5-Aminotetrazole (5-AT)- an energetic compound.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 111(104573): 1, (2020).",
             "distribution": [
                 {
-                    "title": "FRTL-5 dataset for science-hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521086/FRTL-5%20dataset%20for%20science-hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FRTL-5 dataset for science-hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521086",
+            "keyword": [
+                "thyroid",
+                "Sodium Iodide Symporter",
+                "endocrine disruption",
+                "5-aminotetrazole"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-30",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2019.104573"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133252,19 +133246,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2019.104573"
+            ],
+            "rights": null,
+            "title": "FRTL-5 RAIU of 5-AT"
         },
         {
-            "title": "ORD-037657: Sex-, age-, race-, and disease-dependent variations in NRF2-regulated genes in human livers",
-            "description": "Data was generated at KUMC, not EPA. There is no EPA data that is part of this submission. \n\nThis dataset is associated with the following publication:\nLiu, J., J.Y. Cui, Y. Lu, C. Corton, and C. Klaassen. Sex-, Age-, and Race/Ethnicity-Dependent Variations in Drug-Processing and NRF2-Regulated Genes in Human Livers.   DRUG METABOLISM AND DISPOSITION. American Society for Pharmacology and Experimental Therapeutics, Bethesda, MD, USA, 49(1): 111-119, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jon Corton",
+                "hasEmail": "mailto:corton.chris@epa.gov"
+            },
+            "description": "Data was generated at KUMC, not EPA. There is no EPA data that is part of this submission. \n\nThis dataset is associated with the following publication:\nLiu, J., J.Y. Cui, Y. Lu, C. Corton, and C. Klaassen. Sex-, Age-, and Race/Ethnicity-Dependent Variations in Drug-Processing and NRF2-Regulated Genes in Human Livers.   DRUG METABOLISM AND DISPOSITION. American Society for Pharmacology and Experimental Therapeutics, Bethesda, MD, USA, 49(1): 111-119, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518913/Liu_DMD_2021_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Liu_DMD_2021_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518913",
             "keyword": [
@@ -133276,20 +133280,10 @@
                 "Race/ethnicity",
                 "Diseased liver samples"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Liu_DMD_2021_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518913/Liu_DMD_2021_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-06-20",
-            "references": [
-                "https://doi.org/10.1124/dmd.120.000181"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133299,19 +133293,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1124/dmd.120.000181"
+            ],
+            "rights": null,
+            "title": "ORD-037657: Sex-, age-, race-, and disease-dependent variations in NRF2-regulated genes in human livers"
         },
         {
-            "title": "Predicted Background Conductivity Data ",
-            "description": "This \"Predicted Background Conductivity\" view consists of a shapefile derived from National Hydrography Dataset Plus Version 2.0 which displays modeled natural background conductivity for the continental United States.\nThe displayed information is based on specific conductivity predictions for stream segments in the contiguous United States from the Natural Background Specific Conductivity (NBSC) model. The NBSC model was developed using a random forest modeling approach and enables comparison with measured in-stream conductivity. Geology, soil, vegetation, climate and other empirically measured data were used as inputs. The NBSC model was designed for streams with natural background SC < 2000 \u00b5S/cm.  Above this level (typical for freshwater), NBSC model estimates may be less reliable.  Data for some parameters that affect background SC were not readily available and were therefore not included in the model. These include freshwater and marine interfaces, natural mineral springs, salt deposits which may affect groundwater and streams, and other natural sources of salts.  In such areas, the model is likely to underestimate SC. Local knowledge is often necessary to assess differences between predicted and measured background SC. More information about the model and datasets can be found at Freshwater Explorer Story Metadata.\nThe calculated predicted background conductivity for individual stream segments in the contiguous U.S.A. and metadata are accessible from the ArcGIS platform on Predicted Background Conductivity Data.  Data is available as table (from Data) or in by pointing and clicking on a stream segment (from Visualization) (https://arcg.is/9vnrv).  This data set is used in the Freshwater Explorer Beta 0.1 which on Jan. 2020 is password protected but can be obtained by requesting access from cormier.susan@epa.gov and then using the link: https://arcg.is/KHb9S. \n\nThis dataset is associated with the following publication:\nOlson, J., and S. Cormier. Modeling spatial and temporal variation in natural background specific conductivity.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(8): 4316-4325, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Susan Cormier",
+                "hasEmail": "mailto:cormier.susan@epa.gov"
+            },
+            "description": "This \"Predicted Background Conductivity\" view consists of a shapefile derived from National Hydrography Dataset Plus Version 2.0 which displays modeled natural background conductivity for the continental United States.\nThe displayed information is based on specific conductivity predictions for stream segments in the contiguous United States from the Natural Background Specific Conductivity (NBSC) model. The NBSC model was developed using a random forest modeling approach and enables comparison with measured in-stream conductivity. Geology, soil, vegetation, climate and other empirically measured data were used as inputs. The NBSC model was designed for streams with natural background SC < 2000 \u00b5S/cm.  Above this level (typical for freshwater), NBSC model estimates may be less reliable.  Data for some parameters that affect background SC were not readily available and were therefore not included in the model. These include freshwater and marine interfaces, natural mineral springs, salt deposits which may affect groundwater and streams, and other natural sources of salts.  In such areas, the model is likely to underestimate SC. Local knowledge is often necessary to assess differences between predicted and measured background SC. More information about the model and datasets can be found at Freshwater Explorer Story Metadata.\nThe calculated predicted background conductivity for individual stream segments in the contiguous U.S.A. and metadata are accessible from the ArcGIS platform on Predicted Background Conductivity Data.  Data is available as table (from Data) or in by pointing and clicking on a stream segment (from Visualization) (https://arcg.is/9vnrv).  This data set is used in the Freshwater Explorer Beta 0.1 which on Jan. 2020 is password protected but can be obtained by requesting access from cormier.susan@epa.gov and then using the link: https://arcg.is/KHb9S. \n\nThis dataset is associated with the following publication:\nOlson, J., and S. Cormier. Modeling spatial and temporal variation in natural background specific conductivity.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(8): 4316-4325, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://arcg.is/9vnrv",
+                    "title": "https://arcg.is/9vnrv"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1517581",
             "keyword": [
@@ -133321,19 +133324,10 @@
                 "Carbonate Salts",
                 "modeled conductivity"
             ],
-            "contactPoint": {
-                "fn": "Susan Cormier",
-                "hasEmail": "mailto:cormier.susan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://arcg.is/9vnrv",
-                    "accessURL": "https://arcg.is/9vnrv"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-01",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b06777"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133343,40 +133337,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b06777"
+            ],
+            "rights": null,
+            "title": "Predicted Background Conductivity Data "
         },
         {
-            "title": "Rainfall Washoff of Spores Dataset",
-            "description": "Spore washoff data from concrete and asphalt coupons generated with rainfall simulator. \n\nThis dataset is associated with the following publication:\nMikelonis, A., W. Calfee, S. Lee, A. Touati, and K. Ratliff. Rainfall Washoff of Spores from Concrete and Asphalt Surfaces.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 57(3): e2020WR028533, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
-            "identifier": "https://doi.org/10.23719/1518925",
-            "keyword": [
-                "stormwater",
-                "emergency response",
-                "anthrax"
-            ],
             "contactPoint": {
                 "fn": "Anne Mikelonis",
                 "hasEmail": "mailto:mikelonis.anne@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1518925/documents/DataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Spore washoff data from concrete and asphalt coupons generated with rainfall simulator. \n\nThis dataset is associated with the following publication:\nMikelonis, A., W. Calfee, S. Lee, A. Touati, and K. Ratliff. Rainfall Washoff of Spores from Concrete and Asphalt Surfaces.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 57(3): e2020WR028533, (2021).",
             "distribution": [
                 {
-                    "title": "2020WashoffPaperDataset.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518925/2020WashoffPaperDataset.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2020WashoffPaperDataset.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518925",
+            "keyword": [
+                "stormwater",
+                "emergency response",
+                "anthrax"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-23",
-            "references": [
-                "https://doi.org/10.1029/2020wr028533"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133387,42 +133383,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1518925/documents/DataDictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1029/2020wr028533"
+            ],
+            "rights": null,
+            "title": "Rainfall Washoff of Spores Dataset"
         },
         {
-            "title": "Links to Freshwater Explorer datasets A-cjtc 20190408",
-            "description": "These are data stored on the EPA GeoPlatform based on ArcGis (ESRI). They are in the form ArcGis tables or Excel files.\n\nThis \"Predicted Background Conductivity\" view consists of a shapefile derived from National Hydrography Dataset Plus Version 2.0 which displays modeled natural background conductivity for the continental United States.  The Natural Background Specific Conductivity (NBSC) contains predicted natural background conductivity using geology, soil, climate and other input parameters. \n\nThe \"National Measured Conductivity Data - WQP\" view consists of a shapefile derived from data stored in the U.S. EPA Water Quality Portal. The \"National Measured Conductivity Data - WQP\" is based on measured data obtained from the U.S. EPA Water Quality Portal (WQP) data inventory - the nation's largest source for water quality monitoring data. Data were downloaded from the WQP website using the following query criteria: Country - United States.\n\u2022\tSample Media - Water. \n\u2022\tCharacteristics - Conductivity, Specific Conductivity, Specific Conductance, Calculated/Measured Ratio.\n\u2022\tDate range - 1 January 2000 to 01 November 2019.\n\nThe \"National Measured Conductivity Data - NWIS\" view consists of a shapefile derived from United States Geological Survey (USGS) National Water Information System (NWIS) data. The information displayed is based on measured specific conductivity (SC) data retrieved from the USGS NWIS. NWIS data are based upon consistent, documented sample collection and measurement techniques, as well as consistent data reporting. Data was downloaded for river and stream sampling sites between January 1, 1984 and April 20, 2018. Data collected prior to 1984 were excluded because analytical methods used by USGS prior to that date are less reliable. The downloaded dataset includes more than 1 million water chemistry measurements, collected at 65,698 NWIS sampling stations in the continental U.S. (covering all states and most ecoregions).\n\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503696",
-            "keyword": [
-                "stream",
-                "conductivity",
-                "background",
-                "biological effect level",
-                "story map'"
-            ],
             "contactPoint": {
                 "fn": "Susan Cormier",
                 "hasEmail": "mailto:cormier.susan@epa.gov"
             },
+            "description": "These are data stored on the EPA GeoPlatform based on ArcGis (ESRI). They are in the form ArcGis tables or Excel files.\n\nThis \"Predicted Background Conductivity\" view consists of a shapefile derived from National Hydrography Dataset Plus Version 2.0 which displays modeled natural background conductivity for the continental United States.  The Natural Background Specific Conductivity (NBSC) contains predicted natural background conductivity using geology, soil, climate and other input parameters. \n\nThe \"National Measured Conductivity Data - WQP\" view consists of a shapefile derived from data stored in the U.S. EPA Water Quality Portal. The \"National Measured Conductivity Data - WQP\" is based on measured data obtained from the U.S. EPA Water Quality Portal (WQP) data inventory - the nation's largest source for water quality monitoring data. Data were downloaded from the WQP website using the following query criteria: Country - United States.\n\u2022\tSample Media - Water. \n\u2022\tCharacteristics - Conductivity, Specific Conductivity, Specific Conductance, Calculated/Measured Ratio.\n\u2022\tDate range - 1 January 2000 to 01 November 2019.\n\nThe \"National Measured Conductivity Data - NWIS\" view consists of a shapefile derived from United States Geological Survey (USGS) National Water Information System (NWIS) data. The information displayed is based on measured specific conductivity (SC) data retrieved from the USGS NWIS. NWIS data are based upon consistent, documented sample collection and measurement techniques, as well as consistent data reporting. Data was downloaded for river and stream sampling sites between January 1, 1984 and April 20, 2018. Data collected prior to 1984 were excluded because analytical methods used by USGS prior to that date are less reliable. The downloaded dataset includes more than 1 million water chemistry measurements, collected at 65,698 NWIS sampling stations in the continental U.S. (covering all states and most ecoregions).\n\n",
             "distribution": [
                 {
-                    "title": "Links to Freshwater Explorer datasets A-cjtc 20190408.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503696/Links%20to%20Freshwater%20Explorer%20datasets%20A-cjtc%2020190408.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Links to Freshwater Explorer datasets A-cjtc 20190408.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503696",
+            "keyword": [
+                "stream",
+                "conductivity",
+                "background",
+                "biological effect level",
+                "story map'"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-19",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -133431,20 +133427,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Links to Freshwater Explorer datasets A-cjtc 20190408"
         },
         {
-            "title": "Challenges and Opportunities for Translational Research on Congenital Anomalies of External Genitalia: Summary of an NIDDK/AUA Workshop",
-            "description": "This was a summary article from a workshop and did not produce new data. This dataset is not publicly accessible because: This was a summary article from a workshop and did not produce new data. It can be accessed through the following means: Data mentioned in this workshop review can be accessed by accessing the original sources of information, as cited within the review. Format: Not applicable. \n\nThis dataset is associated with the following publication:\nStadler, H.S., C. Peters, R. Sturm, L. Baker, C. Best, V. Byrd, F. Geller, D. Hoshizaki, T. Knudsen, J. Norton, R. Romao, and M. Cohn. Challenges and Opportunities for Translational Research on Congenital Anomalies of External Genitalia:\nSummary of an NIDDK/AUA Workshop.   Journal of Pediatric Urology. Elsevier B.V., Amsterdam,  NETHERLANDS, 16(6): 791-804, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Thomas Knudsen",
+                "hasEmail": "mailto:knudsen.thomas@epa.gov"
+            },
+            "description": "This was a summary article from a workshop and did not produce new data. This dataset is not publicly accessible because: This was a summary article from a workshop and did not produce new data. It can be accessed through the following means: Data mentioned in this workshop review can be accessed by accessing the original sources of information, as cited within the review. Format: Not applicable. \n\nThis dataset is associated with the following publication:\nStadler, H.S., C. Peters, R. Sturm, L. Baker, C. Best, V. Byrd, F. Geller, D. Hoshizaki, T. Knudsen, J. Norton, R. Romao, and M. Cohn. Challenges and Opportunities for Translational Research on Congenital Anomalies of External Genitalia:\nSummary of an NIDDK/AUA Workshop.   Journal of Pediatric Urology. Elsevier B.V., Amsterdam,  NETHERLANDS, 16(6): 791-804, (2020).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1518712",
             "keyword": [
                 "genitourinary development",
@@ -133453,14 +133451,10 @@
                 "hypospadias",
                 "endocrine disruption"
             ],
-            "contactPoint": {
-                "fn": "Thomas Knudsen",
-                "hasEmail": "mailto:knudsen.thomas@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-03-03",
-            "references": [
-                "https://doi.org/10.1016/j.jpurol.2020.09.012"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133470,19 +133464,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jpurol.2020.09.012"
+            ],
+            "rights": null,
+            "title": "Challenges and Opportunities for Translational Research on Congenital Anomalies of External Genitalia: Summary of an NIDDK/AUA Workshop"
         },
         {
-            "title": "DWTRs_Data_P_Sorption_Capacity_Manuscript_Data ",
-            "description": "DWTRs Data and P sorption capacity. \n\nThis dataset is associated with the following publication:\nAment, M.R., S.E. Hurley, M. Voorhees, E. Perkins, Y. Yuan, J.W. Faulkner, and E.D. Roy. Balancing Hydraulic Control and Phosphorus Removal in Bioretention Media Amended with Drinking Water Treatment Residuals.   ACS ES&T Water. American Chemical Society, Washington, DC, USA, 1(3): 688\u2013697, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Yongping Yuan",
+                "hasEmail": "mailto:yuan.yongping@epa.gov"
+            },
+            "description": "DWTRs Data and P sorption capacity. \n\nThis dataset is associated with the following publication:\nAment, M.R., S.E. Hurley, M. Voorhees, E. Perkins, Y. Yuan, J.W. Faulkner, and E.D. Roy. Balancing Hydraulic Control and Phosphorus Removal in Bioretention Media Amended with Drinking Water Treatment Residuals.   ACS ES&T Water. American Chemical Society, Washington, DC, USA, 1(3): 688\u2013697, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518687/DWTRs_Data_P_Sorption_Capacity_Manuscript_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DWTRs_Data_P_Sorption_Capacity_Manuscript_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518687",
             "keyword": [
@@ -133493,20 +133497,10 @@
                 "Hydraulic Conductivity",
                 "drinking water treatment residuals"
             ],
-            "contactPoint": {
-                "fn": "Yongping Yuan",
-                "hasEmail": "mailto:yuan.yongping@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "DWTRs_Data_P_Sorption_Capacity_Manuscript_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518687/DWTRs_Data_P_Sorption_Capacity_Manuscript_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-29",
-            "references": [
-                "https://doi.org/10.1021/acsestwater.0c00178"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133516,19 +133510,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acsestwater.0c00178"
+            ],
+            "rights": null,
+            "title": "DWTRs_Data_P_Sorption_Capacity_Manuscript_Data "
         },
         {
-            "title": "Reactive Organic Carbon Emissions from Volatile Chemical Products",
-            "description": "VCPy was developed to predict evaporative emissions of VOCs from volatile chemical products. The data contains python code and inputs for VCPy v1.0 as well as an excel file containing values from the main text figures in the work of Seltzer et al. (Atmospheric Chemistry and Physics, 2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Havala Pye",
+                "hasEmail": "mailto:pye.havala@epa.gov"
+            },
+            "description": "VCPy was developed to predict evaporative emissions of VOCs from volatile chemical products. The data contains python code and inputs for VCPy v1.0 as well as an excel file containing values from the main text figures in the work of Seltzer et al. (Atmospheric Chemistry and Physics, 2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520157/maintext_figs.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "maintext_figs.xlsx"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520157/VCPy.v1.0.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "VCPy.v1.0.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520157",
             "keyword": [
@@ -133543,24 +133552,11 @@
                 "Semivolatile Organic Compounds (SVOCs)",
                 "Biogenic VOC"
             ],
-            "contactPoint": {
-                "fn": "Havala Pye",
-                "hasEmail": "mailto:pye.havala@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "maintext_figs.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520157/maintext_figs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "VCPy.v1.0.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520157/VCPy.v1.0.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-03",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -133569,31 +133565,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Reactive Organic Carbon Emissions from Volatile Chemical Products"
         },
         {
-            "title": "\uf0c6 ghioandrew_fulvicacid_fig5A.xlsx ",
-            "description": "Excel files for \"A fulvic acid-like substance participates in the pro-inflammatory effects of cigarette smoke and wood smoke particles\". This dataset is not publicly accessible because: Not applicable. It can be accessed through the following means: M:/ghioandrew_fulvicacid_fig5A.xlsx. Format: Excel file",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1506013",
-            "keyword": [
-                "air pollution"
-            ],
             "contactPoint": {
                 "fn": "Andrew Ghio",
                 "hasEmail": "mailto:ghio.andy@epa.gov"
             },
+            "description": "Excel files for \"A fulvic acid-like substance participates in the pro-inflammatory effects of cigarette smoke and wood smoke particles\". This dataset is not publicly accessible because: Not applicable. It can be accessed through the following means: M:/ghioandrew_fulvicacid_fig5A.xlsx. Format: Excel file",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1506013",
+            "keyword": [
+                "air pollution"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-19",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -133602,19 +133598,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "\uf0c6 ghioandrew_fulvicacid_fig5A.xlsx "
         },
         {
-            "title": "Evaluation of 15 years of modeled NOX across the contiguous United States",
-            "description": "These files contain observed and CMAQ estimated gas species data that were used in the analysis documented in the manuscript \u201cEvaluation of 15 years of modeled NOX across the contiguous United States\u201d. The files are packages as a set of .csv, .zip and .tar.gz files that correspond to different plots and analyses in the paper.  Metadata about each file is available in the Data Dictionary.  The data are available on Zenodo: https://doi.org/10.5281/zenodo.4589604",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Keith Appel",
+                "hasEmail": "mailto:appel.wyat@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520141/documents/ToroEtAl_2021_Elementa_Data_Dictionary.pdf",
+            "describedByType": "application/pdf",
+            "description": "These files contain observed and CMAQ estimated gas species data that were used in the analysis documented in the manuscript \u201cEvaluation of 15 years of modeled NOX across the contiguous United States\u201d. The files are packages as a set of .csv, .zip and .tar.gz files that correspond to different plots and analyses in the paper.  Metadata about each file is available in the Data Dictionary.  The data are available on Zenodo: https://doi.org/10.5281/zenodo.4589604",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.5281/zenodo.4589604",
+                    "title": "https://doi.org/10.5281/zenodo.4589604"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520141",
             "keyword": [
@@ -133626,18 +133631,11 @@
                 "air quality modeling",
                 "model evaluation"
             ],
-            "contactPoint": {
-                "fn": "Keith Appel",
-                "hasEmail": "mailto:appel.wyat@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.5281/zenodo.4589604",
-                    "accessURL": "https://doi.org/10.5281/zenodo.4589604"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-01",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -133647,20 +133645,26 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520141/documents/ToroEtAl_2021_Elementa_Data_Dictionary.pdf",
-            "describedByType": "application/pdf"
+            "references": null,
+            "rights": null,
+            "title": "Evaluation of 15 years of modeled NOX across the contiguous United States"
         },
         {
-            "title": "Martin et al_Eucalyptus High Carbohydrate Challenge_All data ",
-            "description": "The file contains all individual values used to generate means and standard deviations presented in the tables and figures reported in this manuscript. \n\nThis dataset is associated with the following publication:\nMartin, B., L. Thompson, Y. Kim, S. Snow, M.C. Schladweiler, P. Phillips, M. Harmon, C. King, J. Richards, I. George, K. Martin, N.H. Coates, I. Gilmour, U. Kodavanti, M. Hazari, and A. Farraj. A Single Exposure to Eucalyptus Smoke Sensitizes Rats to the Postprandial Cardiovascular Effects of a High Carbohydrate Oral Load.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 32(8): 342-353, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Aimen Farraj",
+                "hasEmail": "mailto:farraj.aimen@epa.gov"
+            },
+            "description": "The file contains all individual values used to generate means and standard deviations presented in the tables and figures reported in this manuscript. \n\nThis dataset is associated with the following publication:\nMartin, B., L. Thompson, Y. Kim, S. Snow, M.C. Schladweiler, P. Phillips, M. Harmon, C. King, J. Richards, I. George, K. Martin, N.H. Coates, I. Gilmour, U. Kodavanti, M. Hazari, and A. Farraj. A Single Exposure to Eucalyptus Smoke Sensitizes Rats to the Postprandial Cardiovascular Effects of a High Carbohydrate Oral Load.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 32(8): 342-353, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518662/FarrajAimen_A-dv4m_All%20Data_August-17-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FarrajAimen_A-dv4m_All Data_August-17-2020.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518662",
             "keyword": [
@@ -133678,20 +133682,10 @@
                 "biomass",
                 "Risk"
             ],
-            "contactPoint": {
-                "fn": "Aimen Farraj",
-                "hasEmail": "mailto:farraj.aimen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "FarrajAimen_A-dv4m_All Data_August-17-2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518662/FarrajAimen_A-dv4m_All%20Data_August-17-2020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-05-06",
-            "references": [
-                "https://doi.org/10.1080/08958378.2020.1809572"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133701,49 +133695,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08958378.2020.1809572"
+            ],
+            "rights": null,
+            "title": "Martin et al_Eucalyptus High Carbohydrate Challenge_All data "
         },
         {
-            "title": "Spatiotemporal variability of ammonia across the contiguous United States",
-            "description": "These data are monthly mean annual CMAQ simulations as described in the manuscript. \n\nThis dataset is associated with the following publication:\nWang, R., X. Guo, D.  Pan, J. Kelly, J. Bash, K. Sun, F. Paulot, L. Clarisse, M. Van Damme, S. Whitburn, P. Coheur, C. Clerbaux, and M.A. Zondlo. Monthly Patterns of Ammonia Over the Contiguous United States at 2-km Resolution.   GEOPHYSICAL RESEARCH LETTERS. American Geophysical Union, Washington, DC, USA, 48(5): e2020GL090579, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520484",
-            "keyword": [
-                "CMAQ",
-                "ammonia",
-                "IASI",
-                "pm2.5",
-                "Satellite Air-Quality"
-            ],
             "contactPoint": {
                 "fn": "Jesse Bash",
                 "hasEmail": "mailto:bash.jesse@epa.gov"
             },
+            "description": "These data are monthly mean annual CMAQ simulations as described in the manuscript. \n\nThis dataset is associated with the following publication:\nWang, R., X. Guo, D.  Pan, J. Kelly, J. Bash, K. Sun, F. Paulot, L. Clarisse, M. Van Damme, S. Whitburn, P. Coheur, C. Clerbaux, and M.A. Zondlo. Monthly Patterns of Ammonia Over the Contiguous United States at 2-km Resolution.   GEOPHYSICAL RESEARCH LETTERS. American Geophysical Union, Washington, DC, USA, 48(5): e2020GL090579, (2021).",
             "distribution": [
                 {
-                    "title": "https://github.com/USEPA/CMAQ/",
-                    "accessURL": "https://github.com/USEPA/CMAQ/"
+                    "accessURL": "https://github.com/USEPA/CMAQ/",
+                    "title": "https://github.com/USEPA/CMAQ/"
                 },
                 {
-                    "title": "https://iasi.aeris-data.fr/nh3/",
-                    "accessURL": "https://iasi.aeris-data.fr/nh3/"
+                    "accessURL": "https://iasi.aeris-data.fr/nh3/",
+                    "title": "https://iasi.aeris-data.fr/nh3/"
                 },
                 {
-                    "title": "https://www.gfdl.noaa.gov/am3/",
-                    "accessURL": "https://www.gfdl.noaa.gov/am3/"
+                    "accessURL": "https://www.gfdl.noaa.gov/am3/",
+                    "title": "https://www.gfdl.noaa.gov/am3/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520484",
+            "keyword": [
+                "CMAQ",
+                "ammonia",
+                "IASI",
+                "pm2.5",
+                "Satellite Air-Quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-09",
-            "references": [
-                "https://doi.org/10.1029/2020gl090579"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133753,19 +133747,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2020gl090579"
+            ],
+            "rights": null,
+            "title": "Spatiotemporal variability of ammonia across the contiguous United States"
         },
         {
-            "title": "Rapid production of highly oxidized molecules in isoprene aerosol via peroxy and alkoxy radical isomerization pathways in low and high NOx environments: Combined laboratory, computational and field studies",
-            "description": "Recently, we identified seven novel hydroxy-carboxylic acids resulting from gas-phase reactions of isoprene in the presence of nitrogen oxides (NOx), ozone (O3), and/or hydroxyl radicals (OH). In the present study, we provide evidence that hydroxy-carboxylic acids, namely methyltartaric acids (MTA) are: (1) reliable isoprene tracers, (2) likely produced via rapid peroxy radical hydrogen atom(H) shift reactions (autoxidation mechanism) and analogous alkoxy radical H shifts in low and high NOx environments respectively and (3) representative of aged ambient aerosol in the low NOx regime. Firstly, MTA are reliable tracers of isoprene aerosol because they have been identified in numerous chamber experiments involving isoprene conducted under a wide range of conditions and are absent in the oxidation of mono- and sesquiterpenes. They are also present in numerous samples of ambient aerosol collected during the past 20 years at several locations in the U.S. and Europe. Furthermore, MTA concentrations measured during a year-long field study in Research Triangle Park (RTP), NC in 2003 show a seasonal trend consistent with isoprene emissions and photochemical activity. Secondly, an analysis of chemical ionization mass spectrometer (CIMS) data of several chamber experiments in low and high NOx environments show that highly oxidized molecules (HOMs) derived from isoprene that lead to MTAs may be produced rapidly and considered as early generation isoprene oxidation products in the gas phase. Density functional theory calculations show that rapid intramolecular H shifts involving peroxy and alkoxy radicals possess low barriers for methyl-hydroxy-butenals (MHBs) that may represent precursors for MTA. From these results, a viable rapid H shift mechanism is proposed to occur that produces isoprene derived HOMs like MTA. Finally, an analysis of the mechanism shows that autoxidation-like pathways in low and high NOx may produce HOMs in a few OH oxidation steps like commonly detected methyl tetrol (MT) isoprene tracers. The ratio of MTA/MT in isoprene aerosol is also shown to be significantly greater in field versus chamber samples indicating the importance of such pathways in the atmosphere even for smaller hydrocarbons like isoprene. \n\nThis dataset is associated with the following publication:\nJaoui, M., I. Piletic, R. Szmigielski, K.J. Rudzinski, M. Lewandowski, T. Riedel, and T. Kleindienst. Rapid production of highly oxidized molecules in isoprene aerosol via peroxy and alkoxy radical isomerization pathways in low and high NOx environments: Combined laboratory, computational and field studies.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 775: 145592, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Mohammed Jaoui",
+                "hasEmail": "mailto:jaoui.mohammed@epa.gov"
+            },
+            "description": "Recently, we identified seven novel hydroxy-carboxylic acids resulting from gas-phase reactions of isoprene in the presence of nitrogen oxides (NOx), ozone (O3), and/or hydroxyl radicals (OH). In the present study, we provide evidence that hydroxy-carboxylic acids, namely methyltartaric acids (MTA) are: (1) reliable isoprene tracers, (2) likely produced via rapid peroxy radical hydrogen atom(H) shift reactions (autoxidation mechanism) and analogous alkoxy radical H shifts in low and high NOx environments respectively and (3) representative of aged ambient aerosol in the low NOx regime. Firstly, MTA are reliable tracers of isoprene aerosol because they have been identified in numerous chamber experiments involving isoprene conducted under a wide range of conditions and are absent in the oxidation of mono- and sesquiterpenes. They are also present in numerous samples of ambient aerosol collected during the past 20 years at several locations in the U.S. and Europe. Furthermore, MTA concentrations measured during a year-long field study in Research Triangle Park (RTP), NC in 2003 show a seasonal trend consistent with isoprene emissions and photochemical activity. Secondly, an analysis of chemical ionization mass spectrometer (CIMS) data of several chamber experiments in low and high NOx environments show that highly oxidized molecules (HOMs) derived from isoprene that lead to MTAs may be produced rapidly and considered as early generation isoprene oxidation products in the gas phase. Density functional theory calculations show that rapid intramolecular H shifts involving peroxy and alkoxy radicals possess low barriers for methyl-hydroxy-butenals (MHBs) that may represent precursors for MTA. From these results, a viable rapid H shift mechanism is proposed to occur that produces isoprene derived HOMs like MTA. Finally, an analysis of the mechanism shows that autoxidation-like pathways in low and high NOx may produce HOMs in a few OH oxidation steps like commonly detected methyl tetrol (MT) isoprene tracers. The ratio of MTA/MT in isoprene aerosol is also shown to be significantly greater in field versus chamber samples indicating the importance of such pathways in the atmosphere even for smaller hydrocarbons like isoprene. \n\nThis dataset is associated with the following publication:\nJaoui, M., I. Piletic, R. Szmigielski, K.J. Rudzinski, M. Lewandowski, T. Riedel, and T. Kleindienst. Rapid production of highly oxidized molecules in isoprene aerosol via peroxy and alkoxy radical isomerization pathways in low and high NOx environments: Combined laboratory, computational and field studies.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 775: 145592, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518750/Part2_Iso-Aging_ScienceHub_entry-Data_Final_gcms.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Part2_Iso-Aging_ScienceHub_entry-Data_Final_gcms.xlsx"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518750/Part2_Iso-Aging_ScienceHub_entry-Data_Final_CIMS.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Part2_Iso-Aging_ScienceHub_entry-Data_Final_CIMS.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518750",
             "keyword": [
@@ -133781,25 +133790,10 @@
                 "LC-Orbitrap",
                 "mass spectrometry"
             ],
-            "contactPoint": {
-                "fn": "Mohammed Jaoui",
-                "hasEmail": "mailto:jaoui.mohammed@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Part2_Iso-Aging_ScienceHub_entry-Data_Final_gcms.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518750/Part2_Iso-Aging_ScienceHub_entry-Data_Final_gcms.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "Part2_Iso-Aging_ScienceHub_entry-Data_Final_CIMS.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518750/Part2_Iso-Aging_ScienceHub_entry-Data_Final_CIMS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-22",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2021.145592"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133809,19 +133803,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2021.145592"
+            ],
+            "rights": null,
+            "title": "Rapid production of highly oxidized molecules in isoprene aerosol via peroxy and alkoxy radical isomerization pathways in low and high NOx environments: Combined laboratory, computational and field studies"
         },
         {
-            "title": "Risk-based Decision Support Tool (DST) for TMDL analysis and Watershed Health assessment demonstration dataset (Upper Mississippi River Basin, Ohio River Basin, Maumee River Basin)",
-            "description": "The data set is composed of inputs and outputs of the DST demonstration and application to risk-based TMDLs and water quality risk assessment in Midwest river basins (Upper Mississippi River, Ohio River, and Maumee River). Portions of this dataset are inaccessible because: Too large. They can be accessed through the following means: The data is available in this directory: C:\\Users\\MHantush\\OneDrive - Environmental Protection Agency (EPA)\\ScienceHUB\\Risk-Based WH-TMDL Tool\\gis_files. Format: GIS data files. \n\nThis dataset is associated with the following publication:\nMallya, G., A. Gupta, M.M. Hantush, and R.S. Govindaraju. Uncertainty quantification in reconstruction of sparse water quality time series: Implications for watershed health and risk-based TMDL assessment.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 131: 104735, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Mohamed Hantush",
+                "hasEmail": "mailto:hantush.mohamed@epa.gov"
+            },
+            "description": "The data set is composed of inputs and outputs of the DST demonstration and application to risk-based TMDLs and water quality risk assessment in Midwest river basins (Upper Mississippi River, Ohio River, and Maumee River). Portions of this dataset are inaccessible because: Too large. They can be accessed through the following means: The data is available in this directory: C:\\Users\\MHantush\\OneDrive - Environmental Protection Agency (EPA)\\ScienceHUB\\Risk-Based WH-TMDL Tool\\gis_files. Format: GIS data files. \n\nThis dataset is associated with the following publication:\nMallya, G., A. Gupta, M.M. Hantush, and R.S. Govindaraju. Uncertainty quantification in reconstruction of sparse water quality time series: Implications for watershed health and risk-based TMDL assessment.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 131: 104735, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521110/ezD4762734_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ezD4762734_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521110",
             "keyword": [
@@ -133834,20 +133838,10 @@
                 "uncertainty quantification",
                 "LOADEST"
             ],
-            "contactPoint": {
-                "fn": "Mohamed Hantush",
-                "hasEmail": "mailto:hantush.mohamed@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ezD4762734_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521110/ezD4762734_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-05-27",
-            "references": [
-                "https://doi.org/10.1016/j.envsoft.2020.104735"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133857,41 +133851,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envsoft.2020.104735"
+            ],
+            "rights": null,
+            "title": "Risk-based Decision Support Tool (DST) for TMDL analysis and Watershed Health assessment demonstration dataset (Upper Mississippi River Basin, Ohio River Basin, Maumee River Basin)"
         },
         {
-            "title": "Vitamin D deficiency causes cardiac dysfunction mediated by TRPC6_complete data",
-            "description": "Cardiovascular effects of vitamin D deficiency and pharmacological characterization of the role of TRPC6 in the effects. \n\nThis dataset is associated with the following publication:\nStratford, K., N. Coates, L. Thompson, A. Farraj, and M. Hazari. Early-life persistent vitamin D deficiency-induced cardiovascular dysfunction in mice is mediated by Transit Receptor Potential C Channels.   The Journal of Steroid Biochemistry and Molecular Bio. ELSEVIER, AMSTERDAM,  HOLLAND, 206(105804): 1, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503424",
-            "keyword": [
-                "vitamin d deficiency",
-                "cardiovascular",
-                "TRPC6",
-                "Hypertension"
-            ],
             "contactPoint": {
                 "fn": "Mehdi Hazari",
                 "hasEmail": "mailto:hazari.mehdi@epa.gov"
             },
+            "description": "Cardiovascular effects of vitamin D deficiency and pharmacological characterization of the role of TRPC6 in the effects. \n\nThis dataset is associated with the following publication:\nStratford, K., N. Coates, L. Thompson, A. Farraj, and M. Hazari. Early-life persistent vitamin D deficiency-induced cardiovascular dysfunction in mice is mediated by Transit Receptor Potential C Channels.   The Journal of Steroid Biochemistry and Molecular Bio. ELSEVIER, AMSTERDAM,  HOLLAND, 206(105804): 1, (2021).",
             "distribution": [
                 {
-                    "title": "KS5_VDD TRPC6_Complete data set.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503424/KS5_VDD%20TRPC6_Complete%20data%20set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "KS5_VDD TRPC6_Complete data set.xlsx"
                 }
             ],
-            "modified": "2019-02-21",
-            "references": [
-                "https://doi.org/10.1016/j.jsbmb.2020.105804"
+            "identifier": "https://doi.org/10.23719/1503424",
+            "keyword": [
+                "vitamin d deficiency",
+                "cardiovascular",
+                "TRPC6",
+                "Hypertension"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
+            "modified": "2019-02-21",
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133901,53 +133895,54 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jsbmb.2020.105804"
+            ],
+            "rights": null,
+            "title": "Vitamin D deficiency causes cardiac dysfunction mediated by TRPC6_complete data"
         },
         {
-            "title": "Collodal-Copper based pesticide and wood preservatives against microbial acitivies",
-            "description": "Copper-based pesticides and wood preservative fungicides could end up in the environment during production, use, and end-of-life via different pathways that could cause unintended ecological and adverse health effects. This research provides the effect of colloid-size Cu-based pesticides (), micronized Cu azole (MCA-1 and MCA-2) and alkaline Cu quaternary (ACQ) treated woods, ionic Cu, ionic Cu spiked untreated wood (UTW), and CuCO3 solutions against Gram-positive Bacillus species using five-day biochemical oxygen demand (BOD5) standard test. \n\nThis dataset is associated with the following publications:\nTegenaw, A., G.A. Sorial , and E. Sahle-Demessie. Effect of colloid-size copper-based pesticides and wood preservatives against microbial activities of Gram-positive Bacillus species using five-day biochemical oxygen demand test.   Journal of Environmental Sciences. Elsevier BV, AMSTERDAM,  NETHERLANDS, 105: 71-80, (2021).\nTegenaw, A., G.A. Sorial, E. Sahle-Demessie, and C. Han. Role of water chemistry on stability, aggregation, and dissolution of uncoated and carbon-coated copper nanoparticles.   ENVIRONMENTAL RESEARCH. Elsevier B.V., Amsterdam,  NETHERLANDS, 187: 109700, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520884",
-            "keyword": [
-                "Bacillus species",
-                "BOD5",
-                "Colloid-size Cu-based pesticides",
-                "Leaching",
-                "Wood preservatives"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520884/documents/Data%20Dictionary_Copper_Nanopesticide_March21.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Copper-based pesticides and wood preservative fungicides could end up in the environment during production, use, and end-of-life via different pathways that could cause unintended ecological and adverse health effects. This research provides the effect of colloid-size Cu-based pesticides (), micronized Cu azole (MCA-1 and MCA-2) and alkaline Cu quaternary (ACQ) treated woods, ionic Cu, ionic Cu spiked untreated wood (UTW), and CuCO3 solutions against Gram-positive Bacillus species using five-day biochemical oxygen demand (BOD5) standard test. \n\nThis dataset is associated with the following publications:\nTegenaw, A., G.A. Sorial , and E. Sahle-Demessie. Effect of colloid-size copper-based pesticides and wood preservatives against microbial activities of Gram-positive Bacillus species using five-day biochemical oxygen demand test.   Journal of Environmental Sciences. Elsevier BV, AMSTERDAM,  NETHERLANDS, 105: 71-80, (2021).\nTegenaw, A., G.A. Sorial, E. Sahle-Demessie, and C. Han. Role of water chemistry on stability, aggregation, and dissolution of uncoated and carbon-coated copper nanoparticles.   ENVIRONMENTAL RESEARCH. Elsevier B.V., Amsterdam,  NETHERLANDS, 187: 109700, (2020).",
             "distribution": [
                 {
-                    "title": "Ayu_Cu-NPs_Supplemental Data_Journal of Environmental Management.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520884/Ayu_Cu-NPs_Supplemental%20Data_Journal%20of%20Environmental%20Management.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Ayu_Cu-NPs_Supplemental Data_Journal of Environmental Management.docx"
                 },
                 {
-                    "title": "Ayu_Paper_Figure_file.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520884/Ayu_Paper_Figure_file.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Ayu_Paper_Figure_file.docx"
                 },
                 {
-                    "title": "Ayu_Manuscript_Journal of Environmental Management GS and Sahle Demmessie edits (003).docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520884/Ayu_Manuscript_Journal%20of%20Environmental%20Management%20GS%20and%20Sahle%20Demmessie%20edits%20%28003%29.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Ayu_Manuscript_Journal of Environmental Management GS and Sahle Demmessie edits (003).docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520884",
+            "keyword": [
+                "Bacillus species",
+                "BOD5",
+                "Colloid-size Cu-based pesticides",
+                "Leaching",
+                "Wood preservatives"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-08-04",
-            "references": [
-                "https://doi.org/10.1016/j.jes.2020.12.037",
-                "https://doi.org/10.1016/j.envres.2020.109700"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -133958,41 +133953,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520884/documents/Data%20Dictionary_Copper_Nanopesticide_March21.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.jes.2020.12.037",
+                "https://doi.org/10.1016/j.envres.2020.109700"
+            ],
+            "rights": null,
+            "title": "Collodal-Copper based pesticide and wood preservatives against microbial acitivies"
         },
         {
-            "title": "Machine Learning Modeling of Water Quality Based Risk Assessment",
-            "description": "This is the geospatial and hydroclimate input data used to develop data-driven Machine Learning (ML) models as well as model estimated water quality based risk metrics and watershed health composite measure in three river basins in the Midwest. Model outputs that are used to construct the figures in the paper are displayed in the Excel file with the definitions of the data reported in each datasheet. The directory to the GIS data that were used to construct the inputs and spatially distributed risk metrics at the HUC-10 level is listed here and in the Scientific Data Management Plan. Portions of this dataset are inaccessible because: Large size GIS database. They can be accessed through the following means: C:\\Users\\MHantush\\OneDrive - Environmental Protection Agency (EPA)\\ScienceHUB\\WH ML Modeling. Format: Generic GIS database. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1521112",
-            "keyword": [
-                "machine learning",
-                "water quality",
-                "Risk analysis",
-                "Ungauged Watersheds"
-            ],
             "contactPoint": {
                 "fn": "Mohamed Hantush",
                 "hasEmail": "mailto:hantush.mohamed@epa.gov"
             },
+            "description": "This is the geospatial and hydroclimate input data used to develop data-driven Machine Learning (ML) models as well as model estimated water quality based risk metrics and watershed health composite measure in three river basins in the Midwest. Model outputs that are used to construct the figures in the paper are displayed in the Excel file with the definitions of the data reported in each datasheet. The directory to the GIS data that were used to construct the inputs and spatially distributed risk metrics at the HUC-10 level is listed here and in the Scientific Data Management Plan. Portions of this dataset are inaccessible because: Large size GIS database. They can be accessed through the following means: C:\\Users\\MHantush\\OneDrive - Environmental Protection Agency (EPA)\\ScienceHUB\\WH ML Modeling. Format: Generic GIS database. ",
             "distribution": [
                 {
-                    "title": "ezD4762735_Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521112/ezD4762735_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ezD4762735_Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521112",
+            "keyword": [
+                "machine learning",
+                "water quality",
+                "Risk analysis",
+                "Ungauged Watersheds"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2019-10-17",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -134001,19 +133997,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Machine Learning Modeling of Water Quality Based Risk Assessment"
         },
         {
-            "title": "Bioactivity screening of environmental chemicals using imaging-based high-throughput phenotypic profiling",
-            "description": "In the present study, we adapted an existing phenotypic profiling assay (\u201cCell Painting\u201d, (Bray et al., 2016)) to be compatible with in-house microfluidics capabilities for 384-well culture format, chemical exposures and fluorescent cytochemistry in order to facilitate concentration-response screening of several hundred environmental chemicals. In this assay, human-derived cells were labeled with multiple fluorescent probes to visualize various subcellular organelles and structural features. High content image analysis workflows were used to measure hundreds of morphological features at the level of the individual cell (i.e. shape of the cells, intensity, texture and distribution of fluorescent labels, etc.). The resultant data were then used to calculate well-level summary values, perform high-throughput concentration-response modeling and generate phenotypic response profiles. First, we identified and screened a set of candidate phenotypic reference chemicals for use as plate-based controls for evaluating HTPP assay performance during large-scale screening studies and identified an optimal exposure duration for HTPP screening. Second, we screened a set of 462 environmental chemicals in the U-2 OS cell model and derived in vitro potency estimates for bioactivity of all active chemicals. In addition, we demonstrated the technical reproducibility of the HTPP assay in concentration-response screening mode using the previously identified phenotypic reference chemicals. Next, we used reverse dosimetry to calculate administered equivalent doses (AEDs) corresponding to the thresholds for chemical bioactivity and compared those values to in vivo effect values from mammalian toxicity studies. \n\nThis dataset is associated with the following publication:\nNyffeler, J., C. Willis, R. Lougee, A. Richard, K. Friedman, and J. Harrill. Bioactivity screening of environmental chemicals using imaging-based high-throughput phenotypic profiling.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 389: 114876, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Joshua Harrill",
+                "hasEmail": "mailto:harrill.joshua@epa.gov"
+            },
+            "description": "In the present study, we adapted an existing phenotypic profiling assay (\u201cCell Painting\u201d, (Bray et al., 2016)) to be compatible with in-house microfluidics capabilities for 384-well culture format, chemical exposures and fluorescent cytochemistry in order to facilitate concentration-response screening of several hundred environmental chemicals. In this assay, human-derived cells were labeled with multiple fluorescent probes to visualize various subcellular organelles and structural features. High content image analysis workflows were used to measure hundreds of morphological features at the level of the individual cell (i.e. shape of the cells, intensity, texture and distribution of fluorescent labels, etc.). The resultant data were then used to calculate well-level summary values, perform high-throughput concentration-response modeling and generate phenotypic response profiles. First, we identified and screened a set of candidate phenotypic reference chemicals for use as plate-based controls for evaluating HTPP assay performance during large-scale screening studies and identified an optimal exposure duration for HTPP screening. Second, we screened a set of 462 environmental chemicals in the U-2 OS cell model and derived in vitro potency estimates for bioactivity of all active chemicals. In addition, we demonstrated the technical reproducibility of the HTPP assay in concentration-response screening mode using the previously identified phenotypic reference chemicals. Next, we used reverse dosimetry to calculate administered equivalent doses (AEDs) corresponding to the thresholds for chemical bioactivity and compared those values to in vivo effect values from mammalian toxicity studies. \n\nThis dataset is associated with the following publication:\nNyffeler, J., C. Willis, R. Lougee, A. Richard, K. Friedman, and J. Harrill. Bioactivity screening of environmental chemicals using imaging-based high-throughput phenotypic profiling.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 389: 114876, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Nyffeler/Bioactivity_screening_of_environmental_chemicals/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Nyffeler/Bioactivity_screening_of_environmental_chemicals/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520454",
             "keyword": [
@@ -134024,19 +134027,10 @@
                 "concentration response",
                 "cell painting"
             ],
-            "contactPoint": {
-                "fn": "Joshua Harrill",
-                "hasEmail": "mailto:harrill.joshua@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Nyffeler/Bioactivity_screening_of_environmental_chemicals/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Nyffeler/Bioactivity_screening_of_environmental_chemicals/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-20",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2019.114876"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134046,19 +134040,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2019.114876"
+            ],
+            "rights": null,
+            "title": "Bioactivity screening of environmental chemicals using imaging-based high-throughput phenotypic profiling"
         },
         {
-            "title": "Effects-based monitoring of bioactive contaminants discharged to the Colorado River before and after a municipal wastewater treatment facility replacement",
-            "description": "The present study highlights the utility of bioeffects-based monitoring in conjunction with analytical chemical measurements of surface waters on the Colorado River associated with a historically bioactive wastewater treatment plant effluent. Concurrent with chemical monitoring and in vitro bioactivity measurements, in situ caged fish systems were employed to evaluate the potential bioavailability of predicted biologically-active contaminants associated with ER, GR, and PPAR-associated activities. The present study compares the effects of a wastewater treatment plant facility upgrade on bioactive contaminant loading. \n\nThis dataset is associated with the following publication:\nCavallin, J., W. Battaglin, J. Beihoffer, B. Blackwell, P. Bradley, A. Cole, D. Ekman, R. Hofer, J. Kinsey, K. Keteles, D. Winkelman, and D. Villeneuve. Effects-Based Monitoring of Bioactive Chemicals Discharged to the Colorado River Before and After a Municipal Wastewater Treatment Plant Replacement.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(2): 974-984, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Daniel Villeneuve",
+                "hasEmail": "mailto:villeneuve.dan@epa.gov"
+            },
+            "description": "The present study highlights the utility of bioeffects-based monitoring in conjunction with analytical chemical measurements of surface waters on the Colorado River associated with a historically bioactive wastewater treatment plant effluent. Concurrent with chemical monitoring and in vitro bioactivity measurements, in situ caged fish systems were employed to evaluate the potential bioavailability of predicted biologically-active contaminants associated with ER, GR, and PPAR-associated activities. The present study compares the effects of a wastewater treatment plant facility upgrade on bioactive contaminant loading. \n\nThis dataset is associated with the following publication:\nCavallin, J., W. Battaglin, J. Beihoffer, B. Blackwell, P. Bradley, A. Cole, D. Ekman, R. Hofer, J. Kinsey, K. Keteles, D. Winkelman, and D. Villeneuve. Effects-Based Monitoring of Bioactive Chemicals Discharged to the Colorado River Before and After a Municipal Wastewater Treatment Plant Replacement.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(2): 974-984, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519052/Cavallin%20et%20al_Moab%20caged%20fish_Science%20Hub_12-15-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Cavallin et al_Moab caged fish_Science Hub_12-15-2020.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1519052",
             "keyword": [
@@ -134071,20 +134075,10 @@
                 "screening and prioritization",
                 "aquatic ecosystems"
             ],
-            "contactPoint": {
-                "fn": "Daniel Villeneuve",
-                "hasEmail": "mailto:villeneuve.dan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Cavallin et al_Moab caged fish_Science Hub_12-15-2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519052/Cavallin%20et%20al_Moab%20caged%20fish_Science%20Hub_12-15-2020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-07-10",
-            "references": [
-                "https://doi.org/10.1021/acs.est.0c05269"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134094,41 +134088,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.0c05269"
+            ],
+            "rights": null,
+            "title": "Effects-based monitoring of bioactive contaminants discharged to the Colorado River before and after a municipal wastewater treatment facility replacement"
         },
         {
-            "title": "Metadata Files for Structure-based QSAR models to predict repeat dose toxicity points of departure",
-            "description": "This paper describes a model to take chemical structures and predict a property (the point of departure) for a new chemical. No new data were generated. The contents of this zip file contains metadata that you could use to make a model prediction. It does contain all of the code and a help file describing how to run the model. \n\nThis dataset is associated with the following publication:\nPradeep, P., K. Paul-Friedman, and R. Judson. Structure-based QSAR Models to Predict Repeat Dose Toxicity Points of Departure.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 16(November 2020): 100139, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520778",
-            "keyword": [
-                "systemic toxicity",
-                "point of departure",
-                "qsar",
-                "repeat dose toxicity"
-            ],
             "contactPoint": {
                 "fn": "Richard Judson",
                 "hasEmail": "mailto:judson.richard@epa.gov"
             },
+            "description": "This paper describes a model to take chemical structures and predict a property (the point of departure) for a new chemical. No new data were generated. The contents of this zip file contains metadata that you could use to make a model prediction. It does contain all of the code and a help file describing how to run the model. \n\nThis dataset is associated with the following publication:\nPradeep, P., K. Paul-Friedman, and R. Judson. Structure-based QSAR Models to Predict Repeat Dose Toxicity Points of Departure.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 16(November 2020): 100139, (2020).",
             "distribution": [
                 {
-                    "title": "Pradeep et al QSAR Models Supp Data Files.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520778/Pradeep%20et%20al%20QSAR%20Models%20Supp%20Data%20Files.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Pradeep et al QSAR Models Supp Data Files.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520778",
+            "keyword": [
+                "systemic toxicity",
+                "point of departure",
+                "qsar",
+                "repeat dose toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-09-24",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2020.100139"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134138,40 +134132,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2020.100139"
+            ],
+            "rights": null,
+            "title": "Metadata Files for Structure-based QSAR models to predict repeat dose toxicity points of departure"
         },
         {
-            "title": "Evaluation of polycyclic aromatic hydrocarbons in fine particulate matter censoring-related bias.csv",
-            "description": "The case study data are selected from an EPA study using cookstove combustion experiments to measure polycyclic aromatic hydrocarbon (PAH) concentrations in particulate matter (PM) and were determined using gas chromatography-mass spectrometry (GC-MS) (Shen et al. 2017). Chromatograms of particle emissions reported in Shen et al. (2017) were reanalyzed for the case study to quantify previously censored measurements where the signal-to-noise ratio was >1. \n\nThis dataset is associated with the following publication:\nGeorge, B., L. Gains-Germain, K. Broms, K. Black, M. Furman, M. Hays, K. Thomas, and J.E. Simmons. Censoring Trace-Level Environmental Data: Statistical Analysis Considerations to Limit Bias.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(6): 3786-3795, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1517601",
-            "keyword": [
-                "nondetects",
-                "censoring",
-                "bias"
-            ],
             "contactPoint": {
                 "fn": "Barbara George",
                 "hasEmail": "mailto:george.bj@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517601/documents/data%20dictionary%20-%20Evaluation%20of%20polycyclic%20aromatic%20hydrocarbons%20in%20fine%20particulate%20matter%20censoring-related%20bias.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The case study data are selected from an EPA study using cookstove combustion experiments to measure polycyclic aromatic hydrocarbon (PAH) concentrations in particulate matter (PM) and were determined using gas chromatography-mass spectrometry (GC-MS) (Shen et al. 2017). Chromatograms of particle emissions reported in Shen et al. (2017) were reanalyzed for the case study to quantify previously censored measurements where the signal-to-noise ratio was >1. \n\nThis dataset is associated with the following publication:\nGeorge, B., L. Gains-Germain, K. Broms, K. Black, M. Furman, M. Hays, K. Thomas, and J.E. Simmons. Censoring Trace-Level Environmental Data: Statistical Analysis Considerations to Limit Bias.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 55(6): 3786-3795, (2021).",
             "distribution": [
                 {
-                    "title": "Evaluation of polycyclic aromatic hydrocarbons in fine particulate matter censoring-related bias.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517601/Evaluation%20of%20polycyclic%20aromatic%20hydrocarbons%20in%20fine%20particulate%20matter%20censoring-related%20bias.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Evaluation of polycyclic aromatic hydrocarbons in fine particulate matter censoring-related bias.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517601",
+            "keyword": [
+                "nondetects",
+                "censoring",
+                "bias"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-14",
-            "references": [
-                "https://doi.org/10.1021/acs.est.0c02256"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134182,43 +134178,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517601/documents/data%20dictionary%20-%20Evaluation%20of%20polycyclic%20aromatic%20hydrocarbons%20in%20fine%20particulate%20matter%20censoring-related%20bias.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/acs.est.0c02256"
+            ],
+            "rights": null,
+            "title": "Evaluation of polycyclic aromatic hydrocarbons in fine particulate matter censoring-related bias.csv"
         },
         {
-            "title": "Dataset for ORD-033344: A Set of Six Gene Expression Biomarkers Identify Rat Liver Tumorigens in Short-Term Assays",
-            "description": "Microarray experiments used in the study. \n\nThis dataset is associated with the following publication:\nCorton, J., T. Hill, J. Sutherland, J. Stevens, and J. Rooney. A Set of Six Gene Expression Biomarkers Identify Rat Liver Tumorigens in Short-Term Assays.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  177(1): 11-26, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504416",
-            "keyword": [
-                "2 year bioassay",
-                "adverse outcome pathway",
-                "molecular initiating event",
-                "toxicogenomics",
-                "liver cancer"
-            ],
             "contactPoint": {
                 "fn": "Jon Corton",
                 "hasEmail": "mailto:corton.chris@epa.gov"
             },
+            "description": "Microarray experiments used in the study. \n\nThis dataset is associated with the following publication:\nCorton, J., T. Hill, J. Sutherland, J. Stevens, and J. Rooney. A Set of Six Gene Expression Biomarkers Identify Rat Liver Tumorigens in Short-Term Assays.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  177(1): 11-26, (2020).",
             "distribution": [
                 {
-                    "title": "Data submission for A-fn3f.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504416/Data%20submission%20for%20A-fn3f.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-fn3f.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504416",
+            "keyword": [
+                "2 year bioassay",
+                "adverse outcome pathway",
+                "molecular initiating event",
+                "toxicogenomics",
+                "liver cancer"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-09",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfaa101"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134228,80 +134222,80 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfaa101"
+            ],
+            "rights": null,
+            "title": "Dataset for ORD-033344: A Set of Six Gene Expression Biomarkers Identify Rat Liver Tumorigens in Short-Term Assays"
         },
         {
-            "title": "Total column NO2 from ground based pandora spectrometers at nine locations across the New York City metropolitan. ",
-            "description": "Airborne and ground-based Pandora spectrometer NO2 column measurements were collected during the 2018 Long Island Sound Tropospheric Ozone Study (LISTOS) in the New York City/Long Island Sound region, which coincided with early observations from the Sentinel-5P TROPOspheric Monitoring Instrument (TROPOMI) instrument. Both airborne- and ground-based measurements are used to evaluate the TROPOMI NO2 Tropospheric Vertical Column (TrVC) product v1.2 in this region, which has high spatial and temporal heterogeneity in NO2. First, airborne and Pandora TrVCs are compared to evaluate the uncertainty of the airborne TrVC and establish the spatial representativeness of the Pandora observations. The 171 coincidences between Pandora and airborne TrVCs are found to be highly correlated (r2=\u20090.92 and slope of 1.03), with the largest individual differences being associated with high temporal and/or spatial variability. These reference measurements (Pandora and airborne) are complementary with respect to temporal coverage and spatial representativity. Pandora spectrometers can provide continuous long-term measurements but may lack areal representativity when operated in direct-sun mode. Airborne spectrometers are typically only deployed for short periods of time, but their observations are more spatially representative of the satellite measurements with the added capability of retrieving at subpixel resolutions of 250\u2009m\u2009\u00d7\u2009250\u2009m over the entire TROPOMI pixels they overfly. Thus, airborne data are more correlated with TROPOMI measurements (r2=0.96) than Pandora measurements are with TROPOMI (r2=0.84). The largest outliers between TROPOMI and the reference measurements appear to stem from too spatially coarse a priori surface reflectivity (0.5\u2218) over bright urban scenes. In this work, this results during cloud-free scenes that, at times, are affected by errors in the TROPOMI cloud pressure retrieval impacting the calculation of tropospheric air mass factors. This factor causes a high bias in TROPOMI TrVCs of 4\u2009%\u201311\u2009%. Excluding these cloud-impacted points, TROPOMI has an overall low bias of 19\u2009%\u201333\u2009% during the LISTOS timeframe of June\u2013September 2018. Part of this low bias is caused by coarse a priori profile input from the TM5-MP model; replacing these profiles with those from a 12\u2009km North American Model\u2013Community Multiscale Air Quality (NAMCMAQ) analysis results in a 12\u2009%\u201314\u2009% increase in the TrVCs. Even with this improvement, the TROPOMI-NAMCMAQ TrVCs have a 7\u2009%\u201319\u2009% low bias, indicating needed improvement in a priori assumptions in the air mass factor calculation. Future work should explore additional impacts of a priori inputs to further assess the remaining low biases in TROPOMI using these datasets. \n\nThis dataset is associated with the following publication:\nJudd, L., J. Al-Saadi, J. Szykman, L. Valin, A. Nehrir, S. Janz, M. Kowalewski, R. Swap , D. Williams, H. Eskes, J.P.  Veefkind, A. Cede, M. Mueller, M. Gebetsberger, and R.B. Pierce. Evaluating Sentinel-5P TROPOMI tropospheric NO2 column densities with airborne and Pandora spectrometers near New York City and Long Island Sound.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 13(11): 6113-6140, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1519060",
-            "keyword": [
-                "Nitrogen and Co-pollutants",
-                "Tropospheric column NO2",
-                "Pandora spectrometer",
-                "S5P-TROPOMI",
-                "air quality",
-                "air emissions",
-                "nitrogen di",
-                "regional ozone modeling"
-            ],
             "contactPoint": {
                 "fn": "James Szykman",
                 "hasEmail": "mailto:szykman.jim@epa.gov"
             },
+            "description": "Airborne and ground-based Pandora spectrometer NO2 column measurements were collected during the 2018 Long Island Sound Tropospheric Ozone Study (LISTOS) in the New York City/Long Island Sound region, which coincided with early observations from the Sentinel-5P TROPOspheric Monitoring Instrument (TROPOMI) instrument. Both airborne- and ground-based measurements are used to evaluate the TROPOMI NO2 Tropospheric Vertical Column (TrVC) product v1.2 in this region, which has high spatial and temporal heterogeneity in NO2. First, airborne and Pandora TrVCs are compared to evaluate the uncertainty of the airborne TrVC and establish the spatial representativeness of the Pandora observations. The 171 coincidences between Pandora and airborne TrVCs are found to be highly correlated (r2=\u20090.92 and slope of 1.03), with the largest individual differences being associated with high temporal and/or spatial variability. These reference measurements (Pandora and airborne) are complementary with respect to temporal coverage and spatial representativity. Pandora spectrometers can provide continuous long-term measurements but may lack areal representativity when operated in direct-sun mode. Airborne spectrometers are typically only deployed for short periods of time, but their observations are more spatially representative of the satellite measurements with the added capability of retrieving at subpixel resolutions of 250\u2009m\u2009\u00d7\u2009250\u2009m over the entire TROPOMI pixels they overfly. Thus, airborne data are more correlated with TROPOMI measurements (r2=0.96) than Pandora measurements are with TROPOMI (r2=0.84). The largest outliers between TROPOMI and the reference measurements appear to stem from too spatially coarse a priori surface reflectivity (0.5\u2218) over bright urban scenes. In this work, this results during cloud-free scenes that, at times, are affected by errors in the TROPOMI cloud pressure retrieval impacting the calculation of tropospheric air mass factors. This factor causes a high bias in TROPOMI TrVCs of 4\u2009%\u201311\u2009%. Excluding these cloud-impacted points, TROPOMI has an overall low bias of 19\u2009%\u201333\u2009% during the LISTOS timeframe of June\u2013September 2018. Part of this low bias is caused by coarse a priori profile input from the TM5-MP model; replacing these profiles with those from a 12\u2009km North American Model\u2013Community Multiscale Air Quality (NAMCMAQ) analysis results in a 12\u2009%\u201314\u2009% increase in the TrVCs. Even with this improvement, the TROPOMI-NAMCMAQ TrVCs have a 7\u2009%\u201319\u2009% low bias, indicating needed improvement in a priori assumptions in the air mass factor calculation. Future work should explore additional impacts of a priori inputs to further assess the remaining low biases in TROPOMI using these datasets. \n\nThis dataset is associated with the following publication:\nJudd, L., J. Al-Saadi, J. Szykman, L. Valin, A. Nehrir, S. Janz, M. Kowalewski, R. Swap , D. Williams, H. Eskes, J.P.  Veefkind, A. Cede, M. Mueller, M. Gebetsberger, and R.B. Pierce. Evaluating Sentinel-5P TROPOMI tropospheric NO2 column densities with airborne and Pandora spectrometers near New York City and Long Island Sound.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 13(11): 6113-6140, (2020).",
             "distribution": [
                 {
-                    "title": "https://s5phub.copernicus.eu/dhus/#/home",
-                    "accessURL": "https://s5phub.copernicus.eu/dhus/#/home"
+                    "accessURL": "https://s5phub.copernicus.eu/dhus/#/home",
+                    "title": "https://s5phub.copernicus.eu/dhus/#/home"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?NASA-AIRCRAFT=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?NASA-AIRCRAFT=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?NASA-AIRCRAFT=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?NASA-AIRCRAFT=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-WESTPORT=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-WESTPORT=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-WESTPORT=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-WESTPORT=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-RUTGERS=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-RUTGERS=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-RUTGERS=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-RUTGERS=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BAYONNE=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BAYONNE=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BAYONNE=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BAYONNE=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BRONX-PFIZER=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BRONX-PFIZER=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BRONX-PFIZER=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-BRONX-PFIZER=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-QUEENS-COLLEGE=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-QUEENS-COLLEGE=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-QUEENS-COLLEGE=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-QUEENS-COLLEGE=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-NEW-HAVEN=1"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-HAMMONASSET=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-HAMMONASSET=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-HAMMONASSET=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/listos?GROUND-HAMMONASSET=1"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519060",
+            "keyword": [
+                "Nitrogen and Co-pollutants",
+                "Tropospheric column NO2",
+                "Pandora spectrometer",
+                "S5P-TROPOMI",
+                "air quality",
+                "air emissions",
+                "nitrogen di",
+                "regional ozone modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-06",
-            "references": [
-                "https://doi.org/10.5194/amt-13-6113-2020"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134311,19 +134305,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-13-6113-2020"
+            ],
+            "rights": null,
+            "title": "Total column NO2 from ground based pandora spectrometers at nine locations across the New York City metropolitan. "
         },
         {
-            "title": "Maumee River 2012 and 2016",
-            "description": "The Maumee River and associated tributaries are an example of a system influenced by a mosaic of contaminant inputs from point and nonpoint sources along a gradient of land uses. To assess the potential effects of contaminants on aquatic biota in a system this complex requires a combination of targeted and nontargeted analytical and biological monitoring techniques to provide data that can be assembled and interpreted in an integrated manner. The aim of the current paper was to provide a practical demonstration of this type of approach using a variety of state-of-the-science pathway-based tools. Studies conducted in 2012 and 2106 showed that contaminants in the upper part of the Maumee River reflect agricultural practices, while downstream, the suite of chemicals present includes those from agriculture in conjunction with contaminants more indicative of a general urban setting, influenced in some areas by WWTP inputs. Biological responses using in vitro assays with surface water samples, and measures of biological responses in caged fish deployed a various sites in the Maumee River were used to assess the potential for perturbation of specific biological pathways. Overall there was little evidence for contaminant effects on endocrine pathways involved is reproduction or development. However, multiple lines of evidence suggested the presence of contaminants that could inhibit or induce  cytochrome P450-based enzymes thereby influencing biological pathways/processes associated with these ubiquitous proteins. \n\nThis dataset is associated with the following publication:\nAnkley, G., J. Berninger, B. Blackwell, J. Cavallin, T. Collette, D. Ekman, K. Fay, D. Feifarek, K. Jensen, M. Kahl, J. Mosley, S. Poole, E. Randolph, D. Rearick, A. Schroeder, J. Swintek, and D. Villeneuve. Pathway-based approaches for assessing biological hazards of complex mixtures of contaminants: A case study in the Maumee River.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 40(4): 1098\u20131122, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Gerald Ankley",
+                "hasEmail": "mailto:ankley.gerald@epa.gov"
+            },
+            "description": "The Maumee River and associated tributaries are an example of a system influenced by a mosaic of contaminant inputs from point and nonpoint sources along a gradient of land uses. To assess the potential effects of contaminants on aquatic biota in a system this complex requires a combination of targeted and nontargeted analytical and biological monitoring techniques to provide data that can be assembled and interpreted in an integrated manner. The aim of the current paper was to provide a practical demonstration of this type of approach using a variety of state-of-the-science pathway-based tools. Studies conducted in 2012 and 2106 showed that contaminants in the upper part of the Maumee River reflect agricultural practices, while downstream, the suite of chemicals present includes those from agriculture in conjunction with contaminants more indicative of a general urban setting, influenced in some areas by WWTP inputs. Biological responses using in vitro assays with surface water samples, and measures of biological responses in caged fish deployed a various sites in the Maumee River were used to assess the potential for perturbation of specific biological pathways. Overall there was little evidence for contaminant effects on endocrine pathways involved is reproduction or development. However, multiple lines of evidence suggested the presence of contaminants that could inhibit or induce  cytochrome P450-based enzymes thereby influencing biological pathways/processes associated with these ubiquitous proteins. \n\nThis dataset is associated with the following publication:\nAnkley, G., J. Berninger, B. Blackwell, J. Cavallin, T. Collette, D. Ekman, K. Fay, D. Feifarek, K. Jensen, M. Kahl, J. Mosley, S. Poole, E. Randolph, D. Rearick, A. Schroeder, J. Swintek, and D. Villeneuve. Pathway-based approaches for assessing biological hazards of complex mixtures of contaminants: A case study in the Maumee River.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 40(4): 1098\u20131122, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520748/Maumee%20Bay%20Science%20Hub%20File_Revised.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Maumee Bay Science Hub File_Revised.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520748",
             "keyword": [
@@ -134335,20 +134339,10 @@
                 "aquatic ecosystems",
                 "screening and prioritization"
             ],
-            "contactPoint": {
-                "fn": "Gerald Ankley",
-                "hasEmail": "mailto:ankley.gerald@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Maumee Bay Science Hub File_Revised.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520748/Maumee%20Bay%20Science%20Hub%20File_Revised.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-01",
-            "references": [
-                "https://doi.org/10.1002/etc.4949"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134358,73 +134352,73 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4949"
+            ],
+            "rights": null,
+            "title": "Maumee River 2012 and 2016"
         },
         {
-            "title": "A fulvic acid-like substance participates in the pro-inflammatory effects of cigarette smoke and wood smoke particles",
-            "description": "We tested the postulate that 1) a fulvic acid (FA)-like substance is included in cigarette smoke and wood smoke particles and 2) exposure of respiratory epithelial cells to this substance results in a disruption of iron homeostasis associated with both a cell deficiency of the metal and inflammatory response. It was concluded that 1) FA-like substance is included in cigarette smoke and wood smoke particle and 2) respiratory epithelial cell exposure to this substance results in a disruption of iron homeostasis associated with both a cell deficiency of the metal and inflammatory response. \n\nThis dataset is associated with the following publication:\nGonzalez, D., J. Soukup, M. Madden, M. Hays, J. Berntsen, S. Paulson, and A. Ghio. A fulvic acid-like substance participates in the pro-inflammatory effects of cigarette smoke and wood smoke particles..   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 33(4): 999-1009, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504592",
-            "keyword": [
-                "air pollution"
-            ],
             "contactPoint": {
                 "fn": "Andrew Ghio",
                 "hasEmail": "mailto:ghio.andy@epa.gov"
             },
+            "description": "We tested the postulate that 1) a fulvic acid (FA)-like substance is included in cigarette smoke and wood smoke particles and 2) exposure of respiratory epithelial cells to this substance results in a disruption of iron homeostasis associated with both a cell deficiency of the metal and inflammatory response. It was concluded that 1) FA-like substance is included in cigarette smoke and wood smoke particle and 2) respiratory epithelial cell exposure to this substance results in a disruption of iron homeostasis associated with both a cell deficiency of the metal and inflammatory response. \n\nThis dataset is associated with the following publication:\nGonzalez, D., J. Soukup, M. Madden, M. Hays, J. Berntsen, S. Paulson, and A. Ghio. A fulvic acid-like substance participates in the pro-inflammatory effects of cigarette smoke and wood smoke particles..   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 33(4): 999-1009, (2020).",
             "distribution": [
                 {
-                    "title": "ghioandrew_fulvicacid_fig5A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig5A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig5A.xlsx"
                 },
                 {
-                    "title": "ghioandrew_fulvicacid_fig5B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig5B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig5B.xlsx"
                 },
                 {
-                    "title": "ghioandrew_fulvicacid_fig6A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig6A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig6A.xlsx"
                 },
                 {
-                    "title": "ghioandrew_fulvicacid_fig6B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig6B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig6B.xlsx"
                 },
                 {
-                    "title": "ghioandrew_fulvicacid_fig7A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig7A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig7A.xlsx"
                 },
                 {
-                    "title": "ghioandrew_fulvicacid_fig7B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig7B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig7B.xlsx"
                 },
                 {
-                    "title": "ghioandrew_fulvicacid_fig8A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig8A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig8A.xlsx"
                 },
                 {
-                    "title": "ghioandrew_fulvicacid_fig8B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504592/ghioandrew_fulvicacid_fig8B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ghioandrew_fulvicacid_fig8B.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504592",
+            "keyword": [
+                "air pollution"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-10-10",
-            "references": [
-                "https://doi.org/10.1021/acs.chemrestox.0c00036"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134434,42 +134428,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.chemrestox.0c00036"
+            ],
+            "rights": null,
+            "title": "A fulvic acid-like substance participates in the pro-inflammatory effects of cigarette smoke and wood smoke particles"
         },
         {
-            "title": "Extrapolating In Vitro and Ex Vivo Screening Assay Data for Thyroperoxidase Inhibition to Predict Serum Thyroid Hormones in the Rat ",
-            "description": "This data set is a dose response analysis of two thyroid hormone synthesis disruptors in adult male rats. Data included serum and thyroid gland concentrations of the two chemicals tested, propylthiouracil and methimazole, as well as serum and thyroid gland hormone concentrations. These data were critical for developing a model linking highthroughput assay data on synthesis inhibition to make predictions of thyroid hormone in serum. \n\nThis dataset is associated with the following publication:\nHassan, I., H. El-Masri, J. Ford, A. Brennan, S. Handa, K. Friedman, and M. Gilbert. Extrapolating In Vitro and Ex Vivo Screening Assay Data for Thyroperoxidase Inhibition to Predict Serum Thyroid Hormones in the Rat.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  173(2): 280-292, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504091",
-            "keyword": [
-                "Thyroperoxidase",
-                "thyroid hormone",
-                "mathematical model",
-                "In vitro assay",
-                "Ex vivo"
-            ],
             "contactPoint": {
                 "fn": "Mary Gilbert",
                 "hasEmail": "mailto:gilbert.mary@epa.gov"
             },
+            "description": "This data set is a dose response analysis of two thyroid hormone synthesis disruptors in adult male rats. Data included serum and thyroid gland concentrations of the two chemicals tested, propylthiouracil and methimazole, as well as serum and thyroid gland hormone concentrations. These data were critical for developing a model linking highthroughput assay data on synthesis inhibition to make predictions of thyroid hormone in serum. \n\nThis dataset is associated with the following publication:\nHassan, I., H. El-Masri, J. Ford, A. Brennan, S. Handa, K. Friedman, and M. Gilbert. Extrapolating In Vitro and Ex Vivo Screening Assay Data for Thyroperoxidase Inhibition to Predict Serum Thyroid Hormones in the Rat.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  173(2): 280-292, (2020).",
             "distribution": [
                 {
-                    "title": "PTU and MMI TPO Inhibition Data for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504091/PTU%20and%20MMI%20TPO%20Inhibition%20Data%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PTU and MMI TPO Inhibition Data for Science Hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504091",
+            "keyword": [
+                "Thyroperoxidase",
+                "thyroid hormone",
+                "mathematical model",
+                "In vitro assay",
+                "Ex vivo"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-10-08",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfz227"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134479,19 +134473,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfz227"
+            ],
+            "rights": null,
+            "title": "Extrapolating In Vitro and Ex Vivo Screening Assay Data for Thyroperoxidase Inhibition to Predict Serum Thyroid Hormones in the Rat "
         },
         {
-            "title": "LMR_spatial_temporal_analysis_data",
-            "description": "This file includes the following data for 25 stream sites in the Little Miami River watershed: diatom operational taxonomic units with their numbers and relative abundances of rbcL gene sequence reads, watershed land cover, and nutrient concentration and conductivity data. \n\nThis dataset is associated with the following publication:\nYuan, L., N. Smucker, C. Nietch, and E. Pilgrim. Quantifying spatial and temporal relationships between diatoms and nutrients in streams strengthens evidence of nutrient effects from monitoring data.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  41(1): 100-112, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Erik Pilgrim",
+                "hasEmail": "mailto:pilgrim.erik@epa.gov"
+            },
+            "description": "This file includes the following data for 25 stream sites in the Little Miami River watershed: diatom operational taxonomic units with their numbers and relative abundances of rbcL gene sequence reads, watershed land cover, and nutrient concentration and conductivity data. \n\nThis dataset is associated with the following publication:\nYuan, L., N. Smucker, C. Nietch, and E. Pilgrim. Quantifying spatial and temporal relationships between diatoms and nutrients in streams strengthens evidence of nutrient effects from monitoring data.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  41(1): 100-112, (2022).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521154/LMR_Stats_data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LMR_Stats_data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521154",
             "keyword": [
@@ -134506,20 +134510,10 @@
                 "diatoms",
                 "rbcL"
             ],
-            "contactPoint": {
-                "fn": "Erik Pilgrim",
-                "hasEmail": "mailto:pilgrim.erik@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "LMR_Stats_data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521154/LMR_Stats_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-07-02",
-            "references": [
-                "https://doi.org/10.1086/718631"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134529,42 +134523,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1086/718631"
+            ],
+            "rights": null,
+            "title": "LMR_spatial_temporal_analysis_data"
         },
         {
-            "title": "LP QPCR vs Culture",
-            "description": "Tap water samples measure for Legionella pneumophila  (by QPCR and culture), heterotrophic bacteria, and chlorine residual. \n\nThis dataset is associated with the following publication:\nDonohue, M. Quantification of Legionella pneumophila by qPCR and Culture in Tap Water with Different Concentrations of Residual Disinfectants and Heterotrophic Bacteria.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 774: 145142, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1518684",
-            "keyword": [
-                "Legionella pneumophila",
-                "qPCR",
-                "culture",
-                "chlorine residual",
-                "tap water"
-            ],
             "contactPoint": {
                 "fn": "Maura Donohue",
                 "hasEmail": "mailto:donohue.maura@epa.gov"
             },
+            "description": "Tap water samples measure for Legionella pneumophila  (by QPCR and culture), heterotrophic bacteria, and chlorine residual. \n\nThis dataset is associated with the following publication:\nDonohue, M. Quantification of Legionella pneumophila by qPCR and Culture in Tap Water with Different Concentrations of Residual Disinfectants and Heterotrophic Bacteria.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 774: 145142, (2021).",
             "distribution": [
                 {
-                    "title": "SciHub Lp QPCR vs Culture.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518684/SciHub%20Lp%20QPCR%20vs%20Culture.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub Lp QPCR vs Culture.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518684",
+            "keyword": [
+                "Legionella pneumophila",
+                "qPCR",
+                "culture",
+                "chlorine residual",
+                "tap water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-05-11",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2021.145142"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134574,43 +134568,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2021.145142"
+            ],
+            "rights": null,
+            "title": "LP QPCR vs Culture"
         },
         {
-            "title": "Integrated Assessment Model for Valuing Water Quality Changes_BENSPLASH Input Data",
-            "description": "Input to EPA BENSPLASH model for Republican River example.  Dataset contains COMID, DATE, PARAMETER, and VALUE.  The baseline file contains current information, the scenario file includes the results of applying the scenario described in the publication. \n\nThis dataset is associated with the following publication:\nCorona, J., T. Doley, C. Griffiths, M. Massey, C. Moore, S. Muela, B. Rashleigh, W. Wheeler, S. Whitlock, and J. Hewitt. An Integrated Assessment Model for Valuing Water Quality Changes in the US.   Land Economics. University of Wisconsin Press, Madison, WI, USA, 96(4): 478-492, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1521093",
-            "keyword": [
-                "water quality benefits"
-            ],
             "contactPoint": {
                 "fn": "Brenda Rashleigh",
                 "hasEmail": "mailto:rashleigh.brenda@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1521093/documents/DataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Input to EPA BENSPLASH model for Republican River example.  Dataset contains COMID, DATE, PARAMETER, and VALUE.  The baseline file contains current information, the scenario file includes the results of applying the scenario described in the publication. \n\nThis dataset is associated with the following publication:\nCorona, J., T. Doley, C. Griffiths, M. Massey, C. Moore, S. Muela, B. Rashleigh, W. Wheeler, S. Whitlock, and J. Hewitt. An Integrated Assessment Model for Valuing Water Quality Changes in the US.   Land Economics. University of Wisconsin Press, Madison, WI, USA, 96(4): 478-492, (2020).",
             "distribution": [
                 {
-                    "title": "BENSPLASHinput_scenario.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521093/BENSPLASHinput_scenario.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "BENSPLASHinput_scenario.csv"
                 },
                 {
-                    "title": "BENSPLASHinput_baseline.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521093/BENSPLASHinput_baseline.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "BENSPLASHinput_baseline.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521093",
+            "keyword": [
+                "water quality benefits"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-12",
-            "references": [
-                "https://doi.org/10.3368/wple.96.4.478"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134621,20 +134617,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1521093/documents/DataDictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.3368/wple.96.4.478"
+            ],
+            "rights": null,
+            "title": "Integrated Assessment Model for Valuing Water Quality Changes_BENSPLASH Input Data"
         },
         {
-            "title": "Pend Oreille River temperature and FLIR",
-            "description": "Water temperature data from the Pend Oreille River, Washington and Idaho, 2016-2018\nThe data were collected summer, 2016, 2017, and 2018. Continuous temperature loggers were deployed along the Pend Oreille River between Albeni Falls Dam and the Box Canyon Dam. Loggers were checked every 1-2 weeks throughout the summer. \n\nThis dataset is associated with the following publication:\nMejia, F.H., C.E. Torgersen, E.K. Berntsen, J.R. Maroney, J.M. Connor, A.H. Fullerton, J. Ebersole, and M.S. Lorang. Longitudinal, lateral, vertical and temporal thermal heterogeneity in a large impounded river: implications for cold-water refuges.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 12(9): 1386, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "Water temperature data from the Pend Oreille River, Washington and Idaho, 2016-2018\nThe data were collected summer, 2016, 2017, and 2018. Continuous temperature loggers were deployed along the Pend Oreille River between Albeni Falls Dam and the Box Canyon Dam. Loggers were checked every 1-2 weeks throughout the summer. \n\nThis dataset is associated with the following publication:\nMejia, F.H., C.E. Torgersen, E.K. Berntsen, J.R. Maroney, J.M. Connor, A.H. Fullerton, J. Ebersole, and M.S. Lorang. Longitudinal, lateral, vertical and temporal thermal heterogeneity in a large impounded river: implications for cold-water refuges.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 12(9): 1386, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/5c9d0e2ee4b0b8a7f62e0903",
+                    "title": "https://www.sciencebase.gov/catalog/item/5c9d0e2ee4b0b8a7f62e0903"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518646",
             "keyword": [
@@ -134645,19 +134648,10 @@
                 "Pacific Northwest",
                 "restoration"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.sciencebase.gov/catalog/item/5c9d0e2ee4b0b8a7f62e0903",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/5c9d0e2ee4b0b8a7f62e0903"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-23",
-            "references": [
-                "https://doi.org/10.3390/rs12091386"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134667,19 +134661,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/rs12091386"
+            ],
+            "rights": null,
+            "title": "Pend Oreille River temperature and FLIR"
         },
         {
-            "title": "Raster outputs in support of Sea Level Affecting Marshes Model (SLAMM) projections for salt marshes of the Lower Delaware Bay",
-            "description": "These raster files are associated with the SLAMM projections presented in the EPA report, \"Application of the Sea-Level Affecting Marshes Model (SLAMM) to the Lower Delaware Bay, with a Focus on Salt Marsh Habitat\" (https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NCEA&dirEntryId=344746). A subset of these projections are in turn presented in the journal article associated with the ScienceHub entry, \"Framework for assessing salt marsh vulnerability to sea level rise to support management decision making: Delaware Bay case study\".",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Jordan West",
+                "hasEmail": "mailto:west.jordan@epa.gov"
+            },
+            "description": "These raster files are associated with the SLAMM projections presented in the EPA report, \"Application of the Sea-Level Affecting Marshes Model (SLAMM) to the Lower Delaware Bay, with a Focus on Salt Marsh Habitat\" (https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NCEA&dirEntryId=344746). A subset of these projections are in turn presented in the journal article associated with the ScienceHub entry, \"Framework for assessing salt marsh vulnerability to sea level rise to support management decision making: Delaware Bay case study\".",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.23719/1503846",
+                    "title": "https://doi.org/10.23719/1503846"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1517805",
             "keyword": [
@@ -134692,18 +134695,11 @@
                 "adaptation",
                 "management"
             ],
-            "contactPoint": {
-                "fn": "Jordan West",
-                "hasEmail": "mailto:west.jordan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.23719/1503846",
-                    "accessURL": "https://doi.org/10.23719/1503846"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-17",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -134712,39 +134708,37 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Raster outputs in support of Sea Level Affecting Marshes Model (SLAMM) projections for salt marshes of the Lower Delaware Bay"
         },
         {
-            "title": "H2O2 quant_SciHub_2018",
-            "description": "Data summary for each figure. \n\nThis dataset is associated with the following publication:\nLehmann, D., K. Krishnakuman, M. Batres, A. Hakola-Parry, N. Cokcetin, E. Harry, and D. Carter. A Cost Effective Colourimetric Assay for Quantifying Hydrogen Peroxide in Honey.   Access Microbiology. Microbiology Society, London,  UK, 1(10): e000065, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1435502",
-            "keyword": [
-                "citizen science",
-                "Hydrogen Peroxide"
-            ],
             "contactPoint": {
                 "fn": "David Lehmann",
                 "hasEmail": "mailto:lehmann.david@epa.gov"
             },
+            "description": "Data summary for each figure. \n\nThis dataset is associated with the following publication:\nLehmann, D., K. Krishnakuman, M. Batres, A. Hakola-Parry, N. Cokcetin, E. Harry, and D. Carter. A Cost Effective Colourimetric Assay for Quantifying Hydrogen Peroxide in Honey.   Access Microbiology. Microbiology Society, London,  UK, 1(10): e000065, (2019).",
             "distribution": [
                 {
-                    "title": "H2O2 quant_SciHub_2018.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435502/H2O2%20quant_SciHub_2018.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "H2O2 quant_SciHub_2018.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435502",
+            "keyword": [
+                "citizen science",
+                "Hydrogen Peroxide"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-04",
-            "references": [
-                "https://doi.org/10.1099/acmi.0.000065"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134754,19 +134748,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1099/acmi.0.000065"
+            ],
+            "rights": null,
+            "title": "H2O2 quant_SciHub_2018"
         },
         {
-            "title": "Acetamiprid in pollen_2018_Science Hub_Data.xlxs",
-            "description": "Excel file with processed data used to generate each figure in the manuscript. \n\nThis dataset is associated with the following publication:\nCamp, A., M. Batres, W. Williams, R. Koethe, K. Stoner, and D. Lehmann. Effects of the neonicotinoid acetamiprid in pollen on Bombus impatiens microcolony development.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 39(12): 2560-2569, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "David Lehmann",
+                "hasEmail": "mailto:lehmann.david@epa.gov"
+            },
+            "description": "Excel file with processed data used to generate each figure in the manuscript. \n\nThis dataset is associated with the following publication:\nCamp, A., M. Batres, W. Williams, R. Koethe, K. Stoner, and D. Lehmann. Effects of the neonicotinoid acetamiprid in pollen on Bombus impatiens microcolony development.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 39(12): 2560-2569, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518470/Acetamiprid%20in%20pollen_2018_ScienceHub_%20Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Acetamiprid in pollen_2018_ScienceHub_ Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518470",
             "keyword": [
@@ -134777,20 +134781,10 @@
                 "pollen",
                 "pesticides"
             ],
-            "contactPoint": {
-                "fn": "David Lehmann",
-                "hasEmail": "mailto:lehmann.david@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Acetamiprid in pollen_2018_ScienceHub_ Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518470/Acetamiprid%20in%20pollen_2018_ScienceHub_%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-20",
-            "references": [
-                "https://doi.org/10.1002/etc.4886"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134800,40 +134794,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4886"
+            ],
+            "rights": null,
+            "title": "Acetamiprid in pollen_2018_Science Hub_Data.xlxs"
         },
         {
-            "title": "Final_Ozone_instrument_smoke_evaluation_data",
-            "description": "EPA Federal Reference Method (FRM) and Federal Equivalent Method (FEM) ozone and supporting (carbon monoxide, nitrogen dioxide, nitrogen oxide, total hydrocarbon) measurements  were made during a combustion chamber experiment in April 2018 at the U.S. Forest Service Rocky Mountain Research Station laboratory (Missoula, MT). In addition, similar measurements were made from a mobile measurement platform in 2017 during a series of prescribed tallgrass prairie burns at Konza Prairie Biological Station (Kansas), Tallgrass Prairie National Preserve (Kansas), and Sycan Marsh Preserve (Oregon). \n\nThis dataset is associated with the following publication:\nLong, R., A. Whitehill, A. Habel, S. Urbanski, H. Halliday, M. Colon, S. Kaushik, and M. Landis. Comparison of Ozone Measurement Methods in Biomass Burning Smoke: An evaluation under field and laboratory conditions.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 14(3): 1783-1800, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1519325",
-            "keyword": [
-                "Ozone",
-                "smoke",
-                "UV-Photometric",
-                "chemiluminescence"
-            ],
             "contactPoint": {
                 "fn": "Russell Long",
                 "hasEmail": "mailto:long.russell@epa.gov"
             },
+            "description": "EPA Federal Reference Method (FRM) and Federal Equivalent Method (FEM) ozone and supporting (carbon monoxide, nitrogen dioxide, nitrogen oxide, total hydrocarbon) measurements  were made during a combustion chamber experiment in April 2018 at the U.S. Forest Service Rocky Mountain Research Station laboratory (Missoula, MT). In addition, similar measurements were made from a mobile measurement platform in 2017 during a series of prescribed tallgrass prairie burns at Konza Prairie Biological Station (Kansas), Tallgrass Prairie National Preserve (Kansas), and Sycan Marsh Preserve (Oregon). \n\nThis dataset is associated with the following publication:\nLong, R., A. Whitehill, A. Habel, S. Urbanski, H. Halliday, M. Colon, S. Kaushik, and M. Landis. Comparison of Ozone Measurement Methods in Biomass Burning Smoke: An evaluation under field and laboratory conditions.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 14(3): 1783-1800, (2021).",
             "distribution": [
                 {
-                    "title": "Final O3-Smoke public data for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519325/Final%20O3-Smoke%20public%20data%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Final O3-Smoke public data for Science Hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519325",
+            "keyword": [
+                "Ozone",
+                "smoke",
+                "UV-Photometric",
+                "chemiluminescence"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-03",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -134842,19 +134838,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Final_Ozone_instrument_smoke_evaluation_data"
         },
         {
-            "title": "Phenotypic Profiling of Reference Chemicals across Biologically Diverse Cell Types Using the Cell Painting Assay",
-            "description": "Cell Painting is a high-throughput, phenotypic profiling assay that uses fluorescent cytochemistry o visualize a variety of organelles and high-content imaging to derive a large number of morphological features at the single cell level. Here, we used the Cell Painting assay to characterize the phenotypic effects of sixteen phenotypic reference chemicals in concentration- response screening mode across six biologically diverse human-derived cell lines (U-2 OS, MCF7, HepG2, A549, HTB-9, ARPE-19). All cell lines were labeled using the same cytochemistry protocol and the same set of phenotypic features were calculated. We found it necessary to optimize image acquisition settings and cell segmentation parameters for each cell type but did not adjust the cytochemistry protocol. For some reference chemicals, similar subsets of phenotypic features corresponding to a particular organelle were associated with the highest effect magnitudes in each affected cell type. Overall, for certain chemicals the Cell Painting assay yielded qualitatively similar biological activity profiles across a group of diverse, morphologically distinct human-derived cell lines without the requirement for cell-type specific optimization of cytochemistry protocols. \n\nThis dataset is associated with the following publication:\nWillis, C., J. Nyffeler, and J. Harrill. Phenotypic Profiling of Reference Chemicals Across Biologically Diverse Cell Types Using the Cell Painting Assay.   SLAS Discovery. SAGE Publications, THOUSAND OAKS, CA, USA, 25(7): 755-769, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Joshua Harrill",
+                "hasEmail": "mailto:harrill.joshua@epa.gov"
+            },
+            "description": "Cell Painting is a high-throughput, phenotypic profiling assay that uses fluorescent cytochemistry o visualize a variety of organelles and high-content imaging to derive a large number of morphological features at the single cell level. Here, we used the Cell Painting assay to characterize the phenotypic effects of sixteen phenotypic reference chemicals in concentration- response screening mode across six biologically diverse human-derived cell lines (U-2 OS, MCF7, HepG2, A549, HTB-9, ARPE-19). All cell lines were labeled using the same cytochemistry protocol and the same set of phenotypic features were calculated. We found it necessary to optimize image acquisition settings and cell segmentation parameters for each cell type but did not adjust the cytochemistry protocol. For some reference chemicals, similar subsets of phenotypic features corresponding to a particular organelle were associated with the highest effect magnitudes in each affected cell type. Overall, for certain chemicals the Cell Painting assay yielded qualitatively similar biological activity profiles across a group of diverse, morphologically distinct human-derived cell lines without the requirement for cell-type specific optimization of cytochemistry protocols. \n\nThis dataset is associated with the following publication:\nWillis, C., J. Nyffeler, and J. Harrill. Phenotypic Profiling of Reference Chemicals Across Biologically Diverse Cell Types Using the Cell Painting Assay.   SLAS Discovery. SAGE Publications, THOUSAND OAKS, CA, USA, 25(7): 755-769, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Harrill/ORD-034672/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Harrill/ORD-034672/"
+                },
+                {
+                    "accessURL": "https://doi.org/10.23645/epacomptox.14195270",
+                    "title": "https://doi.org/10.23645/epacomptox.14195270"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520919",
             "keyword": [
@@ -134868,23 +134875,10 @@
                 "concentration response",
                 "cell painting"
             ],
-            "contactPoint": {
-                "fn": "Joshua Harrill",
-                "hasEmail": "mailto:harrill.joshua@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Harrill/ORD-034672/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/CCTE_Publication_Data/BCTD_Publication_Data/Harrill/ORD-034672/"
-                },
-                {
-                    "title": "https://doi.org/10.23645/epacomptox.14195270",
-                    "accessURL": "https://doi.org/10.23645/epacomptox.14195270"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-30",
-            "references": [
-                "https://doi.org/10.1177/2472555220928004"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -134894,50 +134888,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1177/2472555220928004"
+            ],
+            "rights": null,
+            "title": "Phenotypic Profiling of Reference Chemicals across Biologically Diverse Cell Types Using the Cell Painting Assay"
         },
         {
-            "title": "EPA ORD 2019 benthic survey of the Three Bays estuary, Barnstable, MA",
-            "description": "Includes in-situ water quality measurements and sediment grab samples analyzed for grain size distribution, total organic carbon, and benthic macroinvertebrates (counts and taxa) for 25 stations throughout the estuary. Samples were collected September 9-11, 2019. \n\nThis dataset is associated with the following publication:\nErban, L., D. Cobb, C. Strobel, C. Tremper, J. Hagy, and T. Gleason. Summary of benthic conditions in the Three Bays estuary (Cape Cod, MA) as of 2019. U.S. Environmental Protection Agency, Washington, DC, USA, 2021.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520968",
-            "keyword": [
-                "benthic macroinvertebrates",
-                "water quality",
-                "habitat condition",
-                "estuary"
-            ],
             "contactPoint": {
                 "fn": "Laura Erban",
                 "hasEmail": "mailto:erban.laura@epa.gov"
             },
+            "description": "Includes in-situ water quality measurements and sediment grab samples analyzed for grain size distribution, total organic carbon, and benthic macroinvertebrates (counts and taxa) for 25 stations throughout the estuary. Samples were collected September 9-11, 2019. \n\nThis dataset is associated with the following publication:\nErban, L., D. Cobb, C. Strobel, C. Tremper, J. Hagy, and T. Gleason. Summary of benthic conditions in the Three Bays estuary (Cape Cod, MA) as of 2019. U.S. Environmental Protection Agency, Washington, DC, USA, 2021.",
             "distribution": [
                 {
-                    "title": "Computational notebook for Summary.html",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520968/Computational%20notebook%20for%20Summary.html",
-                    "mediaType": "text/html"
+                    "mediaType": "text/html",
+                    "title": "Computational notebook for Summary.html"
                 },
                 {
-                    "title": "data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520968/data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data.zip"
                 },
                 {
-                    "title": "Summary of benthic conditions in the Three Bays estuary as of 2019.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520968/Summary%20of%20benthic%20conditions%20in%20the%20Three%20Bays%20estuary%20as%20of%202019.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Summary of benthic conditions in the Three Bays estuary as of 2019.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520968",
+            "keyword": [
+                "benthic macroinvertebrates",
+                "water quality",
+                "habitat condition",
+                "estuary"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-11",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -134946,76 +134942,74 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "EPA ORD 2019 benthic survey of the Three Bays estuary, Barnstable, MA"
         },
         {
-            "title": "Datasets for Figures and Tables in SIX1 regulates aberrant endometrial epithelial cell differentiation and cancer trajectory",
-            "description": "Data associated with the figures presented in this study are images, graphics, or tabulated data based on histopathologic analysis performed by a certified study pathologist or image analysis. Data for Tables 1 and 2 provide incidence, labeling scores, and p-values for statistical tests for uterine pathology and IHC expression by treatment group and timepoint or human endometrial tissue, as described in the Main Text file of the manuscript. Manual histopathologic data can be found in excel spreadsheets and are based on presence/absences (yes/no) of a pathologic finding and/or severity score as described in the manuscript (Fig. 1, 2, 3, 4). The image analysis data is based on the quantified area that is designated as \u201cpositive\u201d for a particular immunohistochemical stain (Fig. 2, 4, and Suppl. Fig. S2). Supplementary Table 1 provides summary information on antibodies used for immunohistochemistry. Supplementary fig. S1 includes real time RT-PCR data standardized to a housekeeping gene and western blot data. \n\nThis dataset is associated with the following publication:\nSuen, A., W. Jefferson, C. Wood, and C. Williams. SIX1 regulates aberrant endometrial epithelial cell differentiation and cancer trajectory.   Molecular Cancer Research. American Association for Cancer Research, Inc., Philadelphia, PA, USA, 17(12): 2369-2382, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503409",
-            "keyword": [
-                "cancer",
-                "estrogen",
-                "early-life exposure",
-                "development"
-            ],
             "contactPoint": {
                 "fn": "Brian Chorley",
                 "hasEmail": "mailto:chorley.brian@epa.gov"
             },
+            "description": "Data associated with the figures presented in this study are images, graphics, or tabulated data based on histopathologic analysis performed by a certified study pathologist or image analysis. Data for Tables 1 and 2 provide incidence, labeling scores, and p-values for statistical tests for uterine pathology and IHC expression by treatment group and timepoint or human endometrial tissue, as described in the Main Text file of the manuscript. Manual histopathologic data can be found in excel spreadsheets and are based on presence/absences (yes/no) of a pathologic finding and/or severity score as described in the manuscript (Fig. 1, 2, 3, 4). The image analysis data is based on the quantified area that is designated as \u201cpositive\u201d for a particular immunohistochemical stain (Fig. 2, 4, and Suppl. Fig. S2). Supplementary Table 1 provides summary information on antibodies used for immunohistochemistry. Supplementary fig. S1 includes real time RT-PCR data standardized to a housekeeping gene and western blot data. \n\nThis dataset is associated with the following publication:\nSuen, A., W. Jefferson, C. Wood, and C. Williams. SIX1 regulates aberrant endometrial epithelial cell differentiation and cancer trajectory.   Molecular Cancer Research. American Association for Cancer Research, Inc., Philadelphia, PA, USA, 17(12): 2369-2382, (2019).",
             "distribution": [
                 {
-                    "title": "Fig. 1 2 3_Histopath Analysis_Charles Wood_Six1 WT dd CON DES_6 mo.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Fig.%201%202%203_Histopath%20Analysis_Charles%20Wood_Six1%20WT%20dd%20CON%20DES_6%20mo.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig. 1 2 3_Histopath Analysis_Charles Wood_Six1 WT dd CON DES_6 mo.xlsx"
                 },
                 {
-                    "title": "Fig. 1_Suen-Wallach_455-C36_ Electron Micro Report.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Fig.%201_Suen-Wallach_455-C36_%20Electron%20Micro%20Report.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Fig. 1_Suen-Wallach_455-C36_ Electron Micro Report.docx"
                 },
                 {
-                    "title": "Fig. 2 and Supp Fig. 2_Six1 Knockout DES_Image Analysis_Immuno2_Epithelium Analyzed.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Fig.%202%20and%20Supp%20Fig.%202_Six1%20Knockout%20DES_Image%20Analysis_Immuno2_Epithelium%20Analyzed.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig. 2 and Supp Fig. 2_Six1 Knockout DES_Image Analysis_Immuno2_Epithelium Analyzed.xlsx"
                 },
                 {
-                    "title": "Fig. 1 2 3_Histopath Analysis_Charles Wood_Six1 WT dd CON DES_12 mo.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Fig.%201%202%203_Histopath%20Analysis_Charles%20Wood_Six1%20WT%20dd%20CON%20DES_12%20mo.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig. 1 2 3_Histopath Analysis_Charles Wood_Six1 WT dd CON DES_12 mo.xlsx"
                 },
                 {
-                    "title": "Fig. 4_Human TMA Charles Wood Analysis_052518.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Fig.%204_Human%20TMA%20Charles%20Wood%20Analysis_052518.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig. 4_Human TMA Charles Wood Analysis_052518.xlsx"
                 },
                 {
-                    "title": "Supp Fig. 1_Real time RTPCR data all ages.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Supp%20Fig.%201_Real%20time%20RTPCR%20data%20all%20ages.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supp Fig. 1_Real time RTPCR data all ages.xlsx"
                 },
                 {
-                    "title": "Fig. 2 and Supp Fig. 2_Six1 Knockout CON_Image Analysis_Immuno2_Epithelium Analyzed.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Fig.%202%20and%20Supp%20Fig.%202_Six1%20Knockout%20CON_Image%20Analysis_Immuno2_Epithelium%20Analyzed.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig. 2 and Supp Fig. 2_Six1 Knockout CON_Image Analysis_Immuno2_Epithelium Analyzed.xlsx"
                 },
                 {
-                    "title": "Fig. 4_Human TMA Image Analysis_051818.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503409/Fig.%204_Human%20TMA%20Image%20Analysis_051818.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig. 4_Human TMA Image Analysis_051818.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503409",
+            "keyword": [
+                "cancer",
+                "estrogen",
+                "early-life exposure",
+                "development"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-13",
-            "references": [
-                "https://doi.org/10.1158/1541-7786.mcr-19-0475"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135025,42 +135019,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1158/1541-7786.mcr-19-0475"
+            ],
+            "rights": null,
+            "title": "Datasets for Figures and Tables in SIX1 regulates aberrant endometrial epithelial cell differentiation and cancer trajectory"
         },
         {
-            "title": "Data mining approaches to quantifying the formation of secondary organic aerosol",
-            "description": "This research used data mining approaches to better understand factors affecting the formation of secondary organic aerosol (SOA). Although numerous laboratory and computational studies have been completed on SOA formation, it is still challenging to determine factors that most influence SOA formation. Experimental data were based on previous work described by Offenberg et al. (2017), where volume concentrations of SOA were measured in 139 laboratory experiments involving the oxidation of single hydrocarbons under different operating conditions. Three different data mining methods were used, including nearest neighbor, decision tree, and pattern mining. Both decision tree and pattern mining approaches identified similar chemical and experimental conditions that were important to SOA formation. Among these important factors included the number of methyl groups, the number of rings and the presence of dinitrogen pentoxide (N2O5). \n\nThis dataset is associated with the following publication:\nOlson, D., J. Offenberg, M. Lewandowski, T. Kleindienst, K. Docherty, M. Jaoui, J.D. Krug, and T. Riedel. Data mining approaches to understanding the formation of secondary organic aerosol.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 252: 118345, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1519378",
-            "keyword": [
-                "data mining",
-                "air quality",
-                "Secondary Organic Aerosol",
-                "air toxics",
-                "Ozone"
-            ],
             "contactPoint": {
                 "fn": "Michael Lewandowski",
                 "hasEmail": "mailto:lewandowski.michael@epa.gov"
             },
+            "description": "This research used data mining approaches to better understand factors affecting the formation of secondary organic aerosol (SOA). Although numerous laboratory and computational studies have been completed on SOA formation, it is still challenging to determine factors that most influence SOA formation. Experimental data were based on previous work described by Offenberg et al. (2017), where volume concentrations of SOA were measured in 139 laboratory experiments involving the oxidation of single hydrocarbons under different operating conditions. Three different data mining methods were used, including nearest neighbor, decision tree, and pattern mining. Both decision tree and pattern mining approaches identified similar chemical and experimental conditions that were important to SOA formation. Among these important factors included the number of methyl groups, the number of rings and the presence of dinitrogen pentoxide (N2O5). \n\nThis dataset is associated with the following publication:\nOlson, D., J. Offenberg, M. Lewandowski, T. Kleindienst, K. Docherty, M. Jaoui, J.D. Krug, and T. Riedel. Data mining approaches to understanding the formation of secondary organic aerosol.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 252: 118345, (2021).",
             "distribution": [
                 {
-                    "title": "ScienceHub entry (Olson DM SOA).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519378/ScienceHub%20entry%20%28Olson%20DM%20SOA%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHub entry (Olson DM SOA).xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519378",
+            "keyword": [
+                "data mining",
+                "air quality",
+                "Secondary Organic Aerosol",
+                "air toxics",
+                "Ozone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-24",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2021.118345"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135070,40 +135064,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2021.118345"
+            ],
+            "rights": null,
+            "title": "Data mining approaches to quantifying the formation of secondary organic aerosol"
         },
         {
-            "title": "Migration corridor simulation - for second paper",
-            "description": "The model scenario and associated outputs of the case study used to illustrate the migration corridor simulation model demonstrating fish fitness outcomes. \n\nThis dataset is associated with the following publication:\nSnyder, M., N. Schumaker, J. Dunham, M. Keefer, P. Leinenbach, A. Brookes, J. Palmer, J. Wu, D. Keenan, and J. Ebersole. Assessing contributions of coldwater refuges to reproductive migration corridor conditions for adult salmon and steelhead trout in the Columbia River, USA.   Journal of Ecohydraulics. Taylor & Francis Group, London,  UK,  1855086, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1518728",
-            "keyword": [
-                "cold water refuge",
-                "Salmon",
-                "trout",
-                "migration"
-            ],
             "contactPoint": {
                 "fn": "Joseph Ebersole",
                 "hasEmail": "mailto:ebersole.joe@epa.gov"
             },
+            "description": "The model scenario and associated outputs of the case study used to illustrate the migration corridor simulation model demonstrating fish fitness outcomes. \n\nThis dataset is associated with the following publication:\nSnyder, M., N. Schumaker, J. Dunham, M. Keefer, P. Leinenbach, A. Brookes, J. Palmer, J. Wu, D. Keenan, and J. Ebersole. Assessing contributions of coldwater refuges to reproductive migration corridor conditions for adult salmon and steelhead trout in the Columbia River, USA.   Journal of Ecohydraulics. Taylor & Francis Group, London,  UK,  1855086, (2020).",
             "distribution": [
                 {
-                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1503532",
-                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1503532"
+                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1503532",
+                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1503532"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518728",
+            "keyword": [
+                "cold water refuge",
+                "Salmon",
+                "trout",
+                "migration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-12-03",
-            "references": [
-                "https://doi.org/10.1080/24705357.2020.1855086"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135113,49 +135107,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/24705357.2020.1855086"
+            ],
+            "rights": null,
+            "title": "Migration corridor simulation - for second paper"
         },
         {
-            "title": "Fish bio-energetics model metadata",
-            "description": "The Oregon stream temperatures used in Fig. 1 were sourced from 58 sites monitored by the Oregon Department of Environmental Quality and 17 sites monitored by The United States Geological Survey. These data are publicly available at https://www.oregon.gov/deq/wq/Pages/WQdata.aspx and https://waterdata.usgs.gov/nwis/sw, respectively. The water temperature data used in Figs. 2\u20134 are posted on GitHub at https://github.com/chris3jordan/Growth-Potential.\nThe code for processing water temperature and growth potential data for Figs. 2\u20134 is posted on GitHub at https://github.com/chris3jordan/Growth-Potential. The code for the numerical simulation is posted on GitHub at https://github.com/aimeefullerton/growth_regime_IBM. \n\nThis dataset is associated with the following publication:\nArmstrong, J.B., A.H. Fullerton, C.E. Jordan, J. Ebersole, J.R. Bellmore, I. Arismendi, B. Penaluna, and G.H. Reeves. The importance of warm habitat to the growth regime of cold-water fishes.   Nature Climate Change. Nature Publishing Group, New York, NY, USA,  00994, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1519040",
-            "keyword": [
-                "water quality",
-                "wildfire",
-                "refugia",
-                "recovery",
-                "resilience"
-            ],
             "contactPoint": {
                 "fn": "Joseph Ebersole",
                 "hasEmail": "mailto:ebersole.joe@epa.gov"
             },
+            "description": "The Oregon stream temperatures used in Fig. 1 were sourced from 58 sites monitored by the Oregon Department of Environmental Quality and 17 sites monitored by The United States Geological Survey. These data are publicly available at https://www.oregon.gov/deq/wq/Pages/WQdata.aspx and https://waterdata.usgs.gov/nwis/sw, respectively. The water temperature data used in Figs. 2\u20134 are posted on GitHub at https://github.com/chris3jordan/Growth-Potential.\nThe code for processing water temperature and growth potential data for Figs. 2\u20134 is posted on GitHub at https://github.com/chris3jordan/Growth-Potential. The code for the numerical simulation is posted on GitHub at https://github.com/aimeefullerton/growth_regime_IBM. \n\nThis dataset is associated with the following publication:\nArmstrong, J.B., A.H. Fullerton, C.E. Jordan, J. Ebersole, J.R. Bellmore, I. Arismendi, B. Penaluna, and G.H. Reeves. The importance of warm habitat to the growth regime of cold-water fishes.   Nature Climate Change. Nature Publishing Group, New York, NY, USA,  00994, (2021).",
             "distribution": [
                 {
-                    "title": "https://github.com/chris3jordan/Growth-Potential",
-                    "accessURL": "https://github.com/chris3jordan/Growth-Potential"
+                    "accessURL": "https://github.com/chris3jordan/Growth-Potential",
+                    "title": "https://github.com/chris3jordan/Growth-Potential"
                 },
                 {
-                    "title": "https://waterdata.usgs.gov/nwis/sw",
-                    "accessURL": "https://waterdata.usgs.gov/nwis/sw"
+                    "accessURL": "https://waterdata.usgs.gov/nwis/sw",
+                    "title": "https://waterdata.usgs.gov/nwis/sw"
                 },
                 {
-                    "title": "https://www.oregon.gov/deq/wq/Pages/WQdata.aspx",
-                    "accessURL": "https://www.oregon.gov/deq/wq/Pages/WQdata.aspx"
+                    "accessURL": "https://www.oregon.gov/deq/wq/Pages/WQdata.aspx",
+                    "title": "https://www.oregon.gov/deq/wq/Pages/WQdata.aspx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519040",
+            "keyword": [
+                "water quality",
+                "wildfire",
+                "refugia",
+                "recovery",
+                "resilience"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-01-12",
-            "references": [
-                "https://doi.org/10.1038/s41558-021-00994-y"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135165,42 +135159,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41558-021-00994-y"
+            ],
+            "rights": null,
+            "title": "Fish bio-energetics model metadata"
         },
         {
-            "title": "Pulmonary and Vascular Effects of Acute Ozone Exposure in Diabetic Rats Fed an Atherogenic Diet",
-            "description": "In this study, we investigated effects of inhaled ozone exposure and high-cholesterol diet (HCD) in healthy Wistar and Wistar-derived Goto-Kakizaki (GK) rats, a non-obese model of type 2 diabetes. Male rats (4-week old) were fed normal diet or HCD for 12 weeks and then exposed to filtered air or 1.0 ppm ozone (6hrs/day) for 1 or 2 days. We examined pulmonary, vascular, hematology, and inflammatory responses after each exposure plus an 18-hr recovery period. \n\nThis dataset is associated with the following publication:\nSnow, S., A. Henriquez, L. Thompson, C. Fisher, M.C. Schladweiler, C. Wood, and U. Kodavanti. Pulmonary and Vascular Effects of Acute Ozone Exposure in Diabetic Rats Fed an Atherogenic Diet.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 415(115430): 1, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1521140",
-            "keyword": [
-                "type 2 diabetes rat model",
-                "Western high-cholesterol diet",
-                "pulmonary injury",
-                "systemic inflammation",
-                "vasocontraction"
-            ],
             "contactPoint": {
                 "fn": "Urmila Kodavanti",
                 "hasEmail": "mailto:kodavanti.urmila@epa.gov"
             },
+            "description": "In this study, we investigated effects of inhaled ozone exposure and high-cholesterol diet (HCD) in healthy Wistar and Wistar-derived Goto-Kakizaki (GK) rats, a non-obese model of type 2 diabetes. Male rats (4-week old) were fed normal diet or HCD for 12 weeks and then exposed to filtered air or 1.0 ppm ozone (6hrs/day) for 1 or 2 days. We examined pulmonary, vascular, hematology, and inflammatory responses after each exposure plus an 18-hr recovery period. \n\nThis dataset is associated with the following publication:\nSnow, S., A. Henriquez, L. Thompson, C. Fisher, M.C. Schladweiler, C. Wood, and U. Kodavanti. Pulmonary and Vascular Effects of Acute Ozone Exposure in Diabetic Rats Fed an Atherogenic Diet.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 415(115430): 1, (2021).",
             "distribution": [
                 {
-                    "title": "GK-ozone Pulmonary Paper Science Hub-final.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521140/GK-ozone%20Pulmonary%20Paper%20Science%20Hub-final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GK-ozone Pulmonary Paper Science Hub-final.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521140",
+            "keyword": [
+                "type 2 diabetes rat model",
+                "Western high-cholesterol diet",
+                "pulmonary injury",
+                "systemic inflammation",
+                "vasocontraction"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-30",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2021.115430"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135210,19 +135204,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2021.115430"
+            ],
+            "rights": null,
+            "title": "Pulmonary and Vascular Effects of Acute Ozone Exposure in Diabetic Rats Fed an Atherogenic Diet"
         },
         {
-            "title": "Diets Enriched with Coconut, Fish, and Olive Oil Modify Peripheral Metabolic Effects of Ozone in Rats",
-            "description": "In this study male Wistar Kyoto rats maintained on diets enriched with coconut, fish or olive oil were compared with animals receiving normal diet for 8 weeks. After 8 weeks of dietary regimen, and while on respective diets, animals were exposed to air or 0.8 ppm ozone for 4 hours per day for 2 consecutive days and necropsies were performed post air or ozone exposure within 2 hours. Body weights, food consumption and body composition were assessed during dietary regimen. At necropsy, livers were stained for lipids, serum lipids and metabolic hormones were assessed, and liver, muscle and adipose tissues are assessed for gene expression using targeted Illumina sequencing for selected genes. Based on reviewers comments during revision period, circulating n-3, n-6, n-9 and unsaturated fatty acids were assessed in the serum through collaboration with Jenifer I. Fenton and Travis Goeden, Michigan State University where samples were shipped for analysis of these lipids using mass spectrometry. These data were incorporated in the manuscript (Table 1) and part of figure 3. \n\nThis dataset is associated with the following publication:\nSnow, S., A. Henriquez, W. Cheng, A. Fisher, B. Vallanat, M. Angrish, J. Richards, M.C. Schladweiler, C. Wood, H. Tong, and U. Kodavanti. Diets Enriched with Coconut, Fish, and Olive Oil Modify Peripheral Metabolic Effects of Ozone in Rats.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 410(1): 115337, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Urmila Kodavanti",
+                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
+            },
+            "description": "In this study male Wistar Kyoto rats maintained on diets enriched with coconut, fish or olive oil were compared with animals receiving normal diet for 8 weeks. After 8 weeks of dietary regimen, and while on respective diets, animals were exposed to air or 0.8 ppm ozone for 4 hours per day for 2 consecutive days and necropsies were performed post air or ozone exposure within 2 hours. Body weights, food consumption and body composition were assessed during dietary regimen. At necropsy, livers were stained for lipids, serum lipids and metabolic hormones were assessed, and liver, muscle and adipose tissues are assessed for gene expression using targeted Illumina sequencing for selected genes. Based on reviewers comments during revision period, circulating n-3, n-6, n-9 and unsaturated fatty acids were assessed in the serum through collaboration with Jenifer I. Fenton and Travis Goeden, Michigan State University where samples were shipped for analysis of these lipids using mass spectrometry. These data were incorporated in the manuscript (Table 1) and part of figure 3. \n\nThis dataset is associated with the following publication:\nSnow, S., A. Henriquez, W. Cheng, A. Fisher, B. Vallanat, M. Angrish, J. Richards, M.C. Schladweiler, C. Wood, H. Tong, and U. Kodavanti. Diets Enriched with Coconut, Fish, and Olive Oil Modify Peripheral Metabolic Effects of Ozone in Rats.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 410(1): 115337, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521135/Science%20Hub%20Ozone-diets%20TAAP%2003-30-2021.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science Hub Ozone-diets TAAP 03-30-2021.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521135",
             "keyword": [
@@ -135234,20 +135238,10 @@
                 "adipose tissue",
                 "muscle"
             ],
-            "contactPoint": {
-                "fn": "Urmila Kodavanti",
-                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Science Hub Ozone-diets TAAP 03-30-2021.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521135/Science%20Hub%20Ozone-diets%20TAAP%2003-30-2021.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-30",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2020.115337"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135257,19 +135251,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2020.115337"
+            ],
+            "rights": null,
+            "title": "Diets Enriched with Coconut, Fish, and Olive Oil Modify Peripheral Metabolic Effects of Ozone in Rats"
         },
         {
-            "title": "Peripheral Metabolic Effects of Ozone Exposure in Healthy and Diabetic Rats on Normal or High-Cholesterol Diet",
-            "description": "In this study, using male Wistar and Wistar-derived Goto-Kakizaki (GK) rats, which exhibit a non-obese type-2 diabetes phenotype, we investigated whether two key metabolic stressors, type-2 diabetes and a high-cholesterol atherogenic diet, exacerbate ozone-induced metabolic effects. Rats were fed a normal control diet (ND) or high-cholesterol diet (HCD) for 12 weeks starting at 4 week-age and then exposed to filtered air or 1.0-ppm ozone (6h/day) for 1 or 2 days. Metabolic responses were analyzed at the end of each day and after an 18-hour recovery period following the 2-day exposure. \n\nThis dataset is associated with the following publication:\nSnow, S., A. Henriquez, A. Fisher, B. Vallanat, J. House, M.C. Schladweiler, C. Wood, and U. Kodavanti. Peripheral Metabolic Effects of Ozone Exposure in Healthy and Diabetic Rats on Normal or High-Cholesterol Diet.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 415(115427): 1, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Urmila Kodavanti",
+                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
+            },
+            "description": "In this study, using male Wistar and Wistar-derived Goto-Kakizaki (GK) rats, which exhibit a non-obese type-2 diabetes phenotype, we investigated whether two key metabolic stressors, type-2 diabetes and a high-cholesterol atherogenic diet, exacerbate ozone-induced metabolic effects. Rats were fed a normal control diet (ND) or high-cholesterol diet (HCD) for 12 weeks starting at 4 week-age and then exposed to filtered air or 1.0-ppm ozone (6h/day) for 1 or 2 days. Metabolic responses were analyzed at the end of each day and after an 18-hour recovery period following the 2-day exposure. \n\nThis dataset is associated with the following publication:\nSnow, S., A. Henriquez, A. Fisher, B. Vallanat, J. House, M.C. Schladweiler, C. Wood, and U. Kodavanti. Peripheral Metabolic Effects of Ozone Exposure in Healthy and Diabetic Rats on Normal or High-Cholesterol Diet.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 415(115427): 1, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521138/Metabolic%20Paper%20Science%20Hub-final.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Metabolic Paper Science Hub-final.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521138",
             "keyword": [
@@ -135280,20 +135284,10 @@
                 "adipose tissue",
                 "liver"
             ],
-            "contactPoint": {
-                "fn": "Urmila Kodavanti",
-                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Metabolic Paper Science Hub-final.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521138/Metabolic%20Paper%20Science%20Hub-final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-30",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2021.115427"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135303,42 +135297,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2021.115427"
+            ],
+            "rights": null,
+            "title": "Peripheral Metabolic Effects of Ozone Exposure in Healthy and Diabetic Rats on Normal or High-Cholesterol Diet"
         },
         {
-            "title": "Maternal High-Fat Diet Alters Offspring Response to an Acute Ozone Exposure",
-            "description": "This data set for this manuscript is contained within one Excel file.The different tabs of the spreadsheet pertain to each figure found in the manuscript. This file was finalized on 2/1/19 to reflect any changes made to the figures in response to reviewers comments following submission to JTEH. \n\nThis dataset is associated with the following publication:\nSnow, S., P. Phillips, A. Ledbetter, A. Johnstone, M. Schladweiler, C. Gordon, and U. Kodavanti. The influence of maternal and perinatal high-fat diet on ozone-induced pulmonary responses in offspring. JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 82(2): 86-98, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1502583",
-            "keyword": [
-                "high fat diet",
-                "Ozone",
-                "maternal obesity",
-                "pulmonary injury"
-            ],
             "contactPoint": {
                 "fn": "Samantha Snow",
                 "hasEmail": "mailto:snow.samantha@epa.gov"
             },
+            "description": "This data set for this manuscript is contained within one Excel file.The different tabs of the spreadsheet pertain to each figure found in the manuscript. This file was finalized on 2/1/19 to reflect any changes made to the figures in response to reviewers comments following submission to JTEH. \n\nThis dataset is associated with the following publication:\nSnow, S., P. Phillips, A. Ledbetter, A. Johnstone, M. Schladweiler, C. Gordon, and U. Kodavanti. The influence of maternal and perinatal high-fat diet on ozone-induced pulmonary responses in offspring. JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 82(2): 86-98, (2019).",
             "distribution": [
                 {
-                    "title": "Influence of Maternal and Perinatal HFD on Ozone-Induced Pulmonary Responses in Offspring - Data for ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502583/Influence%20of%20Maternal%20and%20Perinatal%20HFD%20on%20Ozone-Induced%20Pulmonary%20Responses%20in%20Offspring%20-%20Data%20for%20ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Influence of Maternal and Perinatal HFD on Ozone-Induced Pulmonary Responses in Offspring - Data for ScienceHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502583",
+            "keyword": [
+                "high fat diet",
+                "Ozone",
+                "maternal obesity",
+                "pulmonary injury"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-01",
-            "references": [
-                "https://doi.org/10.1080/15287394.2018.1564101",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7530537"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135348,69 +135341,70 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/15287394.2018.1564101",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7530537"
+            ],
+            "rights": null,
+            "title": "Maternal High-Fat Diet Alters Offspring Response to an Acute Ozone Exposure"
         },
         {
-            "title": "Human Well-Being Domain and Composite Scores 2000-2017",
-            "description": "This data set contains the average census tract-scale scores, from 2000-2013, for the composite HWBI, each domain within the HWBI, each indicator within domains, and each metric within indicators.  Domain and composite scores at the beginning and end of the study period (2000, 2013) are also given. \n\nThis dataset is associated with the following publication:\nYee, S., E. Paulukonis, and K. Buck. Downscaling a human well-being index for environmental management and environmental justice applications in Puerto Rico.   Applied Geography. ELSEVIER, AMSTERDAM,  HOLLAND, 123: 14, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1503300",
-            "keyword": [
-                "human well-being",
-                "spatial interpolation"
-            ],
             "contactPoint": {
                 "fn": "Susan Yee",
                 "hasEmail": "mailto:yee.susan@epa.gov"
             },
+            "description": "This data set contains the average census tract-scale scores, from 2000-2013, for the composite HWBI, each domain within the HWBI, each indicator within domains, and each metric within indicators.  Domain and composite scores at the beginning and end of the study period (2000, 2013) are also given. \n\nThis dataset is associated with the following publication:\nYee, S., E. Paulukonis, and K. Buck. Downscaling a human well-being index for environmental management and environmental justice applications in Puerto Rico.   Applied Geography. ELSEVIER, AMSTERDAM,  HOLLAND, 123: 14, (2020).",
             "distribution": [
                 {
-                    "title": "FileDescriptions.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503300/FileDescriptions.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FileDescriptions.xlsx"
                 },
                 {
-                    "title": "MetricNames.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503300/MetricNames.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MetricNames.xlsx"
                 },
                 {
-                    "title": "HWBI_Merlin_Domain_Scores_RegStep4tr_Z2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503300/HWBI_Merlin_Domain_Scores_RegStep4tr_Z2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_Merlin_Domain_Scores_RegStep4tr_Z2.csv"
                 },
                 {
-                    "title": "HWBI_Merlin_Indicator_Scores_RegStep4tr_Z2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503300/HWBI_Merlin_Indicator_Scores_RegStep4tr_Z2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_Merlin_Indicator_Scores_RegStep4tr_Z2.csv"
                 },
                 {
-                    "title": "PR_MunicipioScale_RawMetrics_2000-2017.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503300/PR_MunicipioScale_RawMetrics_2000-2017.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "PR_MunicipioScale_RawMetrics_2000-2017.csv"
                 },
                 {
-                    "title": "PR_TractScale_RawMetrics_2000-2017.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503300/PR_TractScale_RawMetrics_2000-2017.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "PR_TractScale_RawMetrics_2000-2017.csv"
                 },
                 {
-                    "title": "HWBI_Merlin_Metric_Scores_RegStep4tr_Z2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503300/HWBI_Merlin_Metric_Scores_RegStep4tr_Z2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_Merlin_Metric_Scores_RegStep4tr_Z2.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503300",
+            "keyword": [
+                "human well-being",
+                "spatial interpolation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-12-12",
-            "references": [
-                "https://doi.org/10.1016/j.apgeog.2020.102231"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135420,57 +135414,59 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apgeog.2020.102231"
+            ],
+            "rights": null,
+            "title": "Human Well-Being Domain and Composite Scores 2000-2017"
         },
         {
-            "title": "Segregation_Indices_2015",
-            "description": "There are two excel data sheets with index values for each of the five minority groups assessed. In addition, there are two zip files with shapefiles containing the same index values. \n\nThis dataset is associated with the following publication:\nBuck, K., K. Summers, and L. Smith. Investigating the relationship between environmental quality, socio-spatial segregation and the social dimension of sustainability in US urban areas.   Sustainable Cities and Society. Elsevier B.V., Amsterdam,  NETHERLANDS, 67(102732): 11, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1502591",
-            "keyword": [
-                "segregation",
-                "neighborhoods",
-                "community",
-                "resilience",
-                "Vulnerability"
-            ],
             "contactPoint": {
                 "fn": "Kyle Buck",
                 "hasEmail": "mailto:buck.kyle@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502591/documents/Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "There are two excel data sheets with index values for each of the five minority groups assessed. In addition, there are two zip files with shapefiles containing the same index values. \n\nThis dataset is associated with the following publication:\nBuck, K., K. Summers, and L. Smith. Investigating the relationship between environmental quality, socio-spatial segregation and the social dimension of sustainability in US urban areas.   Sustainable Cities and Society. Elsevier B.V., Amsterdam,  NETHERLANDS, 67(102732): 11, (2021).",
             "distribution": [
                 {
-                    "title": "Tract_Seg_Index.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502591/Tract_Seg_Index.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tract_Seg_Index.xlsx"
                 },
                 {
-                    "title": "Cnty_Seg_Index.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502591/Cnty_Seg_Index.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Cnty_Seg_Index.xlsx"
                 },
                 {
-                    "title": "Tract_Index_Shapefile.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502591/Tract_Index_Shapefile.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Tract_Index_Shapefile.zip"
                 },
                 {
-                    "title": "Cnty_Index_Shapefile.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502591/Cnty_Index_Shapefile.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Cnty_Index_Shapefile.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502591",
+            "keyword": [
+                "segregation",
+                "neighborhoods",
+                "community",
+                "resilience",
+                "Vulnerability"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-08-24",
-            "references": [
-                "https://doi.org/10.1016/j.scs.2021.102732"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135481,101 +135477,99 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502591/documents/Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.scs.2021.102732"
+            ],
+            "rights": null,
+            "title": "Segregation_Indices_2015"
         },
         {
-            "title": "HWBI Domain and Services Metrics for Puerto Rico 2000-2017",
-            "description": "This data set provides the compile metrics for HWBI domains and services for Puerto Rico from 2000-2017, as well as the downscaled and scaled metrics and aggregated indicators used for statistical analyses. \n\nThis dataset is associated with the following publication:\nYee, S. Contributions of Ecosystem Services to Human Well-being in Puerto Rico.   Sustainability. MDPI AG, Basel,  SWITZERLAND, 12(22): 38, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1519429",
-            "keyword": [
-                "ecosystem services",
-                "human well-being",
-                "spatial interpolation"
-            ],
             "contactPoint": {
                 "fn": "Susan Yee",
                 "hasEmail": "mailto:yee.susan@epa.gov"
             },
+            "description": "This data set provides the compile metrics for HWBI domains and services for Puerto Rico from 2000-2017, as well as the downscaled and scaled metrics and aggregated indicators used for statistical analyses. \n\nThis dataset is associated with the following publication:\nYee, S. Contributions of Ecosystem Services to Human Well-being in Puerto Rico.   Sustainability. MDPI AG, Basel,  SWITZERLAND, 12(22): 38, (2020).",
             "distribution": [
                 {
-                    "title": "Services_RawMetrics_TractScale_2000_2017.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/Services_RawMetrics_TractScale_2000_2017.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Services_RawMetrics_TractScale_2000_2017.csv"
                 },
                 {
-                    "title": "Services_RawMetrics_MunicipioScale_2000_2017.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/Services_RawMetrics_MunicipioScale_2000_2017.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Services_RawMetrics_MunicipioScale_2000_2017.csv"
                 },
                 {
-                    "title": "Services_MetricNames.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/Services_MetricNames.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Services_MetricNames.xlsx"
                 },
                 {
-                    "title": "Service_Merlin_Service_Scores_RegStep5tr_Z.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/Service_Merlin_Service_Scores_RegStep5tr_Z.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Service_Merlin_Service_Scores_RegStep5tr_Z.csv"
                 },
                 {
-                    "title": "Service_Merlin_Metric_Scores_RegStep5tr_Z.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/Service_Merlin_Metric_Scores_RegStep5tr_Z.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Service_Merlin_Metric_Scores_RegStep5tr_Z.csv"
                 },
                 {
-                    "title": "Service_Merlin_Indicator_Scores_RegStep5tr_Z.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/Service_Merlin_Indicator_Scores_RegStep5tr_Z.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Service_Merlin_Indicator_Scores_RegStep5tr_Z.csv"
                 },
                 {
-                    "title": "HWBI_RawMetrics_TractScale_2000_2017.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/HWBI_RawMetrics_TractScale_2000_2017.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_RawMetrics_TractScale_2000_2017.csv"
                 },
                 {
-                    "title": "HWBI_RawMetrics_MunicipioScale_2000_2017.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/HWBI_RawMetrics_MunicipioScale_2000_2017.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_RawMetrics_MunicipioScale_2000_2017.csv"
                 },
                 {
-                    "title": "HWBI_MetricNames.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/HWBI_MetricNames.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HWBI_MetricNames.xlsx"
                 },
                 {
-                    "title": "HWBI_Merlin_Metric_Scores_RegStep4tr_Z2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/HWBI_Merlin_Metric_Scores_RegStep4tr_Z2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_Merlin_Metric_Scores_RegStep4tr_Z2.csv"
                 },
                 {
-                    "title": "HWBI_Merlin_Indicator_Scores_RegStep4tr_Z2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/HWBI_Merlin_Indicator_Scores_RegStep4tr_Z2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_Merlin_Indicator_Scores_RegStep4tr_Z2.csv"
                 },
                 {
-                    "title": "HWBI_Merlin_Domain_Scores_RegStep4tr_Z2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/HWBI_Merlin_Domain_Scores_RegStep4tr_Z2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HWBI_Merlin_Domain_Scores_RegStep4tr_Z2.csv"
                 },
                 {
-                    "title": "FileDescriptions.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519429/FileDescriptions.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FileDescriptions.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519429",
+            "keyword": [
+                "ecosystem services",
+                "human well-being",
+                "spatial interpolation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-23",
-            "references": [
-                "https://doi.org/10.3390/su12229625"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135585,19 +135579,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/su12229625"
+            ],
+            "rights": null,
+            "title": "HWBI Domain and Services Metrics for Puerto Rico 2000-2017"
         },
         {
-            "title": "Sustainability Index _MSAs",
-            "description": "Calculation of average sustainability in US Metropolitan and Micropolitan areas. Three domains of sustainability are measured: economic, social, and environmental. \n\nThis dataset is associated with the following publication:\nBuck, K., K. Summers, and L. Smith. Investigating the relationship between environmental quality, socio-spatial segregation and the social dimension of sustainability in US urban areas.   Sustainable Cities and Society. Elsevier B.V., Amsterdam,  NETHERLANDS, 67(102732): 11, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Kyle Buck",
+                "hasEmail": "mailto:buck.kyle@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519308/documents/Sustainability%20Index%20Metadata.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Calculation of average sustainability in US Metropolitan and Micropolitan areas. Three domains of sustainability are measured: economic, social, and environmental. \n\nThis dataset is associated with the following publication:\nBuck, K., K. Summers, and L. Smith. Investigating the relationship between environmental quality, socio-spatial segregation and the social dimension of sustainability in US urban areas.   Sustainable Cities and Society. Elsevier B.V., Amsterdam,  NETHERLANDS, 67(102732): 11, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519308/Sustainability_ScienceHub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Sustainability_ScienceHub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1519308",
             "keyword": [
@@ -135611,20 +135617,10 @@
                 "resilience",
                 "Vulnerability"
             ],
-            "contactPoint": {
-                "fn": "Kyle Buck",
-                "hasEmail": "mailto:buck.kyle@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Sustainability_ScienceHub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519308/Sustainability_ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-07-01",
-            "references": [
-                "https://doi.org/10.1016/j.scs.2021.102732"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135635,63 +135631,61 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519308/documents/Sustainability%20Index%20Metadata.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.scs.2021.102732"
+            ],
+            "rights": null,
+            "title": "Sustainability Index _MSAs"
         },
         {
-            "title": "Pensacola watershed case study",
-            "description": "This data set contains the spatial layers that were input into ecosystem services models (Maps.zip), including the A2 and B1 landuse change scenarios, and the polygon boundaries for the Pensacola watershed.  This dataset also includes the future climate data (ClimateData.csv) used in scenarios.  Model output for 20 stochastic runs of each A2 and B1 scenario is included in three files: 1) the calculated ES metrics that were used to calculate ES indicators (ESMetrics_CountyYearly.xlsx), 2) the scaled ES indicators used as input into HWBI regression models (ESIndicators_CountyYearly.xlsx), and 3) the calculated HWBI Domain and composite scores (HWBIDomains_CountyYearly.xlsx). \n\nThis dataset is associated with the following publication:\nYee, S., E. Paulukonis, C. Simmons, M. Russell, R. Fulford, L. Harwell, and L. Smith. Projecting effects of land use change on human well-being through changes in ecosystem services.   ECOLOGICAL MODELLING. Elsevier Science BV, Amsterdam,  NETHERLANDS, 440(109358): 20, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1503346",
-            "keyword": [
-                "Human Well-Being Index",
-                "Forecasting",
-                "ecosystem services",
-                "Relationship Functions",
-                "land-use change"
-            ],
             "contactPoint": {
                 "fn": "Susan Yee",
                 "hasEmail": "mailto:yee.susan@epa.gov"
             },
+            "description": "This data set contains the spatial layers that were input into ecosystem services models (Maps.zip), including the A2 and B1 landuse change scenarios, and the polygon boundaries for the Pensacola watershed.  This dataset also includes the future climate data (ClimateData.csv) used in scenarios.  Model output for 20 stochastic runs of each A2 and B1 scenario is included in three files: 1) the calculated ES metrics that were used to calculate ES indicators (ESMetrics_CountyYearly.xlsx), 2) the scaled ES indicators used as input into HWBI regression models (ESIndicators_CountyYearly.xlsx), and 3) the calculated HWBI Domain and composite scores (HWBIDomains_CountyYearly.xlsx). \n\nThis dataset is associated with the following publication:\nYee, S., E. Paulukonis, C. Simmons, M. Russell, R. Fulford, L. Harwell, and L. Smith. Projecting effects of land use change on human well-being through changes in ecosystem services.   ECOLOGICAL MODELLING. Elsevier Science BV, Amsterdam,  NETHERLANDS, 440(109358): 20, (2021).",
             "distribution": [
                 {
-                    "title": "ESIndicators_CountyYearly.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503346/ESIndicators_CountyYearly.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ESIndicators_CountyYearly.xlsx"
                 },
                 {
-                    "title": "ClimateData.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503346/ClimateData.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ClimateData.csv"
                 },
                 {
-                    "title": "ESMetrics_CountyYearly.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503346/ESMetrics_CountyYearly.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ESMetrics_CountyYearly.xlsx"
                 },
                 {
-                    "title": "HWBIDomains_CountyYearly.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503346/HWBIDomains_CountyYearly.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HWBIDomains_CountyYearly.xlsx"
                 },
                 {
-                    "title": "Maps.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503346/Maps.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Maps.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503346",
+            "keyword": [
+                "Human Well-Being Index",
+                "Forecasting",
+                "ecosystem services",
+                "Relationship Functions",
+                "land-use change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-01-30",
-            "references": [
-                "https://doi.org/10.1016/j.ecolmodel.2020.109358"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135701,19 +135695,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolmodel.2020.109358"
+            ],
+            "rights": null,
+            "title": "Pensacola watershed case study"
         },
         {
-            "title": "Independent roles of beta-adrenergic and glucocorticoid receptors in systemic and pulmonary effects of ozone",
-            "description": "A manuscript describing the independent roles of beta adrenergic and glucocorticoid receptors in mediating ozone-induced pulmonary and systemic effects. \n\nThis dataset is associated with the following publication:\nHenriquez, A., S. Snow, M.C. Schladweiler, C. Miller, and U. Kodavanti. Independent roles of beta-adrenergic and glucocorticoid receptors in systemic and pulmonary effects of ozone.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 32(4): 155-169, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Urmila Kodavanti",
+                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
+            },
+            "description": "A manuscript describing the independent roles of beta adrenergic and glucocorticoid receptors in mediating ozone-induced pulmonary and systemic effects. \n\nThis dataset is associated with the following publication:\nHenriquez, A., S. Snow, M.C. Schladweiler, C. Miller, and U. Kodavanti. Independent roles of beta-adrenergic and glucocorticoid receptors in systemic and pulmonary effects of ozone.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 32(4): 155-169, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517608/Copy%20of%20ScienceHub%20data%20-%20Henriquez%20et%20al.%202020%20Inh%20Tox.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of ScienceHub data - Henriquez et al. 2020 Inh Tox.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1517608",
             "keyword": [
@@ -135727,20 +135731,10 @@
                 "lung injury",
                 "metabolic response"
             ],
-            "contactPoint": {
-                "fn": "Urmila Kodavanti",
-                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Copy of ScienceHub data - Henriquez et al. 2020 Inh Tox.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517608/Copy%20of%20ScienceHub%20data%20-%20Henriquez%20et%20al.%202020%20Inh%20Tox.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-21",
-            "references": [
-                "https://doi.org/10.1080/08958378.2020.1759736"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135750,19 +135744,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08958378.2020.1759736"
+            ],
+            "rights": null,
+            "title": "Independent roles of beta-adrenergic and glucocorticoid receptors in systemic and pulmonary effects of ozone"
         },
         {
-            "title": "PRISM Scaled Dataset",
-            "description": "Data for 2015 US Census Tracts includes multi-hazard exposure estimates for 12 natural hazards. There are also estimates of loss, vulnerability, and risk for land area, population, and property within each tract. \n\nThis dataset is associated with the following publication:\nBuck, K., and K. Summers. Application of a multi-hazard risk assessment for local planning.   Geomatics, Natural Hazards and Risk. Taylor & Francis Group, London,  UK, 11(1): 2058-2078, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Kyle Buck",
+                "hasEmail": "mailto:buck.kyle@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519307/documents/PRISM%20Scaled%20ScienceHub%20Metadata.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Data for 2015 US Census Tracts includes multi-hazard exposure estimates for 12 natural hazards. There are also estimates of loss, vulnerability, and risk for land area, population, and property within each tract. \n\nThis dataset is associated with the following publication:\nBuck, K., and K. Summers. Application of a multi-hazard risk assessment for local planning.   Geomatics, Natural Hazards and Risk. Taylor & Francis Group, London,  UK, 11(1): 2058-2078, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519307/Buck_PRISM%20Scaled%20ScienceHub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Buck_PRISM Scaled ScienceHub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1519307",
             "keyword": [
@@ -135774,20 +135780,10 @@
                 "policy",
                 "local"
             ],
-            "contactPoint": {
-                "fn": "Kyle Buck",
-                "hasEmail": "mailto:buck.kyle@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Buck_PRISM Scaled ScienceHub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519307/Buck_PRISM%20Scaled%20ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-11-01",
-            "references": [
-                "https://doi.org/10.1080/19475705.2020.1828190"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135798,47 +135794,45 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519307/documents/PRISM%20Scaled%20ScienceHub%20Metadata.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1080/19475705.2020.1828190"
+            ],
+            "rights": null,
+            "title": "PRISM Scaled Dataset"
         },
         {
-            "title": "Data for effects resulting from exposure to dioxin, and observed survival and fecundity by age and size for unexposed populations",
-            "description": "These laboratory data for estimates of change in fertility and survival rates observed relative to control (unexposed) conditions for fundulus heteroclitus exposed to varying levels of 2,3,7,8-tetrachlorodibenzo-p-dioxin including 112, 296, and 875 pg/g are relative rates, and thus they are unitless.\n\nThe data for observed survival and fecundity by age and size for populations of fundulus heteroclitus that were considered unexposed to chemical stressors contains the following units:  survival rates are fraction surviving per year and fecundity rates are eggs per year. \n\nThis dataset is associated with the following publication:\nMiller, D., B. Clark, and D. Nacci. A multidimensional density dependent matrix population model for assessing risk of stressors to fish populations.   ECOTOXICOLOGY AND ENVIRONMENTAL SAFETY. Elsevier Science Ltd, New York, NY, USA, 201: 1-8, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504161",
-            "keyword": [
-                "population ecology",
-                "density dependence",
-                "matrix models",
-                "ecological risk assessment"
-            ],
             "contactPoint": {
                 "fn": "David Miller",
                 "hasEmail": "mailto:miller.davidh@epa.gov"
             },
+            "description": "These laboratory data for estimates of change in fertility and survival rates observed relative to control (unexposed) conditions for fundulus heteroclitus exposed to varying levels of 2,3,7,8-tetrachlorodibenzo-p-dioxin including 112, 296, and 875 pg/g are relative rates, and thus they are unitless.\n\nThe data for observed survival and fecundity by age and size for populations of fundulus heteroclitus that were considered unexposed to chemical stressors contains the following units:  survival rates are fraction surviving per year and fecundity rates are eggs per year. \n\nThis dataset is associated with the following publication:\nMiller, D., B. Clark, and D. Nacci. A multidimensional density dependent matrix population model for assessing risk of stressors to fish populations.   ECOTOXICOLOGY AND ENVIRONMENTAL SAFETY. Elsevier Science Ltd, New York, NY, USA, 201: 1-8, (2020).",
             "distribution": [
                 {
-                    "title": "Data For Observed Survival And Fecundity By Age And Size (Table 2) .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504161/Data%20For%20Observed%20Survival%20And%20Fecundity%20By%20Age%20And%20Size%20%28Table%202%29%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data For Observed Survival And Fecundity By Age And Size (Table 2) .xlsx"
                 },
                 {
-                    "title": "Data For Effects Resulting From Exposure To Dioxin (Table 1).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504161/Data%20For%20Effects%20Resulting%20From%20Exposure%20To%20Dioxin%20%28Table%201%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data For Effects Resulting From Exposure To Dioxin (Table 1).xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504161",
+            "keyword": [
+                "population ecology",
+                "density dependence",
+                "matrix models",
+                "ecological risk assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-05",
-            "references": [
-                "https://doi.org/10.1016/j.ecoenv.2020.110786"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135848,41 +135842,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecoenv.2020.110786"
+            ],
+            "rights": null,
+            "title": "Data for effects resulting from exposure to dioxin, and observed survival and fecundity by age and size for unexposed populations"
         },
         {
-            "title": "Intersection of Natural Hazard Vulnerability and RCRA Site Location",
-            "description": "Co-occurrence of natural hazard exposures and RCRA site locations at the county level where natural hazards are in the top quartile of exposures. \n\nThis dataset is associated with the following publication:\nSummers, K., A. Lamper, and K. Buck. National Hazards Vulnerability and the Remediation, Restoration and Revitalization of Contaminated Sites \u2013 2. RCRA Sites..   Sustainability. MDPI AG, Basel,  SWITZERLAND, 13(2): 16, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520858",
-            "keyword": [
-                "RCRA",
-                "natural hazards",
-                "exposure",
-                "toxic releases"
-            ],
             "contactPoint": {
                 "fn": "James Summers",
                 "hasEmail": "mailto:summers.kevin@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520858/documents/Data%20Dictionary_RCRA-CRSI.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Co-occurrence of natural hazard exposures and RCRA site locations at the county level where natural hazards are in the top quartile of exposures. \n\nThis dataset is associated with the following publication:\nSummers, K., A. Lamper, and K. Buck. National Hazards Vulnerability and the Remediation, Restoration and Revitalization of Contaminated Sites \u2013 2. RCRA Sites..   Sustainability. MDPI AG, Basel,  SWITZERLAND, 13(2): 16, (2021).",
             "distribution": [
                 {
-                    "title": "CRSIRCRA_FrequencyTables.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520858/CRSIRCRA_FrequencyTables.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CRSIRCRA_FrequencyTables.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520858",
+            "keyword": [
+                "RCRA",
+                "natural hazards",
+                "exposure",
+                "toxic releases"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-04",
-            "references": [
-                "https://doi.org/10.3390/su13020965"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135893,42 +135889,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520858/documents/Data%20Dictionary_RCRA-CRSI.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.3390/su13020965"
+            ],
+            "rights": null,
+            "title": "Intersection of Natural Hazard Vulnerability and RCRA Site Location"
         },
         {
-            "title": "Intersection of Natural Hazard Vulnerability and Superfund Site Location",
-            "description": "Spreadsheet lists all active and upcoming Superfund sites and their vulnerability to 12 natural hazards using a vulnerability score between 0 and 100. \n\nThis dataset is associated with the following publication:\nSummers, K., A. Lamaper, and K. Buck. National Hazards Vulnerability and the Remediation, Restoration and Revitalization of Contaminated Sites \u2013 1. Superfund.   ENVIRONMENTAL MANAGEMENT. Springer-Verlag, New York, NY, USA,  14, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1519284",
-            "keyword": [
-                "Superfund",
-                "natural hazards",
-                "exposure",
-                "toxic releases"
-            ],
             "contactPoint": {
                 "fn": "James Summers",
                 "hasEmail": "mailto:summers.kevin@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519284/documents/Data%20Dictionary_SF-CRSI.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Spreadsheet lists all active and upcoming Superfund sites and their vulnerability to 12 natural hazards using a vulnerability score between 0 and 100. \n\nThis dataset is associated with the following publication:\nSummers, K., A. Lamaper, and K. Buck. National Hazards Vulnerability and the Remediation, Restoration and Revitalization of Contaminated Sites \u2013 1. Superfund.   ENVIRONMENTAL MANAGEMENT. Springer-Verlag, New York, NY, USA,  14, (2021).",
             "distribution": [
                 {
-                    "title": "SF_CRSI_OLEM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519284/SF_CRSI_OLEM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SF_CRSI_OLEM.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519284",
+            "keyword": [
+                "Superfund",
+                "natural hazards",
+                "exposure",
+                "toxic releases"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-08-26",
-            "references": [
-                "https://doi.org/10.1007/s00267-021-01459-w"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -135939,20 +135935,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519284/documents/Data%20Dictionary_SF-CRSI.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1007/s00267-021-01459-w"
+            ],
+            "rights": null,
+            "title": "Intersection of Natural Hazard Vulnerability and Superfund Site Location"
         },
         {
-            "title": "ESR1 expression and DNA methylation data for FHM exposed to EE2",
-            "description": "This dataset contains data for adult male fathead minnows exposed to EE2 (a synthetic estrogen). It is a targeted study on the response of the esr1 gene (expression and DNA methylation profiles) to estrogen exposure. It contains mean and standard deviation for DNA methylation levels per treatment group, and gene expression data. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Janine Fetke",
+                "hasEmail": "mailto:fetke.janine@epa.gov"
+            },
+            "description": "This dataset contains data for adult male fathead minnows exposed to EE2 (a synthetic estrogen). It is a targeted study on the response of the esr1 gene (expression and DNA methylation profiles) to estrogen exposure. It contains mean and standard deviation for DNA methylation levels per treatment group, and gene expression data. ",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521251/esr1%20meta%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "esr1 meta data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521251",
             "keyword": [
@@ -135963,19 +135967,11 @@
                 "fathead minnow",
                 "esr1"
             ],
-            "contactPoint": {
-                "fn": "Janine Fetke",
-                "hasEmail": "mailto:fetke.janine@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "esr1 meta data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521251/esr1%20meta%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-14",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -135984,43 +135980,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "ESR1 expression and DNA methylation data for FHM exposed to EE2"
         },
         {
-            "title": "Characterization data for trout liver S9 fractions used by Droge et al to measure the in vitro intrinsic clearance of cationic surfactants",
-            "description": "This ScienceHub dataset provides characterization data for a pooled sample of trout liver S9 fractions that was used to study the in vitro intrinsic clearance of selected cationic surfactants.  These data describe the activity of the pooled sample toward prototypical substrates for cytochrome P450 (CYP) 1A, glutathione-S-transferase, and UDP-glucuronosyltranserase.  Also provided are the protein content and total CYP content of the sample and well as information pertaining to the size and gender of fish from which the original sample was obtained. \n\nThis dataset is associated with the following publication:\nDroge, S., J. Armitage, J. Arnot, P. Fitzsimmons, and J. Nichols. Biotransformation Potential of Cationic Surfactants in Fish Assessed with Rainbow Trout Liver S9 Fractions.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 40(11): 3123-3136, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1521160",
-            "keyword": [
-                "rainbow trout",
-                "cationic surfactant",
-                "bioaccumulation assessment",
-                "liver S9 fraction",
-                "biotransformation"
-            ],
             "contactPoint": {
                 "fn": "Patrick Fitzsimmons",
                 "hasEmail": "mailto:fitzsimmons.patrick@epa.gov"
             },
+            "description": "This ScienceHub dataset provides characterization data for a pooled sample of trout liver S9 fractions that was used to study the in vitro intrinsic clearance of selected cationic surfactants.  These data describe the activity of the pooled sample toward prototypical substrates for cytochrome P450 (CYP) 1A, glutathione-S-transferase, and UDP-glucuronosyltranserase.  Also provided are the protein content and total CYP content of the sample and well as information pertaining to the size and gender of fish from which the original sample was obtained. \n\nThis dataset is associated with the following publication:\nDroge, S., J. Armitage, J. Arnot, P. Fitzsimmons, and J. Nichols. Biotransformation Potential of Cationic Surfactants in Fish Assessed with Rainbow Trout Liver S9 Fractions.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 40(11): 3123-3136, (2021).",
             "distribution": [
                 {
-                    "title": "Droge et al_cationic surfactants_ScienceHub_entry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521160/Droge%20et%20al_cationic%20surfactants_ScienceHub_entry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Droge et al_cationic surfactants_ScienceHub_entry.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521160",
+            "keyword": [
+                "rainbow trout",
+                "cationic surfactant",
+                "bioaccumulation assessment",
+                "liver S9 fraction",
+                "biotransformation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-25",
-            "references": [
-                "https://doi.org/10.1002/etc.5189",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9187044"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136030,19 +136023,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5189",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9187044"
+            ],
+            "rights": null,
+            "title": "Characterization data for trout liver S9 fractions used by Droge et al to measure the in vitro intrinsic clearance of cationic surfactants"
         },
         {
-            "title": "Quantitative response-response relationships linking aromatase inhibition to decreased fecundity are conserved across three fishes with asynchronous oocyte development",
-            "description": "Data used in the creation of each figure and table cited in Doering et al. (2019; DOI: 10.1021/acs.est.9b02606) are provided. \n\nThis dataset is associated with the following publication:\nDoering, J., D. Villeneuve, S. Poole, B. Blackwell, K. Jensen, M. Kahl, A. Kittelson, D. Feifarek, C. Tilton, C. Lalone, and G. Ankley. Quantitative response-response relationships linking aromatase inhibition to decreased fecunditiy are conserved across three fishes with asynchronous oocyte development.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(17): 10470-10478, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Daniel Villeneuve",
+                "hasEmail": "mailto:villeneuve.dan@epa.gov"
+            },
+            "description": "Data used in the creation of each figure and table cited in Doering et al. (2019; DOI: 10.1021/acs.est.9b02606) are provided. \n\nThis dataset is associated with the following publication:\nDoering, J., D. Villeneuve, S. Poole, B. Blackwell, K. Jensen, M. Kahl, A. Kittelson, D. Feifarek, C. Tilton, C. Lalone, and G. Ankley. Quantitative response-response relationships linking aromatase inhibition to decreased fecunditiy are conserved across three fishes with asynchronous oocyte development.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(17): 10470-10478, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503690/qAOP%20Draft%20Manuscript%20Data%2004-16-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "qAOP Draft Manuscript Data 04-16-2020.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503690",
             "keyword": [
@@ -136055,20 +136059,10 @@
                 "screening and prioritization",
                 "aquatic ecosystems"
             ],
-            "contactPoint": {
-                "fn": "Daniel Villeneuve",
-                "hasEmail": "mailto:villeneuve.dan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "qAOP Draft Manuscript Data 04-16-2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503690/qAOP%20Draft%20Manuscript%20Data%2004-16-2020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-16",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b02606"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136078,34 +136072,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b02606"
+            ],
+            "rights": null,
+            "title": "Quantitative response-response relationships linking aromatase inhibition to decreased fecundity are conserved across three fishes with asynchronous oocyte development"
         },
         {
-            "title": "Application of a multiplex salivary immunoassay to detect sporadic incident norovirus infections ",
-            "description": "Epidemiology data from beachgoers including demographic details. Results from saliva tests for markers of  infection with waterborne pathogens. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact Tim Wade (wade.tim@epa.gov) for details regarding data access. Format: Data are stored in SAS datasets and MS Excel files. Data are documented with codebooks in MS Word describing variables. \n\nThis dataset is associated with the following publication:\nWade, T., S. Griffin, A. Egorov, E. Sams, E. Hudgens, S. Augustine, S. Deflorio-Barker, T. Plunkett, A. Dufour, J. Styles, and K. Oshima. Application of a multiplex salivary immunoassay to detect sporadic incident norovirus infections.   Scientific Reports. Nature Publishing Group, London,  UK, 9(19576): 1, (2019).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Timothy Wade",
+                "hasEmail": "mailto:wade.tim@epa.gov"
+            },
+            "description": "Epidemiology data from beachgoers including demographic details. Results from saliva tests for markers of  infection with waterborne pathogens. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact Tim Wade (wade.tim@epa.gov) for details regarding data access. Format: Data are stored in SAS datasets and MS Excel files. Data are documented with codebooks in MS Word describing variables. \n\nThis dataset is associated with the following publication:\nWade, T., S. Griffin, A. Egorov, E. Sams, E. Hudgens, S. Augustine, S. Deflorio-Barker, T. Plunkett, A. Dufour, J. Styles, and K. Oshima. Application of a multiplex salivary immunoassay to detect sporadic incident norovirus infections.   Scientific Reports. Nature Publishing Group, London,  UK, 9(19576): 1, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1504465",
             "keyword": [
                 "beach water quality",
                 "swimming",
                 "diarrhea"
             ],
-            "contactPoint": {
-                "fn": "Timothy Wade",
-                "hasEmail": "mailto:wade.tim@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-01",
-            "references": [
-                "https://doi.org/10.1038/s41598-019-56040-7"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136115,19 +136109,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-019-56040-7"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Application of a multiplex salivary immunoassay to detect sporadic incident norovirus infections "
         },
         {
-            "title": "Estuarine Habitat and Juvenile Dungeness Crab Data (2010-2011)",
-            "description": "This dataset contains juvenile Dungeness crab (Cancer magister) abundance data and associated habitat data from three estuaries in Oregon (Tillamook, Yaquina, and Alsea bays).  These data were collected by EPA surveys in 2010-2011.  Additionally, this dataset includes areal data on National Wetlands Inventory (NWI) habitat classes within our study areas. \n\nThis dataset is associated with the following publication:\nLewis, N., D. Young, C. Folger, and T. DeWitt. Assessing the Relative Importance of Estuarine Nursery Habitats \u2013 a Dungeness Crab (Cancer magister) Case Study.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA,  s12237-020-00821-1, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Theodore Dewitt",
+                "hasEmail": "mailto:dewitt.ted@epa.gov"
+            },
+            "description": "This dataset contains juvenile Dungeness crab (Cancer magister) abundance data and associated habitat data from three estuaries in Oregon (Tillamook, Yaquina, and Alsea bays).  These data were collected by EPA surveys in 2010-2011.  Additionally, this dataset includes areal data on National Wetlands Inventory (NWI) habitat classes within our study areas. \n\nThis dataset is associated with the following publication:\nLewis, N., D. Young, C. Folger, and T. DeWitt. Assessing the Relative Importance of Estuarine Nursery Habitats \u2013 a Dungeness Crab (Cancer magister) Case Study.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA,  s12237-020-00821-1, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517800/Crabs%26Habitat_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Crabs&Habitat_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1517800",
             "keyword": [
@@ -136139,20 +136143,10 @@
                 "ecological production function",
                 "final ecosystem goods and services (FEGS)"
             ],
-            "contactPoint": {
-                "fn": "Theodore Dewitt",
-                "hasEmail": "mailto:dewitt.ted@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Crabs&Habitat_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517800/Crabs%26Habitat_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-02-13",
-            "references": [
-                "https://doi.org/10.1007/s12237-020-00821-1"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136162,42 +136156,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12237-020-00821-1"
+            ],
+            "rights": null,
+            "title": "Estuarine Habitat and Juvenile Dungeness Crab Data (2010-2011)"
         },
         {
-            "title": "Case study in 21st century ecotoxicology:  using in vitro aromatase inhibition data to predict short term in vivo responses in adult female fish",
-            "description": "This research was designed to evaluate whether a biologically-based computational model aligned with an adverse outcome pathway (AOP) could effectively predict animal (in vivo) responses to chemicals shown to inhibit the enzyme aromatase in a non-animal (in vitro) screening assays. Aromatase is an enzyme that plays a critical role in the synthesis of estrogens, an important class of hormones, and chemicals that inhibit aromatase are viewed as probable endocrine disrupting compounds. Although the model was not able to accurately predict the average in vivo responses observed for all chemicals tested, there was strong qualitative to semi-quantitative agreement with the proposed AOP and predictions did fall within the distribution of measured values. Consequently, this \u201cnew approach methodology\u201d likely has utility for screening-level assessments. This work helps to establish the confidence and limitations of this approach.\nThe data set includes:\n1) High throughput screening results for chemicals identified as aromatase inhibitors. 2) Novel in vitro aromatase inhibition data for six chemicals. 3) Modeled predictions of impacts on 17b-estradiol and vitellogenin concentrations over a range of concentrations. 4) Measured biological effects of 3 aromatase inhibitors in fathead minnows exposed for 24 h. 5) Measured plasma and water concentrations of the test chemicals. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., B. Blackwell, J. Cavallin, W. Cheng, R. Conolly, D. Feifarek, K. Jensen, M. Kahl, R. Milsk, S. Poole, E. Randolph, T. Saari, and G. Ankley. Case study in 21st century ecotoxicology:  Using in vitro aromatase inhibition data to predict short term in vivo responses in adult female fish.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 40(4): 1155-1170, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520048",
-            "keyword": [
-                "adverse outcome pathway",
-                "ecotoxicology",
-                "endocrine disruption",
-                "screening and prioritization",
-                "aquatic ecosystems"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "This research was designed to evaluate whether a biologically-based computational model aligned with an adverse outcome pathway (AOP) could effectively predict animal (in vivo) responses to chemicals shown to inhibit the enzyme aromatase in a non-animal (in vitro) screening assays. Aromatase is an enzyme that plays a critical role in the synthesis of estrogens, an important class of hormones, and chemicals that inhibit aromatase are viewed as probable endocrine disrupting compounds. Although the model was not able to accurately predict the average in vivo responses observed for all chemicals tested, there was strong qualitative to semi-quantitative agreement with the proposed AOP and predictions did fall within the distribution of measured values. Consequently, this \u201cnew approach methodology\u201d likely has utility for screening-level assessments. This work helps to establish the confidence and limitations of this approach.\nThe data set includes:\n1) High throughput screening results for chemicals identified as aromatase inhibitors. 2) Novel in vitro aromatase inhibition data for six chemicals. 3) Modeled predictions of impacts on 17b-estradiol and vitellogenin concentrations over a range of concentrations. 4) Measured biological effects of 3 aromatase inhibitors in fathead minnows exposed for 24 h. 5) Measured plasma and water concentrations of the test chemicals. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., B. Blackwell, J. Cavallin, W. Cheng, R. Conolly, D. Feifarek, K. Jensen, M. Kahl, R. Milsk, S. Poole, E. Randolph, T. Saari, and G. Ankley. Case study in 21st century ecotoxicology:  Using in vitro aromatase inhibition data to predict short term in vivo responses in adult female fish.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 40(4): 1155-1170, (2021).",
             "distribution": [
                 {
-                    "title": "Formatted Aromatase inhib QAOP MS Part 1 Science Hub 2020-10-02.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520048/Formatted%20Aromatase%20inhib%20QAOP%20MS%20Part%201%20Science%20Hub%202020-10-02.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Formatted Aromatase inhib QAOP MS Part 1 Science Hub 2020-10-02.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520048",
+            "keyword": [
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "endocrine disruption",
+                "screening and prioritization",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-06",
-            "references": [
-                "https://doi.org/10.1002/etc.4968"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136207,41 +136201,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4968"
+            ],
+            "rights": null,
+            "title": "Case study in 21st century ecotoxicology:  using in vitro aromatase inhibition data to predict short term in vivo responses in adult female fish"
         },
         {
-            "title": "Xenpous leavis deiodinase type 3 enzyme activity characterization and chemical screening data",
-            "description": "Data set includes optimized assay parameters and kinetic characterization for xenopus laevis deiodinase type 3 enzyme, and inhibition activity of 352 ToxCast chemicals against this enzyme. \n\nThis dataset is associated with the following publication:\nMayasich, S., J. Korte, J. Denny, P. Hartig, J. Olker, P. Degoey, J. O'Flanagan, S. Degitz, and M. Hornung. Xenopus laevis and human type 3 iodothyronine deiodinase enzyme cross-species sensitivity to inhibition by ToxCast chemicals.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  73: 105141, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504033",
-            "keyword": [
-                "Xenopus",
-                "thyroid",
-                "deiodinase",
-                "Enzyme activity"
-            ],
             "contactPoint": {
                 "fn": "Michael Hornung",
                 "hasEmail": "mailto:hornung.michael@epa.gov"
             },
+            "description": "Data set includes optimized assay parameters and kinetic characterization for xenopus laevis deiodinase type 3 enzyme, and inhibition activity of 352 ToxCast chemicals against this enzyme. \n\nThis dataset is associated with the following publication:\nMayasich, S., J. Korte, J. Denny, P. Hartig, J. Olker, P. Degoey, J. O'Flanagan, S. Degitz, and M. Hornung. Xenopus laevis and human type 3 iodothyronine deiodinase enzyme cross-species sensitivity to inhibition by ToxCast chemicals.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  73: 105141, (2021).",
             "distribution": [
                 {
-                    "title": "200714_Mayasich_et_al_Xldio3 screening data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504033/200714_Mayasich_et_al_Xldio3%20screening%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "200714_Mayasich_et_al_Xldio3 screening data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504033",
+            "keyword": [
+                "Xenopus",
+                "thyroid",
+                "deiodinase",
+                "Enzyme activity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-19",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2021.105141"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136251,19 +136245,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2021.105141"
+            ],
+            "rights": null,
+            "title": "Xenpous leavis deiodinase type 3 enzyme activity characterization and chemical screening data"
         },
         {
-            "title": "Assessment of Mercury Cycling in the St Louis River, MN using Mercury and Food Web (Carbon and Nitrogen) Stable Isotopes: U.S. Geological Survey Data Release",
-            "description": "Mercury concentration, mercury stable isotope ratio, and carbon and nitrogen stable isotope ratio data as applicable for sediment, water, invertebrates, and fish collected from the St. Louis River Area of Concern (MN-WI) and the associated reference site, the lower Bad River (WI). \n\nThis dataset is associated with the following publication:\nJanssen, S., J. Hoffman, R. Lepak, D. Krabbenhoft, D. Walters, C. Eagles-Smith, G. Peterson, J. Ogorek, J. DeWild, A. Cotter, M. Pearson, M. Tate, R. Yeardley, and M. Mills. Examining historical mercury sources in the St. Louis River estuary: How legacy contamination influences biological mercury levels in Great Lakes coastal regions.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 779: 146284, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Joel Hoffman",
+                "hasEmail": "mailto:hoffman.joel@epa.gov"
+            },
+            "description": "Mercury concentration, mercury stable isotope ratio, and carbon and nitrogen stable isotope ratio data as applicable for sediment, water, invertebrates, and fish collected from the St. Louis River Area of Concern (MN-WI) and the associated reference site, the lower Bad River (WI). \n\nThis dataset is associated with the following publication:\nJanssen, S., J. Hoffman, R. Lepak, D. Krabbenhoft, D. Walters, C. Eagles-Smith, G. Peterson, J. Ogorek, J. DeWild, A. Cotter, M. Pearson, M. Tate, R. Yeardley, and M. Mills. Examining historical mercury sources in the St. Louis River estuary: How legacy contamination influences biological mercury levels in Great Lakes coastal regions.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 779: 146284, (2021).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/5f43b20582ce4c3d1222d29e",
+                    "title": "https://www.sciencebase.gov/catalog/item/5f43b20582ce4c3d1222d29e"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520946",
             "keyword": [
@@ -136273,19 +136276,10 @@
                 "Great Lakes",
                 "stable isotopes"
             ],
-            "contactPoint": {
-                "fn": "Joel Hoffman",
-                "hasEmail": "mailto:hoffman.joel@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.sciencebase.gov/catalog/item/5f43b20582ce4c3d1222d29e",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/5f43b20582ce4c3d1222d29e"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-08-01",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2021.146284"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136295,20 +136289,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2021.146284"
+            ],
+            "rights": null,
+            "title": "Assessment of Mercury Cycling in the St Louis River, MN using Mercury and Food Web (Carbon and Nitrogen) Stable Isotopes: U.S. Geological Survey Data Release"
         },
         {
-            "title": "Advancing translational research in environmental science: The role and impact of social science",
-            "description": "Our dataset are transcripts and codebooks for a focus group study. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: Contact Katie Williams, williams.kathleen@epa.gov. Format: The data are transcripts and protected by IRB approvals. \n\nThis dataset is associated with the following publication:\nEisenhauer, E., K. Williams, K. Margeson, S. Paczuski, K. Mulvaney, and M.C. Hano. Advancing translational research in environmental science: The role and impact of social science.   Environmental Science & Policy. Elsevier Science Ltd, New York, NY, USA, 120: 165-172, (2021).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy; EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Kathleen Williams",
+                "hasEmail": "mailto:williams.kathleen@epa.gov"
+            },
+            "description": "Our dataset are transcripts and codebooks for a focus group study. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: Contact Katie Williams, williams.kathleen@epa.gov. Format: The data are transcripts and protected by IRB approvals. \n\nThis dataset is associated with the following publication:\nEisenhauer, E., K. Williams, K. Margeson, S. Paczuski, K. Mulvaney, and M.C. Hano. Advancing translational research in environmental science: The role and impact of social science.   Environmental Science & Policy. Elsevier Science Ltd, New York, NY, USA, 120: 165-172, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1521080",
             "keyword": [
                 "social science",
@@ -136316,14 +136314,10 @@
                 "interdisciplinary research",
                 "applied social science"
             ],
-            "contactPoint": {
-                "fn": "Kathleen Williams",
-                "hasEmail": "mailto:williams.kathleen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-06",
-            "references": [
-                "https://doi.org/10.1016/j.envsci.2021.03.010"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136333,19 +136327,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envsci.2021.03.010"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy; EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "title": "Advancing translational research in environmental science: The role and impact of social science"
         },
         {
-            "title": "Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber--Data Set",
-            "description": "The data set contains all data used to generate the figures included in the publication, Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber surfaces1.  The data is arranged by figures and the excel spreadsheet tabs indicate the figure the data is from.  All the data presented in the excel file is clearly labeled.\n\n1. Thornton, S.B.; Boggins, S.J.; Peloquin, D.M.; Luxton, T.P. and Clar, J.G. (2020). Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber. Science of the Total Environment 737: 7. \n\nThis dataset is associated with the following publication:\nThorton, S.B., S.J. Boggins, D.M. Peloquin, T.P. Luxton, and J.G. Clar. Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 737: 139451, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Todd Luxton",
+                "hasEmail": "mailto:luxton.todd@epa.gov"
+            },
+            "description": "The data set contains all data used to generate the figures included in the publication, Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber surfaces1.  The data is arranged by figures and the excel spreadsheet tabs indicate the figure the data is from.  All the data presented in the excel file is clearly labeled.\n\n1. Thornton, S.B.; Boggins, S.J.; Peloquin, D.M.; Luxton, T.P. and Clar, J.G. (2020). Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber. Science of the Total Environment 737: 7. \n\nThis dataset is associated with the following publication:\nThorton, S.B., S.J. Boggins, D.M. Peloquin, T.P. Luxton, and J.G. Clar. Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 737: 139451, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521323/ConsumerProducts-Data%20Summary.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ConsumerProducts-Data Summary.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521323",
             "keyword": [
@@ -136356,20 +136360,10 @@
                 "Speciation",
                 "consumer products"
             ],
-            "contactPoint": {
-                "fn": "Todd Luxton",
-                "hasEmail": "mailto:luxton.todd@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ConsumerProducts-Data Summary.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521323/ConsumerProducts-Data%20Summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-02",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2020.139451"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136379,19 +136373,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2020.139451"
+            ],
+            "rights": null,
+            "title": "Release and transformation of nanoparticle additives from surface coatings on pristine & weathered pressure treated lumber--Data Set"
         },
         {
-            "title": "Ozone- Induced Acute Phase Response in Lung Versus Liver: The Role of Adrenal-Derived Stress Hormones",
-            "description": "The data set pertains to the published research results in a given paper. \nIndividual observations are shown for each pertaining figure or table in the paper.\n\nEach page pertaining to a given table or figure contain biological observations/data for given end point for each individual observation/animal. Experimental observations- animal number, treatment, exposure condition, time point, and parameters assessed are shown in the columns. Each raw shows data for individual animal/replicate for a given condition. Each page also contains copied graph/table published in the paper pertaining to the data on the page. \n\nThis dataset is associated with the following publication:\nAlewel, D., A. Henriquez, C. Colonna, S. Snow, M.C. Schladweiler, C. Miller, and U. Kodavanti. Ozone-Induced Acute Phase Response in Lung Versus Liver: The Role of Adrenal-Derived Stress Hormones.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 84(6): 235-248, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Urmila Kodavanti",
+                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
+            },
+            "description": "The data set pertains to the published research results in a given paper. \nIndividual observations are shown for each pertaining figure or table in the paper.\n\nEach page pertaining to a given table or figure contain biological observations/data for given end point for each individual observation/animal. Experimental observations- animal number, treatment, exposure condition, time point, and parameters assessed are shown in the columns. Each raw shows data for individual animal/replicate for a given condition. Each page also contains copied graph/table published in the paper pertaining to the data on the page. \n\nThis dataset is associated with the following publication:\nAlewel, D., A. Henriquez, C. Colonna, S. Snow, M.C. Schladweiler, C. Miller, and U. Kodavanti. Ozone-Induced Acute Phase Response in Lung Versus Liver: The Role of Adrenal-Derived Stress Hormones.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 84(6): 235-248, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521132/Acute%20Phase%20Response%20ScienceHub%20JTEH%20Devin%20Alewel%202020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Acute Phase Response ScienceHub JTEH Devin Alewel 2020.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521132",
             "keyword": [
@@ -136403,20 +136407,10 @@
                 "neuroendocrine",
                 "adrenal-derived stress hormones"
             ],
-            "contactPoint": {
-                "fn": "Urmila Kodavanti",
-                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Acute Phase Response ScienceHub JTEH Devin Alewel 2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521132/Acute%20Phase%20Response%20ScienceHub%20JTEH%20Devin%20Alewel%202020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-01",
-            "references": [
-                "https://doi.org/10.1080/15287394.2020.1858466"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136426,42 +136420,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/15287394.2020.1858466"
+            ],
+            "rights": null,
+            "title": "Ozone- Induced Acute Phase Response in Lung Versus Liver: The Role of Adrenal-Derived Stress Hormones"
         },
         {
-            "title": "Data used to produce figures and tables",
-            "description": "The dataset are the data used to produce figure in manuscript. \n\nThis dataset is associated with the following publication:\nTang, M., D. Lytle, and J. Botkins. Accumulation and Release of Arsenic from Cast Iron: Impact of Initial Arsenic and Orthophosphate Concentrations.    WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 194: 116942, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519151",
-            "keyword": [
-                "arsenate",
-                "accumulation and release",
-                "cast iron scale",
-                "orthophosphate corrosion control",
-                "drinking water"
-            ],
             "contactPoint": {
                 "fn": "Darren Lytle",
                 "hasEmail": "mailto:lytle.darren@epa.gov"
             },
+            "description": "The dataset are the data used to produce figure in manuscript. \n\nThis dataset is associated with the following publication:\nTang, M., D. Lytle, and J. Botkins. Accumulation and Release of Arsenic from Cast Iron: Impact of Initial Arsenic and Orthophosphate Concentrations.    WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 194: 116942, (2021).",
             "distribution": [
                 {
-                    "title": "Arsenic_Data_Clearance.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519151/Arsenic_Data_Clearance.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Arsenic_Data_Clearance.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519151",
+            "keyword": [
+                "arsenate",
+                "accumulation and release",
+                "cast iron scale",
+                "orthophosphate corrosion control",
+                "drinking water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-02-15",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2021.116942"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136471,41 +136465,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2021.116942"
+            ],
+            "rights": null,
+            "title": "Data used to produce figures and tables"
         },
         {
-            "title": "Data used in tables or figure.",
-            "description": "The dataset  included is data used to produce figures in manuscript. \n\nThis dataset is associated with the following publication:\nLytle, D., C. Formal, E. Dore, C. Muhlen, S. Harmon, D. Williams, S. Triantafyllidou, and M. Pham. SYNTHESIS AND CHARACTERIZATION OF STABLE LEAD (II) ORTHOPHOSPHATE NANOPARTICLE SUSPENSIONS.   JOURNAL OF ENVIRONMENTAL SCIENCE AND HEALTH, PART A. Marcel Dekker Incorporated, New York, NY, USA, 55(13): 1504-1512, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1518478",
-            "keyword": [
-                "lead",
-                "Orthophosphate",
-                "Nanoparticle",
-                "drinking water"
-            ],
             "contactPoint": {
                 "fn": "Darren Lytle",
                 "hasEmail": "mailto:lytle.darren@epa.gov"
             },
+            "description": "The dataset  included is data used to produce figures in manuscript. \n\nThis dataset is associated with the following publication:\nLytle, D., C. Formal, E. Dore, C. Muhlen, S. Harmon, D. Williams, S. Triantafyllidou, and M. Pham. SYNTHESIS AND CHARACTERIZATION OF STABLE LEAD (II) ORTHOPHOSPHATE NANOPARTICLE SUSPENSIONS.   JOURNAL OF ENVIRONMENTAL SCIENCE AND HEALTH, PART A. Marcel Dekker Incorporated, New York, NY, USA, 55(13): 1504-1512, (2020).",
             "distribution": [
                 {
-                    "title": "StableNanoparticleData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518478/StableNanoparticleData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StableNanoparticleData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518478",
+            "keyword": [
+                "lead",
+                "Orthophosphate",
+                "Nanoparticle",
+                "drinking water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-12-14",
-            "references": [
-                "https://doi.org/10.1080/10934529.2020.1810498"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136515,19 +136509,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10934529.2020.1810498"
+            ],
+            "rights": null,
+            "title": "Data used in tables or figure."
         },
         {
-            "title": "The environmental impacts and life cycle cost of co-digestion energy recovery from food waste in medium scale wastewater treatment facility",
-            "description": "The dataset includes the LCA, LCIA, LCC, sensitivity analysis for the wastewater treatment expansion for co-digestion with food waste. \n\nThis dataset is associated with the following publication:\nMorelli, B., S. Cashman, X. Ma, J. Turgeon, S. Arden, and J. Garland. Environmental and Cost Benefits of Co-Digesting Food Waste at Wastewater Treatment Plants.   WATER SCIENCE AND TECHNOLOGY. IWA Publishing, London,  UK, 82(2): 227-241, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Xin Ma",
+                "hasEmail": "mailto:ma.cissy@epa.gov"
+            },
+            "description": "The dataset includes the LCA, LCIA, LCC, sensitivity analysis for the wastewater treatment expansion for co-digestion with food waste. \n\nThis dataset is associated with the following publication:\nMorelli, B., S. Cashman, X. Ma, J. Turgeon, S. Arden, and J. Garland. Environmental and Cost Benefits of Co-Digesting Food Waste at Wastewater Treatment Plants.   WATER SCIENCE AND TECHNOLOGY. IWA Publishing, London,  UK, 82(2): 227-241, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503070/MA%20Case%20Study%20LCIA%20Results.final.5.30.19_macro-free.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MA Case Study LCIA Results.final.5.30.19_macro-free.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503070",
             "keyword": [
@@ -136539,20 +136543,10 @@
                 "LCC",
                 "biogas"
             ],
-            "contactPoint": {
-                "fn": "Xin Ma",
-                "hasEmail": "mailto:ma.cissy@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MA Case Study LCIA Results.final.5.30.19_macro-free.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503070/MA%20Case%20Study%20LCIA%20Results.final.5.30.19_macro-free.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-30",
-            "references": [
-                "https://doi.org/10.2166/wst.2020.104"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136562,19 +136556,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2166/wst.2020.104"
+            ],
+            "rights": null,
+            "title": "The environmental impacts and life cycle cost of co-digestion energy recovery from food waste in medium scale wastewater treatment facility"
         },
         {
-            "title": "Dataset for Evaluation of Drinking Water Treatment and Monitoring Technologies to Improve Public Health in Non-PRASA Communities in Puerto Rico",
-            "description": "Project pathogen results and water quality monitoring data ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Craig Patterson",
+                "hasEmail": "mailto:patterson.craig@epa.gov"
+            },
+            "description": "Project pathogen results and water quality monitoring data ",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521085/R2RAREReportDataSetScienceHub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "R2RAREReportDataSetScienceHub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1521085",
             "keyword": [
@@ -136587,19 +136591,11 @@
                 "turbidity sonde",
                 "disinfectant sonde"
             ],
-            "contactPoint": {
-                "fn": "Craig Patterson",
-                "hasEmail": "mailto:patterson.craig@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "R2RAREReportDataSetScienceHub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521085/R2RAREReportDataSetScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-10",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -136608,49 +136604,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Dataset for Evaluation of Drinking Water Treatment and Monitoring Technologies to Improve Public Health in Non-PRASA Communities in Puerto Rico"
         },
         {
-            "title": "Raw Data for Mechanistic Toxicity Tests Based on an Adverse Outcome Pathway Network for Hepatic Steatosis",
-            "description": "Supplementary Files 1-15 contain the generated assay data that was used to establish BMAD and determine treatment effects. The tabbed spreadsheet data is formatted so that it can be directly analyzed, once converted to individual comma-separated values (.csv) files, using the R code provided in Supplementary File 16. Column headings are described in the supplemental file 'Metadata Glossary.docx'. \n\nThis dataset is associated with the following publication:\nAngrish, M., C. McQueen, E. Hubal, M. Bruno, Y. Ge, and B. Chorley. Mechanistic Toxicity Tests Based on an Adverse Outcome Pathway Network for Hepatic Steatosis.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  159(1): 159-169, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1376696",
-            "keyword": [
-                "adverse outcome pathway",
-                "chemical risk assessment",
-                "high-throughput toxicity testing",
-                "mechanistic toxicology",
-                "non-alcoholic fatty liver disease",
-                "hepatic steatosis"
-            ],
             "contactPoint": {
                 "fn": "Brian Chorley",
                 "hasEmail": "mailto:chorley.brian@epa.gov"
             },
+            "description": "Supplementary Files 1-15 contain the generated assay data that was used to establish BMAD and determine treatment effects. The tabbed spreadsheet data is formatted so that it can be directly analyzed, once converted to individual comma-separated values (.csv) files, using the R code provided in Supplementary File 16. Column headings are described in the supplemental file 'Metadata Glossary.docx'. \n\nThis dataset is associated with the following publication:\nAngrish, M., C. McQueen, E. Hubal, M. Bruno, Y. Ge, and B. Chorley. Mechanistic Toxicity Tests Based on an Adverse Outcome Pathway Network for Hepatic Steatosis.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  159(1): 159-169, (2017).",
             "distribution": [
                 {
-                    "title": "Supporting_files_1-15.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1376696/Supporting_files_1-15.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supporting_files_1-15.xlsx"
                 },
                 {
-                    "title": "Supp File 16.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1376696/Supp%20File%2016.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Supp File 16.txt"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1376696",
+            "keyword": [
+                "adverse outcome pathway",
+                "chemical risk assessment",
+                "high-throughput toxicity testing",
+                "mechanistic toxicology",
+                "non-alcoholic fatty liver disease",
+                "hepatic steatosis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-24",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfx121",
-                "https://pasteur.epa.gov/uploads/10.23719/1376696/documents/Metadata%20Glossary.docx"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136660,19 +136653,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfx121",
+                "https://pasteur.epa.gov/uploads/10.23719/1376696/documents/Metadata%20Glossary.docx"
+            ],
+            "rights": null,
+            "title": "Raw Data for Mechanistic Toxicity Tests Based on an Adverse Outcome Pathway Network for Hepatic Steatosis"
         },
         {
-            "title": "The Effects of Combinations of Limited Ration and Diazinon Exposure on Acetylcholinesterase Activity, Growth, and Reproduction in Oryzias latipes, the Japanese medaka ",
-            "description": "Environmental contamination can negatively impact fish populations. In addition to acute toxicity leading to death, toxicants can reduce fish growth and lower reproduction. The potential for adverse population level effects of environmental contaminants are estimated from laboratory toxicity tests that most often measure apical endpoints related to growth, survival, and reproduction. The relationships between these endpoints are being evaluated to better predict shifts in fish population demography after exposure to environmental toxicants. Environmental contaminants can also affect fish populations indirectly by reducing prey biomass. However, estimating the combined effects of prey reduction and direct toxicity is difficult and rarely attempted. Here we describe a toxicity test designed to estimate the effect on Japanese medaka of both reduced food and chronic exposure to diazinon, an acetylcholinesterase inhibiting organophosphate pesticide. Fish were reared with limited food ration and/or diazinon exposure through a full life-cycle to assess possible interactions between the two stressors in their effects on growth and reproduction. Diazinon exposure, reduced ration, or combinations of both lowered growth rates and reproductive output of Japanese medaka. Various relationships between the two stressors (diazinon and ration) and growth and reproduction were modeled. These results inform fish models being developed by EPA to predict population consequences of chemical exposures. \n\nThis dataset is associated with the following publication:\nFlynn, K., J. Swintek, F. Whiteman, and M. Etterson. The effects of combinations of limited ration and diazinon exposure on acetylcholinesterase activity, growth, and reproduction in Oryzias latipes, the Japanese medaka.   JOURNAL OF APPLIED TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 40(4): 535-547, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Kevin Flynn",
+                "hasEmail": "mailto:flynn.kevin@epa.gov"
+            },
+            "description": "Environmental contamination can negatively impact fish populations. In addition to acute toxicity leading to death, toxicants can reduce fish growth and lower reproduction. The potential for adverse population level effects of environmental contaminants are estimated from laboratory toxicity tests that most often measure apical endpoints related to growth, survival, and reproduction. The relationships between these endpoints are being evaluated to better predict shifts in fish population demography after exposure to environmental toxicants. Environmental contaminants can also affect fish populations indirectly by reducing prey biomass. However, estimating the combined effects of prey reduction and direct toxicity is difficult and rarely attempted. Here we describe a toxicity test designed to estimate the effect on Japanese medaka of both reduced food and chronic exposure to diazinon, an acetylcholinesterase inhibiting organophosphate pesticide. Fish were reared with limited food ration and/or diazinon exposure through a full life-cycle to assess possible interactions between the two stressors in their effects on growth and reproduction. Diazinon exposure, reduced ration, or combinations of both lowered growth rates and reproductive output of Japanese medaka. Various relationships between the two stressors (diazinon and ration) and growth and reproduction were modeled. These results inform fish models being developed by EPA to predict population consequences of chemical exposures. \n\nThis dataset is associated with the following publication:\nFlynn, K., J. Swintek, F. Whiteman, and M. Etterson. The effects of combinations of limited ration and diazinon exposure on acetylcholinesterase activity, growth, and reproduction in Oryzias latipes, the Japanese medaka.   JOURNAL OF APPLIED TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 40(4): 535-547, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504073/ORD-031626%20Diazinon%20Ration%20Science%20Hub%20Data%20File.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ORD-031626 Diazinon Ration Science Hub Data File.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504073",
             "keyword": [
@@ -136683,20 +136687,10 @@
                 "aquatic toxicity",
                 "pesticides"
             ],
-            "contactPoint": {
-                "fn": "Kevin Flynn",
-                "hasEmail": "mailto:flynn.kevin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ORD-031626 Diazinon Ration Science Hub Data File.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504073/ORD-031626%20Diazinon%20Ration%20Science%20Hub%20Data%20File.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-11",
-            "references": [
-                "https://doi.org/10.1002/jat.3925"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136706,40 +136700,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/jat.3925"
+            ],
+            "rights": null,
+            "title": "The Effects of Combinations of Limited Ration and Diazinon Exposure on Acetylcholinesterase Activity, Growth, and Reproduction in Oryzias latipes, the Japanese medaka "
         },
         {
-            "title": "EE2_FHM_larva_RNASeq_20210309a_GSE160535",
-            "description": "The data are maintained at the National Center for Biotechnology Information (NCBI) GEO depository https://www.ncbi.nlm.nih.gov/geo/ .  There are three accession numbers (which can be entered at this site):\n\u2022\tGSE160535 - Development of omic biomarkers for Fathead minnow larva (Pimephales promelas) exposed to ethinyl estradiol\n   A superseries which links to the two separate data sets from the same experiment (below)\n\u2022\tGSE158857 - Development of omic biomarkers for Fathead minnow larva (Pimephales promelas) exposed to ethinyl estradiol [non-coding small RNA]\n   The non-coding small RNA dataset (includes microRNA and PIWI-RNA data and metadata\n\u2022\tGSE160520 - Development of omic biomarkers for Fathead minnow larva (Pimephales promelas) exposed to ethinyl estradiol [mRNA]\n   The mRNA data set including metadata. \n\nThis dataset is associated with the following publication:\nToth, G., J. Martinson, D. Bencic, D. Lattier, M. Kostich, and A. Biales. Development of omcis biomarkers for estrogen exposure using mRNA, miRNA and piRNAs.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 235: 105807, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520955",
-            "keyword": [
-                "estrogen",
-                "transcriptome",
-                "fathead minnow",
-                "non-coding RNA"
-            ],
             "contactPoint": {
                 "fn": "Gregory Toth",
                 "hasEmail": "mailto:toth.greg@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520955/documents/EE2_FHM_larva_RNASeq_20210309a_GSE160535_DDict.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The data are maintained at the National Center for Biotechnology Information (NCBI) GEO depository https://www.ncbi.nlm.nih.gov/geo/ .  There are three accession numbers (which can be entered at this site):\n\u2022\tGSE160535 - Development of omic biomarkers for Fathead minnow larva (Pimephales promelas) exposed to ethinyl estradiol\n   A superseries which links to the two separate data sets from the same experiment (below)\n\u2022\tGSE158857 - Development of omic biomarkers for Fathead minnow larva (Pimephales promelas) exposed to ethinyl estradiol [non-coding small RNA]\n   The non-coding small RNA dataset (includes microRNA and PIWI-RNA data and metadata\n\u2022\tGSE160520 - Development of omic biomarkers for Fathead minnow larva (Pimephales promelas) exposed to ethinyl estradiol [mRNA]\n   The mRNA data set including metadata. \n\nThis dataset is associated with the following publication:\nToth, G., J. Martinson, D. Bencic, D. Lattier, M. Kostich, and A. Biales. Development of omcis biomarkers for estrogen exposure using mRNA, miRNA and piRNAs.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 235: 105807, (2021).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520955",
+            "keyword": [
+                "estrogen",
+                "transcriptome",
+                "fathead minnow",
+                "non-coding RNA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-12-11",
-            "references": [
-                "https://doi.org/10.1016/j.aquatox.2021.105807"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136750,20 +136746,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520955/documents/EE2_FHM_larva_RNASeq_20210309a_GSE160535_DDict.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.aquatox.2021.105807"
+            ],
+            "rights": null,
+            "title": "EE2_FHM_larva_RNASeq_20210309a_GSE160535"
         },
         {
-            "title": "HepRG exposed to microcystin LR and RR gene expression",
-            "description": "RNA-seq data from HepaRG cells exposed for 2 hours to microcystin-LR and -RR at multiple concentrations each. \n\nThis dataset is associated with the following publication:\nBiales, A., D. Bencic, R. Flick, A. Delacruz, D. Gordon, and W. Huang. Global transcriptomic profiling of microcystin-LR or -RR treated hepatocytes (HepaRG)..   Toxicon: X. Elsevier B.V., Amsterdam,  NETHERLANDS, 8: 100060, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Adam Biales",
+                "hasEmail": "mailto:biales.adam@epa.gov"
+            },
+            "description": "RNA-seq data from HepaRG cells exposed for 2 hours to microcystin-LR and -RR at multiple concentrations each. \n\nThis dataset is associated with the following publication:\nBiales, A., D. Bencic, R. Flick, A. Delacruz, D. Gordon, and W. Huang. Global transcriptomic profiling of microcystin-LR or -RR treated hepatocytes (HepaRG)..   Toxicon: X. Elsevier B.V., Amsterdam,  NETHERLANDS, 8: 100060, (2020).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147999.",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147999."
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520947",
             "keyword": [
@@ -136773,19 +136776,10 @@
                 "gene expression",
                 "hepatocytes"
             ],
-            "contactPoint": {
-                "fn": "Adam Biales",
-                "hasEmail": "mailto:biales.adam@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147999.",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147999."
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-15",
-            "references": [
-                "https://doi.org/10.1016/j.toxcx.2020.100060"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136795,40 +136789,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.toxcx.2020.100060"
+            ],
+            "rights": null,
+            "title": "HepRG exposed to microcystin LR and RR gene expression"
         },
         {
-            "title": "An examination of national cancer risk based on monitored hazardous ambient air pollutants",
-            "description": "An examination of national cancer risk based on monitored hazardous ambient air pollutants. \n\nThis dataset is associated with the following publication:\nWeitekamp, C., M. Lein, M. Strum, M. Morris, T. Palma, D. Smith, L. Kerr, and M. Stewart. An Examination of National Cancer Risk Based on Monitored Hazardous Air Pollutants.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 129(3): 1-12, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1517803",
-            "keyword": [
-                "air toxics",
-                "cancer risk",
-                "hazardous air pollutants"
-            ],
             "contactPoint": {
                 "fn": "Michael Stewart",
                 "hasEmail": "mailto:stewart.michael@epa.gov"
             },
+            "description": "An examination of national cancer risk based on monitored hazardous ambient air pollutants. \n\nThis dataset is associated with the following publication:\nWeitekamp, C., M. Lein, M. Strum, M. Morris, T. Palma, D. Smith, L. Kerr, and M. Stewart. An Examination of National Cancer Risk Based on Monitored Hazardous Air Pollutants.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 129(3): 1-12, (2021).",
             "distribution": [
                 {
-                    "title": "data_Ajwtg_20210310.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517803/data_Ajwtg_20210310.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "data_Ajwtg_20210310.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517803",
+            "keyword": [
+                "air toxics",
+                "cancer risk",
+                "hazardous air pollutants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-02-14",
-            "references": [
-                "https://doi.org/10.1289/ehp8044"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -136838,53 +136832,55 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp8044"
+            ],
+            "rights": null,
+            "title": "An examination of national cancer risk based on monitored hazardous ambient air pollutants"
         },
         {
-            "title": "colloid-size copper-based pesticides and wood preservatives against microbial activities of Gram-positive Bacillus species ",
-            "description": "Copper-based pesticides and wood preservative fungicides could end up in the environment during production, use, and end-of-life via different pathways that could cause unintended ecological and adverse health effects. This paper provides the effect of colloid-size Cu-based pesticides, micronized Cu azole and alkaline Cu quaternary (ACQ) treated woods, ionic Cu, ionic Cu spiked untreated wood (UTW), and CuCO3 solutions against Gram-positive Bacillus species using five-day biochemical oxygen demand  standard test. \n\nThis dataset is associated with the following publication:\nTegenaw, A., G.A. Sorial , and E. Sahle-Demessie. Effect of colloid-size copper-based pesticides and wood preservatives against microbial activities of Gram-positive Bacillus species using five-day biochemical oxygen demand test.   Journal of Environmental Sciences. Elsevier BV, AMSTERDAM,  NETHERLANDS, 105: 71-80, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520885",
-            "keyword": [
-                "Bacillus species",
-                "BOD5",
-                "Colloid-size Cu-based pesticides",
-                "Leaching",
-                "Wood preservatives"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520885/documents/Data%20Dictionary_Copper_Nanopesticide.pdf",
+            "describedByType": "application/pdf",
+            "description": "Copper-based pesticides and wood preservative fungicides could end up in the environment during production, use, and end-of-life via different pathways that could cause unintended ecological and adverse health effects. This paper provides the effect of colloid-size Cu-based pesticides, micronized Cu azole and alkaline Cu quaternary (ACQ) treated woods, ionic Cu, ionic Cu spiked untreated wood (UTW), and CuCO3 solutions against Gram-positive Bacillus species using five-day biochemical oxygen demand  standard test. \n\nThis dataset is associated with the following publication:\nTegenaw, A., G.A. Sorial , and E. Sahle-Demessie. Effect of colloid-size copper-based pesticides and wood preservatives against microbial activities of Gram-positive Bacillus species using five-day biochemical oxygen demand test.   Journal of Environmental Sciences. Elsevier BV, AMSTERDAM,  NETHERLANDS, 105: 71-80, (2021).",
             "distribution": [
                 {
-                    "title": "Ayu_Cu-NPs_Supplemental Data_Journal of Environmental Management.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520885/Ayu_Cu-NPs_Supplemental%20Data_Journal%20of%20Environmental%20Management.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Ayu_Cu-NPs_Supplemental Data_Journal of Environmental Management.docx"
                 },
                 {
-                    "title": "Ayu_Paper_Figure_file.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520885/Ayu_Paper_Figure_file.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Ayu_Paper_Figure_file.docx"
                 },
                 {
-                    "title": "Ayu_Manuscript_Journal of Environmental Management GS and Sahle Demmessie edits (003).docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520885/Ayu_Manuscript_Journal%20of%20Environmental%20Management%20GS%20and%20Sahle%20Demmessie%20edits%20%28003%29.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Ayu_Manuscript_Journal of Environmental Management GS and Sahle Demmessie edits (003).docx"
                 }
             ],
-            "modified": "2020-05-20",
-            "references": [
-                "https://doi.org/10.1016/j.jes.2020.12.037"
-            ],
+            "identifier": "https://doi.org/10.23719/1520885",
+            "keyword": [
+                "Bacillus species",
+                "BOD5",
+                "Colloid-size Cu-based pesticides",
+                "Leaching",
+                "Wood preservatives"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
+            "modified": "2020-05-20",
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -136894,20 +136890,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520885/documents/Data%20Dictionary_Copper_Nanopesticide.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1016/j.jes.2020.12.037"
+            ],
+            "rights": null,
+            "title": "colloid-size copper-based pesticides and wood preservatives against microbial activities of Gram-positive Bacillus species "
         },
         {
-            "title": "NLA_52_lakes_all_TP_data",
-            "description": "Total Phosphorus composite monitoring data set for 52 lakes. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "James Carleton",
+                "hasEmail": "mailto:carleton.jim@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1518517/documents/metadata%20for%20NLA_52_lakes_all_TP_data.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Total Phosphorus composite monitoring data set for 52 lakes. ",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518517/NLA_52_lakes_all_TP_data.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NLA_52_lakes_all_TP_data.csv"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518517",
             "keyword": [
@@ -136918,19 +136924,11 @@
                 "trend",
                 "recovery"
             ],
-            "contactPoint": {
-                "fn": "James Carleton",
-                "hasEmail": "mailto:carleton.jim@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "NLA_52_lakes_all_TP_data.csv",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518517/NLA_52_lakes_all_TP_data.csv",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-09",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -136940,20 +136938,25 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1518517/documents/metadata%20for%20NLA_52_lakes_all_TP_data.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": null,
+            "rights": null,
+            "title": "NLA_52_lakes_all_TP_data"
         },
         {
-            "title": "Time lags in watershed nitrogen and phosphorus input-output balances:  A forty-four year record of the Willamette River Basin  ",
-            "description": "The following 4 tables accompany the peer-reviewed journal article GS Metson, J Lin, JE Compton, JA Harrison. \"Where have all the nutrients gone? Long-term Decoupling of Inputs and Outputs in the Willamette River Watershed, Oregon, USA\". Published in JGR Biogeoscience.  \nValues refer to the Willamette River Watershed, which was defined as the area draining to USGS gauge 14211720 (which is 29 018 km2 when delimiting using HydroSHEDs 15 arc-second flow direction maps (Lehner et al 2006)). These datasets were created May 2017. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Jana Compton",
+                "hasEmail": "mailto:compton.jana@epa.gov"
+            },
+            "description": "The following 4 tables accompany the peer-reviewed journal article GS Metson, J Lin, JE Compton, JA Harrison. \"Where have all the nutrients gone? Long-term Decoupling of Inputs and Outputs in the Willamette River Watershed, Oregon, USA\". Published in JGR Biogeoscience.  \nValues refer to the Willamette River Watershed, which was defined as the area draining to USGS gauge 14211720 (which is 29 018 km2 when delimiting using HydroSHEDs 15 arc-second flow direction maps (Lehner et al 2006)). These datasets were created May 2017. ",
+            "distribution": [
+                {
+                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1519181",
+                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1519181"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504006",
             "keyword": [
@@ -136963,18 +136966,11 @@
                 "water quality",
                 "legacies"
             ],
-            "contactPoint": {
-                "fn": "Jana Compton",
-                "hasEmail": "mailto:compton.jana@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1519181",
-                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1519181"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-04-07",
-            "references": null,
+            "programCode": [
+                "020:097"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -136983,46 +136979,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Time lags in watershed nitrogen and phosphorus input-output balances:  A forty-four year record of the Willamette River Basin  "
         },
         {
-            "title": "Fish Quality Index",
-            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data. \n\nThis dataset is associated with the following publication:\nLomnicky, G.A., R.M. Hughes, D. Peck, and P. Ringold. Correspondence between a recreational fishery index and ecological condition for U.S.A. streams and rivers.   Fisheries Research. Elsevier Science Ltd, New York, NY, USA, 223: 105749, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1517662",
-            "keyword": [
-                "assessment",
-                "aquatic monitoring",
-                "coastal",
-                "rivers and streams",
-                "lakes and reservoirs",
-                "wetlands"
-            ],
             "contactPoint": {
                 "fn": "Steven Paulsen",
                 "hasEmail": "mailto:paulsen.steve@epa.gov"
             },
+            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data. \n\nThis dataset is associated with the following publication:\nLomnicky, G.A., R.M. Hughes, D. Peck, and P. Ringold. Correspondence between a recreational fishery index and ecological condition for U.S.A. streams and rivers.   Fisheries Research. Elsevier Science Ltd, New York, NY, USA, 223: 105749, (2021).",
             "distribution": [
                 {
-                    "title": "https://fisheries.org/bookstore/all-titles/special-publications/51035p/",
-                    "accessURL": "https://fisheries.org/bookstore/all-titles/special-publications/51035p/"
+                    "accessURL": "https://fisheries.org/bookstore/all-titles/special-publications/51035p/",
+                    "title": "https://fisheries.org/bookstore/all-titles/special-publications/51035p/"
                 },
                 {
-                    "title": "https://doi.org/10.23719/1407622",
-                    "accessURL": "https://doi.org/10.23719/1407622"
+                    "accessURL": "https://doi.org/10.23719/1407622",
+                    "title": "https://doi.org/10.23719/1407622"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517662",
+            "keyword": [
+                "assessment",
+                "aquatic monitoring",
+                "coastal",
+                "rivers and streams",
+                "lakes and reservoirs",
+                "wetlands"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-01",
-            "references": [
-                "https://doi.org/10.1016/j.fishres.2020.105749"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137032,53 +137026,55 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.fishres.2020.105749"
+            ],
+            "rights": null,
+            "title": "Fish Quality Index"
         },
         {
-            "title": "Priest River Habitat and Regional Context",
-            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519029",
-            "keyword": [
-                "assessment",
-                "aquatic monitoring",
-                "coastal",
-                "rivers and streams",
-                "lakes and reservoirs",
-                "wetlands"
-            ],
             "contactPoint": {
                 "fn": "Steven Paulsen",
                 "hasEmail": "mailto:paulsen.steve@epa.gov"
             },
+            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data.",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.23719/1407622",
-                    "accessURL": "https://doi.org/10.23719/1407622"
+                    "accessURL": "https://doi.org/10.23719/1407622",
+                    "title": "https://doi.org/10.23719/1407622"
                 },
                 {
-                    "title": "https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products",
-                    "accessURL": "https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products"
+                    "accessURL": "https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products",
+                    "title": "https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products"
                 },
                 {
-                    "title": "https://www.fs.fed.us/rm/boise/AWAE/projects/NorWeST.html",
-                    "accessURL": "https://www.fs.fed.us/rm/boise/AWAE/projects/NorWeST.html"
+                    "accessURL": "https://www.fs.fed.us/rm/boise/AWAE/projects/NorWeST.html",
+                    "title": "https://www.fs.fed.us/rm/boise/AWAE/projects/NorWeST.html"
                 },
                 {
-                    "title": "https://www.sciencebase.gov/catalog/item/508eccefe4b0b59cf7f5a7f8",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/508eccefe4b0b59cf7f5a7f8"
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/508eccefe4b0b59cf7f5a7f8",
+                    "title": "https://www.sciencebase.gov/catalog/item/508eccefe4b0b59cf7f5a7f8"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519029",
+            "keyword": [
+                "assessment",
+                "aquatic monitoring",
+                "coastal",
+                "rivers and streams",
+                "lakes and reservoirs",
+                "wetlands"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-01",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137087,47 +137083,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Priest River Habitat and Regional Context"
         },
         {
-            "title": "EMAP-Western Pilot Study Fish Sampling Effort",
-            "description": "Fish count data collected from 300-channel width reaches of Western USA rivers as part of the EMAP-Western Pilot Study.  \n\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519063",
-            "keyword": [
-                "assessment",
-                "aquatic monitoring",
-                "coastal",
-                "rivers and streams",
-                "lakes and reservoirs",
-                "wetlands"
-            ],
             "contactPoint": {
                 "fn": "Steven Paulsen",
                 "hasEmail": "mailto:paulsen.steve@epa.gov"
             },
+            "description": "Fish count data collected from 300-channel width reaches of Western USA rivers as part of the EMAP-Western Pilot Study.  \n\n",
             "distribution": [
                 {
-                    "title": "vertcnt_300cw_metadata.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519063/vertcnt_300cw_metadata.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "vertcnt_300cw_metadata.txt"
                 },
                 {
-                    "title": "vertcnt_300cw.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519063/vertcnt_300cw.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "vertcnt_300cw.txt"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519063",
+            "keyword": [
+                "assessment",
+                "aquatic monitoring",
+                "coastal",
+                "rivers and streams",
+                "lakes and reservoirs",
+                "wetlands"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-07-13",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137136,19 +137132,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "EMAP-Western Pilot Study Fish Sampling Effort"
         },
         {
-            "title": "Drivers of spatial variation in stream nitrogen concentrations across the US",
-            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Steven Paulsen",
+                "hasEmail": "mailto:paulsen.steve@epa.gov"
+            },
+            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data.",
+            "distribution": [
+                {
+                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622",
+                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1519428",
             "keyword": [
@@ -137159,18 +137162,11 @@
                 "lakes and reservoirs",
                 "wetlands"
             ],
-            "contactPoint": {
-                "fn": "Steven Paulsen",
-                "hasEmail": "mailto:paulsen.steve@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622",
-                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-01",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137179,19 +137175,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Drivers of spatial variation in stream nitrogen concentrations across the US"
         },
         {
-            "title": "Quantitative Assessment of Stream and River Physical Habitat Condition",
-            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Steven Paulsen",
+                "hasEmail": "mailto:paulsen.steve@epa.gov"
+            },
+            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data.",
+            "distribution": [
+                {
+                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622",
+                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520619",
             "keyword": [
@@ -137202,18 +137205,11 @@
                 "lakes and reservoirs",
                 "wetlands"
             ],
-            "contactPoint": {
-                "fn": "Steven Paulsen",
-                "hasEmail": "mailto:paulsen.steve@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622",
-                    "accessURL": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=https://doi.org/10.23719/1407622"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-01",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137222,19 +137218,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Quantitative Assessment of Stream and River Physical Habitat Condition"
         },
         {
-            "title": "Effects of shading and composition on green roof media temperature and moisture data set",
-            "description": "Three of the primary functions of green roofs in urban areas are to delay rainwater runoff, moderate building temperatures, and ameliorate the urban heat island (UHI) effect. A major impediment to the survival of plants on an unirrigated extensive green roof (EGR) is the harsh rooftop environment, including high temperatures and limited water during dry periods. Factors that influence EGR thermal and hydrologic performance include the albedo (reflectivity) of the roof and the composition of the green roof substrate (growing media). In this study we used white, reflective shading structures and three different media formulations to evaluate EGR thermal and hydrologic performance in the Pacific Northwest, USA. Shading significantly reduced daytime mean and maximum EGR media temperatures and significantly increased nighttime mean and minimum temperatures, which may provide energy benefits to buildings. Mean media moisture was greater in shaded trays than in exposed (unshaded) trays but differences were not statistically significant. Warmer nighttime media temperatures and lack of dew formation in shaded trays may have partially compensated for greater daytime evaporation from exposed trays. Media composition did not significantly influence media temperature or moisture. Results of this study suggest that adding shade structures to green roofs will combine thermal, hydrologic, and ecological benefits, and help achieve temperature and light regimes that allow for greater plant diversity on EGRs. \n\nThis dataset is associated with the following publication:\nBollman, M., G. DeSantis, R. Waschmann, and P. Mayer. Effects of shading and composition on green roof media temperature and moisture.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 281: 111882, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Michael Bollman",
+                "hasEmail": "mailto:bollman.mike@epa.gov"
+            },
+            "description": "Three of the primary functions of green roofs in urban areas are to delay rainwater runoff, moderate building temperatures, and ameliorate the urban heat island (UHI) effect. A major impediment to the survival of plants on an unirrigated extensive green roof (EGR) is the harsh rooftop environment, including high temperatures and limited water during dry periods. Factors that influence EGR thermal and hydrologic performance include the albedo (reflectivity) of the roof and the composition of the green roof substrate (growing media). In this study we used white, reflective shading structures and three different media formulations to evaluate EGR thermal and hydrologic performance in the Pacific Northwest, USA. Shading significantly reduced daytime mean and maximum EGR media temperatures and significantly increased nighttime mean and minimum temperatures, which may provide energy benefits to buildings. Mean media moisture was greater in shaded trays than in exposed (unshaded) trays but differences were not statistically significant. Warmer nighttime media temperatures and lack of dew formation in shaded trays may have partially compensated for greater daytime evaporation from exposed trays. Media composition did not significantly influence media temperature or moisture. Results of this study suggest that adding shade structures to green roofs will combine thermal, hydrologic, and ecological benefits, and help achieve temperature and light regimes that allow for greater plant diversity on EGRs. \n\nThis dataset is associated with the following publication:\nBollman, M., G. DeSantis, R. Waschmann, and P. Mayer. Effects of shading and composition on green roof media temperature and moisture.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 281: 111882, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520657/Effects%20of%20shading%20and%20composition%20on%20green%20roof%20media%20temperature%20and%20moisture_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Effects of shading and composition on green roof media temperature and moisture_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520657",
             "keyword": [
@@ -137246,20 +137250,10 @@
                 "stormwater management",
                 "green roof design"
             ],
-            "contactPoint": {
-                "fn": "Michael Bollman",
-                "hasEmail": "mailto:bollman.mike@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Effects of shading and composition on green roof media temperature and moisture_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520657/Effects%20of%20shading%20and%20composition%20on%20green%20roof%20media%20temperature%20and%20moisture_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-05",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2020.111882"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137269,55 +137263,57 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2020.111882"
+            ],
+            "rights": null,
+            "title": "Effects of shading and composition on green roof media temperature and moisture data set"
         },
         {
-            "title": "Projecting changes in extreme rainfall from three tropical cyclones using the design-rainfall approach",
-            "description": "The baseline data used for analysis is stored on ORD serves as 2,736 netcdf files ~1.8 Terabyte in size and is not suitable as an attachment in ScienceHub. \nWe provide final Figures and tables used in the manuscript and supplemental materials. Portions of this dataset are inaccessible because: 2,736 netcdf files ~1.8 Terabyte in size. They can be accessed through the following means: upon request to the corresponding author. Format: The baseline data used for analysis contains 2,736 netcdf stored on ORD serves,  ~1.8 Terabyte in size and is not suitable as an attachment in ScienceHub. \n\nThis dataset is associated with the following publication:\nJalowska, A., T. Spero, and J. Bowden. Projecting changes in extreme rainfall from three tropical cyclones using the design-rainfall approach.   Nature Climate Change. Nature Publishing Group, New York, NY, USA, 4(23): 1-8, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519135",
-            "keyword": [
-                "IDF curves",
-                "future projections",
-                "tropical cyclones",
-                "WRF",
-                "GCM",
-                "RCM",
-                "extreme rainfall",
-                "Storm Water Managemnet"
-            ],
             "contactPoint": {
                 "fn": "Tanya Spero",
                 "hasEmail": "mailto:spero.tanya@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519135/documents/data%20dictionary.txt",
+            "describedByType": "text/plain",
+            "description": "The baseline data used for analysis is stored on ORD serves as 2,736 netcdf files ~1.8 Terabyte in size and is not suitable as an attachment in ScienceHub. \nWe provide final Figures and tables used in the manuscript and supplemental materials. Portions of this dataset are inaccessible because: 2,736 netcdf files ~1.8 Terabyte in size. They can be accessed through the following means: upon request to the corresponding author. Format: The baseline data used for analysis contains 2,736 netcdf stored on ORD serves,  ~1.8 Terabyte in size and is not suitable as an attachment in ScienceHub. \n\nThis dataset is associated with the following publication:\nJalowska, A., T. Spero, and J. Bowden. Projecting changes in extreme rainfall from three tropical cyclones using the design-rainfall approach.   Nature Climate Change. Nature Publishing Group, New York, NY, USA, 4(23): 1-8, (2021).",
             "distribution": [
                 {
-                    "title": "Figure 3 data2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519135/Figure%203%20data2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure 3 data2.csv"
                 },
                 {
-                    "title": "Figure 4 data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519135/Figure%204%20data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure 4 data.csv"
                 },
                 {
-                    "title": "Figure 3 data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519135/Figure%203%20data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure 3 data.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519135",
+            "keyword": [
+                "IDF curves",
+                "future projections",
+                "tropical cyclones",
+                "WRF",
+                "GCM",
+                "RCM",
+                "extreme rainfall",
+                "Storm Water Managemnet"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-23",
-            "references": [
-                "https://doi.org/10.1038/s41612-021-00176-9"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137328,41 +137324,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519135/documents/data%20dictionary.txt",
-            "describedByType": "text/plain"
+            "references": [
+                "https://doi.org/10.1038/s41612-021-00176-9"
+            ],
+            "rights": null,
+            "title": "Projecting changes in extreme rainfall from three tropical cyclones using the design-rainfall approach"
         },
         {
-            "title": "Figures and Tables Gilliam et al. 2020. Final",
-            "description": "This is a zip file with all data that were used to generate the figures and tables. The zip file contains a separate zip file for each figures/table. Those files have README metadata files that describe the figure/table datasets.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1519128",
-            "keyword": [
-                "air quality",
-                "global modeling",
-                "land-surface",
-                "meteorology modeling"
-            ],
             "contactPoint": {
                 "fn": "Robert Gilliam",
                 "hasEmail": "mailto:gilliam.robert@epa.gov"
             },
+            "description": "This is a zip file with all data that were used to generate the figures and tables. The zip file contains a separate zip file for each figures/table. Those files have README metadata files that describe the figure/table datasets.",
             "distribution": [
                 {
-                    "title": "data.gilliam.A-63z5.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519128/data.gilliam.A-63z5.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "data.gilliam.A-63z5.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519128",
+            "keyword": [
+                "air quality",
+                "global modeling",
+                "land-surface",
+                "meteorology modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-22",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137371,19 +137367,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Figures and Tables Gilliam et al. 2020. Final"
         },
         {
-            "title": "Wildland Fire Emission Sampling at Fishlake National Forest, Utah Using an Unmanned Aircraft System",
-            "description": "Emissions from a stand replacement prescribed burn were sampled using an unmanned aircraft system (UAS, or \u201cdrone\u201d) in Fishlake National Forest, Utah, U.S.A. Sixteen flights over three days in June 2019 provided emission factors for a broad range of compounds including carbon monoxide (CO), carbon dioxide (CO2), nitric oxide (NO), nitrogen oxide (NO2), particulate matter < 2.5 microns in diameter (PM2.5), volatile organic compounds (VOCs) including carbonyls, black carbon, and elemental/organic carbon. To our knowledge, this is the first UAS-based emission sampling for a fire of this magnitude, including both slash pile and crown fires resulting in wildfire-like conditions. The burns consisted of drip torch ignitions as well as ground-mobile and aerial helicopter ignitions of large stands comprising over 1,000 ha, allowing for comparison of same-species emission factors burned under different conditions. The use of a UAS for emission sampling minimizes risk to personnel and equipment, allowing flexibility in sampling location and ensuring capture of representative, fresh smoke constituents. PM2.5 emission factors varied 5-fold and, like most pollutants, varied inversely with combustion efficiency resulting in lower emission factors from the slash piles than the crown fires. \n\nThis dataset is associated with the following publication:\nAurell, J., B. Gullett, A. Holder, F. Kiros, B. Mitchell, A. Watts, and R. Ottmar. Wildland Fire Emission Sampling at Fishlake National Forest, Utah Using an Unmanned Aircraft System.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 247: 118193, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Brian Gullett",
+                "hasEmail": "mailto:gullett.brian@epa.gov"
+            },
+            "description": "Emissions from a stand replacement prescribed burn were sampled using an unmanned aircraft system (UAS, or \u201cdrone\u201d) in Fishlake National Forest, Utah, U.S.A. Sixteen flights over three days in June 2019 provided emission factors for a broad range of compounds including carbon monoxide (CO), carbon dioxide (CO2), nitric oxide (NO), nitrogen oxide (NO2), particulate matter < 2.5 microns in diameter (PM2.5), volatile organic compounds (VOCs) including carbonyls, black carbon, and elemental/organic carbon. To our knowledge, this is the first UAS-based emission sampling for a fire of this magnitude, including both slash pile and crown fires resulting in wildfire-like conditions. The burns consisted of drip torch ignitions as well as ground-mobile and aerial helicopter ignitions of large stands comprising over 1,000 ha, allowing for comparison of same-species emission factors burned under different conditions. The use of a UAS for emission sampling minimizes risk to personnel and equipment, allowing flexibility in sampling location and ensuring capture of representative, fresh smoke constituents. PM2.5 emission factors varied 5-fold and, like most pollutants, varied inversely with combustion efficiency resulting in lower emission factors from the slash piles than the crown fires. \n\nThis dataset is associated with the following publication:\nAurell, J., B. Gullett, A. Holder, F. Kiros, B. Mitchell, A. Watts, and R. Ottmar. Wildland Fire Emission Sampling at Fishlake National Forest, Utah Using an Unmanned Aircraft System.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 247: 118193, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520907/Data%20Table%20Science%20Hub%20FASMEE%2005-04-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Table Science Hub FASMEE 05-04-2020.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520907",
             "keyword": [
@@ -137395,20 +137399,10 @@
                 "sampler",
                 "unmanned aerials system"
             ],
-            "contactPoint": {
-                "fn": "Brian Gullett",
-                "hasEmail": "mailto:gullett.brian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data Table Science Hub FASMEE 05-04-2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520907/Data%20Table%20Science%20Hub%20FASMEE%2005-04-2020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-07",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2021.118193"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137418,54 +137412,55 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2021.118193"
+            ],
+            "rights": null,
+            "title": "Wildland Fire Emission Sampling at Fishlake National Forest, Utah Using an Unmanned Aircraft System"
         },
         {
-            "title": "Unit and Regression Tests of Scientific Software: A Study on SWMM",
-            "description": "Testing helps assure software quality by executing programs and uncovering bugs. Scientific software developers often find it challenging to carry out systematic and automated testing due to reasons such as inherent model uncertainties and complex floating-point computations. Extending the recent work on analyzing the unit tests written by the developers of the Storm Water Management Model (SWMM), we report in this paper the investigation of both unit and regression tests of SWMM. The results show that the 1,458 SWMM tests have a 54.0% code coverage and an 82.4% User\u2019s Manual coverage. Meanwhile, an examination of eight regression tests from a test set shows a 79.5% code coverage and a near 100% User\u2019s Manual coverage. We also observe a \u201cgetter-setter-getter\u201d testing pattern from the SWMM unit tests and suggest a diversified way of designing or adopting regression tests. \n\nThis dataset is associated with the following publication:\nPeng, Z., X. Lin, M. Simon, and N. Niu. Unit and Regression Tests of Scientific Software: A Study on SWMM.   Journal of Computational Science. Elsevier B.V., Amsterdam,  NETHERLANDS, 53: 101347, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519338",
-            "keyword": [
-                "scientific software",
-                "unit testing",
-                "regression testing",
-                "User\u2019s Manual",
-                "test-coverage",
-                "Storm Water Management Model (SWMM)"
-            ],
             "contactPoint": {
                 "fn": "Michelle Simon",
                 "hasEmail": "mailto:simon.michelle@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519338/documents/Unit%20and%20Regression%20Tests%20of%20Scientific%20Softwaredatadictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Testing helps assure software quality by executing programs and uncovering bugs. Scientific software developers often find it challenging to carry out systematic and automated testing due to reasons such as inherent model uncertainties and complex floating-point computations. Extending the recent work on analyzing the unit tests written by the developers of the Storm Water Management Model (SWMM), we report in this paper the investigation of both unit and regression tests of SWMM. The results show that the 1,458 SWMM tests have a 54.0% code coverage and an 82.4% User\u2019s Manual coverage. Meanwhile, an examination of eight regression tests from a test set shows a 79.5% code coverage and a near 100% User\u2019s Manual coverage. We also observe a \u201cgetter-setter-getter\u201d testing pattern from the SWMM unit tests and suggest a diversified way of designing or adopting regression tests. \n\nThis dataset is associated with the following publication:\nPeng, Z., X. Lin, M. Simon, and N. Niu. Unit and Regression Tests of Scientific Software: A Study on SWMM.   Journal of Computational Science. Elsevier B.V., Amsterdam,  NETHERLANDS, 53: 101347, (2021).",
             "distribution": [
                 {
-                    "title": "Mappings_of_SWMM_unit_tests.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519338/Mappings_of_SWMM_unit_tests.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mappings_of_SWMM_unit_tests.xlsx"
                 },
                 {
-                    "title": "regression test data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519338/regression%20test%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "regression test data.xlsx"
                 },
                 {
-                    "title": "test study on swmm(data table).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519338/test%20study%20on%20swmm%28data%20table%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "test study on swmm(data table).xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519338",
+            "keyword": [
+                "scientific software",
+                "unit testing",
+                "regression testing",
+                "User\u2019s Manual",
+                "test-coverage",
+                "Storm Water Management Model (SWMM)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-08",
-            "references": [
-                "https://doi.org/10.1016/j.jocs.2021.101347",
-                "https://pasteur.epa.gov/uploads/10.23719/1519338/documents/SWMM%20OpenCppCoverage%20Step.pdf"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137476,42 +137471,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1519338/documents/Unit%20and%20Regression%20Tests%20of%20Scientific%20Softwaredatadictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.jocs.2021.101347",
+                "https://pasteur.epa.gov/uploads/10.23719/1519338/documents/SWMM%20OpenCppCoverage%20Step.pdf"
+            ],
+            "rights": null,
+            "title": "Unit and Regression Tests of Scientific Software: A Study on SWMM"
         },
         {
-            "title": "Avoiding Pitfalls When Modeling Removal of Per\u2010 and Polyfluoroalkyl Substances by Anion Exchange",
-            "description": "Time series data from analytical solutions for ion exchange kinetics. \n\nThis dataset is associated with the following publication:\nHaupert, L., J. Pressman, T. Speth, and D. Wahman. Avoiding Pitfalls When Modeling Removal of Per\u2010 and Polyfluoroalkyl Substances by Anion Exchange.   AWWA Water Science. John Wiley & Sons, Inc., Hoboken, NJ, USA, 3(2): e1222, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1519066",
-            "keyword": [
-                "ion exchange",
-                "drinking water",
-                "modeling",
-                "PFAS"
-            ],
             "contactPoint": {
                 "fn": "Levi Haupert",
                 "hasEmail": "mailto:haupert.levi@epa.gov"
             },
+            "description": "Time series data from analytical solutions for ion exchange kinetics. \n\nThis dataset is associated with the following publication:\nHaupert, L., J. Pressman, T. Speth, and D. Wahman. Avoiding Pitfalls When Modeling Removal of Per\u2010 and Polyfluoroalkyl Substances by Anion Exchange.   AWWA Water Science. John Wiley & Sons, Inc., Hoboken, NJ, USA, 3(2): e1222, (2021).",
             "distribution": [
                 {
-                    "title": "plot_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519066/plot_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "plot_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519066",
+            "keyword": [
+                "ion exchange",
+                "drinking water",
+                "modeling",
+                "PFAS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-09",
-            "references": [
-                "https://doi.org/10.1002/aws2.1222"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137521,19 +137515,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/aws2.1222"
+            ],
+            "rights": null,
+            "title": "Avoiding Pitfalls When Modeling Removal of Per\u2010 and Polyfluoroalkyl Substances by Anion Exchange"
         },
         {
-            "title": "SICAS2 Baseline SciHUB",
-            "description": "ERMI analyses of dust samples from schools and homes in the study. \n\nThis dataset is associated with the following publication:\nHowared, E.J., S. Vesper, B.J. Guthrie, C.R. Petty, V.A. Ramdin, W.J. Sheehan, J.M. Gaffin, P. Permaul, P.S. Lai, L.M. Bartnikas, A. Cunningham, M. Hauptman, D.R. Gold, S.N. Baxi, and W. Phipatanakul. Asthma Prevalence and Mold Levels in US Northeastern Schools.   The Journal of Allergy and Clinical Immunology: In Practice. Elsevier B.V., Amsterdam,  NETHERLANDS, 9(3): 1312-1318, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Stephen Vesper",
+                "hasEmail": "mailto:vesper.stephen@epa.gov"
+            },
+            "description": "ERMI analyses of dust samples from schools and homes in the study. \n\nThis dataset is associated with the following publication:\nHowared, E.J., S. Vesper, B.J. Guthrie, C.R. Petty, V.A. Ramdin, W.J. Sheehan, J.M. Gaffin, P. Permaul, P.S. Lai, L.M. Bartnikas, A. Cunningham, M. Hauptman, D.R. Gold, S.N. Baxi, and W. Phipatanakul. Asthma Prevalence and Mold Levels in US Northeastern Schools.   The Journal of Allergy and Clinical Immunology: In Practice. Elsevier B.V., Amsterdam,  NETHERLANDS, 9(3): 1312-1318, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520607/SICAS2%20Baseline%20SciHUB%20Revised%20SV.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SICAS2 Baseline SciHUB Revised SV.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520607",
             "keyword": [
@@ -137544,20 +137548,10 @@
                 "school",
                 "ERMI"
             ],
-            "contactPoint": {
-                "fn": "Stephen Vesper",
-                "hasEmail": "mailto:vesper.stephen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SICAS2 Baseline SciHUB Revised SV.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520607/SICAS2%20Baseline%20SciHUB%20Revised%20SV.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-07-14",
-            "references": [
-                "https://doi.org/10.1016/j.jaip.2020.10.012"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137567,47 +137561,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jaip.2020.10.012"
+            ],
+            "rights": null,
+            "title": "SICAS2 Baseline SciHUB"
         },
         {
-            "title": "Modeling the Photoinactivation and Transport of Somatic and F+ Coliphages at a Great Lakes Beach",
-            "description": "Data include: UV-visible absorption and currents data (ADCP) for swimming waters and a contaminated tributary of Washington Park beach, Michigan City IN obtained  during summer, 2015 . Data include a map of the  locations where samples were collected and ADCP data were collected. \n\nThis dataset is associated with the following publication:\nSafaie, A., C. Weiskerger, T. Nguyen, B. Acrey, R. Zepp, M. Molina, M. Cyterski, G. Whelan, Y. Pachepsky, and M. Phanikumar. Modeling the photoinactivation and transport of somatic and f+ coliphages at a great lakes beach.   JOURNAL OF ENVIRONMENTAL QUALITY. American Society of Agronomy, MADISON, WI, USA, 49(6): 1612-1623, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1520427",
-            "keyword": [
-                "beaches",
-                "Bacteriophage",
-                "E. coli",
-                "modeling",
-                "photoinactivation",
-                "public health"
-            ],
             "contactPoint": {
                 "fn": "Richard Zepp",
                 "hasEmail": "mailto:zepp.richard@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520427/documents/Description%20of%20Dataset%20files%20Washington%20Park%20Indiana%20rvsd.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Data include: UV-visible absorption and currents data (ADCP) for swimming waters and a contaminated tributary of Washington Park beach, Michigan City IN obtained  during summer, 2015 . Data include a map of the  locations where samples were collected and ADCP data were collected. \n\nThis dataset is associated with the following publication:\nSafaie, A., C. Weiskerger, T. Nguyen, B. Acrey, R. Zepp, M. Molina, M. Cyterski, G. Whelan, Y. Pachepsky, and M. Phanikumar. Modeling the photoinactivation and transport of somatic and f+ coliphages at a great lakes beach.   JOURNAL OF ENVIRONMENTAL QUALITY. American Society of Agronomy, MADISON, WI, USA, 49(6): 1612-1623, (2020).",
             "distribution": [
                 {
-                    "title": "WP Abs Coeff Data for June-Sept 2015.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520427/WP%20Abs%20Coeff%20Data%20for%20June-Sept%202015.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "WP Abs Coeff Data for June-Sept 2015.xlsx"
                 },
                 {
-                    "title": "ADCP.DATA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520427/ADCP.DATA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ADCP.DATA.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520427",
+            "keyword": [
+                "beaches",
+                "Bacteriophage",
+                "E. coli",
+                "modeling",
+                "photoinactivation",
+                "public health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-06-14",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137617,43 +137615,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1520427/documents/Description%20of%20Dataset%20files%20Washington%20Park%20Indiana%20rvsd.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": null,
+            "rights": null,
+            "title": "Modeling the Photoinactivation and Transport of Somatic and F+ Coliphages at a Great Lakes Beach"
         },
         {
-            "title": "Data supporting the article titled: Effects of future hydroclimatic conditions on microbial water quality and management practices in two agricultural watersheds.",
-            "description": "File (spreadsheet) contains a summary of data presented in the journal article titled \"Effects of future hydroclimatic conditions on microbial water quality and management practices in two agricultural watersheds\". \n\nThis dataset is associated with the following publication:\nCoffey, R.P., J. Butcher, B. Benham, and T. Johnson. Modeling the Effects of Future Hydroclimatic Conditions on Microbial Water Quality and Management Practices in Two Agricultural Watersheds.   Transactions of the ASABE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 63(3): 753-770, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503908",
-            "keyword": [
-                "microbial water quality",
-                "management responses",
-                "hydroclimatic conditions",
-                "watersheds",
-                "modeling"
-            ],
             "contactPoint": {
                 "fn": "Rory Patrick Coffey",
                 "hasEmail": "mailto:coffey.rory@epa.gov"
             },
+            "description": "File (spreadsheet) contains a summary of data presented in the journal article titled \"Effects of future hydroclimatic conditions on microbial water quality and management practices in two agricultural watersheds\". \n\nThis dataset is associated with the following publication:\nCoffey, R.P., J. Butcher, B. Benham, and T. Johnson. Modeling the Effects of Future Hydroclimatic Conditions on Microbial Water Quality and Management Practices in Two Agricultural Watersheds.   Transactions of the ASABE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 63(3): 753-770, (2020).",
             "distribution": [
                 {
-                    "title": "FC_paper_fig_table_data_20190610.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503908/FC_paper_fig_table_data_20190610.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FC_paper_fig_table_data_20190610.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503908",
+            "keyword": [
+                "microbial water quality",
+                "management responses",
+                "hydroclimatic conditions",
+                "watersheds",
+                "modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-10",
-            "references": [
-                "https://doi.org/10.13031/trans.13630"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -137663,113 +137657,115 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.13031/trans.13630"
+            ],
+            "rights": null,
+            "title": "Data supporting the article titled: Effects of future hydroclimatic conditions on microbial water quality and management practices in two agricultural watersheds."
         },
         {
-            "title": "Estimating PM2.5-related premature mortality and morbidity associated with future wildfire emissions in the western US",
-            "description": "Wildfire burned area, emissions, concentrations, and health impact modeling datasets. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1522293",
-            "keyword": [
-                "climate",
-                "wildfire",
-                "emissions",
-                "health"
-            ],
             "contactPoint": {
                 "fn": "Jeremy Martinich",
                 "hasEmail": "mailto:martinich.jeremy@epa.gov"
             },
+            "description": "Wildfire burned area, emissions, concentrations, and health impact modeling datasets. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "BenMAP README.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522293/BenMAP%20README.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "BenMAP README.txt"
                 },
                 {
-                    "title": "Concentrations README.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522293/Concentrations%20README.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Concentrations README.txt"
                 },
                 {
-                    "title": "Emissions README.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522293/Emissions%20README.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Emissions README.txt"
                 },
                 {
-                    "title": "Acreage Burned README.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522293/Acreage%20Burned%20README.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Acreage Burned README.txt"
                 },
                 {
-                    "title": "https://dmap-data-commons-oar.s3.amazonaws.com/index.html?prefix=Neumann%20et%20al.%202021%20/",
-                    "accessURL": "https://dmap-data-commons-oar.s3.amazonaws.com/index.html?prefix=Neumann%20et%20al.%202021%20/"
+                    "accessURL": "https://dmap-data-commons-oar.s3.amazonaws.com/index.html?prefix=Neumann%20et%20al.%202021%20/",
+                    "title": "https://dmap-data-commons-oar.s3.amazonaws.com/index.html?prefix=Neumann%20et%20al.%202021%20/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1522293",
+            "keyword": [
+                "climate",
+                "wildfire",
+                "emissions",
+                "health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-04-08",
-            "references": [
-                "https://dx.doi.org/10.1088/1748-9326/abe82b",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8048092"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. Environmental Protection Agency",
                 "subOrganizationOf": {
                     "name": "U.S. Government"
                 }
-            }
+            },
+            "references": [
+                "https://dx.doi.org/10.1088/1748-9326/abe82b",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8048092"
+            ],
+            "rights": null,
+            "title": "Estimating PM2.5-related premature mortality and morbidity associated with future wildfire emissions in the western US"
         },
         {
-            "title": "Quantitative Prediction of Repeat Dose Toxicity Values using GenRA",
-            "description": "Per Imran Shah, this was the Data used in and published as supplemental material for this manuscript.\nTable S1. Aggregated point of departure (POD) data obtained from ToxRefDB v2.0. \nTable S2. Chemical structure descriptor data from DSSTox.\nTable S3. Chemical cluster membership.\nTable S5. GenRA optimal predictions for each endpoint category and cluster.\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503854",
-            "keyword": [
-                "DSSTox"
-            ],
             "contactPoint": {
                 "fn": "Ann Richard",
                 "hasEmail": "mailto:richard.ann@epa.gov"
             },
+            "description": "Per Imran Shah, this was the Data used in and published as supplemental material for this manuscript.\nTable S1. Aggregated point of departure (POD) data obtained from ToxRefDB v2.0. \nTable S2. Chemical structure descriptor data from DSSTox.\nTable S3. Chemical cluster membership.\nTable S5. GenRA optimal predictions for each endpoint category and cluster.\n",
             "distribution": [
                 {
-                    "title": "genra-table-S5-cluster-perf.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503854/genra-table-S5-cluster-perf.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "genra-table-S5-cluster-perf.xlsx"
                 },
                 {
-                    "title": "genra-table-S3-clusters.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503854/genra-table-S3-clusters.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "genra-table-S3-clusters.xlsx"
                 },
                 {
-                    "title": "genra-table-S2-chm.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503854/genra-table-S2-chm.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "genra-table-S2-chm.xlsx"
                 },
                 {
-                    "title": "genra-table-S1-pod.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503854/genra-table-S1-pod.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "genra-table-S1-pod.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503854",
+            "keyword": [
+                "DSSTox"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-10",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137778,65 +137774,65 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Quantitative Prediction of Repeat Dose Toxicity Values using GenRA"
         },
         {
-            "title": "Analysis of transcriptomic data from duodena of mice exposed to hexavalent chromium in drinking water: Supplemental data supporting a research report. ",
-            "description": "These secondary data have been produced from the gene expression data generated from duodena of mice exposed to hexavalent chromium in drinking water and deposited in the GEO repository under accession number GSE87259. They include (i) inferred upstream regulators responsible for the observed changes in gene expression, (ii) genes significantly differentially expressed between duodena of exposed and control mice, and (iii) list of CFTR gene variants associated with cancers in COSMIC tumor repository.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1522298",
-            "keyword": [
-                "cystic fibrosis",
-                "CFTR",
-                "carcinogenesis",
-                "chromium"
-            ],
             "contactPoint": {
                 "fn": "Roman Mezencev",
                 "hasEmail": "mailto:mezencev.roman@epa.gov"
             },
+            "description": "These secondary data have been produced from the gene expression data generated from duodena of mice exposed to hexavalent chromium in drinking water and deposited in the GEO repository under accession number GSE87259. They include (i) inferred upstream regulators responsible for the observed changes in gene expression, (ii) genes significantly differentially expressed between duodena of exposed and control mice, and (iii) list of CFTR gene variants associated with cancers in COSMIC tumor repository.",
             "distribution": [
                 {
-                    "title": "Supplemental_file 5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522298/Supplemental_file%205.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental_file 5.xlsx"
                 },
                 {
-                    "title": "Supplemental_file 4.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522298/Supplemental_file%204.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Supplemental_file 4.xls"
                 },
                 {
-                    "title": "Supplemental_file 3.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522298/Supplemental_file%203.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Supplemental_file 3.xls"
                 },
                 {
-                    "title": "Supplemental_file 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522298/Supplemental_file%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental_file 2.xlsx"
                 },
                 {
-                    "title": "Supplemental_file 1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522298/Supplemental_file%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental_file 1.xlsx"
                 },
                 {
-                    "title": "Metadata_Supplemental files1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522298/Metadata_Supplemental%20files1.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Metadata_Supplemental files1.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1522298",
+            "keyword": [
+                "cystic fibrosis",
+                "CFTR",
+                "carcinogenesis",
+                "chromium"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-04-15",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -137845,258 +137841,256 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Analysis of transcriptomic data from duodena of mice exposed to hexavalent chromium in drinking water: Supplemental data supporting a research report. "
         },
         {
-            "title": "Integrative computational approaches to inform relative bioaccumulation potential of per- and polyfluoroalkyl substances (PFAS) across species",
-            "description": "Datasets included in the entry are Results from the US Environmental Protection Agency Sequence Alignment to Predict Across Species Susceptibility (SeqAPASS) tool and from the molecular modeling workflow that includes molecular docking and molecular dynamic simulations. All data that are represented in the figures, tables, and supplemental materials associated with this manuscript are included in this dataset entry. \n\nThis dataset is associated with the following publication:\nCheng, W., J. Doering, C. LaLone, and C. Ng. Integrative computational approaches to inform relative bioaccumulation potential of per- and polyfluoroalkyl substances (PFAS) across species.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  180(2): 212-223, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1519247",
-            "keyword": [
-                "Per- and poly-fluoroalkyl substances",
-                "Liver fatty acid binding protein",
-                "bioaccumulation",
-                "molecular modeling",
-                "SeqAPASS",
-                "adverse outcome pathway",
-                "ecotoxicology",
-                "honey bee",
-                "cross-species extrapolation",
-                "screening and prioritization",
-                "networks"
-            ],
             "contactPoint": {
                 "fn": "Carlie Lalone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Datasets included in the entry are Results from the US Environmental Protection Agency Sequence Alignment to Predict Across Species Susceptibility (SeqAPASS) tool and from the molecular modeling workflow that includes molecular docking and molecular dynamic simulations. All data that are represented in the figures, tables, and supplemental materials associated with this manuscript are included in this dataset entry. \n\nThis dataset is associated with the following publication:\nCheng, W., J. Doering, C. LaLone, and C. Ng. Integrative computational approaches to inform relative bioaccumulation potential of per- and polyfluoroalkyl substances (PFAS) across species.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  180(2): 212-223, (2021).",
             "distribution": [
                 {
-                    "title": "Figure_2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_2.xlsx"
                 },
                 {
-                    "title": "Figure_4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_4.xlsx"
                 },
                 {
-                    "title": "Figure_3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_3.xlsx"
                 },
                 {
-                    "title": "Figure_5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_5.xlsx"
                 },
                 {
-                    "title": "Figure_S3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_S3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_S3.xlsx"
                 },
                 {
-                    "title": "Figure_S4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_S4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_S4.xlsx"
                 },
                 {
-                    "title": "Figure_S5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_S5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_S5.xlsx"
                 },
                 {
-                    "title": "Figure_S6.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure_S6.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_S6.xlsx"
                 },
                 {
-                    "title": "Table_3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Table_3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_3.xlsx"
                 },
                 {
-                    "title": "Table_4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Table_4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_4.xlsx"
                 },
                 {
-                    "title": "Table_S2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Table_S2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S2.xlsx"
                 },
                 {
-                    "title": "Table_S6.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Table_S6.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S6.xlsx"
                 },
                 {
-                    "title": "Table_S3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Table_S3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S3.xlsx"
                 },
                 {
-                    "title": "Table_S7.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Table_S7.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S7.xlsx"
                 },
                 {
-                    "title": "Table_S8.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Table_S8.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S8.xlsx"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfba.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfba.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfba.txt"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfbs.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfbs.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfbs.txt"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfhpa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfhpa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfhpa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfhxa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfhxa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfhxa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfna.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfna.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfna.txt"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfoa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfoa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfoa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfos.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfos.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfos.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfba.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfba.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfba.txt"
                 },
                 {
-                    "title": "Figure S7_dock_fathead_pfpa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_fathead_pfpa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_fathead_pfpa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfbs.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfbs.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfbs.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfhpa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfhpa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfhpa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfhxa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfhxa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfhxa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfhxs.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfhxs.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfhxs.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfoa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfoa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfoa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfos.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfos.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfos.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfna.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfna.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfna.txt"
                 },
                 {
-                    "title": "Figure S7_dock_human_pfpa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_human_pfpa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_human_pfpa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfba.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfba.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfba.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfbs.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfbs.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfbs.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfhpa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfhpa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfhpa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfhxa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfhxa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfhxa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfhxs.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfhxs.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfhxs.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfna.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfna.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfna.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfoa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfoa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfoa.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfos.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfos.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfos.txt"
                 },
                 {
-                    "title": "Figure S7_dock_medaka_pfpa.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Figure%20S7_dock_medaka_pfpa.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure S7_dock_medaka_pfpa.txt"
                 },
                 {
-                    "title": "Data Dictionary Figures.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Data%20Dictionary%20Figures.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Dictionary Figures.docx"
                 },
                 {
-                    "title": "Data Dictionary Tables.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1519247/Data%20Dictionary%20Tables.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Dictionary Tables.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1519247",
+            "keyword": [
+                "Per- and poly-fluoroalkyl substances",
+                "Liver fatty acid binding protein",
+                "bioaccumulation",
+                "molecular modeling",
+                "SeqAPASS",
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "honey bee",
+                "cross-species extrapolation",
+                "screening and prioritization",
+                "networks"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-08-31",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfab004"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -138106,52 +138100,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfab004"
+            ],
+            "rights": null,
+            "title": "Integrative computational approaches to inform relative bioaccumulation potential of per- and polyfluoroalkyl substances (PFAS) across species"
         },
         {
-            "title": "Predictive Models for In Vitro Toxicokinetic Parameters to Inform High-throughput Risk-assessment_Prachi",
-            "description": "The data used in this analysis was obtained from published literature and available through the high-throughput toxicokinetic (HTTK) R package. The dataset consists of 1486 chemicals that span a variety of use classes including pharmaceuticals, food-use chemicals, pesticides and industrial chemicals of which 1139 chemicals had experimental human in vitro fraction unbound data and 642 chemicals that had experimental human in vitro intrinsic clearance data. Structures were curated and obtained from the DSSTox database. The distribution of experimental values for fraction unbound and intrinsic clearance is shown in Supplementary Figure S1. Since the data were non-normally distributed they were appropriately transformed before any analysis was conducted. The details of the transformation and the transformed data distribution are presented in the results section and Supplementary Figures S2 and S3. A complete list of chemicals with CAS registry numbers (CASRN), DSSTox generic substance IDs (DTXSIDs), structure and experimental data for both parameters are included as supplemental data (1.ChemicalListData.csv and 1.ChemicalList-QSARready.sdf). \n\nThis dataset is associated with the following publication:\nPradeep, P., G. Patlewicz, R. Pearce, J. Wambaugh, B. Wetmore, and R. Judson. Using Chemical Structure Information to Develop Predictive Models for In Vitro Toxicokinetic Parameters to Inform High-throughput Risk-assessment.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 16: 100136, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503529",
-            "keyword": [
-                "predictive models",
-                "toxicokinetic (TK) parameters",
-                "in vitro toxicity data",
-                "in silico",
-                "IVIVE",
-                "qsar",
-                "ACToR"
-            ],
             "contactPoint": {
                 "fn": "Richard Judson",
                 "hasEmail": "mailto:judson.richard@epa.gov"
             },
+            "description": "The data used in this analysis was obtained from published literature and available through the high-throughput toxicokinetic (HTTK) R package. The dataset consists of 1486 chemicals that span a variety of use classes including pharmaceuticals, food-use chemicals, pesticides and industrial chemicals of which 1139 chemicals had experimental human in vitro fraction unbound data and 642 chemicals that had experimental human in vitro intrinsic clearance data. Structures were curated and obtained from the DSSTox database. The distribution of experimental values for fraction unbound and intrinsic clearance is shown in Supplementary Figure S1. Since the data were non-normally distributed they were appropriately transformed before any analysis was conducted. The details of the transformation and the transformed data distribution are presented in the results section and Supplementary Figures S2 and S3. A complete list of chemicals with CAS registry numbers (CASRN), DSSTox generic substance IDs (DTXSIDs), structure and experimental data for both parameters are included as supplemental data (1.ChemicalListData.csv and 1.ChemicalList-QSARready.sdf). \n\nThis dataset is associated with the following publication:\nPradeep, P., G. Patlewicz, R. Pearce, J. Wambaugh, B. Wetmore, and R. Judson. Using Chemical Structure Information to Develop Predictive Models for In Vitro Toxicokinetic Parameters to Inform High-throughput Risk-assessment.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 16: 100136, (2020).",
             "distribution": [
                 {
-                    "title": "https://cran.r-project.org/web/packages/httk/index.html",
-                    "accessURL": "https://cran.r-project.org/web/packages/httk/index.html"
+                    "accessURL": "https://cran.r-project.org/web/packages/httk/index.html",
+                    "title": "https://cran.r-project.org/web/packages/httk/index.html"
                 },
                 {
-                    "title": "https://comptox.epa.gov/dashboard",
-                    "accessURL": "https://comptox.epa.gov/dashboard"
+                    "accessURL": "https://comptox.epa.gov/dashboard",
+                    "title": "https://comptox.epa.gov/dashboard"
                 },
                 {
-                    "title": "Supplemental.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503529/Supplemental.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Supplemental.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503529",
+            "keyword": [
+                "predictive models",
+                "toxicokinetic (TK) parameters",
+                "in vitro toxicity data",
+                "in silico",
+                "IVIVE",
+                "qsar",
+                "ACToR"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-21",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2020.100136"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -138161,41 +138155,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2020.100136"
+            ],
+            "rights": null,
+            "title": "Predictive Models for In Vitro Toxicokinetic Parameters to Inform High-throughput Risk-assessment_Prachi"
         },
         {
-            "title": "MagnusonMatthew_A-rxx4_dataset_20180604",
-            "description": "The dataset contains the raw data for the graphs in the paper. \n\nThis dataset is associated with the following publication:\nPhillips, R., R. James, and M. Magnuson. Functional categories of microbial toxicity resulting from three advanced oxidation process treatments during management and disposal of contaminated water.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 238: 124550, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
-            "identifier": "https://doi.org/10.23719/1500918",
-            "keyword": [
-                "water security",
-                "wastewater",
-                "advanced oxidation",
-                "treatment"
-            ],
             "contactPoint": {
                 "fn": "Matthew Magnuson",
                 "hasEmail": "mailto:magnuson.matthew@epa.gov"
             },
+            "description": "The dataset contains the raw data for the graphs in the paper. \n\nThis dataset is associated with the following publication:\nPhillips, R., R. James, and M. Magnuson. Functional categories of microbial toxicity resulting from three advanced oxidation process treatments during management and disposal of contaminated water.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 238: 124550, (2020).",
             "distribution": [
                 {
-                    "title": "MagnusonMatthew_A-rxx4_dataset_20180604.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500918/MagnusonMatthew_A-rxx4_dataset_20180604.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MagnusonMatthew_A-rxx4_dataset_20180604.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500918",
+            "keyword": [
+                "water security",
+                "wastewater",
+                "advanced oxidation",
+                "treatment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-04",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2019.124550"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -138205,67 +138199,67 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2019.124550"
+            ],
+            "rights": null,
+            "title": "MagnusonMatthew_A-rxx4_dataset_20180604"
         },
         {
-            "title": "Assessing Toxicokinetic Uncertainty and Variability in Risk Prioritization",
-            "description": "The supplemental information for this paper includes chemical-specific analytical methods, raw instrument data for chemical concentration analysis, processed data for experiments on intrinsic hepatic clearance (CLint -- metabolism) and chemical fraction unbound in the presence of human plasma protein (fup). Figures showing the curve fits for determining CLint are provided. Finally, all data were released publicly as HTTK R Package v1.10.1. \n\nThis dataset is associated with the following publication:\nWambaugh, J., B. Wetmore, C. Ring, C. Nicolas, R. Pearce, G. Honda, R. Dinallo, D. Angus, J. Gilbert, T. Sierra, A. Badrinarayanan, B. Snodgrass, A. Brockman, C. Strock, R. Setzer, and R. Thomas. Assessing Toxicokinetic Uncertainty and Variability in Risk Prioritization.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  172(2): 235-251, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504435",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "The supplemental information for this paper includes chemical-specific analytical methods, raw instrument data for chemical concentration analysis, processed data for experiments on intrinsic hepatic clearance (CLint -- metabolism) and chemical fraction unbound in the presence of human plasma protein (fup). Figures showing the curve fits for determining CLint are provided. Finally, all data were released publicly as HTTK R Package v1.10.1. \n\nThis dataset is associated with the following publication:\nWambaugh, J., B. Wetmore, C. Ring, C. Nicolas, R. Pearce, G. Honda, R. Dinallo, D. Angus, J. Gilbert, T. Sierra, A. Badrinarayanan, B. Snodgrass, A. Brockman, C. Strock, R. Setzer, and R. Thomas. Assessing Toxicokinetic Uncertainty and Variability in Risk Prioritization.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  172(2): 235-251, (2019).",
             "distribution": [
                 {
-                    "title": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data",
-                    "accessURL": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data"
+                    "accessURL": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data",
+                    "title": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data"
                 },
                 {
-                    "title": "https://cran.r-project.org/package=httk",
-                    "accessURL": "https://cran.r-project.org/package=httk"
+                    "accessURL": "https://cran.r-project.org/package=httk",
+                    "title": "https://cran.r-project.org/package=httk"
                 },
                 {
-                    "title": "SupTable4-ProcessedData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504435/SupTable4-ProcessedData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SupTable4-ProcessedData.xlsx"
                 },
                 {
-                    "title": "SupTable1-AnalyticalMethods.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504435/SupTable1-AnalyticalMethods.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SupTable1-AnalyticalMethods.xlsx"
                 },
                 {
-                    "title": "SupTable2-RawPPBData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504435/SupTable2-RawPPBData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SupTable2-RawPPBData.xlsx"
                 },
                 {
-                    "title": "SupTable3-RawCLintData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504435/SupTable3-RawCLintData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SupTable3-RawCLintData.xlsx"
                 },
                 {
-                    "title": "SupplementalFigures4.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504435/SupplementalFigures4.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "SupplementalFigures4.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504435",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-08",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfz205"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -138275,20 +138269,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfz205"
+            ],
+            "rights": null,
+            "title": "Assessing Toxicokinetic Uncertainty and Variability in Risk Prioritization"
         },
         {
-            "title": "PFLA extracellular enzyme activity",
-            "description": "USDA Data. This dataset is not publicly accessible because: USDA hasn't published a link yet - will modify ScienceHub when link is available. It can be accessed through the following means: USDA owns data will have a link eventually. Format: Excel files. \n\nThis dataset is associated with the following publication:\nTrippe, K.M., V.A. Manning, C.L. Reardon, A.M. Klein, C. Weidman, T.F.  Ducey, J.M. Novak, D.W. Watts, H.  Rushmiller, K.A. Spokas, J.A. Ippolito, and M.G. Johnson. Phytostabilization of acidic mine tailings with biochar, biosolids, lime, and locally-sourced microbial inoculum: Do amendment mixtures influence plant growth, tailing chemistry, and microbial composition?.   Applied Soil Ecology. Elsevier Science Ltd, New York, NY, USA, 165: 103962, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
+            "contactPoint": {
+                "fn": "Mark Johnson",
+                "hasEmail": "mailto:johnson.markg@epa.gov"
+            },
+            "description": "USDA Data. This dataset is not publicly accessible because: USDA hasn't published a link yet - will modify ScienceHub when link is available. It can be accessed through the following means: USDA owns data will have a link eventually. Format: Excel files. \n\nThis dataset is associated with the following publication:\nTrippe, K.M., V.A. Manning, C.L. Reardon, A.M. Klein, C. Weidman, T.F.  Ducey, J.M. Novak, D.W. Watts, H.  Rushmiller, K.A. Spokas, J.A. Ippolito, and M.G. Johnson. Phytostabilization of acidic mine tailings with biochar, biosolids, lime, and locally-sourced microbial inoculum: Do amendment mixtures influence plant growth, tailing chemistry, and microbial composition?.   Applied Soil Ecology. Elsevier Science Ltd, New York, NY, USA, 165: 103962, (2021).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1520575",
             "keyword": [
                 "biochar",
@@ -138296,14 +138294,10 @@
                 "plants",
                 "remediation"
             ],
-            "contactPoint": {
-                "fn": "Mark Johnson",
-                "hasEmail": "mailto:johnson.markg@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-01-11",
-            "references": [
-                "https://doi.org/10.1016/j.apsoil.2021.103962"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -138313,19 +138307,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apsoil.2021.103962"
+            ],
+            "rights": null,
+            "title": "PFLA extracellular enzyme activity"
         },
         {
-            "title": "Bioaccumulation of bis-(2-ethylhexyl)-3,4,5,6-tetrabromophthalate and mono-(2-ethylhexyl)-3,4,5,6-tetrabromophthalate by Lumbriculus variegatus",
-            "description": "- Concentration of TBPH and TBMEHP in sediment\n- Weigh and lipid contents of Lumbriculus variegatus over time\n- Concentrations in Lumbriculus variegatus of TBPH and TBMEPH, and L. variegatus lipid contents\n- Chemical Concentrations in Method Blanks. \n\nThis dataset is associated with the following publication:\nBurkhard, L., T. Lahren, T. Highland, R. Hockett, D. Mount, and T. Norberg-King. Bioaccumulation of bis-(2-ethylhexyl)-3,4,5,6-tetrabromophthalate and mono-(2-ethylhexyl)-3,4,5,6-tetrabromophthalate by Lumbriculus variegatus.   ARCHIVES OF ENVIRONMENTAL CONTAMINATION AND TOXICOLOGY. Springer, New York, NY, USA, 80: 579\u2013586, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Lawrence Burkhard",
+                "hasEmail": "mailto:burkhard.lawrence@epa.gov"
+            },
+            "description": "- Concentration of TBPH and TBMEHP in sediment\n- Weigh and lipid contents of Lumbriculus variegatus over time\n- Concentrations in Lumbriculus variegatus of TBPH and TBMEPH, and L. variegatus lipid contents\n- Chemical Concentrations in Method Blanks. \n\nThis dataset is associated with the following publication:\nBurkhard, L., T. Lahren, T. Highland, R. Hockett, D. Mount, and T. Norberg-King. Bioaccumulation of bis-(2-ethylhexyl)-3,4,5,6-tetrabromophthalate and mono-(2-ethylhexyl)-3,4,5,6-tetrabromophthalate by Lumbriculus variegatus.   ARCHIVES OF ENVIRONMENTAL CONTAMINATION AND TOXICOLOGY. Springer, New York, NY, USA, 80: 579\u2013586, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520087/TBPH%20%26%20TBMEPH%20Data%20Set%206-Oct-2020%20.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TBPH & TBMEPH Data Set 6-Oct-2020 .docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1520087",
             "keyword": [
@@ -138336,20 +138340,10 @@
                 "sediment testing",
                 "fish dietary studies"
             ],
-            "contactPoint": {
-                "fn": "Lawrence Burkhard",
-                "hasEmail": "mailto:burkhard.lawrence@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "TBPH & TBMEPH Data Set 6-Oct-2020 .docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520087/TBPH%20%26%20TBMEPH%20Data%20Set%206-Oct-2020%20.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-10-06",
-            "references": [
-                "https://doi.org/10.1007/s00244-021-00824-4"
+            "programCode": [
+                "020:097"
```

