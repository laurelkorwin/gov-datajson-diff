# Change History for epa.json (Part 29)

### Changes from 31606f9 to dd2190f (Part 19/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -189688,41 +189685,38 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md"
+            "references": null,
+            "rights": null,
+            "title": "U.S. Scaled WARM Waste Management by Sector and Material, 2018 v1.3.2"
         },
         {
-            "title": "National Employment Totals by Industry 2018 v2.0.0",
-            "description": "This dataset contains 2018 national employment by North American Industry Classification System (NAICS) 2012 6-digit codes. This dataset was generated with FLOWSA v2.0.0 (https://github.com/USEPA/flowsa/releases/tag/v2.0.0) and the method file https://github.com/USEPA/flowsa/blob/v2.0.0/flowsa/methods/flowbysectormethods/Employment_national_2018.yaml. The metadata text file included as a supporting document records the FLOWSA tool version and input dataset bibliographic details.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529941",
-            "keyword": [
-                "sector attribution model",
-                "NAICS",
-                "FLOWSA"
-            ],
             "contactPoint": {
                 "fn": "Catherine Birney",
                 "hasEmail": "mailto:birney.catherine@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/v2.0.0/format%20specs/FlowBySector.md",
+            "description": "This dataset contains 2018 national employment by North American Industry Classification System (NAICS) 2012 6-digit codes. This dataset was generated with FLOWSA v2.0.0 (https://github.com/USEPA/flowsa/releases/tag/v2.0.0) and the method file https://github.com/USEPA/flowsa/blob/v2.0.0/flowsa/methods/flowbysectormethods/Employment_national_2018.yaml. The metadata text file included as a supporting document records the FLOWSA tool version and input dataset bibliographic details.",
             "distribution": [
                 {
-                    "title": "Employment_national_2018_v2.0.0_372aab5.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529941/Employment_national_2018_v2.0.0_372aab5.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Employment_national_2018_v2.0.0_372aab5.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529941",
+            "keyword": [
+                "sector attribution model",
+                "NAICS",
+                "FLOWSA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-17",
-            "references": [
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Employment_national_2018_v2.0.0_372aab5.parquet",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Employment_national_2018_v2.0.0_372aab5_metadata.json"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189733,41 +189727,41 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/v2.0.0/format%20specs/FlowBySector.md"
+            "references": [
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Employment_national_2018_v2.0.0_372aab5.parquet",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Employment_national_2018_v2.0.0_372aab5_metadata.json"
+            ],
+            "rights": null,
+            "title": "National Employment Totals by Industry 2018 v2.0.0"
         },
         {
-            "title": "National Commercial Non-Hazardous Waste Totals by Industry 2018 v1.3.0",
-            "description": "This dataset contains 2018 national Commercial Non-Hazardous Waste by North American Industry Classification System (NAICS) 2012 6-digit codes. This dataset was generated with FLOWSA v1.3.0 (https://github.com/USEPA/flowsa/tree/v1.3.0) and the method file https://github.com/USEPA/flowsa/blob/v1.3.0/flowsa/methods/flowbysectormethods/CNHW_national_2018.yaml. The metadata text file included as a supporting document records the FLOWSA tool version and input dataset bibliographic details.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529942",
-            "keyword": [
-                "sector attribution model",
-                "FLOWSA",
-                "NAICS"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.0/format%20specs/FlowBySector.md",
+            "description": "This dataset contains 2018 national Commercial Non-Hazardous Waste by North American Industry Classification System (NAICS) 2012 6-digit codes. This dataset was generated with FLOWSA v1.3.0 (https://github.com/USEPA/flowsa/tree/v1.3.0) and the method file https://github.com/USEPA/flowsa/blob/v1.3.0/flowsa/methods/flowbysectormethods/CNHW_national_2018.yaml. The metadata text file included as a supporting document records the FLOWSA tool version and input dataset bibliographic details.",
             "distribution": [
                 {
-                    "title": "CNHW_national_2018_v1.3.0_4efcd5a.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529942/CNHW_national_2018_v1.3.0_4efcd5a.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "CNHW_national_2018_v1.3.0_4efcd5a.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529942",
+            "keyword": [
+                "sector attribution model",
+                "FLOWSA",
+                "NAICS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-02",
-            "references": [
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CNHW_national_2018_v1.3.0_4efcd5a.parquet",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CNHW_national_2018_v1.3.0_4efcd5a_metadata.json"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189778,39 +189772,42 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.0/format%20specs/FlowBySector.md"
+            "references": [
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CNHW_national_2018_v1.3.0_4efcd5a.parquet",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CNHW_national_2018_v1.3.0_4efcd5a_metadata.json"
+            ],
+            "rights": null,
+            "title": "National Commercial Non-Hazardous Waste Totals by Industry 2018 v1.3.0"
         },
         {
-            "title": "National Recycling Economic Indicators 2012 v1.3.2",
-            "description": "National economic indicators for recycling sectors, generally North American Industry Classification System (NAICS) 2012 codes, using USEPA Recycling Economic Information (REI) Report as the primary data source. This dataset was developed with FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) and the method file https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/REI_primaryfactors_national_2012.yaml.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529943",
-            "keyword": [
-                "sector attribution model",
-                "FLOWSA",
-                "NAICS"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md",
+            "description": "National economic indicators for recycling sectors, generally North American Industry Classification System (NAICS) 2012 codes, using USEPA Recycling Economic Information (REI) Report as the primary data source. This dataset was developed with FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) and the method file https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/REI_primaryfactors_national_2012.yaml.",
             "distribution": [
                 {
-                    "title": "REI_primaryfactors_national_2012_v1.3.2_9b1bb41.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529943/REI_primaryfactors_national_2012_v1.3.2_9b1bb41.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "REI_primaryfactors_national_2012_v1.3.2_9b1bb41.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529943",
+            "keyword": [
+                "sector attribution model",
+                "FLOWSA",
+                "NAICS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-09",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -189820,19 +189817,30 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md"
+            "references": null,
+            "rights": null,
+            "title": "National Recycling Economic Indicators 2012 v1.3.2"
         },
         {
-            "title": "Case Study Data for Separating Measurement Error and Signal in Environmental Data: Use of Replicates to Address Uncertainty (DOI 10.1021/acs.est.3c02231)",
-            "description": "The two case studies used publicly available environmental data excerpted from the National Human Exposure Assessment Survey (NHEXAS) (https://github.com/USEPA/HEDS). These U.S. Environmental Protection Agency (EPA) Region 5 data were samples collected in 1995 to 1997 from the first visit, which removed temporal between-visit correlation from sites across Ohio, Michigan, Illinois, Indiana, Wisconsin, and Minnesota. The NHEXAS tap water sampling design distinguished original samples from quality control replicates, and all samples were analyzed in the same laboratory following EPA standard method 200.8 (version 4.4). The case studies analyze subsets of NHEXAS arsenic and chromium data that were selected to meet distributional assumptions and cannot be interpreted as NHEXAS analyses. \n\nThis dataset is associated with the following publication:\nFurman, M., K. Thomas, and B. George. Separating Measurement Error and Signal in Environmental Data: Use of Replicates to Address Uncertainty.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(41): 15356-15365, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Barbara George",
+                "hasEmail": "mailto:george.bj@epa.gov"
+            },
+            "description": "The two case studies used publicly available environmental data excerpted from the National Human Exposure Assessment Survey (NHEXAS) (https://github.com/USEPA/HEDS). These U.S. Environmental Protection Agency (EPA) Region 5 data were samples collected in 1995 to 1997 from the first visit, which removed temporal between-visit correlation from sites across Ohio, Michigan, Illinois, Indiana, Wisconsin, and Minnesota. The NHEXAS tap water sampling design distinguished original samples from quality control replicates, and all samples were analyzed in the same laboratory following EPA standard method 200.8 (version 4.4). The case studies analyze subsets of NHEXAS arsenic and chromium data that were selected to meet distributional assumptions and cannot be interpreted as NHEXAS analyses. \n\nThis dataset is associated with the following publication:\nFurman, M., K. Thomas, and B. George. Separating Measurement Error and Signal in Environmental Data: Use of Replicates to Address Uncertainty.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(41): 15356-15365, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://pubs.acs.org/doi/full/10.1021/acs.est.3c02231",
+                    "title": "https://pubs.acs.org/doi/full/10.1021/acs.est.3c02231"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529910/es3c02231_si_003.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "es3c02231_si_003.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529910",
             "keyword": [
@@ -189845,26 +189853,10 @@
                 "signal confidence interval",
                 "simulation study"
             ],
-            "contactPoint": {
-                "fn": "Barbara George",
-                "hasEmail": "mailto:george.bj@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://pubs.acs.org/doi/full/10.1021/acs.est.3c02231",
-                    "accessURL": "https://pubs.acs.org/doi/full/10.1021/acs.est.3c02231"
-                },
-                {
-                    "title": "es3c02231_si_003.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529910/es3c02231_si_003.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-31",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c02231",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10733784",
-                "https://pasteur.epa.gov/uploads/10.23719/1529910/documents/es3c02231_si_002.pdf"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189874,60 +189866,62 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c02231",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10733784",
+                "https://pasteur.epa.gov/uploads/10.23719/1529910/documents/es3c02231_si_002.pdf"
+            ],
+            "rights": null,
+            "title": "Case Study Data for Separating Measurement Error and Signal in Environmental Data: Use of Replicates to Address Uncertainty (DOI 10.1021/acs.est.3c02231)"
         },
         {
-            "title": "A U.S. Lead Exposure Hotspots Analysis  ",
-            "description": "This is the dataset used for the U.S. lead exposure risk hotspot analysis in Zartarian et al., 2024, ES&T. The data dictionary files explain the contents of the 2 included zipped data folders. The Figures 1&2 zipped folder contains the data for Figures 1 and 2, the Supplement A figures, and the data for all tables in the paper. The Supplement B zipped folder contains the Random Forest modeling methodology in Supplement B and corresponding data. This folder also includes the full national dataset version of Random Forest model version 1 and 2 used in the analysis (in .csv format). \n\nThis dataset is associated with the following publication:\nZartarian Morrison, V., J. Xue, A. Poulakos, R. Tornero-Velez, L. Stanek, E. Snyder, V. Helms Garrison, K. Egan, and J. Courtney. A U.S. Lead Exposure Hotspots Analysis.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 7(7): 3311-3321, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529907",
-            "keyword": [
-                "Mapping",
-                "public health",
-                "Exposure predictions",
-                "hotspots",
-                "geospatial",
-                "children's health",
-                "Indicators and indices",
-                "lead"
-            ],
             "contactPoint": {
                 "fn": "Valerie Zartarian Morrison",
                 "hasEmail": "mailto:zartarian.valerie@epa.gov"
             },
+            "description": "This is the dataset used for the U.S. lead exposure risk hotspot analysis in Zartarian et al., 2024, ES&T. The data dictionary files explain the contents of the 2 included zipped data folders. The Figures 1&2 zipped folder contains the data for Figures 1 and 2, the Supplement A figures, and the data for all tables in the paper. The Supplement B zipped folder contains the Random Forest modeling methodology in Supplement B and corresponding data. This folder also includes the full national dataset version of Random Forest model version 1 and 2 used in the analysis (in .csv format). \n\nThis dataset is associated with the following publication:\nZartarian Morrison, V., J. Xue, A. Poulakos, R. Tornero-Velez, L. Stanek, E. Snyder, V. Helms Garrison, K. Egan, and J. Courtney. A U.S. Lead Exposure Hotspots Analysis.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 7(7): 3311-3321, (2024).",
             "distribution": [
                 {
-                    "title": "Figures_1_2_02082024.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529907/Figures_1_2_02082024.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Figures_1_2_02082024.zip"
                 },
                 {
-                    "title": "Supplement B.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529907/Supplement%20B.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Supplement B.zip"
                 },
                 {
-                    "title": "Zartarian_et_al_2024_Data_Dictionary_Figures_1_2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529907/Zartarian_et_al_2024_Data_Dictionary_Figures_1_2.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Zartarian_et_al_2024_Data_Dictionary_Figures_1_2.docx"
                 },
                 {
-                    "title": "Zartarian_et_al_2024_Data_Dictionary_Supp_B.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529907/Zartarian_et_al_2024_Data_Dictionary_Supp_B.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Zartarian_et_al_2024_Data_Dictionary_Supp_B.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529907",
+            "keyword": [
+                "Mapping",
+                "public health",
+                "Exposure predictions",
+                "hotspots",
+                "geospatial",
+                "children's health",
+                "Indicators and indices",
+                "lead"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-02-12",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c07881"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189937,20 +189931,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c07881"
+            ],
+            "rights": null,
+            "title": "A U.S. Lead Exposure Hotspots Analysis  "
         },
         {
-            "title": "Metals concentrations in seagrass plant tissues.",
-            "description": "Metals concentrations in seagrass plant tissues. This dataset is not publicly accessible because: Secondary data collected by non EPA authors. It can be accessed through the following means: Contact primary author. Format: Primary authors have the data associated with this manuscript. \n\nThis dataset is associated with the following publication:\nXu, S., J. Kaldy, X. Zhang, S. Yue, Z. Suonan, and Y. Zhou. Comparison of metals in eelgrass (Zostera marina L.) and the environment across the North Pacific Ocean: Environmental processes drive source delivery.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 343: 123096, (2024).",
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
+                "fn": "James Kaldy",
+                "hasEmail": "mailto:kaldy.jim@epa.gov"
+            },
+            "description": "Metals concentrations in seagrass plant tissues. This dataset is not publicly accessible because: Secondary data collected by non EPA authors. It can be accessed through the following means: Contact primary author. Format: Primary authors have the data associated with this manuscript. \n\nThis dataset is associated with the following publication:\nXu, S., J. Kaldy, X. Zhang, S. Yue, Z. Suonan, and Y. Zhou. Comparison of metals in eelgrass (Zostera marina L.) and the environment across the North Pacific Ocean: Environmental processes drive source delivery.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 343: 123096, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529981",
             "keyword": [
                 "bioconcentration",
@@ -189958,14 +189956,10 @@
                 "Bioindicator",
                 "heavy metals"
             ],
-            "contactPoint": {
-                "fn": "James Kaldy",
-                "hasEmail": "mailto:kaldy.jim@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-11-30",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2023.123096"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189975,96 +189969,95 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2023.123096"
+            ],
+            "rights": null,
+            "title": "Metals concentrations in seagrass plant tissues."
         },
         {
-            "title": "Organophosphate pesticide manuscript dataset",
-            "description": "Dataset investigating concordance between short-term transcriptomic points-of-departure and chronic points-of departure for three organophosphate pesticides across mouse and fathead minnow. Portions of this dataset are inaccessible because: The data files are too large. They can be accessed through the following means: Raw FASTQ files and raw and normalized read count matrices for the mouse liver study were submitted to the National Center for Biotechnology Information (NCBI) Gene Expression Omnibus database (accession GSE240853). Raw FASTQ files for the fathead minnow larva study were submitted to the NCBI Sequence Read Archive (submission: SUB13852035). Format: FASTQ files from RNA-sequencing. \n\nThis dataset is associated with the following publication:\nMartin, R., M. Hazemi, K. Flynn, D. Villeneuve, and L. Wehmas. Short-Term Transcriptomic Points of Departure Are Consistent with Chronic Points of Departure for Three Organophosphate Pesticides across Mouse and Fathead Minnow.   Toxics. MDPI, Basel,  SWITZERLAND, 11(10): 820, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529449",
-            "keyword": [
-                "transcriptomics",
-                "benchmark dose response",
-                "organophosphate pesticides",
-                "fathead minnow",
-                "mouse",
-                "fenthion",
-                "methidathion",
-                "parathion"
-            ],
             "contactPoint": {
                 "fn": "Leah Wehmas",
                 "hasEmail": "mailto:wehmas.leah@epa.gov"
             },
+            "description": "Dataset investigating concordance between short-term transcriptomic points-of-departure and chronic points-of departure for three organophosphate pesticides across mouse and fathead minnow. Portions of this dataset are inaccessible because: The data files are too large. They can be accessed through the following means: Raw FASTQ files and raw and normalized read count matrices for the mouse liver study were submitted to the National Center for Biotechnology Information (NCBI) Gene Expression Omnibus database (accession GSE240853). Raw FASTQ files for the fathead minnow larva study were submitted to the NCBI Sequence Read Archive (submission: SUB13852035). Format: FASTQ files from RNA-sequencing. \n\nThis dataset is associated with the following publication:\nMartin, R., M. Hazemi, K. Flynn, D. Villeneuve, and L. Wehmas. Short-Term Transcriptomic Points of Departure Are Consistent with Chronic Points of Departure for Three Organophosphate Pesticides across Mouse and Fathead Minnow.   Toxics. MDPI, Basel,  SWITZERLAND, 11(10): 820, (2023).",
             "distribution": [
                 {
-                    "title": "20230828_BMDExpress_mouse_liver.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230828_BMDExpress_mouse_liver.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230828_BMDExpress_mouse_liver.xlsx"
                 },
                 {
-                    "title": "20230828_BMDExpress_fathead_minnow_larvae.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230828_BMDExpress_fathead_minnow_larvae.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230828_BMDExpress_fathead_minnow_larvae.xlsx"
                 },
                 {
-                    "title": "Supplemental Fig 1_Network categories.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/Supplemental%20Fig%201_Network%20categories.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental Fig 1_Network categories.xlsx"
                 },
                 {
-                    "title": "FHM homologs conversion to HS MM and ZF.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/FHM%20homologs%20conversion%20to%20HS%20MM%20and%20ZF.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FHM homologs conversion to HS MM and ZF.xlsx"
                 },
                 {
-                    "title": "20230927_Supplemental_Tables.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230927_Supplemental_Tables.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230927_Supplemental_Tables.xlsx"
                 },
                 {
-                    "title": "20230927_Supplemental_Fig_2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230927_Supplemental_Fig_2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230927_Supplemental_Fig_2.xlsx"
                 },
                 {
-                    "title": "20230927_Supplemental_Fig_1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230927_Supplemental_Fig_1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230927_Supplemental_Fig_1.xlsx"
                 },
                 {
-                    "title": "20230927_Fig_5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230927_Fig_5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230927_Fig_5.xlsx"
                 },
                 {
-                    "title": "20230927_Fig_4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230927_Fig_4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230927_Fig_4.xlsx"
                 },
                 {
-                    "title": "20230927_Fig_3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230927_Fig_3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230927_Fig_3.xlsx"
                 },
                 {
-                    "title": "20230927_Fig_2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529449/20230927_Fig_2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20230927_Fig_2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529449",
+            "keyword": [
+                "transcriptomics",
+                "benchmark dose response",
+                "organophosphate pesticides",
+                "fathead minnow",
+                "mouse",
+                "fenthion",
+                "methidathion",
+                "parathion"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-06",
-            "references": [
-                "https://doi.org/10.3390/toxics11100820",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10611195"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190074,20 +190067,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxics11100820",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10611195"
+            ],
+            "rights": null,
+            "title": "Organophosphate pesticide manuscript dataset"
         },
         {
-            "title": "E-Cigarette Liquids and Aldehyde Flavoring Agents Inhibit CYP2A6 Activity in Lung Epithelial Cells",
-            "description": "Method to access data for Brett R. Winters et al., 'E-Cigarette Liquids and Aldehyde Flavoring Agents Inhibit CYP2A6 Activity in Lung Epithelial Cells' in ACS Omega, Vol 8, Issue 12, pg 11261-11266, 2023; DOI https://doi.org/10.1021/acsomega.2c08258, PMC10061538. This dataset is not publicly accessible because: Data was not shared by lead author. It can be accessed through the following means: To request data, contact lead author Brett Winters at brwinters@cytokinetics.com. Format: N/A. \n\nThis dataset is associated with the following publication:\nWinters, B., P. Clapp, S. Simmons, T. Kochar, I. Jaspers, and M. Madden. E-Cigarette Liquids and Aldehyde Flavoring Agents Inhibit CYP2A6 Activity in Lung Epithelial Cells.   ACS Omega. American Chemical Society, Washington, DC, USA, 8(12): 11261-11266, (2023).",
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
+                "fn": "Steven Simmons",
+                "hasEmail": "mailto:simmons.steve@epa.gov"
+            },
+            "description": "Method to access data for Brett R. Winters et al., 'E-Cigarette Liquids and Aldehyde Flavoring Agents Inhibit CYP2A6 Activity in Lung Epithelial Cells' in ACS Omega, Vol 8, Issue 12, pg 11261-11266, 2023; DOI https://doi.org/10.1021/acsomega.2c08258, PMC10061538. This dataset is not publicly accessible because: Data was not shared by lead author. It can be accessed through the following means: To request data, contact lead author Brett Winters at brwinters@cytokinetics.com. Format: N/A. \n\nThis dataset is associated with the following publication:\nWinters, B., P. Clapp, S. Simmons, T. Kochar, I. Jaspers, and M. Madden. E-Cigarette Liquids and Aldehyde Flavoring Agents Inhibit CYP2A6 Activity in Lung Epithelial Cells.   ACS Omega. American Chemical Society, Washington, DC, USA, 8(12): 11261-11266, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529957",
             "keyword": [
                 "e-cigarette",
@@ -190095,15 +190093,10 @@
                 "CYP2A6",
                 "aldehyde"
             ],
-            "contactPoint": {
-                "fn": "Steven Simmons",
-                "hasEmail": "mailto:simmons.steve@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-12-29",
-            "references": [
-                "https://doi.org/10.1021/acsomega.2c08258",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10061538"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190113,55 +190106,55 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acsomega.2c08258",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10061538"
+            ],
+            "rights": null,
+            "title": "E-Cigarette Liquids and Aldehyde Flavoring Agents Inhibit CYP2A6 Activity in Lung Epithelial Cells"
         },
         {
-            "title": "Defining the Biologically Plausible Taxonomic Domain of Applicability of an Adverse Outcome Pathway: A Case Study Linking Nicotinic Acetylcholine Receptor Activation to Colony Death",
-            "description": "Supporting Information for \"Jensen, M.A., Blatz, D.J. and LaLone, C.A. (2023), Defining the Biologically Plausible Taxonomic Domain of Applicability of an Adverse Outcome Pathway: A Case Study Linking Nicotinic Acetylcholine Receptor Activation to Colony Death. Environ Toxicol Chem, 42: 71-87. https://doi.org/10.1002/etc.5501\". \n\nThis dataset is associated with the following publication:\nJensen, M., D. Blatz, and C. Lalone. Defining the Biologically Plausible Taxonomic Domain of Applicability of an Adverse Outcome Pathway: A Case Study Linking Nicotinic Acetylcholine Receptor Activation to Colony Death.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(1): 71-87, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529946",
-            "keyword": [
-                "adverse outcome pathway",
-                "ecotoxicology",
-                "Species Extrapolation",
-                "Predictive Toxicology",
-                "SeqAPASS",
-                "pollinator",
-                "bioinformatics"
-            ],
             "contactPoint": {
                 "fn": "Carlie LaLone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Supporting Information for \"Jensen, M.A., Blatz, D.J. and LaLone, C.A. (2023), Defining the Biologically Plausible Taxonomic Domain of Applicability of an Adverse Outcome Pathway: A Case Study Linking Nicotinic Acetylcholine Receptor Activation to Colony Death. Environ Toxicol Chem, 42: 71-87. https://doi.org/10.1002/etc.5501\". \n\nThis dataset is associated with the following publication:\nJensen, M., D. Blatz, and C. Lalone. Defining the Biologically Plausible Taxonomic Domain of Applicability of an Adverse Outcome Pathway: A Case Study Linking Nicotinic Acetylcholine Receptor Activation to Colony Death.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(1): 71-87, (2023).",
             "distribution": [
                 {
-                    "title": "Supplemental Information.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529946/Supplemental%20Information.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supplemental Information.pdf"
                 },
                 {
-                    "title": "Data Dictionary.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529946/Data%20Dictionary.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Dictionary.docx"
                 },
                 {
-                    "title": "Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529946/Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529946",
+            "keyword": [
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "Species Extrapolation",
+                "Predictive Toxicology",
+                "SeqAPASS",
+                "pollinator",
+                "bioinformatics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-10-12",
-            "references": [
-                "https://doi.org/10.1002/etc.5501",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10100214"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190171,19 +190164,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5501",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10100214"
+            ],
+            "rights": null,
+            "title": "Defining the Biologically Plausible Taxonomic Domain of Applicability of an Adverse Outcome Pathway: A Case Study Linking Nicotinic Acetylcholine Receptor Activation to Colony Death"
         },
         {
-            "title": "Estrogenic Activity of Perfluoro Carboxylic and Sulfonic Acids in Rainbow Trout Estrogen Receptor Binding and Liver Slice Vtg mRNA Expression Assays",
-            "description": "Data for \"Estrogenic Activity of Perfluoro Carboxylic and Sulfonic Acids in Rainbow Trout Estrogen Receptor Binding and Liver Slice Vtg mRNA Expression Assays. Mark A. Tapper, Jeffrey S. Denny, Barbara R. Sheedy, Ben Johnson, and Richard C. Kolanczyk. Applied In Vitro Toxicology 2023 9:1, 13-22\". \n\nThis dataset is associated with the following publication:\nTapper, M., J. Denny, B. Sheedy, B. Johnson, and R. Kolanczyk. Estrogenic Activity of Perfluoro Carboxylic and Sulfonic Acids in Rainbow Trout Estrogen Receptor Binding and Liver Slice Vtg mRNA Expression Assays.   Applied In Vitro Toxicology. Mary Ann Liebert, Inc., Larchmont, NY, USA, 9(1): 13-22, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Mark Tapper",
+                "hasEmail": "mailto:tapper.mark@epa.gov"
+            },
+            "description": "Data for \"Estrogenic Activity of Perfluoro Carboxylic and Sulfonic Acids in Rainbow Trout Estrogen Receptor Binding and Liver Slice Vtg mRNA Expression Assays. Mark A. Tapper, Jeffrey S. Denny, Barbara R. Sheedy, Ben Johnson, and Richard C. Kolanczyk. Applied In Vitro Toxicology 2023 9:1, 13-22\". \n\nThis dataset is associated with the following publication:\nTapper, M., J. Denny, B. Sheedy, B. Johnson, and R. Kolanczyk. Estrogenic Activity of Perfluoro Carboxylic and Sulfonic Acids in Rainbow Trout Estrogen Receptor Binding and Liver Slice Vtg mRNA Expression Assays.   Applied In Vitro Toxicology. Mary Ann Liebert, Inc., Larchmont, NY, USA, 9(1): 13-22, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529975/Tapper%20et%20al%20PFAS%20manuscript%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tapper et al PFAS manuscript data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529975",
             "keyword": [
@@ -190195,20 +190199,10 @@
                 "competitive binding",
                 "vitellogenin"
             ],
-            "contactPoint": {
-                "fn": "Mark Tapper",
-                "hasEmail": "mailto:tapper.mark@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Tapper et al PFAS manuscript data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529975/Tapper%20et%20al%20PFAS%20manuscript%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-06",
-            "references": [
-                "https://doi.org/10.1089/aivt.2022.0013"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190218,57 +190212,57 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1089/aivt.2022.0013"
+            ],
+            "rights": null,
+            "title": "Estrogenic Activity of Perfluoro Carboxylic and Sulfonic Acids in Rainbow Trout Estrogen Receptor Binding and Liver Slice Vtg mRNA Expression Assays"
         },
         {
-            "title": "Assessing utility of thyroid in vitro screening assays through comparisons to observed impacts in vivo",
-            "description": "Supplementary data for \"Stephanie A. Eytcheson, Jennifer H. Olker, Katie Paul Friedman, Michael W. Hornung, Sigmund J. Degitz, Assessing utility of thyroid in vitro screening assays through comparisons to observed impacts in vivo, Regulatory Toxicology and Pharmacology, Volume 144, 2023, 105491, ISSN 0273-2300, https://doi.org/10.1016/j.yrtph.2023.105491.\". Portions of this dataset are inaccessible because: N/A. They can be accessed through the following means: N/A. Format: The data used in this analysis are from publicly available sources and are cited in the references and/or the supplemental files. \n\nThis dataset is associated with the following publication:\nEytcheson, S., J. Olker, K. Friedman, M. Hornung, and S. Degitz. Assessing utility of thyroid in vitro screening assays through comparisons to observed impacts in vivo.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 144: 105491, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529963",
-            "keyword": [
-                "endocrine disruption",
-                "high-throughput screening",
-                "thyroid",
-                "in vitro",
-                "in vivo"
-            ],
             "contactPoint": {
                 "fn": "Sigmund Degitz",
                 "hasEmail": "mailto:degitz.sigmund@epa.gov"
             },
+            "description": "Supplementary data for \"Stephanie A. Eytcheson, Jennifer H. Olker, Katie Paul Friedman, Michael W. Hornung, Sigmund J. Degitz, Assessing utility of thyroid in vitro screening assays through comparisons to observed impacts in vivo, Regulatory Toxicology and Pharmacology, Volume 144, 2023, 105491, ISSN 0273-2300, https://doi.org/10.1016/j.yrtph.2023.105491.\". Portions of this dataset are inaccessible because: N/A. They can be accessed through the following means: N/A. Format: The data used in this analysis are from publicly available sources and are cited in the references and/or the supplemental files. \n\nThis dataset is associated with the following publication:\nEytcheson, S., J. Olker, K. Friedman, M. Hornung, and S. Degitz. Assessing utility of thyroid in vitro screening assays through comparisons to observed impacts in vivo.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 144: 105491, (2023).",
             "distribution": [
                 {
-                    "title": "1-s2.0-S0273230023001599-mmc4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529963/1-s2.0-S0273230023001599-mmc4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1-s2.0-S0273230023001599-mmc4.xlsx"
                 },
                 {
-                    "title": "1-s2.0-S0273230023001599-mmc3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529963/1-s2.0-S0273230023001599-mmc3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1-s2.0-S0273230023001599-mmc3.xlsx"
                 },
                 {
-                    "title": "1-s2.0-S0273230023001599-mmc2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529963/1-s2.0-S0273230023001599-mmc2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1-s2.0-S0273230023001599-mmc2.xlsx"
                 },
                 {
-                    "title": "1-s2.0-S0273230023001599-mmc1.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529963/1-s2.0-S0273230023001599-mmc1.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "1-s2.0-S0273230023001599-mmc1.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529963",
+            "keyword": [
+                "endocrine disruption",
+                "high-throughput screening",
+                "thyroid",
+                "in vitro",
+                "in vivo"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-30",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2023.105491"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190278,41 +190272,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2023.105491"
+            ],
+            "rights": null,
+            "title": "Assessing utility of thyroid in vitro screening assays through comparisons to observed impacts in vivo"
         },
         {
-            "title": "Data used in the manuscript",
-            "description": "90% of the data in the spreadsheet is from publicly accessible databases. However, that data was used by ORD to generate emission estimates. \n\nThis dataset is associated with the following publication:\nTolaymat, T., N. Robey, M. Krause, J. Larson, K. Weitz, S. Parvathikar, L. Phelps, W. Linak, S. Burden, T. Speth, and J.D. Krug. A Critical Review of Perfluoroalkyl and Polyfluoroalkyl Substances (PFAS) Landfill Disposal in the United States.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 905: 167185, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529098",
-            "keyword": [
-                "Disposal",
-                "emissions",
-                "landfills",
-                "PFAS"
-            ],
             "contactPoint": {
                 "fn": "Thabet Tolaymat",
                 "hasEmail": "mailto:tolaymat.thabet@epa.gov"
             },
+            "description": "90% of the data in the spreadsheet is from publicly accessible databases. However, that data was used by ORD to generate emission estimates. \n\nThis dataset is associated with the following publication:\nTolaymat, T., N. Robey, M. Krause, J. Larson, K. Weitz, S. Parvathikar, L. Phelps, W. Linak, S. Burden, T. Speth, and J.D. Krug. A Critical Review of Perfluoroalkyl and Polyfluoroalkyl Substances (PFAS) Landfill Disposal in the United States.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 905: 167185, (2023).",
             "distribution": [
                 {
-                    "title": "Spreadsheet of Tables and Figures.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529098/Spreadsheet%20of%20Tables%20and%20Figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Spreadsheet of Tables and Figures.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529098",
+            "keyword": [
+                "Disposal",
+                "emissions",
+                "landfills",
+                "PFAS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-11",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.167185"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190322,42 +190316,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.167185"
+            ],
+            "rights": null,
+            "title": "Data used in the manuscript"
         },
         {
-            "title": "Gonadal Development in Smallmouth Bass (Micropterus Dolomieu) Reared in the Absence and Presence of 17-\u03b1-Ethinylestradiol",
-            "description": "Supporting information for \"Kadlec, S.M., Blackwell, B.R., Blanksma, C.A., Johnson, R.D., Olker, J.H., Schoff, P.K. and Mount, D.R. (2022), Gonadal Development in Smallmouth Bass (Micropterus Dolomieu) Reared in the Absence and Presence of 17-\u03b1-Ethinylestradiol. Environ Toxicol Chem, 41: 1416-1428. https://doi.org/10.1002/etc.5320\". \n\nThis dataset is associated with the following publication:\nKadlec, S., B. Blackwell, C. Blanksma, R. Johnson, J. Olker, P. Schoff, and D. Mount. Gonadal Development in Smallmouth Bass (Micropterus Dolomieu) Reared in the Absence and Presence of 17-\u03b1-Ethinylestradiol.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(6): 1416-1428, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529978",
-            "keyword": [
-                "testicular oocytes",
-                "gonadal development",
-                "endocrine disruption",
-                "smallmouth bass",
-                "ethinyl estradiol"
-            ],
             "contactPoint": {
                 "fn": "David Mount",
                 "hasEmail": "mailto:mount.dave@epa.gov"
             },
+            "description": "Supporting information for \"Kadlec, S.M., Blackwell, B.R., Blanksma, C.A., Johnson, R.D., Olker, J.H., Schoff, P.K. and Mount, D.R. (2022), Gonadal Development in Smallmouth Bass (Micropterus Dolomieu) Reared in the Absence and Presence of 17-\u03b1-Ethinylestradiol. Environ Toxicol Chem, 41: 1416-1428. https://doi.org/10.1002/etc.5320\". \n\nThis dataset is associated with the following publication:\nKadlec, S., B. Blackwell, C. Blanksma, R. Johnson, J. Olker, P. Schoff, and D. Mount. Gonadal Development in Smallmouth Bass (Micropterus Dolomieu) Reared in the Absence and Presence of 17-\u03b1-Ethinylestradiol.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(6): 1416-1428, (2022).",
             "distribution": [
                 {
-                    "title": "Supporting Information.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529978/Supporting%20Information.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supporting Information.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529978",
+            "keyword": [
+                "testicular oocytes",
+                "gonadal development",
+                "endocrine disruption",
+                "smallmouth bass",
+                "ethinyl estradiol"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-02-24",
-            "references": [
-                "https://doi.org/10.1002/etc.5320"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190367,42 +190361,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5320"
+            ],
+            "rights": null,
+            "title": "Gonadal Development in Smallmouth Bass (Micropterus Dolomieu) Reared in the Absence and Presence of 17-\u03b1-Ethinylestradiol"
         },
         {
-            "title": "Read-across application for emissions estimation",
-            "description": "The emission data used is based on this publication. \n\nThis dataset is associated with the following publication:\nTakkellapati, S., and M.A. Gonzalez. Application of read-across methods as a framework for the estimation of emissions from chemical processes.   Clean Technologies and Recycling. AIMS Press, Springfield, MO, USA, 3(4): 283-300, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529986",
-            "keyword": [
-                "emissions",
-                "Read-across",
-                "Environmental Releases",
-                "machine learning",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Sudhakar Takkellapati",
                 "hasEmail": "mailto:takkellapati.sudhakar@epa.gov"
             },
+            "description": "The emission data used is based on this publication. \n\nThis dataset is associated with the following publication:\nTakkellapati, S., and M.A. Gonzalez. Application of read-across methods as a framework for the estimation of emissions from chemical processes.   Clean Technologies and Recycling. AIMS Press, Springfield, MO, USA, 3(4): 283-300, (2023).",
             "distribution": [
                 {
-                    "title": "Meyer_ImprovingReliabilityOfChemicalManufactLCI_2020.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529986/Meyer_ImprovingReliabilityOfChemicalManufactLCI_2020.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Meyer_ImprovingReliabilityOfChemicalManufactLCI_2020.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529986",
+            "keyword": [
+                "emissions",
+                "Read-across",
+                "Environmental Releases",
+                "machine learning",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-11",
-            "references": [
-                "https://doi.org/10.3934/ctr.2023018"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190412,41 +190406,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3934/ctr.2023018"
+            ],
+            "rights": null,
+            "title": "Read-across application for emissions estimation"
         },
         {
-            "title": "Lab analytical data",
-            "description": "chemical concentrations. \n\nThis dataset is associated with the following publication:\nFalzone, S., C. Schaefer, E. Siegenthaler, K. Keating, D. Werkema, and L. Slater. Geophysical Signatures of Soil AFFF Contamination from Spectral Induced Polarization and Low Field Nuclear Magnetic Resonance Methods.   JOURNAL OF CONTAMINANT HYDROLOGY. Elsevier Science Ltd, New York, NY, USA, 260: 104268, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528295",
-            "keyword": [
-                "perfluoroalkyl substances",
-                "source zones",
-                "sorption",
-                "Aqueous Film Forming Foam"
-            ],
             "contactPoint": {
                 "fn": "Douglas Werkema",
                 "hasEmail": "mailto:werkema.d@epa.gov"
             },
+            "description": "chemical concentrations. \n\nThis dataset is associated with the following publication:\nFalzone, S., C. Schaefer, E. Siegenthaler, K. Keating, D. Werkema, and L. Slater. Geophysical Signatures of Soil AFFF Contamination from Spectral Induced Polarization and Low Field Nuclear Magnetic Resonance Methods.   JOURNAL OF CONTAMINANT HYDROLOGY. Elsevier Science Ltd, New York, NY, USA, 260: 104268, (2024).",
             "distribution": [
                 {
-                    "title": "V78124PFAS_Database_1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528295/V78124PFAS_Database_1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "V78124PFAS_Database_1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528295",
+            "keyword": [
+                "perfluoroalkyl substances",
+                "source zones",
+                "sorption",
+                "Aqueous Film Forming Foam"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-11-02",
-            "references": [
-                "https://doi.org/10.1016/j.jconhyd.2023.104268"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190456,42 +190450,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jconhyd.2023.104268"
+            ],
+            "rights": null,
+            "title": "Lab analytical data"
         },
         {
-            "title": "Durden et al data for SciHub 2023",
-            "description": "Data corresponding to figures in manuscript. \n\nThis dataset is associated with the following publication:\nDurden, L., K. Eckhoff, A. Burdsall, S. Youn, C. Andujar-Gonzalez, L. Abu-Niaaj, M. Magnuson, and W. Harper. Characterizing Bacillus globigii as a Bacillus anthracis surrogate for wastewater treatment studies and bioaerosol emissions.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 9(12): 3458\ufffd3466, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529809",
-            "keyword": [
-                "water security",
-                "Decontamination",
-                "biological",
-                "water infrastructure",
-                "Bacillus anthracis"
-            ],
             "contactPoint": {
                 "fn": "Matthew Magnuson",
                 "hasEmail": "mailto:magnuson.matthew@epa.gov"
             },
+            "description": "Data corresponding to figures in manuscript. \n\nThis dataset is associated with the following publication:\nDurden, L., K. Eckhoff, A. Burdsall, S. Youn, C. Andujar-Gonzalez, L. Abu-Niaaj, M. Magnuson, and W. Harper. Characterizing Bacillus globigii as a Bacillus anthracis surrogate for wastewater treatment studies and bioaerosol emissions.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 9(12): 3458\ufffd3466, (2023).",
             "distribution": [
                 {
-                    "title": "Durden et al data for SciHub 2023.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529809/Durden%20et%20al%20data%20for%20SciHub%202023.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Durden et al data for SciHub 2023.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529809",
+            "keyword": [
+                "water security",
+                "Decontamination",
+                "biological",
+                "water infrastructure",
+                "Bacillus anthracis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-23",
-            "references": [
-                "https://doi.org/10.1039/d3ew00524k"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190501,49 +190495,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d3ew00524k"
+            ],
+            "rights": null,
+            "title": "Durden et al data for SciHub 2023"
         },
         {
-            "title": "Growth kinetics summary data.",
-            "description": "Data Set S1 - Growth kinetics summary data. Tables S1 and S2 - Significantly upregulated V. alginolyticus endometabolites detected during iron supplementation and iron starvation experiments. \n\nThese data are available thru open access journal - https://doi.org/10.1128/spectrum.02680-23. Please contact the corresponding author directly for reuse. \n\nThis dataset is associated with the following publication:\nNorfolk, W., C. Shue, W. Henderson, D. Glinski, and E. Lipp. Vibrio alginolyticus growth kinetics and the metabolic effects of iron.   Microbiology Spectrum. American Society for Microbiology, Washington, DC, USA, 11(6): e0268023, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530046",
-            "keyword": [
-                "vibrio alginolyticus",
-                "metabolomics",
-                "Tolerance",
-                "iron",
-                "growth kinetics",
-                "Physiology"
-            ],
             "contactPoint": {
                 "fn": "William Henderson",
                 "hasEmail": "mailto:henderson.matt@epa.gov"
             },
+            "description": "Data Set S1 - Growth kinetics summary data. Tables S1 and S2 - Significantly upregulated V. alginolyticus endometabolites detected during iron supplementation and iron starvation experiments. \n\nThese data are available thru open access journal - https://doi.org/10.1128/spectrum.02680-23. Please contact the corresponding author directly for reuse. \n\nThis dataset is associated with the following publication:\nNorfolk, W., C. Shue, W. Henderson, D. Glinski, and E. Lipp. Vibrio alginolyticus growth kinetics and the metabolic effects of iron.   Microbiology Spectrum. American Society for Microbiology, Washington, DC, USA, 11(6): e0268023, (2023).",
             "distribution": [
                 {
-                    "title": "spectrum.02680-23-s0003.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530046/spectrum.02680-23-s0003.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "spectrum.02680-23-s0003.xlsx"
                 },
                 {
-                    "title": "spectrum.02680-23-s0001.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530046/spectrum.02680-23-s0001.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "spectrum.02680-23-s0001.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530046",
+            "keyword": [
+                "vibrio alginolyticus",
+                "metabolomics",
+                "Tolerance",
+                "iron",
+                "growth kinetics",
+                "Physiology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-26",
-            "references": [
-                "https://doi.org/10.1128/spectrum.02680-23",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10714744"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190553,19 +190546,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1128/spectrum.02680-23",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10714744"
+            ],
+            "rights": null,
+            "title": "Growth kinetics summary data."
         },
         {
-            "title": "Supplementary material for Noble et al. 2023 Characterization of algal community composition and structure from the nearshore environment, Lake Tahoe, (United States)",
-            "description": "Supplementary Data sheet 1.pdf is an image voucher flora of common soft-bodied algae from nearshore Lake Tahoe. \nSupplementary Data sheet 2.pdf is an image voucher flora of diatoms. \nSupplementary Data sheet 3.docx is a list of diatom voucher species references. \nSupplementary Table 1.xlsx is a translation table of diatom operational taxonomic units (OTUs), species names, and references.\nSupplementary Table 2.xlsx is a data matrix of diatom valve counts for seasonal and littoral zone comparison of assemblage composition.\nSupplementary Table 3.xlsx is soft-bodied algae translation table with biovolume information and species name references. \n\nThis dataset is associated with the following publication:\nNoble, P., C. Seitz, S. Lee, K. Manoylov, and S. Chandra. Characterization of algal community composition and structure from the nearshore environment, Lake Tahoe, (United States).   Frontiers in Ecology and Evolution. Frontiers, Lausanne,  SWITZERLAND, 10: 1053499, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Sylvia Lee",
+                "hasEmail": "mailto:lee.sylvia@epa.gov"
+            },
+            "description": "Supplementary Data sheet 1.pdf is an image voucher flora of common soft-bodied algae from nearshore Lake Tahoe. \nSupplementary Data sheet 2.pdf is an image voucher flora of diatoms. \nSupplementary Data sheet 3.docx is a list of diatom voucher species references. \nSupplementary Table 1.xlsx is a translation table of diatom operational taxonomic units (OTUs), species names, and references.\nSupplementary Table 2.xlsx is a data matrix of diatom valve counts for seasonal and littoral zone comparison of assemblage composition.\nSupplementary Table 3.xlsx is soft-bodied algae translation table with biovolume information and species name references. \n\nThis dataset is associated with the following publication:\nNoble, P., C. Seitz, S. Lee, K. Manoylov, and S. Chandra. Characterization of algal community composition and structure from the nearshore environment, Lake Tahoe, (United States).   Frontiers in Ecology and Evolution. Frontiers, Lausanne,  SWITZERLAND, 10: 1053499, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.frontiersin.org/articles/10.3389/fevo.2022.1053499/full#supplementary-material",
+                    "title": "https://www.frontiersin.org/articles/10.3389/fevo.2022.1053499/full#supplementary-material"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529845",
             "keyword": [
@@ -190575,20 +190578,10 @@
                 "periphyton",
                 "cyanobacteria"
             ],
-            "contactPoint": {
-                "fn": "Sylvia Lee",
-                "hasEmail": "mailto:lee.sylvia@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.frontiersin.org/articles/10.3389/fevo.2022.1053499/full#supplementary-material",
-                    "accessURL": "https://www.frontiersin.org/articles/10.3389/fevo.2022.1053499/full#supplementary-material"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-01-20",
-            "references": [
-                "https://doi.org/10.3389/fevo.2022.1053499",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10750852"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190598,128 +190591,127 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fevo.2022.1053499",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10750852"
+            ],
+            "rights": null,
+            "title": "Supplementary material for Noble et al. 2023 Characterization of algal community composition and structure from the nearshore environment, Lake Tahoe, (United States)"
         },
         {
-            "title": "Elemental fingerprint as a potential tool for tracking the fate of real-life model nanoplastics generated from plastic consumer products in environmental systems",
-            "description": "This research contains new data expanding the realm of nanoplastics that can be followed based on their metallic signatures to all kinds of plastics. Additionally, this study illustrates the importance of nanoplastics as a source of metals and metal-bearing nanoparticles in the environment. \n\nThis dataset is associated with the following publication:\nBaalousha, M., J. Wang, M.M. Nabi, M. Alam, M. Erfani, J. Gigault, F. Blancho, M. Davranche, P.M. Potter, and S.R. Al-Abed. The elemental fingerprint as a potential tool for tracking the fate of real-life model nanoplastics generated from plastic consumer products in environmental systems.   Environmental Science: Nano. Royal Society of Chemistry, Cambridge,  UK, 11(1): 373-388, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529444",
-            "keyword": [
-                "Polymers",
-                "metals",
-                "plastics",
-                "Elemental Finger Print"
-            ],
             "contactPoint": {
                 "fn": "Souhail Al-Abed",
                 "hasEmail": "mailto:al-abed.souhail@epa.gov"
             },
+            "description": "This research contains new data expanding the realm of nanoplastics that can be followed based on their metallic signatures to all kinds of plastics. Additionally, this study illustrates the importance of nanoplastics as a source of metals and metal-bearing nanoparticles in the environment. \n\nThis dataset is associated with the following publication:\nBaalousha, M., J. Wang, M.M. Nabi, M. Alam, M. Erfani, J. Gigault, F. Blancho, M. Davranche, P.M. Potter, and S.R. Al-Abed. The elemental fingerprint as a potential tool for tracking the fate of real-life model nanoplastics generated from plastic consumer products in environmental systems.   Environmental Science: Nano. Royal Society of Chemistry, Cambridge,  UK, 11(1): 373-388, (2024).",
             "distribution": [
                 {
-                    "title": "icpTOF11.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF11.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF11.csv"
                 },
                 {
-                    "title": "icpTOF10.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF10.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF10.csv"
                 },
                 {
-                    "title": "icpTOF9.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF9.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF9.csv"
                 },
                 {
-                    "title": "icpTOF8.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF8.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF8.csv"
                 },
                 {
-                    "title": "icpTOF7.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF7.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF7.csv"
                 },
                 {
-                    "title": "icpTOF6.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF6.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF6.csv"
                 },
                 {
-                    "title": "icpTOF5.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF5.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF5.csv"
                 },
                 {
-                    "title": "icpTOF4.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF4.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF4.csv"
                 },
                 {
-                    "title": "icpTOF3.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF3.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF3.csv"
                 },
                 {
-                    "title": "icpTOF2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF2.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF2.csv"
                 },
                 {
-                    "title": "icpTOF2 - Copy.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF2%20-%20Copy.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF2 - Copy.csv"
                 },
                 {
-                    "title": "icpTOF1.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/icpTOF1.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "icpTOF1.csv"
                 },
                 {
-                    "title": "Density.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/Density.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Density.csv"
                 },
                 {
-                    "title": "Density - Copy.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/Density%20-%20Copy.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Density - Copy.csv"
                 },
                 {
-                    "title": "Conversion.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/Conversion.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Conversion.csv"
                 },
                 {
-                    "title": "Conversion - Copy.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/Conversion%20-%20Copy.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Conversion - Copy.csv"
                 },
                 {
-                    "title": "Nanoplastics total metal concentrations.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/Nanoplastics%20total%20metal%20concentrations.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Nanoplastics total metal concentrations.xlsx"
                 },
                 {
-                    "title": "EPA plastics total metal concentrations.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529444/EPA%20plastics%20total%20metal%20concentrations.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA plastics total metal concentrations.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529444",
+            "keyword": [
+                "Polymers",
+                "metals",
+                "plastics",
+                "Elemental Finger Print"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-22",
-            "references": [
-                "https://doi.org/10.1039/d3en00559c",
-                "https://pasteur.epa.gov/uploads/10.23719/1529444/documents/EPA%20plastics%20total%20metal%20concentrations.xlsx",
-                "https://pasteur.epa.gov/uploads/10.23719/1529444/documents/Nanoplastics%20total%20metal%20concentrations.xlsx"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190729,43 +190721,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d3en00559c",
+                "https://pasteur.epa.gov/uploads/10.23719/1529444/documents/EPA%20plastics%20total%20metal%20concentrations.xlsx",
+                "https://pasteur.epa.gov/uploads/10.23719/1529444/documents/Nanoplastics%20total%20metal%20concentrations.xlsx"
+            ],
+            "rights": null,
+            "title": "Elemental fingerprint as a potential tool for tracking the fate of real-life model nanoplastics generated from plastic consumer products in environmental systems"
         },
         {
-            "title": "FASEB J Ozone HFD",
-            "description": "Data from Prenatal ozone exposure programs a sexually dimorphic susceptibility to high fat diet in adolescent Long-Evans rats. \n\nThis dataset is associated with the following publication:\nStewart, E., J. Dye, M. Schladweiler, P. Phillips, K. McDaniel, J. Richards, R. Grindstaff, W. Padgett, M. Moore, D. Jenkins-Hill, C. Gordon, U. Kodavanti, and C. Miller. Prenatal ozone exposure programs a sexually dimorphic susceptibility to high fat diet in adolescent Long-Evans rats..   FASEB JOURNAL. Federation of American Societies for Experimental Biology (FASEB), Bethesda, MD, USA, 36(12): e22664, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530056",
-            "keyword": [
-                "Susceptibility",
-                "Prenatal Exposure",
-                "Ozone",
-                "Metabolic Disease",
-                "Children's Environmental Health"
-            ],
             "contactPoint": {
                 "fn": "Colette Miller",
                 "hasEmail": "mailto:miller.colette@epa.gov"
             },
+            "description": "Data from Prenatal ozone exposure programs a sexually dimorphic susceptibility to high fat diet in adolescent Long-Evans rats. \n\nThis dataset is associated with the following publication:\nStewart, E., J. Dye, M. Schladweiler, P. Phillips, K. McDaniel, J. Richards, R. Grindstaff, W. Padgett, M. Moore, D. Jenkins-Hill, C. Gordon, U. Kodavanti, and C. Miller. Prenatal ozone exposure programs a sexually dimorphic susceptibility to high fat diet in adolescent Long-Evans rats..   FASEB JOURNAL. Federation of American Societies for Experimental Biology (FASEB), Bethesda, MD, USA, 36(12): e22664, (2022).",
             "distribution": [
                 {
-                    "title": "Offspring Data for SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530056/Offspring%20Data%20for%20SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Offspring Data for SciHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530056",
+            "keyword": [
+                "Susceptibility",
+                "Prenatal Exposure",
+                "Ozone",
+                "Metabolic Disease",
+                "Children's Environmental Health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-30",
-            "references": [
-                "https://doi.org/10.1096/fj.202201514r",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10010258"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190775,34 +190768,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1096/fj.202201514r",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10010258"
+            ],
+            "rights": null,
+            "title": "FASEB J Ozone HFD"
         },
         {
-            "title": "Birth Defects Metadata 2021",
-            "description": "This dataset describes birth outcomes (weight, gestational age, sex assigned at birth, presence of birth defects, etc.) and parental factors (age, address, health status, etc.) for people born in North Carolina between 2003 and 2015. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Data come from the North Carolina Birth Defects Monitoring Program. These data are not publicly available, but more information can be obtained at https://schs.dph.ncdhhs.gov/units/bdmp/ (accessed 11/9/2021). Format: Data are stored as csv files and contain information on birth records in North Carolina from 2003 to 2015, including addresses of parents and medical information on parents and neonates. \n\nThis dataset is associated with the following publication:\nSlawsky, E., A. Weaver, T. Luben, and K. Rappazzo. A Cross-sectional Study of Brownfields and Birth Defects.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA, 114(5-6): 197-207, (2022).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Anne Weaver",
+                "hasEmail": "mailto:weaver.anne@epa.gov"
+            },
+            "description": "This dataset describes birth outcomes (weight, gestational age, sex assigned at birth, presence of birth defects, etc.) and parental factors (age, address, health status, etc.) for people born in North Carolina between 2003 and 2015. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Data come from the North Carolina Birth Defects Monitoring Program. These data are not publicly available, but more information can be obtained at https://schs.dph.ncdhhs.gov/units/bdmp/ (accessed 11/9/2021). Format: Data are stored as csv files and contain information on birth records in North Carolina from 2003 to 2015, including addresses of parents and medical information on parents and neonates. \n\nThis dataset is associated with the following publication:\nSlawsky, E., A. Weaver, T. Luben, and K. Rappazzo. A Cross-sectional Study of Brownfields and Birth Defects.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA, 114(5-6): 197-207, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1524239",
             "keyword": [
                 "Birth Defects",
                 "birth records",
                 "North Carolina"
             ],
-            "contactPoint": {
-                "fn": "Anne Weaver",
-                "hasEmail": "mailto:weaver.anne@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-11-01",
-            "references": [
-                "https://doi.org/10.1002/bdr2.1992"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190812,53 +190806,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/bdr2.1992"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Birth Defects Metadata 2021"
         },
         {
-            "title": "Combining in vitro and in silico New Approach Methods to investigate type 3 iodothyronine deiodinase chemical inhibition across species",
-            "description": "Dataset for \"Combining in vitro and in silico New Approach Methods to investigate type 3 iodothyronine deiodinase chemical inhibition across species\". \n\nThis dataset is associated with the following publication:\nMayasich, S., M. Goldsmith, K. Mattingly, and C. Lalone. Combining In Vitro and In Silico New Approach Methods to Investigate Type 3 Iodothyronine Deiodinase Chemical Inhibition Across Species.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(5): 1032-1048, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528341",
-            "keyword": [
-                "Cross species extrapolation",
-                "Androgen receptor",
-                "weight of evidence",
-                "Systematic Literature Review",
-                "endocrine disrupting chemicals",
-                "Computational Analysis"
-            ],
             "contactPoint": {
                 "fn": "Carlie LaLone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Dataset for \"Combining in vitro and in silico New Approach Methods to investigate type 3 iodothyronine deiodinase chemical inhibition across species\". \n\nThis dataset is associated with the following publication:\nMayasich, S., M. Goldsmith, K. Mattingly, and C. Lalone. Combining In Vitro and In Silico New Approach Methods to Investigate Type 3 Iodothyronine Deiodinase Chemical Inhibition Across Species.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(5): 1032-1048, (2023).",
             "distribution": [
                 {
-                    "title": "SupportingInfo_Molecular Model pdb files.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528341/SupportingInfo_Molecular%20Model%20pdb%20files.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "SupportingInfo_Molecular Model pdb files.zip"
                 },
                 {
-                    "title": "hDIO3 SDM Full database SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528341/hDIO3%20SDM%20Full%20database%20SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "hDIO3 SDM Full database SciHub.xlsx"
                 },
                 {
-                    "title": "Data Dictionary hDIO3 SDM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528341/Data%20Dictionary%20hDIO3%20SDM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Dictionary hDIO3 SDM.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528341",
+            "keyword": [
+                "Cross species extrapolation",
+                "Androgen receptor",
+                "weight of evidence",
+                "Systematic Literature Review",
+                "endocrine disrupting chemicals",
+                "Computational Analysis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-13",
-            "references": [
-                "https://doi.org/10.1002/etc.5591"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190868,19 +190862,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5591"
+            ],
+            "rights": null,
+            "title": "Combining in vitro and in silico New Approach Methods to investigate type 3 iodothyronine deiodinase chemical inhibition across species"
         },
         {
-            "title": "Saunders et al. Amended IVIVE model",
-            "description": "This paper described development of an in vitro/in vivo model that accounts for first pass clearance effects.  The model details are contained in the supporting information for the paper. \n\nThis dataset is associated with the following publication:\nSaunders, L., J. Nichols, J.A. Arnot, J. Armitage, and F. Wania. An amended in vitro\u2013in vivo extrapolation model that accounts for first pass clearance effects on chemical bioaccumulation in fish.   Environmental Science: Processes & Impacts. Royal Society of Chemistry, Cambridge,  UK, 25(4): 741-754, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "David Mount",
+                "hasEmail": "mailto:mount.dave@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1528369/documents/Saunders%20et%20al.%20ScienceHub%20entry_amended%20IVIVE%20model.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This paper described development of an in vitro/in vivo model that accounts for first pass clearance effects.  The model details are contained in the supporting information for the paper. \n\nThis dataset is associated with the following publication:\nSaunders, L., J. Nichols, J.A. Arnot, J. Armitage, and F. Wania. An amended in vitro\u2013in vivo extrapolation model that accounts for first pass clearance effects on chemical bioaccumulation in fish.   Environmental Science: Processes & Impacts. Royal Society of Chemistry, Cambridge,  UK, 25(4): 741-754, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528369/Saunders%20et%20al.%20ScienceHub%20entry_amended%20IVIVE%20model.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Saunders et al. ScienceHub entry_amended IVIVE model.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528369",
             "keyword": [
@@ -190891,21 +190897,10 @@
                 "bioaccumulation",
                 "rainbow trout"
             ],
-            "contactPoint": {
-                "fn": "David Mount",
-                "hasEmail": "mailto:mount.dave@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Saunders et al. ScienceHub entry_amended IVIVE model.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528369/Saunders%20et%20al.%20ScienceHub%20entry_amended%20IVIVE%20model.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-02-09",
-            "references": [
-                "https://doi.org/10.1039/d2em00522k",
-                "https://pasteur.epa.gov/uploads/10.23719/1528369/documents/Saunders%20et%20al.%20ScienceHub%20entry_amended%20IVIVE%20model.xlsx"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190916,40 +190911,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1528369/documents/Saunders%20et%20al.%20ScienceHub%20entry_amended%20IVIVE%20model.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1039/d2em00522k",
+                "https://pasteur.epa.gov/uploads/10.23719/1528369/documents/Saunders%20et%20al.%20ScienceHub%20entry_amended%20IVIVE%20model.xlsx"
+            ],
+            "rights": null,
+            "title": "Saunders et al. Amended IVIVE model"
         },
         {
-            "title": "Lightning Assimilation WRF Data",
-            "description": "The immediate data, except the lightning flash data behind the figures,\nare available from https://doi.org/10.5281/zenodo.6493145 ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526408",
-            "keyword": [
-                "WRF",
-                "air quality",
-                "lightning assimilation"
-            ],
             "contactPoint": {
                 "fn": "Daiwen Kang",
                 "hasEmail": "mailto:kang.daiwen@epa.gov"
             },
+            "description": "The immediate data, except the lightning flash data behind the figures,\nare available from https://doi.org/10.5281/zenodo.6493145 ",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.5281/zenodo.6493145",
-                    "accessURL": "https://doi.org/10.5281/zenodo.6493145"
+                    "accessURL": "https://doi.org/10.5281/zenodo.6493145",
+                    "title": "https://doi.org/10.5281/zenodo.6493145"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526408",
+            "keyword": [
+                "WRF",
+                "air quality",
+                "lightning assimilation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-07",
-            "references": [
-                "https://zenodo.org/record/6493145"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -190959,19 +190953,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://zenodo.org/record/6493145"
+            ],
+            "rights": null,
+            "title": "Lightning Assimilation WRF Data"
         },
         {
-            "title": "Increased endocrine activity of xenobiotic chemicals as mediated by metabolic activation - data set",
-            "description": "Data set to support the manuscript \"Increased endocrine activity of xenobiotic chemicals as mediated by metabolic activation\". Contains analytical measurement of metabolites, binding potential to the estrogen receptor, and gene activation to vitellogenin induction in the rainbow trout assays. Chemicals of interest in this study were phenolphthalein, phenolphthalin, and 4,4\u2019-methylenedianiline. \n\nThis dataset is associated with the following publication:\nKolanczyk, R., J. Denny, B. Sheedy, V. Olson, J. Serrano, and M. Tapper. Increased Endocrine Activity of Xenobiotic Chemicals as Mediated by Metabolic Activation..   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(12): 2747-2757, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Richard Kolanczyk",
+                "hasEmail": "mailto:kolanczyk.rick@epa.gov"
+            },
+            "description": "Data set to support the manuscript \"Increased endocrine activity of xenobiotic chemicals as mediated by metabolic activation\". Contains analytical measurement of metabolites, binding potential to the estrogen receptor, and gene activation to vitellogenin induction in the rainbow trout assays. Chemicals of interest in this study were phenolphthalein, phenolphthalin, and 4,4\u2019-methylenedianiline. \n\nThis dataset is associated with the following publication:\nKolanczyk, R., J. Denny, B. Sheedy, V. Olson, J. Serrano, and M. Tapper. Increased Endocrine Activity of Xenobiotic Chemicals as Mediated by Metabolic Activation..   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(12): 2747-2757, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529119/ER%20Metabolism_data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ER Metabolism_data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529119",
             "keyword": [
@@ -190982,20 +190986,10 @@
                 "estrogen receptor",
                 "phenolphthalin"
             ],
-            "contactPoint": {
-                "fn": "Richard Kolanczyk",
-                "hasEmail": "mailto:kolanczyk.rick@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ER Metabolism_data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529119/ER%20Metabolism_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-06",
-            "references": [
-                "https://doi.org/10.1002/etc.5748"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191005,55 +190999,55 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5748"
+            ],
+            "rights": null,
+            "title": "Increased endocrine activity of xenobiotic chemicals as mediated by metabolic activation - data set"
         },
         {
-            "title": "Dataset and code for cross species applicability of an AOP network for thyroid hormone system disruption",
-            "description": "The data set consists of the following:\n1) AOP-Wiki xml downloads from March 2022 used in constructing and evaluating the AOP network.\n2) A literature database containing all literature that was cited in the main document. The database also contains additional references that were not explicitly cited in the associated manuscript.\n3) R code used for the analyses and visualizations\n4) Detailed results from the SeqAPASS tool. \n\nThis dataset is associated with the following publication:\nHaigis, A., L. Vergauwen, C. LaLone, D. Villeneuve, J. O'Brien, and D. Knapen. Cross-species applicability of an adverse outcome pathway network for thyroid hormone system disruption.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  195(1): 1-27, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529155",
-            "keyword": [
-                "endocrine disruption",
-                "thyroid",
-                "Adverse Outcome Pathways (AOPs)",
-                "cross-species extrapolation"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "The data set consists of the following:\n1) AOP-Wiki xml downloads from March 2022 used in constructing and evaluating the AOP network.\n2) A literature database containing all literature that was cited in the main document. The database also contains additional references that were not explicitly cited in the associated manuscript.\n3) R code used for the analyses and visualizations\n4) Detailed results from the SeqAPASS tool. \n\nThis dataset is associated with the following publication:\nHaigis, A., L. Vergauwen, C. LaLone, D. Villeneuve, J. O'Brien, and D. Knapen. Cross-species applicability of an adverse outcome pathway network for thyroid hormone system disruption.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  195(1): 1-27, (2023).",
             "distribution": [
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/6495afabe4b08a6b394f8bf2?space=62e913afe4b055edffc06b16",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/6495afabe4b08a6b394f8bf2?space=62e913afe4b055edffc06b16"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/6495afabe4b08a6b394f8bf2?space=62e913afe4b055edffc06b16",
+                    "title": "https://clowder.edap-cluster.com/datasets/6495afabe4b08a6b394f8bf2?space=62e913afe4b055edffc06b16"
                 },
                 {
-                    "title": "SeqAPASS-details.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529155/SeqAPASS-details.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SeqAPASS-details.xlsx"
                 },
                 {
-                    "title": "R-files.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529155/R-files.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "R-files.zip"
                 },
                 {
-                    "title": "literature-database.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529155/literature-database.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "literature-database.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529155",
+            "keyword": [
+                "endocrine disruption",
+                "thyroid",
+                "Adverse Outcome Pathways (AOPs)",
+                "cross-species extrapolation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-23",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfad063"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191063,49 +191057,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfad063"
+            ],
+            "rights": null,
+            "title": "Dataset and code for cross species applicability of an AOP network for thyroid hormone system disruption"
         },
         {
-            "title": "Cross-species comparison of chemical inhibition of human and Xenopus iodotyrosine deiodinase",
-            "description": "Supplementary materials for \"Olker JH, Korte JJ, Haselman JT, Hornung MW, Degitz SJ. Cross-species comparison of chemical inhibition of human and Xenopus iodotyrosine deiodinase. Aquat Toxicol. 2022 Aug;249:106227. doi: 10.1016/j.aquatox.2022.106227. Epub 2022 Jun 15. PMID: 35767922; PMCID: PMC9887787.\"\n\nThe excel spreadsheet contains the resultant data from an assay for chemical inhibition of amphibian Iodotyrosine Deiodinase (IYD) enzyme activity. 154 chemicals from the EPA\u2019s ToxCast chemical library were tested in concentration-response and these amphibian IYD assay results were compared to those from the human IYD inhibition assay reported in Olker et al. 2021 (doi:10.1016/j.tiv.2020.105073). The same set of 154 chemicals were tested in both assays and compared here. This data set the median, minimum, and maximum inhibition produced at each concentration for each tested chemical. A model inhibitor (3-Nitro-L-Tyrosine) was included on each plate as a positive control, with concentration response data for those curves also included in the data set. \n\nThis dataset is associated with the following publication:\nOlker, J., J. Korte, J. Haselman, M. Hornung, and S. Degitz. Xenopus laevis and Human iodotyrosine deiodinase enzyme cross-species sensitivity to inhibition by ToxCast chemicals..   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 249: N/A, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530078",
-            "keyword": [
-                "endocrine disruption",
-                "amphibian",
-                "iodotyrosine deiodinase",
-                "Xenopus",
-                "screening",
-                "thyroid"
-            ],
             "contactPoint": {
                 "fn": "Jennifer Olker",
                 "hasEmail": "mailto:olker.jennifer@epa.gov"
             },
+            "description": "Supplementary materials for \"Olker JH, Korte JJ, Haselman JT, Hornung MW, Degitz SJ. Cross-species comparison of chemical inhibition of human and Xenopus iodotyrosine deiodinase. Aquat Toxicol. 2022 Aug;249:106227. doi: 10.1016/j.aquatox.2022.106227. Epub 2022 Jun 15. PMID: 35767922; PMCID: PMC9887787.\"\n\nThe excel spreadsheet contains the resultant data from an assay for chemical inhibition of amphibian Iodotyrosine Deiodinase (IYD) enzyme activity. 154 chemicals from the EPA\u2019s ToxCast chemical library were tested in concentration-response and these amphibian IYD assay results were compared to those from the human IYD inhibition assay reported in Olker et al. 2021 (doi:10.1016/j.tiv.2020.105073). The same set of 154 chemicals were tested in both assays and compared here. This data set the median, minimum, and maximum inhibition produced at each concentration for each tested chemical. A model inhibitor (3-Nitro-L-Tyrosine) was included on each plate as a positive control, with concentration response data for those curves also included in the data set. \n\nThis dataset is associated with the following publication:\nOlker, J., J. Korte, J. Haselman, M. Hornung, and S. Degitz. Xenopus laevis and Human iodotyrosine deiodinase enzyme cross-species sensitivity to inhibition by ToxCast chemicals..   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 249: N/A, (2022).",
             "distribution": [
                 {
-                    "title": "Appendix A - Supplementary Data.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530078/Appendix%20A%20-%20Supplementary%20Data.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Appendix A - Supplementary Data.pdf"
                 },
                 {
-                    "title": "Olker_et_al_IYD_in vitro Species Comp_210709.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530078/Olker_et_al_IYD_in%20vitro%20Species%20Comp_210709.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Olker_et_al_IYD_in vitro Species Comp_210709.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530078",
+            "keyword": [
+                "endocrine disruption",
+                "amphibian",
+                "iodotyrosine deiodinase",
+                "Xenopus",
+                "screening",
+                "thyroid"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-14",
-            "references": [
-                "https://doi.org/10.1016/j.aquatox.2022.106227",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9887787"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191115,50 +191108,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.aquatox.2022.106227",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9887787"
+            ],
+            "rights": null,
+            "title": "Cross-species comparison of chemical inhibition of human and Xenopus iodotyrosine deiodinase"
         },
         {
-            "title": "Density declines, richness increases, and composition shifts in stream macroinvertebrates",
-            "description": "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Datasets and code for analyses and generation of figures are available via FigShare (doi: 10.6084/m9.figshare.22266046) and a public GitHub repository (https://github.com/rumschsl/MacroBiodivTrends). \n\nThis dataset is associated with the following publication:\nRumschlag, S., M. Mahon, D. Jones, W. Battaglin, J. Behrens, E. Bernhardt, P. Bradley, E. Brown, F. De Laender, R. Hill, S. Kunz, S. Lee, E. Rosi, R. Schafer, T. Schmidt, M. Simonin, K. Smalling, K. Voss, and J. Rohr. Density declines, richness increases, and composition shifts in stream macroinvertebrates.   Science Advances. American Association for the Advancement of Science (AAAS), Washington, DC, USA, 9(18): eadf4896, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530081",
-            "keyword": [
-                "stream macroinvertebrates",
-                "composition shifts",
-                "biomonitoring",
-                "biodiversity"
-            ],
             "contactPoint": {
                 "fn": "Samantha Rumschlag",
                 "hasEmail": "mailto:rumschlag.samantha@epa.gov"
             },
+            "description": "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Datasets and code for analyses and generation of figures are available via FigShare (doi: 10.6084/m9.figshare.22266046) and a public GitHub repository (https://github.com/rumschsl/MacroBiodivTrends). \n\nThis dataset is associated with the following publication:\nRumschlag, S., M. Mahon, D. Jones, W. Battaglin, J. Behrens, E. Bernhardt, P. Bradley, E. Brown, F. De Laender, R. Hill, S. Kunz, S. Lee, E. Rosi, R. Schafer, T. Schmidt, M. Simonin, K. Smalling, K. Voss, and J. Rohr. Density declines, richness increases, and composition shifts in stream macroinvertebrates.   Science Advances. American Association for the Advancement of Science (AAAS), Washington, DC, USA, 9(18): eadf4896, (2023).",
             "distribution": [
                 {
-                    "title": "Supplementary Materials.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530081/Supplementary%20Materials.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supplementary Materials.pdf"
                 },
                 {
-                    "title": "https://doi.org/10.6084/m9.figshare.22266046.v1",
-                    "accessURL": "https://doi.org/10.6084/m9.figshare.22266046.v1"
+                    "accessURL": "https://doi.org/10.6084/m9.figshare.22266046.v1",
+                    "title": "https://doi.org/10.6084/m9.figshare.22266046.v1"
                 },
                 {
-                    "title": "https://github.com/rumschsl/MacroBiodivTrends",
-                    "accessURL": "https://github.com/rumschsl/MacroBiodivTrends"
+                    "accessURL": "https://github.com/rumschsl/MacroBiodivTrends",
+                    "title": "https://github.com/rumschsl/MacroBiodivTrends"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530081",
+            "keyword": [
+                "stream macroinvertebrates",
+                "composition shifts",
+                "biomonitoring",
+                "biodiversity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-03",
-            "references": [
-                "https://doi.org/10.1126/sciadv.adf4896",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10156106"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191168,20 +191161,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.adf4896",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10156106"
+            ],
+            "rights": null,
+            "title": "Density declines, richness increases, and composition shifts in stream macroinvertebrates"
         },
         {
-            "title": "Indicators for Assessing Community and Contaminated Site Vulnerability to Extreme Events",
-            "description": "The indicators (non-EPA owned, yet described in the Handbook and Manuscript) represent: 1) potential exposures due to extreme events (heat, floods, drought, and wildfire), 2) specific sources of contaminant releases (the different types of sites/waste facilities), 3) contaminant fate and transport (through water and wind), and 4) population sensitivity characteristics (demographics, socioeconomic conditions, existing health conditions) that indicate which individuals in the community may be impacted more by extreme events. The geospatial indicator data layers are at the Block Group level (U.S. Census Bureau, 2022), and each Block Group is considered to be a \u201ccommunity\u201d. This dataset is not publicly accessible because: The indicator data are from external co-authors collected solely from coauthor resources. The indicator data were all generated using publicly available data sources, as documented in the External Review Draft of Handbook (research product attached). It can be accessed through the following means: This data can be accessed by contacting the external lead author on the Handbook and Manuscript (Dr. Paramita Sinha, RTI), who can provide all of the indicator data layers and associated metadata documentation. Format: The indicator data are from external co-authors collected solely from co-author resources. The format of the indicator data are geospatial data layers (e.g., Shapefiles, NetCDFs) with daily/hourly temporal resolution and Census Block Group level spatial resolution. There are over 250 individual geospatial data files which would be too large to upload and store. The data are already available from public data sources, as documented in the External Review Draft of Handbook. \n\nThis dataset is associated with the following publications:\nSinha, P., R. Truesdale, M. Fry, and S. Julius. Handbook on Indicators of Community Vulnerability to Extreme Events: Considering Sites and Waste Management Facilities. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.\nSinha, P., S. Julius, M. Fry, R. Truesdale, J. Cajka, M. Eddy , P. Doraiswamya, and D. Womacka. Assessing community vulnerability to extreme events in the presence of contaminated sites and waste management facilities: An indicator approach.   Urban Climate. Elsevier Science, New York, NY,   53(101800): 1-30, (2024).",
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
+                "fn": "Meridith Fry",
+                "hasEmail": "mailto:fry.meridith@epa.gov"
+            },
+            "description": "The indicators (non-EPA owned, yet described in the Handbook and Manuscript) represent: 1) potential exposures due to extreme events (heat, floods, drought, and wildfire), 2) specific sources of contaminant releases (the different types of sites/waste facilities), 3) contaminant fate and transport (through water and wind), and 4) population sensitivity characteristics (demographics, socioeconomic conditions, existing health conditions) that indicate which individuals in the community may be impacted more by extreme events. The geospatial indicator data layers are at the Block Group level (U.S. Census Bureau, 2022), and each Block Group is considered to be a \u201ccommunity\u201d. This dataset is not publicly accessible because: The indicator data are from external co-authors collected solely from coauthor resources. The indicator data were all generated using publicly available data sources, as documented in the External Review Draft of Handbook (research product attached). It can be accessed through the following means: This data can be accessed by contacting the external lead author on the Handbook and Manuscript (Dr. Paramita Sinha, RTI), who can provide all of the indicator data layers and associated metadata documentation. Format: The indicator data are from external co-authors collected solely from co-author resources. The format of the indicator data are geospatial data layers (e.g., Shapefiles, NetCDFs) with daily/hourly temporal resolution and Census Block Group level spatial resolution. There are over 250 individual geospatial data files which would be too large to upload and store. The data are already available from public data sources, as documented in the External Review Draft of Handbook. \n\nThis dataset is associated with the following publications:\nSinha, P., R. Truesdale, M. Fry, and S. Julius. Handbook on Indicators of Community Vulnerability to Extreme Events: Considering Sites and Waste Management Facilities. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.\nSinha, P., S. Julius, M. Fry, R. Truesdale, J. Cajka, M. Eddy , P. Doraiswamya, and D. Womacka. Assessing community vulnerability to extreme events in the presence of contaminated sites and waste management facilities: An indicator approach.   Urban Climate. Elsevier Science, New York, NY,   53(101800): 1-30, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1528291",
             "keyword": [
                 "climate change",
@@ -191189,15 +191187,10 @@
                 "Vulnerability",
                 "Disadvantaged Community"
             ],
-            "contactPoint": {
-                "fn": "Meridith Fry",
-                "hasEmail": "mailto:fry.meridith@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-07-27",
-            "references": [
-                "https://www.epa.gov/research",
-                "https://doi.org/10.1016/j.uclim.2023.101800"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191207,48 +191200,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.epa.gov/research",
+                "https://doi.org/10.1016/j.uclim.2023.101800"
+            ],
+            "rights": null,
+            "title": "Indicators for Assessing Community and Contaminated Site Vulnerability to Extreme Events"
         },
         {
-            "title": "Towards a framework for invasive aquatic plant survey design in Great Lakes coastal areas",
-            "description": "Supplementary files for \"Tucker AJ, Annis G, Elgin E, Chadderton WL, Hoffman J. Towards a framework for invasive aquatic plant survey design in Great Lakes coastal areas. Manag Biol Invasion. 2022 Feb 4;13(1):45-67. doi: 10.3391/mbi.2022.13.1.03. PMID: 35664708; PMCID: PMC9157784.\". \n\nThis dataset is associated with the following publication:\nTucker, A., G. Annis, E. Elgin, L. Chadderton, and J. Hoffman. Towards a framework for invasive aquatic plant survey design in Great Lakes coastal areas.   Management of Biological Invasions. Regional Euro-Asian Biological Invasions Centre, Helsinki,  FINLAND,  45-67, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530058",
-            "keyword": [
-                "aquatic macrophytes",
-                "early detection",
-                "monitoring",
-                "rarefaction",
-                "surveillance"
-            ],
             "contactPoint": {
                 "fn": "Joel Hoffman",
                 "hasEmail": "mailto:hoffman.joel@epa.gov"
             },
+            "description": "Supplementary files for \"Tucker AJ, Annis G, Elgin E, Chadderton WL, Hoffman J. Towards a framework for invasive aquatic plant survey design in Great Lakes coastal areas. Manag Biol Invasion. 2022 Feb 4;13(1):45-67. doi: 10.3391/mbi.2022.13.1.03. PMID: 35664708; PMCID: PMC9157784.\". \n\nThis dataset is associated with the following publication:\nTucker, A., G. Annis, E. Elgin, L. Chadderton, and J. Hoffman. Towards a framework for invasive aquatic plant survey design in Great Lakes coastal areas.   Management of Biological Invasions. Regional Euro-Asian Biological Invasions Centre, Helsinki,  FINLAND,  45-67, (2022).",
             "distribution": [
                 {
-                    "title": "MBI_2022_Tucker_etal_SupplementaryTables.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530058/MBI_2022_Tucker_etal_SupplementaryTables.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MBI_2022_Tucker_etal_SupplementaryTables.xlsx"
                 },
                 {
-                    "title": "MBI_2022_Tucker_etal_SupplementaryFigures.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530058/MBI_2022_Tucker_etal_SupplementaryFigures.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "MBI_2022_Tucker_etal_SupplementaryFigures.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530058",
+            "keyword": [
+                "aquatic macrophytes",
+                "early detection",
+                "monitoring",
+                "rarefaction",
+                "surveillance"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-02-04",
-            "references": [
-                "https://doi.org/10.3391/mbi.2022.13.1.03",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9157784"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191258,41 +191251,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3391/mbi.2022.13.1.03",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9157784"
+            ],
+            "rights": null,
+            "title": "Towards a framework for invasive aquatic plant survey design in Great Lakes coastal areas"
         },
         {
-            "title": "National-Scale Assessment of Total Gaseous Mercury Isotopes Across the United States",
-            "description": "Data for \"Tate, M. T., Janssen, S. E., Lepak, R. F., Flucke, L., & Krabbenhoft, D. P. (2023). National-scale assessment of total gaseous mercury isotopes across the United States. Journal of Geophysical Research: Atmospheres, 128, e2022JD038276. https://doi.org/10.1029/2022JD038276\". \n\nThis dataset is associated with the following publication:\nTate, M., S. Janssen, R. Lepak, L. Fluke, and D. Krabbenhoft. Assessment and Application of an Active Total Gaseous Mercury Collector to Survey Mercury Sources Across the United States.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA, 128(8): N/A, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530079",
-            "keyword": [
-                "mercury",
-                "mercury isotopes",
-                "United States",
-                "Point source"
-            ],
             "contactPoint": {
                 "fn": "Ryan Lepak",
                 "hasEmail": "mailto:lepak.ryan@epa.gov"
             },
+            "description": "Data for \"Tate, M. T., Janssen, S. E., Lepak, R. F., Flucke, L., & Krabbenhoft, D. P. (2023). National-scale assessment of total gaseous mercury isotopes across the United States. Journal of Geophysical Research: Atmospheres, 128, e2022JD038276. https://doi.org/10.1029/2022JD038276\". \n\nThis dataset is associated with the following publication:\nTate, M., S. Janssen, R. Lepak, L. Fluke, and D. Krabbenhoft. Assessment and Application of an Active Total Gaseous Mercury Collector to Survey Mercury Sources Across the United States.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA, 128(8): N/A, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.sciencebase.gov/catalog/item/5d51e54de4b01d82ce8e205f",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/5d51e54de4b01d82ce8e205f"
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/5d51e54de4b01d82ce8e205f",
+                    "title": "https://www.sciencebase.gov/catalog/item/5d51e54de4b01d82ce8e205f"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530079",
+            "keyword": [
+                "mercury",
+                "mercury isotopes",
+                "United States",
+                "Point source"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-01",
-            "references": [
-                "https://doi.org/10.1029/2022jd038276",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10430761"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191302,51 +191295,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2022jd038276",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10430761"
+            ],
+            "rights": null,
+            "title": "National-Scale Assessment of Total Gaseous Mercury Isotopes Across the United States"
         },
         {
-            "title": "PFAS Biotransformation Pathways: A Species Comparison Study",
-            "description": "Data for \"Kolanczyk RC, Saley MR, Serrano JA, Daley SM, Tapper MA. PFAS Biotransformation Pathways: A Species Comparison Study. Toxics. 2023 Jan 12;11(1):74. doi: 10.3390/toxics11010074. PMID: 36668800; PMCID: PMC9862377.\". \n\nThis dataset is associated with the following publication:\nKolanczyk, R., M. Saley, J. Serrano, S. Daley, and M. Tapper. PFAS Biotransformation Pathways: A Species Comparison Study.   Toxics. MDPI, Basel,  SWITZERLAND, 11(1): 74, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529952",
-            "keyword": [
-                "biotransformation",
-                "Comparison",
-                "PFAS",
-                "pathway",
-                "Biodegradation",
-                "fish",
-                "Metabolism",
-                "MetaPath"
-            ],
             "contactPoint": {
                 "fn": "Richard Kolanczyk",
                 "hasEmail": "mailto:kolanczyk.rick@epa.gov"
             },
+            "description": "Data for \"Kolanczyk RC, Saley MR, Serrano JA, Daley SM, Tapper MA. PFAS Biotransformation Pathways: A Species Comparison Study. Toxics. 2023 Jan 12;11(1):74. doi: 10.3390/toxics11010074. PMID: 36668800; PMCID: PMC9862377.\". \n\nThis dataset is associated with the following publication:\nKolanczyk, R., M. Saley, J. Serrano, S. Daley, and M. Tapper. PFAS Biotransformation Pathways: A Species Comparison Study.   Toxics. MDPI, Basel,  SWITZERLAND, 11(1): 74, (2023).",
             "distribution": [
                 {
-                    "title": "PFAS OPEN LIT_2022_v.3.4.0.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529952/PFAS%20OPEN%20LIT_2022_v.3.4.0.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "PFAS OPEN LIT_2022_v.3.4.0.zip"
                 },
                 {
-                    "title": "PFAS OPEN LIT_2022_v.3.3.1.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529952/PFAS%20OPEN%20LIT_2022_v.3.3.1.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "PFAS OPEN LIT_2022_v.3.3.1.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529952",
+            "keyword": [
+                "biotransformation",
+                "Comparison",
+                "PFAS",
+                "pathway",
+                "Biodegradation",
+                "fish",
+                "Metabolism",
+                "MetaPath"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-07",
-            "references": [
-                "https://doi.org/10.3390/toxics11010074",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9862377"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191356,42 +191349,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxics11010074",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9862377"
+            ],
+            "rights": null,
+            "title": "PFAS Biotransformation Pathways: A Species Comparison Study"
         },
         {
-            "title": "Can Preserved Museum Specimens Be Used to Reconstruct Fish Mercury Burden and Sources through Time?",
-            "description": "Supporting information for \"Ryan F. Lepak, Sarah E. Janssen, Jacob M. Ogorek, Casey B. Dillman, Joel C. Hoffman, Michael T. Tate, and Peter B. McIntyre\nEnvironmental Science & Technology Letters 2023 10 (2), 165-171\nDOI: 10.1021/acs.estlett.3c00009\". \n\nThis dataset is associated with the following publication:\nLepak, R., S. Janssen, J. Ogorek, C. Dillman, J. Hoffman, M. Tate, and P. McIntyre. Can Preserved Museum Specimens Be Used to Reconstruct Fish Mercury Burden and Sources through Time?.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA, 10(2): 165-171, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530087",
-            "keyword": [
-                "minamata convention",
-                "preserved fish",
-                "mercury isotopes",
-                "isotopes",
-                "museums"
-            ],
             "contactPoint": {
                 "fn": "Ryan Lepak",
                 "hasEmail": "mailto:lepak.ryan@epa.gov"
             },
+            "description": "Supporting information for \"Ryan F. Lepak, Sarah E. Janssen, Jacob M. Ogorek, Casey B. Dillman, Joel C. Hoffman, Michael T. Tate, and Peter B. McIntyre\nEnvironmental Science & Technology Letters 2023 10 (2), 165-171\nDOI: 10.1021/acs.estlett.3c00009\". \n\nThis dataset is associated with the following publication:\nLepak, R., S. Janssen, J. Ogorek, C. Dillman, J. Hoffman, M. Tate, and P. McIntyre. Can Preserved Museum Specimens Be Used to Reconstruct Fish Mercury Burden and Sources through Time?.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA, 10(2): 165-171, (2023).",
             "distribution": [
                 {
-                    "title": "Supporting Information.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530087/Supporting%20Information.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supporting Information.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530087",
+            "keyword": [
+                "minamata convention",
+                "preserved fish",
+                "mercury isotopes",
+                "isotopes",
+                "museums"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-01-30",
-            "references": [
-                "https://doi.org/10.1021/acs.estlett.3c00009"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191401,38 +191395,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.estlett.3c00009"
+            ],
+            "rights": null,
+            "title": "Can Preserved Museum Specimens Be Used to Reconstruct Fish Mercury Burden and Sources through Time?"
         },
         {
-            "title": "PFAS in vitro data set",
-            "description": "Results of single concentration and concentration response testing of 165 PFAS samples from the USEPA ToxCast chemical library in nine (9) thyroid relevant assays. Chemicals were first screened in single concentration ('Single Concentration' tab) and then those chemicals with 50% or greater activity were further tested in concentration-response mode ('Concentration Response' tab). \n\nThis dataset is associated with the following publication:\nDegitz, S., J. Olker, J. Denny, P. Degoey, P. Hartig, M. Cardon, S. Eytcheson, J. Haselman, S. Mayasich, and M. Hornung. In vitro screening of per- and polyfluorinated substances (PFAS) for interference with seven thyroid hormone system targets across nine assays.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 95: 105762, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528672",
-            "keyword": [
-                "PFAS"
-            ],
             "contactPoint": {
                 "fn": "Sigmund Degitz",
                 "hasEmail": "mailto:degitz.sigmund@epa.gov"
             },
+            "description": "Results of single concentration and concentration response testing of 165 PFAS samples from the USEPA ToxCast chemical library in nine (9) thyroid relevant assays. Chemicals were first screened in single concentration ('Single Concentration' tab) and then those chemicals with 50% or greater activity were further tested in concentration-response mode ('Concentration Response' tab). \n\nThis dataset is associated with the following publication:\nDegitz, S., J. Olker, J. Denny, P. Degoey, P. Hartig, M. Cardon, S. Eytcheson, J. Haselman, S. Mayasich, and M. Hornung. In vitro screening of per- and polyfluorinated substances (PFAS) for interference with seven thyroid hormone system targets across nine assays.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 95: 105762, (2024).",
             "distribution": [
                 {
-                    "title": "Degitz_Thyroid_PFAS screening_230203.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528672/Degitz_Thyroid_PFAS%20screening_230203.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Degitz_Thyroid_PFAS screening_230203.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528672",
+            "keyword": [
+                "PFAS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-02-03",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2023.105762"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191442,41 +191436,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2023.105762"
+            ],
+            "rights": null,
+            "title": "PFAS in vitro data set"
         },
         {
-            "title": "EPA-generated bioassay data for NEIA 2018 Agricultural Study",
-            "description": "Data file cotains EPA-generated bioassay data published as TABLE S6b. EPA BIOASSAY with manuscript. \n\nThis dataset is associated with the following publication:\nBradley, P., D. Kolpin, D. Thompson, K. Romanok, K. Smalling, S. Breitmeyer, D. Cwiertny, N. Evans, R.W. Field, M. Focazio, L. Freeman, C. Givens, J. Gray, G. Hager, M. Hladik, J. Hofmann, R. Jones, L. Kanagy, R. Lane, R.B. McCleskey, D. Medgyesi, E. Medlock Kakaley, S. Meppelink, M. Meyer, D. Stavreva, M. Ward, and M. Cardon. Juxtaposition of Intense Agriculture, Vulnerable Aquifers, and Mixed Chemical/Microbial Exposures in Private-Well Tapwater in Northeast Iowa.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 868: 161672, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530047",
-            "keyword": [
-                "tapwater",
-                "bioassay",
-                "estrogen",
-                "androgen"
-            ],
             "contactPoint": {
                 "fn": "Elizabeth Medlock Kakaley",
                 "hasEmail": "mailto:medlockkakaley.elizabeth@epa.gov"
             },
+            "description": "Data file cotains EPA-generated bioassay data published as TABLE S6b. EPA BIOASSAY with manuscript. \n\nThis dataset is associated with the following publication:\nBradley, P., D. Kolpin, D. Thompson, K. Romanok, K. Smalling, S. Breitmeyer, D. Cwiertny, N. Evans, R.W. Field, M. Focazio, L. Freeman, C. Givens, J. Gray, G. Hager, M. Hladik, J. Hofmann, R. Jones, L. Kanagy, R. Lane, R.B. McCleskey, D. Medgyesi, E. Medlock Kakaley, S. Meppelink, M. Meyer, D. Stavreva, M. Ward, and M. Cardon. Juxtaposition of Intense Agriculture, Vulnerable Aquifers, and Mixed Chemical/Microbial Exposures in Private-Well Tapwater in Northeast Iowa.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 868: 161672, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0048969723002875?via%3Dihub#s0080",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0048969723002875?via%3Dihub#s0080"
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0048969723002875?via%3Dihub#s0080",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0048969723002875?via%3Dihub#s0080"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530047",
+            "keyword": [
+                "tapwater",
+                "bioassay",
+                "estrogen",
+                "androgen"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-18",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.161672",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9976626"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191486,40 +191479,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.161672",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9976626"
+            ],
+            "rights": null,
+            "title": "EPA-generated bioassay data for NEIA 2018 Agricultural Study"
         },
         {
-            "title": "EPA-generated bioassay data for 2020 bottled water study",
-            "description": "EPA-generated bioassay data published with 2020 bottled water study manuscript. \n\nThis dataset is associated with the following publication:\nBradley, P., K. Romanok, K. Smalling, M. Focazio, N. Evans, S. Fitzpatrick, C. Givens, S. Gordon, J. Gray, E. Green, D. Griffin, M. Hladik, L. Kanagy, J. Lisle, K. Loftin, R.B. McCleskey, E. Medlock Kakaley, A. Navas-Acien, D. Roth, and C. Weis. Bottled Water Contaminant Exposures and Predicted Human Effects.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 171(107701): 1, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530048",
-            "keyword": [
-                "drinking water",
-                "estrogen",
-                "bioassay"
-            ],
             "contactPoint": {
                 "fn": "Elizabeth Medlock Kakaley",
                 "hasEmail": "mailto:medlockkakaley.elizabeth@epa.gov"
             },
+            "description": "EPA-generated bioassay data published with 2020 bottled water study manuscript. \n\nThis dataset is associated with the following publication:\nBradley, P., K. Romanok, K. Smalling, M. Focazio, N. Evans, S. Fitzpatrick, C. Givens, S. Gordon, J. Gray, E. Green, D. Griffin, M. Hladik, L. Kanagy, J. Lisle, K. Loftin, R.B. McCleskey, E. Medlock Kakaley, A. Navas-Acien, D. Roth, and C. Weis. Bottled Water Contaminant Exposures and Predicted Human Effects.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 171(107701): 1, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0160412022006286#s0090",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0160412022006286#s0090"
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0160412022006286#s0090",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0160412022006286#s0090"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530048",
+            "keyword": [
+                "drinking water",
+                "estrogen",
+                "bioassay"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-18",
-            "references": [
-                "https://doi.org/10.1016/j.envint.2022.107701",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10123854"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191529,40 +191522,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envint.2022.107701",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10123854"
+            ],
+            "rights": null,
+            "title": "EPA-generated bioassay data for 2020 bottled water study"
         },
         {
-            "title": "Tillamook Estuary, Oregon 2017/2018 Coastal Acidification Case Study",
-            "description": "Synoptic survey and continuous monitoring data for coastal acidification in Tillamook Estuary, OR, USA",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529988",
-            "keyword": [
-                "coastal acidification",
-                "water quality",
-                "climate change",
-                "Nitrogen and Co-pollutants"
-            ],
             "contactPoint": {
                 "fn": "Stephen Pacella",
                 "hasEmail": "mailto:pacella.stephen@epa.gov"
             },
+            "description": "Synoptic survey and continuous monitoring data for coastal acidification in Tillamook Estuary, OR, USA",
             "distribution": [
                 {
-                    "title": "Pacella_TILL23_SciHub_Dataset Final.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529988/Pacella_TILL23_SciHub_Dataset%20Final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Pacella_TILL23_SciHub_Dataset Final.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529988",
+            "keyword": [
+                "coastal acidification",
+                "water quality",
+                "climate change",
+                "Nitrogen and Co-pollutants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-09",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -191571,41 +191567,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Tillamook Estuary, Oregon 2017/2018 Coastal Acidification Case Study"
         },
         {
-            "title": "Data for Deiodinase inhibition impairs the formation of the three posterior swim bladder tissue layers during early embryonic development in zebrafish",
-            "description": "The data set includes:\n1) Swimbladder inflation at 120 hours post-fertilization (hpf)\n2) Swimbladder surface area at 120 hpf\n3) Larval body length at 120 hpf\n4) Swimming activity at 120 hpf\n5) Targeted whole body gene expression results for nine mRNA transcripts evaluated at 60 hpf (hb9; fgf10a; acta2; anxa5b; wnt5b; fzd2; shha; ihha; ptc1)\n6) Targeted whole body gene expression results for the same nine mRNA transcripts evaluated at 120 hpf.\n7) Whole body thyroid hormone concentrations measured at 48, 60, 96, and 120 hpf\n8) Whole body thyroid hormone concentrations in IOP exposed embryos/larvae at 48, 60, and 120 hpf\n9) Data for supplementary figures S6, S7A, S7B\n10) Ratio T3 of IOP exposed embryos over control T3 levels during embryonic-juvenile development (4 replicates, Figure S9). \n\nThis dataset is associated with the following publication:\nVan Dingenen, I., L. Vergauwen, A. Haigis, B. Blackwell, E. Stacy, D. Villeneuve, and D. Knapen. Deiodinase inhibition impairs the formation of the three posterior swim bladder tissue layers during early embryonic development in zebrafish.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 261: 106632, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529156",
-            "keyword": [
-                "zebrafish",
-                "endocrine disruption",
-                "fish",
-                "Adverse Outcome Pathways (AOPs)"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "The data set includes:\n1) Swimbladder inflation at 120 hours post-fertilization (hpf)\n2) Swimbladder surface area at 120 hpf\n3) Larval body length at 120 hpf\n4) Swimming activity at 120 hpf\n5) Targeted whole body gene expression results for nine mRNA transcripts evaluated at 60 hpf (hb9; fgf10a; acta2; anxa5b; wnt5b; fzd2; shha; ihha; ptc1)\n6) Targeted whole body gene expression results for the same nine mRNA transcripts evaluated at 120 hpf.\n7) Whole body thyroid hormone concentrations measured at 48, 60, 96, and 120 hpf\n8) Whole body thyroid hormone concentrations in IOP exposed embryos/larvae at 48, 60, and 120 hpf\n9) Data for supplementary figures S6, S7A, S7B\n10) Ratio T3 of IOP exposed embryos over control T3 levels during embryonic-juvenile development (4 replicates, Figure S9). \n\nThis dataset is associated with the following publication:\nVan Dingenen, I., L. Vergauwen, A. Haigis, B. Blackwell, E. Stacy, D. Villeneuve, and D. Knapen. Deiodinase inhibition impairs the formation of the three posterior swim bladder tissue layers during early embryonic development in zebrafish.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 261: 106632, (2023).",
             "distribution": [
                 {
-                    "title": "Van Dingenen et al_AllData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529156/Van%20Dingenen%20et%20al_AllData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Van Dingenen et al_AllData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529156",
+            "keyword": [
+                "zebrafish",
+                "endocrine disruption",
+                "fish",
+                "Adverse Outcome Pathways (AOPs)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-23",
-            "references": [
-                "https://doi.org/10.1016/j.aquatox.2023.106632"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191615,41 +191609,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.aquatox.2023.106632"
+            ],
+            "rights": null,
+            "title": "Data for Deiodinase inhibition impairs the formation of the three posterior swim bladder tissue layers during early embryonic development in zebrafish"
         },
         {
-            "title": "Supplemental Information for Dietary uptake of highly hydrophobic chemicals by rainbow trout",
-            "description": "Detailed data and analysis supporting manuscript Dietary uptake of highly hydrophobic chemicals by rainbow trout. \n\nThis dataset is associated with the following publication:\nBurkhard, L., T. Lahren, K. Hanson, A. Kasparek, and D. Mount. Dietary Uptake of Highly Hydrophobic Chemicals by Rainbow Trout (Oncorhynchus Mykiss).   ARCHIVES OF ENVIRONMENTAL CONTAMINATION AND TOXICOLOGY. Springer, New York, NY, USA, 85(4): 390-403, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529165",
-            "keyword": [
-                "hydrophobicity",
-                "Kow",
-                "bioaccumulation",
-                "fish"
-            ],
             "contactPoint": {
                 "fn": "David Mount",
                 "hasEmail": "mailto:mount.dave@epa.gov"
             },
+            "description": "Detailed data and analysis supporting manuscript Dietary uptake of highly hydrophobic chemicals by rainbow trout. \n\nThis dataset is associated with the following publication:\nBurkhard, L., T. Lahren, K. Hanson, A. Kasparek, and D. Mount. Dietary Uptake of Highly Hydrophobic Chemicals by Rainbow Trout (Oncorhynchus Mykiss).   ARCHIVES OF ENVIRONMENTAL CONTAMINATION AND TOXICOLOGY. Springer, New York, NY, USA, 85(4): 390-403, (2023).",
             "distribution": [
                 {
-                    "title": "SI-Tables DRM 2023-06-28.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529165/SI-Tables%20DRM%202023-06-28.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI-Tables DRM 2023-06-28.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529165",
+            "keyword": [
+                "hydrophobicity",
+                "Kow",
+                "bioaccumulation",
+                "fish"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-28",
-            "references": [
-                "https://doi.org/10.1007/s00244-023-01038-6"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191659,20 +191653,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s00244-023-01038-6"
+            ],
+            "rights": null,
+            "title": "Supplemental Information for Dietary uptake of highly hydrophobic chemicals by rainbow trout"
         },
         {
-            "title": "Cross species extrapolation of the disruption of thyroid hormone synthesis by oxyfluorfen using in vitro data, physiologically based pharmacokinetic (PBPK), and thyroid hormone kinetics models",
-            "description": "How to access data for \"Decrane R, Stoker T, Murr A, Ford J, El-Masri H. Cross species extrapolation of the disruption of thyroid hormone synthesis by oxyfluorfen using in vitro data, physiologically based pharmacokinetic (PBPK), and thyroid hormone kinetics models. Curr Res Toxicol. 2023 Nov 23;5:100138. doi: 10.1016/j.crtox.2023.100138. PMID: 38074188; PMCID: PMC10697989.\". This dataset is not publicly accessible because: N/A. It can be accessed through the following means: Data will be made available on request from Hisham El-Masri (el-masri.hisham@epa.gov). Format: N/A. \n\nThis dataset is associated with the following publication:\nDecrane, R., T. Stoker, A. Murr, J. Ford, and H. El-Masri. Cross species extrapolation of the disruption of thyroid hormone synthesis by oxyfluorfen using in vitro data, physiologically based pharmacokinetic (PBPK), and thyroid hormone kinetics models.   Current Research in Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 5: 100138, (2023).",
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
+                "fn": "Hisham El-Masri",
+                "hasEmail": "mailto:el-masri.hisham@epa.gov"
+            },
+            "description": "How to access data for \"Decrane R, Stoker T, Murr A, Ford J, El-Masri H. Cross species extrapolation of the disruption of thyroid hormone synthesis by oxyfluorfen using in vitro data, physiologically based pharmacokinetic (PBPK), and thyroid hormone kinetics models. Curr Res Toxicol. 2023 Nov 23;5:100138. doi: 10.1016/j.crtox.2023.100138. PMID: 38074188; PMCID: PMC10697989.\". This dataset is not publicly accessible because: N/A. It can be accessed through the following means: Data will be made available on request from Hisham El-Masri (el-masri.hisham@epa.gov). Format: N/A. \n\nThis dataset is associated with the following publication:\nDecrane, R., T. Stoker, A. Murr, J. Ford, and H. El-Masri. Cross species extrapolation of the disruption of thyroid hormone synthesis by oxyfluorfen using in vitro data, physiologically based pharmacokinetic (PBPK), and thyroid hormone kinetics models.   Current Research in Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 5: 100138, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530082",
             "keyword": [
                 "Biological Modeling",
@@ -191680,15 +191678,10 @@
                 "pbpk",
                 "thyroid"
             ],
-            "contactPoint": {
-                "fn": "Hisham El-Masri",
-                "hasEmail": "mailto:el-masri.hisham@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-14",
-            "references": [
-                "https://doi.org/10.1016/j.crtox.2023.100138",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10697989"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191698,43 +191691,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.crtox.2023.100138",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10697989"
+            ],
+            "rights": null,
+            "title": "Cross species extrapolation of the disruption of thyroid hormone synthesis by oxyfluorfen using in vitro data, physiologically based pharmacokinetic (PBPK), and thyroid hormone kinetics models"
         },
         {
-            "title": "Mercury Isotope Values in Shoreline Spiders Reveal the Transfer of Aquatic Mercury Sources to Terrestrial Food Webs",
-            "description": "Supporting information for \"Janssen SE, Kotalik CJ, Eagles-Smith CA, Beaubien GB, Hoffman JC, Peterson G, Mills MA, Walters DM. Mercury Isotope Values in Shoreline Spiders Reveal the Transfer of Aquatic Mercury Sources to Terrestrial Food Webs. Environ Sci Technol Lett. 2023 Sep 13;10(10):891-896. doi: 10.1021/acs.estlett.3c00450. PMID: 37840816; PMCID: PMC10569030.\". \n\nThis dataset is associated with the following publication:\nJanssen, S., C. Kotalik, C. Eagles-Smith, G. Beaubien, J. Hoffman, G. Peterson, M. Mills, and D. Walters. Mercury Isotope Values in Shoreline Spiders Reveal the Transfer of Aquatic Mercury Sources to Terrestrial Food Webs.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA, 10(10): 891-896, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530083",
-            "keyword": [
-                "spiders",
-                "bioaccumulation",
-                "mercury stable isotopes",
-                "mercury",
-                "Bioindicator"
-            ],
             "contactPoint": {
                 "fn": "Joel Hoffman",
                 "hasEmail": "mailto:hoffman.joel@epa.gov"
             },
+            "description": "Supporting information for \"Janssen SE, Kotalik CJ, Eagles-Smith CA, Beaubien GB, Hoffman JC, Peterson G, Mills MA, Walters DM. Mercury Isotope Values in Shoreline Spiders Reveal the Transfer of Aquatic Mercury Sources to Terrestrial Food Webs. Environ Sci Technol Lett. 2023 Sep 13;10(10):891-896. doi: 10.1021/acs.estlett.3c00450. PMID: 37840816; PMCID: PMC10569030.\". \n\nThis dataset is associated with the following publication:\nJanssen, S., C. Kotalik, C. Eagles-Smith, G. Beaubien, J. Hoffman, G. Peterson, M. Mills, and D. Walters. Mercury Isotope Values in Shoreline Spiders Reveal the Transfer of Aquatic Mercury Sources to Terrestrial Food Webs.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA, 10(10): 891-896, (2023).",
             "distribution": [
                 {
-                    "title": "Supporting Information.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530083/Supporting%20Information.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supporting Information.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530083",
+            "keyword": [
+                "spiders",
+                "bioaccumulation",
+                "mercury stable isotopes",
+                "mercury",
+                "Bioindicator"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-21",
-            "references": [
-                "https://doi.org/10.1021/acs.estlett.3c00450",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569030"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191744,43 +191737,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.estlett.3c00450",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569030"
+            ],
+            "rights": null,
+            "title": "Mercury Isotope Values in Shoreline Spiders Reveal the Transfer of Aquatic Mercury Sources to Terrestrial Food Webs"
         },
         {
-            "title": "Contrasting mercury contamination scenarios and site susceptibilities confound fish mercury burdens in Suriname, South America",
-            "description": "Supplementary data for \"Vreedzaam A, Ouboter P, Hindori-Mohangoo AD, Lepak R, Rumschlag S, Janssen S, Landburg G, Shankar A, Zijlmans W, Lichtveld MY, Wickliffe JK. Contrasting mercury contamination scenarios and site susceptibilities confound fish mercury burdens in Suriname, South America. Environ Pollut. 2023 Nov 1;336:122447. doi: 10.1016/j.envpol.2023.122447. Epub 2023 Aug 28. PMID: 37648055; PMCID: PMC10756560.\". \n\nThis dataset is associated with the following publication:\nVreedzaam, A., P. Ouboter, A. Hindori-Mohangoo, R. Lepak, S. Rumschlag, S. Janssen, G. Landburg, A. Shankar, W. Zijlmans, M. Lichtveld, and J. Wickliffe. Contrasting mercury contamination scenarios and site susceptibilities confound fish mercury burdens in Suriname, South America.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 336: 122447, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530085",
-            "keyword": [
-                "Hg isotopes",
-                "fish",
-                "Suriname",
-                "Gold mining",
-                "mercury"
-            ],
             "contactPoint": {
                 "fn": "Ryan Lepak",
                 "hasEmail": "mailto:lepak.ryan@epa.gov"
             },
+            "description": "Supplementary data for \"Vreedzaam A, Ouboter P, Hindori-Mohangoo AD, Lepak R, Rumschlag S, Janssen S, Landburg G, Shankar A, Zijlmans W, Lichtveld MY, Wickliffe JK. Contrasting mercury contamination scenarios and site susceptibilities confound fish mercury burdens in Suriname, South America. Environ Pollut. 2023 Nov 1;336:122447. doi: 10.1016/j.envpol.2023.122447. Epub 2023 Aug 28. PMID: 37648055; PMCID: PMC10756560.\". \n\nThis dataset is associated with the following publication:\nVreedzaam, A., P. Ouboter, A. Hindori-Mohangoo, R. Lepak, S. Rumschlag, S. Janssen, G. Landburg, A. Shankar, W. Zijlmans, M. Lichtveld, and J. Wickliffe. Contrasting mercury contamination scenarios and site susceptibilities confound fish mercury burdens in Suriname, South America.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 336: 122447, (2023).",
             "distribution": [
                 {
-                    "title": "Supplementary Data.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530085/Supplementary%20Data.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary Data.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530085",
+            "keyword": [
+                "Hg isotopes",
+                "fish",
+                "Suriname",
+                "Gold mining",
+                "mercury"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-22",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2023.122447",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10756560"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191790,20 +191783,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2023.122447",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10756560"
+            ],
+            "rights": null,
+            "title": "Contrasting mercury contamination scenarios and site susceptibilities confound fish mercury burdens in Suriname, South America"
         },
         {
-            "title": "Metadata description for Higher daily air temperature is associated with shorter leukocyte telomere length: KORA F3 and KORA F4",
-            "description": "The data consists of a series of tables containing individual identifiers; countrywide high-resolution (1 km \u00d7 1 km) minimum, mean, and maximum daily air temperature data estimated using hybrid spatiotemporal regression-based models; daily concentrations of relative humidity (RH), ozone (O3), nitrogen dioxide (NO2), particulate matter within Augsburg, Germany; leukocyte telomere length; age (year), sex (male, female), education (years), and body mass index (BMI [kg/m2]); lifestyle characteristics, including smoking status, alcohol consumption (g/day), and physical activity; medical history of the participants, including hypertension (no/yes), angina pectoris (no/yes), myocardial infarction (no/yes), and stroke (no/yes); and current medications, including antihypertensive (no/yes), lipid-lowering (no/yes), and antidiabetic medication (no/yes). The data also contains serum total cholesterol; high-density lipoprotein (HDL); low-density lipoprotein (LDL); and triglycerides. This dataset is not publicly accessible because: The data is owned by an institute other than the EPA (Helmholtz Institute). It can be accessed through the following means: The data can be accessed by contacting the corresponding author of the study Wenli Ni (wenli.ni@helmholtz-muenchen.de). Format: The data consists of a series of tables containing individual identifiers; countrywide high-resolution (1 km \u00d7 1 km) minimum, mean, and maximum daily air temperature data estimated using hybrid spatiotemporal regression-based models; daily concentrations of relative humidity (RH), ozone (O3), nitrogen dioxide (NO2), particulate matter within Augsburg, Germany; leukocyte telomere length; age (year), sex (male, female), education (years), and body mass index (BMI [kg/m2]); lifestyle characteristics, including smoking status, alcohol consumption (g/day), and physical activity; medical history of the participants, including hypertension (no/yes), angina pectoris (no/yes), myocardial infarction (no/yes), and stroke (no/yes); and current medications, including antihypertensive (no/yes), lipid-lowering (no/yes), and antidiabetic medication (no/yes). The data also contains serum total cholesterol; high-density lipoprotein (HDL); low-density lipoprotein (LDL); and triglycerides. \n\nThis dataset is associated with the following publication:\nNi, W., K. Wolf, S.  Breitner, S. Zhang, N. Nikolaou, C. Ward-Caviness, M. Waldenberger, C. Gieger, A. Peters, and A. Schneider. Higher daily air temperature is associated with shorter leukocyte telomere length: KORA F3 and KORA F4.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 56(24): 17815-17824, (2022).",
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
+                "fn": "Cavin Ward-Caviness",
+                "hasEmail": "mailto:ward-caviness.cavin@epa.gov"
+            },
+            "description": "The data consists of a series of tables containing individual identifiers; countrywide high-resolution (1 km \u00d7 1 km) minimum, mean, and maximum daily air temperature data estimated using hybrid spatiotemporal regression-based models; daily concentrations of relative humidity (RH), ozone (O3), nitrogen dioxide (NO2), particulate matter within Augsburg, Germany; leukocyte telomere length; age (year), sex (male, female), education (years), and body mass index (BMI [kg/m2]); lifestyle characteristics, including smoking status, alcohol consumption (g/day), and physical activity; medical history of the participants, including hypertension (no/yes), angina pectoris (no/yes), myocardial infarction (no/yes), and stroke (no/yes); and current medications, including antihypertensive (no/yes), lipid-lowering (no/yes), and antidiabetic medication (no/yes). The data also contains serum total cholesterol; high-density lipoprotein (HDL); low-density lipoprotein (LDL); and triglycerides. This dataset is not publicly accessible because: The data is owned by an institute other than the EPA (Helmholtz Institute). It can be accessed through the following means: The data can be accessed by contacting the corresponding author of the study Wenli Ni (wenli.ni@helmholtz-muenchen.de). Format: The data consists of a series of tables containing individual identifiers; countrywide high-resolution (1 km \u00d7 1 km) minimum, mean, and maximum daily air temperature data estimated using hybrid spatiotemporal regression-based models; daily concentrations of relative humidity (RH), ozone (O3), nitrogen dioxide (NO2), particulate matter within Augsburg, Germany; leukocyte telomere length; age (year), sex (male, female), education (years), and body mass index (BMI [kg/m2]); lifestyle characteristics, including smoking status, alcohol consumption (g/day), and physical activity; medical history of the participants, including hypertension (no/yes), angina pectoris (no/yes), myocardial infarction (no/yes), and stroke (no/yes); and current medications, including antihypertensive (no/yes), lipid-lowering (no/yes), and antidiabetic medication (no/yes). The data also contains serum total cholesterol; high-density lipoprotein (HDL); low-density lipoprotein (LDL); and triglycerides. \n\nThis dataset is associated with the following publication:\nNi, W., K. Wolf, S.  Breitner, S. Zhang, N. Nikolaou, C. Ward-Caviness, M. Waldenberger, C. Gieger, A. Peters, and A. Schneider. Higher daily air temperature is associated with shorter leukocyte telomere length: KORA F3 and KORA F4.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 56(24): 17815-17824, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530089",
             "keyword": [
                 "air pollution",
@@ -191811,15 +191809,10 @@
                 "telomere length",
                 "Aging"
             ],
-            "contactPoint": {
-                "fn": "Cavin Ward-Caviness",
-                "hasEmail": "mailto:ward-caviness.cavin@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-12-20",
-            "references": [
-                "https://doi.org/10.1021/acs.est.2c04486",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9775210"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191829,32 +191822,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.2c04486",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9775210"
+            ],
+            "rights": null,
+            "title": "Metadata description for Higher daily air temperature is associated with shorter leukocyte telomere length: KORA F3 and KORA F4"
         },
         {
-            "title": "Closing Dichloramine Decomposition Nitrogen and Oxygen Mass Balances: Relative Importance of End-Products from the Reactive Nitrogen Species Pathway",
-            "description": "Data is for manuscript entitled \"Closing Dichloramine Decomposition Nitrogen and Oxygen Mass Balances: Relative Importance of End-Products from the Reactive Nitrogen Species Pathway\". This dataset is not publicly accessible because: The data was not generated by EPA.  It can be accessed by contacting the corresponding author. It can be accessed through the following means: Contact the manuscript corresponding author: Julian L. Fairey at julianf@uark.edu. Format: N/A. \n\nThis dataset is associated with the following publication:\nPham, H., D. Wahman, and J. Fairey. Closing Dichloramine Decomposition Nitrogen and Oxygen Mass Balances - Relative Importance of End-Products from the Reactive Nitrogen Species Pathway.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58( ): 2048-2057, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529535",
-            "keyword": [
-                "chloramine"
-            ],
             "contactPoint": {
                 "fn": "David Wahman",
                 "hasEmail": "mailto:wahman.david@epa.gov"
             },
+            "description": "Data is for manuscript entitled \"Closing Dichloramine Decomposition Nitrogen and Oxygen Mass Balances: Relative Importance of End-Products from the Reactive Nitrogen Species Pathway\". This dataset is not publicly accessible because: The data was not generated by EPA.  It can be accessed by contacting the corresponding author. It can be accessed through the following means: Contact the manuscript corresponding author: Julian L. Fairey at julianf@uark.edu. Format: N/A. \n\nThis dataset is associated with the following publication:\nPham, H., D. Wahman, and J. Fairey. Closing Dichloramine Decomposition Nitrogen and Oxygen Mass Balances - Relative Importance of End-Products from the Reactive Nitrogen Species Pathway.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58( ): 2048-2057, (2024).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1529535",
+            "keyword": [
+                "chloramine"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-09-06",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c08088"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191864,43 +191858,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c08088"
+            ],
+            "rights": null,
+            "title": "Closing Dichloramine Decomposition Nitrogen and Oxygen Mass Balances: Relative Importance of End-Products from the Reactive Nitrogen Species Pathway"
         },
         {
-            "title": "Intratracheal instillation of respirable particulate matter elicits neuroendocrine activation",
-            "description": "Objective: Inhalation of ozone activates central sympathetic-adrenal-medullary and hypothalamic-pituitary-adrenal stress axes. While airway neural networks are known to communicate noxious stimuli to higher brain centers, it is not known to what extent responses generated from pulmonary airways contribute to neuroendocrine activation.\n\nMaterials and methods: Unlike inhalational exposures that involve the entire respiratory tract, we employed intratracheal (IT) instillations to expose only pulmonary airways to either soluble metal-rich residual oil fly ash (ROFA) or compressor-generated diesel exhaust particles (C-DEP). Male Wistar-Kyoto rats (12-13 weeks) were IT instilled with either saline, C-DEP or ROFA (5 mg/kg) and necropsied at 4 or 24 hr to assess temporal effects.\n\nResults: IT-instillation of particulate matter (PM) induced hyperglycemia as early as 30-min and glucose intolerance when measured at 2 hr post-exposure. We observed PM- and time-specific effects on markers of pulmonary injury/inflammation (ROFA>C-DEP; 24 hr>4hr) as corroborated by increases in lavage fluid injury markers, neutrophils (ROFA>C-DEP), and lymphocytes (ROFA). Increases in lavage fluid pro-inflammatory cytokines differed between C-DEP and ROFA in that C-DEP caused larger increases in TNF-\u03b1 whereas ROFA caused larger increases in IL-6. No increases in circulating cytokines occurred. At 4 hr, PM impacts on neuroendocrine activation were observed through depletion of circulating leukocytes, increases in adrenaline (ROFA), and decreases in thyroid-stimulating-hormone, T3, prolactin, luteinizing-hormone, and testosterone. C-DEP and ROFA both increased lung expression of genes involved in acute stress and inflammatory processes. Moreover, small increases occurred in hypothalamic Fkbp5, a glucocorticoid-sensitive gene.\n\nConclusion: Respiratory alterations differed between C-DEP and ROFA, with ROFA inducing greater overall lung injury/inflammation; however, both PM induced a similar degree of neuroendocrine activation. These findings demonstrate neuroendocrine activation after pulmonary-only PM exposure, and suggest the involvement of pituitary- and adrenal-derived hormones. \n\nThis dataset is associated with the following publication:\nAlewel, D., A. Henriquez, M. Schladweiler, R. Grindstaff, A. Astriab Fisher, S. Snow , T. Jackson, and U. Kodavanti. Intratracheal instillation of respirable particulate matter elicits neuroendocrine activation.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 35(3-4): 59-75, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530092",
-            "keyword": [
-                "neuroendocrine",
-                "diesel exhaust particles",
-                "gene expression",
-                "hypothalamus",
-                "particulate matter"
-            ],
             "contactPoint": {
                 "fn": "Urmila Kodavanti",
                 "hasEmail": "mailto:kodavanti.urmila@epa.gov"
             },
+            "description": "Objective: Inhalation of ozone activates central sympathetic-adrenal-medullary and hypothalamic-pituitary-adrenal stress axes. While airway neural networks are known to communicate noxious stimuli to higher brain centers, it is not known to what extent responses generated from pulmonary airways contribute to neuroendocrine activation.\n\nMaterials and methods: Unlike inhalational exposures that involve the entire respiratory tract, we employed intratracheal (IT) instillations to expose only pulmonary airways to either soluble metal-rich residual oil fly ash (ROFA) or compressor-generated diesel exhaust particles (C-DEP). Male Wistar-Kyoto rats (12-13 weeks) were IT instilled with either saline, C-DEP or ROFA (5 mg/kg) and necropsied at 4 or 24 hr to assess temporal effects.\n\nResults: IT-instillation of particulate matter (PM) induced hyperglycemia as early as 30-min and glucose intolerance when measured at 2 hr post-exposure. We observed PM- and time-specific effects on markers of pulmonary injury/inflammation (ROFA>C-DEP; 24 hr>4hr) as corroborated by increases in lavage fluid injury markers, neutrophils (ROFA>C-DEP), and lymphocytes (ROFA). Increases in lavage fluid pro-inflammatory cytokines differed between C-DEP and ROFA in that C-DEP caused larger increases in TNF-\u03b1 whereas ROFA caused larger increases in IL-6. No increases in circulating cytokines occurred. At 4 hr, PM impacts on neuroendocrine activation were observed through depletion of circulating leukocytes, increases in adrenaline (ROFA), and decreases in thyroid-stimulating-hormone, T3, prolactin, luteinizing-hormone, and testosterone. C-DEP and ROFA both increased lung expression of genes involved in acute stress and inflammatory processes. Moreover, small increases occurred in hypothalamic Fkbp5, a glucocorticoid-sensitive gene.\n\nConclusion: Respiratory alterations differed between C-DEP and ROFA, with ROFA inducing greater overall lung injury/inflammation; however, both PM induced a similar degree of neuroendocrine activation. These findings demonstrate neuroendocrine activation after pulmonary-only PM exposure, and suggest the involvement of pituitary- and adrenal-derived hormones. \n\nThis dataset is associated with the following publication:\nAlewel, D., A. Henriquez, M. Schladweiler, R. Grindstaff, A. Astriab Fisher, S. Snow , T. Jackson, and U. Kodavanti. Intratracheal instillation of respirable particulate matter elicits neuroendocrine activation.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 35(3-4): 59-75, (2023).",
             "distribution": [
                 {
-                    "title": "Sciencehub - WKYROFAit - UK2020 (3-1-22).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530092/Sciencehub%20-%20WKYROFAit%20-%20UK2020%20%283-1-22%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Sciencehub - WKYROFAit - UK2020 (3-1-22).xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530092",
+            "keyword": [
+                "neuroendocrine",
+                "diesel exhaust particles",
+                "gene expression",
+                "hypothalamus",
+                "particulate matter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-31",
-            "references": [
-                "https://doi.org/10.1080/08958378.2022.2100019",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10590194"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -191910,285 +191903,290 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08958378.2022.2100019",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10590194"
+            ],
+            "rights": null,
+            "title": "Intratracheal instillation of respirable particulate matter elicits neuroendocrine activation"
         },
         {
-            "title": "USEEIO State Models v1.0 for 2020",
-            "description": "These are Excel outputs of each of the USEEIO State Models v1.0 for year 2020. They were developed using useeior v1.4.0 (https://github.com/USEPA/useeior/releases/tag/v1.4.0). See the referenced USEPA report for a full description. See the Data Dictionary for interpretation of the sheets in each Excel file. \n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530076",
-            "keyword": [
-                "environmental-economic model",
-                "subnational model",
-                "U.S. states",
-                "consumption-based GHG inventory"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530076/documents/StateEEIOv1.0-DataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "These are Excel outputs of each of the USEEIO State Models v1.0 for year 2020. They were developed using useeior v1.4.0 (https://github.com/USEPA/useeior/releases/tag/v1.4.0). See the referenced USEPA report for a full description. See the Data Dictionary for interpretation of the sheets in each Excel file. \n",
             "distribution": [
                 {
-                    "title": "StateEEIOv1.0-s-20-TX.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-TX.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-TX.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-TN.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-TN.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-TN.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-SD.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-SD.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-SD.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-SC.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-SC.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-SC.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-RI.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-RI.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-RI.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-PA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-PA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-PA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-OR.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-OR.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-OR.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-OK.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-OK.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-OK.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-OH.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-OH.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-OH.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-NY.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-NY.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-NY.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-NV.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-NV.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-NV.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-NM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-NM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-NM.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-NJ.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-NJ.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-NJ.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-NH.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-NH.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-NH.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-NE.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-NE.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-NE.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-ND.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-ND.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-ND.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-NC.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-NC.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-NC.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-MT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-MT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-MT.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-MS.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-MS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-MS.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-MO.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-MO.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-MO.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-MN.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-MN.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-MN.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-MI.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-MI.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-MI.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-ME.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-ME.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-ME.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-MD.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-MD.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-MD.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-MA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-MA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-MA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-LA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-LA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-LA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-KY.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-KY.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-KY.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-KS.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-KS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-KS.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-IN.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-IN.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-IN.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-IL.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-IL.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-IL.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-ID.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-ID.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-ID.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-IA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-IA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-IA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-HI.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-HI.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-HI.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-GA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-GA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-GA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-FL.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-FL.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-FL.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-DE.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-DE.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-DE.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-CT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-CT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-CT.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-CO.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-CO.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-CO.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-CA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-CA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-CA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-AZ.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-AZ.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-AZ.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-AR.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-AR.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-AR.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-AL.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-AL.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-AL.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-AK.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-AK.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-AK.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-WY.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-WY.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-WY.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-WV.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-WV.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-WV.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-WI.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-WI.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-WI.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-WA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-WA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-WA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-VT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-VT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-VT.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-VA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-VA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-VA.xlsx"
                 },
                 {
-                    "title": "StateEEIOv1.0-s-20-UT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530076/StateEEIOv1.0-s-20-UT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StateEEIOv1.0-s-20-UT.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530076",
+            "keyword": [
+                "environmental-economic model",
+                "subnational model",
+                "U.S. states",
+                "consumption-based GHG inventory"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-22",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -192198,20 +192196,25 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530076/documents/StateEEIOv1.0-DataDictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": null,
+            "rights": null,
+            "title": "USEEIO State Models v1.0 for 2020"
         },
         {
-            "title": "Metadata for Pavlovic et al. - Machine Learning Critical Loads",
-            "description": "This is the metadata associated with Pavlovic et al. (2023) entitled \"Empirical nitrogen and sulfur critical loads of U.S. tree species and their uncertainties with machine learning\" (https://www.sciencedirect.com/science/article/pii/S0048969722063513). It is not EPA data and the data and associated metadata is already publicly available on the journal website. \n\nThis dataset is associated with the following publication:\nPavlovic, N., S. Chang, J. Huang, K. Craig, C. Clark, K. Horn, and C. Driscoll. Empirical nitrogen and sulfur critical loads of U.S. tree species and their uncertainties with machine learning.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 857: 1-10, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Christopher Clark",
+                "hasEmail": "mailto:clark.christopher@epa.gov"
+            },
+            "description": "This is the metadata associated with Pavlovic et al. (2023) entitled \"Empirical nitrogen and sulfur critical loads of U.S. tree species and their uncertainties with machine learning\" (https://www.sciencedirect.com/science/article/pii/S0048969722063513). It is not EPA data and the data and associated metadata is already publicly available on the journal website. \n\nThis dataset is associated with the following publication:\nPavlovic, N., S. Chang, J. Huang, K. Craig, C. Clark, K. Horn, and C. Driscoll. Empirical nitrogen and sulfur critical loads of U.S. tree species and their uncertainties with machine learning.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 857: 1-10, (2022).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0048969722063513",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0048969722063513"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530094",
             "keyword": [
@@ -192221,20 +192224,10 @@
                 "Tree",
                 "NAAQS"
             ],
-            "contactPoint": {
-                "fn": "Christopher Clark",
-                "hasEmail": "mailto:clark.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0048969722063513",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0048969722063513"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-10-01",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2022.159252",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10241478"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192244,20 +192237,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2022.159252",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10241478"
+            ],
+            "rights": null,
+            "title": "Metadata for Pavlovic et al. - Machine Learning Critical Loads"
         },
         {
-            "title": "No dataset available.",
-            "description": "The dataset to support the journal article was generated by a cooperative non-EPA research organization. Readers may inquire underlying dataset from the corresponding author as specified in the journal article. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: The corresponding author of the paper, as noted in the journal article, can provide datasets upon request. Format: The dataset to support the journal article was generated by a cooperative non-EPA research organization. No further information on dataset format and status is available. \n\nThis dataset is associated with the following publication:\nShao, Y., K. Li, T. Zhang, J. Yang, and S. Chu. Modeling of Truncated Normal Distribution for Estimating Hydraulic Parameters in Water Distribution Systems - Taking Nodal Water Demand as an Example.   Journal of Hydroinformatics. IWA Publishing, London,  UK, 25(5): 2053\u20132068, (2023).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Yingping Yang",
+                "hasEmail": "mailto:yang.jeff@epa.gov"
+            },
+            "description": "The dataset to support the journal article was generated by a cooperative non-EPA research organization. Readers may inquire underlying dataset from the corresponding author as specified in the journal article. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: The corresponding author of the paper, as noted in the journal article, can provide datasets upon request. Format: The dataset to support the journal article was generated by a cooperative non-EPA research organization. No further information on dataset format and status is available. \n\nThis dataset is associated with the following publication:\nShao, Y., K. Li, T. Zhang, J. Yang, and S. Chu. Modeling of Truncated Normal Distribution for Estimating Hydraulic Parameters in Water Distribution Systems - Taking Nodal Water Demand as an Example.   Journal of Hydroinformatics. IWA Publishing, London,  UK, 25(5): 2053\u20132068, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529984",
             "keyword": [
                 "Parameter Estimation",
@@ -192265,14 +192263,10 @@
                 "Bayesian framework",
                 "Truncated Normal Distribution"
             ],
-            "contactPoint": {
-                "fn": "Yingping Yang",
-                "hasEmail": "mailto:yang.jeff@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2024-01-10",
-            "references": [
-                "https://doi.org/10.2166/hydro.2023.250"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192282,40 +192276,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2166/hydro.2023.250"
+            ],
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "title": "No dataset available."
         },
         {
-            "title": "Hat Island and Mission Beach discrete and continuous time series data for carbonate chemistry and other physical/biogechemical parameters",
-            "description": "High-resolution (15-minute frequency) monitoring data of pH, dissolved oxygen, salinity, temperature, depth, and chlorophyll from July 2015 \u2013 April 2016 in two seagrass systems of Puget Sound, WA, USA. Grab samples for instrument validation and carbonate chemistry analysis were periodically taken next to the in-situ instrumentation and are included.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503725",
-            "keyword": [
-                "Ocean acidification",
-                "coastal acidification",
-                "seagrasses",
-                "carbonate chemistry"
-            ],
             "contactPoint": {
                 "fn": "Stephen Pacella",
                 "hasEmail": "mailto:pacella.stephen@epa.gov"
             },
+            "description": "High-resolution (15-minute frequency) monitoring data of pH, dissolved oxygen, salinity, temperature, depth, and chlorophyll from July 2015 \u2013 April 2016 in two seagrass systems of Puget Sound, WA, USA. Grab samples for instrument validation and carbonate chemistry analysis were periodically taken next to the in-situ instrumentation and are included.",
             "distribution": [
                 {
-                    "title": "Pacella-JGR23-Resubmission Dataset.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503725/Pacella-JGR23-Resubmission%20Dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Pacella-JGR23-Resubmission Dataset.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503725",
+            "keyword": [
+                "Ocean acidification",
+                "coastal acidification",
+                "seagrasses",
+                "carbonate chemistry"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-28",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -192324,42 +192320,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Hat Island and Mission Beach discrete and continuous time series data for carbonate chemistry and other physical/biogechemical parameters"
         },
         {
-            "title": "K means clustering the opportunity atlas 2023APR",
-            "description": "All code and input files used in k-means clustering analysis of Opportunity Atlas data. \n\nThis dataset is associated with the following publication:\nZelasky, S., C. Martin, C. Weaver, L. Baxter, and K. Rappazzo. Identifying groups of children's social mobility opportunity for public health applications using k-means clustering.   Heliyon. Elsevier B.V., Amsterdam,  NETHERLANDS, 9(9): E20250, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530105",
-            "keyword": [
-                "opportunity",
-                "social mobility",
-                "k-means clustering",
-                "children's health"
-            ],
             "contactPoint": {
                 "fn": "Kristen Rappazzo",
                 "hasEmail": "mailto:rappazzo.kristen@epa.gov"
             },
+            "description": "All code and input files used in k-means clustering analysis of Opportunity Atlas data. \n\nThis dataset is associated with the following publication:\nZelasky, S., C. Martin, C. Weaver, L. Baxter, and K. Rappazzo. Identifying groups of children's social mobility opportunity for public health applications using k-means clustering.   Heliyon. Elsevier B.V., Amsterdam,  NETHERLANDS, 9(9): E20250, (2023).",
             "distribution": [
                 {
-                    "title": "ScienceHub.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530105/ScienceHub.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ScienceHub.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530105",
+            "keyword": [
+                "opportunity",
+                "social mobility",
+                "k-means clustering",
+                "children's health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-28",
-            "references": [
-                "https://doi.org/10.1016/j.heliyon.2023.e20250",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10560027"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192369,49 +192362,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.heliyon.2023.e20250",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10560027"
+            ],
+            "rights": null,
+            "title": "K means clustering the opportunity atlas 2023APR"
         },
         {
-            "title": "NEST preterm birth air pollution dietary factors 2023MAY",
-            "description": "Data dictionary and code files associated with analysis of air pollution and dietary factor interactions with preterm birth. \n\nThis dataset is associated with the following publication:\nJardel, H., C. Martin, C. Hoyo, and K. Rappazzo. Interplay of gestational parent exposure to ambient air pollution and diet characteristics on preterm birth.   BMC PUBLIC HEALTH. BioMed Central Ltd, London,  UK, 23: 822, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530106",
-            "keyword": [
-                "Modification",
-                "air pollution",
-                "preterm birth",
-                "diet",
-                "epidemiology",
-                "Children's Environmental Health"
-            ],
             "contactPoint": {
                 "fn": "Kristen Rappazzo",
                 "hasEmail": "mailto:rappazzo.kristen@epa.gov"
             },
+            "description": "Data dictionary and code files associated with analysis of air pollution and dietary factor interactions with preterm birth. \n\nThis dataset is associated with the following publication:\nJardel, H., C. Martin, C. Hoyo, and K. Rappazzo. Interplay of gestational parent exposure to ambient air pollution and diet characteristics on preterm birth.   BMC PUBLIC HEALTH. BioMed Central Ltd, London,  UK, 23: 822, (2023).",
             "distribution": [
                 {
-                    "title": "Code NEST pollution diet 2023MAY.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530106/Code%20NEST%20pollution%20diet%202023MAY.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Code NEST pollution diet 2023MAY.zip"
                 },
                 {
-                    "title": "Data dictionary NEST-Pollution-Diet.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530106/Data%20dictionary%20NEST-Pollution-Diet.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data dictionary NEST-Pollution-Diet.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530106",
+            "keyword": [
+                "Modification",
+                "air pollution",
+                "preterm birth",
+                "diet",
+                "epidemiology",
+                "Children's Environmental Health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-30",
-            "references": [
-                "https://doi.org/10.1186/s12889-023-15676-x",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10161541"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192421,58 +192414,59 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12889-023-15676-x",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10161541"
+            ],
+            "rights": null,
+            "title": "NEST preterm birth air pollution dietary factors 2023MAY"
         },
         {
-            "title": "Evaluation of a high-throughput H295R homogenous time resolved fluorescence assay for androgen and estrogen steroidogenesis screening",
-            "description": "Dataset for 'Evaluation of a high-throughput H295R homogenous time resolved fluorescence assay for androgen and estrogen steroidogenesis screening', Garnovskaya, et al., Toxicology in Vitro, Vol 92, 105659, Oct 2023, https://doi.org/10.1016/j.tiv.2023.105659. Contains the ToxCast Pipeline datasets and curve fits that can be pulled up from InvitroDB on the CompTox Chemicals Dashboard. \n\nThis dataset is associated with the following publication:\nGarnovskaya, M., M. Feshuk, W. Stewart, K. Friedman, R. Thomas, and C. Deisenroth. Evaluation of a High-throughput H295R Homogenous Time Resolved Fluorescence Assay for Androgen and Estrogen Steroidogenesis Screening.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 92: 105659, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530103",
-            "keyword": [
-                "androgen",
-                "estrogen",
-                "New Approach Methods (Alternatives to Animal Testing)",
-                "steroidogenesis",
-                "High throughput screening",
-                "endocrine toxicology"
-            ],
             "contactPoint": {
                 "fn": "Chad Deisenroth",
                 "hasEmail": "mailto:deisenroth.chad@epa.gov"
             },
+            "description": "Dataset for 'Evaluation of a high-throughput H295R homogenous time resolved fluorescence assay for androgen and estrogen steroidogenesis screening', Garnovskaya, et al., Toxicology in Vitro, Vol 92, 105659, Oct 2023, https://doi.org/10.1016/j.tiv.2023.105659. Contains the ToxCast Pipeline datasets and curve fits that can be pulled up from InvitroDB on the CompTox Chemicals Dashboard. \n\nThis dataset is associated with the following publication:\nGarnovskaya, M., M. Feshuk, W. Stewart, K. Friedman, R. Thomas, and C. Deisenroth. Evaluation of a High-throughput H295R Homogenous Time Resolved Fluorescence Assay for Androgen and Estrogen Steroidogenesis Screening.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 92: 105659, (2023).",
             "distribution": [
                 {
-                    "title": "ccte_deisenroth_htrf_fsk_08AUG2022.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530103/ccte_deisenroth_htrf_fsk_08AUG2022.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ccte_deisenroth_htrf_fsk_08AUG2022.xlsx"
                 },
                 {
-                    "title": "ccte_deisenroth_htrf_fsk_08AUG2022.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530103/ccte_deisenroth_htrf_fsk_08AUG2022.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "ccte_deisenroth_htrf_fsk_08AUG2022.pdf"
                 },
                 {
-                    "title": "ccte_deisenroth_htrf_08AUG2022.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530103/ccte_deisenroth_htrf_08AUG2022.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ccte_deisenroth_htrf_08AUG2022.xlsx"
                 },
                 {
-                    "title": "ccte_deisenroth_htrf_08AUG2022.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530103/ccte_deisenroth_htrf_08AUG2022.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "ccte_deisenroth_htrf_08AUG2022.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530103",
+            "keyword": [
+                "androgen",
+                "estrogen",
+                "New Approach Methods (Alternatives to Animal Testing)",
+                "steroidogenesis",
+                "High throughput screening",
+                "endocrine toxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-08",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2023.105659"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192482,42 +192476,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2023.105659"
+            ],
+            "rights": null,
+            "title": "Evaluation of a high-throughput H295R homogenous time resolved fluorescence assay for androgen and estrogen steroidogenesis screening"
         },
         {
-            "title": "HSRP Project Data",
-            "description": "Percent recovery of somatic and F+ coliphage. \n\nThis dataset is associated with the following publication:\nHurst, B.N., A. Korajkic, A. Pemberton, and B. McMinn. Improved Virus Concentration Methods for Wash Waters from Decontamination of Permeable and Non-Permeable Surfaces.   JOURNAL OF VIROLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 322: 114826, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528647",
-            "keyword": [
-                "hollow fiber",
-                "wash water",
-                "percent recovery",
-                "coliphage"
-            ],
             "contactPoint": {
                 "fn": "Brian McMinn",
                 "hasEmail": "mailto:mcminn.brian@epa.gov"
             },
+            "description": "Percent recovery of somatic and F+ coliphage. \n\nThis dataset is associated with the following publication:\nHurst, B.N., A. Korajkic, A. Pemberton, and B. McMinn. Improved Virus Concentration Methods for Wash Waters from Decontamination of Permeable and Non-Permeable Surfaces.   JOURNAL OF VIROLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 322: 114826, (2023).",
             "distribution": [
                 {
-                    "title": "HSRP_Project Data_030323.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528647/HSRP_Project%20Data_030323.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HSRP_Project Data_030323.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528647",
+            "keyword": [
+                "hollow fiber",
+                "wash water",
+                "percent recovery",
+                "coliphage"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-03",
-            "references": [
-                "https://doi.org/10.1016/j.jviromet.2023.114826",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10841435"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192527,47 +192520,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jviromet.2023.114826",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10841435"
+            ],
+            "rights": null,
+            "title": "HSRP Project Data"
         },
         {
-            "title": "An Interlaboratory Comparison of Extractable Organofluorine Measurements in Groundwater and Eel (Anguilla rostrata): Recommendations for Methods Standardization",
-            "description": "Standardized methods for organofluorine analysis are currently unavailable including for extractable organofluorine (EOF) measured using combustion ion chromatography (CIC). Here we evaluate the reproducibility, precision, and accuracy of EOF based on an international interlaboratory comparison. Seven laboratories representing academia, government, and the private sector measured paired EOF and PFAS concentrations in groundwater and eel (Anguilla rostrata) from a site contaminated by aqueous film forming foam. \n\nThis dataset is associated with the following publication:\nRuyle, B.J., H.M. Pickard, L. Schultes, F. Fredriksson, A.L. Heffernan, D.R.U. Knappe, H.L. Lord, P. Meng, M.A. Mills, K. Ndungu, P. Roesch, J.T. Rundberget, D.R. Tettenhorst, J. Van Buren, C. Vogel, D.C. Westerman, L.W.Y. Yeung, and E.M. Sunderlanda. Interlaboratory Comparison of Extractable Organofluorine Measurements in Groundwater and Eel (Anguilla rostrata): Recommendations for Methods Standardization.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(48): 20159-20168, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529107",
-            "keyword": [
-                "PFAS",
-                "analytical method",
-                "organofluorine",
-                "water quality"
-            ],
             "contactPoint": {
                 "fn": "Jean Van Buren",
                 "hasEmail": "mailto:vanburen.jean@epa.gov"
             },
+            "description": "Standardized methods for organofluorine analysis are currently unavailable including for extractable organofluorine (EOF) measured using combustion ion chromatography (CIC). Here we evaluate the reproducibility, precision, and accuracy of EOF based on an international interlaboratory comparison. Seven laboratories representing academia, government, and the private sector measured paired EOF and PFAS concentrations in groundwater and eel (Anguilla rostrata) from a site contaminated by aqueous film forming foam. \n\nThis dataset is associated with the following publication:\nRuyle, B.J., H.M. Pickard, L. Schultes, F. Fredriksson, A.L. Heffernan, D.R.U. Knappe, H.L. Lord, P. Meng, M.A. Mills, K. Ndungu, P. Roesch, J.T. Rundberget, D.R. Tettenhorst, J. Van Buren, C. Vogel, D.C. Westerman, L.W.Y. Yeung, and E.M. Sunderlanda. Interlaboratory Comparison of Extractable Organofluorine Measurements in Groundwater and Eel (Anguilla rostrata): Recommendations for Methods Standardization.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(48): 20159-20168, (2023).",
             "distribution": [
                 {
-                    "title": "EOF_Interlab_SI_20230525.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529107/EOF_Interlab_SI_20230525.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "EOF_Interlab_SI_20230525.docx"
                 },
                 {
-                    "title": "EOF_Interlab_SI_Tables_20230525.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529107/EOF_Interlab_SI_Tables_20230525.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EOF_Interlab_SI_Tables_20230525.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529107",
+            "keyword": [
+                "PFAS",
+                "analytical method",
+                "organofluorine",
+                "water quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-05-30",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c04560",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10702518"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192577,35 +192570,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c04560",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10702518"
+            ],
+            "rights": null,
+            "title": "An Interlaboratory Comparison of Extractable Organofluorine Measurements in Groundwater and Eel (Anguilla rostrata): Recommendations for Methods Standardization"
         },
         {
-            "title": "Sorption of heavy metals by hydrochar",
-            "description": "Heavy metal sorption data.   Material characterization using scanning electron microscopy (SEM, Hitachi SU8020, Japan) and energy spectrometry (EDS), Fourier transform infrared (FTIR, Nichlet IS 10, USA) spectroscopy, X-ray photoelectron spectroscopy (XPS, Thermo escalab 250Xi, USA) and X-ray diffraction (XRD, BRUCKER D8 ADVANCE, Germany). This dataset is not publicly accessible because: None-EPA data - owned by the University of Florida. It can be accessed through the following means: Contact Dr. Yue Zhang at the University of Florida at 352-871-2488 . Format: The data included in the manuscript: Heavy metal sorption data in Excel; Images of scanning electron microscopy (SEM, Hitachi SU8020, Japan) and energy spectrometry (EDS). Spectra of Fourier transform infrared (FTIR, Nichlet IS 10, USA) spectroscopy, X-ray photoelectron spectroscopy (XPS, Thermo escalab 250Xi, USA), and X-ray diffraction (XRD, BRUCKER D8 ADVANCE, Germany). \n\nThis dataset is associated with the following publication:\nZhang , Y., Y. Wan, Y.  Zheng , Y. Yang, J. Huang, H. Chen, and B. Gao. Potassium permanganate modification of hydrochar enhances sorption of Pb(II), Cu(II), and Cd(II).   Bioresource Technology. Elsevier Online, New York, NY, USA, 386: 129482, (2023).",
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
+                "fn": "Yongshan Wan",
+                "hasEmail": "mailto:wan.yongshan@epa.gov"
+            },
+            "description": "Heavy metal sorption data.   Material characterization using scanning electron microscopy (SEM, Hitachi SU8020, Japan) and energy spectrometry (EDS), Fourier transform infrared (FTIR, Nichlet IS 10, USA) spectroscopy, X-ray photoelectron spectroscopy (XPS, Thermo escalab 250Xi, USA) and X-ray diffraction (XRD, BRUCKER D8 ADVANCE, Germany). This dataset is not publicly accessible because: None-EPA data - owned by the University of Florida. It can be accessed through the following means: Contact Dr. Yue Zhang at the University of Florida at 352-871-2488 . Format: The data included in the manuscript: Heavy metal sorption data in Excel; Images of scanning electron microscopy (SEM, Hitachi SU8020, Japan) and energy spectrometry (EDS). Spectra of Fourier transform infrared (FTIR, Nichlet IS 10, USA) spectroscopy, X-ray photoelectron spectroscopy (XPS, Thermo escalab 250Xi, USA), and X-ray diffraction (XRD, BRUCKER D8 ADVANCE, Germany). \n\nThis dataset is associated with the following publication:\nZhang , Y., Y. Wan, Y.  Zheng , Y. Yang, J. Huang, H. Chen, and B. Gao. Potassium permanganate modification of hydrochar enhances sorption of Pb(II), Cu(II), and Cd(II).   Bioresource Technology. Elsevier Online, New York, NY, USA, 386: 129482, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530108",
             "keyword": [
                 "heavy metals",
                 "biochar",
                 "Metal sorption"
             ],
-            "contactPoint": {
-                "fn": "Yongshan Wan",
-                "hasEmail": "mailto:wan.yongshan@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-05-29",
-            "references": [
-                "https://doi.org/10.1016/j.biortech.2023.129482",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10558135"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192615,100 +192608,100 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.biortech.2023.129482",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10558135"
+            ],
+            "rights": null,
+            "title": "Sorption of heavy metals by hydrochar"
         },
         {
-            "title": "Beneficiary and Ecosystem Services Profiles from MassBays Document Analysis",
-            "description": "This data set contains the output from a keyword search document analysis of MassBays NEP Assessment Area communities.  S1 is the list of keyword search terms. S2 is the list of planning documents included in the search. S3 are graphs of beneficiary profiles and ecosystem services profiles for each assessment area.  S4 are graphs of ecosystem frequencies, beneficiary profiles, and ecosystem services for each cluster. S5 is the table of socio-economic and ecological variables for each assessment area. S6 are graphs of socio-economic and ecological variables for each cluster. S7 are post-hoc statistical analysis to relate socio-economic and ecological variables to ecosystem services priorities. S8 are the frequency at which ecosystems are mentioned in documents for each assessment area. S9 is the table of beneficiary profiles for each assessment area.  S10 are the relative importance of ecosystem services attributes to each beneficiary type for each assessment area. S11 are the final ecosystem services profiles for each assessment area. S12 is the full list of final ecosystem services (an ecosystem + a beneficiary + an ecosystem services attribute) from all search documents. \n\nThis dataset is associated with the following publication:\nYee, S., L. Sharpe, B. Branoff, C. Jackson, G. Cicchetti, S. Jackson, M. Pryor, and E. Shumchenia. Ecosystem Services Profiles for Communities Benefitting from Estuarine Habitats along the Massachusetts Coast, USA.   Ecological Informatics. Elsevier Science Ltd, New York, NY, USA, 77: 102182, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528467",
-            "keyword": [
-                "estuary",
-                "Massachusetts Bay",
-                "document analysis",
-                "Salt marsh",
-                "tidal flats",
-                "seagrass",
-                "ecosystem services"
-            ],
             "contactPoint": {
                 "fn": "Susan Yee",
                 "hasEmail": "mailto:yee.susan@epa.gov"
             },
+            "description": "This data set contains the output from a keyword search document analysis of MassBays NEP Assessment Area communities.  S1 is the list of keyword search terms. S2 is the list of planning documents included in the search. S3 are graphs of beneficiary profiles and ecosystem services profiles for each assessment area.  S4 are graphs of ecosystem frequencies, beneficiary profiles, and ecosystem services for each cluster. S5 is the table of socio-economic and ecological variables for each assessment area. S6 are graphs of socio-economic and ecological variables for each cluster. S7 are post-hoc statistical analysis to relate socio-economic and ecological variables to ecosystem services priorities. S8 are the frequency at which ecosystems are mentioned in documents for each assessment area. S9 is the table of beneficiary profiles for each assessment area.  S10 are the relative importance of ecosystem services attributes to each beneficiary type for each assessment area. S11 are the final ecosystem services profiles for each assessment area. S12 is the full list of final ecosystem services (an ecosystem + a beneficiary + an ecosystem services attribute) from all search documents. \n\nThis dataset is associated with the following publication:\nYee, S., L. Sharpe, B. Branoff, C. Jackson, G. Cicchetti, S. Jackson, M. Pryor, and E. Shumchenia. Ecosystem Services Profiles for Communities Benefitting from Estuarine Habitats along the Massachusetts Coast, USA.   Ecological Informatics. Elsevier Science Ltd, New York, NY, USA, 77: 102182, (2023).",
             "distribution": [
                 {
-                    "title": "S3_Assessment_Area_Profiles.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S3_Assessment_Area_Profiles.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "S3_Assessment_Area_Profiles.pdf"
                 },
                 {
-                    "title": "S2.Document_List.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S2.Document_List.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S2.Document_List.xlsx"
                 },
                 {
-                    "title": "S1.Keyword_List_MassBays.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S1.Keyword_List_MassBays.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S1.Keyword_List_MassBays.xlsx"
                 },
                 {
-                    "title": "S10.EcoServices_Per_Beneficiary_for_EachAssessmentArea_EachHabitat.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S10.EcoServices_Per_Beneficiary_for_EachAssessmentArea_EachHabitat.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S10.EcoServices_Per_Beneficiary_for_EachAssessmentArea_EachHabitat.xlsx"
                 },
                 {
-                    "title": "S9.Beneficiaries_for_EachAssessmentArea_EachHabitat.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S9.Beneficiaries_for_EachAssessmentArea_EachHabitat.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S9.Beneficiaries_for_EachAssessmentArea_EachHabitat.xlsx"
                 },
                 {
-                    "title": "S8.Ecosystems_EachAssessmentArea.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S8.Ecosystems_EachAssessmentArea.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S8.Ecosystems_EachAssessmentArea.xlsx"
                 },
                 {
-                    "title": "S7.PostHoc_Analyses.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S7.PostHoc_Analyses.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S7.PostHoc_Analyses.xlsx"
                 },
                 {
-                    "title": "S6_Socioeconomic_Data_By_Cluster.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S6_Socioeconomic_Data_By_Cluster.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "S6_Socioeconomic_Data_By_Cluster.pdf"
                 },
                 {
-                    "title": "S5.SocioEcological_Data_EachAssessmentArea.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S5.SocioEcological_Data_EachAssessmentArea.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S5.SocioEcological_Data_EachAssessmentArea.xlsx"
                 },
                 {
-                    "title": "S4_Profiles_By_Cluster.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S4_Profiles_By_Cluster.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "S4_Profiles_By_Cluster.pdf"
                 },
                 {
-                    "title": "S12.Triplets_Each_Document.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S12.Triplets_Each_Document.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S12.Triplets_Each_Document.xlsx"
                 },
                 {
-                    "title": "S11.FinalEcoServices_for_EachAssessmentArea_EachHabitat.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528467/S11.FinalEcoServices_for_EachAssessmentArea_EachHabitat.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S11.FinalEcoServices_for_EachAssessmentArea_EachHabitat.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528467",
+            "keyword": [
+                "estuary",
+                "Massachusetts Bay",
+                "document analysis",
+                "Salt marsh",
+                "tidal flats",
+                "seagrass",
+                "ecosystem services"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-26",
-            "references": [
-                "https://doi.org/10.1016/j.ecoinf.2023.102182",
-                "https://pasteur.epa.gov/uploads/10.23719/1528467/documents/MB_Assessment_Areas.zip"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192718,42 +192711,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecoinf.2023.102182",
+                "https://pasteur.epa.gov/uploads/10.23719/1528467/documents/MB_Assessment_Areas.zip"
+            ],
+            "rights": null,
+            "title": "Beneficiary and Ecosystem Services Profiles from MassBays Document Analysis"
         },
         {
-            "title": "Verification of in vivo estrogenic activity for four per- and polyfluoroalkyl substances (PFAS) identified as estrogen receptor agonists via new approach methodologies (v4)",
-            "description": "The dataset includes data from six experiments in which adult male fathead minnows were exposed to five concentrations of a per- or polyfluorinated alkyl substance (PFAS) and a 17beta-estradiol positive control for 96 hours. Meta data on each fish exposed including treatment, replicate, sex, whole body wet weight, and gonad weights are included. Endpoints measured include nuptial tubercle scores, gonadosomatic index, and hepatic expression of four estrogen regulated mRNA transcripts:  vitellogenin, estrogen receptor alpha, apolipoprotein eb, and insulin-like growth factor 1. The data set also includes water quality data collected over the course of each exposure, and measured concentrations of the test chemicals in water and plasma. The PFAS tested include: Perfluorooctanoic acid; 1H,1H,8H,8H-Perfluorooctane-1,8-diol; 1H,1H,10H,10H-Perfluorodecane-1,10-diol; 1H,1H,8H,8H-Perfluoro-3,6-dioxaoctane-1,8-diol; and Perfluoro-2-methyl-3-oxahexanoic acid. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., B. Blackwell, J. Cavallin, J. Collins, J. Hoang, R. Hofer, K. Houck, K. Jensen, M. Kahl, R. Kutsi, A. Opseth, K. Santana Rodriguez, C. Schaupp, E. Stacy, and G. Ankley. Verification of In Vivo Estrogenic Activity for Four Per- and Polyfluoroalkyl Substances (PFAS) Identified as Estrogen Receptor Agonists via New Approach Methodologies.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(9): 3794-3803, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528334",
-            "keyword": [
-                "PFAS",
-                "endocrine",
-                "ecological risk",
-                "high throughput",
-                "Adverse Outcome Pathways (AOPs)"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "The dataset includes data from six experiments in which adult male fathead minnows were exposed to five concentrations of a per- or polyfluorinated alkyl substance (PFAS) and a 17beta-estradiol positive control for 96 hours. Meta data on each fish exposed including treatment, replicate, sex, whole body wet weight, and gonad weights are included. Endpoints measured include nuptial tubercle scores, gonadosomatic index, and hepatic expression of four estrogen regulated mRNA transcripts:  vitellogenin, estrogen receptor alpha, apolipoprotein eb, and insulin-like growth factor 1. The data set also includes water quality data collected over the course of each exposure, and measured concentrations of the test chemicals in water and plasma. The PFAS tested include: Perfluorooctanoic acid; 1H,1H,8H,8H-Perfluorooctane-1,8-diol; 1H,1H,10H,10H-Perfluorodecane-1,10-diol; 1H,1H,8H,8H-Perfluoro-3,6-dioxaoctane-1,8-diol; and Perfluoro-2-methyl-3-oxahexanoic acid. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., B. Blackwell, J. Cavallin, J. Collins, J. Hoang, R. Hofer, K. Houck, K. Jensen, M. Kahl, R. Kutsi, A. Opseth, K. Santana Rodriguez, C. Schaupp, E. Stacy, and G. Ankley. Verification of In Vivo Estrogenic Activity for Four Per- and Polyfluoroalkyl Substances (PFAS) Identified as Estrogen Receptor Agonists via New Approach Methodologies.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(9): 3794-3803, (2023).",
             "distribution": [
                 {
-                    "title": "PFAS ER Studies_Science Hub_v4a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528334/PFAS%20ER%20Studies_Science%20Hub_v4a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PFAS ER Studies_Science Hub_v4a.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528334",
+            "keyword": [
+                "PFAS",
+                "endocrine",
+                "ecological risk",
+                "high throughput",
+                "Adverse Outcome Pathways (AOPs)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-09",
-            "references": [
-                "https://doi.org/10.1021/acs.est.2c09315"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192763,51 +192757,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.2c09315"
+            ],
+            "rights": null,
+            "title": "Verification of in vivo estrogenic activity for four per- and polyfluoroalkyl substances (PFAS) identified as estrogen receptor agonists via new approach methodologies (v4)"
         },
         {
-            "title": "Dose Response, Dosimetric, and Metabolic Evaluations of Replacement PFAS Perfluoro-(2,5,8-trimethyl-3,6,9-trioxadodecanoic) Acid (HFPO-TeA)",
-            "description": "The supporting information can be downloaded at: https://www.mdpi.com/article/10.3390/toxics11120951/s1. Text S1: Chemicals; Text S2: Thyroid Hormone Chemicals and Analysis; Text S3: In Vivo Statistics; Text S4: Plasma Dosimetry Chemicals, Materials, and Analysis; Text S5: Normalization of Dosimetry Data Calculations; Text S6: Liver Dosimetry Chemicals, Materials, and Analysis; Text S7: Liver-to-Plasma Partitioning Calculations; Text S8: Non-Targeted Analysis Method and Data Processing; Text S9: Hepatocyte Metabolic Stability Assay Materials, Chemicals, and Calculations; Text S10: Plasma Protein Binding Materials, Chemicals, Assay Design, and Calculations; Text S11: In Vitro\u2013In Vivo Extrapolation (IVIVE) Calculations. Table S1: Data processing parameters used with Sciex OS 3.0; Table S2: Data processing parameters used with Sciex MarkerView 1.3.1; Table S3: Chemical identification, vendor, purity, and experiment usage for all analytes and internal standards; Table S4: Mobile phase gradient for targeted analysis of thyroid hormones in plasma on a Sciex 6500+ QTRAP. Both mobile phases contained 0.1% formic acid as an additive; Table S5: Various instrument conditions for plasma thyroid hormone quantitation on a Sciex 6500+ QTRAP; Table S6: Monitored transitions for analysis of thyroid hormones and 13C-labeled internal standards on a Sciex 6500+ QTRAP. All ions were acquired in positive ion mode; Table S7: Mobile phase gradient for targeted analysis of HFPO-TeA on a Sciex X500R QTOF/MS. Both mobile phases contained ammonium formate (4 mM) as an additive; Table S8: Various instrument conditions for sample analysis on a Sciex X500R QTOF/MS; Table S9: Monitored transitions for analysis of HFPO-TeA using PFHxDA as an internal standard on a Sciex X500R QTOF/MS. The ion of m/z 350.97 is the in-source fragment formed from the HFPO-TeA molecular ion of m/z 660.97. All ions were acquired in negative ion mode; Table S10: Mobile phase gradient for non-targeted analysis on a Sciex X500R QTOF/MS. Ammonium formate (4 mM) was present in both mobile phases as an additive; Table S11: Mobile phase gradient for targeted analysis of HFPO-TeA on a Waters Xevo-TQS. Both mobile phases contained the additive ammonium acetate (2.5 mM); Table S12: Various instrument conditions for hepatocyte clearance and protein plasma binding assays on a Waters Xevo-TQS; Table S13: Monitored transitions for analysis of the in vitro analytes using a Waters Xevo-TQS; Table S14: Individual body weights, absolute liver weights, and relative liver weights for all rats after 5 days of exposure; Table S15: Individual concentrations for plasma T3, rT3, and T4 in all rats after 5 days of exposure to HFPO-TeA. N/A = Calculation not completed due the majority of samples being below the LOQ; Table S16: Individual HFPO-TeA plasma and plasma extract concentrations for all rats after 2 h of exposure... \n\nThis dataset is associated with the following publication:\nRenyer, A., K. Ravindra, B. Wetmore, J. Ford, M. Devito, M. Hughes, L. Wehmas, and D. Macmillan. Dose Response, Dosimetric, and Metabolic Evaluations of Replacement PFAS Perfluoro-(2,5,8-trimethyl-3,6,9-trioxadodecanoic) Acid (HFPO-TeA).   Toxics. MDPI, Basel,  SWITZERLAND, 11(12): 951, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529959",
-            "keyword": [
-                "plasma protein binding",
-                "PFAS",
-                "thyroid disruption",
-                "hepatic clearance",
-                "dosimetry",
-                "IVIVE",
-                "PFECA",
-                "non-targeted analysis"
-            ],
             "contactPoint": {
                 "fn": "Denise Macmillan",
                 "hasEmail": "mailto:macmillan.denise@epa.gov"
             },
+            "description": "The supporting information can be downloaded at: https://www.mdpi.com/article/10.3390/toxics11120951/s1. Text S1: Chemicals; Text S2: Thyroid Hormone Chemicals and Analysis; Text S3: In Vivo Statistics; Text S4: Plasma Dosimetry Chemicals, Materials, and Analysis; Text S5: Normalization of Dosimetry Data Calculations; Text S6: Liver Dosimetry Chemicals, Materials, and Analysis; Text S7: Liver-to-Plasma Partitioning Calculations; Text S8: Non-Targeted Analysis Method and Data Processing; Text S9: Hepatocyte Metabolic Stability Assay Materials, Chemicals, and Calculations; Text S10: Plasma Protein Binding Materials, Chemicals, Assay Design, and Calculations; Text S11: In Vitro\u2013In Vivo Extrapolation (IVIVE) Calculations. Table S1: Data processing parameters used with Sciex OS 3.0; Table S2: Data processing parameters used with Sciex MarkerView 1.3.1; Table S3: Chemical identification, vendor, purity, and experiment usage for all analytes and internal standards; Table S4: Mobile phase gradient for targeted analysis of thyroid hormones in plasma on a Sciex 6500+ QTRAP. Both mobile phases contained 0.1% formic acid as an additive; Table S5: Various instrument conditions for plasma thyroid hormone quantitation on a Sciex 6500+ QTRAP; Table S6: Monitored transitions for analysis of thyroid hormones and 13C-labeled internal standards on a Sciex 6500+ QTRAP. All ions were acquired in positive ion mode; Table S7: Mobile phase gradient for targeted analysis of HFPO-TeA on a Sciex X500R QTOF/MS. Both mobile phases contained ammonium formate (4 mM) as an additive; Table S8: Various instrument conditions for sample analysis on a Sciex X500R QTOF/MS; Table S9: Monitored transitions for analysis of HFPO-TeA using PFHxDA as an internal standard on a Sciex X500R QTOF/MS. The ion of m/z 350.97 is the in-source fragment formed from the HFPO-TeA molecular ion of m/z 660.97. All ions were acquired in negative ion mode; Table S10: Mobile phase gradient for non-targeted analysis on a Sciex X500R QTOF/MS. Ammonium formate (4 mM) was present in both mobile phases as an additive; Table S11: Mobile phase gradient for targeted analysis of HFPO-TeA on a Waters Xevo-TQS. Both mobile phases contained the additive ammonium acetate (2.5 mM); Table S12: Various instrument conditions for hepatocyte clearance and protein plasma binding assays on a Waters Xevo-TQS; Table S13: Monitored transitions for analysis of the in vitro analytes using a Waters Xevo-TQS; Table S14: Individual body weights, absolute liver weights, and relative liver weights for all rats after 5 days of exposure; Table S15: Individual concentrations for plasma T3, rT3, and T4 in all rats after 5 days of exposure to HFPO-TeA. N/A = Calculation not completed due the majority of samples being below the LOQ; Table S16: Individual HFPO-TeA plasma and plasma extract concentrations for all rats after 2 h of exposure... \n\nThis dataset is associated with the following publication:\nRenyer, A., K. Ravindra, B. Wetmore, J. Ford, M. Devito, M. Hughes, L. Wehmas, and D. Macmillan. Dose Response, Dosimetric, and Metabolic Evaluations of Replacement PFAS Perfluoro-(2,5,8-trimethyl-3,6,9-trioxadodecanoic) Acid (HFPO-TeA).   Toxics. MDPI, Basel,  SWITZERLAND, 11(12): 951, (2023).",
             "distribution": [
                 {
-                    "title": "Tables and Figures.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529959/Tables%20and%20Figures.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Tables and Figures.pdf"
                 },
                 {
-                    "title": "Calculations Sheet.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529959/Calculations%20Sheet.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Calculations Sheet.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529959",
+            "keyword": [
+                "plasma protein binding",
+                "PFAS",
+                "thyroid disruption",
+                "hepatic clearance",
+                "dosimetry",
+                "IVIVE",
+                "PFECA",
+                "non-targeted analysis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-18",
-            "references": [
-                "https://doi.org/10.3390/toxics11120951",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10747602"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192817,68 +192810,69 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxics11120951",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10747602"
+            ],
+            "rights": null,
+            "title": "Dose Response, Dosimetric, and Metabolic Evaluations of Replacement PFAS Perfluoro-(2,5,8-trimethyl-3,6,9-trioxadodecanoic) Acid (HFPO-TeA)"
         },
         {
-            "title": "From Protein Sequence to Structure: The Next Frontier in Cross-Species Extrapolation for Chemical Safety Evaluations",
-            "description": "Supplemental data for \"LaLone CA, Blatz DJ, Jensen MA, Vliet SMF, Mayasich S, Mattingly KZ, Transue TR, Melendez W, Wilkinson A, Simmons CW, Ng C, Zhang C, Zhang Y. From Protein Sequence to Structure: The Next Frontier in Cross-Species Extrapolation for Chemical Safety Evaluations. Environ Toxicol Chem. 2023 Feb;42(2):463-474. doi: 10.1002/etc.5537. Epub 2023 Jan 16. PMID: 36524855.\". \n\nThis dataset is associated with the following publication:\nLalone, C., D. Blatz, M. Jensen, S. Vliet, S. Mayasich, K. Mattingly, T. Transue, W. Melendez, A. Wilkinson, C. Simmons, C. Ng, C. Zhang, and Y. Zhang. From Protein Sequence to Structure: The Next Frontier in Cross-Species Extrapolation for Chemical Safety Evaluations.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 463-474, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530080",
-            "keyword": [
-                "bioinformatics",
-                "Protein Structure",
-                "Species Extrapolation",
-                "SeqAPASS",
-                "Predictive Toxicology",
-                "computational toxicology"
-            ],
             "contactPoint": {
                 "fn": "Carlie LaLone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Supplemental data for \"LaLone CA, Blatz DJ, Jensen MA, Vliet SMF, Mayasich S, Mattingly KZ, Transue TR, Melendez W, Wilkinson A, Simmons CW, Ng C, Zhang C, Zhang Y. From Protein Sequence to Structure: The Next Frontier in Cross-Species Extrapolation for Chemical Safety Evaluations. Environ Toxicol Chem. 2023 Feb;42(2):463-474. doi: 10.1002/etc.5537. Epub 2023 Jan 16. PMID: 36524855.\". \n\nThis dataset is associated with the following publication:\nLalone, C., D. Blatz, M. Jensen, S. Vliet, S. Mayasich, K. Mattingly, T. Transue, W. Melendez, A. Wilkinson, C. Simmons, C. Ng, C. Zhang, and Y. Zhang. From Protein Sequence to Structure: The Next Frontier in Cross-Species Extrapolation for Chemical Safety Evaluations.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 463-474, (2023).",
             "distribution": [
                 {
-                    "title": "etc5537-sup-0003-supplemental_data_s3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530080/etc5537-sup-0003-supplemental_data_s3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "etc5537-sup-0003-supplemental_data_s3.xlsx"
                 },
                 {
-                    "title": "etc5537-sup-0002-supplemental_data_s2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530080/etc5537-sup-0002-supplemental_data_s2.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "etc5537-sup-0002-supplemental_data_s2.docx"
                 },
                 {
-                    "title": "etc5537-sup-0001-supplemental_data_s1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530080/etc5537-sup-0001-supplemental_data_s1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "etc5537-sup-0001-supplemental_data_s1.xlsx"
                 },
                 {
-                    "title": "etc5537-sup-0006-additional_supporting_information.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530080/etc5537-sup-0006-additional_supporting_information.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "etc5537-sup-0006-additional_supporting_information.zip"
                 },
                 {
-                    "title": "etc5537-sup-0005-supplemental_data_s5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530080/etc5537-sup-0005-supplemental_data_s5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "etc5537-sup-0005-supplemental_data_s5.xlsx"
                 },
                 {
-                    "title": "etc5537-sup-0004-supplemental_data_s4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530080/etc5537-sup-0004-supplemental_data_s4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "etc5537-sup-0004-supplemental_data_s4.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530080",
+            "keyword": [
+                "bioinformatics",
+                "Protein Structure",
+                "Species Extrapolation",
+                "SeqAPASS",
+                "Predictive Toxicology",
+                "computational toxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-06",
-            "references": [
-                "https://doi.org/10.1002/etc.5537"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192888,19 +192882,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5537"
+            ],
+            "rights": null,
+            "title": "From Protein Sequence to Structure: The Next Frontier in Cross-Species Extrapolation for Chemical Safety Evaluations"
         },
         {
-            "title": "Development and application of a systematic and quantitative weighting framework to evaluate the quality and relevance of relative potency estimates for dioxin-like compounds (DLCs) for human health risk assessment",
-            "description": "Supplementary data for \"Wikoff D, Ring C, DeVito M, Walker N, Birnbaum L, Haws L. Development and application of a systematic and quantitative weighting framework to evaluate the quality and relevance of relative potency estimates for dioxin-like compounds (DLCs) for human health risk assessment. Regul Toxicol Pharmacol. 2023 Dec;145:105500. doi: 10.1016/j.yrtph.2023.105500. Epub 2023 Oct 21. PMID: 37866700.\". \n\nThis dataset is associated with the following publication:\nWikoff, D., C. Ring, M. Devito, N. Walker, L. Birnbaum, and L. Haws. Development and application of a systematic and quantitative weighting framework to evaluate the quality and relevance of relative potency estimates for dioxin-like compounds (DLCs) for human health risk assessment.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 145: 105500, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Michael Devito",
+                "hasEmail": "mailto:devito.michael@epa.gov"
+            },
+            "description": "Supplementary data for \"Wikoff D, Ring C, DeVito M, Walker N, Birnbaum L, Haws L. Development and application of a systematic and quantitative weighting framework to evaluate the quality and relevance of relative potency estimates for dioxin-like compounds (DLCs) for human health risk assessment. Regul Toxicol Pharmacol. 2023 Dec;145:105500. doi: 10.1016/j.yrtph.2023.105500. Epub 2023 Oct 21. PMID: 37866700.\". \n\nThis dataset is associated with the following publication:\nWikoff, D., C. Ring, M. Devito, N. Walker, L. Birnbaum, and L. Haws. Development and application of a systematic and quantitative weighting framework to evaluate the quality and relevance of relative potency estimates for dioxin-like compounds (DLCs) for human health risk assessment.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 145: 105500, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530093/Supplementary%20data.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary data.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530093",
             "keyword": [
@@ -192916,20 +192920,10 @@
                 "Risk Assessment",
                 "Integration"
             ],
-            "contactPoint": {
-                "fn": "Michael Devito",
-                "hasEmail": "mailto:devito.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Supplementary data.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530093/Supplementary%20data.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-09-28",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2023.105500"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192939,19 +192933,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2023.105500"
+            ],
+            "rights": null,
+            "title": "Development and application of a systematic and quantitative weighting framework to evaluate the quality and relevance of relative potency estimates for dioxin-like compounds (DLCs) for human health risk assessment"
         },
         {
-            "title": "High-Throughput Transcriptomics of Water Extracts Detects Reductions in Biological Activity with Water Treatment Processes",
-            "description": "Dataset for Rogers, et al., 'High-Throughput Transcriptomics of Water Extracts Detects Reductions in Biological Activity with Water Treatment Processes', published in Environmental Science & Technology, doi https://doi.org/10.1021/acs.est.3c07525. Contains 7 files \nHTTr analysis of water extracts_SI_v3: Supplemental information with detailed descriptions of cell culture, exposure to water extracts, cell viability assays, HTTr assay, and HTTr data processing, and Figures S1\u2013S4 detailing cell viability results, HTTr quality control results, signature-level potency magnitude comparisons, and gene/signature activity of laboratory blanks (PDF)\nTable S1: well-level cell viability metrics for water extracts (XLSX)\nTable S2: treatment-level cell viability metrics for water extracts (XLSX)\nTable S3: well-level HTTr quality control metrics for water extracts (XLSX)\nTable S4: signature collection used for HTTr signature concentration\u2013response modeling (XLSX)\nTable S5: signature concentration-modeling profiling results for water extracts (XLSX)\nTable S6: gene concentration-modeling profiling results for water extracts (XLSX). \n\nThis dataset is associated with the following publication:\nRogers, J., F. Leusch, B. Chambers, K. Daniels, L. Everett, R. Judson, K. Maruya, A. Mehinto, P. Neale, K. Friedman, R. Thomas, S. Snyder, and J. Harrill. High-Throughput Transcriptomics of Water Extracts Detects Reductions in Biological Activity with Water Treatment Processes.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58(4): 2027-2037, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Joshua Harrill",
+                "hasEmail": "mailto:harrill.joshua@epa.gov"
+            },
+            "description": "Dataset for Rogers, et al., 'High-Throughput Transcriptomics of Water Extracts Detects Reductions in Biological Activity with Water Treatment Processes', published in Environmental Science & Technology, doi https://doi.org/10.1021/acs.est.3c07525. Contains 7 files \nHTTr analysis of water extracts_SI_v3: Supplemental information with detailed descriptions of cell culture, exposure to water extracts, cell viability assays, HTTr assay, and HTTr data processing, and Figures S1\u2013S4 detailing cell viability results, HTTr quality control results, signature-level potency magnitude comparisons, and gene/signature activity of laboratory blanks (PDF)\nTable S1: well-level cell viability metrics for water extracts (XLSX)\nTable S2: treatment-level cell viability metrics for water extracts (XLSX)\nTable S3: well-level HTTr quality control metrics for water extracts (XLSX)\nTable S4: signature collection used for HTTr signature concentration\u2013response modeling (XLSX)\nTable S5: signature concentration-modeling profiling results for water extracts (XLSX)\nTable S6: gene concentration-modeling profiling results for water extracts (XLSX). \n\nThis dataset is associated with the following publication:\nRogers, J., F. Leusch, B. Chambers, K. Daniels, L. Everett, R. Judson, K. Maruya, A. Mehinto, P. Neale, K. Friedman, R. Thomas, S. Snyder, and J. Harrill. High-Throughput Transcriptomics of Water Extracts Detects Reductions in Biological Activity with Water Treatment Processes.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58(4): 2027-2037, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65c5075ae4b063812d6939f9",
+                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65c5075ae4b063812d6939f9"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530112",
             "keyword": [
@@ -192962,19 +192965,10 @@
                 "water quality",
                 "Water Cycle"
             ],
-            "contactPoint": {
-                "fn": "Joshua Harrill",
-                "hasEmail": "mailto:harrill.joshua@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65c5075ae4b063812d6939f9",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65c5075ae4b063812d6939f9"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-27",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c07525"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -192984,59 +192978,59 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c07525"
+            ],
+            "rights": null,
+            "title": "High-Throughput Transcriptomics of Water Extracts Detects Reductions in Biological Activity with Water Treatment Processes"
         },
         {
-            "title": "Combination of computational new approach methodologies for enhancing evidence of biological pathway conservation across species",
-            "description": "Supplementary data for \"Peter Schumann, Claudia Rivetti, Jade Houghton, Bruno Campos, Geoff Hodges, Carlie LaLone, Combination of computational new approach methodologies for enhancing evidence of biological pathway conservation across species, Science of The Total Environment, Volume 912, 2024, 168573, ISSN 0048-9697, https://doi.org/10.1016/j.scitotenv.2023.168573.\". \n\nThis dataset is associated with the following publication:\nSchumann, P., C. Rivetti, J. Houghton, B. Campos, G. Hodges, and C. LaLone. Combination of computational new approach methodologies for enhancing evidence of biological pathway conservation across species.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 912: 168573, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530084",
-            "keyword": [
-                "ecotoxicology",
-                "Species conservation analysis",
-                "Genes to pathways",
-                "SeqAPASS",
-                "new approach methodologies",
-                "Biological pathways",
-                "In silico methods"
-            ],
             "contactPoint": {
                 "fn": "Carlie LaLone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Supplementary data for \"Peter Schumann, Claudia Rivetti, Jade Houghton, Bruno Campos, Geoff Hodges, Carlie LaLone, Combination of computational new approach methodologies for enhancing evidence of biological pathway conservation across species, Science of The Total Environment, Volume 912, 2024, 168573, ISSN 0048-9697, https://doi.org/10.1016/j.scitotenv.2023.168573.\". \n\nThis dataset is associated with the following publication:\nSchumann, P., C. Rivetti, J. Houghton, B. Campos, G. Hodges, and C. LaLone. Combination of computational new approach methodologies for enhancing evidence of biological pathway conservation across species.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 912: 168573, (2024).",
             "distribution": [
                 {
-                    "title": "1-s2.0-S0048969723072017-mmc4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530084/1-s2.0-S0048969723072017-mmc4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1-s2.0-S0048969723072017-mmc4.xlsx"
                 },
                 {
-                    "title": "1-s2.0-S0048969723072017-mmc3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530084/1-s2.0-S0048969723072017-mmc3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1-s2.0-S0048969723072017-mmc3.xlsx"
                 },
                 {
-                    "title": "1-s2.0-S0048969723072017-mmc2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530084/1-s2.0-S0048969723072017-mmc2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1-s2.0-S0048969723072017-mmc2.xlsx"
                 },
                 {
-                    "title": "1-s2.0-S0048969723072017-mmc1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530084/1-s2.0-S0048969723072017-mmc1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1-s2.0-S0048969723072017-mmc1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530084",
+            "keyword": [
+                "ecotoxicology",
+                "Species conservation analysis",
+                "Genes to pathways",
+                "SeqAPASS",
+                "new approach methodologies",
+                "Biological pathways",
+                "In silico methods"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-12",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.168573"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193046,116 +193040,116 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.168573"
+            ],
+            "rights": null,
+            "title": "Combination of computational new approach methodologies for enhancing evidence of biological pathway conservation across species"
         },
         {
-            "title": "Effects of multi-walled carbon nano tubes on human lung epithelial BEAS-2B cells",
-            "description": "Dataset for 'Effects of multi-walled carbon nano tubes on human lung epithelial BEAS-2B cells' journal article by Sheau-Fung Thai, et al., to be published in Materials Express.\n\nFor the data set:\nDEG: differentially expressed genes\n33-MWCNT: parent MWCNT \n55-OH-MWCNT: MWCNT modified with -OH group\n66-COOH-MWCNT: MWCNT modified with -COOH group. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, B. Robinette, G. Nelson, A. Tennant, H. Ren, B. Vallanat, A. Astriab Fisher, J. Ross, and K. Kitchin. Effects of multi-walled carbon nanotubes on message and Micro-RNA in human lung BEAS-2B cells.   Materials Express. American Scientific Publishers, VALENCIA, CA, USA, 14(2): 249-263, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529905",
-            "keyword": [
-                "Multi-walled carbon nanotubes",
-                "signaling pathways",
-                "microrna",
-                "Target Filter Analysis"
-            ],
             "contactPoint": {
                 "fn": "Sheau-Fung Thai",
                 "hasEmail": "mailto:thai.sheau-fung@epa.gov"
             },
+            "description": "Dataset for 'Effects of multi-walled carbon nano tubes on human lung epithelial BEAS-2B cells' journal article by Sheau-Fung Thai, et al., to be published in Materials Express.\n\nFor the data set:\nDEG: differentially expressed genes\n33-MWCNT: parent MWCNT \n55-OH-MWCNT: MWCNT modified with -OH group\n66-COOH-MWCNT: MWCNT modified with -COOH group. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, B. Robinette, G. Nelson, A. Tennant, H. Ren, B. Vallanat, A. Astriab Fisher, J. Ross, and K. Kitchin. Effects of multi-walled carbon nanotubes on message and Micro-RNA in human lung BEAS-2B cells.   Materials Express. American Scientific Publishers, VALENCIA, CA, USA, 14(2): 249-263, (2024).",
             "distribution": [
                 {
-                    "title": "DEG-0.05-GRC337_resultsubset_55_low - .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC337_resultsubset_55_low%20-%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC337_resultsubset_55_low - .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC337_resultsubset_55_10.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC337_resultsubset_55_10.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC337_resultsubset_55_10.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC337_resultsubset_55_3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC337_resultsubset_55_3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC337_resultsubset_55_3.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC337_resultsubset_55_1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC337_resultsubset_55_1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC337_resultsubset_55_1.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_66_low .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_66_low%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_66_low .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_66_30 .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_66_30%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_66_30 .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_66_10 .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_66_10%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_66_10 .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_66_3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_66_3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_66_3.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_66_1 .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_66_1%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_66_1 .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_55_30 .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_55_30%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_55_30 .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_33_low .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_33_low%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_33_low .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_33_30.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_33_30.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_33_30.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_33_10.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_33_10.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_33_10.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_33_3 .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_33_3%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_33_3 .xlsx"
                 },
                 {
-                    "title": "DEG-0.05-GRC336_resultsubset_33_1 .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/DEG-0.05-GRC336_resultsubset_33_1%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-GRC336_resultsubset_33_1 .xlsx"
                 },
                 {
-                    "title": "all signaling pathway IPA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529905/all%20signaling%20pathway%20IPA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "all signaling pathway IPA.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529905",
+            "keyword": [
+                "Multi-walled carbon nanotubes",
+                "signaling pathways",
+                "microrna",
+                "Target Filter Analysis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-05-04",
-            "references": [
-                "https://doi.org/10.1166/mex.2024.2620"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193165,19 +193159,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1166/mex.2024.2620"
+            ],
+            "rights": null,
+            "title": "Effects of multi-walled carbon nano tubes on human lung epithelial BEAS-2B cells"
         },
         {
-            "title": "Climate change will impact surface water extents across the central United States - underlying data",
-            "description": "surface water data and projections produced for 32 sites in the central US. Surface water data consists of open and vegetated surface water 2 week averages from 2017-2021. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., J. Christensen, L. Alexander, C. Lane, and H. Golden. Climate Change Will Impact Surface Water Extents and Dynamics Across the Central United States.   Earth\ufffds Future. John Wiley & Sons, Inc., Hoboken, NJ, USA, 12(2): e2023EF004106, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jay Christensen",
+                "hasEmail": "mailto:christensen.jay@epa.gov"
+            },
+            "description": "surface water data and projections produced for 32 sites in the central US. Surface water data consists of open and vegetated surface water 2 week averages from 2017-2021. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., J. Christensen, L. Alexander, C. Lane, and H. Golden. Climate Change Will Impact Surface Water Extents and Dynamics Across the Central United States.   Earth\ufffds Future. John Wiley & Sons, Inc., Hoboken, NJ, USA, 12(2): e2023EF004106, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.5066/P9UOACNH",
+                    "title": "https://doi.org/10.5066/P9UOACNH"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529434",
             "keyword": [
@@ -193192,19 +193195,10 @@
                 "climate change",
                 "wetlands"
             ],
-            "contactPoint": {
-                "fn": "Jay Christensen",
-                "hasEmail": "mailto:christensen.jay@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.5066/P9UOACNH",
-                    "accessURL": "https://doi.org/10.5066/P9UOACNH"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-17",
-            "references": [
-                "https://doi.org/10.1029/2023ef004106"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193214,47 +193208,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2023ef004106"
+            ],
+            "rights": null,
+            "title": "Climate change will impact surface water extents across the central United States - underlying data"
         },
         {
-            "title": "Establishing performance metrics for quantitative non-targeted analysis: a demonstration using per- and poly-fluoroalkyl substances",
-            "description": "Non-targeted analysis (NTA) is an increasingly popular technique for characterizing undefined chemical analytes. Generating quantitative NTA (qNTA) concentration estimates requires the use of training data from calibration \u201csurrogates\u201d. The use of surrogate training data can yield diminished performance of concentration estimation approaches. In order to evaluate performance differences between targeted and qNTA approaches, we defined new metrics that convey predictive accuracy, uncertainty (using 95% inverse confidence intervals), and reliability (the extent to which confidence intervals contain true values). We calculated and examined these newly defined metrics across five quantitative approaches applied to a mixture of 29 per- and polyfluoroalkyl substances (PFAS). The quantitative approaches spanned a traditional targeted design using chemical-specific calibration curves to a generalizable qNTA design using bootstrap-sampled calibration values from chemical surrogates. \n\nThis dataset is associated with the following publication:\nPu, S., J. McCord, J. Bangma, and J. Sobus. Establishing performance metrics for quantitative non-targeted analysis: a demonstration using per- and polyfluoroalkyl substances.   Analytical and Bioanalytical Chemistry. Springer, New York, NY, USA, 416: 1249-1267, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529977",
-            "keyword": [
-                "qNTA",
-                "chemical analytes",
-                "PFAS",
-                "performance metrics"
-            ],
             "contactPoint": {
                 "fn": "Jon Sobus",
                 "hasEmail": "mailto:sobus.jon@epa.gov"
             },
+            "description": "Non-targeted analysis (NTA) is an increasingly popular technique for characterizing undefined chemical analytes. Generating quantitative NTA (qNTA) concentration estimates requires the use of training data from calibration \u201csurrogates\u201d. The use of surrogate training data can yield diminished performance of concentration estimation approaches. In order to evaluate performance differences between targeted and qNTA approaches, we defined new metrics that convey predictive accuracy, uncertainty (using 95% inverse confidence intervals), and reliability (the extent to which confidence intervals contain true values). We calculated and examined these newly defined metrics across five quantitative approaches applied to a mixture of 29 per- and polyfluoroalkyl substances (PFAS). The quantitative approaches spanned a traditional targeted design using chemical-specific calibration curves to a generalizable qNTA design using bootstrap-sampled calibration values from chemical surrogates. \n\nThis dataset is associated with the following publication:\nPu, S., J. McCord, J. Bangma, and J. Sobus. Establishing performance metrics for quantitative non-targeted analysis: a demonstration using per- and polyfluoroalkyl substances.   Analytical and Bioanalytical Chemistry. Springer, New York, NY, USA, 416: 1249-1267, (2024).",
             "distribution": [
                 {
-                    "title": "Pu_et_al_qNTA_metric_Supplementary_File_2.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529977/Pu_et_al_qNTA_metric_Supplementary_File_2.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Pu_et_al_qNTA_metric_Supplementary_File_2.zip"
                 },
                 {
-                    "title": "Pu_et_al_2023_qNTA_metrics_Supplementary_File_5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529977/Pu_et_al_2023_qNTA_metrics_Supplementary_File_5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Pu_et_al_2023_qNTA_metrics_Supplementary_File_5.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529977",
+            "keyword": [
+                "qNTA",
+                "chemical analytes",
+                "PFAS",
+                "performance metrics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-04",
-            "references": [
-                "https://doi.org/10.1007/s00216-023-05117-4",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10850229"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193264,96 +193257,97 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s00216-023-05117-4",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10850229"
+            ],
+            "rights": null,
+            "title": "Establishing performance metrics for quantitative non-targeted analysis: a demonstration using per- and poly-fluoroalkyl substances"
         },
         {
-            "title": "Mass spec data from AFFF headspace and combustion",
-            "description": "This data represents processed data from chemical ionization time of flight mass spectrometry instrument used to generate each figure in the manuscript. A data dictionary is included in the dataset. \n\nThis dataset is associated with the following publication:\nMattila, J., J. Krug, W. Roberson, R. Burnette, S. McDonald, P. Virtaranta, J. Offenberg, and W. Linak. Characterizing volatile emissions and combustion by-products from aqueous film-forming foams using online chemical ionization mass spectrometry.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  0, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529810",
-            "keyword": [
-                "PFAS",
-                "thermal treatment",
-                "AFFF",
-                "Chemical Ionization Mass Spectrometry"
-            ],
             "contactPoint": {
                 "fn": "Jonathan Krug",
                 "hasEmail": "mailto:krug.jonathan@epa.gov"
             },
+            "description": "This data represents processed data from chemical ionization time of flight mass spectrometry instrument used to generate each figure in the manuscript. A data dictionary is included in the dataset. \n\nThis dataset is associated with the following publication:\nMattila, J., J. Krug, W. Roberson, R. Burnette, S. McDonald, P. Virtaranta, J. Offenberg, and W. Linak. Characterizing volatile emissions and combustion by-products from aqueous film-forming foams using online chemical ionization mass spectrometry.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  0, (2024).",
             "distribution": [
                 {
-                    "title": "FigureS8.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/FigureS8.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FigureS8.txt"
                 },
                 {
-                    "title": "FigureS7.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/FigureS7.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FigureS7.txt"
                 },
                 {
-                    "title": "FigureS6.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/FigureS6.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FigureS6.txt"
                 },
                 {
-                    "title": "FigureS5.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/FigureS5.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FigureS5.txt"
                 },
                 {
-                    "title": "FigureS4.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/FigureS4.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FigureS4.txt"
                 },
                 {
-                    "title": "FigureS3.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/FigureS3.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FigureS3.txt"
                 },
                 {
-                    "title": "FigureS1.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/FigureS1.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FigureS1.txt"
                 },
                 {
-                    "title": "Figure4.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/Figure4.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure4.txt"
                 },
                 {
-                    "title": "Figure3.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/Figure3.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure3.txt"
                 },
                 {
-                    "title": "Figure2.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/Figure2.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure2.txt"
                 },
                 {
-                    "title": "Figure1.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/Figure1.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure1.txt"
                 },
                 {
-                    "title": "Data dictionary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529810/Data%20dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data dictionary.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529810",
+            "keyword": [
+                "PFAS",
+                "thermal treatment",
+                "AFFF",
+                "Chemical Ionization Mass Spectrometry"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-17",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c09255"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193363,19 +193357,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c09255"
+            ],
+            "rights": null,
+            "title": "Mass spec data from AFFF headspace and combustion"
         },
         {
-            "title": "Data used in the analysis documented in \"Revisiting Day-of-Week Ozone Patterns in an Era of Evolving U.S. Air Quality\"",
-            "description": "This dataset hosted at https://zenodo.org/records/10222897 contains observed and CMAQ estimated gas species data and meteorological data that were used in the analysis documented in the manuscript \"Revisiting Day-of-Week Ozone Patterns in an Era of Evolving U.S. Air Quality\".  The files are packages as a set of .tar.gz files with a corresponding Data Dictionary that contains meta data for each data file. \n\nThis dataset is associated with the following publication:\nSimon, H., C. Hogrefe, A. Whitehill, K. Foley, J. Liljegren, N. Possiel, B. Wells, B. Henderson, L. Valin, G. Tonnesen, K. Appel, and S. Koplitz. Revisiting day-of-week ozone patterns in an era of evolving US air quality.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 24(3): 1855-1871, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Christian Hogrefe",
+                "hasEmail": "mailto:hogrefe.christian@epa.gov"
+            },
+            "description": "This dataset hosted at https://zenodo.org/records/10222897 contains observed and CMAQ estimated gas species data and meteorological data that were used in the analysis documented in the manuscript \"Revisiting Day-of-Week Ozone Patterns in an Era of Evolving U.S. Air Quality\".  The files are packages as a set of .tar.gz files with a corresponding Data Dictionary that contains meta data for each data file. \n\nThis dataset is associated with the following publication:\nSimon, H., C. Hogrefe, A. Whitehill, K. Foley, J. Liljegren, N. Possiel, B. Wells, B. Henderson, L. Valin, G. Tonnesen, K. Appel, and S. Koplitz. Revisiting day-of-week ozone patterns in an era of evolving US air quality.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 24(3): 1855-1871, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://zenodo.org/records/10222897",
+                    "title": "https://zenodo.org/records/10222897"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529980",
             "keyword": [
@@ -193385,19 +193388,10 @@
                 "Weekday",
                 "EQUATES"
             ],
-            "contactPoint": {
-                "fn": "Christian Hogrefe",
-                "hasEmail": "mailto:hogrefe.christian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://zenodo.org/records/10222897",
-                    "accessURL": "https://zenodo.org/records/10222897"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-29",
-            "references": [
-                "https://doi.org/10.5194/acp-24-1855-2024"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193407,40 +193401,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-24-1855-2024"
+            ],
+            "rights": null,
+            "title": "Data used in the analysis documented in \"Revisiting Day-of-Week Ozone Patterns in an Era of Evolving U.S. Air Quality\""
         },
         {
-            "title": "Building Resilience to Extreme Weather Events in Phoenix: Considering Contaminated Sites and Under-resourced Communities",
-            "description": "The dataset includes tables of the 58 indicator datasets (dataset descriptions, data formats, links to publicly available data sources for producing GIS data layers). \n\nThis dataset is associated with the following publications:\nSinha, P., M. Fry, S. Julius, R. Truesdale, J. Cajka, M. Eddy, P. Doraiswamy, R. Albright, J. Riemenschneider, M. Potzler, B. Lim, J. Richkus, and M. O'Neal. Building Resilience to Extreme Weather Events in Phoenix: Considering Contaminated Sites and Under-resourced Communities.   Climate Risk Management. Elsevier B.V., Amsterdam,  NETHERLANDS, 43: 100586, (2024).\nSinha, P., R. Truesdale, M. Fry, and S. Julius. Handbook on Indicators of Community Vulnerability to Extreme Events: Considering Sites and Waste Management Facilities. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.\nSinha, P., S. Julius, M. Fry, R. Truesdale, J. Cajka, M. Eddy , P. Doraiswamya, and D. Womacka. Assessing community vulnerability to extreme events in the presence of contaminated sites and waste management facilities: An indicator approach.   Urban Climate. Elsevier Science, New York, NY,   53(101800): 1-30, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530277",
-            "keyword": [
-                "indicators",
-                "Vulnerability"
-            ],
             "contactPoint": {
                 "fn": "Meridith Fry",
                 "hasEmail": "mailto:fry.meridith@epa.gov"
             },
+            "description": "The dataset includes tables of the 58 indicator datasets (dataset descriptions, data formats, links to publicly available data sources for producing GIS data layers). \n\nThis dataset is associated with the following publications:\nSinha, P., M. Fry, S. Julius, R. Truesdale, J. Cajka, M. Eddy, P. Doraiswamy, R. Albright, J. Riemenschneider, M. Potzler, B. Lim, J. Richkus, and M. O'Neal. Building Resilience to Extreme Weather Events in Phoenix: Considering Contaminated Sites and Under-resourced Communities.   Climate Risk Management. Elsevier B.V., Amsterdam,  NETHERLANDS, 43: 100586, (2024).\nSinha, P., R. Truesdale, M. Fry, and S. Julius. Handbook on Indicators of Community Vulnerability to Extreme Events: Considering Sites and Waste Management Facilities. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.\nSinha, P., S. Julius, M. Fry, R. Truesdale, J. Cajka, M. Eddy , P. Doraiswamya, and D. Womacka. Assessing community vulnerability to extreme events in the presence of contaminated sites and waste management facilities: An indicator approach.   Urban Climate. Elsevier Science, New York, NY,   53(101800): 1-30, (2024).",
             "distribution": [
                 {
-                    "title": "https://assessments.epa.gov/risk/document/&deid=358458",
-                    "accessURL": "https://assessments.epa.gov/risk/document/&deid=358458"
+                    "accessURL": "https://assessments.epa.gov/risk/document/&deid=358458",
+                    "title": "https://assessments.epa.gov/risk/document/&deid=358458"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530277",
+            "keyword": [
+                "indicators",
+                "Vulnerability"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-01",
-            "references": [
-                "https://doi.org/10.1016/j.crm.2024.100586",
-                "https://www.epa.gov/research",
-                "https://doi.org/10.1016/j.uclim.2023.101800"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193450,19 +193442,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.crm.2024.100586",
+                "https://www.epa.gov/research",
+                "https://doi.org/10.1016/j.uclim.2023.101800"
+            ],
+            "rights": null,
+            "title": "Building Resilience to Extreme Weather Events in Phoenix: Considering Contaminated Sites and Under-resourced Communities"
         },
         {
-            "title": "Linked data for Wildfire Impact Modeling with Counterfactual Probabilistic Analysis",
-            "description": "The datasets analyzed for this study can be found in the USDA Forest Service Research Data Archive. The \"date of last update\" was required in this entry but I could not find exact information on this in the Forest Service data repository website but metadata indicated April of 2022 upload. \n\nThis dataset is associated with the following publication:\nThompson, M.P., and J.F. Carriger. Avoided wildfire impact modeling with counterfactual probabilistic analysis.  Luciana Ghermandi  Frontiers in Forests and Global Change. Frontiers, Lausanne,  SWITZERLAND, 6: 1266413, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Carriger",
+                "hasEmail": "mailto:carriger.john@epa.gov"
+            },
+            "description": "The datasets analyzed for this study can be found in the USDA Forest Service Research Data Archive. The \"date of last update\" was required in this entry but I could not find exact information on this in the Forest Service data repository website but metadata indicated April of 2022 upload. \n\nThis dataset is associated with the following publication:\nThompson, M.P., and J.F. Carriger. Avoided wildfire impact modeling with counterfactual probabilistic analysis.  Luciana Ghermandi  Frontiers in Forests and Global Change. Frontiers, Lausanne,  SWITZERLAND, 6: 1266413, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.2737/RDS-2022-0026",
+                    "title": "https://doi.org/10.2737/RDS-2022-0026"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529354",
             "keyword": [
@@ -193474,19 +193477,10 @@
                 "mitigation",
                 "effectiveness"
             ],
-            "contactPoint": {
-                "fn": "John Carriger",
-                "hasEmail": "mailto:carriger.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.2737/RDS-2022-0026",
-                    "accessURL": "https://doi.org/10.2737/RDS-2022-0026"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-15",
-            "references": [
-                "https://doi.org/10.3389/ffgc.2023.1266413"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193496,19 +193490,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/ffgc.2023.1266413"
+            ],
+            "rights": null,
+            "title": "Linked data for Wildfire Impact Modeling with Counterfactual Probabilistic Analysis"
         },
         {
-            "title": "Data on county-level forest tree carbon estimates from Reese et al. \"Geographic variation in projected US forest aboveground carbon responses to climate change and atmospheric deposition\"",
-            "description": "This is the data for Reese et al. in Environmental Research Letters  \"Geographic variation in projected US forest aboveground carbon responses to climate change and atmospheric deposition.\" It includes the estimated forest aboveground carbon from 2010 to 2100 for each forested county in the contiguous U.S. across all 20 scenarios analyzed. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Christopher Clark",
+                "hasEmail": "mailto:clark.christopher@epa.gov"
+            },
+            "description": "This is the data for Reese et al. in Environmental Research Letters  \"Geographic variation in projected US forest aboveground carbon responses to climate change and atmospheric deposition.\" It includes the estimated forest aboveground carbon from 2010 to 2100 for each forested county in the contiguous U.S. across all 20 scenarios analyzed. ",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530107/Science%20Hub%20data_Reese%20et%20al_Forest%20carbon%20by%20county%20by%20scenario%202010%20to%202100.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science Hub data_Reese et al_Forest carbon by county by scenario 2010 to 2100.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530107",
             "keyword": [
@@ -193519,19 +193523,11 @@
                 "climate change",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Christopher Clark",
-                "hasEmail": "mailto:clark.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Science Hub data_Reese et al_Forest carbon by county by scenario 2010 to 2100.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530107/Science%20Hub%20data_Reese%20et%20al_Forest%20carbon%20by%20county%20by%20scenario%202010%20to%202100.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-02-06",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -193540,20 +193536,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Data on county-level forest tree carbon estimates from Reese et al. \"Geographic variation in projected US forest aboveground carbon responses to climate change and atmospheric deposition\""
         },
         {
-            "title": "EPA Facilities Status Dashboard",
-            "description": "A portion of the data used is publicly available through John Hopkins Coronavirus Resource Center and CDC COVID Data Tracker. Another portion data is password protected through HHS Protect. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: https://covid.cdc.gov/covid-data-tracker/#county-view and https://coronavirus.jhu.edu/map.html. For the data through HHS Protect, interested parties must submit a request to HHS. Format: Much of the data is publicly available at https://coronavirus.jhu.edu/map.html and https://covid.cdc.gov/covid-data-tracker/#county-view. What is not publicly available is through HHS Protect which is password protected. \n\nThis dataset is associated with the following publication:\nBaxter, L., J. Baynes, A. Weaver, A. Neale, T. Wade, M. Mehaffey, D. Lobdell, K. Widener, and W. Cascio. Development of the United States Environmental Protection Agency\u2019s Facilities Status Dashboard for the COVID-19 Pandemic: Approach and Challenges..   International Journal of Public Health. Springer Basel AG, Basel,  SWITZERLAND, 61(1604761): 9, (2022).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Lisa Baxter",
+                "hasEmail": "mailto:baxter.lisa@epa.gov"
+            },
+            "description": "A portion of the data used is publicly available through John Hopkins Coronavirus Resource Center and CDC COVID Data Tracker. Another portion data is password protected through HHS Protect. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: https://covid.cdc.gov/covid-data-tracker/#county-view and https://coronavirus.jhu.edu/map.html. For the data through HHS Protect, interested parties must submit a request to HHS. Format: Much of the data is publicly available at https://coronavirus.jhu.edu/map.html and https://covid.cdc.gov/covid-data-tracker/#county-view. What is not publicly available is through HHS Protect which is password protected. \n\nThis dataset is associated with the following publication:\nBaxter, L., J. Baynes, A. Weaver, A. Neale, T. Wade, M. Mehaffey, D. Lobdell, K. Widener, and W. Cascio. Development of the United States Environmental Protection Agency\u2019s Facilities Status Dashboard for the COVID-19 Pandemic: Approach and Challenges..   International Journal of Public Health. Springer Basel AG, Basel,  SWITZERLAND, 61(1604761): 9, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1523054",
             "keyword": [
                 "COVID-19",
@@ -193561,15 +193559,10 @@
                 "Risk Communications",
                 "epidemiology"
             ],
-            "contactPoint": {
-                "fn": "Lisa Baxter",
-                "hasEmail": "mailto:baxter.lisa@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-08-25",
-            "references": [
-                "https://doi.org/10.3389/ijph.2022.1604761",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9172581"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193579,51 +193572,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/ijph.2022.1604761",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9172581"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "EPA Facilities Status Dashboard"
         },
         {
-            "title": "Putative adverse outcome pathway development based on physiological responses of female fathead minnows to model estrogen versus androgen receptor agonists",
-            "description": "\"Morshead ML, Jensen KM, Ankley GT, Vliet S, LaLone CA, Aller AV, Watanabe KH, Villeneuve DL. Putative adverse outcome pathway development based on physiological responses of female fathead minnows to model estrogen versus androgen receptor agonists. Aquat Toxicol. 2023 Aug;261:106607. doi: 10.1016/j.aquatox.2023.106607. Epub 2023 Jun 9. PMID: 37354817.\". \n\nThis dataset is associated with the following publication:\nMorshead, M., K. Jensen, G. Ankley, S. Vliet, C. LaLone, D. Villeneuve, A. Vidales Aller, and K. Watanabe. Putative adverse outcome pathway development based on physiological responses of female fathead minnows to model estrogen versus androgen receptor agonists.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 261: 106607, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530091",
-            "keyword": [
-                "Mixture",
-                "adverse outcome pathway",
-                "fish",
-                "reproduction",
-                "endocrine disruption"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "\"Morshead ML, Jensen KM, Ankley GT, Vliet S, LaLone CA, Aller AV, Watanabe KH, Villeneuve DL. Putative adverse outcome pathway development based on physiological responses of female fathead minnows to model estrogen versus androgen receptor agonists. Aquat Toxicol. 2023 Aug;261:106607. doi: 10.1016/j.aquatox.2023.106607. Epub 2023 Jun 9. PMID: 37354817.\". \n\nThis dataset is associated with the following publication:\nMorshead, M., K. Jensen, G. Ankley, S. Vliet, C. LaLone, D. Villeneuve, A. Vidales Aller, and K. Watanabe. Putative adverse outcome pathway development based on physiological responses of female fathead minnows to model estrogen versus androgen receptor agonists.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 261: 106607, (2023).",
             "distribution": [
                 {
-                    "title": "Supplementary materials.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530091/Supplementary%20materials.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary materials.docx"
                 },
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/65be6cd9e4b063812d68d5bd",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/65be6cd9e4b063812d68d5bd"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/65be6cd9e4b063812d68d5bd",
+                    "title": "https://clowder.edap-cluster.com/datasets/65be6cd9e4b063812d68d5bd"
                 },
                 {
-                    "title": "CSS.4.6.2.1_ORD-053574_Morshead et al Data for Science Hub .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530091/CSS.4.6.2.1_ORD-053574_Morshead%20et%20al%20Data%20for%20Science%20Hub%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CSS.4.6.2.1_ORD-053574_Morshead et al Data for Science Hub .xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530091",
+            "keyword": [
+                "Mixture",
+                "adverse outcome pathway",
+                "fish",
+                "reproduction",
+                "endocrine disruption"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-07",
-            "references": [
-                "https://doi.org/10.1016/j.aquatox.2023.106607"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193633,19 +193627,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.aquatox.2023.106607"
+            ],
+            "rights": null,
+            "title": "Putative adverse outcome pathway development based on physiological responses of female fathead minnows to model estrogen versus androgen receptor agonists"
         },
         {
-            "title": "High-Throughput Transcriptomics Screen of ToxCast Chemicals in U-2 OS Cells",
-            "description": "Supplemental datafiles for journal article 'High-Throughput Transcriptomics Screen of ToxCast Chemicals in U-2 OS Cells'.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Joseph Bundy",
+                "hasEmail": "mailto:bundy.joseph@epa.gov"
+            },
+            "description": "Supplemental datafiles for journal article 'High-Throughput Transcriptomics Screen of ToxCast Chemicals in U-2 OS Cells'.",
+            "distribution": [
+                {
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65959df8e4b063812d5c7706",
+                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65959df8e4b063812d5c7706"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530097",
             "keyword": [
@@ -193655,18 +193658,11 @@
                 "bioinformatics",
                 "high throughput transcriptomics"
             ],
-            "contactPoint": {
-                "fn": "Joseph Bundy",
-                "hasEmail": "mailto:bundy.joseph@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65959df8e4b063812d5c7706",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65959df8e4b063812d5c7706"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-18",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -193675,56 +193671,54 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "High-Throughput Transcriptomics Screen of ToxCast Chemicals in U-2 OS Cells"
         },
         {
-            "title": "Dataset title: Postfire summer stream water temperature",
-            "description": "Data Description: Water temperature, precipitation, and watershed attributes for burned and unburned watershed sites in the Pacific Northwest. \n\nThis dataset is associated with the following publication:\nBeyene, M., and S. Leibowitz. Heterogeneity in post-fire thermal responses across Pacific Northwest streams: A multi-site study.   Journal of Hydrology X. Elsevier B.V., Amsterdam,  NETHERLANDS, 23(1): 100173, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529168",
-            "keyword": [
-                "water quality",
-                "wildfire",
-                "Pacific Northwest",
-                "summer stream temperature"
-            ],
             "contactPoint": {
                 "fn": "Scott Leibowitz",
                 "hasEmail": "mailto:leibowitz.scott@epa.gov"
             },
+            "description": "Data Description: Water temperature, precipitation, and watershed attributes for burned and unburned watershed sites in the Pacific Northwest. \n\nThis dataset is associated with the following publication:\nBeyene, M., and S. Leibowitz. Heterogeneity in post-fire thermal responses across Pacific Northwest streams: A multi-site study.   Journal of Hydrology X. Elsevier B.V., Amsterdam,  NETHERLANDS, 23(1): 100173, (2024).",
             "distribution": [
                 {
-                    "title": "Burned_watershed_Attributes.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529168/Burned_watershed_Attributes.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Burned_watershed_Attributes.xlsx"
                 },
                 {
-                    "title": "Burned_Sites_WT_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529168/Burned_Sites_WT_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Burned_Sites_WT_data.xlsx"
                 },
                 {
-                    "title": "Burned_Sites_PPT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529168/Burned_Sites_PPT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Burned_Sites_PPT.xlsx"
                 },
                 {
-                    "title": "Burned_Sites_AirT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529168/Burned_Sites_AirT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Burned_Sites_AirT.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529168",
+            "keyword": [
+                "water quality",
+                "wildfire",
+                "Pacific Northwest",
+                "summer stream temperature"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-30",
-            "references": [
-                "https://doi.org/10.1016/j.hydroa.2024.100173"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193734,63 +193728,62 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.hydroa.2024.100173"
+            ],
+            "rights": null,
+            "title": "Dataset title: Postfire summer stream water temperature"
         },
         {
-            "title": "Hepatic Transcriptome Comparative In Silico Analysis Reveals Similar Pathways and Targets Altered by Legacy and Alternative Per- and Polyfluoroalkyl Substances in Mice",
-            "description": "Dataset for Robarts et al., 'Hepatic Transcriptome Comparative In Silico Analysis Reveals Similar Pathways and Targets Altered by Legacy and Alternative Per- and Polyfluoroalkyl Substances in Mice' published in Toxics, DOI https://doi.org/10.3390/toxics11120963, PMCID 10748317. \n\nThis dataset is associated with the following publication:\nRobarts, D., J. Dai, C. Lau, U. Apte, and J. Corton. Hepatic Transcriptome Comparative In Silico Analysis Reveals Similar Pathways and Targets Altered by Legacy and Alternative Per- and Polyfluoroalkyl Substances in Mice.   Toxics. MDPI, Basel,  SWITZERLAND, 11(12): 963, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530278",
-            "keyword": [
-                "toxicogenomics",
-                "PPAR\u03b1",
-                "STAT5b",
-                "SREBP",
-                "GenX"
-            ],
             "contactPoint": {
                 "fn": "Jon Corton",
                 "hasEmail": "mailto:corton.chris@epa.gov"
             },
+            "description": "Dataset for Robarts et al., 'Hepatic Transcriptome Comparative In Silico Analysis Reveals Similar Pathways and Targets Altered by Legacy and Alternative Per- and Polyfluoroalkyl Substances in Mice' published in Toxics, DOI https://doi.org/10.3390/toxics11120963, PMCID 10748317. \n\nThis dataset is associated with the following publication:\nRobarts, D., J. Dai, C. Lau, U. Apte, and J. Corton. Hepatic Transcriptome Comparative In Silico Analysis Reveals Similar Pathways and Targets Altered by Legacy and Alternative Per- and Polyfluoroalkyl Substances in Mice.   Toxics. MDPI, Basel,  SWITZERLAND, 11(12): 963, (2023).",
             "distribution": [
                 {
-                    "title": "Table S1. Compound Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530278/Table%20S1.%20Compound%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S1. Compound Information.xlsx"
                 },
                 {
-                    "title": "Table S2. IPA Canonical Pathways.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530278/Table%20S2.%20IPA%20Canonical%20Pathways.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S2. IPA Canonical Pathways.xlsx"
                 },
                 {
-                    "title": "Table S3. BSCE.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530278/Table%20S3.%20BSCE.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S3. BSCE.xlsx"
                 },
                 {
-                    "title": "Table S4. IPA Upstream Regulators.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530278/Table%20S4.%20IPA%20Upstream%20Regulators.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S4. IPA Upstream Regulators.xlsx"
                 },
                 {
-                    "title": "Table S5. Biomarkers.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530278/Table%20S5.%20Biomarkers.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S5. Biomarkers.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530278",
+            "keyword": [
+                "toxicogenomics",
+                "PPAR\u03b1",
+                "STAT5b",
+                "SREBP",
+                "GenX"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-04-14",
-            "references": [
-                "https://doi.org/10.3390/toxics11120963",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10748317"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193800,41 +193793,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxics11120963",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10748317"
+            ],
+            "rights": null,
+            "title": "Hepatic Transcriptome Comparative In Silico Analysis Reveals Similar Pathways and Targets Altered by Legacy and Alternative Per- and Polyfluoroalkyl Substances in Mice"
         },
         {
-            "title": "Applying Microelectrodes to Investigate Aged Ductile Iron and Copper Coupon Reactivity during Free Chlorine Application Data Set",
-            "description": "Data set associated with manuscript Applying Microelectrodes to Investigate Aged Ductile Iron and Copper Coupon Reactivity during Free Chlorine Application. \n\nThis dataset is associated with the following publication:\nLiggett, J., B. Gonzalez, D. Lytle, J. Pressman, D.  Dionysiou, W.H. Lee, S. Harmon, and D. Wahman. Applying Microelectrodes to Investigate Aged Ductile Iron and Copper Coupon Reactivity during Free Chlorine Application.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 253: 121324, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529610",
-            "keyword": [
-                "Ductile Iron",
-                "microelectrode",
-                "Copper",
-                "corrosion"
-            ],
             "contactPoint": {
                 "fn": "David Wahman",
                 "hasEmail": "mailto:wahman.david@epa.gov"
             },
+            "description": "Data set associated with manuscript Applying Microelectrodes to Investigate Aged Ductile Iron and Copper Coupon Reactivity during Free Chlorine Application. \n\nThis dataset is associated with the following publication:\nLiggett, J., B. Gonzalez, D. Lytle, J. Pressman, D.  Dionysiou, W.H. Lee, S. Harmon, and D. Wahman. Applying Microelectrodes to Investigate Aged Ductile Iron and Copper Coupon Reactivity during Free Chlorine Application.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 253: 121324, (2024).",
             "distribution": [
                 {
-                    "title": "Applying_Microelectrodes_to_Investigate_Aged_Ductile_Iron_and_Copper_Coupon_Reactivity_v1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529610/Applying_Microelectrodes_to_Investigate_Aged_Ductile_Iron_and_Copper_Coupon_Reactivity_v1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Applying_Microelectrodes_to_Investigate_Aged_Ductile_Iron_and_Copper_Coupon_Reactivity_v1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529610",
+            "keyword": [
+                "Ductile Iron",
+                "microelectrode",
+                "Copper",
+                "corrosion"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-26",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2024.121324"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193844,42 +193838,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2024.121324"
+            ],
+            "rights": null,
+            "title": "Applying Microelectrodes to Investigate Aged Ductile Iron and Copper Coupon Reactivity during Free Chlorine Application Data Set"
         },
         {
-            "title": "Edge-of-field agricultural conservation practice studies in the Corn Belt region",
-            "description": "Summary dataset showing reviewed literature related to edge-of-field agricultural conservation practices in the Corn Belt region. \n\nThis dataset is associated with the following publication:\nMitchell, M., T. Newcomer Johnson, J. Christensen, W. Crumpton, B. Dyson, T. Canfield, M. Helmers, and K. Forshay. A review of ecosystem services from edge-of-field practices in tile-drained agricultural systems in the United States Corn Belt Region.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 348: 119220, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529113",
-            "keyword": [
-                "Land management",
-                "climate change",
-                "biodiversity",
-                "Agriculture",
-                "Nitrogen and Co-pollutants"
-            ],
             "contactPoint": {
                 "fn": "Kenneth Forshay",
                 "hasEmail": "mailto:forshay.ken@epa.gov"
             },
+            "description": "Summary dataset showing reviewed literature related to edge-of-field agricultural conservation practices in the Corn Belt region. \n\nThis dataset is associated with the following publication:\nMitchell, M., T. Newcomer Johnson, J. Christensen, W. Crumpton, B. Dyson, T. Canfield, M. Helmers, and K. Forshay. A review of ecosystem services from edge-of-field practices in tile-drained agricultural systems in the United States Corn Belt Region.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 348: 119220, (2023).",
             "distribution": [
                 {
-                    "title": "ScienceHub Data_Supplemental Table 2_Reviewed Literature.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529113/ScienceHub%20Data_Supplemental%20Table%202_Reviewed%20Literature.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHub Data_Supplemental Table 2_Reviewed Literature.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529113",
+            "keyword": [
+                "Land management",
+                "climate change",
+                "biodiversity",
+                "Agriculture",
+                "Nitrogen and Co-pollutants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-02",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2023.119220"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193889,40 +193883,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2023.119220"
+            ],
+            "rights": null,
+            "title": "Edge-of-field agricultural conservation practice studies in the Corn Belt region"
         },
         {
-            "title": "Glucose Suppressed Cyanobacterial Abundance ",
-            "description": "Data shows that prophylactic addition of glucose to Harsha Lake water samples could inhibit cyanobacteria growth based on metagenomic sequencing data used to examine differences in the composition of bacterial communities between Treated and Control containers. The sequencing data shows that the addition of glucose to a container receiving weekly additions of Lake water suppressed the cyanobacterial populations during the entire summer bloom season. \n\nThis dataset is associated with the following publication:\nLinz, D., I. Struewing, N. Sienkiewicz, A.D. Steinman, C.G. Partridge, K. McIntosh, J. Lu, and S. Vesper. Periodic Addition of Glucose Suppressed Cyanobacterial Abundance in Additive Lake Water Samples during the Entire Bloom Season.   Journal of Water Resource and Protection. Scientific Research Publishing, Inc., Irvine, CA, USA, 16: 140-15, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529157",
-            "keyword": [
-                "glucose",
-                "sequencing",
-                "16S amplicon",
-                "cyanobacteria"
-            ],
             "contactPoint": {
                 "fn": "Stephen Vesper",
                 "hasEmail": "mailto:vesper.stephen@epa.gov"
             },
+            "description": "Data shows that prophylactic addition of glucose to Harsha Lake water samples could inhibit cyanobacteria growth based on metagenomic sequencing data used to examine differences in the composition of bacterial communities between Treated and Control containers. The sequencing data shows that the addition of glucose to a container receiving weekly additions of Lake water suppressed the cyanobacterial populations during the entire summer bloom season. \n\nThis dataset is associated with the following publication:\nLinz, D., I. Struewing, N. Sienkiewicz, A.D. Steinman, C.G. Partridge, K. McIntosh, J. Lu, and S. Vesper. Periodic Addition of Glucose Suppressed Cyanobacterial Abundance in Additive Lake Water Samples during the Entire Bloom Season.   Journal of Water Resource and Protection. Scientific Research Publishing, Inc., Irvine, CA, USA, 16: 140-15, (2024).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA972685",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA972685"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA972685",
+                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA972685"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529157",
+            "keyword": [
+                "glucose",
+                "sequencing",
+                "16S amplicon",
+                "cyanobacteria"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-16",
-            "references": [
-                "https://doi.org/10.4236/jwarp.2024.162009"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193932,20 +193926,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.4236/jwarp.2024.162009"
+            ],
+            "rights": null,
+            "title": "Glucose Suppressed Cyanobacterial Abundance "
         },
         {
-            "title": "Sister Study - Neighborhood greenery, depressive symptoms, and redlining",
-            "description": "This dataset contains health outcome (depressive symptoms defined by CES-D 10), neighborhood greenery (percent tree cover within 500m and 2000m from residences), historical HOLC grades, and sociodemographic factors (age, race/ethnicity, marital status, education, employment status, income, use of depression medication) for 3555 Sister Study participants. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Please submit data request through https://sisterstudy.niehs.nih.gov/English/coll-data.htm. Format: The Sister Study data are released in SAS format. \n\nThis dataset is associated with the following publication:\nTsai, W., M. Nash, D. Rosenbaum, S. Prince, A. D'Aloisio, M. Mehaffey, D. Sandler, T. Buckley, and A. Neale. Association of Redlining and Natural Environment with Depressive Symptoms in Women in the Sister Study.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 131(10): 107009, (2022).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Wei-Lun Tsai",
+                "hasEmail": "mailto:tsai.wei-lun@epa.gov"
+            },
+            "description": "This dataset contains health outcome (depressive symptoms defined by CES-D 10), neighborhood greenery (percent tree cover within 500m and 2000m from residences), historical HOLC grades, and sociodemographic factors (age, race/ethnicity, marital status, education, employment status, income, use of depression medication) for 3555 Sister Study participants. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Please submit data request through https://sisterstudy.niehs.nih.gov/English/coll-data.htm. Format: The Sister Study data are released in SAS format. \n\nThis dataset is associated with the following publication:\nTsai, W., M. Nash, D. Rosenbaum, S. Prince, A. D'Aloisio, M. Mehaffey, D. Sandler, T. Buckley, and A. Neale. Association of Redlining and Natural Environment with Depressive Symptoms in Women in the Sister Study.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 131(10): 107009, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1527959",
             "keyword": [
                 "Depressive symptoms",
@@ -193953,15 +193951,10 @@
                 "redlining",
                 "Environmental Justice"
             ],
-            "contactPoint": {
-                "fn": "Wei-Lun Tsai",
-                "hasEmail": "mailto:tsai.wei-lun@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-08-17",
-            "references": [
-                "https://doi.org/10.1289/ehp12212",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10584058"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -193971,42 +193964,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp12212",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10584058"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Sister Study - Neighborhood greenery, depressive symptoms, and redlining"
         },
         {
-            "title": "Dataset for Extracellular Vesicles altered by Per- and Polyfluoroalkyl Substance Mixtures: In Vitro Dose-Dependent Release, Chemical Content, and MicroRNA Signatures involved in Liver Health.",
-            "description": "These data represent underlying data generated for the study titled 'Extracellular Vesicles altered by Per- and Polyfluoroalkyl Substance Mixtures: In Vitro Dose-Dependent Release, Chemical Content, and MicroRNA Signatures involved in Liver Health'. Data include extracellular vesicle particle count and size distribution from nanoparticle tracking analysis; microRNA expression data from mRNA sequencing in extracellular vesicles; PFAS signature data from mass spectrometry analysis of isolated HepG2 cell lysates and their secreted extracellular vesicles; in vitro cell viability data. \n\nThis dataset is associated with the following publication:\nCarberry, C., J. Bangma, L. Koval, D. Keshava, h. Hartwell, M. Sokolsky, R. Fry, and J. Rager. Extracellular vesicles altered by a per- and polyfluoroalkyl substance mixture: in vitro dose-dependent release, chemical content, and microRNA signatures involved in liver health.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  197(2): 155-169, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529913",
-            "keyword": [
-                "Mixtures",
-                "PFAS",
-                "liver toxicity",
-                "extracellular vesicles"
-            ],
             "contactPoint": {
                 "fn": "Jacqueline Bangma",
                 "hasEmail": "mailto:bangma.jacqueline@epa.gov"
             },
+            "description": "These data represent underlying data generated for the study titled 'Extracellular Vesicles altered by Per- and Polyfluoroalkyl Substance Mixtures: In Vitro Dose-Dependent Release, Chemical Content, and MicroRNA Signatures involved in Liver Health'. Data include extracellular vesicle particle count and size distribution from nanoparticle tracking analysis; microRNA expression data from mRNA sequencing in extracellular vesicles; PFAS signature data from mass spectrometry analysis of isolated HepG2 cell lysates and their secreted extracellular vesicles; in vitro cell viability data. \n\nThis dataset is associated with the following publication:\nCarberry, C., J. Bangma, L. Koval, D. Keshava, h. Hartwell, M. Sokolsky, R. Fry, and J. Rager. Extracellular vesicles altered by a per- and polyfluoroalkyl substance mixture: in vitro dose-dependent release, chemical content, and microRNA signatures involved in liver health.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  197(2): 155-169, (2024).",
             "distribution": [
                 {
-                    "title": "PFASEVs_Tables.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529913/PFASEVs_Tables.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PFASEVs_Tables.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529913",
+            "keyword": [
+                "Mixtures",
+                "PFAS",
+                "liver toxicity",
+                "extracellular vesicles"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-02-16",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfad108",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10823775"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194016,42 +194009,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfad108",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10823775"
+            ],
+            "rights": null,
+            "title": "Dataset for Extracellular Vesicles altered by Per- and Polyfluoroalkyl Substance Mixtures: In Vitro Dose-Dependent Release, Chemical Content, and MicroRNA Signatures involved in Liver Health."
         },
         {
-            "title": "Post ingestion bioaccessibility of pesticides sorbed to soils and house dusts",
-            "description": "post ingestion bioaccessibility data for pesticides. \n\nThis dataset is associated with the following publication:\nParker, B., E. Valentini, S. Graham, and J. Starr. In vitro modeling of the post-ingestion bioaccessibility of per- and polyfluoroalkyl substances sorbed to soil and house dust.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  197(1): 95-103, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527792",
-            "keyword": [
-                "House dust",
-                "bioaccesibility",
-                "soil",
-                "ingestion",
-                "PFAS"
-            ],
             "contactPoint": {
                 "fn": "James Starr",
                 "hasEmail": "mailto:starr.james@epa.gov"
             },
+            "description": "post ingestion bioaccessibility data for pesticides. \n\nThis dataset is associated with the following publication:\nParker, B., E. Valentini, S. Graham, and J. Starr. In vitro modeling of the post-ingestion bioaccessibility of per- and polyfluoroalkyl substances sorbed to soil and house dust.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  197(1): 95-103, (2024).",
             "distribution": [
                 {
-                    "title": "PFAS Bioaccessibility Data Set For clearance 071122.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527792/PFAS%20Bioaccessibility%20Data%20Set%20For%20clearance%20071122.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PFAS Bioaccessibility Data Set For clearance 071122.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527792",
+            "keyword": [
+                "House dust",
+                "bioaccesibility",
+                "soil",
+                "ingestion",
+                "PFAS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-29",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfad098"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194061,20 +194055,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfad098"
+            ],
+            "rights": null,
+            "title": "Post ingestion bioaccessibility of pesticides sorbed to soils and house dusts"
         },
         {
-            "title": "Metadata for Baker et al. 2023 (\"Projecting I.S. forest management...https://doi.org/10.1016/j.forpol.2022.102898)",
-            "description": "This is the data for Baker et al., contact Jeremy Martinich for additional information (martinich.jeremy@epa.gov). This dataset is not publicly accessible because: The data is owned by OAR, not ORD, and they host it. It can be accessed through the following means: Email Jeremy Martinich in EPA\"s Office of Atmospheric Programs (martinich.jeremy@epa.gov). Format: N/A. \n\nThis dataset is associated with the following publication:\nBaker, J., G. van Houtven, J. Phelan, G. Latta, C. Clark, K. Austin, O. Sodiya, S. Bushey Ohrel, J. Buckley, L. Gentile, and J. Martinich. Projecting U.S. forest management, market, and carbon sequestration responses to a high-impact climate scenario manuscript.   Forest Policy and Economics. Elsevier BV, AMSTERDAM,  NETHERLANDS, 147(February 2023): 1-17, (2022).",
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
+                "fn": "Christopher Clark",
+                "hasEmail": "mailto:clark.christopher@epa.gov"
+            },
+            "description": "This is the data for Baker et al., contact Jeremy Martinich for additional information (martinich.jeremy@epa.gov). This dataset is not publicly accessible because: The data is owned by OAR, not ORD, and they host it. It can be accessed through the following means: Email Jeremy Martinich in EPA\"s Office of Atmospheric Programs (martinich.jeremy@epa.gov). Format: N/A. \n\nThis dataset is associated with the following publication:\nBaker, J., G. van Houtven, J. Phelan, G. Latta, C. Clark, K. Austin, O. Sodiya, S. Bushey Ohrel, J. Buckley, L. Gentile, and J. Martinich. Projecting U.S. forest management, market, and carbon sequestration responses to a high-impact climate scenario manuscript.   Forest Policy and Economics. Elsevier BV, AMSTERDAM,  NETHERLANDS, 147(February 2023): 1-17, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530322",
             "keyword": [
                 "Forest Biomass",
@@ -194082,15 +194080,10 @@
                 "FASOM",
                 "climate change"
             ],
-            "contactPoint": {
-                "fn": "Christopher Clark",
-                "hasEmail": "mailto:clark.christopher@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-02-01",
-            "references": [
-                "https://doi.org/10.1016/j.forpol.2022.102898",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10013705"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194100,95 +194093,96 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.forpol.2022.102898",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10013705"
+            ],
+            "rights": null,
+            "title": "Metadata for Baker et al. 2023 (\"Projecting I.S. forest management...https://doi.org/10.1016/j.forpol.2022.102898)"
         },
         {
-            "title": "Liquid Application Dosing Alters Air-Liquid-Interface Bronchial Epithelial Culture Physiology and Toxicity Testing Relevant Endpoints",
-            "description": "Data accompanying the manuscript titled, \"Liquid Application Dosing Alters Air-Liquid-Interface Bronchial Epithelial Culture Physiology and Toxicity Testing Relevant Endpoints\"\n\nAuthors: Nicholas M. Mallek, Elizabeth M. Martin, Lisa A. Dailey, and Shaun D. McCullough. \n\nThis dataset is associated with the following publication:\nMallek, N., E. Martin, L. Dailey, and S. McCullough. Liquid Application Dosing Alters the Physiology of Air-Liquid Interface (ALI) Primary Human Bronchial Epithelial Cell/Lung Fibroblast Co-Cultures and In Vitro Testing Relevant Endpoints.   Frontiers in Toxicology. Frontiers, Lausanne,  SWITZERLAND, 5: 1264331, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526421",
-            "keyword": [
-                "primary",
-                "NAMs",
-                "inhalation",
-                "in vitro",
-                "chlorothalonil",
-                "bronchial",
-                "ALI",
-                "air-liquid inter"
-            ],
             "contactPoint": {
                 "fn": "Shaun McCullough",
                 "hasEmail": "mailto:mccullough.shaun@epa.gov"
             },
+            "description": "Data accompanying the manuscript titled, \"Liquid Application Dosing Alters Air-Liquid-Interface Bronchial Epithelial Culture Physiology and Toxicity Testing Relevant Endpoints\"\n\nAuthors: Nicholas M. Mallek, Elizabeth M. Martin, Lisa A. Dailey, and Shaun D. McCullough. \n\nThis dataset is associated with the following publication:\nMallek, N., E. Martin, L. Dailey, and S. McCullough. Liquid Application Dosing Alters the Physiology of Air-Liquid Interface (ALI) Primary Human Bronchial Epithelial Cell/Lung Fibroblast Co-Cultures and In Vitro Testing Relevant Endpoints.   Frontiers in Toxicology. Frontiers, Lausanne,  SWITZERLAND, 5: 1264331, (2023).",
             "distribution": [
                 {
-                    "title": "Mallek et al_Liquid Application_Data_Growth Factor ELISA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application_Data_Growth%20Factor%20ELISA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application_Data_Growth Factor ELISA.xlsx"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application_Data_Analysis of Re-Sub Rep3-5 Export_RAW DATA.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application_Data_Analysis%20of%20Re-Sub%20Rep3-5%20Export_RAW%20DATA.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mallek et al_Liquid Application_Data_Analysis of Re-Sub Rep3-5 Export_RAW DATA.xls"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application_Data_Analysis of Re-Sub CBF_Processed Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application_Data_Analysis%20of%20Re-Sub%20CBF_Processed%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application_Data_Analysis of Re-Sub CBF_Processed Data.xlsx"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application Data_PHBEC 24h Gene Lists_Raw_Thresholded.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application%20Data_PHBEC%2024h%20Gene%20Lists_Raw_Thresholded.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application Data_PHBEC 24h Gene Lists_Raw_Thresholded.xlsx"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application Data_PHBEC 6h Gene Lists_Raw_Thresholded.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application%20Data_PHBEC%206h%20Gene%20Lists_Raw_Thresholded.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application Data_PHBEC 6h Gene Lists_Raw_Thresholded.xlsx"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application Data_TEER and FITC.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application%20Data_TEER%20and%20FITC.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application Data_TEER and FITC.xlsx"
                 },
                 {
-                    "title": "Liquid Application Manuscript Prism File.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Liquid%20Application%20Manuscript%20Prism%20File.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Liquid Application Manuscript Prism File.zip"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application_Western Blots.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application_Western%20Blots.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Mallek et al_Liquid Application_Western Blots.pdf"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application_p38 Densitometry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application_p38%20Densitometry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application_p38 Densitometry.xlsx"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application_HIF1a Densitometry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application_HIF1a%20Densitometry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application_HIF1a Densitometry.xlsx"
                 },
                 {
-                    "title": "Mallek et al_Liquid Application_ERK Densitometry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526421/Mallek%20et%20al_Liquid%20Application_ERK%20Densitometry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mallek et al_Liquid Application_ERK Densitometry.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526421",
+            "keyword": [
+                "primary",
+                "NAMs",
+                "inhalation",
+                "in vitro",
+                "chlorothalonil",
+                "bronchial",
+                "ALI",
+                "air-liquid inter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-05-09",
-            "references": [
-                "https://doi.org/10.3389/ftox.2023.1264331"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194198,20 +194192,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/ftox.2023.1264331"
+            ],
+            "rights": null,
+            "title": "Liquid Application Dosing Alters Air-Liquid-Interface Bronchial Epithelial Culture Physiology and Toxicity Testing Relevant Endpoints"
         },
         {
-            "title": "Responses to Wildfire and Prescribed Fire Smoke: A Survey of a Medically Vulnerable Adult Population in the Wildland-Urban Interface, Mariposa County, California",
-            "description": "Using a cross-sectional design, we surveyed participants in the program, Support and Aid for Everyone (SAFE) operated by Mariposa County Health and Human Services Agency (MC), which assists persons who self-identify as having special needs in an emergency, e.g., use wheelchairs or electrical medical equipment.  \nA questionnaire was distributed to SAFE participants on behalf of California Department of Public Health (CDPH) by MC staff allowed for anonymous participation. Following a modified Dillman method, the survey was mailed, with a phone interview option. Reminders were made by postcard and follow-up calls by MC staff. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Data analysis files are available from the corresponding author upon reasonable request to Sumi Hoshiko sumi.hoshiko@cdph.ca.gov. Format: Raw data from this study will not be made publicly available to protect confidentiality. Data analysis files are available from the corresponding author upon reasonable request to Sumi Hoshiko sumi.hoshiko@cdph.ca.gov. \n\nThis dataset is associated with the following publication:\nRappold, A., S. Hoshiko, J. Buckman, C.G. Jones, K. Yeomans, A. Mello, R. Thilakaratne, E. Sergienko, MD, K. Allen, and L. Bello. Responses to wildfire and prescribed fire smoke: A survey of a medically vulnerable adult population in the wildland-urban interface, Mariposa County, California.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 20(2): 1, (2023).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Ana Rappold",
+                "hasEmail": "mailto:rappold.ana@epa.gov"
+            },
+            "description": "Using a cross-sectional design, we surveyed participants in the program, Support and Aid for Everyone (SAFE) operated by Mariposa County Health and Human Services Agency (MC), which assists persons who self-identify as having special needs in an emergency, e.g., use wheelchairs or electrical medical equipment.  \nA questionnaire was distributed to SAFE participants on behalf of California Department of Public Health (CDPH) by MC staff allowed for anonymous participation. Following a modified Dillman method, the survey was mailed, with a phone interview option. Reminders were made by postcard and follow-up calls by MC staff. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Data analysis files are available from the corresponding author upon reasonable request to Sumi Hoshiko sumi.hoshiko@cdph.ca.gov. Format: Raw data from this study will not be made publicly available to protect confidentiality. Data analysis files are available from the corresponding author upon reasonable request to Sumi Hoshiko sumi.hoshiko@cdph.ca.gov. \n\nThis dataset is associated with the following publication:\nRappold, A., S. Hoshiko, J. Buckman, C.G. Jones, K. Yeomans, A. Mello, R. Thilakaratne, E. Sergienko, MD, K. Allen, and L. Bello. Responses to wildfire and prescribed fire smoke: A survey of a medically vulnerable adult population in the wildland-urban interface, Mariposa County, California.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 20(2): 1, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530329",
             "keyword": [
                 "wildfire",
@@ -194224,15 +194222,10 @@
                 "managed fire",
                 "wildland-urban-interface"
             ],
-            "contactPoint": {
-                "fn": "Ana Rappold",
-                "hasEmail": "mailto:rappold.ana@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-12-23",
-            "references": [
-                "https://doi.org/10.3390/ijerph20021210",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9858942"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194242,42 +194235,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ijerph20021210",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9858942"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Responses to Wildfire and Prescribed Fire Smoke: A Survey of a Medically Vulnerable Adult Population in the Wildland-Urban Interface, Mariposa County, California"
         },
         {
-            "title": "Dataset_Urban_Lakes",
-            "description": "The dataset including qPCR and sequences is used for cyanobacterial characterization and qPCR assay evaluation. \n\nThis dataset is associated with the following publication:\nJeon, Y., I. Struewing, K. McIntosh, M. Tidd, L. Webb, H. Ryu, H. Mash, and J. Lu. Spatial and Temporal Variability of Saxitoxin-Producing Cyanobacteria in U.S. Urban Lakes.   Toxins. MDPI, Basel,  SWITZERLAND, 16(2): 70, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529357",
-            "keyword": [
-                "saxitoxin",
-                "sxtA gene",
-                "cyanotoxin producer",
-                "qPCR"
-            ],
             "contactPoint": {
                 "fn": "Jingrang Lu",
                 "hasEmail": "mailto:lu.jingrang@epa.gov"
             },
+            "description": "The dataset including qPCR and sequences is used for cyanobacterial characterization and qPCR assay evaluation. \n\nThis dataset is associated with the following publication:\nJeon, Y., I. Struewing, K. McIntosh, M. Tidd, L. Webb, H. Ryu, H. Mash, and J. Lu. Spatial and Temporal Variability of Saxitoxin-Producing Cyanobacteria in U.S. Urban Lakes.   Toxins. MDPI, Basel,  SWITZERLAND, 16(2): 70, (2024).",
             "distribution": [
                 {
-                    "title": "Dataset_Urban_Lakes.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529357/Dataset_Urban_Lakes.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dataset_Urban_Lakes.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529357",
+            "keyword": [
+                "saxitoxin",
+                "sxtA gene",
+                "cyanotoxin producer",
+                "qPCR"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-13",
-            "references": [
-                "https://doi.org/10.3390/toxins16020070",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10892283"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194287,35 +194280,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxins16020070",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10892283"
+            ],
+            "rights": null,
+            "title": "Dataset_Urban_Lakes"
         },
         {
-            "title": "Metadata for Associations between long-term fine particulate matter exposure and hospital procedures in heart failure patients",
-            "description": "This dataset contains information on air pollution exposure, census block group socioeconomic status, hospital procedures, demographics, and disease diagnosis history for heart failure patients in North Carolina (seen at a UNCHCS hospital or clinic). This dataset is not publicly accessible because: This data is composed of electronic health records containing PII and thus cannot be included in ScienceHub or released to the public. It can be accessed through the following means: The data can be accessed with written request accompanied by an appropriate, approved IRB application. Format: The data contains details on the air pollution exposure, performed hospital procedures, census tract socioeconomic status, and diagnoses information (including dates of diagnoses) for heart failure patients seen at UNCHCS hospital or clinic. The data is in tabular (flatfile) format. \n\nThis dataset is associated with the following publication:\nCatalano, S., J. Moyer, A. Weaver, Q. Di, J. Schwartz, M. Caralano, and C. Ward-Caviness. Associations between long-term fine particulate matter exposure and hospital procedures in heart failure patients..   PLOS ONE. Public Library of Science, San Francisco, CA, USA, 18(5): e0283759, (2023).",
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
+                "fn": "Cavin Ward-Caviness",
+                "hasEmail": "mailto:ward-caviness.cavin@epa.gov"
+            },
+            "description": "This dataset contains information on air pollution exposure, census block group socioeconomic status, hospital procedures, demographics, and disease diagnosis history for heart failure patients in North Carolina (seen at a UNCHCS hospital or clinic). This dataset is not publicly accessible because: This data is composed of electronic health records containing PII and thus cannot be included in ScienceHub or released to the public. It can be accessed through the following means: The data can be accessed with written request accompanied by an appropriate, approved IRB application. Format: The data contains details on the air pollution exposure, performed hospital procedures, census tract socioeconomic status, and diagnoses information (including dates of diagnoses) for heart failure patients seen at UNCHCS hospital or clinic. The data is in tabular (flatfile) format. \n\nThis dataset is associated with the following publication:\nCatalano, S., J. Moyer, A. Weaver, Q. Di, J. Schwartz, M. Caralano, and C. Ward-Caviness. Associations between long-term fine particulate matter exposure and hospital procedures in heart failure patients..   PLOS ONE. Public Library of Science, San Francisco, CA, USA, 18(5): e0283759, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530328",
             "keyword": [
                 "air pollution",
                 "hospital procedures",
                 "electronic health records"
             ],
-            "contactPoint": {
-                "fn": "Cavin Ward-Caviness",
-                "hasEmail": "mailto:ward-caviness.cavin@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-05-03",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0283759",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10155991"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194325,20 +194318,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0283759",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10155991"
+            ],
+            "rights": null,
+            "title": "Metadata for Associations between long-term fine particulate matter exposure and hospital procedures in heart failure patients"
         },
         {
-            "title": "NOAA Data",
-            "description": "Data owner is Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. This dataset is not publicly accessible because: Data is property of NOAA. It can be accessed through the following means: Data owner is Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. Format: Data is raster format and table format. \n\nThis dataset is associated with the following publication:\nMishra, S., R. Stumpf, B. Schaeffer, and P.J. Werdell. Recent changes in cyanobacteria algal bloom magnitude in large lakes across the contiguous United States.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 897: 165253, (2023).",
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
+            "description": "Data owner is Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. This dataset is not publicly accessible because: Data is property of NOAA. It can be accessed through the following means: Data owner is Sachidananda Mishra (sachi.mishra@noaa.gov) and Richard Stumpf at NOAA. Format: Data is raster format and table format. \n\nThis dataset is associated with the following publication:\nMishra, S., R. Stumpf, B. Schaeffer, and P.J. Werdell. Recent changes in cyanobacteria algal bloom magnitude in large lakes across the contiguous United States.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 897: 165253, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530327",
             "keyword": [
                 "satellite",
@@ -194346,15 +194344,10 @@
                 "water quality",
                 "cyanobacteria"
             ],
-            "contactPoint": {
-                "fn": "Blake Schaeffer",
-                "hasEmail": "mailto:schaeffer.blake@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-18",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.165253",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10835736"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194364,40 +194357,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.165253",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10835736"
+            ],
+            "rights": null,
+            "title": "NOAA Data"
         },
         {
-            "title": "CyAN Predictor Ranks - Upper Midwest USA",
-            "description": "This dataset ranks 88 predictors run in a random forest analysis for 369 freshwater lakes in the Upper Midwest USA. \n\nThis dataset is associated with the following publication:\nIiames, J., W. Salls, M. Mehaffey, M. Nash, J. Christensen, and B. Schaeffer. Modeling Anthropogenic and Environmental Influences on Freshwater Harmful Algal Bloom Development Detected by MERIS Over the Central United States.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 57(10): e2020WR028946, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1521321",
-            "keyword": [
-                "cyanobacteria index",
-                "random forest"
-            ],
             "contactPoint": {
                 "fn": "John Iiames",
                 "hasEmail": "mailto:iiames.john@epa.gov"
             },
+            "description": "This dataset ranks 88 predictors run in a random forest analysis for 369 freshwater lakes in the Upper Midwest USA. \n\nThis dataset is associated with the following publication:\nIiames, J., W. Salls, M. Mehaffey, M. Nash, J. Christensen, and B. Schaeffer. Modeling Anthropogenic and Environmental Influences on Freshwater Harmful Algal Bloom Development Detected by MERIS Over the Central United States.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 57(10): e2020WR028946, (2021).",
             "distribution": [
                 {
-                    "title": "var_ranks_SUMMARY_2021-04-05.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521321/var_ranks_SUMMARY_2021-04-05.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "var_ranks_SUMMARY_2021-04-05.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521321",
+            "keyword": [
+                "cyanobacteria index",
+                "random forest"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-04-06",
-            "references": [
-                "https://doi.org/10.1029/2020wr028946",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9285409"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194407,42 +194400,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2020wr028946",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9285409"
+            ],
+            "rights": null,
+            "title": "CyAN Predictor Ranks - Upper Midwest USA"
         },
         {
-            "title": "Data support results reported in \"Modeling future land cover change scenarios in Minneapolis, MN, to support drinking water source protection decisions\"",
-            "description": "Data supporting results presented in \"Modeling future land cover change scenarios in Minneapolis, MN, to support drinking water source protection decisions.\". \n\nThis dataset is associated with the following publication:\nWoznicki, S., G. Kraynick, J. Wickham, M. Nash, and T. Sohl. Modeling future land cover and water quality change in Minneapolis, MN, USA to support drinking water source protection decisions.   Global Environmental Change. Elsevier B.V., Amsterdam,  NETHERLANDS, 59(4): 726-742, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1521325",
-            "keyword": [
-                "drinking water",
-                "land cover change",
-                "SWAT",
-                "FORE-SCE",
-                "source water protection"
-            ],
             "contactPoint": {
                 "fn": "James Wickham",
                 "hasEmail": "mailto:wickham.james@epa.gov"
             },
+            "description": "Data supporting results presented in \"Modeling future land cover change scenarios in Minneapolis, MN, to support drinking water source protection decisions.\". \n\nThis dataset is associated with the following publication:\nWoznicki, S., G. Kraynick, J. Wickham, M. Nash, and T. Sohl. Modeling future land cover and water quality change in Minneapolis, MN, USA to support drinking water source protection decisions.   Global Environmental Change. Elsevier B.V., Amsterdam,  NETHERLANDS, 59(4): 726-742, (2023).",
             "distribution": [
                 {
-                    "title": "SciHub_A-fbgt.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1521325/SciHub_A-fbgt.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "SciHub_A-fbgt.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1521325",
+            "keyword": [
+                "drinking water",
+                "land cover change",
+                "SWAT",
+                "FORE-SCE",
+                "source water protection"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-12-15",
-            "references": [
-                "https://doi.org/10.1111/1752-1688.13109"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194452,20 +194446,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/1752-1688.13109"
+            ],
+            "rights": null,
+            "title": "Data support results reported in \"Modeling future land cover change scenarios in Minneapolis, MN, to support drinking water source protection decisions\""
         },
         {
-            "title": "Mangrove Database of CONUS 1980-2020",
-            "description": "Readme.txt\nDirectory name: Final Mosaic. These datasets were prepare using Landsat Satellite Data.  \nFile path:L:\\Public\\Mangrove\\CONUS\\change analysis\\Mosaic\\Final Mosaic\nThis directory has the following files\n1980_mosaicf.img\n1985_mosaicf.img\n1990_mosaicf.img\n1995_mosaicf.img\n2005_mosaicf.img\n2015_mosaicf.img\n2020_mosaicf.img\nThe datas are in ERDAS Imagine format with the following details.\nData Type: unsigned 4bit\nType: Thematic\nSpatial Resolution=30m\nProjection=Geographic (lat/long)\nSpheroid: WGS84\nDatum: WGS84\nEPSG CODE:4326. This dataset is not publicly accessible because: the format is not supported by ScienceHub. It can be accessed through the following means: L:\\Public\\Mangrove\\CONUS\\change analysis\\Mosaic\\Final Mosaic. Format: The data are in ERDAS imagine format with an extension of .img. \n\nThis dataset is associated with the following publication:\nGiri, C., J. Long, and P. Poudel. Mangrove Forest Cover Change in the Conterminous United States from 1980\u20132020.   Remote Sensing. MDPI, Basel,  SWITZERLAND, 15(20): 5018, (2023).",
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
+                "fn": "Chandra Giri",
+                "hasEmail": "mailto:giri.chandra@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529541/documents/readme.txt",
+            "describedByType": "text/plain",
+            "description": "Readme.txt\nDirectory name: Final Mosaic. These datasets were prepare using Landsat Satellite Data.  \nFile path:L:\\Public\\Mangrove\\CONUS\\change analysis\\Mosaic\\Final Mosaic\nThis directory has the following files\n1980_mosaicf.img\n1985_mosaicf.img\n1990_mosaicf.img\n1995_mosaicf.img\n2005_mosaicf.img\n2015_mosaicf.img\n2020_mosaicf.img\nThe datas are in ERDAS Imagine format with the following details.\nData Type: unsigned 4bit\nType: Thematic\nSpatial Resolution=30m\nProjection=Geographic (lat/long)\nSpheroid: WGS84\nDatum: WGS84\nEPSG CODE:4326. This dataset is not publicly accessible because: the format is not supported by ScienceHub. It can be accessed through the following means: L:\\Public\\Mangrove\\CONUS\\change analysis\\Mosaic\\Final Mosaic. Format: The data are in ERDAS imagine format with an extension of .img. \n\nThis dataset is associated with the following publication:\nGiri, C., J. Long, and P. Poudel. Mangrove Forest Cover Change in the Conterminous United States from 1980\u20132020.   Remote Sensing. MDPI, Basel,  SWITZERLAND, 15(20): 5018, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529541",
             "keyword": [
                 "climate change",
@@ -194475,14 +194475,10 @@
                 "Change Analysis",
                 "image processing"
             ],
-            "contactPoint": {
-                "fn": "Chandra Giri",
-                "hasEmail": "mailto:giri.chandra@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-01",
-            "references": [
-                "https://doi.org/10.3390/rs15205018"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194493,44 +194489,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529541/documents/readme.txt",
-            "describedByType": "text/plain"
+            "references": [
+                "https://doi.org/10.3390/rs15205018"
+            ],
+            "rights": null,
+            "title": "Mangrove Database of CONUS 1980-2020"
         },
         {
-            "title": "Methods for Thyroid Hormone Measurements in Neonatal Rat Brain",
-            "description": "Serum and brain thyroid hormone measurements in rat brain. \n\nThis dataset is associated with the following publication:\nGilbert, M., J. Ford, C. Riutta, K. OShaughnessy, and P.A. Kosian. Reducing Uncertainties in Quantitative Adverse Outcome Pathways by Analysis of Thyroid Hormone in the Neonatal Rat Brain.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  193(2): 192-203, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530336",
-            "keyword": [
-                "developmental neurotoxicity",
-                "Adverse Outcome Pathways (AOPs)",
-                "endocrine disruption",
-                "Children's Environmental Health",
-                "thyroid hormone"
-            ],
             "contactPoint": {
                 "fn": "Jermaine Ford",
                 "hasEmail": "mailto:ford.jermaine@epa.gov"
             },
+            "description": "Serum and brain thyroid hormone measurements in rat brain. \n\nThis dataset is associated with the following publication:\nGilbert, M., J. Ford, C. Riutta, K. OShaughnessy, and P.A. Kosian. Reducing Uncertainties in Quantitative Adverse Outcome Pathways by Analysis of Thyroid Hormone in the Neonatal Rat Brain.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  193(2): 192-203, (2023).",
             "distribution": [
                 {
-                    "title": "Science Hub M0918 Brain Hormone Methods Science .xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530336/Science%20Hub%20M0918%20Brain%20Hormone%20Methods%20Science%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science Hub M0918 Brain Hormone Methods Science .xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530336",
+            "keyword": [
+                "developmental neurotoxicity",
+                "Adverse Outcome Pathways (AOPs)",
+                "endocrine disruption",
+                "Children's Environmental Health",
+                "thyroid hormone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-01",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfad040",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10732312"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194540,19 +194533,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfad040",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10732312"
+            ],
+            "rights": null,
+            "title": "Methods for Thyroid Hormone Measurements in Neonatal Rat Brain"
         },
         {
-            "title": "Where forest may not return in the western United States",
-            "description": "Data from the National Land Cover Database (NLCD) were used to examine where forest was lost in the western United States between 2001 and 2004 and had not returned to forest by 2016 (the latest date of land cover in NLCD at the time of the analysis).  Remotely sensed vegetation indices were used to guide interpretation of the land cover trends. \n\nThis dataset is associated with the following publication:\nWickham, J., A. Neale, K. Riitters, M. Nash, J. Dewitz, S. Jin, M. Van Fossen, and D. Rosenbaum. Where forest may not return in the western United States.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 146: 109756, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
+            "description": "Data from the National Land Cover Database (NLCD) were used to examine where forest was lost in the western United States between 2001 and 2004 and had not returned to forest by 2016 (the latest date of land cover in NLCD at the time of the analysis).  Remotely sensed vegetation indices were used to guide interpretation of the land cover trends. \n\nThis dataset is associated with the following publication:\nWickham, J., A. Neale, K. Riitters, M. Nash, J. Dewitz, S. Jin, M. Van Fossen, and D. Rosenbaum. Where forest may not return in the western United States.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 146: 109756, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://mrlc.gov",
+                    "title": "https://mrlc.gov"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530333",
             "keyword": [
@@ -194563,19 +194566,10 @@
                 "NLCD",
                 "MRLC"
             ],
-            "contactPoint": {
-                "fn": "James Wickham",
-                "hasEmail": "mailto:wickham.james@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://mrlc.gov",
-                    "accessURL": "https://mrlc.gov"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-12-07",
-            "references": [
-                "https://doi.org/10.1016/j.ecolind.2022.109756"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194585,114 +194579,115 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolind.2022.109756"
+            ],
+            "rights": null,
+            "title": "Where forest may not return in the western United States"
         },
         {
-            "title": "Columbia River Scenario Temperatures and Shade",
-            "description": "This dataset includes supporting data for the paper \"Riparian vegetation shade restoration and loss effects on recent and future stream temperatures\" by Fuller et al. 2022.  Data include temperature predictions for stream reaches in the MidColumbia and Oregon Coast NorWEST processing units for different vegetation (current vegetation, restored riparian vegetation, and riparian vegetation removal) and climate change scenarios (years 2000, 2040, and 2080).  Also included are percent shade estimates for the same scenarios and temperature and discharge associated with tributary outlets to the Columbia River. \n\nThis dataset is associated with the following publication:\nFuller, M.R., P. Leinenbach, N.E. Detenbeck, R. Labiosa, and D.J. Isaak. Riparian vegetation shade restoration and loss effects on recent and future stream temperatures.   RESTORATION ECOLOGY. Blackwell Publishing, Malden, MA, USA, 30(7): e13626, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529983",
-            "keyword": [
-                "climate change",
-                "coldwater refuges",
-                "Columbia River",
-                "spatial stream network model",
-                "ecological forecasting",
-                "riparian shade restoration"
-            ],
             "contactPoint": {
                 "fn": "Naomi Detenbeck",
                 "hasEmail": "mailto:detenbeck.naomi@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529983/documents/Fuller_etal_2022_EcoRes_Data_README.txt",
+            "describedByType": "text/plain",
+            "description": "This dataset includes supporting data for the paper \"Riparian vegetation shade restoration and loss effects on recent and future stream temperatures\" by Fuller et al. 2022.  Data include temperature predictions for stream reaches in the MidColumbia and Oregon Coast NorWEST processing units for different vegetation (current vegetation, restored riparian vegetation, and riparian vegetation removal) and climate change scenarios (years 2000, 2040, and 2080).  Also included are percent shade estimates for the same scenarios and temperature and discharge associated with tributary outlets to the Columbia River. \n\nThis dataset is associated with the following publication:\nFuller, M.R., P. Leinenbach, N.E. Detenbeck, R. Labiosa, and D.J. Isaak. Riparian vegetation shade restoration and loss effects on recent and future stream temperatures.   RESTORATION ECOLOGY. Blackwell Publishing, Malden, MA, USA, 30(7): e13626, (2022).",
             "distribution": [
                 {
-                    "title": "MC_AUG_SSN_predictions.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/MC_AUG_SSN_predictions.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MC_AUG_SSN_predictions.zip"
                 },
                 {
-                    "title": "OC_AUG_SSN_predictions.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/OC_AUG_SSN_predictions.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "OC_AUG_SSN_predictions.zip"
                 },
                 {
-                    "title": "Fuller_etal_2022_EcoRes_Data_README.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/Fuller_etal_2022_EcoRes_Data_README.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Fuller_etal_2022_EcoRes_Data_README.txt"
                 },
                 {
-                    "title": "OCShade.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/OCShade.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "OCShade.zip"
                 },
                 {
-                    "title": "OC_trib_outflow_points.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/OC_trib_outflow_points.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "OC_trib_outflow_points.zip"
                 },
                 {
-                    "title": "OC_pred_edges.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/OC_pred_edges.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "OC_pred_edges.zip"
                 },
                 {
-                    "title": "MCShade.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/MCShade.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MCShade.zip"
                 },
                 {
-                    "title": "MC_trib_outflow_points.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/MC_trib_outflow_points.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MC_trib_outflow_points.zip"
                 },
                 {
-                    "title": "MC_pred_edges.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/MC_pred_edges.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MC_pred_edges.zip"
                 },
                 {
-                    "title": "OCShade.shp.xml",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/OCShade.shp.xml",
-                    "mediaType": "application/xml"
+                    "mediaType": "application/xml",
+                    "title": "OCShade.shp.xml"
                 },
                 {
-                    "title": "OC_trib_outflow_points.shp.xml",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/OC_trib_outflow_points.shp.xml",
-                    "mediaType": "application/xml"
+                    "mediaType": "application/xml",
+                    "title": "OC_trib_outflow_points.shp.xml"
                 },
                 {
-                    "title": "OC_pred_edges.shp.xml",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/OC_pred_edges.shp.xml",
-                    "mediaType": "application/xml"
+                    "mediaType": "application/xml",
+                    "title": "OC_pred_edges.shp.xml"
                 },
                 {
-                    "title": "MCShade.shp.xml",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/MCShade.shp.xml",
-                    "mediaType": "application/xml"
+                    "mediaType": "application/xml",
+                    "title": "MCShade.shp.xml"
                 },
                 {
-                    "title": "MC_trib_outflow_points.shp.xml",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/MC_trib_outflow_points.shp.xml",
-                    "mediaType": "application/xml"
+                    "mediaType": "application/xml",
+                    "title": "MC_trib_outflow_points.shp.xml"
                 },
                 {
-                    "title": "MC_pred_edges.shp.xml",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529983/MC_pred_edges.shp.xml",
-                    "mediaType": "application/xml"
+                    "mediaType": "application/xml",
+                    "title": "MC_pred_edges.shp.xml"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529983",
+            "keyword": [
+                "climate change",
+                "coldwater refuges",
+                "Columbia River",
+                "spatial stream network model",
+                "ecological forecasting",
+                "riparian shade restoration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-20",
-            "references": [
-                "https://doi.org/10.1111/rec.13626",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9580334"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194703,74 +194698,77 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529983/documents/Fuller_etal_2022_EcoRes_Data_README.txt",
-            "describedByType": "text/plain"
+            "references": [
+                "https://doi.org/10.1111/rec.13626",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9580334"
+            ],
+            "rights": null,
+            "title": "Columbia River Scenario Temperatures and Shade"
         },
         {
-            "title": "Paired Sentinel-2 \u2013 water quality databases for estuaries and tidal freshwater rivers.",
-            "description": "There are five datasets included in this collection.  One dataset (SiteInventoryunique.shp) provides metadata for sampling stations associated with estuarine water quality data focused on chlorophyll measurements from 1984 to 2021 and with ancillary data parameters added. Water quality data compiled by US EPA from multiple sources are provided in a separate .csv file (surfchl_withSiteInvID.csv) also downloadable from EPA's Estuary Data Mapper (EDM; www.epa.gov/edm). Chlorophyll data were collected as part of a project to refine algorithms for chlorophyll a and harmful algae using Sentinel 2 remote sensing data. Water quality data observations can be matched to the station file using the SiteInvID variable. \n\nA station inventory (Sentinel2matchedsets_surface_uniqstns_NAD83.shp) and two additional datasets (also in EDM) are available with matched chlorophyll - remote sensing Sentinel 2 Level 2A data (Sent2matchsurfchl_wStnIndex.csv) and with matched chlorophyll - Sentinel 2 Level 1C data (....csv).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530288",
-            "keyword": [
-                "chlorophyll",
-                "remote sensing",
-                "Sentinel 2",
-                "estuary",
-                "freshwater tidal river",
-                "United States",
-                "Estuaries"
-            ],
             "contactPoint": {
                 "fn": "Steven Rego",
                 "hasEmail": "mailto:rego.steven@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530288/documents/Sentinel2matchedsets_surface_metadata%20Level%201C.csv",
+            "describedByType": "text/csv",
+            "description": "There are five datasets included in this collection.  One dataset (SiteInventoryunique.shp) provides metadata for sampling stations associated with estuarine water quality data focused on chlorophyll measurements from 1984 to 2021 and with ancillary data parameters added. Water quality data compiled by US EPA from multiple sources are provided in a separate .csv file (surfchl_withSiteInvID.csv) also downloadable from EPA's Estuary Data Mapper (EDM; www.epa.gov/edm). Chlorophyll data were collected as part of a project to refine algorithms for chlorophyll a and harmful algae using Sentinel 2 remote sensing data. Water quality data observations can be matched to the station file using the SiteInvID variable. \n\nA station inventory (Sentinel2matchedsets_surface_uniqstns_NAD83.shp) and two additional datasets (also in EDM) are available with matched chlorophyll - remote sensing Sentinel 2 Level 2A data (Sent2matchsurfchl_wStnIndex.csv) and with matched chlorophyll - Sentinel 2 Level 1C data (....csv).",
             "distribution": [
                 {
-                    "title": "surfchl_withSiteInvID.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530288/surfchl_withSiteInvID.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "surfchl_withSiteInvID.zip"
                 },
                 {
-                    "title": "SiteInventoryunique.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530288/SiteInventoryunique.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "SiteInventoryunique.zip"
                 },
                 {
-                    "title": "Sentinel2matchedsets_surface_uniqstns_NAD83.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530288/Sentinel2matchedsets_surface_uniqstns_NAD83.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Sentinel2matchedsets_surface_uniqstns_NAD83.zip"
                 },
                 {
-                    "title": "Sentinel2matchedsets_surface_metadata Level 1C.csv.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530288/Sentinel2matchedsets_surface_metadata%20Level%201C.csv.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Sentinel2matchedsets_surface_metadata Level 1C.csv.xlsx"
                 },
                 {
-                    "title": "Sentinel2matchedsets_surface_metadata Level 1C.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530288/Sentinel2matchedsets_surface_metadata%20Level%201C.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Sentinel2matchedsets_surface_metadata Level 1C.csv"
                 },
                 {
-                    "title": "Sent2matchsurfchl_wStnIndex.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530288/Sent2matchsurfchl_wStnIndex.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Sent2matchsurfchl_wStnIndex.csv"
                 },
                 {
-                    "title": "L1chl_surface_filtered_comb.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530288/L1chl_surface_filtered_comb.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "L1chl_surface_filtered_comb.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530288",
+            "keyword": [
+                "chlorophyll",
+                "remote sensing",
+                "Sentinel 2",
+                "estuary",
+                "freshwater tidal river",
+                "United States",
+                "Estuaries"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-09-13",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -194780,42 +194778,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530288/documents/Sentinel2matchedsets_surface_metadata%20Level%201C.csv",
-            "describedByType": "text/csv"
+            "references": null,
+            "rights": null,
+            "title": "Paired Sentinel-2 \u2013 water quality databases for estuaries and tidal freshwater rivers."
         },
         {
-            "title": "National Land Cover Data (NLCD) 2019 reference data for accuracy assessment",
-            "description": "Using survey statistics, reference land cover data to compare to mapped land cover data for development of data quality and its evaluation. \n\nThis dataset is associated with the following publication:\nWickham, J., S. Stehman, D. Sorenson, L. Gass, and J. Dewitz. Thematic accuracy assessment of the NLCD 2019 land cover for the conterminous United States.   GIScience and Remote Sensing. Taylor & Francis Group, London,  UK, 60(1): 2181143, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530414",
-            "keyword": [
-                "land cover",
-                "NLCD",
-                "MRLC",
-                "essential climate variable"
-            ],
             "contactPoint": {
                 "fn": "James Wickham",
                 "hasEmail": "mailto:wickham.james@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530414/documents/NLCD2019ReferenceDataDictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Using survey statistics, reference land cover data to compare to mapped land cover data for development of data quality and its evaluation. \n\nThis dataset is associated with the following publication:\nWickham, J., S. Stehman, D. Sorenson, L. Gass, and J. Dewitz. Thematic accuracy assessment of the NLCD 2019 land cover for the conterminous United States.   GIScience and Remote Sensing. Taylor & Francis Group, London,  UK, 60(1): 2181143, (2023).",
             "distribution": [
                 {
-                    "title": "NLCD2019_AA_RefData.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530414/NLCD2019_AA_RefData.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "NLCD2019_AA_RefData.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530414",
+            "keyword": [
+                "land cover",
+                "NLCD",
+                "MRLC",
+                "essential climate variable"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-01",
-            "references": [
-                "https://doi.org/10.1080/15481603.2023.2181143"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194826,42 +194822,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530414/documents/NLCD2019ReferenceDataDictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1080/15481603.2023.2181143"
+            ],
+            "rights": null,
+            "title": "National Land Cover Data (NLCD) 2019 reference data for accuracy assessment"
         },
         {
-            "title": "Stable Isotope data for Vadose Zone Leaching Study, Corvallis Oregon",
-            "description": "Nitrate concentration and stable isotope data from lysimeters in a vadose zone leaching study.  Lysimeters were installed at 0.8, 1.5 and 3 m depth within the soil.  In addition, stable water isotope data of lysimeter water and precipitation are included.  ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529554",
-            "keyword": [
-                "nitrogen stable isotopes",
-                "water stable isotope",
-                "lysimeters",
-                "Nitrate Flux",
-                "vadose zone"
-            ],
             "contactPoint": {
                 "fn": "Jacqueline Brooks",
                 "hasEmail": "mailto:brooks.reneej@epa.gov"
             },
+            "description": "Nitrate concentration and stable isotope data from lysimeters in a vadose zone leaching study.  Lysimeters were installed at 0.8, 1.5 and 3 m depth within the soil.  In addition, stable water isotope data of lysimeter water and precipitation are included.  ",
             "distribution": [
                 {
-                    "title": "VCOR Isotope DataSet for SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529554/VCOR%20Isotope%20DataSet%20for%20SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "VCOR Isotope DataSet for SciHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529554",
+            "keyword": [
+                "nitrogen stable isotopes",
+                "water stable isotope",
+                "lysimeters",
+                "Nitrate Flux",
+                "vadose zone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-01",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -194870,52 +194866,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Stable Isotope data for Vadose Zone Leaching Study, Corvallis Oregon"
         },
         {
-            "title": "Comparison of in silico, in vitro, and in vivo toxicity benchmarks suggests a role for ToxCast data in ecological hazard assessment",
-            "description": "Supplemental data for \"Schaupp CM, Maloney EM, Mattingly K, Olker JH, Villeneuve DL. Comparison of in silico, in vitro, and in vivo toxicity benchmarks suggests a role for ToxCast data in ecological hazard assessment. Toxicol Sci. 2023 Jul 25:kfad072. doi: 10.1093/toxsci/kfad072. Epub ahead of print. PMID: 37490521.\". \n\nThis dataset is associated with the following publication:\nSchaupp, C., E. Maloney, K. Mattingly, J. Olker, and D. Villeneuve. Comparison of in silico, in vitro, and in vivo toxicity benchmarks suggests a role for ToxCast data in ecological hazard assessment..   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  195(2): 145-154, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529448",
-            "keyword": [
-                "Alternative toxicity testing",
-                "qsar",
-                "new approach methodologies",
-                "high-throughput screening",
-                "ecological risk assessment"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Supplemental data for \"Schaupp CM, Maloney EM, Mattingly K, Olker JH, Villeneuve DL. Comparison of in silico, in vitro, and in vivo toxicity benchmarks suggests a role for ToxCast data in ecological hazard assessment. Toxicol Sci. 2023 Jul 25:kfad072. doi: 10.1093/toxsci/kfad072. Epub ahead of print. PMID: 37490521.\". \n\nThis dataset is associated with the following publication:\nSchaupp, C., E. Maloney, K. Mattingly, J. Olker, and D. Villeneuve. Comparison of in silico, in vitro, and in vivo toxicity benchmarks suggests a role for ToxCast data in ecological hazard assessment..   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  195(2): 145-154, (2023).",
             "distribution": [
                 {
-                    "title": "toxsci-23-0080-File003.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529448/toxsci-23-0080-File003.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "toxsci-23-0080-File003.docx"
                 },
                 {
-                    "title": "toxsci-23-0080-File005.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529448/toxsci-23-0080-File005.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "toxsci-23-0080-File005.xlsx"
                 },
                 {
-                    "title": "toxsci-23-0080-File004.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529448/toxsci-23-0080-File004.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "toxsci-23-0080-File004.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529448",
+            "keyword": [
+                "Alternative toxicity testing",
+                "qsar",
+                "new approach methodologies",
+                "high-throughput screening",
+                "ecological risk assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-25",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfad072"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194925,41 +194919,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfad072"
+            ],
+            "rights": null,
+            "title": "Comparison of in silico, in vitro, and in vivo toxicity benchmarks suggests a role for ToxCast data in ecological hazard assessment"
         },
         {
-            "title": "Non-target chemical features found in: De facto water reuse - Investigating the fate and transport of chemicals of emerging concern from wastewater discharge through drinking water treatment using non-targeted analysis and suspect screening",
-            "description": "A full list of non-target chemical features found in the study \"De facto water reuse - Investigating the fate and transport of chemicals of emerging concern from wastewater discharge through drinking water treatment using non-targeted analysis and suspect screening.\" This would include all identified and unidentified chemicals found in a watershed with wastewater, surface water, and drinking water, chemicals that were found to survive drinking water treatment. \n\nThis dataset is associated with the following publication:\nBrunelle, L., A. Batt, A. Chao, S. Glassmeyer, N. Quinete, D. Alvarez, D. Kolpin, E. Furlong, M. Mills, and D. Aga. De facto water reuse - Investigating the fate and transport of chemicals of emerging concern from wastewater discharge through drinking water treatment using non-targeted analysis and suspect screening.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58(5): 2468-2478, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530331",
-            "keyword": [
-                "De Facto Water Reuse",
-                "surface water",
-                "Ambient Water",
-                "chemicals"
-            ],
             "contactPoint": {
                 "fn": "Angela Batt",
                 "hasEmail": "mailto:batt.angela@epa.gov"
             },
+            "description": "A full list of non-target chemical features found in the study \"De facto water reuse - Investigating the fate and transport of chemicals of emerging concern from wastewater discharge through drinking water treatment using non-targeted analysis and suspect screening.\" This would include all identified and unidentified chemicals found in a watershed with wastewater, surface water, and drinking water, chemicals that were found to survive drinking water treatment. \n\nThis dataset is associated with the following publication:\nBrunelle, L., A. Batt, A. Chao, S. Glassmeyer, N. Quinete, D. Alvarez, D. Kolpin, E. Furlong, M. Mills, and D. Aga. De facto water reuse - Investigating the fate and transport of chemicals of emerging concern from wastewater discharge through drinking water treatment using non-targeted analysis and suspect screening.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58(5): 2468-2478, (2024).",
             "distribution": [
                 {
-                    "title": "DeFactoWaterReuse-metadata-Aug2023.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530331/DeFactoWaterReuse-metadata-Aug2023.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DeFactoWaterReuse-metadata-Aug2023.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530331",
+            "keyword": [
+                "De Facto Water Reuse",
+                "surface water",
+                "Ambient Water",
+                "chemicals"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-31",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c07514"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -194969,20 +194963,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c07514"
+            ],
+            "rights": null,
+            "title": "Non-target chemical features found in: De facto water reuse - Investigating the fate and transport of chemicals of emerging concern from wastewater discharge through drinking water treatment using non-targeted analysis and suspect screening"
         },
         {
-            "title": "PFAS Measurements in Fayetteville, NC water and serum of residents",
-            "description": "Measures of PFAS concentration in blood of private wells in Fayetteville, NC as well as blood serum levels of well users. Some additional demographic/survey data. This dataset is not publicly accessible because: Data is property of NC State. It can be accessed through the following means: Contact the author. Format: Data is property of NC State. \n\nThis dataset is associated with the following publication:\nKotlarz, N., T. Guillette, C. Critchley, D. Collier, S. Lea, J. McCord, M. Strynar, M. Cuffney, Z. Hopkins, D. Knappe, and J. Hoppin. Per- and polyfluoroalkyl ether acids in well water and blood serum from private well users residing by a fluorochemical facility near Fayetteville, North Carolina.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 34: 97-107, (2024).",
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
+                "fn": "James McCord",
+                "hasEmail": "mailto:mccord.james@epa.gov"
+            },
+            "description": "Measures of PFAS concentration in blood of private wells in Fayetteville, NC as well as blood serum levels of well users. Some additional demographic/survey data. This dataset is not publicly accessible because: Data is property of NC State. It can be accessed through the following means: Contact the author. Format: Data is property of NC State. \n\nThis dataset is associated with the following publication:\nKotlarz, N., T. Guillette, C. Critchley, D. Collier, S. Lea, J. McCord, M. Strynar, M. Cuffney, Z. Hopkins, D. Knappe, and J. Hoppin. Per- and polyfluoroalkyl ether acids in well water and blood serum from private well users residing by a fluorochemical facility near Fayetteville, North Carolina.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 34: 97-107, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529359",
             "keyword": [
                 "drinking water",
@@ -194994,14 +194992,10 @@
                 "PFAS",
                 "blood serum"
             ],
-            "contactPoint": {
-                "fn": "James McCord",
-                "hasEmail": "mailto:mccord.james@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-26",
-            "references": [
-                "https://doi.org/10.1038/s41370-023-00626-x"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195011,40 +195005,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-023-00626-x"
+            ],
+            "rights": null,
+            "title": "PFAS Measurements in Fayetteville, NC water and serum of residents"
         },
         {
-            "title": "Effects of UAS Rotor Wash on Air Quality Measurements Data Set",
-            "description": ": Laboratory and field tests examined the potential for unmanned aircraft system (UAS) rotor wash effects on gas and particle measurements from a biomass combustion source. Tests compared simultaneous placement of two sets of CO and CO2 gas sensors and PM2.5 instruments on a UAS body and on a vertical or horizontal extension arm beyond the rotors. For 1 Hz temporal concentration comparisons, correlations of body versus arm placement for the PM2.5 particle sensors yielded R2 = 0.85, and for both gas sensor pairs, exceeded an R2 of 0.90. Increasing the timestep to 10 s average concentrations throughout the burns improved the R2 value for the PM2.5 to 0.95 from 0.85. Finally, comparison of the whole-test average concentrations further increased the correlations between body- and arm-mounted sensors, exceeding an R2 of 0.98 for both gases and particle measurements. Evaluation of PM2.5 emission factors with single-factor ANOVA analyses showed no significant differences between the values derived from the arm, either vertical or horizontal, and those from the body. These results suggest that rotor wash effects on body- and arm-mounted sensors are minimal in scenarios where short-duration, time-averaged concentrations are used to calculate emission factors and whole-area flux values. \n\nThis dataset is associated with the following publication:\nAurell, J., and B. Gullett. Effects of UAS Rotor Wash on Air Quality Measurements.   Drones. MDPI, Basel,  SWITZERLAND,  0, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530478",
-            "keyword": [
-                "rotor wash",
-                "smoke plumes",
-                "UAS",
-                "Gas Sensors"
-            ],
             "contactPoint": {
                 "fn": "Johanna Aurell",
                 "hasEmail": "mailto:aurell.johanna@epa.gov"
             },
+            "description": ": Laboratory and field tests examined the potential for unmanned aircraft system (UAS) rotor wash effects on gas and particle measurements from a biomass combustion source. Tests compared simultaneous placement of two sets of CO and CO2 gas sensors and PM2.5 instruments on a UAS body and on a vertical or horizontal extension arm beyond the rotors. For 1 Hz temporal concentration comparisons, correlations of body versus arm placement for the PM2.5 particle sensors yielded R2 = 0.85, and for both gas sensor pairs, exceeded an R2 of 0.90. Increasing the timestep to 10 s average concentrations throughout the burns improved the R2 value for the PM2.5 to 0.95 from 0.85. Finally, comparison of the whole-test average concentrations further increased the correlations between body- and arm-mounted sensors, exceeding an R2 of 0.98 for both gases and particle measurements. Evaluation of PM2.5 emission factors with single-factor ANOVA analyses showed no significant differences between the values derived from the arm, either vertical or horizontal, and those from the body. These results suggest that rotor wash effects on body- and arm-mounted sensors are minimal in scenarios where short-duration, time-averaged concentrations are used to calculate emission factors and whole-area flux values. \n\nThis dataset is associated with the following publication:\nAurell, J., and B. Gullett. Effects of UAS Rotor Wash on Air Quality Measurements.   Drones. MDPI, Basel,  SWITZERLAND,  0, (2024).",
             "distribution": [
                 {
-                    "title": "Science Hub Aurell and Gullett Drones 2024.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530478/Science%20Hub%20Aurell%20and%20Gullett%20Drones%202024.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science Hub Aurell and Gullett Drones 2024.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530478",
+            "keyword": [
+                "rotor wash",
+                "smoke plumes",
+                "UAS",
+                "Gas Sensors"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-12",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -195053,42 +195049,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Effects of UAS Rotor Wash on Air Quality Measurements Data Set"
         },
         {
-            "title": "Niche changes of three fish species in Narragansett Bay",
-            "description": "Non-EPA data are owned by Roger Williams University. \n\nThis dataset is associated with the following publication:\nTaylor, D., C. Pearson, L. Green-Gavrielidis, N. Hobbs, C. Thornber, G. Cicchetti, A. Gerber-Williams, and M.C. McManus. Habitat and trophic niche overlap among juvenile black sea bass, tautog, and cunner: interspecific interactions amid a species geographic range expansion.   MARINE ECOLOGY PROGRESS SERIES. Inter-Research, Luhe,  GERMANY, 720: 133-159, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529940",
-            "keyword": [
-                "sediments",
-                "ecology",
-                "fish",
-                "climate change",
-                "stable isotopes"
-            ],
             "contactPoint": {
                 "fn": "Giancarlo Cicchetti",
                 "hasEmail": "mailto:cicchetti.giancarlo@epa.gov"
             },
+            "description": "Non-EPA data are owned by Roger Williams University. \n\nThis dataset is associated with the following publication:\nTaylor, D., C. Pearson, L. Green-Gavrielidis, N. Hobbs, C. Thornber, G. Cicchetti, A. Gerber-Williams, and M.C. McManus. Habitat and trophic niche overlap among juvenile black sea bass, tautog, and cunner: interspecific interactions amid a species geographic range expansion.   MARINE ECOLOGY PROGRESS SERIES. Inter-Research, Luhe,  GERMANY, 720: 133-159, (2023).",
             "distribution": [
                 {
-                    "title": "EPA Isotope Data ORD 058034 Cicchetti.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529940/EPA%20Isotope%20Data%20ORD%20058034%20Cicchetti.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA Isotope Data ORD 058034 Cicchetti.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529940",
+            "keyword": [
+                "sediments",
+                "ecology",
+                "fish",
+                "climate change",
+                "stable isotopes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-15",
-            "references": [
-                "https://doi.org/10.3354/meps14409"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195098,41 +195092,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3354/meps14409"
+            ],
+            "rights": null,
+            "title": "Niche changes of three fish species in Narragansett Bay"
         },
         {
-            "title": "Marsh migration and hazardous and contaminated sites Rhode Island data",
-            "description": "This dataset provides the data used to identify where potentially hazardous and contaminated sites could interact with future salt marsh migration corridors. The dataset collates data from: 1) the University of Rhode Island, 2) Rhode Island Department of Environmental Management, 3) U.S. Environmental Protection Agency, 4) U.S. Census Bureau , and 5) RIGIS. \n\nThis dataset is associated with the following publication:\nBurman, E., K. Mulvaney, N. Merrill, M. Bradley, and C. Wigand. Hazardous and contaminated sites within salt marsh migration corridors in Rhode Island, USA..   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 331(1 April 2023): 117218, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530479",
-            "keyword": [
-                "climate ad",
-                "hazardous and contaminated sites",
-                "Salt marsh",
-                "marsh migration"
-            ],
             "contactPoint": {
                 "fn": "Kate Mulvaney",
                 "hasEmail": "mailto:mulvaney.kate@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530479/documents/Marsh%20migration%20contaminated%20sites%20Data_dictionary_8_8_2022.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This dataset provides the data used to identify where potentially hazardous and contaminated sites could interact with future salt marsh migration corridors. The dataset collates data from: 1) the University of Rhode Island, 2) Rhode Island Department of Environmental Management, 3) U.S. Environmental Protection Agency, 4) U.S. Census Bureau , and 5) RIGIS. \n\nThis dataset is associated with the following publication:\nBurman, E., K. Mulvaney, N. Merrill, M. Bradley, and C. Wigand. Hazardous and contaminated sites within salt marsh migration corridors in Rhode Island, USA..   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 331(1 April 2023): 117218, (2023).",
             "distribution": [
                 {
-                    "title": "https://zenodo.org/records/7348410",
-                    "accessURL": "https://zenodo.org/records/7348410"
+                    "accessURL": "https://zenodo.org/records/7348410",
+                    "title": "https://zenodo.org/records/7348410"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530479",
+            "keyword": [
+                "climate ad",
+                "hazardous and contaminated sites",
+                "Salt marsh",
+                "marsh migration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-04-15",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2023.117218",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10859864"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195143,21 +195138,24 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530479/documents/Marsh%20migration%20contaminated%20sites%20Data_dictionary_8_8_2022.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2023.117218",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10859864"
+            ],
+            "rights": null,
+            "title": "Marsh migration and hazardous and contaminated sites Rhode Island data"
         },
         {
-            "title": "Virus and bacteria concentration from wastewater",
-            "description": "Numerous studies have shown that adsorption-extraction (AE) method holds promise, yet several uncertainties remain regarding the optimal AE workflow. Several procedural components may influence the recovered concentrations of target nucleic acid, including membrane types, homogenization instruments, speed and duration, and lysis buffer. In this study, 42 different AE workflows that varied these components were compared to determine the optimal workflow by quantifying endogenous SARS-CoV-2, human adenovirus 40/41 (HAdV 40/41), and a bacterial marker gene of fecal contamination (Bacteroides HF183). Our findings suggest that the workflow chosen had a significant impact on SARS-CoV-2 concentrations, whereas it had minimal impact on HF183 and no effect on HAdV 40/41 concentrations. This dataset is not publicly accessible because: data are not owned by the EPA. It can be accessed through the following means: Contact the corresponding author, Warish Ahmed (Warish.Ahmed@csiro.au). Format: data are not owned by the EPA. \n\nThis dataset is associated with the following publication:\nAkter, J., W.J.M. Smith, Y. Liu, S.L. Simpson, P. Thai, A. Korajkic, and W. Ahmed. Comparison of adsorption-extraction (AE) workflows for improved measurements of viral and bacterial nucleic acid in untreated wastewater.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 908: 167966, (2024).",
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
+                "fn": "Asja Korajkic",
+                "hasEmail": "mailto:korajkic.asja@epa.gov"
+            },
+            "description": "Numerous studies have shown that adsorption-extraction (AE) method holds promise, yet several uncertainties remain regarding the optimal AE workflow. Several procedural components may influence the recovered concentrations of target nucleic acid, including membrane types, homogenization instruments, speed and duration, and lysis buffer. In this study, 42 different AE workflows that varied these components were compared to determine the optimal workflow by quantifying endogenous SARS-CoV-2, human adenovirus 40/41 (HAdV 40/41), and a bacterial marker gene of fecal contamination (Bacteroides HF183). Our findings suggest that the workflow chosen had a significant impact on SARS-CoV-2 concentrations, whereas it had minimal impact on HF183 and no effect on HAdV 40/41 concentrations. This dataset is not publicly accessible because: data are not owned by the EPA. It can be accessed through the following means: Contact the corresponding author, Warish Ahmed (Warish.Ahmed@csiro.au). Format: data are not owned by the EPA. \n\nThis dataset is associated with the following publication:\nAkter, J., W.J.M. Smith, Y. Liu, S.L. Simpson, P. Thai, A. Korajkic, and W. Ahmed. Comparison of adsorption-extraction (AE) workflows for improved measurements of viral and bacterial nucleic acid in untreated wastewater.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 908: 167966, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530413",
             "keyword": [
                 "Centrifugation",
@@ -195167,15 +195165,10 @@
                 "adsorption-extraction",
                 "SARS-CoV-2"
             ],
-            "contactPoint": {
-                "fn": "Asja Korajkic",
-                "hasEmail": "mailto:korajkic.asja@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-10-18",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.167966",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10927021"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195185,20 +195178,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.167966",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10927021"
+            ],
+            "rights": null,
+            "title": "Virus and bacteria concentration from wastewater"
         },
         {
-            "title": "Phylogeographical structure and invasion history of the seagrass Zostera japonica in the North Pacific",
-            "description": "Data are molecular markers for describing phylogeographical structure of Zostera japonica. This dataset is not publicly accessible because: EPA does not have access to the data. It can be accessed through the following means: Contact Xiaomei Zhang, lead author. Format: No EPA generated data.  All samples and analyses were conducted by co-authors. \n\nThis dataset is associated with the following publication:\nZhang, X., Y. Li, J. Kaldy, Z. Suonan, T. Komatsu, S. Xu, M. Xu, F. Wang, P. Liu, X. Liu, S. Yue, Y. Zhang, K. Lee, J. Liu, and Y. Zhou. Population genetic patterns across the native and invasive range of a widely distributed seagrass: Phylogeographic structure, invasive history and conservation implications.   Diversity and Distributions. Blackwell Publishing Limited, Oxford,  UK, 30(3): e13803, (2023).",
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
+                "fn": "James Kaldy",
+                "hasEmail": "mailto:kaldy.jim@epa.gov"
+            },
+            "description": "Data are molecular markers for describing phylogeographical structure of Zostera japonica. This dataset is not publicly accessible because: EPA does not have access to the data. It can be accessed through the following means: Contact Xiaomei Zhang, lead author. Format: No EPA generated data.  All samples and analyses were conducted by co-authors. \n\nThis dataset is associated with the following publication:\nZhang, X., Y. Li, J. Kaldy, Z. Suonan, T. Komatsu, S. Xu, M. Xu, F. Wang, P. Liu, X. Liu, S. Yue, Y. Zhang, K. Lee, J. Liu, and Y. Zhou. Population genetic patterns across the native and invasive range of a widely distributed seagrass: Phylogeographic structure, invasive history and conservation implications.   Diversity and Distributions. Blackwell Publishing Limited, Oxford,  UK, 30(3): e13803, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529115",
             "keyword": [
                 "phylogeographica structure",
@@ -195206,14 +195204,10 @@
                 "climate change",
                 "genetic diversity"
             ],
-            "contactPoint": {
-                "fn": "James Kaldy",
-                "hasEmail": "mailto:kaldy.jim@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-02",
-            "references": [
-                "https://doi.org/10.1111/ddi.13803"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195223,68 +195217,67 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/ddi.13803"
+            ],
+            "rights": null,
+            "title": "Phylogeographical structure and invasion history of the seagrass Zostera japonica in the North Pacific"
         },
         {
-            "title": "Expanded ORD PFAS SEM",
-            "description": "We used systematic evidence map methods to summarize the available epidemiological and animal bioassay evidence for an expanded set of ~345 PFAS that were prioritized in 2019 by the EPA\u2019s Center for Computational Toxicology and Exposure (CCTE) for in vitro toxicity and toxicokinetic screening. This work builds upon our previously published evidence map for ~150 PFAS chemicals (Carlson et al. 2022, https://doi.org/10.1289/EHP10343). \n\nThis dataset is associated with the following publication:\nShirke, A., E. Radke-Farabaugh, C. Lin, R. Blain, N. Vetter, c. lemeris, p. hartman, H. Hubbard, M. Angrish, X. Arzuaga Andino, J. Congleton, J. Davis, L. Dishaw, R. Jones, R. Judson, J. Kaiser, A. Kraft, L. Lizarraga, P. Noyes, G. Patlewicz, M. Taylor, A. Williams, K. Chialton, and L. Carlson. Expanded Systematic Evidence Map for Hundreds of Per- and Polyfluoroalkyl Substances (PFAS) and Comprehensive PFAS Human Health Dashboard.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 132(2): CID: 026001, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528783",
-            "keyword": [
-                "PFAS",
-                "systematic review",
-                "Environmental Justice",
-                "per and polyfluoroaklyl substance",
-                "hazard identification"
-            ],
             "contactPoint": {
                 "fn": "Laura Carlson",
                 "hasEmail": "mailto:carlson.laura@epa.gov"
             },
+            "description": "We used systematic evidence map methods to summarize the available epidemiological and animal bioassay evidence for an expanded set of ~345 PFAS that were prioritized in 2019 by the EPA\u2019s Center for Computational Toxicology and Exposure (CCTE) for in vitro toxicity and toxicokinetic screening. This work builds upon our previously published evidence map for ~150 PFAS chemicals (Carlson et al. 2022, https://doi.org/10.1289/EHP10343). \n\nThis dataset is associated with the following publication:\nShirke, A., E. Radke-Farabaugh, C. Lin, R. Blain, N. Vetter, c. lemeris, p. hartman, H. Hubbard, M. Angrish, X. Arzuaga Andino, J. Congleton, J. Davis, L. Dishaw, R. Jones, R. Judson, J. Kaiser, A. Kraft, L. Lizarraga, P. Noyes, G. Patlewicz, M. Taylor, A. Williams, K. Chialton, and L. Carlson. Expanded Systematic Evidence Map for Hundreds of Per- and Polyfluoroalkyl Substances (PFAS) and Comprehensive PFAS Human Health Dashboard.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 132(2): CID: 026001, (2024).",
             "distribution": [
                 {
-                    "title": "https://hawc.epa.gov/assessment/100500256/",
-                    "accessURL": "https://hawc.epa.gov/assessment/100500256/"
+                    "accessURL": "https://hawc.epa.gov/assessment/100500256/",
+                    "title": "https://hawc.epa.gov/assessment/100500256/"
                 },
                 {
-                    "title": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2875",
-                    "accessURL": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2875"
+                    "accessURL": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2875",
+                    "title": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2875"
                 },
                 {
-                    "title": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2877",
-                    "accessURL": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2877"
+                    "accessURL": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2877",
+                    "title": "https://heronet.epa.gov/heronet/index.cfm/project/page/project_id/2877"
                 },
                 {
-                    "title": "https://public.tableau.com/app/profile/literature.inventory/viz/ComprehensivePFASEvidenceMapVisualizations/AnimalStudies",
-                    "accessURL": "https://public.tableau.com/app/profile/literature.inventory/viz/ComprehensivePFASEvidenceMapVisualizations/AnimalStudies"
+                    "accessURL": "https://public.tableau.com/app/profile/literature.inventory/viz/ComprehensivePFASEvidenceMapVisualizations/AnimalStudies",
+                    "title": "https://public.tableau.com/app/profile/literature.inventory/viz/ComprehensivePFASEvidenceMapVisualizations/AnimalStudies"
                 },
                 {
-                    "title": "https://public.tableau.com/app/profile/literature.inventory/viz/ExpandedPFASEvidenceMapVisualizations/ReadMe",
-                    "accessURL": "https://public.tableau.com/app/profile/literature.inventory/viz/ExpandedPFASEvidenceMapVisualizations/ReadMe"
+                    "accessURL": "https://public.tableau.com/app/profile/literature.inventory/viz/ExpandedPFASEvidenceMapVisualizations/ReadMe",
+                    "title": "https://public.tableau.com/app/profile/literature.inventory/viz/ExpandedPFASEvidenceMapVisualizations/ReadMe"
                 },
                 {
-                    "title": "Expanded PFAS SEM_Supplemental Excel File.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528783/Expanded%20PFAS%20SEM_Supplemental%20Excel%20File.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expanded PFAS SEM_Supplemental Excel File.xlsx"
                 },
                 {
-                    "title": "Expanded PFAS SEM_Supplemental Material.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528783/Expanded%20PFAS%20SEM_Supplemental%20Material.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Expanded PFAS SEM_Supplemental Material.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528783",
+            "keyword": [
+                "PFAS",
+                "systematic review",
+                "Environmental Justice",
+                "per and polyfluoroaklyl substance",
+                "hazard identification"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-18",
-            "references": [
-                "https://doi.org/10.1289/ehp13423",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10846678"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195294,35 +195287,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp13423",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10846678"
+            ],
+            "rights": null,
+            "title": "Expanded ORD PFAS SEM"
         },
         {
-            "title": "Community engagement and the importance of partnerships within the Great Lakes Areas of Concern program: A mixed-methods case study",
-            "description": "Supplementary data for \"Alison Rentschler, Kathleen C. Williams, Community engagement and the importance of partnerships within the Great Lakes Areas of Concern program: A mixed-methods case study, Journal of Great Lakes Research, Volume 48, Issue 6, 2022, Pages 1473-1484, ISSN 0380-1330, https://doi.org/10.1016/j.jglr.2022.08.005.\". This dataset is not publicly accessible because: The supplementary data is covered by an IRB with the University of Michigan. It can be accessed through the following means: The supplementary data is available for download through the journal article published online. Format: A file with Figures and Tables is available for download as a docx. file through the journal article published online. \n\nThis dataset is associated with the following publication:\nRentschler, A., and K. Williams. Community engagement and the importance of partnerships within the Great Lakes Areas of Concern program: A mixed-methods case study.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA,  N/A, (2022).",
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
+                "fn": "Kathleen Williams",
+                "hasEmail": "mailto:williams.kathleen@epa.gov"
+            },
+            "description": "Supplementary data for \"Alison Rentschler, Kathleen C. Williams, Community engagement and the importance of partnerships within the Great Lakes Areas of Concern program: A mixed-methods case study, Journal of Great Lakes Research, Volume 48, Issue 6, 2022, Pages 1473-1484, ISSN 0380-1330, https://doi.org/10.1016/j.jglr.2022.08.005.\". This dataset is not publicly accessible because: The supplementary data is covered by an IRB with the University of Michigan. It can be accessed through the following means: The supplementary data is available for download through the journal article published online. Format: A file with Figures and Tables is available for download as a docx. file through the journal article published online. \n\nThis dataset is associated with the following publication:\nRentschler, A., and K. Williams. Community engagement and the importance of partnerships within the Great Lakes Areas of Concern program: A mixed-methods case study.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA,  N/A, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530057",
             "keyword": [
                 "Areas of Concern program",
                 "community engagement",
                 "partnerships"
             ],
-            "contactPoint": {
-                "fn": "Kathleen Williams",
-                "hasEmail": "mailto:williams.kathleen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-06-14",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2022.08.005",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10807300"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195332,57 +195325,60 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2022.08.005",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10807300"
+            ],
+            "rights": null,
+            "title": "Community engagement and the importance of partnerships within the Great Lakes Areas of Concern program: A mixed-methods case study"
         },
         {
-            "title": "Data for Temperature-dependent composition of summertime PM2.5 in observations and model predictions  across the Eastern U.S",
-            "description": "Total fine particle mass (pm25), organic carbon fine particle mass (oc), sulfate fine particle mass (so4), and sulfur dioxide gas (so2) observed EPA AQS sites (ob) and predicted by the CMAQ-CRACMM model v5.4 (mod) for summer 2019 in the United States used in the study of Vannucci et al. ACS ESC 2024. Additional data includes AQS site identifiers as well as ambient air temperature. Aerosol concentrations are in micrograms per cubic meter of air (ug/m3), temperature is in degrees Celsius (iC), and sulfur dioxide is in parts per billion by volume (ppb). Links are provided to obtain the CMAQ code and raw AQS observations.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529132",
-            "keyword": [
-                "CRACMM",
-                "pm2.5",
-                "sulfate",
-                "heat",
-                "temperature",
-                "SOA",
-                "CMAQ",
-                "isoprene",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Havala Pye",
                 "hasEmail": "mailto:pye.havala@epa.gov"
             },
+            "description": "Total fine particle mass (pm25), organic carbon fine particle mass (oc), sulfate fine particle mass (so4), and sulfur dioxide gas (so2) observed EPA AQS sites (ob) and predicted by the CMAQ-CRACMM model v5.4 (mod) for summer 2019 in the United States used in the study of Vannucci et al. ACS ESC 2024. Additional data includes AQS site identifiers as well as ambient air temperature. Aerosol concentrations are in micrograms per cubic meter of air (ug/m3), temperature is in degrees Celsius (iC), and sulfur dioxide is in parts per billion by volume (ppb). Links are provided to obtain the CMAQ code and raw AQS observations.",
             "distribution": [
                 {
-                    "title": "https://www.github.com/USEPA/CMAQ",
-                    "accessURL": "https://www.github.com/USEPA/CMAQ"
+                    "accessURL": "https://www.github.com/USEPA/CMAQ",
+                    "title": "https://www.github.com/USEPA/CMAQ"
                 },
                 {
-                    "title": "https://doi.org/10.5281/zenodo.7218076",
-                    "accessURL": "https://doi.org/10.5281/zenodo.7218076"
+                    "accessURL": "https://doi.org/10.5281/zenodo.7218076",
+                    "title": "https://doi.org/10.5281/zenodo.7218076"
                 },
                 {
-                    "title": "https://www.epa.gov/aqs",
-                    "accessURL": "https://www.epa.gov/aqs"
+                    "accessURL": "https://www.epa.gov/aqs",
+                    "title": "https://www.epa.gov/aqs"
                 },
                 {
-                    "title": "vannucci_obs_model_data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529132/vannucci_obs_model_data.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "vannucci_obs_model_data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529132",
+            "keyword": [
+                "CRACMM",
+                "pm2.5",
+                "sulfate",
+                "heat",
+                "temperature",
+                "SOA",
+                "CMAQ",
+                "isoprene",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-18",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -195391,62 +195387,60 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Data for Temperature-dependent composition of summertime PM2.5 in observations and model predictions  across the Eastern U.S"
         },
         {
-            "title": "Data for: Leveraging scientific community knowledge for air quality model chemistry parameterizations",
-            "description": "Files contain values from Figures 1, 2, and 3 of the article by Pye et al., \"Leveraging scientific community knowledge for air quality model chemistry parameterizations,\" scheduled for publication in EM in January 2024. Figures 2 and 3 are available in csv and excel spreadsheet format. Figure 1 is only available in spreadsheet format. Figure 1 shows gas and aerosol-phase chemistry representations in CMAQ since 2010. Figure 2 shows ozone and SOA formation potential (in g/g) for CRACMM species. Figure 3 shows the size (number of species and reactions) for various chemical mechanisms. \n\nThis dataset is associated with the following publication:\nPye, H., R. Schwantes, K. Barsanti, V.F. McNeill, and G. Wolfe. Leveraging scientific community knowledge for air quality model chemistry parameterizations.   EM Magazine. Air and Waste Management Association, Pittsburgh, PA, USA,  24-31, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529808",
-            "keyword": [
-                "Ozone",
-                "Chemical Mechanism",
-                "CRACMM",
-                "HAP",
-                "CMAQ",
-                "secondary organic aerosol (SOA)",
-                "Nitrogen and Co-pollutants"
-            ],
             "contactPoint": {
                 "fn": "Havala Pye",
                 "hasEmail": "mailto:pye.havala@epa.gov"
             },
+            "description": "Files contain values from Figures 1, 2, and 3 of the article by Pye et al., \"Leveraging scientific community knowledge for air quality model chemistry parameterizations,\" scheduled for publication in EM in January 2024. Figures 2 and 3 are available in csv and excel spreadsheet format. Figure 1 is only available in spreadsheet format. Figure 1 shows gas and aerosol-phase chemistry representations in CMAQ since 2010. Figure 2 shows ozone and SOA formation potential (in g/g) for CRACMM species. Figure 3 shows the size (number of species and reactions) for various chemical mechanisms. \n\nThis dataset is associated with the following publication:\nPye, H., R. Schwantes, K. Barsanti, V.F. McNeill, and G. Wolfe. Leveraging scientific community knowledge for air quality model chemistry parameterizations.   EM Magazine. Air and Waste Management Association, Pittsburgh, PA, USA,  24-31, (2024).",
             "distribution": [
                 {
-                    "title": "https://www.github.com/USEPA/CMAQ",
-                    "accessURL": "https://www.github.com/USEPA/CMAQ"
+                    "accessURL": "https://www.github.com/USEPA/CMAQ",
+                    "title": "https://www.github.com/USEPA/CMAQ"
                 },
                 {
-                    "title": "https://doi.org/10.5281/zenodo.7218076",
-                    "accessURL": "https://doi.org/10.5281/zenodo.7218076"
+                    "accessURL": "https://doi.org/10.5281/zenodo.7218076",
+                    "title": "https://doi.org/10.5281/zenodo.7218076"
                 },
                 {
-                    "title": "Fig2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529808/Fig2.csv",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Fig2.csv"
                 },
                 {
-                    "title": "Fig3.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529808/Fig3.csv",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Fig3.csv"
                 },
                 {
-                    "title": "20231120_pye_em_figuredata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529808/20231120_pye_em_figuredata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20231120_pye_em_figuredata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529808",
+            "keyword": [
+                "Ozone",
+                "Chemical Mechanism",
+                "CRACMM",
+                "HAP",
+                "CMAQ",
+                "secondary organic aerosol (SOA)",
+                "Nitrogen and Co-pollutants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-20",
-            "references": [
-                "https://www.awma.org/emcurrentissue"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195456,19 +195450,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.awma.org/emcurrentissue"
+            ],
+            "rights": null,
+            "title": "Data for: Leveraging scientific community knowledge for air quality model chemistry parameterizations"
         },
         {
-            "title": "Data for \"Predictions of PFAS regional-scale atmospheric deposition and ambient air exposure\" published in Science of the Total Environment, Aug 2023",
-            "description": "The dataset provided here documents the information used to generate figures for \"Predictions of PFAS regional-scale atmospheric deposition and ambient air exposure\" published in Science of the Total Environment. \n\nThis dataset is associated with the following publication:\nD'Ambro, E., B. Murphy, J. Bash, R. Gilliam, and H. Pye. Predictions of PFAS regional-scale atmospheric deposition and ambient air exposure.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 902: N/A, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Emma D'Ambro",
+                "hasEmail": "mailto:dambro.emma@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529815/documents/DAmbro_etal_2023_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The dataset provided here documents the information used to generate figures for \"Predictions of PFAS regional-scale atmospheric deposition and ambient air exposure\" published in Science of the Total Environment. \n\nThis dataset is associated with the following publication:\nD'Ambro, E., B. Murphy, J. Bash, R. Gilliam, and H. Pye. Predictions of PFAS regional-scale atmospheric deposition and ambient air exposure.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 902: N/A, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529815/DAmbroMurphy_CMAQPFAS_Chemours_STotEn2023_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DAmbroMurphy_CMAQPFAS_Chemours_STotEn2023_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529815",
             "keyword": [
@@ -195479,21 +195485,10 @@
                 "CMAQ",
                 "Environmental Justice"
             ],
-            "contactPoint": {
-                "fn": "Emma D'Ambro",
-                "hasEmail": "mailto:dambro.emma@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "DAmbroMurphy_CMAQPFAS_Chemours_STotEn2023_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529815/DAmbroMurphy_CMAQPFAS_Chemours_STotEn2023_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-10",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.166256",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10642304"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195504,69 +195499,77 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529815/documents/DAmbro_etal_2023_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.166256",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10642304"
+            ],
+            "rights": null,
+            "title": "Data for \"Predictions of PFAS regional-scale atmospheric deposition and ambient air exposure\" published in Science of the Total Environment, Aug 2023"
         },
         {
-            "title": "By-degree Health and Economic Impacts of Lyme Disease, Eastern and Midwestern United States",
-            "description": "Data for \"By-degree Health and Economic Impacts of Lyme Disease, Eastern and Midwestern United States\", published March 2024. The datasets show cases by state,\tfips code,\tcase status, sex, age (by 5-year increments), and frequency. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530485",
-            "keyword": [
-                "Lyme Disease",
-                "Animal Tick Borne Diseases",
-                "Animal Tick-Borne Diseases",
-                "Animal Vector-Borne Diseases",
-                "eastern US",
-                "midwestern US",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Caitlin Gould",
                 "hasEmail": "mailto:gould.caitlin@epa.gov"
             },
+            "description": "Data for \"By-degree Health and Economic Impacts of Lyme Disease, Eastern and Midwestern United States\", published March 2024. The datasets show cases by state,\tfips code,\tcase status, sex, age (by 5-year increments), and frequency. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "aggregate_withgeog_1992_2007_epa.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530485/aggregate_withgeog_1992_2007_epa.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "aggregate_withgeog_1992_2007_epa.xlsx"
                 },
                 {
-                    "title": "aggregate_withgeog_2008_2019_epa.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530485/aggregate_withgeog_2008_2019_epa.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "aggregate_withgeog_2008_2019_epa.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530485",
+            "keyword": [
+                "Lyme Disease",
+                "Animal Tick Borne Diseases",
+                "Animal Tick-Borne Diseases",
+                "Animal Vector-Borne Diseases",
+                "eastern US",
+                "midwestern US",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-11-30",
-            "references": [
-                "https://dx.doi.org/10.1007/s10393-024-01676-9"
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
+                "https://dx.doi.org/10.1007/s10393-024-01676-9"
+            ],
+            "rights": null,
+            "title": "By-degree Health and Economic Impacts of Lyme Disease, Eastern and Midwestern United States"
         },
         {
-            "title": "Benton Harbor Water Study Data",
-            "description": "This dataset represents all of the data collected by EPA during the Benton Harbor Drinking Water Study, which was published as an EPA report: Tully, J., S. Shilling, V. Bosscher, M. Schock, and D. Lytle. Benton Harbor Drinking Water Study. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.\nFor the journal article: An evaluation of properly operated NSF/ANSI-53 Pb certified drinking water filters in Benton Harbor, MI, published in 2024 (https://doi.org/10.2166/wh.2024.231). A subset of the filter study data, background water quality data, and particulate sample data was evaluated. \n\nThis dataset is associated with the following publication:\nTully, J., M. Schock, S. Shilling, V. Bosscher, D. Lytle, S. Harmon, and C. Bennett-Stamper. An evaluation of properly operated NSF/ANSI-53 Pb certified drinking water filters in Benton Harbor, MI.   JOURNAL OF WATER AND HEALTH. IWA Publishing, London,  UK, 22(2): 296-308, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jennifer Tully",
+                "hasEmail": "mailto:tully.jennifer@epa.gov"
+            },
+            "description": "This dataset represents all of the data collected by EPA during the Benton Harbor Drinking Water Study, which was published as an EPA report: Tully, J., S. Shilling, V. Bosscher, M. Schock, and D. Lytle. Benton Harbor Drinking Water Study. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.\nFor the journal article: An evaluation of properly operated NSF/ANSI-53 Pb certified drinking water filters in Benton Harbor, MI, published in 2024 (https://doi.org/10.2166/wh.2024.231). A subset of the filter study data, background water quality data, and particulate sample data was evaluated. \n\nThis dataset is associated with the following publication:\nTully, J., M. Schock, S. Shilling, V. Bosscher, D. Lytle, S. Harmon, and C. Bennett-Stamper. An evaluation of properly operated NSF/ANSI-53 Pb certified drinking water filters in Benton Harbor, MI.   JOURNAL OF WATER AND HEALTH. IWA Publishing, London,  UK, 22(2): 296-308, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://catalog.data.gov/dataset/benton-harbor-drinking-water-study",
+                    "title": "https://catalog.data.gov/dataset/benton-harbor-drinking-water-study"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530330",
             "keyword": [
@@ -195576,19 +195579,10 @@
                 "community",
                 "lead nanoparticulate"
             ],
-            "contactPoint": {
-                "fn": "Jennifer Tully",
-                "hasEmail": "mailto:tully.jennifer@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://catalog.data.gov/dataset/benton-harbor-drinking-water-study",
-                    "accessURL": "https://catalog.data.gov/dataset/benton-harbor-drinking-water-study"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-17",
-            "references": [
-                "https://doi.org/10.2166/wh.2024.231"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195598,41 +195592,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2166/wh.2024.231"
+            ],
+            "rights": null,
+            "title": "Benton Harbor Water Study Data"
         },
         {
-            "title": "NIH Data and Specimen Hub (DASH)",
-            "description": "\"The NICHD Data and Specimen Hub (DASH) is a centralized resource that allows researchers to share and access de-identified data from studies funded by NICHD. DASH also serves as a portal for requesting biospecimens from selected DASH studies.\". \n\nThis dataset is associated with the following publication:\nDeluca, N., K. Thomas, A. Mullikin, R. Slover, L. Stanek, D. Pilant, and E. Hubal. Geographic and demographic variability in serum PFAS concentrations for pregnant women in the United States.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 33(1): 710-724, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530539",
-            "keyword": [
-                "PFAS",
-                "exposure",
-                "national children's study",
-                "Children's Environmental Health"
-            ],
             "contactPoint": {
                 "fn": "Nicole Deluca",
                 "hasEmail": "mailto:deluca.nikki@epa.gov"
             },
+            "description": "\"The NICHD Data and Specimen Hub (DASH) is a centralized resource that allows researchers to share and access de-identified data from studies funded by NICHD. DASH also serves as a portal for requesting biospecimens from selected DASH studies.\". \n\nThis dataset is associated with the following publication:\nDeluca, N., K. Thomas, A. Mullikin, R. Slover, L. Stanek, D. Pilant, and E. Hubal. Geographic and demographic variability in serum PFAS concentrations for pregnant women in the United States.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 33(1): 710-724, (2023).",
             "distribution": [
                 {
-                    "title": "https://dash.nichd.nih.gov/",
-                    "accessURL": "https://dash.nichd.nih.gov/"
+                    "accessURL": "https://dash.nichd.nih.gov/",
+                    "title": "https://dash.nichd.nih.gov/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530539",
+            "keyword": [
+                "PFAS",
+                "exposure",
+                "national children's study",
+                "Children's Environmental Health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-02-09",
-            "references": [
-                "https://doi.org/10.1038/s41370-023-00520-6",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10541323"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195642,20 +195635,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-023-00520-6",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10541323"
+            ],
+            "rights": null,
+            "title": "NIH Data and Specimen Hub (DASH)"
         },
         {
-            "title": "Metadata",
-            "description": "Dataset includes CMAQ predicted results. This dataset is not publicly accessible because: Shanghai Jiao Tong University created the dataset - EPA does not have the dataset. It can be accessed through the following means: Contact - Ping Liu, School of Environmental Science and Engineering, Shanghai Jiao Tong University, Shanghai 200240, China, email: ping_liu@sjtu.edu.cn. Format: Dataset includes CMAQ output files using netcdf format. \n\nThis dataset is associated with the following publication:\nChen, H., P. Liu, Q. Wang, R. Huang, and G. Sarwar. Impact and pathway of halogens on atmospheric oxidants in coastal city clusters in the Yangtze River Delta region in China.   Atmospheric Pollution Research. Turkish National Committee for Air Pollution Research and Control, Izmir,  TURKEY, 15(2): N/A, (2024).",
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
+                "fn": "Golam Sarwar",
+                "hasEmail": "mailto:sarwar.golam@epa.gov"
+            },
+            "description": "Dataset includes CMAQ predicted results. This dataset is not publicly accessible because: Shanghai Jiao Tong University created the dataset - EPA does not have the dataset. It can be accessed through the following means: Contact - Ping Liu, School of Environmental Science and Engineering, Shanghai Jiao Tong University, Shanghai 200240, China, email: ping_liu@sjtu.edu.cn. Format: Dataset includes CMAQ output files using netcdf format. \n\nThis dataset is associated with the following publication:\nChen, H., P. Liu, Q. Wang, R. Huang, and G. Sarwar. Impact and pathway of halogens on atmospheric oxidants in coastal city clusters in the Yangtze River Delta region in China.   Atmospheric Pollution Research. Turkish National Committee for Air Pollution Research and Control, Izmir,  TURKEY, 15(2): N/A, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529594",
             "keyword": [
                 "atmospheric oxidants",
@@ -195664,14 +195662,10 @@
                 "process analysis",
                 "atmospheric oxidation capacity"
             ],
-            "contactPoint": {
-                "fn": "Golam Sarwar",
-                "hasEmail": "mailto:sarwar.golam@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-11",
-            "references": [
-                "https://doi.org/10.1016/j.apr.2023.101979"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195681,19 +195675,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apr.2023.101979"
+            ],
+            "rights": null,
+            "title": "Metadata"
         },
         {
-            "title": "Demonstrating the reliability of in vivo metabolomics-based chemical grouping: Towards best practice",
-            "description": "The experimental metabolomics data generated during the current study are available in the MetaboLights repository under the identifier MTBLS8274. Portions of this dataset are inaccessible because: L:\\Priv\\Metabolomics. They can be accessed through the following means: L:\\Priv\\Metabolomics. Format: L:\\Priv\\Metabolomics. \n\nThis dataset is associated with the following publication:\nViant, M., E. Amstalden, T. Athersuch, M. Bouhifd, S. Camuzeaux, D. Crizer, P. Driemert, T. Ebbels, D. Ekman, B. Flick, V. Giri, M. G?mez-Romero, V. Haake, M. Herold, A. Kende, F. Lai, P. Leonards, P. Lim, G. Lloyd, J. Mosley, C. Namini, J. Rice, S. Romano, C. Sands, M. Smith, T. Sobansky, A. Southam, L. Swindale, B. van Ravenzwaay, T. Walk, R. Weber, F. Zickgraf, and H. Kamp. Demonstrating the reliability of in vivo metabolomics based chemical grouping: towards best practice.   Archives of Toxicology. Springer, New York, NY, USA, 98: 1111-1123, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jonathan Mosley",
+                "hasEmail": "mailto:mosley.jonathan@epa.gov"
+            },
+            "description": "The experimental metabolomics data generated during the current study are available in the MetaboLights repository under the identifier MTBLS8274. Portions of this dataset are inaccessible because: L:\\Priv\\Metabolomics. They can be accessed through the following means: L:\\Priv\\Metabolomics. Format: L:\\Priv\\Metabolomics. \n\nThis dataset is associated with the following publication:\nViant, M., E. Amstalden, T. Athersuch, M. Bouhifd, S. Camuzeaux, D. Crizer, P. Driemert, T. Ebbels, D. Ekman, B. Flick, V. Giri, M. G?mez-Romero, V. Haake, M. Herold, A. Kende, F. Lai, P. Leonards, P. Lim, G. Lloyd, J. Mosley, C. Namini, J. Rice, S. Romano, C. Sands, M. Smith, T. Sobansky, A. Southam, L. Swindale, B. van Ravenzwaay, T. Walk, R. Weber, F. Zickgraf, and H. Kamp. Demonstrating the reliability of in vivo metabolomics based chemical grouping: towards best practice.   Archives of Toxicology. Springer, New York, NY, USA, 98: 1111-1123, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.ebi.ac.uk/metabolights/editor/MTBLS8274/descriptors",
+                    "title": "https://www.ebi.ac.uk/metabolights/editor/MTBLS8274/descriptors"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529781",
             "keyword": [
@@ -195704,20 +195707,10 @@
                 "metabolomics",
                 "Validation"
             ],
-            "contactPoint": {
-                "fn": "Jonathan Mosley",
-                "hasEmail": "mailto:mosley.jonathan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.ebi.ac.uk/metabolights/editor/MTBLS8274/descriptors",
-                    "accessURL": "https://www.ebi.ac.uk/metabolights/editor/MTBLS8274/descriptors"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-06",
-            "references": [
-                "https://doi.org/10.1007/s00204-024-03680-y",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10944399"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195727,46 +195720,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s00204-024-03680-y",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10944399"
+            ],
+            "rights": null,
+            "title": "Demonstrating the reliability of in vivo metabolomics-based chemical grouping: Towards best practice"
         },
         {
-            "title": "Data supporting draft article \"Geographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate\"",
-            "description": "This dataset supports the journal article \"Geographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate\", by Butcher et al. Two Excel spreadsheets containing the data presented/discussed in this paper will be uploaded to Science HUB. Data summaries include (1) a list of lakes included in the analysis (from 2007 National Lakes Assessment), including latitude/longitude coordinates, key lake physical attributes, and the set of vulnerability and risk metric developed and used in this analysis, and (2) a list of relevant articles identified in the literature and used to develop risk hypotheses used in this analysis. \nAll Variable names and units are defined in column headings of each file uploaded to Science HUB. Details about the data and methodology used to develop risk metrics will be described in detail in a published journal article (draft paper will be submitted to the journal Earth Interactions, titled \u201cGeographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate\u201d. \n\nThis dataset is associated with the following publication:\nButcher, J., M. Fernandez, T. Johnson, A. Shabani, and S. Lee. Geographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate.   Earth Interactions. American Meteorological Society, Boston, MA, USA, 27(1): e230004, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528306",
-            "keyword": [
-                "climate change",
-                "HAB",
-                "Risk",
-                "lakes"
-            ],
             "contactPoint": {
                 "fn": "Thomas Johnson",
                 "hasEmail": "mailto:johnson.thomas@epa.gov"
             },
+            "description": "This dataset supports the journal article \"Geographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate\", by Butcher et al. Two Excel spreadsheets containing the data presented/discussed in this paper will be uploaded to Science HUB. Data summaries include (1) a list of lakes included in the analysis (from 2007 National Lakes Assessment), including latitude/longitude coordinates, key lake physical attributes, and the set of vulnerability and risk metric developed and used in this analysis, and (2) a list of relevant articles identified in the literature and used to develop risk hypotheses used in this analysis. \nAll Variable names and units are defined in column headings of each file uploaded to Science HUB. Details about the data and methodology used to develop risk metrics will be described in detail in a published journal article (draft paper will be submitted to the journal Earth Interactions, titled \u201cGeographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate\u201d. \n\nThis dataset is associated with the following publication:\nButcher, J., M. Fernandez, T. Johnson, A. Shabani, and S. Lee. Geographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate.   Earth Interactions. American Meteorological Society, Boston, MA, USA, 27(1): e230004, (2023).",
             "distribution": [
                 {
-                    "title": "Data_Literature Review Results_ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528306/Data_Literature%20Review%20Results_ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data_Literature Review Results_ScienceHub.xlsx"
                 },
                 {
-                    "title": "Data_Lake Chars and Metrics_ScienceHub.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528306/Data_Lake%20Chars%20and%20Metrics_ScienceHub.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Data_Lake Chars and Metrics_ScienceHub.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528306",
+            "keyword": [
+                "climate change",
+                "HAB",
+                "Risk",
+                "lakes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-11-28",
-            "references": [
-                "https://doi.org/10.1175/ei-d-23-0004.1"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195776,42 +195770,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1175/ei-d-23-0004.1"
+            ],
+            "rights": null,
+            "title": "Data supporting draft article \"Geographic Analysis of the Vulnerability of U.S. Lakes to Cyanobacterial Blooms under Future Climate\""
         },
         {
-            "title": "Dataset of Leachate Parameters from an Elevated Temperature Landfill ",
-            "description": "Leachate volumes and composition data before and after a subsurface exothermic reaction. \n\nThis dataset is associated with the following publication:\nKrause, M., W. Eades, N. Detwiler, and T. Tolaymat. Leachate indicators of an elevated temperature landfill.   WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 171: 628-633, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530581",
-            "keyword": [
-                "exothermic",
-                "elevated temperature landfill",
-                "VOCs",
-                "Municipal Solid Waste",
-                "leachate"
-            ],
             "contactPoint": {
                 "fn": "Max Krause",
                 "hasEmail": "mailto:krause.max@epa.gov"
             },
+            "description": "Leachate volumes and composition data before and after a subsurface exothermic reaction. \n\nThis dataset is associated with the following publication:\nKrause, M., W. Eades, N. Detwiler, and T. Tolaymat. Leachate indicators of an elevated temperature landfill.   WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 171: 628-633, (2023).",
             "distribution": [
                 {
-                    "title": "Data for 2023 ETLF Leachate Indicators.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530581/Data%20for%202023%20ETLF%20Leachate%20Indicators.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data for 2023 ETLF Leachate Indicators.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530581",
+            "keyword": [
+                "exothermic",
+                "elevated temperature landfill",
+                "VOCs",
+                "Municipal Solid Waste",
+                "leachate"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-28",
-            "references": [
-                "https://doi.org/10.1016/j.wasman.2023.10.001"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195821,19 +195815,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.wasman.2023.10.001"
+            ],
+            "rights": null,
+            "title": "Dataset of Leachate Parameters from an Elevated Temperature Landfill "
         },
         {
-            "title": "Connecting Stakeholder Priorities and Desired Environmental Attributes for Wetland Restoration Using Ecosystem Services and a Heat Map Analysis for Communications",
-            "description": "Compilation of data used to generate figures and tables in the manuscript. \n\nThis dataset is associated with the following publication:\nHernandez, C., L. Sharpe, C. Jackson, M. Harwell, and T. DeWitt. Connecting Stakeholder Priorities and Desired Environmental Attributes for Wetland Restoration Using Ecosystem Services and a Heat Map Analysis for Communications.   Frontiers in Ecology and Evolution. Frontiers, Lausanne,  SWITZERLAND, 12: 1290090, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Matthew Harwell",
+                "hasEmail": "mailto:harwell.matthew@epa.gov"
+            },
+            "description": "Compilation of data used to generate figures and tables in the manuscript. \n\nThis dataset is associated with the following publication:\nHernandez, C., L. Sharpe, C. Jackson, M. Harwell, and T. DeWitt. Connecting Stakeholder Priorities and Desired Environmental Attributes for Wetland Restoration Using Ecosystem Services and a Heat Map Analysis for Communications.   Frontiers in Ecology and Evolution. Frontiers, Lausanne,  SWITZERLAND, 12: 1290090, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529422/Hernandez-TillamookWetlands_Manuscript%20tables%20and%20figures.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Hernandez-TillamookWetlands_Manuscript tables and figures.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529422",
             "keyword": [
@@ -195844,20 +195848,10 @@
                 "tidal wetlands",
                 "prioritization"
             ],
-            "contactPoint": {
-                "fn": "Matthew Harwell",
-                "hasEmail": "mailto:harwell.matthew@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Hernandez-TillamookWetlands_Manuscript tables and figures.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529422/Hernandez-TillamookWetlands_Manuscript%20tables%20and%20figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-14",
-            "references": [
-                "https://doi.org/10.3389/fevo.2024.1290090"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195867,19 +195861,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fevo.2024.1290090"
+            ],
+            "rights": null,
+            "title": "Connecting Stakeholder Priorities and Desired Environmental Attributes for Wetland Restoration Using Ecosystem Services and a Heat Map Analysis for Communications"
         },
         {
-            "title": "Sun Valley Asthma and AD SciHUB.xlsx ",
-            "description": "Medicaid claims for AD and asthma for all 6 and 7-year-olds between 2016 to 2019 living in the Sun Valley community (zip code 80204). \n\nThis dataset is associated with the following publication:\nBernstein, J.A., L. Wymer, M. Nye, and S. Vesper. The relationship between childhood atopic dermatitis and asthma in an under resourced community.   Allergy and Asthma Proceedings. OceanSide Publications, Providence, RI, USA, 45(2): 108-111, (2024).",
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
+            "description": "Medicaid claims for AD and asthma for all 6 and 7-year-olds between 2016 to 2019 living in the Sun Valley community (zip code 80204). \n\nThis dataset is associated with the following publication:\nBernstein, J.A., L. Wymer, M. Nye, and S. Vesper. The relationship between childhood atopic dermatitis and asthma in an under resourced community.   Allergy and Asthma Proceedings. OceanSide Publications, Providence, RI, USA, 45(2): 108-111, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529197/Sun%20Valley%20Asthma%20and%20AD%20SciHUB.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Sun Valley Asthma and AD SciHUB.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529197",
             "keyword": [
@@ -195890,20 +195894,10 @@
                 "Medicaid",
                 "Center for improving value in Health Care"
             ],
-            "contactPoint": {
-                "fn": "Stephen Vesper",
-                "hasEmail": "mailto:vesper.stephen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Sun Valley Asthma and AD SciHUB.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529197/Sun%20Valley%20Asthma%20and%20AD%20SciHUB.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-28",
-            "references": [
-                "https://doi.org/10.2500/aap.2024.45.230093"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195913,20 +195907,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2500/aap.2024.45.230093"
+            ],
+            "rights": null,
+            "title": "Sun Valley Asthma and AD SciHUB.xlsx "
         },
         {
-            "title": "Global Surface Water Extent Paper",
-            "description": "Global Surface Water Extent Paper. This dataset is not publicly accessible because: Data is the property of Texas A&M University Kingsville. It can be accessed through the following means: Contact Texas A&M University Kingsville. Format: Texas A&M University Kingsville authors are the sole developers and analyzer of the dataset. EPA co-authors only provided scientific guidance and input - including help with writing the paper - and did not access or analyze any of the data used in it. \n\nThis dataset is associated with the following publication:\nRajib, A., A. Khare, H. Golden, B. Gupta, Q. Wu, C. Lane, J. Christensen, Q. Zheng, T. Dahl, J. Ryder, and B. McFall. A call for consistency and integration in global surface water estimates.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 19: 021002, (2024).",
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
+            "description": "Global Surface Water Extent Paper. This dataset is not publicly accessible because: Data is the property of Texas A&M University Kingsville. It can be accessed through the following means: Contact Texas A&M University Kingsville. Format: Texas A&M University Kingsville authors are the sole developers and analyzer of the dataset. EPA co-authors only provided scientific guidance and input - including help with writing the paper - and did not access or analyze any of the data used in it. \n\nThis dataset is associated with the following publication:\nRajib, A., A. Khare, H. Golden, B. Gupta, Q. Wu, C. Lane, J. Christensen, Q. Zheng, T. Dahl, J. Ryder, and B. McFall. A call for consistency and integration in global surface water estimates.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 19: 021002, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1528114",
             "keyword": [
                 "wetlands",
@@ -195935,14 +195933,10 @@
                 "lakes",
                 "global surface water"
             ],
-            "contactPoint": {
-                "fn": "Heather Golden",
-                "hasEmail": "mailto:golden.heather@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-10-01",
-            "references": [
-                "https://doi.org/10.1088/1748-9326/ad1722"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195952,41 +195946,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1748-9326/ad1722"
+            ],
+            "rights": null,
+            "title": "Global Surface Water Extent Paper"
         },
         {
-            "title": "Wisconsin Dep. Of Natural Resources Shallow Groundwater PFAS",
-            "description": "Feature layer displaying sample results from Wisconsin DNR\u2019s Private Well PFAS Study\n\nSample results from Wisconsin DNR\u2019s Private Well PFAS Study: \u201cPrevalence and Source Tracing of PFAS in Shallow Groundwater Used for Drinking Water in Wisconsin\u201d, Environmental Science & Technology.\n\nPer- and polyfluoroalkyl substances (PFAS) and other water quality parameter results from samples collected from 450 homes with shallow private wells throughout Wisconsin. The samples were analyzed for 44 PFAS, major ions, metals, total organic carbon, and indicators of human waste as well as agricultural influence. \n\nMore information about the study can be found at https://dnr.wisconsin.gov/topic/Groundwater/PFASStudy.html. \n\nThis dataset is associated with the following publication:\nSilver, M., W. Phelps, K. Masarik, K. Burke, C. Zhang, A. Schwartz, M. Wang, A.L. Nitka, J. Schutz, T. Trainor, J. Washington, and B. Rheineck. Prevalence and Source Tracing of PFAS in Shallow Groundwater Used for Drinking Water in Wisconsin, USA.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(45): 17415\u201317426, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528718",
-            "keyword": [
-                "Drinking water (Groundwater)",
-                "Drinking water contaminants",
-                "Wisconsin",
-                "PFAS"
-            ],
             "contactPoint": {
                 "fn": "John Washington",
                 "hasEmail": "mailto:washington.john@epa.gov"
             },
+            "description": "Feature layer displaying sample results from Wisconsin DNR\u2019s Private Well PFAS Study\n\nSample results from Wisconsin DNR\u2019s Private Well PFAS Study: \u201cPrevalence and Source Tracing of PFAS in Shallow Groundwater Used for Drinking Water in Wisconsin\u201d, Environmental Science & Technology.\n\nPer- and polyfluoroalkyl substances (PFAS) and other water quality parameter results from samples collected from 450 homes with shallow private wells throughout Wisconsin. The samples were analyzed for 44 PFAS, major ions, metals, total organic carbon, and indicators of human waste as well as agricultural influence. \n\nMore information about the study can be found at https://dnr.wisconsin.gov/topic/Groundwater/PFASStudy.html. \n\nThis dataset is associated with the following publication:\nSilver, M., W. Phelps, K. Masarik, K. Burke, C. Zhang, A. Schwartz, M. Wang, A.L. Nitka, J. Schutz, T. Trainor, J. Washington, and B. Rheineck. Prevalence and Source Tracing of PFAS in Shallow Groundwater Used for Drinking Water in Wisconsin, USA.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(45): 17415\u201317426, (2023).",
             "distribution": [
                 {
-                    "title": "https://data-wi-dnr.opendata.arcgis.com/search?q=shallow%20well%20pfas",
-                    "accessURL": "https://data-wi-dnr.opendata.arcgis.com/search?q=shallow%20well%20pfas"
+                    "accessURL": "https://data-wi-dnr.opendata.arcgis.com/search?q=shallow%20well%20pfas",
+                    "title": "https://data-wi-dnr.opendata.arcgis.com/search?q=shallow%20well%20pfas"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528718",
+            "keyword": [
+                "Drinking water (Groundwater)",
+                "Drinking water contaminants",
+                "Wisconsin",
+                "PFAS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-12",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c02826",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10653221"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -195996,100 +195989,103 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c02826",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10653221"
+            ],
+            "rights": null,
+            "title": "Wisconsin Dep. Of Natural Resources Shallow Groundwater PFAS"
         },
         {
-            "title": "Coastal Generalized Ecosystem Model (CGEM) 1.0: A Complex Biogeochemical Model for Simulating Lower Trophic Levels and Ecosystem Dynamics",
-            "description": "These data describe CGEM functional form output for optional model formulations. These data also include post-processed simulation outputs applied to develop figures in the manuscript.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530541",
-            "keyword": [
-                "modeling",
-                "water quality",
-                "Nitrogen and Co-pollutants",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Brandon Jarvis",
                 "hasEmail": "mailto:jarvis.brandon@epa.gov"
             },
+            "description": "These data describe CGEM functional form output for optional model formulations. These data also include post-processed simulation outputs applied to develop figures in the manuscript.",
             "distribution": [
                 {
-                    "title": "Fig13_WeeksBay_LightAttenuation.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig13_WeeksBay_LightAttenuation.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig13_WeeksBay_LightAttenuation.xlsx"
                 },
                 {
-                    "title": "Fig12_irradiance_LAshelf.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig12_irradiance_LAshelf.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig12_irradiance_LAshelf.xlsx"
                 },
                 {
-                    "title": "Fig11_Weeks_HourlyDO.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig11_Weeks_HourlyDO.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig11_Weeks_HourlyDO.xlsx"
                 },
                 {
-                    "title": "Fig10_SedimentProcesses.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig10_SedimentProcesses.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Fig10_SedimentProcesses.txt"
                 },
                 {
-                    "title": "Fig9_WeeksTempResponse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig9_WeeksTempResponse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig9_WeeksTempResponse.xlsx"
                 },
                 {
-                    "title": "Fig8_TempResponse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig8_TempResponse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig8_TempResponse.xlsx"
                 },
                 {
-                    "title": "Fig7_Shapefiles.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig7_Shapefiles.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Fig7_Shapefiles.zip"
                 },
                 {
-                    "title": "Fig6_NutUptake.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig6_NutUptake.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig6_NutUptake.xlsx"
                 },
                 {
-                    "title": "Fig5_QuotaGrowth.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig5_QuotaGrowth.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig5_QuotaGrowth.xlsx"
                 },
                 {
-                    "title": "Fig4_Photoinhibition.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig4_Photoinhibition.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig4_Photoinhibition.xlsx"
                 },
                 {
-                    "title": "Fig3_TempResponse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig3_TempResponse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig3_TempResponse.xlsx"
                 },
                 {
-                    "title": "Fig2_PAR.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/Fig2_PAR.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig2_PAR.xlsx"
                 },
                 {
-                    "title": "DataDictionary.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530541/DataDictionary.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "DataDictionary.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530541",
+            "keyword": [
+                "modeling",
+                "water quality",
+                "Nitrogen and Co-pollutants",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-18",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -196098,19 +196094,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Coastal Generalized Ecosystem Model (CGEM) 1.0: A Complex Biogeochemical Model for Simulating Lower Trophic Levels and Ecosystem Dynamics"
         },
         {
-            "title": "Changes in forest tree species composition for 2010-2100",
-            "description": "This data is from Clark et al. (2023), \"Future climate change effects on US forest composition may offset benefits of reduced atmospheric deposition of N and S.\" (https://onlinelibrary.wiley.com/doi/10.1111/gcb.16817). The dataset provides the decadal data (2010, 2020, etc., to 2100), for estimates of biomass and stem count, for each county (FIPS) in the lower 48 states, for the 94 tree species analyzed in Horn et al. (2018), separately for the 20 climate and atmospheric deposition scenarios examined in the Clark et al. manuscript. Summary tables and key supporting information are also provided. The data are too large to upload to Science Hub (>10 GB) and are instead available on the DataDryad here: https://datadryad.org/stash/dataset/doi:10.5061/dryad.tht76hf4f. \n\nThis dataset is associated with the following publication:\nClark, C., J. Phelan, J. Ash, J. Buckley, J. Cajka, K. Horn, R.Q. Thomas, and R.D. Sabo. Future climate change effects on U.S. forest composition may offset benefits of reduced atmospheric deposition of N and S.   GLOBAL CHANGE BIOLOGY. Blackwell Publishing, Malden, MA, USA, 29(17): 4793-4810, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Christopher Clark",
+                "hasEmail": "mailto:clark.christopher@epa.gov"
+            },
+            "description": "This data is from Clark et al. (2023), \"Future climate change effects on US forest composition may offset benefits of reduced atmospheric deposition of N and S.\" (https://onlinelibrary.wiley.com/doi/10.1111/gcb.16817). The dataset provides the decadal data (2010, 2020, etc., to 2100), for estimates of biomass and stem count, for each county (FIPS) in the lower 48 states, for the 94 tree species analyzed in Horn et al. (2018), separately for the 20 climate and atmospheric deposition scenarios examined in the Clark et al. manuscript. Summary tables and key supporting information are also provided. The data are too large to upload to Science Hub (>10 GB) and are instead available on the DataDryad here: https://datadryad.org/stash/dataset/doi:10.5061/dryad.tht76hf4f. \n\nThis dataset is associated with the following publication:\nClark, C., J. Phelan, J. Ash, J. Buckley, J. Cajka, K. Horn, R.Q. Thomas, and R.D. Sabo. Future climate change effects on U.S. forest composition may offset benefits of reduced atmospheric deposition of N and S.   GLOBAL CHANGE BIOLOGY. Blackwell Publishing, Malden, MA, USA, 29(17): 4793-4810, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.tht76hf4f",
+                    "title": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.tht76hf4f"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529091",
             "keyword": [
@@ -196121,19 +196124,10 @@
                 "Nitrogen and Co-pollutants",
                 "climate change"
             ],
-            "contactPoint": {
-                "fn": "Christopher Clark",
-                "hasEmail": "mailto:clark.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.tht76hf4f",
-                    "accessURL": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.tht76hf4f"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-08",
-            "references": [
-                "https://doi.org/10.1111/gcb.16817"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196143,45 +196137,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/gcb.16817"
+            ],
+            "rights": null,
+            "title": "Changes in forest tree species composition for 2010-2100"
         },
         {
-            "title": "Estimate of sediment accumulation rates and bottom core ages in northeast lakes",
-            "description": "Supplementary data for the report in the format of an Excel spreadsheet (with data dictionary) and an Microsoft Access database file (downloaded as a zip file). The Access database file contains multiple data tables examined or generated during the project to investigate sediment accumulation rates (SAR) of northeast lakes.\n1. Baud_SARMAR: data downloaded from Baud et al. 2019 for northeast lake sediment accumulation rates.\n2. EPA_Extra_Chron_Data: additional lake sedimentation chronology data.\n3. Lake_Metadata_n701: coordinates, waterbody type, area, elevation, and slope information.\n4. Neotoma_Chron_Data: lake sediment core depth, age estimates, and age model info downloaded from Neotoma.\n5. RARE_Sample_Metadata: RARE project lakes' name, collection date, source.\n6. SAR_Calc_1850_n691: data for variables required by the Baud SAR equation.\n7. SAR_Comparison_Results: comparison of observed and predicted SAR.\n8. Stations_RARE_Neotoma_Crosswalk: data used to match RARE project lakes with lakes from Neotoma to confirm they are the same lakes.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530540",
-            "keyword": [
-                "paleolimnology",
-                "diatoms",
-                "sediment",
-                "lake"
-            ],
             "contactPoint": {
                 "fn": "Sylvia Lee",
                 "hasEmail": "mailto:lee.sylvia@epa.gov"
             },
+            "description": "Supplementary data for the report in the format of an Excel spreadsheet (with data dictionary) and an Microsoft Access database file (downloaded as a zip file). The Access database file contains multiple data tables examined or generated during the project to investigate sediment accumulation rates (SAR) of northeast lakes.\n1. Baud_SARMAR: data downloaded from Baud et al. 2019 for northeast lake sediment accumulation rates.\n2. EPA_Extra_Chron_Data: additional lake sedimentation chronology data.\n3. Lake_Metadata_n701: coordinates, waterbody type, area, elevation, and slope information.\n4. Neotoma_Chron_Data: lake sediment core depth, age estimates, and age model info downloaded from Neotoma.\n5. RARE_Sample_Metadata: RARE project lakes' name, collection date, source.\n6. SAR_Calc_1850_n691: data for variables required by the Baud SAR equation.\n7. SAR_Comparison_Results: comparison of observed and predicted SAR.\n8. Stations_RARE_Neotoma_Crosswalk: data used to match RARE project lakes with lakes from Neotoma to confirm they are the same lakes.",
             "distribution": [
                 {
-                    "title": "NE_Sed_Chron_Data_20220930.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530540/NE_Sed_Chron_Data_20220930.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "NE_Sed_Chron_Data_20220930.zip"
                 },
                 {
-                    "title": "NE_SedimentDiatom_SAR_LakeCat_20230926 with metadata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530540/NE_SedimentDiatom_SAR_LakeCat_20230926%20with%20metadata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NE_SedimentDiatom_SAR_LakeCat_20230926 with metadata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530540",
+            "keyword": [
+                "paleolimnology",
+                "diatoms",
+                "sediment",
+                "lake"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-26",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -196190,66 +196186,64 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Estimate of sediment accumulation rates and bottom core ages in northeast lakes"
         },
         {
-            "title": "Screening for drinking water contaminants of concern using an automated exposure-focused workflow",
-            "description": "Supplementary information and tables for \"Isaacs, K.K., Wall, J.T., Paul Friedman, K. et al. Screening for drinking water contaminants of concern using an automated exposure-focused workflow. J Expo Sci Environ Epidemiol (2023). https://doi.org/10.1038/s41370-023-00552-y\". \n\nThis dataset is associated with the following publication:\nIsaacs, K., T. Wall, K. Paul-Friedman, J. Franzosa, H. Goeden, A. Williams, K. Dionisio, J. Lambert, M. Linnenbrink, A. Singh, J. Wambaugh, A. Bogdan, and C. Greene. Screening for drinking water contaminants of concern using an automated exposure-focused workflow.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 34: 136-147, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529142",
-            "keyword": [
-                "new approach methodologies",
-                "environmental monitoring",
-                "Emerging Contaminants",
-                "Exposure modeling"
-            ],
             "contactPoint": {
                 "fn": "Kristin Isaacs",
                 "hasEmail": "mailto:isaacs.kristin@epa.gov"
             },
+            "description": "Supplementary information and tables for \"Isaacs, K.K., Wall, J.T., Paul Friedman, K. et al. Screening for drinking water contaminants of concern using an automated exposure-focused workflow. J Expo Sci Environ Epidemiol (2023). https://doi.org/10.1038/s41370-023-00552-y\". \n\nThis dataset is associated with the following publication:\nIsaacs, K., T. Wall, K. Paul-Friedman, J. Franzosa, H. Goeden, A. Williams, K. Dionisio, J. Lambert, M. Linnenbrink, A. Singh, J. Wambaugh, A. Bogdan, and C. Greene. Screening for drinking water contaminants of concern using an automated exposure-focused workflow.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 34: 136-147, (2024).",
             "distribution": [
                 {
-                    "title": "41370_2023_552_MOESM2_ESM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529142/41370_2023_552_MOESM2_ESM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "41370_2023_552_MOESM2_ESM.xlsx"
                 },
                 {
-                    "title": "41370_2023_552_MOESM1_ESM.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529142/41370_2023_552_MOESM1_ESM.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "41370_2023_552_MOESM1_ESM.pdf"
                 },
                 {
-                    "title": "41370_2023_552_MOESM6_ESM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529142/41370_2023_552_MOESM6_ESM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "41370_2023_552_MOESM6_ESM.xlsx"
                 },
                 {
-                    "title": "41370_2023_552_MOESM5_ESM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529142/41370_2023_552_MOESM5_ESM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "41370_2023_552_MOESM5_ESM.xlsx"
                 },
                 {
-                    "title": "41370_2023_552_MOESM4_ESM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529142/41370_2023_552_MOESM4_ESM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "41370_2023_552_MOESM4_ESM.xlsx"
                 },
                 {
-                    "title": "41370_2023_552_MOESM3_ESM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529142/41370_2023_552_MOESM3_ESM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "41370_2023_552_MOESM3_ESM.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529142",
+            "keyword": [
+                "new approach methodologies",
+                "environmental monitoring",
+                "Emerging Contaminants",
+                "Exposure modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-17",
-            "references": [
-                "https://doi.org/10.1038/s41370-023-00552-y"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196259,42 +196253,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-023-00552-y"
+            ],
+            "rights": null,
+            "title": "Screening for drinking water contaminants of concern using an automated exposure-focused workflow"
         },
         {
-            "title": "Data and Supporting Information for \"Sublethal toxicity of 17 PFASs with diverse structures to Ceriodaphnia dubia, Hyalella azteca, and Chironomus dilutus\", manuscript submitted to Environmental Toxicology and Chemistry July 7., 2023",
-            "description": "Data and supporting information for \"Sublethal toxicity of 17 PFASs with diverse structures to Ceriodaphnia dubia, Hyalella azteca, and Chironomus dilutus\", manuscript submitted to Environmental Toxicology and Chemistry, July 7, 2023. \n\nThis dataset is associated with the following publication:\nKadlec, S., W. Backe, R. Erickson, J.R. Hockett, S. Howe, I. Mundy, E. Piasecki, H. Sluka, L. Votava, and D. Mount. Sublethal Toxicity of 17 Per- and Polyfluoroalkyl Substances with Diverse Structures to Ceriodaphnia dubia, Hyalella azteca, and Chironomus dilutus.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(2): 359-373, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529172",
-            "keyword": [
-                "PFOS",
-                "PFAS",
-                "aquatic invertebrates",
-                "PFOA",
-                "sublethal toxicity"
-            ],
             "contactPoint": {
                 "fn": "Sarah Kadlec",
                 "hasEmail": "mailto:kadlec.sarah@epa.gov"
             },
+            "description": "Data and supporting information for \"Sublethal toxicity of 17 PFASs with diverse structures to Ceriodaphnia dubia, Hyalella azteca, and Chironomus dilutus\", manuscript submitted to Environmental Toxicology and Chemistry, July 7, 2023. \n\nThis dataset is associated with the following publication:\nKadlec, S., W. Backe, R. Erickson, J.R. Hockett, S. Howe, I. Mundy, E. Piasecki, H. Sluka, L. Votava, and D. Mount. Sublethal Toxicity of 17 Per- and Polyfluoroalkyl Substances with Diverse Structures to Ceriodaphnia dubia, Hyalella azteca, and Chironomus dilutus.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(2): 359-373, (2024).",
             "distribution": [
                 {
-                    "title": "Kadlec et al. 17 PFASs 3 species_Supplemental information.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529172/Kadlec%20et%20al.%2017%20PFASs%203%20species_Supplemental%20information.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Kadlec et al. 17 PFASs 3 species_Supplemental information.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529172",
+            "keyword": [
+                "PFOS",
+                "PFAS",
+                "aquatic invertebrates",
+                "PFOA",
+                "sublethal toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-07",
-            "references": [
-                "https://doi.org/10.1002/etc.5784"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196304,47 +196298,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5784"
+            ],
+            "rights": null,
+            "title": "Data and Supporting Information for \"Sublethal toxicity of 17 PFASs with diverse structures to Ceriodaphnia dubia, Hyalella azteca, and Chironomus dilutus\", manuscript submitted to Environmental Toxicology and Chemistry July 7., 2023"
         },
         {
-            "title": "Suspect Screening Analysis of Pooled Human Serum Samples Using GC \u00d7 GC/TOF-MS",
-            "description": "Supporting information for \"Phillips KA, Chao A, Church RL, Favela K, Garantziotis S, Isaacs KK, Meyer B, Rice A, Sayre R, Wetmore BA, Yau A, Wambaugh JF. Suspect Screening Analysis of Pooled Human Serum Samples Using GC \u00d7 GC/TOF-MS. Environ Sci Technol. 2024 Jan 30;58(4):1802-1812. doi: 10.1021/acs.est.3c05092. Epub 2024 Jan 13. PMID: 38217501.\". \n\nThis dataset is associated with the following publication:\nPhillips, K., A. Chao, R. Church, K. Favela, S. Garantziotis, K. Isaacs, B. Meyer, A. Rice, R. Sayre, B. Wetmore, A. Yau, and J. Wambaugh. Suspect Screening Analysis of Pooled Human Serum Samples Using GC \u00d7 GC/TOF-MS.   ACS ES&T Engineering. American Chemical Society, Washington, DC, USA, 58(4): 1802-1812, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530115",
-            "keyword": [
-                "gas chromatography",
-                "chemical risk",
-                "exposure forensics",
-                "Suspect Screening Analysis",
-                "biomonitoring"
-            ],
             "contactPoint": {
                 "fn": "Katherine Phillips",
                 "hasEmail": "mailto:phillips.katherine@epa.gov"
             },
+            "description": "Supporting information for \"Phillips KA, Chao A, Church RL, Favela K, Garantziotis S, Isaacs KK, Meyer B, Rice A, Sayre R, Wetmore BA, Yau A, Wambaugh JF. Suspect Screening Analysis of Pooled Human Serum Samples Using GC \u00d7 GC/TOF-MS. Environ Sci Technol. 2024 Jan 30;58(4):1802-1812. doi: 10.1021/acs.est.3c05092. Epub 2024 Jan 13. PMID: 38217501.\". \n\nThis dataset is associated with the following publication:\nPhillips, K., A. Chao, R. Church, K. Favela, S. Garantziotis, K. Isaacs, B. Meyer, A. Rice, R. Sayre, B. Wetmore, A. Yau, and J. Wambaugh. Suspect Screening Analysis of Pooled Human Serum Samples Using GC \u00d7 GC/TOF-MS.   ACS ES&T Engineering. American Chemical Society, Washington, DC, USA, 58(4): 1802-1812, (2024).",
             "distribution": [
                 {
-                    "title": "es3c05092_si_002.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530115/es3c05092_si_002.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "es3c05092_si_002.pdf"
                 },
                 {
-                    "title": "pooled_serum_supplemental_tables_v2_3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530115/pooled_serum_supplemental_tables_v2_3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "pooled_serum_supplemental_tables_v2_3.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530115",
+            "keyword": [
+                "gas chromatography",
+                "chemical risk",
+                "exposure forensics",
+                "Suspect Screening Analysis",
+                "biomonitoring"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-12",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c05092"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196354,41 +196348,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c05092"
+            ],
+            "rights": null,
+            "title": "Suspect Screening Analysis of Pooled Human Serum Samples Using GC \u00d7 GC/TOF-MS"
         },
         {
-            "title": "Data associated with the figures in the GLIMPSE 1.1 Users' Guide",
-            "description": "The GLIMPSE Users' Guide includes many figures, including those that illustrate the tutorials and key results from the Reference Case scenario. This dataset includes the underlying data depicted in those figures. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530077",
-            "keyword": [
-                "mitigation",
-                "energy",
-                "Nitrogen and Co-pollutants",
-                "climate change",
-                "air quality"
-            ],
             "contactPoint": {
                 "fn": "Daniel Loughlin",
                 "hasEmail": "mailto:loughlin.dan@epa.gov"
             },
+            "description": "The GLIMPSE Users' Guide includes many figures, including those that illustrate the tutorials and key results from the Reference Case scenario. This dataset includes the underlying data depicted in those figures. ",
             "distribution": [
                 {
-                    "title": "graphics_for_GLIMPSEv1.1_UsersGuide_2024.01.03.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530077/graphics_for_GLIMPSEv1.1_UsersGuide_2024.01.03.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "graphics_for_GLIMPSEv1.1_UsersGuide_2024.01.03.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530077",
+            "keyword": [
+                "mitigation",
+                "energy",
+                "Nitrogen and Co-pollutants",
+                "climate change",
+                "air quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-18",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -196397,19 +196393,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Data associated with the figures in the GLIMPSE 1.1 Users' Guide"
         },
         {
-            "title": "Data for: Tidal Flushing Rather Than Non-Point Source Nitrogen Pollution Drives Nutrient Dynamics in A Putatively Eutrophic Estuary",
-            "description": "These are the data associated with the manuscript \"https://www.mdpi.com/2073-4441/15/1/15.\" They are available under \"Supplementary Materials\" on the left side of the webpage, under the Table of Contents. \n\nThis dataset is associated with the following publication:\nKrause, J.R., M.E. Gannon, A.J. Oczkowski, M.J. Schwartz, L.K. Champlin, D. Steinmann, M. Maxwell-Doyle, E. Pirl, V. Allen, and E.B. Watson. Tidal Flushing Rather Than Non-Point Source Nitrogen Pollution Drives Nutrient Dynamics in A Putatively Eutrophic Estuary.   WATER. MDPI, Basel,  SWITZERLAND, 15(1): 15, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Autumn Oczkowski",
+                "hasEmail": "mailto:oczkowski.autumn@epa.gov"
+            },
+            "description": "These are the data associated with the manuscript \"https://www.mdpi.com/2073-4441/15/1/15.\" They are available under \"Supplementary Materials\" on the left side of the webpage, under the Table of Contents. \n\nThis dataset is associated with the following publication:\nKrause, J.R., M.E. Gannon, A.J. Oczkowski, M.J. Schwartz, L.K. Champlin, D. Steinmann, M. Maxwell-Doyle, E. Pirl, V. Allen, and E.B. Watson. Tidal Flushing Rather Than Non-Point Source Nitrogen Pollution Drives Nutrient Dynamics in A Putatively Eutrophic Estuary.   WATER. MDPI, Basel,  SWITZERLAND, 15(1): 15, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.mdpi.com/2073-4441/15/1/15",
+                    "title": "https://www.mdpi.com/2073-4441/15/1/15"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530483",
             "keyword": [
@@ -196419,20 +196422,10 @@
                 "stable isotope",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Autumn Oczkowski",
-                "hasEmail": "mailto:oczkowski.autumn@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.mdpi.com/2073-4441/15/1/15",
-                    "accessURL": "https://www.mdpi.com/2073-4441/15/1/15"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-21",
-            "references": [
-                "https://doi.org/10.3390/w15010015",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9926401"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196442,41 +196435,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/w15010015",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9926401"
+            ],
+            "rights": null,
+            "title": "Data for: Tidal Flushing Rather Than Non-Point Source Nitrogen Pollution Drives Nutrient Dynamics in A Putatively Eutrophic Estuary"
         },
         {
-            "title": "Data for: Integrated multi-trophic aquaculture with sugar kelp and oysters in a shallow coastal salt pond and open estuary site",
-            "description": "The data set includes environmental data as well as kelp and oyster data from an integrated multi-trophic aquaculture study where sugar kelp was planted on four established oyster farms in Rhode Island, USA over 2 growing seasons (Year 1 = 2017\u20132018; Year 2 = 2018-2019). At each site, we planted 60 m kelp lines (denoted as Line 1 and Line 2) approximately three weeks apart to determine optimal planting time. Kelp blade length and width were recorded at periodic intervals, and tissues were collected for carbon, nitrogen, \u03b415N, and \u03b413C analyses. Oyster growth data was collected from the same sites across the same timespans. Environmental data includes data collected on monthly farm visits with a YSI Sonde, as well as dissolved nutrients in the seawater. In addition, temperatures were logged on kelp lines every 15 minutes during each growing season. \n\nThis dataset is associated with the following publication:\nGreen-Gavrielidis, L., C. Thornber, and A. Oczkowski. Integrated multi-trophic aquaculture with sugar kelp and oysters in a shallow coastal salt pond and open estuary site.   Frontiers in Aquaculture. Frontiers, Lausanne,  SWITZERLAND, 2: 1147524, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530481",
-            "keyword": [
-                "nitrogen",
-                "Oyster",
-                "kelp",
-                "aquaculture"
-            ],
             "contactPoint": {
                 "fn": "Autumn Oczkowski",
                 "hasEmail": "mailto:oczkowski.autumn@epa.gov"
             },
+            "description": "The data set includes environmental data as well as kelp and oyster data from an integrated multi-trophic aquaculture study where sugar kelp was planted on four established oyster farms in Rhode Island, USA over 2 growing seasons (Year 1 = 2017\u20132018; Year 2 = 2018-2019). At each site, we planted 60 m kelp lines (denoted as Line 1 and Line 2) approximately three weeks apart to determine optimal planting time. Kelp blade length and width were recorded at periodic intervals, and tissues were collected for carbon, nitrogen, \u03b415N, and \u03b413C analyses. Oyster growth data was collected from the same sites across the same timespans. Environmental data includes data collected on monthly farm visits with a YSI Sonde, as well as dissolved nutrients in the seawater. In addition, temperatures were logged on kelp lines every 15 minutes during each growing season. \n\nThis dataset is associated with the following publication:\nGreen-Gavrielidis, L., C. Thornber, and A. Oczkowski. Integrated multi-trophic aquaculture with sugar kelp and oysters in a shallow coastal salt pond and open estuary site.   Frontiers in Aquaculture. Frontiers, Lausanne,  SWITZERLAND, 2: 1147524, (2023).",
             "distribution": [
                 {
-                    "title": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.hqbzkh1m3",
-                    "accessURL": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.hqbzkh1m3"
+                    "accessURL": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.hqbzkh1m3",
+                    "title": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.hqbzkh1m3"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530481",
+            "keyword": [
+                "nitrogen",
+                "Oyster",
+                "kelp",
+                "aquaculture"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-26",
-            "references": [
-                "https://doi.org/10.3389/faquc.2023.1147524",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10581391"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196486,20 +196479,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/faquc.2023.1147524",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10581391"
+            ],
+            "rights": null,
+            "title": "Data for: Integrated multi-trophic aquaculture with sugar kelp and oysters in a shallow coastal salt pond and open estuary site"
         },
         {
-            "title": "Society for Women in Marine Science survey data",
-            "description": "This project looks specifically at gender diversity within marine sciences, and the experiences of women and gender-diverse people in the field. Based on survey data collected from participants in symposia hosted by the Society for Women in Marine Science, we identify shared challenges, training opportunities, and logistic improvements to create more inclusive symposia in the future. Intersectional considerations of the multiple identities researchers possess are an important focus for diversifying marine science and fostering belonging. This dataset is not publicly accessible because: Data are owned by the Society for Women in Marine Science. It can be accessed through the following means: Data will be made available on request. Format: Survey data conducted by the Society for Women in Marine Science as part of their annual symposium 2018-2020. \n\nThis dataset is associated with the following publication:\nCanfield, K., A. Sterling, C. Hernandez, S. Chu, B. Edwards, D. Fontaine, J. Freese, M. Giroux, A. Jones, A. McCarty, H. Morrissette, H. Palevsky, C. Raker, A. Robuck, G. Serrato Marks, P. Thibodeau, and A. Windle. Building an inclusive wave in marine science: Sense of belonging and Society for Women in Marine Science symposia.   Progress in Oceanography. Elsevier B.V., Amsterdam,  NETHERLANDS, 218: 103110, (2023).",
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
+                "fn": "Katherine Canfield",
+                "hasEmail": "mailto:canfield.katherine@epa.gov"
+            },
+            "description": "This project looks specifically at gender diversity within marine sciences, and the experiences of women and gender-diverse people in the field. Based on survey data collected from participants in symposia hosted by the Society for Women in Marine Science, we identify shared challenges, training opportunities, and logistic improvements to create more inclusive symposia in the future. Intersectional considerations of the multiple identities researchers possess are an important focus for diversifying marine science and fostering belonging. This dataset is not publicly accessible because: Data are owned by the Society for Women in Marine Science. It can be accessed through the following means: Data will be made available on request. Format: Survey data conducted by the Society for Women in Marine Science as part of their annual symposium 2018-2020. \n\nThis dataset is associated with the following publication:\nCanfield, K., A. Sterling, C. Hernandez, S. Chu, B. Edwards, D. Fontaine, J. Freese, M. Giroux, A. Jones, A. McCarty, H. Morrissette, H. Palevsky, C. Raker, A. Robuck, G. Serrato Marks, P. Thibodeau, and A. Windle. Building an inclusive wave in marine science: Sense of belonging and Society for Women in Marine Science symposia.   Progress in Oceanography. Elsevier B.V., Amsterdam,  NETHERLANDS, 218: 103110, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530486",
             "keyword": [
                 "social science",
@@ -196507,15 +196505,10 @@
                 "women in science",
                 "marine science"
             ],
-            "contactPoint": {
-                "fn": "Katherine Canfield",
-                "hasEmail": "mailto:canfield.katherine@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-28",
-            "references": [
-                "https://doi.org/10.1016/j.pocean.2023.103110",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10805246"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196525,20 +196518,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
             },
-        {
-            "title": "Non-EPA data for \"Runnels mitigate marsh drowning in microtidal salt marshes\"",
-            "description": "We report on 5 years of vegetation and hydrologic monitoring of two locations where a total of 600-m of shallow (0.15\u20130.30-m in diameter and depth) runnels were installed in 2015 and 2016 to enhance drainage, in the Pettaquamscutt River Estuary, in southern Rhode Island, United States. Results from this Before-After Control-Impact (BACI) designed study found that runnel installation successfully promoted plant recolonization, although runnels did not consistently promote increases in high marsh species presence or diversity. This dataset is not publicly accessible because: EPA is not the owner of this data. It can be accessed through the following means: All data is available as Supplementary Material in journal article. Inquiries can be directed to the corresponding author. Format: All data is available as Supplementary Material in journal article. Inquiries can be directed to the corresponding author. \n\nThis dataset is associated with the following publication:\nWatson, E., W. Ferguson, L. Champlin, J. White, N. Ernst, H. Sylla, B. Wilburn, and C. Wigand. Runnels mitigate marsh drowning in microtidal salt marshes.   Frontiers in Environmental Science. Frontiers, Lausanne,  SWITZERLAND, 10: 987246, (2022).",
-            "accessLevel": "public",
+            "references": [
+                "https://doi.org/10.1016/j.pocean.2023.103110",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10805246"
+            ],
             "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
+            "title": "Society for Women in Marine Science survey data"
+        },
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Cathleen Wigand",
+                "hasEmail": "mailto:wigand.cathleen@epa.gov"
+            },
+            "description": "We report on 5 years of vegetation and hydrologic monitoring of two locations where a total of 600-m of shallow (0.15\u20130.30-m in diameter and depth) runnels were installed in 2015 and 2016 to enhance drainage, in the Pettaquamscutt River Estuary, in southern Rhode Island, United States. Results from this Before-After Control-Impact (BACI) designed study found that runnel installation successfully promoted plant recolonization, although runnels did not consistently promote increases in high marsh species presence or diversity. This dataset is not publicly accessible because: EPA is not the owner of this data. It can be accessed through the following means: All data is available as Supplementary Material in journal article. Inquiries can be directed to the corresponding author. Format: All data is available as Supplementary Material in journal article. Inquiries can be directed to the corresponding author. \n\nThis dataset is associated with the following publication:\nWatson, E., W. Ferguson, L. Champlin, J. White, N. Ernst, H. Sylla, B. Wilburn, and C. Wigand. Runnels mitigate marsh drowning in microtidal salt marshes.   Frontiers in Environmental Science. Frontiers, Lausanne,  SWITZERLAND, 10: 987246, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530415",
             "keyword": [
                 "restoration",
@@ -196547,15 +196545,10 @@
                 "Salt marsh",
                 "climate change"
             ],
-            "contactPoint": {
-                "fn": "Cathleen Wigand",
-                "hasEmail": "mailto:wigand.cathleen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-10-12",
-            "references": [
-                "https://doi.org/10.3389/fenvs.2022.987246",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9728634"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196565,20 +196558,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fenvs.2022.987246",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9728634"
+            ],
+            "rights": null,
+            "title": "Non-EPA data for \"Runnels mitigate marsh drowning in microtidal salt marshes\""
         },
         {
-            "title": "Birnessite films are sensitive indicators of microbial manganese reduction in soil",
-            "description": "Development of rapid and inexpensive assessment tools to evaluate the integrity of wetlands soils is important to managers and natural resource stewards. In this study researchers developed an effective, rapid, and low cost tool to assess the degree of oxygenation in wetland soils. Strips of white plastic were painted with the brown-colored birnessite, which indicates low oxidizing conditions in the soil when the brown color disappears from the strip. Use of these strips may assist in monitoring wetlands and prioritizing wetland areas for restoration efforts. This dataset is not publicly accessible because: EPA does not own the data. It can be accessed through the following means: Contact article's corresponding author. Format: Supplemental Figure S1. Curated spreadsheet containing raw and processed data from Mn indicator of reduction in soils (IRIS) film paint removal quantification and sand weighing data.\r\nSupplemental Figure S2. Two-way ANOVA analyses of Mn indicator of reduction in soils (IRIS) film paint removal data. \n\nThis dataset is associated with the following publication:\nHino, K.C., J. Romero, J.L. Loffredo, M. Stolt, J. Amador, S. Moseman-Valtierra, C. Wigand, and B. Pellock. Birnessite films are sensitive indicators of microbial manganese reduction in soil.   SOIL SCIENCE SOCIETY OF AMERICA JOURNAL. Soil Science Society of America, Madison, WI, USA, 87(1): 196-201, (2023).",
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
+                "fn": "Cathleen Wigand",
+                "hasEmail": "mailto:wigand.cathleen@epa.gov"
+            },
+            "description": "Development of rapid and inexpensive assessment tools to evaluate the integrity of wetlands soils is important to managers and natural resource stewards. In this study researchers developed an effective, rapid, and low cost tool to assess the degree of oxygenation in wetland soils. Strips of white plastic were painted with the brown-colored birnessite, which indicates low oxidizing conditions in the soil when the brown color disappears from the strip. Use of these strips may assist in monitoring wetlands and prioritizing wetland areas for restoration efforts. This dataset is not publicly accessible because: EPA does not own the data. It can be accessed through the following means: Contact article's corresponding author. Format: Supplemental Figure S1. Curated spreadsheet containing raw and processed data from Mn indicator of reduction in soils (IRIS) film paint removal quantification and sand weighing data.\r\nSupplemental Figure S2. Two-way ANOVA analyses of Mn indicator of reduction in soils (IRIS) film paint removal data. \n\nThis dataset is associated with the following publication:\nHino, K.C., J. Romero, J.L. Loffredo, M. Stolt, J. Amador, S. Moseman-Valtierra, C. Wigand, and B. Pellock. Birnessite films are sensitive indicators of microbial manganese reduction in soil.   SOIL SCIENCE SOCIETY OF AMERICA JOURNAL. Soil Science Society of America, Madison, WI, USA, 87(1): 196-201, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530475",
             "keyword": [
                 "bioremediation",
@@ -196586,15 +196584,10 @@
                 "wetland soil",
                 "wetland"
             ],
-            "contactPoint": {
-                "fn": "Cathleen Wigand",
-                "hasEmail": "mailto:wigand.cathleen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-07-20",
-            "references": [
-                "https://doi.org/10.1002/saj2.20468",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10116846"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196604,20 +196597,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/saj2.20468",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10116846"
+            ],
+            "rights": null,
+            "title": "Birnessite films are sensitive indicators of microbial manganese reduction in soil"
         },
         {
-            "title": "SDR StRAP 3 interviews",
-            "description": "Interview data from EPA researchers and partners involved with solutions-driven research pilots on nutrient management and wildland fire smoke. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Restricted access may be granted to authorized persons by contacting the party listed. Format: Confidential interview data contains identifiable information of interviewees, including identifiable experiences at or with EPA, position with EPA, and role within the projects studied. \n\nThis dataset is associated with the following publication:\nCanfield, K.N., B. Hubbell, L. Rivers, B. Rodan, B. Hassett-Sipple, A. Rea, T. Gleason, A. Holder, C. Berg, C.D. Chatelain, S. Coefield, B. Schmidt, and B. McCaughey. Lessons learned and recommendations in conducting solutions-driven environmental and public health research.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 354(March 2024): 120270, (2024).",
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
+                "fn": "Katherine Canfield",
+                "hasEmail": "mailto:canfield.katherine@epa.gov"
+            },
+            "description": "Interview data from EPA researchers and partners involved with solutions-driven research pilots on nutrient management and wildland fire smoke. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Restricted access may be granted to authorized persons by contacting the party listed. Format: Confidential interview data contains identifiable information of interviewees, including identifiable experiences at or with EPA, position with EPA, and role within the projects studied. \n\nThis dataset is associated with the following publication:\nCanfield, K.N., B. Hubbell, L. Rivers, B. Rodan, B. Hassett-Sipple, A. Rea, T. Gleason, A. Holder, C. Berg, C.D. Chatelain, S. Coefield, B. Schmidt, and B. McCaughey. Lessons learned and recommendations in conducting solutions-driven environmental and public health research.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 354(March 2024): 120270, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530588",
             "keyword": [
                 "Wildland Fire",
@@ -196628,15 +196626,10 @@
                 "Solutions based research",
                 "solutions-driven research"
             ],
-            "contactPoint": {
-                "fn": "Katherine Canfield",
-                "hasEmail": "mailto:canfield.katherine@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-07",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2024.120270",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10939729"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196646,45 +196639,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2024.120270",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10939729"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "SDR StRAP 3 interviews"
         },
         {
-            "title": "Data Links for Monitoring Chemical Contaminants in the Gulf of Maine, using Sediments and Mussels: an evaluation ",
-            "description": "The monitoring programs used to determine if sediments and mussels can be used interchangeably to assess environmental condition were: Mussel Watch (MW, National Status and Trends (NS&T), NOAA), Gulfwatch (GW, Gulf of Maine Council), National Coastal Assessment (NCA, US EPA), National Coastal Condition Assessment (NCCA, US EPA), and newly available sediment data from the EcoSystem Indicator Partnership (ESIP). Mussel Watch, Gulfwatch, NCA and NCCA are high profile, long-term, well organized national and regional mussel and/ or sediment monitoring programs. Sediment contaminant data generated by Eastern Charlotte Waterways (ECW) Inc, from funding by the Gulf of Maine Council on the Marine Environment\u2019s EcoSystem Indicator Partnership, were used for sites in the Canadian portion of the GOM; sediments were collected by ECW and analyzed by RPC (http://www.rpc.ca/english/index.html). All the data source programs have quality assurance measures (details can be found at the URLs listed below).\n\nNOAA\u2019s NS&T Mussel Watch (NOAA MW)\nhttps://en.wikipedia.org/wiki/Mussel_Watch_Program\nhttps://products.coastalscience.noaa.gov/nsandt_data/data.aspx\n\nGulf of Maine Council\u2019s Gulfwatch (GOMC GW) \nhttp://www.gulfofmaine.org/2/gulfwatch-homepage/\nhttps://gulfofmaine.org/public/gulfwatch-contaminants-monitoring/data-reports/ \nThe Canadian portion of Gulfwatch also has published QA documentation (Sowles et al., 1997).\n\nEPA\u2019s National Coastal Assessment (EPA NCA) & National Coastal Condition Assessment (NCCA)\nhttps://archive.epa.gov/emap/archive-emap/web/html/about.html\nhttps://www.epa.gov/national-aquatic-resource-surveys/ncca\nhttps://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-\nsurveys\n\nEcoSystem Indictor Partnership (ESiP)\nhttp://www.gulfofmaine.org/2/esip-homepage/ \nEastern Charlotte Waterways Inc. (D. Killorn, pers comm). Sediments were collected by ECW and analyzed through a subcontract to RPC. Data with accompanying QA data were obtained from Donald Killorn, ECW (pers comm). \n\nThis dataset is associated with the following publication:\nElskus, A., L. LeBlanc, J. Latimer, D. Page, G. Harding, and P. Wells. Monitoring chemical contaminants in the Gulf of Maine, using sediments and mussels (Mytilus edulis): An evaluation.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 153: 110956, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530585",
-            "keyword": [
-                "contaminants",
-                "gulf of maine",
-                "estuary",
-                "monitoring"
-            ],
             "contactPoint": {
                 "fn": "James Latimer",
                 "hasEmail": "mailto:latimer.jim@epa.gov"
             },
+            "description": "The monitoring programs used to determine if sediments and mussels can be used interchangeably to assess environmental condition were: Mussel Watch (MW, National Status and Trends (NS&T), NOAA), Gulfwatch (GW, Gulf of Maine Council), National Coastal Assessment (NCA, US EPA), National Coastal Condition Assessment (NCCA, US EPA), and newly available sediment data from the EcoSystem Indicator Partnership (ESIP). Mussel Watch, Gulfwatch, NCA and NCCA are high profile, long-term, well organized national and regional mussel and/ or sediment monitoring programs. Sediment contaminant data generated by Eastern Charlotte Waterways (ECW) Inc, from funding by the Gulf of Maine Council on the Marine Environment\u2019s EcoSystem Indicator Partnership, were used for sites in the Canadian portion of the GOM; sediments were collected by ECW and analyzed by RPC (http://www.rpc.ca/english/index.html). All the data source programs have quality assurance measures (details can be found at the URLs listed below).\n\nNOAA\u2019s NS&T Mussel Watch (NOAA MW)\nhttps://en.wikipedia.org/wiki/Mussel_Watch_Program\nhttps://products.coastalscience.noaa.gov/nsandt_data/data.aspx\n\nGulf of Maine Council\u2019s Gulfwatch (GOMC GW) \nhttp://www.gulfofmaine.org/2/gulfwatch-homepage/\nhttps://gulfofmaine.org/public/gulfwatch-contaminants-monitoring/data-reports/ \nThe Canadian portion of Gulfwatch also has published QA documentation (Sowles et al., 1997).\n\nEPA\u2019s National Coastal Assessment (EPA NCA) & National Coastal Condition Assessment (NCCA)\nhttps://archive.epa.gov/emap/archive-emap/web/html/about.html\nhttps://www.epa.gov/national-aquatic-resource-surveys/ncca\nhttps://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-\nsurveys\n\nEcoSystem Indictor Partnership (ESiP)\nhttp://www.gulfofmaine.org/2/esip-homepage/ \nEastern Charlotte Waterways Inc. (D. Killorn, pers comm). Sediments were collected by ECW and analyzed through a subcontract to RPC. Data with accompanying QA data were obtained from Donald Killorn, ECW (pers comm). \n\nThis dataset is associated with the following publication:\nElskus, A., L. LeBlanc, J. Latimer, D. Page, G. Harding, and P. Wells. Monitoring chemical contaminants in the Gulf of Maine, using sediments and mussels (Mytilus edulis): An evaluation.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 153: 110956, (2020).",
             "distribution": [
                 {
-                    "title": "https://products.coastalscience.noaa.gov/nsandt_data/data.aspx",
-                    "accessURL": "https://products.coastalscience.noaa.gov/nsandt_data/data.aspx"
+                    "accessURL": "https://products.coastalscience.noaa.gov/nsandt_data/data.aspx",
+                    "title": "https://products.coastalscience.noaa.gov/nsandt_data/data.aspx"
                 },
                 {
-                    "title": "https://gulfofmaine.org/public/gulfwatch-contaminants-monitoring/data-reports/",
-                    "accessURL": "https://gulfofmaine.org/public/gulfwatch-contaminants-monitoring/data-reports/"
+                    "accessURL": "https://gulfofmaine.org/public/gulfwatch-contaminants-monitoring/data-reports/",
+                    "title": "https://gulfofmaine.org/public/gulfwatch-contaminants-monitoring/data-reports/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530585",
+            "keyword": [
+                "contaminants",
+                "gulf of maine",
+                "estuary",
+                "monitoring"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2019-10-04",
-            "references": [
-                "https://doi.org/10.1016/j.marpolbul.2020.110956",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10775826"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196694,39 +196687,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.marpolbul.2020.110956",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10775826"
+            ],
+            "rights": null,
+            "title": "Data Links for Monitoring Chemical Contaminants in the Gulf of Maine, using Sediments and Mussels: an evaluation "
         },
         {
-            "title": "Supporting modeling components",
-            "description": "This journal paper summarizes a Bayesian Network modeling approach for integrating climate change factors into ecological risk assessment. The BN modeling was not EPA generated. It was rather developed as a part of a special series generated under a SETAC Pellston Workgroup that was charged with developing strategies and approaches for considering climate change in ecological and chemical risk assessment.  Supporting BN modeling inputs and components are included as supplemental information with the published manuscript. EPA scientists (John Carriger, Pamela Noyes) participated on the Pellston workgroup. Pamela Noyes was a coauthor and John Carriger reviewed and provided technical guidance on the paper and modeling. \n\nThis dataset is associated with the following publication:\nMentzel, S., R. Nathan, P. Noyes, K.V. Brix, S.J. Moe, J.R. Rohr, J. Verheyen, P.J. Van den Brink, and J. Stauber. Evaluating the effects of climate change and chemical, physical, and biological stressors on nearshore coral reefs: A case study in the Great Barrier Reef, Australia.   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 20(2): 401-418, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530601",
-            "keyword": [
-                "climate change",
-                "cumulative risk assessment",
-                "ecological risk assessment"
-            ],
             "contactPoint": {
                 "fn": "Pamela Noyes",
                 "hasEmail": "mailto:noyes.pamela@epa.gov"
             },
+            "description": "This journal paper summarizes a Bayesian Network modeling approach for integrating climate change factors into ecological risk assessment. The BN modeling was not EPA generated. It was rather developed as a part of a special series generated under a SETAC Pellston Workgroup that was charged with developing strategies and approaches for considering climate change in ecological and chemical risk assessment.  Supporting BN modeling inputs and components are included as supplemental information with the published manuscript. EPA scientists (John Carriger, Pamela Noyes) participated on the Pellston workgroup. Pamela Noyes was a coauthor and John Carriger reviewed and provided technical guidance on the paper and modeling. \n\nThis dataset is associated with the following publication:\nMentzel, S., R. Nathan, P. Noyes, K.V. Brix, S.J. Moe, J.R. Rohr, J. Verheyen, P.J. Van den Brink, and J. Stauber. Evaluating the effects of climate change and chemical, physical, and biological stressors on nearshore coral reefs: A case study in the Great Barrier Reef, Australia.   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 20(2): 401-418, (2024).",
             "distribution": [
                 {
-                    "title": "https://setac.onlinelibrary.wiley.com/doi/full/10.1002/ieam.4871",
-                    "accessURL": "https://setac.onlinelibrary.wiley.com/doi/full/10.1002/ieam.4871"
+                    "accessURL": "https://setac.onlinelibrary.wiley.com/doi/full/10.1002/ieam.4871",
+                    "title": "https://setac.onlinelibrary.wiley.com/doi/full/10.1002/ieam.4871"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530601",
+            "keyword": [
+                "climate change",
+                "cumulative risk assessment",
+                "ecological risk assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-09-15",
-            "references": [
-                "https://doi.org/10.1002/ieam.4871"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196736,20 +196730,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/ieam.4871"
+            ],
+            "rights": null,
+            "title": "Supporting modeling components"
         },
         {
-            "title": "CARES_COPD_casecrossover",
-            "description": "Information on hospitalizations of COPD patients from electronic health records linked to air pollution concentrations for the study period. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Can be requested through NCTracts https://tracs.unc.edu/index.php/services/comparative-effectiveness-research/data-linkage. Format: Data used in this analysis include electronic health records from the UNC healthcare system. \n\nThis dataset is associated with the following publication:\nCowan, K., L. Wyatt, T. Luben, J. Sacks, C. Ward-Caviness, and K. Rappazzo. Effect measure modification of the association between short-term exposures to PM2.5 and hospitalizations by longs-term PM2.5 exposure among a cohort of people with Chronic Obstructive Pulmonary Disease (COPD) in North Carolina, 2002\u20132015.   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 22: 49, (2023).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Kristen Rappazzo",
+                "hasEmail": "mailto:rappazzo.kristen@epa.gov"
+            },
+            "description": "Information on hospitalizations of COPD patients from electronic health records linked to air pollution concentrations for the study period. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Can be requested through NCTracts https://tracs.unc.edu/index.php/services/comparative-effectiveness-research/data-linkage. Format: Data used in this analysis include electronic health records from the UNC healthcare system. \n\nThis dataset is associated with the following publication:\nCowan, K., L. Wyatt, T. Luben, J. Sacks, C. Ward-Caviness, and K. Rappazzo. Effect measure modification of the association between short-term exposures to PM2.5 and hospitalizations by longs-term PM2.5 exposure among a cohort of people with Chronic Obstructive Pulmonary Disease (COPD) in North Carolina, 2002\u20132015.   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 22: 49, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530582",
             "keyword": [
                 "hospitalization",
@@ -196758,15 +196756,10 @@
                 "particulate matter (PM)",
                 "long and short term interaction"
             ],
-            "contactPoint": {
-                "fn": "Kristen Rappazzo",
-                "hasEmail": "mailto:rappazzo.kristen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2024-01-19",
-            "references": [
-                "https://doi.org/10.1186/s12940-023-00999-4",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10308617"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196776,20 +196769,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12940-023-00999-4",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10308617"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "CARES_COPD_casecrossover"
         },
         {
-            "title": "Sisk.food.desert.networks",
-            "description": "Networks of public transit and food deserts. This dataset is not publicly accessible because: Data was never accessed by EPA authors. It can be accessed through the following means: Data is available on request from lead author, Dr. Anna Sisk at asisk9@alum.utk.edu. Format: spatial datasets. \n\nThis dataset is associated with the following publication:\nSisk, A., K. Rappazzo, T. Luben, and N. Fefferman. Connecting people to food: A network approach to alleviating food deserts.   Journal of Transport & Health. Elsevier B.V., Amsterdam,  NETHERLANDS, 31: 101627, (2023).",
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
+                "fn": "Kristen Rappazzo",
+                "hasEmail": "mailto:rappazzo.kristen@epa.gov"
+            },
+            "description": "Networks of public transit and food deserts. This dataset is not publicly accessible because: Data was never accessed by EPA authors. It can be accessed through the following means: Data is available on request from lead author, Dr. Anna Sisk at asisk9@alum.utk.edu. Format: spatial datasets. \n\nThis dataset is associated with the following publication:\nSisk, A., K. Rappazzo, T. Luben, and N. Fefferman. Connecting people to food: A network approach to alleviating food deserts.   Journal of Transport & Health. Elsevier B.V., Amsterdam,  NETHERLANDS, 31: 101627, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530586",
             "keyword": [
                 "transportation",
@@ -196799,14 +196797,10 @@
                 "geospatial analysis",
                 "Environmental Justice"
             ],
-            "contactPoint": {
-                "fn": "Kristen Rappazzo",
-                "hasEmail": "mailto:rappazzo.kristen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-10",
-            "references": [
-                "https://doi.org/10.1016/j.jth.2023.101627"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196816,41 +196810,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jth.2023.101627"
+            ],
+            "rights": null,
+            "title": "Sisk.food.desert.networks"
         },
         {
-            "title": "MMWR Metadata",
-            "description": "Metadata for MMWR on Canadian Wildfire Smoke episodes and asthma ED visits. Portions of this dataset are inaccessible because: Jurisdictions own data with protections under their laws and regulations. NSSP (CDC) has access to data through data-use agreements that allow for reporting at the HHS regional aggregate level. They can be accessed through the following means: For the non-public data, all end users with access are credentialled and must gain access through PIV following CDC approved protocols. All team members with access are CDC employees. For the public data that is associated with the MMWR publication, results will be presented in a visual format showing graphs of ED visit counts and air quality levels in the publication. \r\n\r\nPublicly available Aggregated data will be available in CDCStacks library system. For non-public data. Format: Data will  be presented in aggregate form during dissemination phase through a publicly accessible MMWR. \n\nThis dataset is associated with the following publication:\nMcArdle, C., T. Dowling, K. Carey, J. DeVies, D. Johns, A. Gates, Z. Stein, K. van Santen, L. Radhakrishnan, A. Kite-Powell, K. Soetebier, J. Sacks, K. Sircar, K. Hartnett, and M. Mirabelli. Asthma-Associated Emergency Department Visits During the Canadian Wildfire Smoke Episodes \u2014 United States, April\u2013August 2023.   MORBIDITY AND MORTALITY WEEKLY REPORT. U.S. Department of Health and Human Services, Washington, DC, USA, 72: 926-932, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529455",
-            "keyword": [
-                "public health",
-                "Wildfire smoke",
-                "asthma",
-                "air quality"
-            ],
             "contactPoint": {
                 "fn": "Jason Sacks",
                 "hasEmail": "mailto:sacks.jason@epa.gov"
             },
+            "description": "Metadata for MMWR on Canadian Wildfire Smoke episodes and asthma ED visits. Portions of this dataset are inaccessible because: Jurisdictions own data with protections under their laws and regulations. NSSP (CDC) has access to data through data-use agreements that allow for reporting at the HHS regional aggregate level. They can be accessed through the following means: For the non-public data, all end users with access are credentialled and must gain access through PIV following CDC approved protocols. All team members with access are CDC employees. For the public data that is associated with the MMWR publication, results will be presented in a visual format showing graphs of ED visit counts and air quality levels in the publication. \r\n\r\nPublicly available Aggregated data will be available in CDCStacks library system. For non-public data. Format: Data will  be presented in aggregate form during dissemination phase through a publicly accessible MMWR. \n\nThis dataset is associated with the following publication:\nMcArdle, C., T. Dowling, K. Carey, J. DeVies, D. Johns, A. Gates, Z. Stein, K. van Santen, L. Radhakrishnan, A. Kite-Powell, K. Soetebier, J. Sacks, K. Sircar, K. Hartnett, and M. Mirabelli. Asthma-Associated Emergency Department Visits During the Canadian Wildfire Smoke Episodes \u2014 United States, April\u2013August 2023.   MORBIDITY AND MORTALITY WEEKLY REPORT. U.S. Department of Health and Human Services, Washington, DC, USA, 72: 926-932, (2023).",
             "distribution": [
                 {
-                    "title": "https://stacks.cdc.gov/view/cdc/132183",
-                    "accessURL": "https://stacks.cdc.gov/view/cdc/132183"
+                    "accessURL": "https://stacks.cdc.gov/view/cdc/132183",
+                    "title": "https://stacks.cdc.gov/view/cdc/132183"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529455",
+            "keyword": [
+                "public health",
+                "Wildfire smoke",
+                "asthma",
+                "air quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-22",
-            "references": [
-                "https://doi.org/10.15585/mmwr.mm7234a5",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10468220"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196860,20 +196853,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.15585/mmwr.mm7234a5",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10468220"
+            ],
+            "rights": null,
+            "title": "MMWR Metadata"
         },
         {
-            "title": "KFTI data",
-            "description": "This study quantifying the sensitivity and tolerance of fish species to stressor gradients in the Karun River basin (Western Iran) and to used this information to develop a fish-based tolerance index, the Karun Fish Tolerance Index (KFTI), that can serve as a practical management tool. We also tested if native, endemic, and nonnative fish species differ in tolerance to the range of stressors that occur in the Karun River system. The KFTI complements a multimetric index (KFMMI) based on the same data developed in a companion study. The two complementary fish-based indices developed based on this dataset, that is, KFTI (this study) and KFMMI (Zare Shahraki et al., 2022b) are now available for use by stakeholders, managers, and scientists to evaluate the quality of freshwater ecosystems in Iran and elsewhere. This dataset is not publicly accessible because: Data is the property of Swiss Leading House South Asia and Iran (ZHAW) and Isfahan University of Technology. It can be accessed through the following means: The data that support the findings of this study are available from the corresponding author (Andreas Bruder) upon reasonable request. Format: Physical habitat, landscape data, and water chemistry. \n\nThis dataset is associated with the following publication:\nZare Shahraki, M., P. Fathi, E. Ebrahimi Dorche, J. Flotemersch, K. Blocksom, J. Stribling, and A. Bruder. Environmental impact assessment and conservation planning of a Middle-Eastern River basin using a fish-based tolerance index.   River Research and Applications. John Wiley & Sons Incorporated, New York, NY, USA, 40(3): 411-424, (2024).",
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
+                "fn": "Joseph Flotemersch",
+                "hasEmail": "mailto:flotemersch.joseph@epa.gov"
+            },
+            "description": "This study quantifying the sensitivity and tolerance of fish species to stressor gradients in the Karun River basin (Western Iran) and to used this information to develop a fish-based tolerance index, the Karun Fish Tolerance Index (KFTI), that can serve as a practical management tool. We also tested if native, endemic, and nonnative fish species differ in tolerance to the range of stressors that occur in the Karun River system. The KFTI complements a multimetric index (KFMMI) based on the same data developed in a companion study. The two complementary fish-based indices developed based on this dataset, that is, KFTI (this study) and KFMMI (Zare Shahraki et al., 2022b) are now available for use by stakeholders, managers, and scientists to evaluate the quality of freshwater ecosystems in Iran and elsewhere. This dataset is not publicly accessible because: Data is the property of Swiss Leading House South Asia and Iran (ZHAW) and Isfahan University of Technology. It can be accessed through the following means: The data that support the findings of this study are available from the corresponding author (Andreas Bruder) upon reasonable request. Format: Physical habitat, landscape data, and water chemistry. \n\nThis dataset is associated with the following publication:\nZare Shahraki, M., P. Fathi, E. Ebrahimi Dorche, J. Flotemersch, K. Blocksom, J. Stribling, and A. Bruder. Environmental impact assessment and conservation planning of a Middle-Eastern River basin using a fish-based tolerance index.   River Research and Applications. John Wiley & Sons Incorporated, New York, NY, USA, 40(3): 411-424, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530325",
             "keyword": [
                 "biodiversity",
@@ -196881,14 +196879,10 @@
                 "ecosystem management",
                 "stressor sensitivity"
             ],
-            "contactPoint": {
-                "fn": "Joseph Flotemersch",
-                "hasEmail": "mailto:flotemersch.joseph@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-20",
-            "references": [
-                "https://doi.org/10.1002/rra.4233"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196898,40 +196892,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/rra.4233"
+            ],
+            "rights": null,
+            "title": "KFTI data"
         },
         {
-            "title": "PFAS Occurrence Systematic Evidence Mapping Data Extraction September 7 2022",
-            "description": "Database file containing the data extractions for the first batch of eight PFAS (XLSX)\nDatabase file containing the data extractions for the second batch of 12 PFAS (XLSX)\nLiterature search strategy, filters used in SWIFT-Review, specific information fields extracted from each study that underwent full-text screening and data extraction, information on incidental extractions, and descriptions on information extracted from biomonitoring/cohort papers (PDF). \n\nThis dataset is associated with the following publication:\nHolder, C., N. DeLuca, J. Luh, P. Alexander, J. Minucci, D. Vallero, K. Thomas, and E. Cohen-Hubal. Systematic Evidence Mapping of Potential Exposure Pathways for Per- and Polyfluoroalkyl Substances Based on Measured Occurrence in Multiple Media.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(13): 5107-5116, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530691",
-            "keyword": [
-                "Exposure pathways",
-                "PFAS",
-                "systematic evi",
-                "exposure data curation"
-            ],
             "contactPoint": {
                 "fn": "Elaine Cohen-Hubal",
                 "hasEmail": "mailto:hubal.elaine@epa.gov"
             },
+            "description": "Database file containing the data extractions for the first batch of eight PFAS (XLSX)\nDatabase file containing the data extractions for the second batch of 12 PFAS (XLSX)\nLiterature search strategy, filters used in SWIFT-Review, specific information fields extracted from each study that underwent full-text screening and data extraction, information on incidental extractions, and descriptions on information extracted from biomonitoring/cohort papers (PDF). \n\nThis dataset is associated with the following publication:\nHolder, C., N. DeLuca, J. Luh, P. Alexander, J. Minucci, D. Vallero, K. Thomas, and E. Cohen-Hubal. Systematic Evidence Mapping of Potential Exposure Pathways for Per- and Polyfluoroalkyl Substances Based on Measured Occurrence in Multiple Media.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(13): 5107-5116, (2023).",
             "distribution": [
                 {
-                    "title": "https://pubs.acs.org/doi/10.1021/acs.est.2c07185?goto=supporting-info",
-                    "accessURL": "https://pubs.acs.org/doi/10.1021/acs.est.2c07185?goto=supporting-info"
+                    "accessURL": "https://pubs.acs.org/doi/10.1021/acs.est.2c07185?goto=supporting-info",
+                    "title": "https://pubs.acs.org/doi/10.1021/acs.est.2c07185?goto=supporting-info"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530691",
+            "keyword": [
+                "Exposure pathways",
+                "PFAS",
+                "systematic evi",
+                "exposure data curation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-09-07",
-            "references": [
-                "https://doi.org/10.1021/acs.est.2c07185"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196941,49 +196935,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.2c07185"
+            ],
+            "rights": null,
+            "title": "PFAS Occurrence Systematic Evidence Mapping Data Extraction September 7 2022"
         },
         {
-            "title": "SWAT_RockCreek_Baseline_Calibration_Validation; SWAT_RockCreek_ACP_Scenario_Comparison",
-            "description": "The dataset supports findings in the study: \"Integrating Agricultural Conservation Planning Framework with the Soil and Water Assessment Tool to Reduce Phosphorus Loadings to Lake Erie: A Case Study\". Results of this study demonstrate the integration of the ACPF and SWAT in a small agricultural watershed within the Western Lake Erie Basin. Datasets include SWAT model calibration and validation as well as SWAT model ACP scenario results. \n\nThis dataset is associated with the following publication:\nYuan, Y., and S. Whisenant. Integrating ACPF and SWAT to Assess Potential Phosphorus Loading Reductions to Lake Erie: A Case Study.   APPLIED ENGINEERING IN AGRICULTURE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 39(6): 645-655, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528721",
-            "keyword": [
-                "ACPF",
-                "water quality",
-                "agricultural conservation practices",
-                "Nutrient loadings",
-                "effectiveness",
-                "Lake Erie",
-                "SWAT"
-            ],
             "contactPoint": {
                 "fn": "Yongping Yuan",
                 "hasEmail": "mailto:yuan.yongping@epa.gov"
             },
+            "description": "The dataset supports findings in the study: \"Integrating Agricultural Conservation Planning Framework with the Soil and Water Assessment Tool to Reduce Phosphorus Loadings to Lake Erie: A Case Study\". Results of this study demonstrate the integration of the ACPF and SWAT in a small agricultural watershed within the Western Lake Erie Basin. Datasets include SWAT model calibration and validation as well as SWAT model ACP scenario results. \n\nThis dataset is associated with the following publication:\nYuan, Y., and S. Whisenant. Integrating ACPF and SWAT to Assess Potential Phosphorus Loading Reductions to Lake Erie: A Case Study.   APPLIED ENGINEERING IN AGRICULTURE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 39(6): 645-655, (2023).",
             "distribution": [
                 {
-                    "title": "SWAT_RockCreek_Baseline_Calibration_Validation.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528721/SWAT_RockCreek_Baseline_Calibration_Validation.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SWAT_RockCreek_Baseline_Calibration_Validation.xlsx"
                 },
                 {
-                    "title": "SWAT_RockCreek_ACP_Scenario_Comparison.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528721/SWAT_RockCreek_ACP_Scenario_Comparison.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SWAT_RockCreek_ACP_Scenario_Comparison.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528721",
+            "keyword": [
+                "ACPF",
+                "water quality",
+                "agricultural conservation practices",
+                "Nutrient loadings",
+                "effectiveness",
+                "Lake Erie",
+                "SWAT"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-22",
-            "references": [
-                "https://doi.org/10.13031/aea.15644"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -196993,20 +196987,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.13031/aea.15644"
+            ],
+            "rights": null,
+            "title": "SWAT_RockCreek_Baseline_Calibration_Validation; SWAT_RockCreek_ACP_Scenario_Comparison"
         },
         {
-            "title": "NCS Pb summary statistics",
-            "description": "NA. This dataset is not publicly accessible because: The data used in this manuscript were obtained under Data Use Agreements with the NCS Vanguard Data and Sample Archive and Access System and the NICHD Data and Specimen Hub (DASH). Because of the requirements of the DUA, we are unable to provide raw data; thus, the summary data are provided that are included in the manuscript. It can be accessed through the following means: The manuscript contains tables of the summary statistics. For the original data, users must have an approved DUA with NICHD DASH. Format: Word file of tables with summary statistics for maternal blood Pb, urine Pb, Pb surface wipe loading and Pb vacuum bag dust. \n\nThis dataset is associated with the following publication:\nStanek, L., N. Grokhowsky, B. George, and K. Thomas. Assessing lead exposure in U.S. pregnant women using biological and residential measurements.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, (905): 167135, (2023).",
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
+                "fn": "Lindsay Stanek",
+                "hasEmail": "mailto:stanek.lindsay@epa.gov"
+            },
+            "description": "NA. This dataset is not publicly accessible because: The data used in this manuscript were obtained under Data Use Agreements with the NCS Vanguard Data and Sample Archive and Access System and the NICHD Data and Specimen Hub (DASH). Because of the requirements of the DUA, we are unable to provide raw data; thus, the summary data are provided that are included in the manuscript. It can be accessed through the following means: The manuscript contains tables of the summary statistics. For the original data, users must have an approved DUA with NICHD DASH. Format: Word file of tables with summary statistics for maternal blood Pb, urine Pb, Pb surface wipe loading and Pb vacuum bag dust. \n\nThis dataset is associated with the following publication:\nStanek, L., N. Grokhowsky, B. George, and K. Thomas. Assessing lead exposure in U.S. pregnant women using biological and residential measurements.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, (905): 167135, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529133",
             "keyword": [
                 "lead",
@@ -197014,14 +197012,10 @@
                 "Children's Environmental Health",
                 "House dust"
             ],
-            "contactPoint": {
-                "fn": "Lindsay Stanek",
-                "hasEmail": "mailto:stanek.lindsay@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-12",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.167135"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197031,19 +197025,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.167135"
+            ],
+            "rights": null,
+            "title": "NCS Pb summary statistics"
         },
         {
-            "title": "Dataset_For _P_Management_Paper",
-            "description": "The dataset contains coded data extracted from 24 publications with quantitative values on the effectiveness of nutrient management practices for DRP losses. Within the dataset has been split into two categories: 1) plot-scale studies where the maximum study area was 0.05 ha and 2) field-scale studies with study areas ranging from 0.5 to 20 ha. The dataset contains information regarding study areas, soil type, monitoring details, nutrient management details, and phosphorus losses from the study areas. \n\nThis dataset is associated with the following publication:\nPrasad, L.R., A.M. Thomason, F.J. Arriaga, L. Koropeckyj-Cox, and Y. Yuan. Effectiveness of Residue and Tillage Management on Runoff Pollutant Reduction from Agricultural Areas.   Journal of the ASABE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 66(6): 1341-1354, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Yongping Yuan",
+                "hasEmail": "mailto:yuan.yongping@epa.gov"
+            },
+            "description": "The dataset contains coded data extracted from 24 publications with quantitative values on the effectiveness of nutrient management practices for DRP losses. Within the dataset has been split into two categories: 1) plot-scale studies where the maximum study area was 0.05 ha and 2) field-scale studies with study areas ranging from 0.5 to 20 ha. The dataset contains information regarding study areas, soil type, monitoring details, nutrient management details, and phosphorus losses from the study areas. \n\nThis dataset is associated with the following publication:\nPrasad, L.R., A.M. Thomason, F.J. Arriaga, L. Koropeckyj-Cox, and Y. Yuan. Effectiveness of Residue and Tillage Management on Runoff Pollutant Reduction from Agricultural Areas.   Journal of the ASABE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 66(6): 1341-1354, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529914/Dataset_For_RTM_Paper_Final.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dataset_For_RTM_Paper_Final.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529914",
             "keyword": [
@@ -197054,20 +197058,10 @@
                 "effectiveness",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Yongping Yuan",
-                "hasEmail": "mailto:yuan.yongping@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Dataset_For_RTM_Paper_Final.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529914/Dataset_For_RTM_Paper_Final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-02-03",
-            "references": [
-                "https://doi.org/10.13031/ja.15518"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197077,40 +197071,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.13031/ja.15518"
+            ],
+            "rights": null,
+            "title": "Dataset_For _P_Management_Paper"
         },
         {
-            "title": "Data in support of the Pawcatuck River and Little Narragansett Bay Eutrophication Modeling Effort",
-            "description": "This data repository has been created to support Cashel et al. 2024 publication titled \u201cUsing Monitoring and Mechanistic Modeling to Improve Understanding of Eutrophication in a Shallow New England Estuary\u201d. This research served to explore the applicability of observed data and a dynamic, mechanistic fate and transport water quality model to assess eutrophication and hypoxia in the Pawcatuck River Estuary (New England, USA). Associated files include outputs from the Wood-Pawcatuck Watershed HSPF model, atmospheric forcing functions, continuous and discrete observed data in the Pawcatuck River Estuary, and additional information used to support this research. Refer to Section 6 of the Supplementary Materials associated with this research paper for a description of the contents of each file. \n\nContinuous (15-min intervals) sonde data and grab samples were collected across several years with locations designed to capture longitudinal, vertical, and lateral spatial variation within the system. Observed data include: salinity (SAL, ppt), water temperature (WT, \u00b0C), depth (DEP, m), dissolved oxygen (DO, mg/L), chlorophyll a (chl a, \u03bcg/L as chl a), ammonium (NH4, \u03bcg/L as N), nitrate (NO3, \u03bcg/L as N), dissolved inorganic phosphorus (DIP, \u03bcg/L as P), total nitrogen (TN, \u03bcg/L as N), total phosphorus (TP, \u03bcg/L as P), and total suspended solids (TSS, \u03bcg/L). \n\nThis dataset is associated with the following publication:\nCashel, F.S., C.D. Knightes, C. Lupo, T. Iott, K. Streich, C.J. Conville, T.W. Bridges, and I. Dombroski. Using monitoring and mechanistic modeling to improve understanding of eutrophication in a shallow New England estuary.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 355(March 2024): 120478, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529784",
-            "keyword": [
-                "Nitrogen and Co-pollutants",
-                "water quality",
-                "modeling",
-                "eutrophication"
-            ],
             "contactPoint": {
                 "fn": "Christopher Knightes",
                 "hasEmail": "mailto:knightes.chris@epa.gov"
             },
+            "description": "This data repository has been created to support Cashel et al. 2024 publication titled \u201cUsing Monitoring and Mechanistic Modeling to Improve Understanding of Eutrophication in a Shallow New England Estuary\u201d. This research served to explore the applicability of observed data and a dynamic, mechanistic fate and transport water quality model to assess eutrophication and hypoxia in the Pawcatuck River Estuary (New England, USA). Associated files include outputs from the Wood-Pawcatuck Watershed HSPF model, atmospheric forcing functions, continuous and discrete observed data in the Pawcatuck River Estuary, and additional information used to support this research. Refer to Section 6 of the Supplementary Materials associated with this research paper for a description of the contents of each file. \n\nContinuous (15-min intervals) sonde data and grab samples were collected across several years with locations designed to capture longitudinal, vertical, and lateral spatial variation within the system. Observed data include: salinity (SAL, ppt), water temperature (WT, \u00b0C), depth (DEP, m), dissolved oxygen (DO, mg/L), chlorophyll a (chl a, \u03bcg/L as chl a), ammonium (NH4, \u03bcg/L as N), nitrate (NO3, \u03bcg/L as N), dissolved inorganic phosphorus (DIP, \u03bcg/L as P), total nitrogen (TN, \u03bcg/L as N), total phosphorus (TP, \u03bcg/L as P), and total suspended solids (TSS, \u03bcg/L). \n\nThis dataset is associated with the following publication:\nCashel, F.S., C.D. Knightes, C. Lupo, T. Iott, K. Streich, C.J. Conville, T.W. Bridges, and I. Dombroski. Using monitoring and mechanistic modeling to improve understanding of eutrophication in a shallow New England estuary.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 355(March 2024): 120478, (2024).",
             "distribution": [
                 {
-                    "title": "https://data.mendeley.com/datasets/vywyyks4r6/1",
-                    "accessURL": "https://data.mendeley.com/datasets/vywyyks4r6/1"
+                    "accessURL": "https://data.mendeley.com/datasets/vywyyks4r6/1",
+                    "title": "https://data.mendeley.com/datasets/vywyyks4r6/1"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529784",
+            "keyword": [
+                "Nitrogen and Co-pollutants",
+                "water quality",
+                "modeling",
+                "eutrophication"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-02-21",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2024.120478"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197120,41 +197114,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2024.120478"
+            ],
+            "rights": null,
+            "title": "Data in support of the Pawcatuck River and Little Narragansett Bay Eutrophication Modeling Effort"
         },
         {
-            "title": "Dataset for Performance of Vehicle Add-on Mobile Monitoring System PM2.5 measurements during wildland fire episodes",
-            "description": "This file provides the data used to generate the tables and figures in the manuscript, including a definition of each parameter and units where applicable. \n\nThis dataset is associated with the following publication:\nBittner, A., A. Holder, A. Grieshop, G. Hagler, and W. Mitchell. Performance of Vehicle Add-on Mobile Monitoring System PM2.5 measurements during wildland fire episodes.   Environmental Science: Atmospheres. Royal Society of Chemistry, Cambridge,  UK, 4(3): 306-320, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530760",
-            "keyword": [
-                "Wildfire smoke",
-                "mobile monitoring",
-                "geospatial analysis",
-                "Averaging Time"
-            ],
             "contactPoint": {
                 "fn": "Amara Holder",
                 "hasEmail": "mailto:holder.amara@epa.gov"
             },
+            "description": "This file provides the data used to generate the tables and figures in the manuscript, including a definition of each parameter and units where applicable. \n\nThis dataset is associated with the following publication:\nBittner, A., A. Holder, A. Grieshop, G. Hagler, and W. Mitchell. Performance of Vehicle Add-on Mobile Monitoring System PM2.5 measurements during wildland fire episodes.   Environmental Science: Atmospheres. Royal Society of Chemistry, Cambridge,  UK, 4(3): 306-320, (2024).",
             "distribution": [
                 {
-                    "title": "VAMMS Evaluation Data Tables and Dictionary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530760/VAMMS%20Evaluation%20Data%20Tables%20and%20Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "VAMMS Evaluation Data Tables and Dictionary.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530760",
+            "keyword": [
+                "Wildfire smoke",
+                "mobile monitoring",
+                "geospatial analysis",
+                "Averaging Time"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-02-20",
-            "references": [
-                "https://doi.org/10.1039/d3ea00170a"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197164,20 +197158,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d3ea00170a"
+            ],
+            "rights": null,
+            "title": "Dataset for Performance of Vehicle Add-on Mobile Monitoring System PM2.5 measurements during wildland fire episodes"
         },
         {
-            "title": "Maternal exposure to nitrosamines in drinking water during pregnancy and birth outcomes in a Chinese cohort",
-            "description": "Chinese Vital Records from 2015 to 2016. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: It cannot due to PII and Non-EPA data being used. Format: Chinese vital records data. \n\nThis dataset is associated with the following publication:\nLuo, Q., C. Liu, E. Bei, Y. Deng, Y. Miao, Y. Qiu, W. Lu, J. Wright, c. chen, and Q. Zeng. Maternal exposure to nitrosamines in drinking water during pregnancy and birth outcomes in a Chinese cohort.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, (315): 137776, (2023).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "John Wright",
+                "hasEmail": "mailto:wright.michael@epa.gov"
+            },
+            "description": "Chinese Vital Records from 2015 to 2016. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: It cannot due to PII and Non-EPA data being used. Format: Chinese vital records data. \n\nThis dataset is associated with the following publication:\nLuo, Q., C. Liu, E. Bei, Y. Deng, Y. Miao, Y. Qiu, W. Lu, J. Wright, c. chen, and Q. Zeng. Maternal exposure to nitrosamines in drinking water during pregnancy and birth outcomes in a Chinese cohort.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, (315): 137776, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530694",
             "keyword": [
                 "Nitrosamines",
@@ -197185,14 +197183,10 @@
                 "Low Birth Weight",
                 "preterm birth"
             ],
-            "contactPoint": {
-                "fn": "John Wright",
-                "hasEmail": "mailto:wright.michael@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-01-05",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2023.137776"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197202,62 +197196,64 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2023.137776"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Maternal exposure to nitrosamines in drinking water during pregnancy and birth outcomes in a Chinese cohort"
         },
         {
-            "title": "Data supporting Modeling the Oxygen Isotope Anomaly of Reactive Nitrogen in the Community Multiscale Air Quality (CMAQ) Model",
-            "description": "The data contains CMAQ fortran model code and shell scripts used for configuration in the work of Walters et al. Links are provided to base (unmodified) CMAQ release code (github and doi: 10.5281/zenodo.1079878), emissions and meteorology input data (doi: 10.15139/S3/F2KJSK), and output data from the work (doi: 10.5281/zenodo.10493756).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529801",
-            "keyword": [
-                "nitrate",
-                "CMAQ",
-                "Nitrogen and Co-pollutants",
-                "Reactive Nitrogen",
-                "air quality",
-                "Nitric Acid",
-                "pm2.5",
-                "deposition",
-                "nitrogen oxides",
-                "stable isotopes"
-            ],
             "contactPoint": {
                 "fn": "Havala Pye",
                 "hasEmail": "mailto:pye.havala@epa.gov"
             },
+            "description": "The data contains CMAQ fortran model code and shell scripts used for configuration in the work of Walters et al. Links are provided to base (unmodified) CMAQ release code (github and doi: 10.5281/zenodo.1079878), emissions and meteorology input data (doi: 10.15139/S3/F2KJSK), and output data from the work (doi: 10.5281/zenodo.10493756).",
             "distribution": [
                 {
-                    "title": "https://github.com/USEPA/CMAQ",
-                    "accessURL": "https://github.com/USEPA/CMAQ"
+                    "accessURL": "https://github.com/USEPA/CMAQ",
+                    "title": "https://github.com/USEPA/CMAQ"
                 },
                 {
-                    "title": "https://doi.org/10.5281/zenodo.10493756",
-                    "accessURL": "https://doi.org/10.5281/zenodo.10493756"
+                    "accessURL": "https://doi.org/10.5281/zenodo.10493756",
+                    "title": "https://doi.org/10.5281/zenodo.10493756"
                 },
                 {
-                    "title": "https://doi.org/10.5281/zenodo.1079878",
-                    "accessURL": "https://doi.org/10.5281/zenodo.1079878"
+                    "accessURL": "https://doi.org/10.5281/zenodo.1079878",
+                    "title": "https://doi.org/10.5281/zenodo.1079878"
                 },
                 {
-                    "title": "20240416_walters_code.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529801/20240416_walters_code.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "20240416_walters_code.zip"
                 },
                 {
-                    "title": "https://doi.org/10.15139/S3/F2KJSK",
-                    "accessURL": "https://doi.org/10.15139/S3/F2KJSK"
+                    "accessURL": "https://doi.org/10.15139/S3/F2KJSK",
+                    "title": "https://doi.org/10.15139/S3/F2KJSK"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529801",
+            "keyword": [
+                "nitrate",
+                "CMAQ",
+                "Nitrogen and Co-pollutants",
+                "Reactive Nitrogen",
+                "air quality",
+                "Nitric Acid",
+                "pm2.5",
+                "deposition",
+                "nitrogen oxides",
+                "stable isotopes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-04-16",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -197266,19 +197262,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Data supporting Modeling the Oxygen Isotope Anomaly of Reactive Nitrogen in the Community Multiscale Air Quality (CMAQ) Model"
         },
         {
-            "title": "Collocation Shelter Design Documents",
-            "description": "This file contains design documents (pdf and dwg) that could be provided to a fabricator to build air sensor collocation shelters. \n\nThis dataset is associated with the following publication:\nKumar, M., K. Barkjohn, and A. Clements. Lessons Learned and Best Practices: Air Sensor Collocation Shelters. Presented at Summary Slides on the Air Sensor Toolbox, Virtual, NC, USA, 04/12/2024 - 04/12/2024.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Karoline Barkjohn",
+                "hasEmail": "mailto:barkjohn.karoline@epa.gov"
+            },
+            "description": "This file contains design documents (pdf and dwg) that could be provided to a fabricator to build air sensor collocation shelters. \n\nThis dataset is associated with the following publication:\nKumar, M., K. Barkjohn, and A. Clements. Lessons Learned and Best Practices: Air Sensor Collocation Shelters. Presented at Summary Slides on the Air Sensor Toolbox, Virtual, NC, USA, 04/12/2024 - 04/12/2024.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530867/CollocationShelterDesignDocuments_DWG.zip",
+                    "mediaType": "application/zip",
+                    "title": "CollocationShelterDesignDocuments_DWG.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530867",
             "keyword": [
@@ -197289,19 +197293,11 @@
                 "Shelter",
                 "design"
             ],
-            "contactPoint": {
-                "fn": "Karoline Barkjohn",
-                "hasEmail": "mailto:barkjohn.karoline@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "CollocationShelterDesignDocuments_DWG.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530867/CollocationShelterDesignDocuments_DWG.zip",
-                    "mediaType": "application/zip"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-09-14",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -197310,42 +197306,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Collocation Shelter Design Documents"
         },
         {
-            "title": "Dataset_For _P_Management_Paper",
-            "description": "Dataset_For _P_Management_Paper. \n\nThis dataset is associated with the following publication:\nKamrath, B., and Y. Yuan. Effectiveness of Nutrient Management For Reducing Phosphorus Losses From Agricultural Areas..   Transactions of the ASABE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 1(2): 77-88, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529898",
-            "keyword": [
-                "agricultural conservation practices",
-                "nutrient management",
-                "phosphorous fertilization rate",
-                "effectiveness",
-                "agricultural areas"
-            ],
             "contactPoint": {
                 "fn": "Yongping Yuan",
                 "hasEmail": "mailto:yuan.yongping@epa.gov"
             },
+            "description": "Dataset_For _P_Management_Paper. \n\nThis dataset is associated with the following publication:\nKamrath, B., and Y. Yuan. Effectiveness of Nutrient Management For Reducing Phosphorus Losses From Agricultural Areas..   Transactions of the ASABE. AMERICAN SOCIETY OF AGRICULTURAL AND BIOLOGICAL ENGINEERS, ST. JOSEPH, MI, USA, 1(2): 77-88, (2023).",
             "distribution": [
                 {
-                    "title": "Nutrient_Management_Supplemental_Materials.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529898/Nutrient_Management_Supplemental_Materials.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Nutrient_Management_Supplemental_Materials.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529898",
+            "keyword": [
+                "agricultural conservation practices",
+                "nutrient management",
+                "phosphorous fertilization rate",
+                "effectiveness",
+                "agricultural areas"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-02-03",
-            "references": [
-                "https://doi.org/10.13031/jnrae.15572"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197355,20 +197349,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.13031/jnrae.15572"
+            ],
+            "rights": null,
+            "title": "Dataset_For _P_Management_Paper"
         },
         {
-            "title": "Assessing the nucleic acid decay of human wastewater markers and enteric viruses in estuarine waters in Sydney, Australia",
-            "description": "This study describes decay rates of microbial source tracking markers, viral surrogates and pathogens in estuarine waters under in situ conditions and in light vs dark conditions. This dataset is not publicly accessible because: Because it is not owned by EPA. It can be accessed through the following means: Data will be made available on request to corresponding author. Format: N/A- no primary/secondary data owned by EPA. \n\nThis dataset is associated with the following publication:\nAhmed, W., A. Korajkic, M. Gabrewold, S. Payyappat, M. Cassidy, N. Harrison, and C. Besley. Assessing the nucleic acid decay of human wastewater markers and enteric viruses in estuarine waters in Sydney, Australia.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 926: 171389, (2024).",
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
+                "fn": "Asja Korajkic",
+                "hasEmail": "mailto:korajkic.asja@epa.gov"
+            },
+            "description": "This study describes decay rates of microbial source tracking markers, viral surrogates and pathogens in estuarine waters under in situ conditions and in light vs dark conditions. This dataset is not publicly accessible because: Because it is not owned by EPA. It can be accessed through the following means: Data will be made available on request to corresponding author. Format: N/A- no primary/secondary data owned by EPA. \n\nThis dataset is associated with the following publication:\nAhmed, W., A. Korajkic, M. Gabrewold, S. Payyappat, M. Cassidy, N. Harrison, and C. Besley. Assessing the nucleic acid decay of human wastewater markers and enteric viruses in estuarine waters in Sydney, Australia.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 926: 171389, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530474",
             "keyword": [
                 "Microbial Source Tracking",
@@ -197378,14 +197376,10 @@
                 "Human Health Risk",
                 "estuarine waters"
             ],
-            "contactPoint": {
-                "fn": "Asja Korajkic",
-                "hasEmail": "mailto:korajkic.asja@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-01-31",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2024.171389"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197395,20 +197389,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2024.171389"
+            ],
+            "rights": null,
+            "title": "Assessing the nucleic acid decay of human wastewater markers and enteric viruses in estuarine waters in Sydney, Australia"
         },
         {
-            "title": "Human biomonitoring health based guidance values Dashboard",
-            "description": "a Dashboard containing current human biomonitoring health based guidance values. This dataset is not publicly accessible because: data not funded by EPA. It can be accessed through the following means: https://www.intlexposurescience.org/i-hbm/. Format: human biomonitoring health based guidance values in human specimen concentrations. \n\nThis dataset is associated with the following publication:\nMelnyk, L., S. Nakayama, A. St. Armand, and T. Pollock. Interpreting biomonitoring data: Introducing the international human biomonitoring (i-HBM) working group's health-based guidance value (HB2GV) dashboard.   INTERNATIONAL JOURNAL OF HYGIENE AND ENVIRONMENTAL HEALTH. Elsevier B.V., Amsterdam,  NETHERLANDS, 247(114046): 1, (2023).",
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
+                "fn": "Lisa Melnyk",
+                "hasEmail": "mailto:melnyk.lisa@epa.gov"
+            },
+            "description": "a Dashboard containing current human biomonitoring health based guidance values. This dataset is not publicly accessible because: data not funded by EPA. It can be accessed through the following means: https://www.intlexposurescience.org/i-hbm/. Format: human biomonitoring health based guidance values in human specimen concentrations. \n\nThis dataset is associated with the following publication:\nMelnyk, L., S. Nakayama, A. St. Armand, and T. Pollock. Interpreting biomonitoring data: Introducing the international human biomonitoring (i-HBM) working group's health-based guidance value (HB2GV) dashboard.   INTERNATIONAL JOURNAL OF HYGIENE AND ENVIRONMENTAL HEALTH. Elsevier B.V., Amsterdam,  NETHERLANDS, 247(114046): 1, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1528919",
             "keyword": [
                 "reference values",
@@ -197416,15 +197414,10 @@
                 "biomonitoring equivalents",
                 "biomonitoring"
             ],
-            "contactPoint": {
-                "fn": "Lisa Melnyk",
-                "hasEmail": "mailto:melnyk.lisa@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-12-31",
-            "references": [
-                "https://doi.org/10.1016/j.ijheh.2022.114046",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10103580"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197434,41 +197427,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ijheh.2022.114046",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10103580"
+            ],
+            "rights": null,
+            "title": "Human biomonitoring health based guidance values Dashboard"
         },
         {
-            "title": "Dataset for A Comparison of In Vitro Points of Departure with Human Biomonitoring Levels for Per- and Polyfluoroalkyl Substances (PFAS)",
-            "description": "Dataset for A Comparison of In Vitro Points of Departure with Human Biomonitoring Levels for Per- and Polyfluoroalkyl Substances (PFAS), to be published by Environmental Health Perspectives (EHP). \n\nThis dataset is associated with the following publication:\nJudson, R., D. Smith, M. Devito, J. Wambaugh, B. Wetmore, K. Friedman, G. Patlewicz, R. Thomas, R. Sayre, J. Olker, S. Degitz, S. Padilla, J. Harrill, T. Shafer, and K. Carstens. A Comparison of In Vitro Points of Departure with Human Blood Levels for Per- and Polyfluoroalkyl Substances (PFAS) (Toxics).   Toxics. MDPI, Basel,  SWITZERLAND, 12(4): 271, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529862",
-            "keyword": [
-                "biomonitoring",
-                "in vitro points of departure",
-                "CompTox Chemicals Dashboard",
-                "PFAS"
-            ],
             "contactPoint": {
                 "fn": "Richard Judson",
                 "hasEmail": "mailto:judson.richard@epa.gov"
             },
+            "description": "Dataset for A Comparison of In Vitro Points of Departure with Human Biomonitoring Levels for Per- and Polyfluoroalkyl Substances (PFAS), to be published by Environmental Health Perspectives (EHP). \n\nThis dataset is associated with the following publication:\nJudson, R., D. Smith, M. Devito, J. Wambaugh, B. Wetmore, K. Friedman, G. Patlewicz, R. Thomas, R. Sayre, J. Olker, S. Degitz, S. Padilla, J. Harrill, T. Shafer, and K. Carstens. A Comparison of In Vitro Points of Departure with Human Blood Levels for Per- and Polyfluoroalkyl Substances (PFAS) (Toxics).   Toxics. MDPI, Basel,  SWITZERLAND, 12(4): 271, (2024).",
             "distribution": [
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65650844e4b063812d55a86c",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65650844e4b063812d55a86c"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65650844e4b063812d55a86c",
+                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=65650844e4b063812d55a86c"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529862",
+            "keyword": [
+                "biomonitoring",
+                "in vitro points of departure",
+                "CompTox Chemicals Dashboard",
+                "PFAS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-25",
-            "references": [
-                "https://doi.org/10.3390/toxics12040271",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11053643"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197478,42 +197471,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxics12040271",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11053643"
+            ],
+            "rights": null,
+            "title": "Dataset for A Comparison of In Vitro Points of Departure with Human Biomonitoring Levels for Per- and Polyfluoroalkyl Substances (PFAS)"
         },
         {
-            "title": "Survival, Growth, and Reproduction Responses in a Three-Generation Exposure of the Zebrafish (Danio rerio) to Perfluorooctane Sulfonate",
-            "description": "Supporting Information for \"Gust KA, Mylroie JE, Kimble AN, Wilbanks MS, Steward CSC, Chapman KA, Jensen KM, Kennedy AJ, Krupa PM, Waisner SA, Pandelides Z, Garcia-Reyero N, Erickson RJ, Ankley GT, Conder J, Moore DW. Survival, Growth, and Reproduction Responses in a Three-Generation Exposure of the Zebrafish (Danio rerio) to Perfluorooctane Sulfonate. Environ Toxicol Chem. 2024 Jan;43(1):115-131. doi: 10.1002/etc.5770. Epub 2023 Nov 29. PMID: 38018867.\". \n\nThis dataset is associated with the following publication:\nGust, K., J. Mylroie, A. Kimble, M. Wilbanks, C. Steward, K. Chapman, K. Jensen, A. Kennedy, P. Krupa, S. Waisner, Z. Pandelides, N. Garcia-Reyero, R. Erickson, G. Ankley, J. Conder, and D. Moore. Survival, Growth, and Reproduction Responses in a Three-Generation Exposure of the Zebrafish (Danio rerio) to Perfluorooctane Sulfonate.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(1): 115-131, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530689",
-            "keyword": [
-                "growth",
-                "Multigenerational exposure",
-                "Perfluorooctane sulfonic acid",
-                "reproduction",
-                "zebrafish"
-            ],
             "contactPoint": {
                 "fn": "Russell Erickson",
                 "hasEmail": "mailto:erickson.russell@epa.gov"
             },
+            "description": "Supporting Information for \"Gust KA, Mylroie JE, Kimble AN, Wilbanks MS, Steward CSC, Chapman KA, Jensen KM, Kennedy AJ, Krupa PM, Waisner SA, Pandelides Z, Garcia-Reyero N, Erickson RJ, Ankley GT, Conder J, Moore DW. Survival, Growth, and Reproduction Responses in a Three-Generation Exposure of the Zebrafish (Danio rerio) to Perfluorooctane Sulfonate. Environ Toxicol Chem. 2024 Jan;43(1):115-131. doi: 10.1002/etc.5770. Epub 2023 Nov 29. PMID: 38018867.\". \n\nThis dataset is associated with the following publication:\nGust, K., J. Mylroie, A. Kimble, M. Wilbanks, C. Steward, K. Chapman, K. Jensen, A. Kennedy, P. Krupa, S. Waisner, Z. Pandelides, N. Garcia-Reyero, R. Erickson, G. Ankley, J. Conder, and D. Moore. Survival, Growth, and Reproduction Responses in a Three-Generation Exposure of the Zebrafish (Danio rerio) to Perfluorooctane Sulfonate.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(1): 115-131, (2024).",
             "distribution": [
                 {
-                    "title": "PFOS ZF Multi Gen All Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530689/PFOS%20ZF%20Multi%20Gen%20All%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PFOS ZF Multi Gen All Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530689",
+            "keyword": [
+                "growth",
+                "Multigenerational exposure",
+                "Perfluorooctane sulfonic acid",
+                "reproduction",
+                "zebrafish"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-29",
-            "references": [
-                "https://doi.org/10.1002/etc.5770"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197523,53 +197517,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5770"
+            ],
+            "rights": null,
+            "title": "Survival, Growth, and Reproduction Responses in a Three-Generation Exposure of the Zebrafish (Danio rerio) to Perfluorooctane Sulfonate"
         },
         {
-            "title": "Characterizing Chemical Exposure Trends from NHANES Urinary Biomonitoring Data",
-            "description": "Supplementary material for \"Characterizing Chemical Exposure Trends from NHANES Urinary Biomonitoring Data\". \n\nThis dataset is associated with the following publication:\nStanfield, Z., W. Setzer, V. Hull, R. Sayre, K. Isaacs, and J. Wambaugh. Characterizing Chemical Exposure Trends from NHANES Urinary Biomonitoring Data.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 132(1): 017009, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530114",
-            "keyword": [
-                "Trend analysis",
-                "biomonitoring data",
-                "ExpoCast",
-                "exposure",
-                "Bayesian inference"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "Supplementary material for \"Characterizing Chemical Exposure Trends from NHANES Urinary Biomonitoring Data\". \n\nThis dataset is associated with the following publication:\nStanfield, Z., W. Setzer, V. Hull, R. Sayre, K. Isaacs, and J. Wambaugh. Characterizing Chemical Exposure Trends from NHANES Urinary Biomonitoring Data.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 132(1): 017009, (2024).",
             "distribution": [
                 {
-                    "title": "ehp12188.s001.acco.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530114/ehp12188.s001.acco.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "ehp12188.s001.acco.pdf"
                 },
                 {
-                    "title": "EHP12188R1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530114/EHP12188R1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EHP12188R1.xlsx"
                 },
                 {
-                    "title": "ehp12188.smcontents.508.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530114/ehp12188.smcontents.508.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "ehp12188.smcontents.508.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530114",
+            "keyword": [
+                "Trend analysis",
+                "biomonitoring data",
+                "ExpoCast",
+                "exposure",
+                "Bayesian inference"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-29",
-            "references": [
-                "https://doi.org/10.1289/ehp12188",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10824265"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197579,20 +197572,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp12188",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10824265"
+            ],
+            "rights": null,
+            "title": "Characterizing Chemical Exposure Trends from NHANES Urinary Biomonitoring Data"
         },
         {
-            "title": "Comparing the decay of human wastewater-associated markers and enteric viruses in laboratory microcosms simulating estuarine waters in a temperate climatic zone using qPCR/RT-qPCR assays",
-            "description": "This study provides valuable insights into the decay rates of wastewater-associated markers and enteric viruses under different experimental conditions that mimicked temperate environmental conditions. The findings contribute to our understanding of the fate and persistence of these markers in the environment which is crucial for assessing and managing risks from contamination by untreated human wastewater. This dataset is not publicly accessible because: no primary/secondary data owned by EPA. It can be accessed through the following means: Data will be made available on request to the corresponding author, Dr Warish Ahmed. Format: N/A- no primary/secondary data owned by EPA. \n\nThis dataset is associated with the following publication:\nAhmed, W., A. Korajkic, W.J.M. Smith, S. Payyappat, M. Cassidy, N. Harrison, and C. Besley. Comparing the decay of human wastewater-associated markers and enteric viruses in laboratory microcosms simulating estuarine waters in a temperate climatic zone using qPCR/RT-qPCR assays.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 908: 167845, (2024).",
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
+                "fn": "Asja Korajkic",
+                "hasEmail": "mailto:korajkic.asja@epa.gov"
+            },
+            "description": "This study provides valuable insights into the decay rates of wastewater-associated markers and enteric viruses under different experimental conditions that mimicked temperate environmental conditions. The findings contribute to our understanding of the fate and persistence of these markers in the environment which is crucial for assessing and managing risks from contamination by untreated human wastewater. This dataset is not publicly accessible because: no primary/secondary data owned by EPA. It can be accessed through the following means: Data will be made available on request to the corresponding author, Dr Warish Ahmed. Format: N/A- no primary/secondary data owned by EPA. \n\nThis dataset is associated with the following publication:\nAhmed, W., A. Korajkic, W.J.M. Smith, S. Payyappat, M. Cassidy, N. Harrison, and C. Besley. Comparing the decay of human wastewater-associated markers and enteric viruses in laboratory microcosms simulating estuarine waters in a temperate climatic zone using qPCR/RT-qPCR assays.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 908: 167845, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530868",
             "keyword": [
                 "decay",
@@ -197602,14 +197600,10 @@
                 "Marker Gene",
                 "wastewater pollution"
             ],
-            "contactPoint": {
-                "fn": "Asja Korajkic",
-                "hasEmail": "mailto:korajkic.asja@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-10-12",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.167845"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197619,42 +197613,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.167845"
+            ],
+            "rights": null,
+            "title": "Comparing the decay of human wastewater-associated markers and enteric viruses in laboratory microcosms simulating estuarine waters in a temperate climatic zone using qPCR/RT-qPCR assays"
         },
         {
-            "title": "Simulated gastric leachate of 3D printer metal-fill filaments induces cytotoxic effects in rat and human intestinal models",
-            "description": "Supplemental material for \"Hughes MF, Clapper HM, Tedla G, Sowers TD, Rogers KR. Simulated gastric leachate of 3D printer metal-fill filaments induces cytotoxic effects in rat and human intestinal models. Toxicol In Vitro. 2024 Mar 6;97:105805. doi: 10.1016/j.tiv.2024.105805. Epub ahead of print. PMID: 38458500.\". Portions of this dataset are inaccessible because: N/A. They can be accessed through the following means: Data will be made available on request from Michael Hughes (hughes.michaelf@epa.gov). Format: N/A. \n\nThis dataset is associated with the following publication:\nHughes, M., H. Clapper, G. Tedla, T. Sowers, and K. Rogers. Simulated gastric leachate of 3D printer metal-fill filaments induces cytotoxic effects in rat and human intestinal models.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 97: 105805, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530690",
-            "keyword": [
-                "3D printing",
-                "cytotoxicity",
-                "Gastrointestinal Tract",
-                "in vitro",
-                "metals"
-            ],
             "contactPoint": {
                 "fn": "Michael Hughes",
                 "hasEmail": "mailto:hughes.michaelf@epa.gov"
             },
+            "description": "Supplemental material for \"Hughes MF, Clapper HM, Tedla G, Sowers TD, Rogers KR. Simulated gastric leachate of 3D printer metal-fill filaments induces cytotoxic effects in rat and human intestinal models. Toxicol In Vitro. 2024 Mar 6;97:105805. doi: 10.1016/j.tiv.2024.105805. Epub ahead of print. PMID: 38458500.\". Portions of this dataset are inaccessible because: N/A. They can be accessed through the following means: Data will be made available on request from Michael Hughes (hughes.michaelf@epa.gov). Format: N/A. \n\nThis dataset is associated with the following publication:\nHughes, M., H. Clapper, G. Tedla, T. Sowers, and K. Rogers. Simulated gastric leachate of 3D printer metal-fill filaments induces cytotoxic effects in rat and human intestinal models.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 97: 105805, (2024).",
             "distribution": [
                 {
-                    "title": "Supplemental Information.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530690/Supplemental%20Information.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supplemental Information.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530690",
+            "keyword": [
+                "3D printing",
+                "cytotoxicity",
+                "Gastrointestinal Tract",
+                "in vitro",
+                "metals"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-06",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2024.105805"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197664,41 +197658,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2024.105805"
+            ],
+            "rights": null,
+            "title": "Simulated gastric leachate of 3D printer metal-fill filaments induces cytotoxic effects in rat and human intestinal models"
         },
         {
-            "title": "HD Vapor Profiles 091223",
-            "description": "Measured sulfur mustard vapor concentrations in a 150 liter chamber in the presence of absorptive building materials. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529582",
-            "keyword": [
-                "fate and transport",
-                "sulfur mustard",
-                "chemical warfare agent",
-                "CWA",
-                "Air monitoring"
-            ],
             "contactPoint": {
                 "fn": "Lukas Oudejans",
                 "hasEmail": "mailto:oudejans.lukas@epa.gov"
             },
+            "description": "Measured sulfur mustard vapor concentrations in a 150 liter chamber in the presence of absorptive building materials. ",
             "distribution": [
                 {
-                    "title": "HD Vapor Profiles 091223.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529582/HD%20Vapor%20Profiles%20091223.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HD Vapor Profiles 091223.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529582",
+            "keyword": [
+                "fate and transport",
+                "sulfur mustard",
+                "chemical warfare agent",
+                "CWA",
+                "Air monitoring"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-15",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -197707,40 +197703,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "HD Vapor Profiles 091223"
         },
         {
-            "title": "Datasets for book chapter \"Current Progress in Sustainability Evaluation, Pollution Prevention, and Source Reduction using GREENSCOPE\"",
-            "description": "https://github.com/gruizmer/GRNS_Book_chapter\n\nThis GitHub repository contains all the data needed to run the case studies for the CRC book chapter entitled \"Current Progress in Sustainability Evaluation, Pollution Prevention, and Source Reduction using GREENSCOPE.\"\n\nThe dataset files contain the steady-state and dynamic (time sets) chemical process simulation results (mass flows, temperature profiles), GREENSCOPE performance indicator results, and concentration profiles of different components for the production of acetic acid (with two separation schemes), a novel biorefinery process when operated at steady state, and the dynamic assessment for optimization and control of a coal/biomass co-gasification process (with and without a novel process control strategy). The datasets show all data values used to generate each of the figures. \n\nThis dataset is associated with the following publication:\nAgbleze, S., S. Li, E.T. Quintanar Orozco, G.J. Ruiz-Mercado, and F.V. Lima. Current Progress in Sustainability Evaluation, Pollution Prevention, and Source Reduction Using GREENSCOPE. 1st. Chapter 14, Eric C.D. Tan (ed.), Sustainability Engineering Challenges, Technologies, and Applications. CRC Press - Taylor & Francis Group, LLC, Boca Raton, FL, USA,  289-318, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1524738",
-            "keyword": [
-                "life cycle inventory data",
-                "Chemical releases",
-                "emission control strategies",
-                "End of Life"
-            ],
             "contactPoint": {
                 "fn": "Gerardo Ruiz-Mercado",
                 "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
             },
+            "description": "https://github.com/gruizmer/GRNS_Book_chapter\n\nThis GitHub repository contains all the data needed to run the case studies for the CRC book chapter entitled \"Current Progress in Sustainability Evaluation, Pollution Prevention, and Source Reduction using GREENSCOPE.\"\n\nThe dataset files contain the steady-state and dynamic (time sets) chemical process simulation results (mass flows, temperature profiles), GREENSCOPE performance indicator results, and concentration profiles of different components for the production of acetic acid (with two separation schemes), a novel biorefinery process when operated at steady state, and the dynamic assessment for optimization and control of a coal/biomass co-gasification process (with and without a novel process control strategy). The datasets show all data values used to generate each of the figures. \n\nThis dataset is associated with the following publication:\nAgbleze, S., S. Li, E.T. Quintanar Orozco, G.J. Ruiz-Mercado, and F.V. Lima. Current Progress in Sustainability Evaluation, Pollution Prevention, and Source Reduction Using GREENSCOPE. 1st. Chapter 14, Eric C.D. Tan (ed.), Sustainability Engineering Challenges, Technologies, and Applications. CRC Press - Taylor & Francis Group, LLC, Boca Raton, FL, USA,  289-318, (2023).",
             "distribution": [
                 {
-                    "title": "https://github.com/gruizmer/GRNS_Book_chapter",
-                    "accessURL": "https://github.com/gruizmer/GRNS_Book_chapter"
+                    "accessURL": "https://github.com/gruizmer/GRNS_Book_chapter",
+                    "title": "https://github.com/gruizmer/GRNS_Book_chapter"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1524738",
+            "keyword": [
+                "life cycle inventory data",
+                "Chemical releases",
+                "emission control strategies",
+                "End of Life"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-03-01",
-            "references": [
-                "https://doi.org/10.1201/9781003167693"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197750,39 +197744,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1201/9781003167693"
+            ],
+            "rights": null,
+            "title": "Datasets for book chapter \"Current Progress in Sustainability Evaluation, Pollution Prevention, and Source Reduction using GREENSCOPE\""
         },
         {
-            "title": "OMG-miRNA-Biomarker for STICS",
-            "description": "Excel file of miRNA data. \n\nThis dataset is associated with the following publication:\nChen, H., S. Masood, A. Rappold, D. Diaz Sanchez, J. Samet, and H. Tong. The effects of controlled ozone exposure on circulating microRNAs and vascular and coagulation biomarkers: a mediation analysis.   Non-Coding RNA. MDPI, Basel,  SWITZERLAND, 9(4): 43, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530958",
-            "keyword": [
-                "inflammation"
-            ],
             "contactPoint": {
                 "fn": "Haiyan Tong",
                 "hasEmail": "mailto:tong.haiyan@epa.gov"
             },
+            "description": "Excel file of miRNA data. \n\nThis dataset is associated with the following publication:\nChen, H., S. Masood, A. Rappold, D. Diaz Sanchez, J. Samet, and H. Tong. The effects of controlled ozone exposure on circulating microRNAs and vascular and coagulation biomarkers: a mediation analysis.   Non-Coding RNA. MDPI, Basel,  SWITZERLAND, 9(4): 43, (2023).",
             "distribution": [
                 {
-                    "title": "OMG-miRNA-Biomarkers-for STICS(2).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530958/OMG-miRNA-Biomarkers-for%20STICS%282%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OMG-miRNA-Biomarkers-for STICS(2).xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530958",
+            "keyword": [
+                "inflammation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-05-06",
-            "references": [
-                "https://doi.org/10.3390/ncrna9040043",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10459325"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197792,51 +197785,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ncrna9040043",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10459325"
+            ],
+            "rights": null,
+            "title": "OMG-miRNA-Biomarker for STICS"
         },
         {
-            "title": "Multi-pollutant BenMAP Analysis Data",
-            "description": "Air quality data for Georgia for the years 2011 and 2025 for the pollutants: CO, EC, NH4, NO2, NO3-, O3, OC, PM2.5, SO2, SO4, and Secondary PM2.5. In addition the beta coefficients for single and multipollutant models and the accompanying variance-covariance matrix from Winquist et al. (2014), which examined single and multipollutant exposures and pediatric asthma ED visits. \n\nThis dataset is associated with the following publication:\nCoffman, E., A.G. Rappold, R.C. Nethery, J. Anderton, M. Amend, M.A. Jackson, H. Roman, N. Fann, K.R. Baker, and J.D. Sacks. Quantifying Multipollutant Health Impacts Using the Environmental Benefits Mapping and Analysis Program\u2013Community Edition (BenMAP-CE): A Case Study in Atlanta, Georgia.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 132(3): 037003, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530090",
-            "keyword": [
-                "asthma",
-                "air pollution",
-                "Multipollutant Approach"
-            ],
             "contactPoint": {
                 "fn": "Jason Sacks",
                 "hasEmail": "mailto:sacks.jason@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530090/documents/MP%20BenMAP_Meta-data%20for%20Science%20Hub%20-%204192023.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Air quality data for Georgia for the years 2011 and 2025 for the pollutants: CO, EC, NH4, NO2, NO3-, O3, OC, PM2.5, SO2, SO4, and Secondary PM2.5. In addition the beta coefficients for single and multipollutant models and the accompanying variance-covariance matrix from Winquist et al. (2014), which examined single and multipollutant exposures and pediatric asthma ED visits. \n\nThis dataset is associated with the following publication:\nCoffman, E., A.G. Rappold, R.C. Nethery, J. Anderton, M. Amend, M.A. Jackson, H. Roman, N. Fann, K.R. Baker, and J.D. Sacks. Quantifying Multipollutant Health Impacts Using the Environmental Benefits Mapping and Analysis Program\u2013Community Edition (BenMAP-CE): A Case Study in Atlanta, Georgia.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 132(3): 037003, (2024).",
             "distribution": [
                 {
-                    "title": "Winquist_vcov.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530090/Winquist_vcov.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Winquist_vcov.csv"
                 },
                 {
-                    "title": "Winquist_betas.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530090/Winquist_betas.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Winquist_betas.csv"
                 },
                 {
-                    "title": "MP BenMAP - GA AQ Data 2011 and 2025.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530090/MP%20BenMAP%20-%20GA%20AQ%20Data%202011%20and%202025.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MP BenMAP - GA AQ Data 2011 and 2025.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530090",
+            "keyword": [
+                "asthma",
+                "air pollution",
+                "Multipollutant Approach"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-10",
-            "references": [
-                "https://doi.org/10.1289/ehp12969",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10916644"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197847,43 +197842,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530090/documents/MP%20BenMAP_Meta-data%20for%20Science%20Hub%20-%204192023.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1289/ehp12969",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10916644"
+            ],
+            "rights": null,
+            "title": "Multi-pollutant BenMAP Analysis Data"
         },
         {
-            "title": "PFAS leachate concentrations in Puerto Rico Landfills",
-            "description": "The data represents the information that was used to create the figures and the tables used in the manuscript. \n\nThis dataset is associated with the following publication:\nRobey, N., Y. Liu, M. Crespo-Medina, J. Bowden, H. Solo-Gabriele, T. Townsend, and T. Tolaymat. Characterization of Per- and Polyfluoroalkyl Substances (PFAS) and Other Constituents in MSW Landfill Leachate from Puerto Rico.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 358: 142131, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529916",
-            "keyword": [
-                "Contamination",
-                "PFAS",
-                "leachate",
-                "landfills",
-                "Puerto Rico"
-            ],
             "contactPoint": {
                 "fn": "Thabet Tolaymat",
                 "hasEmail": "mailto:tolaymat.thabet@epa.gov"
             },
+            "description": "The data represents the information that was used to create the figures and the tables used in the manuscript. \n\nThis dataset is associated with the following publication:\nRobey, N., Y. Liu, M. Crespo-Medina, J. Bowden, H. Solo-Gabriele, T. Townsend, and T. Tolaymat. Characterization of Per- and Polyfluoroalkyl Substances (PFAS) and Other Constituents in MSW Landfill Leachate from Puerto Rico.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 358: 142131, (2024).",
             "distribution": [
                 {
-                    "title": "Tables and Figures data from PR PFAS.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529916/Tables%20and%20Figures%20data%20from%20PR%20PFAS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tables and Figures data from PR PFAS.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529916",
+            "keyword": [
+                "Contamination",
+                "PFAS",
+                "leachate",
+                "landfills",
+                "Puerto Rico"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-01",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2024.142141"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197893,43 +197887,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2024.142141"
+            ],
+            "rights": null,
+            "title": "PFAS leachate concentrations in Puerto Rico Landfills"
         },
         {
-            "title": "Soybean microbiome response to CeO2 nanoparticles",
-            "description": "16S amplicon sequencing data used to determine the changes in the soybean root-associated microbiome in response to cerium oxide nanoparticles (CeNPs) in a natural soil. Samples include low (1 ppm) and high (100 ppm) concentrations of CeNPs, as well as pristine and aged CeNP treatments. These treatments were designed to assess how environmentally relevant concentrations of CeNPs affect soybean growth, and whether aging CeNPs changes the biological response. The 60 total samples are comprised of 4 experimental replicates from each of the 5 treatments, with 3 spatial compartments (of varying proximity to the root surface). \n\nThis dataset is associated with the following publication:\nReichman, J., M.R. Slattery, M.G. Johnson, C. Andersen, and S.L. Harper. CeO2 nanoparticle dose and exposure modulate soybean development and plant-mediated responses in root-associated bacterial communities.   Scientific Reports. Nature Publishing Group, London,  UK, 14: 10231, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504131",
-            "keyword": [
-                "ammonium nitrate",
-                "intergenerational effects",
-                "isotope",
-                "isotopic discrimination",
-                "nitrogen",
-                "engineered nanomaterials (ENMs)"
-            ],
             "contactPoint": {
                 "fn": "Christian Andersen",
                 "hasEmail": "mailto:andersen.christian@epa.gov"
             },
+            "description": "16S amplicon sequencing data used to determine the changes in the soybean root-associated microbiome in response to cerium oxide nanoparticles (CeNPs) in a natural soil. Samples include low (1 ppm) and high (100 ppm) concentrations of CeNPs, as well as pristine and aged CeNP treatments. These treatments were designed to assess how environmentally relevant concentrations of CeNPs affect soybean growth, and whether aging CeNPs changes the biological response. The 60 total samples are comprised of 4 experimental replicates from each of the 5 treatments, with 3 spatial compartments (of varying proximity to the root surface). \n\nThis dataset is associated with the following publication:\nReichman, J., M.R. Slattery, M.G. Johnson, C. Andersen, and S.L. Harper. CeO2 nanoparticle dose and exposure modulate soybean development and plant-mediated responses in root-associated bacterial communities.   Scientific Reports. Nature Publishing Group, London,  UK, 14: 10231, (2024).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA549519",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA549519"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA549519",
+                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA549519"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504131",
+            "keyword": [
+                "ammonium nitrate",
+                "intergenerational effects",
+                "isotope",
+                "isotopic discrimination",
+                "nitrogen",
+                "engineered nanomaterials (ENMs)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-04-07",
-            "references": [
-                "https://doi.org/10.1038/s41598-024-60344-8",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11068890"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197939,19 +197932,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-024-60344-8",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11068890"
+            ],
+            "rights": null,
+            "title": "Soybean microbiome response to CeO2 nanoparticles"
         },
         {
-            "title": "Effects of Age and Exposure Duration on the Sensitivity of Early Life Stage Fathead Minnow (Pimephales promelas) to Waterborne Propranolol Exposure",
-            "description": "Given that larval fish stages provide opportunities for development of stressor-selective screening level tests, this work aimed to investigate the optimal age of fathead minnow larva and duration of exposure for the pharmaceutical, propranolol, found in the environment. Differentially expressed genes were studied as well as gene set enrichment analysis. \n\nThis dataset is associated with the following publication:\nBiales, A., D. Bencic, R. Flick, and G. Toth. Effects of Age and Exposure Duration on the Sensitivity of Early Life Stage Fathead Minnow (Pimephales promelas) to Waterborne Propranolol Exposure.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(4): 807-820, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Adam Biales",
+                "hasEmail": "mailto:biales.adam@epa.gov"
+            },
+            "description": "Given that larval fish stages provide opportunities for development of stressor-selective screening level tests, this work aimed to investigate the optimal age of fathead minnow larva and duration of exposure for the pharmaceutical, propranolol, found in the environment. Differentially expressed genes were studied as well as gene set enrichment analysis. \n\nThis dataset is associated with the following publication:\nBiales, A., D. Bencic, R. Flick, and G. Toth. Effects of Age and Exposure Duration on the Sensitivity of Early Life Stage Fathead Minnow (Pimephales promelas) to Waterborne Propranolol Exposure.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(4): 807-820, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE197442",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE197442"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530882",
             "keyword": [
@@ -197961,19 +197964,10 @@
                 "gene expression",
                 "propranolol"
             ],
-            "contactPoint": {
-                "fn": "Adam Biales",
-                "hasEmail": "mailto:biales.adam@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE197442",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE197442"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-10-03",
-            "references": [
-                "https://doi.org/10.1002/etc.5814"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -197983,20 +197977,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5814"
+            ],
+            "rights": null,
+            "title": "Effects of Age and Exposure Duration on the Sensitivity of Early Life Stage Fathead Minnow (Pimephales promelas) to Waterborne Propranolol Exposure"
         },
         {
-            "title": "EPA Dynamically Downscaled Ensemble (EDDE), Version 1",
-            "description": "The EPA Dynamically Downscaled Ensemble (EDDE) datasets were prepared by EPA/ORD staff and by contract staff who worked under the technical guidance of EPA/ORD staff. The dataset here represents a subset of data that were dynamically downscaled by EPA from the fifth Coupled Model Intercomparison Project (CMIP5) using the Weather Research and Forecasting (WRF) model using the EPA High-End Scientific Computing platforms. Scenarios were downscaled from the Community Earth System Model (CESM) and the Geophysical Fluid Dynamics Laboratory (GFDL) Coupled Model version 3 (CM3). Simulations followed the historical periods 1975-2005 (CESM only) and 1995-2005 (both CESM and CM3), and Representative Concentration Pathways (RCP) 4.5 for 2025-2100 (CESM only), RCP6.0 for 2025-2055 (CESM only), and RCP8.5 for 2025-2100 (both CESM and CM3). The original downscaling was conducted during 2013-2018. Subsets of the original dataset were prepared using postprocessing software developed by EPA/ORD staff. This dataset is not publicly accessible because: Dataset is too large to be hosted in ScienceHub. It is ~5 terabytes. It can be accessed through the following means: Ideally, this dataset will be publicly accessible from the Cloud. Negotiations are underway to support that hosting venue. Format: Data are in Network Common Data Form (netCDF; https://unidata.ucar.edu/software/netcdf) version 4, which is commonly used and consumed by practitioners in the atmospheric modeling community. The EDDE data in netCDF are further written to adhere to principles of Climate and Forecasting System (CF) Compliance, as outlined at https://cfconventions.org. The files to be hosted are self-describing with metadata included in the netCDF header.",
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
+                "fn": "Tanya Spero",
+                "hasEmail": "mailto:spero.tanya@epa.gov"
+            },
+            "description": "The EPA Dynamically Downscaled Ensemble (EDDE) datasets were prepared by EPA/ORD staff and by contract staff who worked under the technical guidance of EPA/ORD staff. The dataset here represents a subset of data that were dynamically downscaled by EPA from the fifth Coupled Model Intercomparison Project (CMIP5) using the Weather Research and Forecasting (WRF) model using the EPA High-End Scientific Computing platforms. Scenarios were downscaled from the Community Earth System Model (CESM) and the Geophysical Fluid Dynamics Laboratory (GFDL) Coupled Model version 3 (CM3). Simulations followed the historical periods 1975-2005 (CESM only) and 1995-2005 (both CESM and CM3), and Representative Concentration Pathways (RCP) 4.5 for 2025-2100 (CESM only), RCP6.0 for 2025-2055 (CESM only), and RCP8.5 for 2025-2100 (both CESM and CM3). The original downscaling was conducted during 2013-2018. Subsets of the original dataset were prepared using postprocessing software developed by EPA/ORD staff. This dataset is not publicly accessible because: Dataset is too large to be hosted in ScienceHub. It is ~5 terabytes. It can be accessed through the following means: Ideally, this dataset will be publicly accessible from the Cloud. Negotiations are underway to support that hosting venue. Format: Data are in Network Common Data Form (netCDF; https://unidata.ucar.edu/software/netcdf) version 4, which is commonly used and consumed by practitioners in the atmospheric modeling community. The EDDE data in netCDF are further written to adhere to principles of Climate and Forecasting System (CF) Compliance, as outlined at https://cfconventions.org. The files to be hosted are self-describing with metadata included in the netCDF header.",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530964",
             "keyword": [
                 "climate change",
@@ -198005,13 +198003,11 @@
                 "regional climate",
                 "WRF"
             ],
-            "contactPoint": {
-                "fn": "Tanya Spero",
-                "hasEmail": "mailto:spero.tanya@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-05-07",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -198020,41 +198016,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "EPA Dynamically Downscaled Ensemble (EDDE), Version 1"
         },
         {
-            "title": "A comparison of machine learning approaches for predicting hepatotoxicity potential using chemical structure and targeted transcriptomic data",
-            "description": "Supplementary data for \"Tia Tate, Grace Patlewicz, Imran Shah,\nA comparison of machine learning approaches for predicting hepatotoxicity potential using chemical structure and targeted transcriptomic data, Computational Toxicology, Volume 29,  2024, 100301, ISSN 2468-1113, https://doi.org/10.1016/j.comtox.2024.100301.\". \n\nThis dataset is associated with the following publication:\nTate, T., G. Patlewicz, and I. Shah. A comparison of machine learning approaches for predicting hepatotoxicity potential using chemical structure and targeted transcriptomic data.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 29: 100301, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530883",
-            "keyword": [
-                "machine learning",
-                "ToxRefDB",
-                "HTTr",
-                "GenRA"
-            ],
             "contactPoint": {
                 "fn": "Grace Patlewicz",
                 "hasEmail": "mailto:patlewicz.grace@epa.gov"
             },
+            "description": "Supplementary data for \"Tia Tate, Grace Patlewicz, Imran Shah,\nA comparison of machine learning approaches for predicting hepatotoxicity potential using chemical structure and targeted transcriptomic data, Computational Toxicology, Volume 29,  2024, 100301, ISSN 2468-1113, https://doi.org/10.1016/j.comtox.2024.100301.\". \n\nThis dataset is associated with the following publication:\nTate, T., G. Patlewicz, and I. Shah. A comparison of machine learning approaches for predicting hepatotoxicity potential using chemical structure and targeted transcriptomic data.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 29: 100301, (2024).",
             "distribution": [
                 {
-                    "title": "1-s2.0-S2468111324000033-mmc1.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530883/1-s2.0-S2468111324000033-mmc1.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "1-s2.0-S2468111324000033-mmc1.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530883",
+            "keyword": [
+                "machine learning",
+                "ToxRefDB",
+                "HTTr",
+                "GenRA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-02-04",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2024.100301"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198064,40 +198058,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2024.100301"
+            ],
+            "rights": null,
+            "title": "A comparison of machine learning approaches for predicting hepatotoxicity potential using chemical structure and targeted transcriptomic data"
         },
         {
-            "title": "Mussel test methods development",
-            "description": "Additional data generated during the present study are available as a US Geological Survey data release at https://doi.org/XXXX (pending). \n\nThis dataset is associated with the following publication:\nWang, N., J. Kunz, D. Cleveland, R. Dorman, J. Steevens, S. Raimondo, T. Augsberger, and C. Barnhardt. Evaluation of Chronic Effects of Potassium Chloride and Nickel on Survival, Growth, and Reproduction of a Unionid Mussel (Lampsilis siliquoidea).   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(5): 1097\u20131111, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529596",
-            "keyword": [
-                "freshwater mussels",
-                "chronic toxicity",
-                "Methods development",
-                "aquatic toxicity"
-            ],
             "contactPoint": {
                 "fn": "Sandra Raimondo",
                 "hasEmail": "mailto:raimondo.sandy@epa.gov"
             },
+            "description": "Additional data generated during the present study are available as a US Geological Survey data release at https://doi.org/XXXX (pending). \n\nThis dataset is associated with the following publication:\nWang, N., J. Kunz, D. Cleveland, R. Dorman, J. Steevens, S. Raimondo, T. Augsberger, and C. Barnhardt. Evaluation of Chronic Effects of Potassium Chloride and Nickel on Survival, Growth, and Reproduction of a Unionid Mussel (Lampsilis siliquoidea).   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 43(5): 1097\u20131111, (2024).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.5066/P9Z2M6QL.",
-                    "accessURL": "https://doi.org/10.5066/P9Z2M6QL."
+                    "accessURL": "https://doi.org/10.5066/P9Z2M6QL.",
+                    "title": "https://doi.org/10.5066/P9Z2M6QL."
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529596",
+            "keyword": [
+                "freshwater mussels",
+                "chronic toxicity",
+                "Methods development",
+                "aquatic toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-16",
-            "references": [
-                "https://doi.org/10.1002/etc.5843"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198107,19 +198101,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5843"
+            ],
+            "rights": null,
+            "title": "Mussel test methods development"
         },
         {
-            "title": "FKastury JHazMat XAS and SEM data",
-            "description": "Includes all data collected by the US EPA; X-ray absorption spectroscopy (XAS) data on the Lead L3-edge and the Arsenic K-edge and Scanning Electron Microscopy with paired energy dispersive X-ray spectroscopy (EDS) at select spots. \n\nThis dataset is associated with the following publication:\nKastury, F., J. Basedin, A.R. Betts, R. Asamoah, C. Herde, P. Netherway, J. Tully, K.G. Scheckel, and A.L. Juhasz. Arsenic, cadmium, lead, antimony bioaccessibility and relative bioavailability in legacy gold mining waste.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 469: 133948, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Aaron Betts",
+                "hasEmail": "mailto:betts.aaron@epa.gov"
+            },
+            "description": "Includes all data collected by the US EPA; X-ray absorption spectroscopy (XAS) data on the Lead L3-edge and the Arsenic K-edge and Scanning Electron Microscopy with paired energy dispersive X-ray spectroscopy (EDS) at select spots. \n\nThis dataset is associated with the following publication:\nKastury, F., J. Basedin, A.R. Betts, R. Asamoah, C. Herde, P. Netherway, J. Tully, K.G. Scheckel, and A.L. Juhasz. Arsenic, cadmium, lead, antimony bioaccessibility and relative bioavailability in legacy gold mining waste.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 469: 133948, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530970/FKastury%20JHazMat%20data.zip",
+                    "mediaType": "application/zip",
+                    "title": "FKastury JHazMat data.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530970",
             "keyword": [
@@ -198131,20 +198135,10 @@
                 "synchrotron speciation",
                 "Gold mining"
             ],
-            "contactPoint": {
-                "fn": "Aaron Betts",
-                "hasEmail": "mailto:betts.aaron@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "FKastury JHazMat data.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530970/FKastury%20JHazMat%20data.zip",
-                    "mediaType": "application/zip"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-01",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2024.133948"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198154,108 +198148,107 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2024.133948"
+            ],
+            "rights": null,
+            "title": "FKastury JHazMat XAS and SEM data"
         },
         {
-            "title": "Data for manuscript Neutralization of Ricin Toxin on Building Interior Surfaces Using Liquid Decontaminants",
-            "description": "These are the raw data underlying the data presented in the manuscript. \n\nThis dataset is associated with the following publication:\nRichter, W., B. Weston, M. Sunderman, Z. Willenberg, K. Ratliff, and J. Wood. Neutralization of Ricin Toxin on Building Interior Surfaces using Liquid Decontaminants.   PLOS ONE. Public Library of Science, San Francisco, CA, USA, 19(5): e0302967, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529431",
-            "keyword": [
-                "Ricin",
-                "Decontamination",
-                "homeland security",
-                "emergency response",
-                "Contaminated Sites"
-            ],
             "contactPoint": {
                 "fn": "Joseph Wood",
                 "hasEmail": "mailto:wood.joe@epa.gov"
             },
+            "description": "These are the raw data underlying the data presented in the manuscript. \n\nThis dataset is associated with the following publication:\nRichter, W., B. Weston, M. Sunderman, Z. Willenberg, K. Ratliff, and J. Wood. Neutralization of Ricin Toxin on Building Interior Surfaces using Liquid Decontaminants.   PLOS ONE. Public Library of Science, San Francisco, CA, USA, 19(5): e0302967, (2024).",
             "distribution": [
                 {
-                    "title": "Repeated_H2O2_Minncare_30m_Results-ZJWedits.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Repeated_H2O2_Minncare_30m_Results-ZJWedits.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Repeated_H2O2_Minncare_30m_Results-ZJWedits.xlsx"
                 },
                 {
-                    "title": "Repeat_3% H2O2_60_120m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Repeat_3%25%20H2O2_60_120m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Repeat_3% H2O2_60_120m_Results.xlsx"
                 },
                 {
-                    "title": "Oxyclean_60_120m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Oxyclean_60_120m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Oxyclean_60_120m_Results.xlsx"
                 },
                 {
-                    "title": "Minncare_15_60m_Results-ZJW comments.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Minncare_15_60m_Results-ZJW%20comments.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Minncare_15_60m_Results-ZJW comments.xlsx"
                 },
                 {
-                    "title": "Formula409_60_120m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Formula409_60_120m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Formula409_60_120m_Results.xlsx"
                 },
                 {
-                    "title": "Formula_409_30m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Formula_409_30m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Formula_409_30m_Results.xlsx"
                 },
                 {
-                    "title": "Clorox_Oxyclean_30m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Clorox_Oxyclean_30m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Clorox_Oxyclean_30m_Results.xlsx"
                 },
                 {
-                    "title": "Clorox_7500ppm_30m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Clorox_7500ppm_30m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Clorox_7500ppm_30m_Results.xlsx"
                 },
                 {
-                    "title": "Clorox_20Kppm_30m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Clorox_20Kppm_30m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Clorox_20Kppm_30m_Results.xlsx"
                 },
                 {
-                    "title": "Clorox 7500_60_120m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Clorox%207500_60_120m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Clorox 7500_60_120m_Results.xlsx"
                 },
                 {
-                    "title": "Clorox 1000ppm_60_120m_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Clorox%201000ppm_60_120m_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Clorox 1000ppm_60_120m_Results.xlsx"
                 },
                 {
-                    "title": "20K Clorox_60m_120m_Results-ZJW comments.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/20K%20Clorox_60m_120m_Results-ZJW%20comments.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20K Clorox_60m_120m_Results-ZJW comments.xlsx"
                 },
                 {
-                    "title": "Data Explanation.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Data%20Explanation.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Explanation.xlsx"
                 },
                 {
-                    "title": "Read me first data dictionary.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529431/Read%20me%20first%20data%20dictionary.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Read me first data dictionary.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529431",
+            "keyword": [
+                "Ricin",
+                "Decontamination",
+                "homeland security",
+                "emergency response",
+                "Contaminated Sites"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-21",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0302967",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11081333"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198265,19 +198258,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0302967",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11081333"
+            ],
+            "rights": null,
+            "title": "Data for manuscript Neutralization of Ricin Toxin on Building Interior Surfaces Using Liquid Decontaminants"
         },
         {
-            "title": "Smoot et al_Burn pit developmental data",
-            "description": "Raw data for Smoot et al Burn pit manuscript. \n\nThis dataset is associated with the following publication:\nSmoot, J., S. Padilla, Y.H. Kim, D. Hunter, A. Tennant, B. Hill, M. Lowery, B. Knapp, W. Oshiro, M. Hazari, M. Hays, W. Preston, i. Jaspers, M. Gilmour, and A. Farraj. Burn pit-related smoke causes developmental and behavioral toxicity in zebrafish: Influence of material type and emissions chemistry.   Heliyon. Elsevier B.V., Amsterdam,  NETHERLANDS, 10(8): e29675, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Aimen Farraj",
+                "hasEmail": "mailto:farraj.aimen@epa.gov"
+            },
+            "description": "Raw data for Smoot et al Burn pit manuscript. \n\nThis dataset is associated with the following publication:\nSmoot, J., S. Padilla, Y.H. Kim, D. Hunter, A. Tennant, B. Hill, M. Lowery, B. Knapp, W. Oshiro, M. Hazari, M. Hays, W. Preston, i. Jaspers, M. Gilmour, and A. Farraj. Burn pit-related smoke causes developmental and behavioral toxicity in zebrafish: Influence of material type and emissions chemistry.   Heliyon. Elsevier B.V., Amsterdam,  NETHERLANDS, 10(8): e29675, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530967/Smoot%20et%20al_Supplementary%20File%202_Data_1-18-24.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Smoot et al_Supplementary File 2_Data_1-18-24.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530967",
             "keyword": [
@@ -198290,21 +198294,10 @@
                 "behavior",
                 "malformations"
             ],
-            "contactPoint": {
-                "fn": "Aimen Farraj",
-                "hasEmail": "mailto:farraj.aimen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Smoot et al_Supplementary File 2_Data_1-18-24.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530967/Smoot%20et%20al_Supplementary%20File%202_Data_1-18-24.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-01-18",
-            "references": [
-                "https://doi.org/10.1016/j.heliyon.2024.e29675",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11053193"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198314,34 +198307,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.heliyon.2024.e29675",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11053193"
+            ],
+            "rights": null,
+            "title": "Smoot et al_Burn pit developmental data"
         },
         {
-            "title": "Data Description for Risk of Dementia Due to Co-Exposure to Air Pollution and Neighborhood Disadvantage",
-            "description": "This dataset contains information on air pollution exposure, social determinants of health, dementia outcomes, and related confounders from the National Health and Aging Trends Study. This dataset is not publicly accessible because: This data was not produced by the EPA and is not owned by the EPA. It can be accessed through the following means: The data can be accessed by contacting the corresponding author listed in the manuscript. Format: The data is in tabular format with rows corresponding to observations and columns corresponding to outcomes, confounders, and exposures. \n\nThis dataset is associated with the following publication:\nFrndak, S., Z. Deng, C. Ward-Caviness, I. Gorski-Steiner, R. Thorpe, and A. Dickerson. Risk of Dementia Due to Co-Exposure to Air Pollution and Neighborhood Disadvantage.   ENVIRONMENTAL RESEARCH. Elsevier B.V., Amsterdam,  NETHERLANDS, 251(Part 2): 118709, (2024).",
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
+                "fn": "Cavin Ward-Caviness",
+                "hasEmail": "mailto:ward-caviness.cavin@epa.gov"
+            },
+            "description": "This dataset contains information on air pollution exposure, social determinants of health, dementia outcomes, and related confounders from the National Health and Aging Trends Study. This dataset is not publicly accessible because: This data was not produced by the EPA and is not owned by the EPA. It can be accessed through the following means: The data can be accessed by contacting the corresponding author listed in the manuscript. Format: The data is in tabular format with rows corresponding to observations and columns corresponding to outcomes, confounders, and exposures. \n\nThis dataset is associated with the following publication:\nFrndak, S., Z. Deng, C. Ward-Caviness, I. Gorski-Steiner, R. Thorpe, and A. Dickerson. Risk of Dementia Due to Co-Exposure to Air Pollution and Neighborhood Disadvantage.   ENVIRONMENTAL RESEARCH. Elsevier B.V., Amsterdam,  NETHERLANDS, 251(Part 2): 118709, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1530960",
             "keyword": [
                 "Dementia",
                 "air pollution",
                 "Aging"
             ],
-            "contactPoint": {
-                "fn": "Cavin Ward-Caviness",
-                "hasEmail": "mailto:ward-caviness.cavin@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2024-03-15",
-            "references": [
-                "https://doi.org/10.1016/j.envres.2024.118709"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198351,20 +198345,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envres.2024.118709"
+            ],
+            "rights": null,
+            "title": "Data Description for Risk of Dementia Due to Co-Exposure to Air Pollution and Neighborhood Disadvantage"
         },
         {
-            "title": "Historical Case Studies for Coatings",
-            "description": "Data present in references cited are in graphs, tables, and/or text. This dataset is not publicly accessible because: Data are publicly available in the references cited. It can be accessed through the following means: Accessing the references. Format: Journal articles (references for the review article) contain data on which percent efficiencies (when presented in the manuscript) were calculated. \n\nThis dataset is associated with the following publication:\nButler, B.A., and L.E. Brase. Critical Review of Field Studies of Chemical Surface Coatings to Mitigate Leaching from Mining Wastes.   Mine Water and the Environment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 43: 03-15, (2024).",
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
+                "fn": "Barbara Butler",
+                "hasEmail": "mailto:butler.barbara@epa.gov"
+            },
+            "description": "Data present in references cited are in graphs, tables, and/or text. This dataset is not publicly accessible because: Data are publicly available in the references cited. It can be accessed through the following means: Accessing the references. Format: Journal articles (references for the review article) contain data on which percent efficiencies (when presented in the manuscript) were calculated. \n\nThis dataset is associated with the following publication:\nButler, B.A., and L.E. Brase. Critical Review of Field Studies of Chemical Surface Coatings to Mitigate Leaching from Mining Wastes.   Mine Water and the Environment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 43: 03-15, (2024).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529127",
             "keyword": [
                 "Passivation",
@@ -198372,14 +198370,10 @@
                 "source control",
                 "microencapsulation"
             ],
-            "contactPoint": {
-                "fn": "Barbara Butler",
-                "hasEmail": "mailto:butler.barbara@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-01",
-            "references": [
-                "https://doi.org/10.1007/s10230-024-00973-7"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198389,19 +198383,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10230-024-00973-7"
+            ],
+            "rights": null,
+            "title": "Historical Case Studies for Coatings"
         },
         {
-            "title": "UEFW-ConstructedWetlands_MSDataFile_17Jul2023.xlsx",
-            "description": "Watershed flow and nutrient species measured data for model calibration, Edge-of-field wetland demonstration project flow monitoring and water quality sampling data for assessing treatment performance; UEFW SWAT Model HRU subbasin output for ACPF sited NRWs; summary cost effectiveness results and parameters used in calculating cost effectiveness. \n\nThis dataset is associated with the following publication:\nNietch, C., B. Hawley, A. Safwat, J. Christensen, M. Heberling, J. McManus, R. McClatchey, H. Lubbers, N. Smucker, E. Onderak, and S. Macy. Implementing constructed wetlands for nutrient reduction at watershed scale: Opportunity to link models and real-world execution.   JOURNAL OF SOIL AND WATER CONSERVATION. Soil and Water Conservation Society,    79(3): 113-131, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Christopher Nietch",
+                "hasEmail": "mailto:nietch.christopher@epa.gov"
+            },
+            "description": "Watershed flow and nutrient species measured data for model calibration, Edge-of-field wetland demonstration project flow monitoring and water quality sampling data for assessing treatment performance; UEFW SWAT Model HRU subbasin output for ACPF sited NRWs; summary cost effectiveness results and parameters used in calculating cost effectiveness. \n\nThis dataset is associated with the following publication:\nNietch, C., B. Hawley, A. Safwat, J. Christensen, M. Heberling, J. McManus, R. McClatchey, H. Lubbers, N. Smucker, E. Onderak, and S. Macy. Implementing constructed wetlands for nutrient reduction at watershed scale: Opportunity to link models and real-world execution.   JOURNAL OF SOIL AND WATER CONSERVATION. Soil and Water Conservation Society,    79(3): 113-131, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529278/UEFW-ConstructedWetlands_MSDataFile_17Jul2023.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "UEFW-ConstructedWetlands_MSDataFile_17Jul2023.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529278",
             "keyword": [
@@ -198415,20 +198419,10 @@
                 "edge-of-field wetland demonstration data",
                 "parameters for cost effectiveness calculations"
             ],
-            "contactPoint": {
-                "fn": "Christopher Nietch",
-                "hasEmail": "mailto:nietch.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "UEFW-ConstructedWetlands_MSDataFile_17Jul2023.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529278/UEFW-ConstructedWetlands_MSDataFile_17Jul2023.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-17",
-            "references": [
-                "https://doi.org/10.2489/jswc.2024.00077"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198438,40 +198432,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2489/jswc.2024.00077"
+            ],
+            "rights": null,
+            "title": "UEFW-ConstructedWetlands_MSDataFile_17Jul2023.xlsx"
         },
         {
-            "title": "Improving predictions of compound amenability for liquid chromatography-mass spectrometry to enhance non-targeted analysis",
-            "description": "Twelve supplementary files from the manuscript \"Improving predictions of compound amenability for liquid chromatography-mass spectrometry to enhance non-targeted analysis\".",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530975",
-            "keyword": [
-                "mass spectrometry",
-                "non-targeted analysis",
-                "Predictive Modeling",
-                "Suspect screening analysis."
-            ],
             "contactPoint": {
                 "fn": "Nathaniel Charest",
                 "hasEmail": "mailto:charest.nathaniel@epa.gov"
             },
+            "description": "Twelve supplementary files from the manuscript \"Improving predictions of compound amenability for liquid chromatography-mass spectrometry to enhance non-targeted analysis\".",
             "distribution": [
                 {
-                    "title": "216_2024_5229_MOESM_ESM.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530975/216_2024_5229_MOESM_ESM.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "216_2024_5229_MOESM_ESM.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530975",
+            "keyword": [
+                "mass spectrometry",
+                "non-targeted analysis",
+                "Predictive Modeling",
+                "Suspect screening analysis."
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-26",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -198480,48 +198476,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Improving predictions of compound amenability for liquid chromatography-mass spectrometry to enhance non-targeted analysis"
         },
         {
-            "title": "A systematic analysis of read-across within REACH registration dossiers",
-            "description": "G. Patlewicz, P. Karamertzanis, K. Paul Friedman, M. Sannicola, I. Shah, A systematic analysis of read-across within REACH registration dossiers, Computational Toxicology, Volume 30, 2024, 100304, ISSN 2468-1113, https://doi.org/10.1016/j.comtox.2024.100304",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530988",
-            "keyword": [
-                "ToxValDB",
-                "GenRA",
-                "ECHA",
-                "Reach"
-            ],
             "contactPoint": {
                 "fn": "Grace Patlewicz",
                 "hasEmail": "mailto:patlewicz.grace@epa.gov"
             },
+            "description": "G. Patlewicz, P. Karamertzanis, K. Paul Friedman, M. Sannicola, I. Shah, A systematic analysis of read-across within REACH registration dossiers, Computational Toxicology, Volume 30, 2024, 100304, ISSN 2468-1113, https://doi.org/10.1016/j.comtox.2024.100304",
             "distribution": [
                 {
-                    "title": "https://github.com/patlewig/read-across/",
-                    "accessURL": "https://github.com/patlewig/read-across/"
+                    "accessURL": "https://github.com/patlewig/read-across/",
+                    "title": "https://github.com/patlewig/read-across/"
                 },
                 {
-                    "title": "https://doi.org/10.23645/epacomptox.25343383",
-                    "accessURL": "https://doi.org/10.23645/epacomptox.25343383"
+                    "accessURL": "https://doi.org/10.23645/epacomptox.25343383",
+                    "title": "https://doi.org/10.23645/epacomptox.25343383"
                 },
                 {
-                    "title": "1-s2.0-S2468111324000069-mmc1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530988/1-s2.0-S2468111324000069-mmc1.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "1-s2.0-S2468111324000069-mmc1.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530988",
+            "keyword": [
+                "ToxValDB",
+                "GenRA",
+                "ECHA",
+                "Reach"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-02-27",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -198530,45 +198526,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "A systematic analysis of read-across within REACH registration dossiers"
         },
         {
-            "title": "Systematic Approaches for the Encoding of Chemical Groups: A Case Study",
-            "description": "The Supporting Information contains the following material: data set with ARN groups downloaded from https://echa.europa.eu/assessment-regulatory-needs in Feb 2023 (S1_2023_02_03_assessment-of-regulatory-needs--arn\u2500export.xlsx)\n\nCurated data set with ARN groups with molecular structures and their quality scores, that was used for building the models (S2_ARN_groups.xlsx)\n\nDescriptive statistics for the 86 substance groups (S3_ARN_stats.xlsx). For each group, we provide the number of substances as in the ARN group, the number of substances matched in DSSTox, the DSSTox substance type and the number of substances with structural information and its quality; document with additional figures and explanations referred to in the manuscript (S4_SystematicGroupingSI.docx)\n\nPredicted groups, probabilities and domain assessment for all nonconfidential substances registered under REACH (S5_rf_application_1_results_redacted.xlsx); Cross-validation scoring results obtained in every iteration of outer and inner grid search for the random forest (RF) model (S6_outer_inner_grid_details_rf.xlsx)\n\nCross-validation scoring results obtained in every iteration of outer and inner grid search for the nearest neighbor (kNN) model (S7_outer_inner_grid_details_kn.xlsx)\n\nCross-validation scoring results obtained for the gradient boosting (GB) model. This data set is only provided for completeness because the GB model was evaluated but not used further. Due to the computational cost, we only performed the inner grid search using the optimal fingerprint parameters identified by the outer grid search with kNN and RF (radius 2, length 2,560) (S8_outer_inner_grid_details_gb.xlsx) (ZIP)",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530990",
-            "keyword": [
-                "DSSTox",
-                "categories",
-                "TSCA",
-                "ECHA",
-                "Reach"
-            ],
             "contactPoint": {
                 "fn": "Grace Patlewicz",
                 "hasEmail": "mailto:patlewicz.grace@epa.gov"
             },
+            "description": "The Supporting Information contains the following material: data set with ARN groups downloaded from https://echa.europa.eu/assessment-regulatory-needs in Feb 2023 (S1_2023_02_03_assessment-of-regulatory-needs--arn\u2500export.xlsx)\n\nCurated data set with ARN groups with molecular structures and their quality scores, that was used for building the models (S2_ARN_groups.xlsx)\n\nDescriptive statistics for the 86 substance groups (S3_ARN_stats.xlsx). For each group, we provide the number of substances as in the ARN group, the number of substances matched in DSSTox, the DSSTox substance type and the number of substances with structural information and its quality; document with additional figures and explanations referred to in the manuscript (S4_SystematicGroupingSI.docx)\n\nPredicted groups, probabilities and domain assessment for all nonconfidential substances registered under REACH (S5_rf_application_1_results_redacted.xlsx); Cross-validation scoring results obtained in every iteration of outer and inner grid search for the random forest (RF) model (S6_outer_inner_grid_details_rf.xlsx)\n\nCross-validation scoring results obtained in every iteration of outer and inner grid search for the nearest neighbor (kNN) model (S7_outer_inner_grid_details_kn.xlsx)\n\nCross-validation scoring results obtained for the gradient boosting (GB) model. This data set is only provided for completeness because the GB model was evaluated but not used further. Due to the computational cost, we only performed the inner grid search using the optimal fingerprint parameters identified by the outer grid search with kNN and RF (radius 2, length 2,560) (S8_outer_inner_grid_details_gb.xlsx) (ZIP)",
             "distribution": [
                 {
-                    "title": "Supporting Information.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530990/Supporting%20Information.zip",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supporting Information.zip"
                 },
                 {
-                    "title": "https://github.com/pkaramertzanis/regulatory_grouping",
-                    "accessURL": "https://github.com/pkaramertzanis/regulatory_grouping"
+                    "accessURL": "https://github.com/pkaramertzanis/regulatory_grouping",
+                    "title": "https://github.com/pkaramertzanis/regulatory_grouping"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530990",
+            "keyword": [
+                "DSSTox",
+                "categories",
+                "TSCA",
+                "ECHA",
+                "Reach"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-01",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -198577,19 +198573,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Systematic Approaches for the Encoding of Chemical Groups: A Case Study"
         },
         {
-            "title": "Virginia Site A Database",
-            "description": "The dataset is comprised of: 1)VOC concentrations of soil gas and indoor air samples collected over the site; 2) the pressure readings used to monitor the pressure differential between subslab and indoor air. \n\nThis dataset is associated with the following publication:\nLutes, C., V. Boyd, G. Buckley, L. Levy, K. Bronstein, J. Zimmerman, A. Williams, and B. Schumacher. Impact of Hurricanes, Tropical Storms, and Coastal Extratropical Storms on Indoor Air VOC Concentrations.   Groundwater Monitoring & Remediation. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 44(2): 101-117, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Zimmerman",
+                "hasEmail": "mailto:zimmerman.johnh@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529536/documents/Data%20dictionary%20can%20be%20found%20in%20supplemental%20data%20in%20supporting%20document%20section.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The dataset is comprised of: 1)VOC concentrations of soil gas and indoor air samples collected over the site; 2) the pressure readings used to monitor the pressure differential between subslab and indoor air. \n\nThis dataset is associated with the following publication:\nLutes, C., V. Boyd, G. Buckley, L. Levy, K. Bronstein, J. Zimmerman, A. Williams, and B. Schumacher. Impact of Hurricanes, Tropical Storms, and Coastal Extratropical Storms on Indoor Air VOC Concentrations.   Groundwater Monitoring & Remediation. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 44(2): 101-117, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1111/gwmr.12642",
+                    "title": "https://doi.org/10.1111/gwmr.12642"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529536",
             "keyword": [
@@ -198599,20 +198604,10 @@
                 "vapor intrusion",
                 "radon"
             ],
-            "contactPoint": {
-                "fn": "John Zimmerman",
-                "hasEmail": "mailto:zimmerman.johnh@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1111/gwmr.12642",
-                    "accessURL": "https://doi.org/10.1111/gwmr.12642"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-07-12",
-            "references": [
-                "https://doi.org/10.1111/gwmr.12642",
-                "https://pasteur.epa.gov/uploads/10.23719/1529536/documents/gwmr12642-sup-0001-supinfo.docx"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198623,43 +198618,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529536/documents/Data%20dictionary%20can%20be%20found%20in%20supplemental%20data%20in%20supporting%20document%20section.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1111/gwmr.12642",
+                "https://pasteur.epa.gov/uploads/10.23719/1529536/documents/gwmr12642-sup-0001-supinfo.docx"
+            ],
+            "rights": null,
+            "title": "Virginia Site A Database"
         },
         {
-            "title": "Occurrence of Recreational Water Quality Monitoring General Fecal Indicator Bacteria and Fecal Source Identification Genetic Markers in Gray Seal Scat",
-            "description": "Data set consists of qPCR measurements for fecal indicator bacteria genetic markers reported in Figure 2. \n\nThis dataset is associated with the following publication:\nPaar, J., J. Willis, L. Sette, S.A. Wood, A. Bogomolni, M. Dulac, M. Sivaganesan, and O. Shanks. Occurrence of recreational water quality monitoring general fecal indicator bacteria and fecal source identification genetic markers in gray seal scat.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 934: 173220, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529743",
-            "keyword": [
-                "micorbial source tracking",
-                "qPCR",
-                "fecal indicator bacteria",
-                "gray seal",
-                "Microbial Source Tracking"
-            ],
             "contactPoint": {
                 "fn": "Orin Shanks",
                 "hasEmail": "mailto:shanks.orin@epa.gov"
             },
+            "description": "Data set consists of qPCR measurements for fecal indicator bacteria genetic markers reported in Figure 2. \n\nThis dataset is associated with the following publication:\nPaar, J., J. Willis, L. Sette, S.A. Wood, A. Bogomolni, M. Dulac, M. Sivaganesan, and O. Shanks. Occurrence of recreational water quality monitoring general fecal indicator bacteria and fecal source identification genetic markers in gray seal scat.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 934: 173220, (2024).",
             "distribution": [
                 {
-                    "title": "Paar etal 20xx_ Gray Seal FIB data set.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529743/Paar%20etal%2020xx_%20Gray%20Seal%20FIB%20data%20set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Paar etal 20xx_ Gray Seal FIB data set.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529743",
+            "keyword": [
+                "micorbial source tracking",
+                "qPCR",
+                "fecal indicator bacteria",
+                "gray seal",
+                "Microbial Source Tracking"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-21",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2024.173220"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198669,41 +198663,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2024.173220"
+            ],
+            "rights": null,
+            "title": "Occurrence of Recreational Water Quality Monitoring General Fecal Indicator Bacteria and Fecal Source Identification Genetic Markers in Gray Seal Scat"
         },
         {
-            "title": "Datasets for manuscript: Phosphorus recovery in municipal wastewater and socioeconomic impacts in Canada and the United States",
-            "description": "The datasets contain the computer code and data required to determine the cost and economic impacts of phosphorus recovery from municipal wastewater in Canada and the United States. The datasets supply data to (i) calculate the efficiency and cost of phosphorus recovery from the aqueous phase of digestate and sewage sludge for wastewater resource recovery facilities (WRRFs) as shown in Figure 1; (ii) estimate the average annual per capita phosphorus recovery cost and the household affordability index (HAI) across the second-level territory divisions (census divisions (Canada) and counties (United States)) when excluding and including the offset cost derived from avoiding potential environmental damage caused by phosphorus releases as shown in Figure 2; (iii) supply the distribution of population in urban and rural areas, the treatment level of the WRRFs, and the phosphorus recovery points as a function of the WRRF scale in the studied regions of Canada and the United States as shown in Figure 3; and (iv) describe the distribution of the average phosphorus recovery cost, annual per capita phosphorus recovery costs, and the HAI per studied regions as shown in Figure 4.  \n\nData describing the WRRFs\u2019 location and characteristics across the studied regions of Canada and the United States are retrieved from the HydroWASTE database (https://www.hydrosheds.org/products/hydrowaste), including their spatial coordinates, treatment level, treatment design capacity, and population served. The HydroWASTE database reports the WRRF treatment level as primary, secondary, and advanced treatment. Since the U.S. Environmental Protection Agency does not define numeric nutrient water quality criteria for secondary wastewater treatment effluents, we consider that only the WRRFs with advanced treatments have specific processes for removing phosphorus from the liquid effluent.\n\nTo perform the analysis at the second-level divisions, data on total population, distribution of population in urban and rural areas, total income, and average annual income per capita are retrieved at the census division and county level for Canada and the United States, respectively. Data for the year 2020 is considered since it is the most recent information available for both countries. The first-level divisions level corresponds to census divisions of the United States, which provide territorial divisions similar in terms of development, demographic characteristics, and economic activities, being extensively used for collecting and analyzing data throughout the United States. A table of the states included in each United States census division can be found in the Supplementary Information file. The equivalent of the United States census divisions for Canada is the Canadian provinces and territories, although it must be noted that, unlike the case of the United States, their definition is guided by administrative and political considerations instead of statistical criteria.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530881",
-            "keyword": [
-                "nutrient pollution",
-                "Phosphorus recovery",
-                "Social impact",
-                "Wastewater Resource Recovery Facilities"
-            ],
             "contactPoint": {
                 "fn": "Gerardo Ruiz-Mercado",
                 "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
             },
+            "description": "The datasets contain the computer code and data required to determine the cost and economic impacts of phosphorus recovery from municipal wastewater in Canada and the United States. The datasets supply data to (i) calculate the efficiency and cost of phosphorus recovery from the aqueous phase of digestate and sewage sludge for wastewater resource recovery facilities (WRRFs) as shown in Figure 1; (ii) estimate the average annual per capita phosphorus recovery cost and the household affordability index (HAI) across the second-level territory divisions (census divisions (Canada) and counties (United States)) when excluding and including the offset cost derived from avoiding potential environmental damage caused by phosphorus releases as shown in Figure 2; (iii) supply the distribution of population in urban and rural areas, the treatment level of the WRRFs, and the phosphorus recovery points as a function of the WRRF scale in the studied regions of Canada and the United States as shown in Figure 3; and (iv) describe the distribution of the average phosphorus recovery cost, annual per capita phosphorus recovery costs, and the HAI per studied regions as shown in Figure 4.  \n\nData describing the WRRFs\u2019 location and characteristics across the studied regions of Canada and the United States are retrieved from the HydroWASTE database (https://www.hydrosheds.org/products/hydrowaste), including their spatial coordinates, treatment level, treatment design capacity, and population served. The HydroWASTE database reports the WRRF treatment level as primary, secondary, and advanced treatment. Since the U.S. Environmental Protection Agency does not define numeric nutrient water quality criteria for secondary wastewater treatment effluents, we consider that only the WRRFs with advanced treatments have specific processes for removing phosphorus from the liquid effluent.\n\nTo perform the analysis at the second-level divisions, data on total population, distribution of population in urban and rural areas, total income, and average annual income per capita are retrieved at the census division and county level for Canada and the United States, respectively. Data for the year 2020 is considered since it is the most recent information available for both countries. The first-level divisions level corresponds to census divisions of the United States, which provide territorial divisions similar in terms of development, demographic characteristics, and economic activities, being extensively used for collecting and analyzing data throughout the United States. A table of the states included in each United States census division can be found in the Supplementary Information file. The equivalent of the United States census divisions for Canada is the Canadian provinces and territories, although it must be noted that, unlike the case of the United States, their definition is guided by administrative and political considerations instead of statistical criteria.",
             "distribution": [
                 {
-                    "title": "https://zenodo.org/doi/10.5281/zenodo.10485771",
-                    "accessURL": "https://zenodo.org/doi/10.5281/zenodo.10485771"
+                    "accessURL": "https://zenodo.org/doi/10.5281/zenodo.10485771",
+                    "title": "https://zenodo.org/doi/10.5281/zenodo.10485771"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530881",
+            "keyword": [
+                "nutrient pollution",
+                "Phosphorus recovery",
+                "Social impact",
+                "Wastewater Resource Recovery Facilities"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2024-04-12",
-            "references": [
-                "https://pasteur.epa.gov/uploads/10.23719/1530881/documents/P_WWTP_Impact%20manuscript%20for%20RAPID%20SupMat.pdf",
-                "https://www.hydrosheds.org/products/hydrowaste"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198713,19 +198706,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://pasteur.epa.gov/uploads/10.23719/1530881/documents/P_WWTP_Impact%20manuscript%20for%20RAPID%20SupMat.pdf",
+                "https://www.hydrosheds.org/products/hydrowaste"
+            ],
+            "rights": null,
+            "title": "Datasets for manuscript: Phosphorus recovery in municipal wastewater and socioeconomic impacts in Canada and the United States"
         },
         {
-            "title": "Conley 2023 Dose additive effects mixture HFPO-DA, NBP2, PFOS Dataset",
-            "description": "Dataset includes summary statistics (mean, standard error, sample size) for all endpoints measured and reported in the experiments described in the published manuscript. \n\nThis dataset is associated with the following publication:\nConley, J., C. Lambright, N. Evans, A. Farraj, J. Smoot, R. Grindstaff, D. Jenkins-Hill, J. McCord, E. Medlock Kakaley, A. Dixon, E. Hines, and L. Gray. Dose additive maternal and offspring effects of oral maternal exposure to a mixture of three PFAS (HFPO-DA, NBP2, PFOS) during pregnancy in the Sprague-Dawley rat.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 892: 164609, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Justin Conley",
+                "hasEmail": "mailto:conley.justin@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530884/documents/ConleyJustin_359421_Dataset_Dictionary_2023-6-10.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Dataset includes summary statistics (mean, standard error, sample size) for all endpoints measured and reported in the experiments described in the published manuscript. \n\nThis dataset is associated with the following publication:\nConley, J., C. Lambright, N. Evans, A. Farraj, J. Smoot, R. Grindstaff, D. Jenkins-Hill, J. McCord, E. Medlock Kakaley, A. Dixon, E. Hines, and L. Gray. Dose additive maternal and offspring effects of oral maternal exposure to a mixture of three PFAS (HFPO-DA, NBP2, PFOS) during pregnancy in the Sprague-Dawley rat.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 892: 164609, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://ars.els-cdn.com/content/image/1-s2.0-S0048969723032308-mmc1.xlsx",
+                    "title": "https://ars.els-cdn.com/content/image/1-s2.0-S0048969723032308-mmc1.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530884",
             "keyword": [
@@ -198735,20 +198740,10 @@
                 "Developmental Toxicity",
                 "liver toxicity"
             ],
-            "contactPoint": {
-                "fn": "Justin Conley",
-                "hasEmail": "mailto:conley.justin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://ars.els-cdn.com/content/image/1-s2.0-S0048969723032308-mmc1.xlsx",
-                    "accessURL": "https://ars.els-cdn.com/content/image/1-s2.0-S0048969723032308-mmc1.xlsx"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-10",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.164609",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10681034"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198759,44 +198754,46 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1530884/documents/ConleyJustin_359421_Dataset_Dictionary_2023-6-10.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.164609",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10681034"
+            ],
+            "rights": null,
+            "title": "Conley 2023 Dose additive effects mixture HFPO-DA, NBP2, PFOS Dataset"
         },
         {
-            "title": "Colorado 2020 Input-Output Model with Extensions for Jobs, Greenhouse Gases and Value Added",
-            "description": "This is a USEEIO State Model created for Colorado in 2020 that has a limited number of environmental and economic extensions for jobs, greenhouse gas emissions, and value added. The model was created in useeior using StateIO model components. A script to create the model can be found at https://github.com/USEPA/USEEIO-State/blob/4a89319002dd25810ac7fca26052e7e77017417b/Demo-Multipliers-CO.md. The useeior model specification file is at https://github.com/USEPA/USEEIO-State/blob/4a89319002dd25810ac7fca26052e7e77017417b/model_specs/COEEIOv1.0-s-JGV-20.yml. This model was created to demonstrate the use of StateIO models for the 2024 Department of Interior Economics training workshop.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1531007",
-            "keyword": [
-                "economic impact analysis",
-                "state economic models",
-                "Input-Output Analysis",
-                "USEEIO"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/useeior/blob/v1.5.1/format_specs/Model.md",
+            "description": "This is a USEEIO State Model created for Colorado in 2020 that has a limited number of environmental and economic extensions for jobs, greenhouse gas emissions, and value added. The model was created in useeior using StateIO model components. A script to create the model can be found at https://github.com/USEPA/USEEIO-State/blob/4a89319002dd25810ac7fca26052e7e77017417b/Demo-Multipliers-CO.md. The useeior model specification file is at https://github.com/USEPA/USEEIO-State/blob/4a89319002dd25810ac7fca26052e7e77017417b/model_specs/COEEIOv1.0-s-JGV-20.yml. This model was created to demonstrate the use of StateIO models for the 2024 Department of Interior Economics training workshop.",
             "distribution": [
                 {
-                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.xlsx",
-                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.xlsx"
+                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.xlsx",
+                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.xlsx"
                 },
                 {
-                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.rds",
-                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.rds"
+                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.rds",
+                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/USEEIO-State/COEEIOv1.0-s-JGV-20.rds"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1531007",
+            "keyword": [
+                "economic impact analysis",
+                "state economic models",
+                "Input-Output Analysis",
+                "USEEIO"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-05-20",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -198806,85 +198803,81 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/useeior/blob/v1.5.1/format_specs/Model.md"
+            "references": null,
+            "rights": null,
+            "title": "Colorado 2020 Input-Output Model with Extensions for Jobs, Greenhouse Gases and Value Added"
         },
         {
-            "title": "Dataset for \"Persistent gene expression and DNA methylation alterations linked to carcinogenic effects of dichloroacetic acid'",
-            "description": "These spreadsheets contain the underlying data, calculations, and R code for the figures of the manuscript \"Persistent gene expression and DNA methylation alterations linked to carcinogenic effects of dichloroacetic acid\". The first tab of every spreadsheet contains descriptions of the data (metadata). For clarifying questions regarding the data, please contact Dr. Brian Chorley (EPA-ORD) at chorley.brian@epa.gov. If you require a review token for the sequencing datasets located in the GEO links (RNAseq and RRBS), please contact Dr. Chorley. \n\nThis dataset is associated with the following publication:\nCarswell, G., J. Chamberlin, B. Bennett, P. Bushel, and B. Chorley. Persistent gene expression and DNA methylation alterations linked to carcinogenic effects of dichloroacetic acid.   Frontiers in Oncology. Frontiers, Lausanne,  SWITZERLAND, 14: 1389634, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529544",
-            "keyword": [
-                "dichloroacetic acid",
-                "liver cancer",
-                "DNA methylation",
-                "transcriptomics",
-                "archival samples"
-            ],
             "contactPoint": {
                 "fn": "Brian Chorley",
                 "hasEmail": "mailto:chorley.brian@epa.gov"
             },
+            "description": "These spreadsheets contain the underlying data, calculations, and R code for the figures of the manuscript \"Persistent gene expression and DNA methylation alterations linked to carcinogenic effects of dichloroacetic acid\". The first tab of every spreadsheet contains descriptions of the data (metadata). For clarifying questions regarding the data, please contact Dr. Brian Chorley (EPA-ORD) at chorley.brian@epa.gov. If you require a review token for the sequencing datasets located in the GEO links (RNAseq and RRBS), please contact Dr. Chorley. \n\nThis dataset is associated with the following publication:\nCarswell, G., J. Chamberlin, B. Bennett, P. Bushel, and B. Chorley. Persistent gene expression and DNA methylation alterations linked to carcinogenic effects of dichloroacetic acid.   Frontiers in Oncology. Frontiers, Lausanne,  SWITZERLAND, 14: 1389634, (2024).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242661",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242661"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242661",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242661"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242664",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242664"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242664",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242664"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242665",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242665"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242665",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242665"
                 },
                 {
-                    "title": "Figures 5C_7C_9C_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529544/Figures%205C_7C_9C_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figures 5C_7C_9C_data.xlsx"
                 },
                 {
-                    "title": "Figures 2_5_7_9A_B_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529544/Figures%202_5_7_9A_B_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figures 2_5_7_9A_B_data.xlsx"
                 },
                 {
-                    "title": "Figure 8_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529544/Figure%208_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 8_data.xlsx"
                 },
                 {
-                    "title": "Figure 6_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529544/Figure%206_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 6_data.xlsx"
                 },
                 {
-                    "title": "Figure 4_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529544/Figure%204_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 4_data.xlsx"
                 },
                 {
-                    "title": "Figure 3B_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529544/Figure%203B_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 3B_data.xlsx"
                 },
                 {
-                    "title": "Figure 3A_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529544/Figure%203A_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 3A_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529544",
+            "keyword": [
+                "dichloroacetic acid",
+                "liver cancer",
+                "DNA methylation",
+                "transcriptomics",
+                "archival samples"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-08",
-            "references": [
-                "https://doi.org/10.3389/fonc.2024.1389634",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11099211"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198894,67 +198887,70 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fonc.2024.1389634",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11099211"
+            ],
+            "rights": null,
+            "title": "Dataset for \"Persistent gene expression and DNA methylation alterations linked to carcinogenic effects of dichloroacetic acid'"
         },
         {
-            "title": "Nutrient Explorer Application Default Datasets from LAGOS-NE and National Nutrient Inventories",
-            "description": "This dataset contains the default data provided with the Nutrient Explorer Downloadable application (SI: https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=CPHEA&dirEntryId=358039), which is used for testing out the features and capabilities of the app.  The dataset is based off of LAGOS-NE, lake total nitrogen and total phosphorus concentration data from lakes in the Northeast United States and is combined with a number of explanatory variables such as geology, land use, climate, nutrient inputs, and lake characteristics. Portions of this dataset are inaccessible because: The *.RData format is not allowed to be uploaded on ScienceHub (see above response). They can be accessed through the following means: The *.RData files can be accessed when the user downloaded the NutrientExplorer application zip files on the ScienceInventory link: https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=CPHEA&dirEntryId=358039.\r\nThe user need to have RStudio installed to open the application and be able to use the RData files. Format: Some of the data files associated with the Nutrient Explorer application are in the *.RData format, which can not be uploaded to ScienceHub.  These files include hydrologic unit (HU8) watershed shapefiles and some datasets similar to the *.csv files uploaded here containing variables used for testing out the application's features. \n\nThis dataset is associated with the following publication:\nPennino, M., M. Fry, R. Sabo, and J. Carleton. Nutrient Explorer: An analytical framework to visualize and investigate drivers of surface water quality.   ENVIRONMENTAL MODELLING & SOFTWARE. Elsevier Science, New York, NY,   170: 105853, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529141",
-            "keyword": [
-                "Multilinear regression",
-                "Lake water quality",
-                "phosphorus",
-                "random forest modeling",
-                "Nitrogen and Co-pollutants"
-            ],
             "contactPoint": {
                 "fn": "Michael Pennino",
                 "hasEmail": "mailto:pennino.michael@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529141/documents/Table_S1_LAGOS_Full_Variables.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This dataset contains the default data provided with the Nutrient Explorer Downloadable application (SI: https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=CPHEA&dirEntryId=358039), which is used for testing out the features and capabilities of the app.  The dataset is based off of LAGOS-NE, lake total nitrogen and total phosphorus concentration data from lakes in the Northeast United States and is combined with a number of explanatory variables such as geology, land use, climate, nutrient inputs, and lake characteristics. Portions of this dataset are inaccessible because: The *.RData format is not allowed to be uploaded on ScienceHub (see above response). They can be accessed through the following means: The *.RData files can be accessed when the user downloaded the NutrientExplorer application zip files on the ScienceInventory link: https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=CPHEA&dirEntryId=358039.\r\nThe user need to have RStudio installed to open the application and be able to use the RData files. Format: Some of the data files associated with the Nutrient Explorer application are in the *.RData format, which can not be uploaded to ScienceHub.  These files include hydrologic unit (HU8) watershed shapefiles and some datasets similar to the *.csv files uploaded here containing variables used for testing out the application's features. \n\nThis dataset is associated with the following publication:\nPennino, M., M. Fry, R. Sabo, and J. Carleton. Nutrient Explorer: An analytical framework to visualize and investigate drivers of surface water quality.   ENVIRONMENTAL MODELLING & SOFTWARE. Elsevier Science, New York, NY,   170: 105853, (2023).",
             "distribution": [
                 {
-                    "title": "LAGOS_Data_Reduced.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529141/LAGOS_Data_Reduced.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "LAGOS_Data_Reduced.csv"
                 },
                 {
-                    "title": "Table_S1_LAGOS_Full_Variables.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529141/Table_S1_LAGOS_Full_Variables.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S1_LAGOS_Full_Variables.xlsx"
                 },
                 {
-                    "title": "LAGOS_Full_Variables.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529141/LAGOS_Full_Variables.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LAGOS_Full_Variables.xlsx"
                 },
                 {
-                    "title": "LAGOS_Data_5000Rows.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529141/LAGOS_Data_5000Rows.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "LAGOS_Data_5000Rows.csv"
                 },
                 {
-                    "title": "HUC8_2007_7_Average_MaxDepth2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529141/HUC8_2007_7_Average_MaxDepth2.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "HUC8_2007_7_Average_MaxDepth2.csv"
                 },
                 {
-                    "title": "HUC8_2007_7_Average_MaxDepth.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529141/HUC8_2007_7_Average_MaxDepth.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "HUC8_2007_7_Average_MaxDepth.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529141",
+            "keyword": [
+                "Multilinear regression",
+                "Lake water quality",
+                "phosphorus",
+                "random forest modeling",
+                "Nitrogen and Co-pollutants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-16",
-            "references": [
-                "https://doi.org/10.1016/j.envsoft.2023.105853"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -198965,20 +198961,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529141/documents/Table_S1_LAGOS_Full_Variables.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.envsoft.2023.105853"
+            ],
+            "rights": null,
+            "title": "Nutrient Explorer Application Default Datasets from LAGOS-NE and National Nutrient Inventories"
         },
         {
-            "title": "National Wetland Condition Assessment 2016 Datafiles for Report \u201cNational Wetland Condition Assessment: The Second Collaborative Survey of Wetlands in the United States\u201d",
-            "description": "The National Wetland Condition Assessment (NWCA) is a statistical survey of the condition of wetlands in the conterminous United States. It is designed to provide information on the extent of wetlands that support healthy biological condition, estimate how widespread major stressors are that impact wetland quality, and provide insight into the ecological integrity of wetlands nationwide. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NWCA 2016 report. Sampling was conducted in the spring and summer of 2016 at approximately 1,000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include site information, vegetation characteristics, soil properties and chemistry, hydrology sources and disturbances, physical habitat, landscape metrics, algal toxins (microcystin), and water chemistry. Users are encouraged to visit the NARS data webpage for updates to data files and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys.\n\nCitation for the NWCA 2016 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Wetland Condition Assessment 2016 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-wetland-condition-assessment-2016. DOI: 10.23719/1531014 \n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Wetland Condition Assessment 2016 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d \n\nAdditional information: NWCA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Gregg Serenbetz",
+                "hasEmail": "mailto:serenbetz.gregg@epa.gov"
+            },
+            "description": "The National Wetland Condition Assessment (NWCA) is a statistical survey of the condition of wetlands in the conterminous United States. It is designed to provide information on the extent of wetlands that support healthy biological condition, estimate how widespread major stressors are that impact wetland quality, and provide insight into the ecological integrity of wetlands nationwide. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NWCA 2016 report. Sampling was conducted in the spring and summer of 2016 at approximately 1,000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include site information, vegetation characteristics, soil properties and chemistry, hydrology sources and disturbances, physical habitat, landscape metrics, algal toxins (microcystin), and water chemistry. Users are encouraged to visit the NARS data webpage for updates to data files and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys.\n\nCitation for the NWCA 2016 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Wetland Condition Assessment 2016 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-wetland-condition-assessment-2016. DOI: 10.23719/1531014 \n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Wetland Condition Assessment 2016 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d \n\nAdditional information: NWCA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-wetland-condition-assessment-2016",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-wetland-condition-assessment-2016"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1531014",
             "keyword": [
@@ -199000,58 +199003,49 @@
                 "National Aquatic Resource Surveys",
                 "NARS"
             ],
-            "contactPoint": {
-                "fn": "Gregg Serenbetz",
-                "hasEmail": "mailto:serenbetz.gregg@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-wetland-condition-assessment-2016",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-wetland-condition-assessment-2016"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-10",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. Environmental Protection Agency",
                 "subOrganizationOf": {
                     "name": "U.S. Government"
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "National Wetland Condition Assessment 2016 Datafiles for Report \u201cNational Wetland Condition Assessment: The Second Collaborative Survey of Wetlands in the United States\u201d"
         },
         {
-            "title": "Pregnancy gut metabolome",
-            "description": "Data from, \"Gut metabolic changes during pregnancy reveal the importance of gastrointestinal region in sample collection.\". \n\nThis dataset is associated with the following publication:\nMoore, M., J. Ford, M. Schladweiler, J. Dye, T. Jackson, and C. Miller. Gut metabolic changes during pregnancy reveal the importance of gastrointestinal region in sample collection.   Metabolomics. Plenum Press, New York, NY, USA, 20(2): 40, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530871",
-            "keyword": [
-                "gut",
-                "metabolomics",
-                "pregnancy",
-                "Children's Environmental Health"
-            ],
             "contactPoint": {
                 "fn": "Colette Miller",
                 "hasEmail": "mailto:miller.colette@epa.gov"
             },
+            "description": "Data from, \"Gut metabolic changes during pregnancy reveal the importance of gastrointestinal region in sample collection.\". \n\nThis dataset is associated with the following publication:\nMoore, M., J. Ford, M. Schladweiler, J. Dye, T. Jackson, and C. Miller. Gut metabolic changes during pregnancy reveal the importance of gastrointestinal region in sample collection.   Metabolomics. Plenum Press, New York, NY, USA, 20(2): 40, (2024).",
             "distribution": [
                 {
-                    "title": "ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530871/ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530871",
+            "keyword": [
+                "gut",
+                "metabolomics",
+                "pregnancy",
+                "Children's Environmental Health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-16",
-            "references": [
-                "https://doi.org/10.1007/s11306-024-02099-x"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199061,42 +199055,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11306-024-02099-x"
+            ],
+            "rights": null,
+            "title": "Pregnancy gut metabolome"
         },
         {
-            "title": "Dataset for emissions estimates from fires in the wildland urban interface",
-            "description": "This data set includes the emission factors and emission estimates that are used to generate the figures and tables in the manuscript. \n\nThis dataset is associated with the following publication:\nHolder, A., A. Ahmed, J. Vukovich, and V. Rao. Hazardous air pollutants emission estimates from wildfires in the wildland urban interface.   PNAS Nexus. Oxford University Press, OXFORD,  UK, 2(6): pgad186, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528455",
-            "keyword": [
-                "smoke",
-                "particulate matter (PM)",
-                "Toxic emissions",
-                "Structure fire"
-            ],
             "contactPoint": {
                 "fn": "Amara Holder",
                 "hasEmail": "mailto:holder.amara@epa.gov"
             },
+            "description": "This data set includes the emission factors and emission estimates that are used to generate the figures and tables in the manuscript. \n\nThis dataset is associated with the following publication:\nHolder, A., A. Ahmed, J. Vukovich, and V. Rao. Hazardous air pollutants emission estimates from wildfires in the wildland urban interface.   PNAS Nexus. Oxford University Press, OXFORD,  UK, 2(6): pgad186, (2023).",
             "distribution": [
                 {
-                    "title": "Dataset for emission estimates.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528455/Dataset%20for%20emission%20estimates.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dataset for emission estimates.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528455",
+            "keyword": [
+                "smoke",
+                "particulate matter (PM)",
+                "Toxic emissions",
+                "Structure fire"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-23",
-            "references": [
-                "https://doi.org/10.1093/pnasnexus/pgad186",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10281377"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199106,41 +199099,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/pnasnexus/pgad186",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10281377"
+            ],
+            "rights": null,
+            "title": "Dataset for emissions estimates from fires in the wildland urban interface"
         },
         {
-            "title": "An improved multicellular human organoid model for the study of chemical effects on palatal fusion",
-            "description": "Effects of chemicals on palate organoid fusion. Portions of this dataset are inaccessible because: Dataset upload. For questions, contact data lead. They can be accessed through the following means: Dataset is attached. Format: Various file formats. \n\nThis dataset is associated with the following publication:\nWolf, C., H. Ftizpatrick, C. Becker, J. Smith, and C. Wood. An improved multicellular human organoid model for the study of chemical effects on palatal fusion.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA, 115(16): 1513-1533, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1530973",
-            "keyword": [
-                "tissue fusion",
-                "cleft palate",
-                "Teratogen",
-                "organotypic"
-            ],
             "contactPoint": {
                 "fn": "Cynthia Wolf",
                 "hasEmail": "mailto:wolf.cynthiaj@epa.gov"
             },
+            "description": "Effects of chemicals on palate organoid fusion. Portions of this dataset are inaccessible because: Dataset upload. For questions, contact data lead. They can be accessed through the following means: Dataset is attached. Format: Various file formats. \n\nThis dataset is associated with the following publication:\nWolf, C., H. Ftizpatrick, C. Becker, J. Smith, and C. Wood. An improved multicellular human organoid model for the study of chemical effects on palatal fusion.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA, 115(16): 1513-1533, (2023).",
             "distribution": [
                 {
-                    "title": "Spheroid-organoid 3CT model paper data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530973/Spheroid-organoid%203CT%20model%20paper%20data.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Spheroid-organoid 3CT model paper data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1530973",
+            "keyword": [
+                "tissue fusion",
+                "cleft palate",
+                "Teratogen",
+                "organotypic"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-02",
-            "references": [
-                "https://doi.org/10.1002/bdr2.2229"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199150,19 +199144,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/bdr2.2229"
+            ],
+            "rights": null,
+            "title": "An improved multicellular human organoid model for the study of chemical effects on palatal fusion"
         },
         {
-            "title": "Microbial Emission Factors: The Foundation for a Terrestrial-Atmospheric Modeling of Bacteria Aerosolized in Wildland Fires",
-            "description": "The data includes PM2.5 emission factors from prescribed forest fires at Fishlake National Forest, Utah, USA. Portions of this dataset are inaccessible because: The non-generated data was not commissioned by EPA. They can be accessed through the following means: By contacting the creator lkobziar@uidaho.edu. Format: Data were created by Leda Kobizar and is publicly available upon request. \n\nThis dataset is associated with the following publication:\nKobziar, L., P. Lampman, A. Tohidi, A. Kochanski, A. Cervantes, A. Hudak, R. McCarley, B. Gullett, J. Aurell, R. Moore, D. Vuono, B. Christner, A. Watts, J. Cronan, and R. Ottmar. Bacterial Emission Factors: A Foundation for the Terrestrial-Atmospheric Modeling of Bacteria Aerosolized by Wildland Fires.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58: 2413-2422, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Johanna Aurell",
+                "hasEmail": "mailto:aurell.johanna@epa.gov"
+            },
+            "description": "The data includes PM2.5 emission factors from prescribed forest fires at Fishlake National Forest, Utah, USA. Portions of this dataset are inaccessible because: The non-generated data was not commissioned by EPA. They can be accessed through the following means: By contacting the creator lkobziar@uidaho.edu. Format: Data were created by Leda Kobizar and is publicly available upon request. \n\nThis dataset is associated with the following publication:\nKobziar, L., P. Lampman, A. Tohidi, A. Kochanski, A. Cervantes, A. Hudak, R. McCarley, B. Gullett, J. Aurell, R. Moore, D. Vuono, B. Christner, A. Watts, J. Cronan, and R. Ottmar. Bacterial Emission Factors: A Foundation for the Terrestrial-Atmospheric Modeling of Bacteria Aerosolized by Wildland Fires.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 58: 2413-2422, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530968/Data%20Table%20Science%20Hub%20Micro%20EF.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Table Science Hub Micro EF.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530968",
             "keyword": [
@@ -199173,21 +199177,10 @@
                 "wildfire",
                 "atmospheric transport model"
             ],
-            "contactPoint": {
-                "fn": "Johanna Aurell",
-                "hasEmail": "mailto:aurell.johanna@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data Table Science Hub Micro EF.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1530968/Data%20Table%20Science%20Hub%20Micro%20EF.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-05-09",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c05142",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10851933"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199197,19 +199190,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c05142",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10851933"
+            ],
+            "rights": null,
+            "title": "Microbial Emission Factors: The Foundation for a Terrestrial-Atmospheric Modeling of Bacteria Aerosolized in Wildland Fires"
         },
         {
-            "title": "Detection of anatoxins in human urine by liquid chromatography triple quadrupole mass spectrometry and ELISA ",
-            "description": "Validated analytical chemistry methods for measuring anatoxin-a in urine. \n\nThis dataset is associated with the following publication:\nCunningham, B., S. Lagon, W. Bragg, D. Jenkins-Hill, R. Shaner, and E. Hamelin. Detection of anatoxins in human urine by liquid chromatography triple quadrupole mass spectrometry and ELISA.   Toxins. MDPI, Basel,  SWITZERLAND, 16(3): 129, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Donna Jenkins-Hill",
+                "hasEmail": "mailto:hill.donna@epa.gov"
+            },
+            "description": "Validated analytical chemistry methods for measuring anatoxin-a in urine. \n\nThis dataset is associated with the following publication:\nCunningham, B., S. Lagon, W. Bragg, D. Jenkins-Hill, R. Shaner, and E. Hamelin. Detection of anatoxins in human urine by liquid chromatography triple quadrupole mass spectrometry and ELISA.   Toxins. MDPI, Basel,  SWITZERLAND, 16(3): 129, (2024).",
+            "distribution": [
+                {
+                    "accessURL": "https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.mdpi.com%2F2072-6651%2F16%2F3%2F129&data=05%7C02%7CHill.Donna%40epa.gov%7C11b45092ecfb4e6dc8cd08dc6f9718d2%7C88b378b367484867acf976aacbeca6a7%7C0%7C0%7C638507942011853631%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=9MY%2B48CaLvGhvp1qiZPXv%2Bs097Op9ElCQ3r6iPcPEzE%3D&reserved=0",
+                    "title": "https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.mdpi.com%2F2072-6651%2F16%2F3%2F129&data=05%7C02%7CHill.Donna%40epa.gov%7C11b45092ecfb4e6dc8cd08dc6f9718d2%7C88b378b367484867acf976aacbeca6a7%7C0%7C0%7C638507942011853631%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=9MY%2B48CaLvGhvp1qiZPXv%2Bs097Op9ElCQ3r6iPcPEzE%3D&reserved=0"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1530966",
             "keyword": [
@@ -199220,20 +199223,10 @@
                 "exposure",
                 "Harmful Algal Blooms"
             ],
-            "contactPoint": {
-                "fn": "Donna Jenkins-Hill",
-                "hasEmail": "mailto:hill.donna@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.mdpi.com%2F2072-6651%2F16%2F3%2F129&data=05%7C02%7CHill.Donna%40epa.gov%7C11b45092ecfb4e6dc8cd08dc6f9718d2%7C88b378b367484867acf976aacbeca6a7%7C0%7C0%7C638507942011853631%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=9MY%2B48CaLvGhvp1qiZPXv%2Bs097Op9ElCQ3r6iPcPEzE%3D&reserved=0",
-                    "accessURL": "https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.mdpi.com%2F2072-6651%2F16%2F3%2F129&data=05%7C02%7CHill.Donna%40epa.gov%7C11b45092ecfb4e6dc8cd08dc6f9718d2%7C88b378b367484867acf976aacbeca6a7%7C0%7C0%7C638507942011853631%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=9MY%2B48CaLvGhvp1qiZPXv%2Bs097Op9ElCQ3r6iPcPEzE%3D&reserved=0"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2024-02-23",
-            "references": [
-                "https://doi.org/10.3390/toxins16030129",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10975466"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199243,91 +199236,92 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxins16030129",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10975466"
+            ],
+            "rights": null,
+            "title": "Detection of anatoxins in human urine by liquid chromatography triple quadrupole mass spectrometry and ELISA "
         },
         {
-            "title": "Microphysical Characteristics of North Carolina Coastal Precipitation Measured using a Parsivel2 Disdrometer from October 2021 to April 2022",
-            "description": "The data used for presenting the accumulated raw raindrops number distribution in the diameter-velocity domain and the normalized occurrence frequency of DSD samples in the Dm\u2015log10Nw domain. These data are also used to generate numerous relationships. These relationships include rain intercept parameter (N0) vs. shape factor (\u03bc), \u03bc vs. slope factor (\u039b), log10Nw vs. median volume diameter (D0), D0 vs. R, R vs. kinetic energy (KE), and the Z\u2015R relationship. \n\nThis dataset is associated with the following publication:\nYuan, L., A. Mikelonis, and M. Pirhalla. Exploring the Statistical Characteristics of Coastal Winter Precipitation Measured using a Parsivel2 Disdrometer: A Case Study in North Carolina.   Atmospheric Research. Elsevier Science BV, Amsterdam,  NETHERLANDS, 307: 107487, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529804",
-            "keyword": [
-                "Raindrop size distribution",
-                "Rainfall",
-                "coastal precipitation",
-                "DSD"
-            ],
             "contactPoint": {
                 "fn": "Lifeng Yuan",
                 "hasEmail": "mailto:yuan.lifeng@epa.gov"
             },
+            "description": "The data used for presenting the accumulated raw raindrops number distribution in the diameter-velocity domain and the normalized occurrence frequency of DSD samples in the Dm\u2015log10Nw domain. These data are also used to generate numerous relationships. These relationships include rain intercept parameter (N0) vs. shape factor (\u03bc), \u03bc vs. slope factor (\u039b), log10Nw vs. median volume diameter (D0), D0 vs. R, R vs. kinetic energy (KE), and the Z\u2015R relationship. \n\nThis dataset is associated with the following publication:\nYuan, L., A. Mikelonis, and M. Pirhalla. Exploring the Statistical Characteristics of Coastal Winter Precipitation Measured using a Parsivel2 Disdrometer: A Case Study in North Carolina.   Atmospheric Research. Elsevier Science BV, Amsterdam,  NETHERLANDS, 307: 107487, (2024).",
             "distribution": [
                 {
-                    "title": "figure12.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure12.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure12.xlsx"
                 },
                 {
-                    "title": "figure11.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure11.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure11.xlsx"
                 },
                 {
-                    "title": "figure10.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure10.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure10.xlsx"
                 },
                 {
-                    "title": "figure9.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure9.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure9.xlsx"
                 },
                 {
-                    "title": "figure8.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure8.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure8.xlsx"
                 },
                 {
-                    "title": "figure7.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure7.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure7.xlsx"
                 },
                 {
-                    "title": "figure6.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure6.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure6.xlsx"
                 },
                 {
-                    "title": "figure5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure5.xlsx"
                 },
                 {
-                    "title": "figure4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure4.xlsx"
                 },
                 {
-                    "title": "figure3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/figure3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "figure3.xlsx"
                 },
                 {
-                    "title": "Figure2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529804/Figure2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529804",
+            "keyword": [
+                "Raindrop size distribution",
+                "Rainfall",
+                "coastal precipitation",
+                "DSD"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-18",
-            "references": [
-                "https://doi.org/10.1016/j.atmosres.2024.107487"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199337,32 +199331,32 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosres.2024.107487"
+            ],
+            "rights": null,
+            "title": "Microphysical Characteristics of North Carolina Coastal Precipitation Measured using a Parsivel2 Disdrometer from October 2021 to April 2022"
         },
         {
-            "title": "Simultaneous time-resolved aqueous haloamine measurement empowers robust kinetic model analysis V1",
-            "description": "Data is for manuscript entitled \"Simultaneous time-resolved aqueous haloamine measurement empowers robust kinetic model analysis\". This dataset is not publicly accessible because: The data was not generated by EPA.  It can be accessed by contacting the corresponding author. It can be accessed through the following means: Contact the manuscript corresponding author: Pawel K. Mistztal at misztal@utexas.edu. Format: N/A. \n\nThis dataset is associated with the following publication:\nBrodfuehrer, S., D. Blomdahl, D. Wahman, G. Speitel, Jr., P. Mistztal, and L. Katz. Simultaneous time-resolved aqueous haloamine measurement enable analysis of disinfectant degradation kinetics and by-product formation.   Nature Water. Nature Portfolio, Berlin,  GERMANY, 2: 434-442, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528543",
-            "keyword": [
-                "chloramine"
-            ],
             "contactPoint": {
                 "fn": "David Wahman",
                 "hasEmail": "mailto:wahman.david@epa.gov"
             },
+            "description": "Data is for manuscript entitled \"Simultaneous time-resolved aqueous haloamine measurement empowers robust kinetic model analysis\". This dataset is not publicly accessible because: The data was not generated by EPA.  It can be accessed by contacting the corresponding author. It can be accessed through the following means: Contact the manuscript corresponding author: Pawel K. Mistztal at misztal@utexas.edu. Format: N/A. \n\nThis dataset is associated with the following publication:\nBrodfuehrer, S., D. Blomdahl, D. Wahman, G. Speitel, Jr., P. Mistztal, and L. Katz. Simultaneous time-resolved aqueous haloamine measurement enable analysis of disinfectant degradation kinetics and by-product formation.   Nature Water. Nature Portfolio, Berlin,  GERMANY, 2: 434-442, (2024).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1528543",
+            "keyword": [
+                "chloramine"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-02-14",
-            "references": [
-                "https://doi.org/10.1038/s44221-024-00227-4"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199372,40 +199366,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s44221-024-00227-4"
+            ],
+            "rights": null,
+            "title": "Simultaneous time-resolved aqueous haloamine measurement empowers robust kinetic model analysis V1"
         },
         {
-            "title": "Estimates of biomass reductions of ozone sensitive herbaceous plants in California",
-            "description": "We estimated risk of biomass loss due to ozone for selected ozone-sensitive herbaceous plants in California.  We combined U.S. Environmental Protection Agency ozone monitoring data from the entirety of 2016 with published exposure-response relationships from controlled exposure experiments for twenty herbaceous plant species occurring in California.  Dataset includes previously published exposure response functions for the twenty plant species, ozone exposure metrics in AOT40 for each monitor in CA for the selected year, map of the interpolated ozone surface, RMSE of the interpolation, and maps of estimated biomass loss for the herbaceous plant species. \n\nThis dataset is associated with the following publication:\nKaylor, S.D., S.J. Snell Taylor, and J. Herrick. Estimates of biomass reductions of ozone sensitive herbaceous plants in California.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 878: 163134, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1531008",
-            "keyword": [
-                "ecological risk assessment",
-                "herbaceous plants",
-                "Ozone"
-            ],
             "contactPoint": {
                 "fn": "Steven Kaylor",
                 "hasEmail": "mailto:kaylor.doug@epa.gov"
             },
+            "description": "We estimated risk of biomass loss due to ozone for selected ozone-sensitive herbaceous plants in California.  We combined U.S. Environmental Protection Agency ozone monitoring data from the entirety of 2016 with published exposure-response relationships from controlled exposure experiments for twenty herbaceous plant species occurring in California.  Dataset includes previously published exposure response functions for the twenty plant species, ozone exposure metrics in AOT40 for each monitor in CA for the selected year, map of the interpolated ozone surface, RMSE of the interpolation, and maps of estimated biomass loss for the herbaceous plant species. \n\nThis dataset is associated with the following publication:\nKaylor, S.D., S.J. Snell Taylor, and J. Herrick. Estimates of biomass reductions of ozone sensitive herbaceous plants in California.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 878: 163134, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0048969723017539",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0048969723017539"
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0048969723017539",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0048969723017539"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1531008",
+            "keyword": [
+                "ecological risk assessment",
+                "herbaceous plants",
+                "Ozone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-23",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.163134",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10543089"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199415,41 +199408,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.163134",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10543089"
+            ],
+            "rights": null,
+            "title": "Estimates of biomass reductions of ozone sensitive herbaceous plants in California"
         },
         {
-            "title": "Data for Figure 2: Peak areas of fluorinated features detected with nontargeted analysis of OTM-45 extracts",
-            "description": "This dataset contains data from nontargeted analysis of the OTM-45 extracts obtained during the incineration of PFAS containing AFFF. The data was used to create Figure 2 in the associated manuscript. The Figure uses the sums of the peak areas to create a bar graph show relative peak areas of fluorinated features for each of the incineration conditions studied. The peak areas for the features identified as PFAS that are targeted for typical analyses were plotted along with the total areas to show how many of the features fall outside of typical PFAS analyses. \n\nThis dataset is associated with the following publication:\nShields, E., J. Krug, W. Roberson, S. Jackson, M. Smeltz, M. Allen, R.(. Burnette, J. Nash, L. Virtaranta, W. Preston, H. Liberatore, A. Wallace, J. Ryan, P. Kariher, P. Lemieux, and B. Linak. Pilot\u2010Scale Thermal Destruction of Per\u2010 and Polyfluoroalkyl Substances in a Legacy Aqueous Film Forming Foam.   ACS ES&T Engineering. American Chemical Society, Washington, DC, USA, 3(9): 1308\u20131317, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528511",
-            "keyword": [
-                "nontargeted analysis",
-                "per and polyfluoroalkyl substances (PFAS)",
-                "AFFF",
-                "incineration"
-            ],
             "contactPoint": {
                 "fn": "Erin Shields",
                 "hasEmail": "mailto:shields.erin@epa.gov"
             },
+            "description": "This dataset contains data from nontargeted analysis of the OTM-45 extracts obtained during the incineration of PFAS containing AFFF. The data was used to create Figure 2 in the associated manuscript. The Figure uses the sums of the peak areas to create a bar graph show relative peak areas of fluorinated features for each of the incineration conditions studied. The peak areas for the features identified as PFAS that are targeted for typical analyses were plotted along with the total areas to show how many of the features fall outside of typical PFAS analyses. \n\nThis dataset is associated with the following publication:\nShields, E., J. Krug, W. Roberson, S. Jackson, M. Smeltz, M. Allen, R.(. Burnette, J. Nash, L. Virtaranta, W. Preston, H. Liberatore, A. Wallace, J. Ryan, P. Kariher, P. Lemieux, and B. Linak. Pilot\u2010Scale Thermal Destruction of Per\u2010 and Polyfluoroalkyl Substances in a Legacy Aqueous Film Forming Foam.   ACS ES&T Engineering. American Chemical Society, Washington, DC, USA, 3(9): 1308\u20131317, (2023).",
             "distribution": [
                 {
-                    "title": "Figure2-OTM45-NTA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528511/Figure2-OTM45-NTA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure2-OTM45-NTA.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528511",
+            "keyword": [
+                "nontargeted analysis",
+                "per and polyfluoroalkyl substances (PFAS)",
+                "AFFF",
+                "incineration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-02-07",
-            "references": [
-                "https://doi.org/10.1021/acsestengg.3c00098"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199459,20 +199453,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acsestengg.3c00098"
+            ],
+            "rights": null,
+            "title": "Data for Figure 2: Peak areas of fluorinated features detected with nontargeted analysis of OTM-45 extracts"
         },
         {
-            "title": "Convex Hulls for Species Richness and Invivudal Species",
-            "description": "These are .tiff files, with bands for total distance to the convex hull (Distance), as well as individual distances for the 5 dimensions of pH (pH), precipitation (Precipitation), temperature (Temperature), nitrogen deposition (Nitrogen), and sulfur deposition (Sulfur). Note that for open and closed canopy convex hulls, sulfur was not included in the original analysis (Simkin et al. 2016) and thus are not included in the convex hulls. The units for all distances are in standard deviations (based on Mahalanobis distance). Distances are unitless and based on Mahalanobis distance. This dataset is not publicly accessible because: The files are too big for Science Hub (15.9 GB). It can be accessed through the following means: Email Christopher Clark (clark.christopher@epa.gov) for access to the data. Format: The data are .tif files for convex hulls for richness (2 convex hulls, open and closed canopy communities) and species (198 convex hulls).",
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
+                "fn": "Christopher Clark",
+                "hasEmail": "mailto:clark.christopher@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1531021/documents/Metadata%20for%20Hulls_Final.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "These are .tiff files, with bands for total distance to the convex hull (Distance), as well as individual distances for the 5 dimensions of pH (pH), precipitation (Precipitation), temperature (Temperature), nitrogen deposition (Nitrogen), and sulfur deposition (Sulfur). Note that for open and closed canopy convex hulls, sulfur was not included in the original analysis (Simkin et al. 2016) and thus are not included in the convex hulls. The units for all distances are in standard deviations (based on Mahalanobis distance). Distances are unitless and based on Mahalanobis distance. This dataset is not publicly accessible because: The files are too big for Science Hub (15.9 GB). It can be accessed through the following means: Email Christopher Clark (clark.christopher@epa.gov) for access to the data. Format: The data are .tif files for convex hulls for richness (2 convex hulls, open and closed canopy communities) and species (198 convex hulls).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1531021",
             "keyword": [
                 "biodiversity",
@@ -199481,13 +199481,11 @@
                 "critical loads",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Christopher Clark",
-                "hasEmail": "mailto:clark.christopher@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-15",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -199497,47 +199495,45 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1531021/documents/Metadata%20for%20Hulls_Final.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": null,
+            "rights": null,
+            "title": "Convex Hulls for Species Richness and Invivudal Species"
         },
         {
-            "title": "Data for figures in Phelan et al. \"Climate change could negate U.S. forest ecosystem service benefits gained through reductions in nitrogen and sulfur deposition\"",
-            "description": "This dataset has all the summary tables for the Figures and supplementary information in the Phelan et al. publication. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1531022",
-            "keyword": [
-                "climate change",
-                "Nitrogen and Co-pollutants",
-                "forest",
-                "ecosystem services",
-                "nitrogen deposition",
-                "biodiversity"
-            ],
             "contactPoint": {
                 "fn": "Christopher Clark",
                 "hasEmail": "mailto:clark.christopher@epa.gov"
             },
+            "description": "This dataset has all the summary tables for the Figures and supplementary information in the Phelan et al. publication. ",
             "distribution": [
                 {
-                    "title": "https://www.nature.com/articles/s41598-024-60652-z",
-                    "accessURL": "https://www.nature.com/articles/s41598-024-60652-z"
+                    "accessURL": "https://www.nature.com/articles/s41598-024-60652-z",
+                    "title": "https://www.nature.com/articles/s41598-024-60652-z"
                 },
                 {
-                    "title": "Phelan_2024_Scientific Reports_Atmos dep and CC effects on forest ecoservices_SI.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1531022/Phelan_2024_Scientific%20Reports_Atmos%20dep%20and%20CC%20effects%20on%20forest%20ecoservices_SI.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Phelan_2024_Scientific Reports_Atmos dep and CC effects on forest ecoservices_SI.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1531022",
+            "keyword": [
+                "climate change",
+                "Nitrogen and Co-pollutants",
+                "forest",
+                "ecosystem services",
+                "nitrogen deposition",
+                "biodiversity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-10",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -199546,49 +199542,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Data for figures in Phelan et al. \"Climate change could negate U.S. forest ecosystem service benefits gained through reductions in nitrogen and sulfur deposition\""
         },
         {
-            "title": "Metadata for Effects of point and nonpoint source controls on total phosphorus load trends across the Chesapeake Bay watershed, USA",
-            "description": "These datasets allow users to acquire necessary input data to replication Zhang et al. (2023) and also review the model output results. \n\nThis dataset is associated with the following publication:\nZhang, Q., J. Bostic, and R. Sabo. Effects of point and nonpoint source controls on total phosphorus load trends across the Chesapeake Bay watershed, USA.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 19: 014012, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1531010",
-            "keyword": [
-                "phosphorus",
-                "water quality",
-                "eutrophication",
-                "rivers",
-                "Phosphorus and Nitrogen"
-            ],
             "contactPoint": {
                 "fn": "Robert Sabo",
                 "hasEmail": "mailto:sabo.robert@epa.gov"
             },
+            "description": "These datasets allow users to acquire necessary input data to replication Zhang et al. (2023) and also review the model output results. \n\nThis dataset is associated with the following publication:\nZhang, Q., J. Bostic, and R. Sabo. Effects of point and nonpoint source controls on total phosphorus load trends across the Chesapeake Bay watershed, USA.   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 19: 014012, (2023).",
             "distribution": [
                 {
-                    "title": "https://iopscience.iop.org/article/10.1088/1748-9326/ad0d3c",
-                    "accessURL": "https://iopscience.iop.org/article/10.1088/1748-9326/ad0d3c"
+                    "accessURL": "https://iopscience.iop.org/article/10.1088/1748-9326/ad0d3c",
+                    "title": "https://iopscience.iop.org/article/10.1088/1748-9326/ad0d3c"
                 },
                 {
-                    "title": "https://www.sciencebase.gov/catalog/item/62bdc7a4d34e82c548cec1e7",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/62bdc7a4d34e82c548cec1e7"
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/62bdc7a4d34e82c548cec1e7",
+                    "title": "https://www.sciencebase.gov/catalog/item/62bdc7a4d34e82c548cec1e7"
                 },
                 {
-                    "title": "https://cast.chesapeakebay.net/Documentation/ModelDocumentation",
-                    "accessURL": "https://cast.chesapeakebay.net/Documentation/ModelDocumentation"
+                    "accessURL": "https://cast.chesapeakebay.net/Documentation/ModelDocumentation",
+                    "title": "https://cast.chesapeakebay.net/Documentation/ModelDocumentation"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1531010",
+            "keyword": [
+                "phosphorus",
+                "water quality",
+                "eutrophication",
+                "rivers",
+                "Phosphorus and Nitrogen"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-12-01",
-            "references": [
-                "https://doi.org/10.1088/1748-9326/ad0d3c"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -199598,47 +199592,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1748-9326/ad0d3c"
+            ],
+            "rights": null,
+            "title": "Metadata for Effects of point and nonpoint source controls on total phosphorus load trends across the Chesapeake Bay watershed, USA"
         },
         {
-            "title": "Urine pH and Risk of Bladder Cancer in Northern New England",
```

