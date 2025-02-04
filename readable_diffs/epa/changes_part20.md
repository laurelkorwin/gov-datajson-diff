# Change History for epa.json (Part 20)

### Changes from 31606f9 to dd2190f (Part 10/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
             },
+            "description": "The data in this archive in in a zipped R data binary format, https://cran.r-project.org/doc/manuals/r-release/R-data.html. These data can be read by using the open source and free to use statistical software package R, https://www.r-project.org/. The data are organized following the figure numbering in the manuscript, e.g. Figure 1a is fig1a, and contains the same labeling as the figures including units and variable names. For a full explanation of the figure, please see the captions in the manuscript. \n\nTo open this data file, use the following commands in R. \n\n> load(\u2018JKelly_NH4NO3_JGR_2018.rdata\u2019)\n\nTo list the contents of the file, use the following command in R\n\n> ls()\n\nThe data for each figure is contained in the data object with the figures name. To list the data, simply type the name of the figure returned from the ls() command. \n\nThe original model output and emissions used for this study are located on the ASM archived storage at /asm/ROMO/finescale/sjv2013. These data are in NetCDF format with self contained metadata with descriptive headers containing variable names, units, and simulation times. \n\nThis dataset is associated with the following publication:\nKelly, J., C. Parworth, Q. Zhang, D. Miller, K. Sun, M. Zondlo , K. Baker, A. Wisthaler, J. Nowak , S. Pusede , R. Cohen , A. Weinheimer , A. Beyersdorf , G. Tonnesen, J. Bash, L. Valin, J. Crawford, A. Fried , and J. Walega. Modeling NH4NO3 Over the San Joaquin Valley During the 2013 DISCOVER\u2010AQ Campaign.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 123(9): 4727-4745, (2018).",
             "distribution": [
                 {
-                    "title": "Metadata.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434678/Metadata.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Metadata.docx"
                 },
                 {
-                    "title": "JKelly_NH4NO3_JGR_2018.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434678/JKelly_NH4NO3_JGR_2018.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "JKelly_NH4NO3_JGR_2018.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434678",
+            "keyword": [
+                "CMAQ",
+                "Ambient air quality",
+                "ammonia",
+                "particulate matter",
+                "air quality model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-02",
-            "references": [
-                "https://doi.org/10.1029/2018jd028290"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97459,48 +97453,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2018jd028290"
+            ],
+            "rights": null,
+            "title": "Modeling data and data for figures and text"
         },
         {
-            "title": "Bacterial community on biofilms from MAIFAS reactors",
-            "description": "Sequence reads (16S rDNA- and 16S rRNA-based) were processed and analyzed using Mothur software. The results presented in the attached Excel file. Also, the other MS word file includes taxonomic summary tables for bacterial communities on biofilms from the MAIFAS reactor as well as the detailed description of Materials & Methods. \n\nThis dataset is associated with the following publication:\nChurch, J., H. Ryu, A. Sadmani, A. Randall, J. Santodomingo, and W.H. Lee. Multiscale investigation of a symbiotic microalgal-integrated fixed film activated sludge (MAIFAS) process for nutrient removal and photo-oxygenation.   Bioresource Technology. Elsevier Online, New York, NY, USA, 268: 128-138, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1423208",
-            "keyword": [
-                "Algae",
-                "Bacteria",
-                "Biofilm",
-                "Chlorella vulgaris",
-                "Microsensors",
-                "Illumina sequencing"
-            ],
             "contactPoint": {
                 "fn": "Hodon Ryu",
                 "hasEmail": "mailto:ryu.hodon@epa.gov"
             },
+            "description": "Sequence reads (16S rDNA- and 16S rRNA-based) were processed and analyzed using Mothur software. The results presented in the attached Excel file. Also, the other MS word file includes taxonomic summary tables for bacterial communities on biofilms from the MAIFAS reactor as well as the detailed description of Materials & Methods. \n\nThis dataset is associated with the following publication:\nChurch, J., H. Ryu, A. Sadmani, A. Randall, J. Santodomingo, and W.H. Lee. Multiscale investigation of a symbiotic microalgal-integrated fixed film activated sludge (MAIFAS) process for nutrient removal and photo-oxygenation.   Bioresource Technology. Elsevier Online, New York, NY, USA, 268: 128-138, (2018).",
             "distribution": [
                 {
-                    "title": "MAIFAS_16S rRNA Illumina seq_tables_methods.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1423208/MAIFAS_16S%20rRNA%20Illumina%20seq_tables_methods.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "MAIFAS_16S rRNA Illumina seq_tables_methods.docx"
                 },
                 {
-                    "title": "MAIFAS_16S rRNA Illumina seq_muthur analyses.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1423208/MAIFAS_16S%20rRNA%20Illumina%20seq_muthur%20analyses.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "MAIFAS_16S rRNA Illumina seq_muthur analyses.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1423208",
+            "keyword": [
+                "Algae",
+                "Bacteria",
+                "Biofilm",
+                "Chlorella vulgaris",
+                "Microsensors",
+                "Illumina sequencing"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-01",
-            "references": [
-                "https://doi.org/10.1016/j.biortech.2018.07.123"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97510,41 +97504,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.biortech.2018.07.123"
+            ],
+            "rights": null,
+            "title": "Bacterial community on biofilms from MAIFAS reactors"
         },
         {
-            "title": "Ceriodaphnia dubia control reproduction 9-CA-labs",
-            "description": "The data represent the reproduction endpoint for the Ceriodaphnia dubia survival and reproduction aquatic toxicity test. Data on control reproduction was acquired for nine California laboratories and 370 WET tests. The data is used in a study comparing the ability of two statistical hypothesis-test approaches to detect toxicity. \n\nThis dataset is associated with the following publication:\nFox, J., J. Diamond, D. Denton, and R. Stuber. Comparison of Statistical Approaches Applied to the Ceriodaphnia dubia Chronic Toxicity Method.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA,  511-523, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1376211",
-            "keyword": [
-                "Whole effluent toxicity (WET)",
-                "Test of Significant Toxicity (TST)",
-                "No Observed Effect Concentration (NOEC)",
-                "statistical error rates"
-            ],
             "contactPoint": {
                 "fn": "John Fox",
                 "hasEmail": "mailto:fox.john@epa.gov"
             },
+            "description": "The data represent the reproduction endpoint for the Ceriodaphnia dubia survival and reproduction aquatic toxicity test. Data on control reproduction was acquired for nine California laboratories and 370 WET tests. The data is used in a study comparing the ability of two statistical hypothesis-test approaches to detect toxicity. \n\nThis dataset is associated with the following publication:\nFox, J., J. Diamond, D. Denton, and R. Stuber. Comparison of Statistical Approaches Applied to the Ceriodaphnia dubia Chronic Toxicity Method.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA,  511-523, (2019).",
             "distribution": [
                 {
-                    "title": "crc-merged.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1376211/crc-merged.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "crc-merged.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1376211",
+            "keyword": [
+                "Whole effluent toxicity (WET)",
+                "Test of Significant Toxicity (TST)",
+                "No Observed Effect Concentration (NOEC)",
+                "statistical error rates"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-14",
-            "references": [
-                "https://doi.org/10.1002/etc.4347"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97554,42 +97548,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4347"
+            ],
+            "rights": null,
+            "title": "Ceriodaphnia dubia control reproduction 9-CA-labs"
         },
         {
-            "title": "The relative importance of waterborne and dietborne As exposure on survival and growth of juvenile fathead minnows.",
-            "description": "This dataset provides exposure and effects data for two experiments regarding the dietborne toxicity of inorganic arsenic on fathead minnows survival and growth.  There are separate spreadsheets for the two experiments, at the replicate exposure chamber level, of fish exposure, survival, and weights and calculated growth metrics.  Each spreadsheet provides footnote descriptions of the data and calculations provided.  Descriptions of experimental protocols are also provided as supporting documents. \n\nThis dataset is associated with the following publication:\nErickson, R., D. Mount, T. Highland, R. Hockett, D. Hoff, C. Jenson, and T. Lahren. The relative importance of waterborne and dietborne As exposure on survival and growth of juvenile fathead minnows.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 211: 18-28, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1502610",
-            "keyword": [
-                "fathead minnow",
-                "arsenic",
-                "ecological risk assessment",
-                "fish dietary studies",
-                "aquatic toxicity"
-            ],
             "contactPoint": {
                 "fn": "Russell Erickson",
                 "hasEmail": "mailto:erickson.russell@epa.gov"
             },
+            "description": "This dataset provides exposure and effects data for two experiments regarding the dietborne toxicity of inorganic arsenic on fathead minnows survival and growth.  There are separate spreadsheets for the two experiments, at the replicate exposure chamber level, of fish exposure, survival, and weights and calculated growth metrics.  Each spreadsheet provides footnote descriptions of the data and calculations provided.  Descriptions of experimental protocols are also provided as supporting documents. \n\nThis dataset is associated with the following publication:\nErickson, R., D. Mount, T. Highland, R. Hockett, D. Hoff, C. Jenson, and T. Lahren. The relative importance of waterborne and dietborne As exposure on survival and growth of juvenile fathead minnows.   AQUATIC TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 211: 18-28, (2019).",
             "distribution": [
                 {
-                    "title": "MEDDietaryPaper4_Dataset.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502610/MEDDietaryPaper4_Dataset.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "MEDDietaryPaper4_Dataset.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502610",
+            "keyword": [
+                "fathead minnow",
+                "arsenic",
+                "ecological risk assessment",
+                "fish dietary studies",
+                "aquatic toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-04",
-            "references": [
-                "https://doi.org/10.1016/j.aquatox.2019.03.008"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97599,41 +97593,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.aquatox.2019.03.008"
+            ],
+            "rights": null,
+            "title": "The relative importance of waterborne and dietborne As exposure on survival and growth of juvenile fathead minnows."
         },
         {
-            "title": "Nova Scotia Sediment UnmixO source contributions.",
-            "description": "PAH source contributions for each Nova Scotia harbors. \n\nThis dataset is associated with the following publication:\nDavis, E., T. Walker, M. Adams, R. Willis, G. Norris, and R. Henry. Source apportionment of polycyclic aromatic hydrocarbons (PAHs) in small craft harbor (SCH) surficial sediments in Nova Scotia, Canada.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 691: 528-537, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503517",
-            "keyword": [
-                "Polycyclic aromatic hydrocarbons (PAHs)",
-                "source apportionment",
-                "Unmix Optimum",
-                "PAHs"
-            ],
             "contactPoint": {
                 "fn": "Gary Norris",
                 "hasEmail": "mailto:norris.gary@epa.gov"
             },
+            "description": "PAH source contributions for each Nova Scotia harbors. \n\nThis dataset is associated with the following publication:\nDavis, E., T. Walker, M. Adams, R. Willis, G. Norris, and R. Henry. Source apportionment of polycyclic aromatic hydrocarbons (PAHs) in small craft harbor (SCH) surficial sediments in Nova Scotia, Canada.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 691: 528-537, (2019).",
             "distribution": [
                 {
-                    "title": "Source Contributions for EPA website_NSHarbours_Feb202019.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503517/Source%20Contributions%20for%20EPA%20website_NSHarbours_Feb202019.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Source Contributions for EPA website_NSHarbours_Feb202019.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503517",
+            "keyword": [
+                "Polycyclic aromatic hydrocarbons (PAHs)",
+                "source apportionment",
+                "Unmix Optimum",
+                "PAHs"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-20",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2019.07.114"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97643,19 +97637,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2019.07.114"
+            ],
+            "rights": null,
+            "title": "Nova Scotia Sediment UnmixO source contributions."
         },
         {
-            "title": "Data for Boquer\u00f3n Beach, Puerto Rico immunoconversion study",
-            "description": "The data contained in this worksheet provides the Median Fluorescence Intensity (MFI) readings from saliva samples serially collected during the Boquer\u00f3n Beach, Puerto Rico study.  Samples were analyzed using the bead-based multiplex immunoassay to assess immunoconversions in the beachgoers to multiple waterborne pathogens.  In the study, we collected an initial sample (S1) at the beach  and the remaining samples (S2 and S3) were self-collected by participants 10 -14 and 30 - 40 days later, respectively. \n\nThis dataset is associated with the following publication:\nSimmons, K.J., T. Eason, C.L. Curioso, S. Griffin, M.K.D. Ramudit, K. Oshima, E. Sams, T. Wade, A. Grimm, A. Dufour, and S. Augustine. Visitors to a Tropical Marine Beach Show Evidence of Immunoconversions to Multiple Waterborne Pathogens.   Frontiers in Public Health. Frontiers, Lausanne,  SWITZERLAND, issue}: 231, (2019).",
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
+            "description": "The data contained in this worksheet provides the Median Fluorescence Intensity (MFI) readings from saliva samples serially collected during the Boquer\u00f3n Beach, Puerto Rico study.  Samples were analyzed using the bead-based multiplex immunoassay to assess immunoconversions in the beachgoers to multiple waterborne pathogens.  In the study, we collected an initial sample (S1) at the beach  and the remaining samples (S2 and S3) were self-collected by participants 10 -14 and 30 - 40 days later, respectively. \n\nThis dataset is associated with the following publication:\nSimmons, K.J., T. Eason, C.L. Curioso, S. Griffin, M.K.D. Ramudit, K. Oshima, E. Sams, T. Wade, A. Grimm, A. Dufour, and S. Augustine. Visitors to a Tropical Marine Beach Show Evidence of Immunoconversions to Multiple Waterborne Pathogens.   Frontiers in Public Health. Frontiers, Lausanne,  SWITZERLAND, issue}: 231, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503882/Copy%20of%20Boqueron%20IC%20data%20%28Augustine%20et%20al.%202019-Frontiers%29.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of Boqueron IC data (Augustine et al. 2019-Frontiers).xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503882",
             "keyword": [
@@ -97666,20 +97670,10 @@
                 "salivary antibodies",
                 "luminex assay"
             ],
-            "contactPoint": {
-                "fn": "Swinburne Augustine",
-                "hasEmail": "mailto:augustine.swinburne@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Copy of Boqueron IC data (Augustine et al. 2019-Frontiers).xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503882/Copy%20of%20Boqueron%20IC%20data%20%28Augustine%20et%20al.%202019-Frontiers%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-02",
-            "references": [
-                "https://doi.org/10.3389/fpubh.2019.00231"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97689,45 +97683,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fpubh.2019.00231"
+            ],
+            "rights": null,
+            "title": "Data for Boquer\u00f3n Beach, Puerto Rico immunoconversion study"
         },
         {
-            "title": "Village Green Project station data - March 2015",
-            "description": "The data sets include the Village Green Project station time series, including air pollutant concentrations, meteorology data, and diagnostic data from instrumentation. Additionally, air pollutant concentration data from the Hong Kong Environmental Protection Department's Eastern station are included. \n\nThis dataset is associated with the following publication:\nWei, P., Z. Ning, D. Westerdahl, Y.F. Lam, P. Louie, R. Sharpe, R. Williams, and G. Hagler. Solar-powered air quality monitor applied under subtropical conditions in Hong Kong: Performance evaluation and application for pollution source tracking.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 214: 116825, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504019",
-            "keyword": [
-                "air quality",
-                "Village Green Project",
-                "air monitoring technology"
-            ],
             "contactPoint": {
                 "fn": "Gayle Hagler",
                 "hasEmail": "mailto:hagler.gayle@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1504019/documents/DataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The data sets include the Village Green Project station time series, including air pollutant concentrations, meteorology data, and diagnostic data from instrumentation. Additionally, air pollutant concentration data from the Hong Kong Environmental Protection Department's Eastern station are included. \n\nThis dataset is associated with the following publication:\nWei, P., Z. Ning, D. Westerdahl, Y.F. Lam, P. Louie, R. Sharpe, R. Williams, and G. Hagler. Solar-powered air quality monitor applied under subtropical conditions in Hong Kong: Performance evaluation and application for pollution source tracking.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 214: 116825, (2019).",
             "distribution": [
                 {
-                    "title": "HKEPD_Eastern_sum.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504019/HKEPD_Eastern_sum.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HKEPD_Eastern_sum.xlsx"
                 },
                 {
-                    "title": "VGP-HongKong.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504019/VGP-HongKong.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "VGP-HongKong.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504019",
+            "keyword": [
+                "air quality",
+                "Village Green Project",
+                "air monitoring technology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-08",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2019.116825"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97738,20 +97734,35 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1504019/documents/DataDictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2019.116825"
+            ],
+            "rights": null,
+            "title": "Village Green Project station data - March 2015"
         },
         {
-            "title": "Assessing PM2.5 Model Performance for the Conterminous U.S. with Comparison to Model Performance Statistics from 2007-2015",
-            "description": "Dataset includes links to CMAQ codes, evaluation of model predictions against network data, and additional supporting information. \n\nThis dataset is associated with the following publication:\nKelly, J., S. Koplitz, K. Baker, A. Holder, H. Pye, B. Murphy, J. Bash, B. Henderson, N. Possiel, H. Simon, A. Eyth, C. Jang, S. Phillips, and B. Timin. Assessing PM2.5 model performance for the conterminous U.S. with comparison to model performance statistics from 2007-2015.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 214: 116872, (2019).",
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
+            "description": "Dataset includes links to CMAQ codes, evaluation of model predictions against network data, and additional supporting information. \n\nThis dataset is associated with the following publication:\nKelly, J., S. Koplitz, K. Baker, A. Holder, H. Pye, B. Murphy, J. Bash, B. Henderson, N. Possiel, H. Simon, A. Eyth, C. Jang, S. Phillips, and B. Timin. Assessing PM2.5 model performance for the conterminous U.S. with comparison to model performance statistics from 2007-2015.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 214: 116872, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc1.csv",
+                    "title": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc1.csv"
+                },
+                {
+                    "accessURL": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc3.pdf",
+                    "title": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc3.pdf"
+                },
+                {
+                    "accessURL": "https://doi.org/10.5281/zenodo.1212601",
+                    "title": "https://doi.org/10.5281/zenodo.1212601"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503788",
             "keyword": [
@@ -97765,27 +97776,10 @@
                 "Semivolatile Organic Compounds (SVOCs)",
                 "Biogenic VOC"
             ],
-            "contactPoint": {
-                "fn": "Havala Pye",
-                "hasEmail": "mailto:pye.havala@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc1.csv",
-                    "accessURL": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc1.csv"
-                },
-                {
-                    "title": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc3.pdf",
-                    "accessURL": "https://ars.els-cdn.com/content/image/1-s2.0-S1352231019305023-mmc3.pdf"
-                },
-                {
-                    "title": "https://doi.org/10.5281/zenodo.1212601",
-                    "accessURL": "https://doi.org/10.5281/zenodo.1212601"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-04",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2019.116872"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97795,19 +97789,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2019.116872"
+            ],
+            "rights": null,
+            "title": "Assessing PM2.5 Model Performance for the Conterminous U.S. with Comparison to Model Performance Statistics from 2007-2015"
         },
         {
-            "title": "Alternatives Assessment Dashboard Hazard Database Version 1.0  Generated 12/07/2018",
-            "description": "This is a collection of over 290,000 hazard data records compiled for the Alternatives Assessment Dashboard. The hazard data includes records for human health, ecotoxicity, and fate. The human health records include records for Acute mammalian toxicity, Carcinogenicity, Mutagenicity, Endocrine disruption, Reproductive toxicity, Developmental toxicity, Neurotoxicity, Systemic toxicity, Skin sensitization, Skin irritation, and Eye irritation.  The ecotoxicity records include records for acute and chronic aquatic toxicity. The fate records include records for persistance and bioaccumulation.  The source of the hazard records include GHS (Globally Harmonized System) hazard codes, hazard categories, quantitative toxicity data, and predicted toxicity data.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Todd Martin",
+                "hasEmail": "mailto:martin.todd@epa.gov"
+            },
+            "description": "This is a collection of over 290,000 hazard data records compiled for the Alternatives Assessment Dashboard. The hazard data includes records for human health, ecotoxicity, and fate. The human health records include records for Acute mammalian toxicity, Carcinogenicity, Mutagenicity, Endocrine disruption, Reproductive toxicity, Developmental toxicity, Neurotoxicity, Systemic toxicity, Skin sensitization, Skin irritation, and Eye irritation.  The ecotoxicity records include records for acute and chronic aquatic toxicity. The fate records include records for persistance and bioaccumulation.  The source of the hazard records include GHS (Globally Harmonized System) hazard codes, hazard categories, quantitative toxicity data, and predicted toxicity data.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503620/flat%20file%202018-12-07.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "flat file 2018-12-07.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503620",
             "keyword": [
@@ -97818,21 +97822,10 @@
                 "toxicity",
                 "GHS Data"
             ],
-            "contactPoint": {
-                "fn": "Todd Martin",
-                "hasEmail": "mailto:martin.todd@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "flat file 2018-12-07.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503620/flat%20file%202018-12-07.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-12-07",
-            "references": [
-                "https://pasteur.epa.gov/uploads/10.23719/1503620/documents/Parse.zip",
-                "https://pasteur.epa.gov/uploads/10.23719/1503620/documents/api.zip"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97842,41 +97835,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://pasteur.epa.gov/uploads/10.23719/1503620/documents/Parse.zip",
+                "https://pasteur.epa.gov/uploads/10.23719/1503620/documents/api.zip"
+            ],
+            "rights": null,
+            "title": "Alternatives Assessment Dashboard Hazard Database Version 1.0  Generated 12/07/2018"
         },
         {
-            "title": "Smoke Sense Analysis Data 2017-08-01 Through 2018-01-07 with Identifiers Removed",
-            "description": "Citizen science reports from Smoke Sense app participants from the pilot study during 2017-08-01 through 2018-01-07, with personal identifiers removed. \n\nThis dataset is associated with the following publication:\nRappold, A., M. Hano, S. Prince, L. Wei, M. Huang, C. Baghdikian, B. Sterns, X. Gao, S. Hoshiko, W. Cascio, D. Diazsanchez, and B. Hubbell. Smoke Sense Initiative Leverages Citizen Science to Address the Growing Wildfire-Related Public Health Problem.   GeoHealth. American Geophysical Union, Washington, DC, USA, 3(12): 443-457, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503824",
-            "keyword": [
-                "Health Behavior",
-                "citizen science",
-                "Wildfire smoke",
-                "Smartphone app"
-            ],
             "contactPoint": {
                 "fn": "Ana Rappold",
                 "hasEmail": "mailto:rappold.ana@epa.gov"
             },
+            "description": "Citizen science reports from Smoke Sense app participants from the pilot study during 2017-08-01 through 2018-01-07, with personal identifiers removed. \n\nThis dataset is associated with the following publication:\nRappold, A., M. Hano, S. Prince, L. Wei, M. Huang, C. Baghdikian, B. Sterns, X. Gao, S. Hoshiko, W. Cascio, D. Diazsanchez, and B. Hubbell. Smoke Sense Initiative Leverages Citizen Science to Address the Growing Wildfire-Related Public Health Problem.   GeoHealth. American Geophysical Union, Washington, DC, USA, 3(12): 443-457, (2019).",
             "distribution": [
                 {
-                    "title": "Smoke Sense Analysis Data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503824/Smoke%20Sense%20Analysis%20Data.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Smoke Sense Analysis Data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503824",
+            "keyword": [
+                "Health Behavior",
+                "citizen science",
+                "Wildfire smoke",
+                "Smartphone app"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-01-07",
-            "references": [
-                "https://doi.org/10.1029/2019gh000199"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97886,48 +97880,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2019gh000199"
+            ],
+            "rights": null,
+            "title": "Smoke Sense Analysis Data 2017-08-01 Through 2018-01-07 with Identifiers Removed"
         },
         {
-            "title": "2011 results are for Figs 1-4; 2012 results are for Figs 5-8",
-            "description": "The data sets are for Figures 1-8 in the manuscript. \n\nThis dataset is associated with the following publication:\nHuling, J.R., S.G. Huling, and R. Ludwig. Enhanced adsorption of arsenic through the oxidative Treatment of Reduced Aquifer Solids.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 123: 183-191, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1394839",
-            "keyword": [
-                "no additional keywords",
-                "arsenic",
-                "treatment",
-                "permanganate",
-                "oxidation",
-                "ground water"
-            ],
             "contactPoint": {
                 "fn": "Scott Huling",
                 "hasEmail": "mailto:huling.scott@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1394839/documents/Data%20Dictionary%20for%20SDMP_Arsenic%20Immobilization.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The data sets are for Figures 1-8 in the manuscript. \n\nThis dataset is associated with the following publication:\nHuling, J.R., S.G. Huling, and R. Ludwig. Enhanced adsorption of arsenic through the oxidative Treatment of Reduced Aquifer Solids.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 123: 183-191, (2017).",
             "distribution": [
                 {
-                    "title": "SDMP_Arsenic Immobilization_SG Huling_2011_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1394839/SDMP_Arsenic%20Immobilization_SG%20Huling_2011_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SDMP_Arsenic Immobilization_SG Huling_2011_Results.xlsx"
                 },
                 {
-                    "title": "SDMP_Arsenic Immobilization_SG Huling_2012_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1394839/SDMP_Arsenic%20Immobilization_SG%20Huling_2012_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SDMP_Arsenic Immobilization_SG Huling_2012_Results.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1394839",
+            "keyword": [
+                "no additional keywords",
+                "arsenic",
+                "treatment",
+                "permanganate",
+                "oxidation",
+                "ground water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-01",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2017.06.064"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97938,42 +97934,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1394839/documents/Data%20Dictionary%20for%20SDMP_Arsenic%20Immobilization.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.watres.2017.06.064"
+            ],
+            "rights": null,
+            "title": "2011 results are for Figs 1-4; 2012 results are for Figs 5-8"
         },
         {
-            "title": "Fathead minnow growth data",
-            "description": "This dataset provides a time series of size of fathead minnows over time growing under laboratory conditions (approximately 23 C, ad lib feeding). \n\nThis dataset is associated with the following publication:\nSwintek, J., M. Etterson, K. Flynn, and R. Johnson. Optimized temporal sampling designs of the Weibull growth curve with extensions to the von Bertalanffy model.   ENVIRONMETRICS. John Wiley & Sons Incorporated, New York, NY, USA, 30(6): 1-14, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1413281",
-            "keyword": [
-                "Weibull",
-                "growth curve",
-                "study design",
-                "population modeling"
-            ],
             "contactPoint": {
                 "fn": "Matthew Etterson",
                 "hasEmail": "mailto:etterson.matthew@epa.gov"
             },
+            "description": "This dataset provides a time series of size of fathead minnows over time growing under laboratory conditions (approximately 23 C, ad lib feeding). \n\nThis dataset is associated with the following publication:\nSwintek, J., M. Etterson, K. Flynn, and R. Johnson. Optimized temporal sampling designs of the Weibull growth curve with extensions to the von Bertalanffy model.   ENVIRONMETRICS. John Wiley & Sons Incorporated, New York, NY, USA, 30(6): 1-14, (2019).",
             "distribution": [
                 {
-                    "title": "SwintekEtAlSupplementaryData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413281/SwintekEtAlSupplementaryData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SwintekEtAlSupplementaryData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1413281",
+            "keyword": [
+                "Weibull",
+                "growth curve",
+                "study design",
+                "population modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-19",
-            "references": [
-                "https://doi.org/10.1002/env.2552"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -97983,75 +97977,75 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/env.2552"
+            ],
+            "rights": null,
+            "title": "Fathead minnow growth data"
         },
         {
-            "title": "2011 PR Survey data",
-            "description": "EPA conducted a probabilistic survey at 64 stations from linear reef habitat along the southern coastline of Puerto Rico to characterize the regional condition of coral reef inhabitants.  The probabilistic design was the first step toward establishing a long-term monitoring program for biological water quality standards (such as biocriteria) in Puerto Rico using these indicators. The target population was limited to coral reef and hardbottom substrate within 1.5 km o f shore and between 2-12 m depth.\nDivers dropped a buoy at the appropriate station coordinates and assessed the reef resources at the best available habitat within a 20 m radius of the buoy. If suitable habitat was not found, the next location on the predetermined site list was chosen. \n\nThis dataset is associated with the following publication:\nFisher, W., D. Vivian, J. Campbell, C. Lobue, R. Hemmer, S. Wilkinson, P. Harris, D. Santavy, M. Parsons, P. Bradley, A. Humphrey, L. Oliver, and L. Harwell. Biological Status Assessment of Coral Reefs in Southern Puerto Rico: Supporting Coral Reef Protection Under the U.S. Clean Water Act..   Coastal Management. Taylor and Francis, Philadelphia, PA, USA, 47(5): 429-452, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1407509",
-            "keyword": [
-                "Puerto Rico",
-                "stony coral",
-                "coral reef condition",
-                "biocriteria",
-                "proabability-based sampling",
-                "probability based sampling",
-                "reef assessments",
-                "USVI"
-            ],
             "contactPoint": {
                 "fn": "William Fisher",
                 "hasEmail": "mailto:fisher.william@epa.gov"
             },
+            "description": "EPA conducted a probabilistic survey at 64 stations from linear reef habitat along the southern coastline of Puerto Rico to characterize the regional condition of coral reef inhabitants.  The probabilistic design was the first step toward establishing a long-term monitoring program for biological water quality standards (such as biocriteria) in Puerto Rico using these indicators. The target population was limited to coral reef and hardbottom substrate within 1.5 km o f shore and between 2-12 m depth.\nDivers dropped a buoy at the appropriate station coordinates and assessed the reef resources at the best available habitat within a 20 m radius of the buoy. If suitable habitat was not found, the next location on the predetermined site list was chosen. \n\nThis dataset is associated with the following publication:\nFisher, W., D. Vivian, J. Campbell, C. Lobue, R. Hemmer, S. Wilkinson, P. Harris, D. Santavy, M. Parsons, P. Bradley, A. Humphrey, L. Oliver, and L. Harwell. Biological Status Assessment of Coral Reefs in Southern Puerto Rico: Supporting Coral Reef Protection Under the U.S. Clean Water Act..   Coastal Management. Taylor and Francis, Philadelphia, PA, USA, 47(5): 429-452, (2019).",
             "distribution": [
                 {
-                    "title": "StonyCoral_PR2011_FNDec052016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407509/StonyCoral_PR2011_FNDec052016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StonyCoral_PR2011_FNDec052016.xlsx"
                 },
                 {
-                    "title": "StationInfo_PR2011_FDec2016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407509/StationInfo_PR2011_FDec2016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StationInfo_PR2011_FDec2016.xlsx"
                 },
                 {
-                    "title": "SpGorg_PR2011_FJuly032017.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407509/SpGorg_PR2011_FJuly032017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SpGorg_PR2011_FJuly032017.xlsx"
                 },
                 {
-                    "title": "Rugosity_PR2011_FDec052016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407509/Rugosity_PR2011_FDec052016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rugosity_PR2011_FDec052016.xlsx"
                 },
                 {
-                    "title": "Palythoa_PR2011_FJJul032017.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407509/Palythoa_PR2011_FJJul032017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Palythoa_PR2011_FJJul032017.xlsx"
                 },
                 {
-                    "title": "Invert_PR2011_FDec052016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407509/Invert_PR2011_FDec052016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Invert_PR2011_FDec052016.xlsx"
                 },
                 {
-                    "title": "Fish_PR2011_FDec052016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407509/Fish_PR2011_FDec052016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fish_PR2011_FDec052016.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407509",
+            "keyword": [
+                "Puerto Rico",
+                "stony coral",
+                "coral reef condition",
+                "biocriteria",
+                "proabability-based sampling",
+                "probability based sampling",
+                "reef assessments",
+                "USVI"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-18",
-            "references": [
-                "https://doi.org/10.1080/08920753.2019.1641039"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98061,19 +98055,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08920753.2019.1641039"
+            ],
+            "rights": null,
+            "title": "2011 PR Survey data"
         },
         {
-            "title": "Stanley and Wilkin (2019) dataset",
-            "description": "The spreadsheet contains mineralogical and solubility data for the uranyl minerals: metaschoepite and uranophane. \n\nThis dataset is associated with the following publication:\nStanley, D.M., and R.T. Wilkin. Solution equilibria of uranyl minerals: Role of the common groundwater ions calcium and carbonate.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 377: 315-320, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Richard Wilkin",
+                "hasEmail": "mailto:wilkin.rick@epa.gov"
+            },
+            "description": "The spreadsheet contains mineralogical and solubility data for the uranyl minerals: metaschoepite and uranophane. \n\nThis dataset is associated with the following publication:\nStanley, D.M., and R.T. Wilkin. Solution equilibria of uranyl minerals: Role of the common groundwater ions calcium and carbonate.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 377: 315-320, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503429/Stanley%20and%20Wilkin%20%282019%29%20dataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Stanley and Wilkin (2019) dataset.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503429",
             "keyword": [
@@ -98084,20 +98088,10 @@
                 "iron sulfides",
                 "uranium"
             ],
-            "contactPoint": {
-                "fn": "Richard Wilkin",
-                "hasEmail": "mailto:wilkin.rick@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Stanley and Wilkin (2019) dataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503429/Stanley%20and%20Wilkin%20%282019%29%20dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-27",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2019.05.101"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98107,51 +98101,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2019.05.101"
+            ],
+            "rights": null,
+            "title": "Stanley and Wilkin (2019) dataset"
         },
         {
-            "title": "Impacts of chemical oxidation reagents on soil microbes in remediation of polycyclic aromatic hydrocarbon-contaminated soil",
-            "description": "The dataset describes physical and chemical properties of soils used in the study, removal efficiencies of PAHs, changes of microbe counts in soil after oxidation treatments, and concentrations of total PAHs in soil after oxidation treatments. \n\nThis dataset is associated with the following publication:\nLiao, X., Z. Wu, Y. Li, H. Cao, and C. Su. Effect of various chemical oxidation reagents on soil indigenous microbial diversity in remediation of soil contaminated by PAHs.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 226: 483-491, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504162",
-            "keyword": [
-                "PAHs",
-                "Chemical oxidation",
-                "microorganism",
-                "diversity"
-            ],
             "contactPoint": {
                 "fn": "Chunming Su",
                 "hasEmail": "mailto:su.chunming@epa.gov"
             },
+            "description": "The dataset describes physical and chemical properties of soils used in the study, removal efficiencies of PAHs, changes of microbe counts in soil after oxidation treatments, and concentrations of total PAHs in soil after oxidation treatments. \n\nThis dataset is associated with the following publication:\nLiao, X., Z. Wu, Y. Li, H. Cao, and C. Su. Effect of various chemical oxidation reagents on soil indigenous microbial diversity in remediation of soil contaminated by PAHs.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 226: 483-491, (2019).",
             "distribution": [
                 {
-                    "title": "Xiaoyong Liao Chemosphere 2019 paper microbe counts & PAH concentrations 719.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504162/Xiaoyong%20Liao%20Chemosphere%202019%20paper%20microbe%20counts%20%26%20PAH%20concentrations%20719.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Xiaoyong Liao Chemosphere 2019 paper microbe counts & PAH concentrations 719.xlsx"
                 },
                 {
-                    "title": "Xiaoyong Liao Chemosphere 2019 paper 2 tables 719.doc",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504162/Xiaoyong%20Liao%20Chemosphere%202019%20paper%202%20tables%20719.doc",
-                    "mediaType": "application/msword"
+                    "mediaType": "application/msword",
+                    "title": "Xiaoyong Liao Chemosphere 2019 paper 2 tables 719.doc"
                 },
                 {
-                    "title": "Xiaoyong Liao Chemosphere 2019 paper 6 figures 719.doc",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504162/Xiaoyong%20Liao%20Chemosphere%202019%20paper%206%20figures%20719.doc",
-                    "mediaType": "application/msword"
+                    "mediaType": "application/msword",
+                    "title": "Xiaoyong Liao Chemosphere 2019 paper 6 figures 719.doc"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504162",
+            "keyword": [
+                "PAHs",
+                "Chemical oxidation",
+                "microorganism",
+                "diversity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-31",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2019.03.126"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98161,41 +98155,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2019.03.126"
+            ],
+            "rights": null,
+            "title": "Impacts of chemical oxidation reagents on soil microbes in remediation of polycyclic aromatic hydrocarbon-contaminated soil"
         },
         {
-            "title": "ORD-026626: Assessment of the performance of the TGx-DDI biomarker to detect DNA damage-inducing agents using quantitative RT- PCR in TK6 cells ",
-            "description": "The dataset shows the results of the Running Fisher test between the TGx-DDI biomarker and each of the qPCR-generated gene lists from chemical treatments in TK6 cells. The results are divided into training and test sets. \n\nThis dataset is associated with the following publication:\nCho, E., J. Buick, A. Williams, R. Chen, H. Li, C. Corton, A. Fornace, J. Aubrecht, and C. Yauk. Assessment of the performance of the TGx-DDI biomarker to detect DNA damage-inducing agents using quantitative RT- PCR in TK6 cells.   ENVIRONMENTAL AND MOLECULAR MUTAGENESIS. John Wiley & Sons, Inc, Hoboken, NJ, USA, 60(2): 122-133, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1500453",
-            "keyword": [
-                "genotoxicity testing",
-                "biomarker",
-                "high throughput testing",
-                "TGx-DDI"
-            ],
             "contactPoint": {
                 "fn": "Jon Corton",
                 "hasEmail": "mailto:corton.chris@epa.gov"
             },
+            "description": "The dataset shows the results of the Running Fisher test between the TGx-DDI biomarker and each of the qPCR-generated gene lists from chemical treatments in TK6 cells. The results are divided into training and test sets. \n\nThis dataset is associated with the following publication:\nCho, E., J. Buick, A. Williams, R. Chen, H. Li, C. Corton, A. Fornace, J. Aubrecht, and C. Yauk. Assessment of the performance of the TGx-DDI biomarker to detect DNA damage-inducing agents using quantitative RT- PCR in TK6 cells.   ENVIRONMENTAL AND MOLECULAR MUTAGENESIS. John Wiley & Sons, Inc, Hoboken, NJ, USA, 60(2): 122-133, (2019).",
             "distribution": [
                 {
-                    "title": "Data submission for A-4tmz.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500453/Data%20submission%20for%20A-4tmz.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-4tmz.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500453",
+            "keyword": [
+                "genotoxicity testing",
+                "biomarker",
+                "high throughput testing",
+                "TGx-DDI"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-15",
-            "references": [
-                "https://doi.org/10.1002/em.22257"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98205,19 +98199,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/em.22257"
+            ],
+            "rights": null,
+            "title": "ORD-026626: Assessment of the performance of the TGx-DDI biomarker to detect DNA damage-inducing agents using quantitative RT- PCR in TK6 cells "
         },
         {
-            "title": "Trends in the oxidation and relative volatility of  chamber-generated secondary organic aerosol ",
-            "description": "The relationship between the oxidation state and relative volatility of secondary organic aerosol (SOA) from the oxidation of a wide range of hydrocarbons is investigated using a fast-stepping, scanning thermodenuder interfaced with a high resolution time-of-flight aerosol mass spectrometer (AMS). SOA oxidation state varied widely across the investigated range of parent hydrocarbons but was relatively stable for replicate experiments using a single hydrocarbon precursor. On average, unit mass resolution indicators of SOA oxidation (e.g., AMS f43 and f44) are consistent with previously reported values. Linear regression of H:C vs O:C obtained from parameterization of f43 and f44 and elemental analysis of high resolution spectra in Van Krevelen space both yield a slope of ~0.5 across different SOA types. A similar slope was obtained for a distinct subset of toluene/NOx reactions in which the integrated oxidant exposure was varied to alter oxidation. The relative volatility of different SOA types displays similar variability and is strongly correlated with SOA oxidation state (OSC). On average, relatively low oxidation and volatility were observed for aliphatic alkene (including terpenes) and n-alkane SOA while the opposite is true for mono- and polycyclic aromatic hydrocarbon SOA. Effective enthalpy for total chamber aerosol obtained from volatility differential mobility analysis is also highly correlated with OSC indicating a primary role for oxidation levels in determining the volatility of chamber SOA. Effective enthalpies for chamber SOA are substantially lower than those of neat organic standards but are on the order of those obtained for partially oligomerized glyoxal and methyl glyoxal. \n\nThis dataset is associated with the following publication:\nDocherty, K., E. Corse, M. Jaoui, J. Offenberg, T. Kleindienst, J. Krug, T. Riedel, and M. Lewandowski. Trends in the oxidation and relative volatility of chamber-generated secondary organic aerosol.   AEROSOL SCIENCE AND TECHNOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 52(9): 992-1004, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Michael Lewandowski",
+                "hasEmail": "mailto:lewandowski.michael@epa.gov"
+            },
+            "description": "The relationship between the oxidation state and relative volatility of secondary organic aerosol (SOA) from the oxidation of a wide range of hydrocarbons is investigated using a fast-stepping, scanning thermodenuder interfaced with a high resolution time-of-flight aerosol mass spectrometer (AMS). SOA oxidation state varied widely across the investigated range of parent hydrocarbons but was relatively stable for replicate experiments using a single hydrocarbon precursor. On average, unit mass resolution indicators of SOA oxidation (e.g., AMS f43 and f44) are consistent with previously reported values. Linear regression of H:C vs O:C obtained from parameterization of f43 and f44 and elemental analysis of high resolution spectra in Van Krevelen space both yield a slope of ~0.5 across different SOA types. A similar slope was obtained for a distinct subset of toluene/NOx reactions in which the integrated oxidant exposure was varied to alter oxidation. The relative volatility of different SOA types displays similar variability and is strongly correlated with SOA oxidation state (OSC). On average, relatively low oxidation and volatility were observed for aliphatic alkene (including terpenes) and n-alkane SOA while the opposite is true for mono- and polycyclic aromatic hydrocarbon SOA. Effective enthalpy for total chamber aerosol obtained from volatility differential mobility analysis is also highly correlated with OSC indicating a primary role for oxidation levels in determining the volatility of chamber SOA. Effective enthalpies for chamber SOA are substantially lower than those of neat organic standards but are on the order of those obtained for partially oligomerized glyoxal and methyl glyoxal. \n\nThis dataset is associated with the following publication:\nDocherty, K., E. Corse, M. Jaoui, J. Offenberg, T. Kleindienst, J. Krug, T. Riedel, and M. Lewandowski. Trends in the oxidation and relative volatility of chamber-generated secondary organic aerosol.   AEROSOL SCIENCE AND TECHNOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 52(9): 992-1004, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500926/Docherty_volatility_Figures.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Docherty_volatility_Figures.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500926",
             "keyword": [
@@ -98228,20 +98232,10 @@
                 "air toxics",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Michael Lewandowski",
-                "hasEmail": "mailto:lewandowski.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Docherty_volatility_Figures.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500926/Docherty_volatility_Figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-05",
-            "references": [
-                "https://doi.org/10.1080/02786826.2018.1500014"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98251,63 +98245,65 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/02786826.2018.1500014"
+            ],
+            "rights": null,
+            "title": "Trends in the oxidation and relative volatility of  chamber-generated secondary organic aerosol "
         },
         {
-            "title": "Phosphate recovery from water using cellulose enhanced magnesium carbonate pellets: Kinetics, isotherms, and desorption",
-            "description": "Phosphate recovery from water using cellulose enhanced magnesium carbonate pellets: Kinetics, isotherms, and desorption. \n\nThis dataset is associated with the following publication:\nMartin, E., J. Lalley, W. Wang, M. Nadagouda, E. Sahle-Demessie, and S. Chae. Phosphate recovery from water using cellulose enhanced magnesium carbonate pellets: Kinetics, isotherms, and desorption.   Chemical Engineering Journal. Elsevier BV, AMSTERDAM,  NETHERLANDS, 352: 612-624, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1434491",
-            "keyword": [
-                "phosphorus",
-                "Magnesium carbonate",
-                "cellulose",
-                "adsorption",
-                "Kinetics and sorption isotherms",
-                "Recovery of phosphate from water"
-            ],
             "contactPoint": {
                 "fn": "Mallikarjuna Nadagouda",
                 "hasEmail": "mailto:nadagouda.mallikarjuna@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434491/documents/All%20Data%20files.zip",
+            "describedByType": "application/zip",
+            "description": "Phosphate recovery from water using cellulose enhanced magnesium carbonate pellets: Kinetics, isotherms, and desorption. \n\nThis dataset is associated with the following publication:\nMartin, E., J. Lalley, W. Wang, M. Nadagouda, E. Sahle-Demessie, and S. Chae. Phosphate recovery from water using cellulose enhanced magnesium carbonate pellets: Kinetics, isotherms, and desorption.   Chemical Engineering Journal. Elsevier BV, AMSTERDAM,  NETHERLANDS, 352: 612-624, (2018).",
             "distribution": [
                 {
-                    "title": "DraftProduct_ChemicalEngJournalArticle_edited2.0.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434491/DraftProduct_ChemicalEngJournalArticle_edited2.0.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "DraftProduct_ChemicalEngJournalArticle_edited2.0.docx"
                 },
                 {
-                    "title": "Abstract CERMACS 2016-Revised_ChaeandMartin.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434491/Abstract%20CERMACS%202016-Revised_ChaeandMartin.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Abstract CERMACS 2016-Revised_ChaeandMartin.docx"
                 },
                 {
-                    "title": "HASP 2016-066 FINAL.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434491/HASP%202016-066%20FINAL.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "HASP 2016-066 FINAL.pdf"
                 },
                 {
-                    "title": "Thesis_EMartin_3.8.2017.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434491/Thesis_EMartin_3.8.2017.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Thesis_EMartin_3.8.2017.pdf"
                 },
                 {
-                    "title": "All Data files.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434491/All%20Data%20files.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "All Data files.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434491",
+            "keyword": [
+                "phosphorus",
+                "Magnesium carbonate",
+                "cellulose",
+                "adsorption",
+                "Kinetics and sorption isotherms",
+                "Recovery of phosphate from water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-25",
-            "references": [
-                "https://doi.org/10.1016/j.cej.2018.06.183"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98318,20 +98314,32 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434491/documents/All%20Data%20files.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.1016/j.cej.2018.06.183"
+            ],
+            "rights": null,
+            "title": "Phosphate recovery from water using cellulose enhanced magnesium carbonate pellets: Kinetics, isotherms, and desorption"
         },
         {
-            "title": "Vapor-pressure pathways initiate but hydrolysis products dominate the aerosol estimated from organic nitrates  ",
-            "description": "The data includes (1) one zip file of CMAQ code used for simulations in the manuscript and (2) a link to field data (total alkyl nitrates) used for evaluation. See S-T13-TNO2ANsPNsTDLIF_CTR_20130601_RE.ict at the link for measurement information. For other information, please contact the corresponding authors Havala Pye (pye.havala@epa.gov) and Ron Cohen. \n\nThis dataset is associated with the following publication:\nZare, A., K. Fahey, G. Sarwar, R. Cohen, and H. Pye. Vapor-Pressure Pathways Initiate but Hydrolysis Products Dominate the Aerosol Estimated from Organic Nitrates.   ACS Earth and Space Chemistry. American Chemical Society, Washington, DC, USA, 3(8): 1426-1437, (2019).",
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
+            "description": "The data includes (1) one zip file of CMAQ code used for simulations in the manuscript and (2) a link to field data (total alkyl nitrates) used for evaluation. See S-T13-TNO2ANsPNsTDLIF_CTR_20130601_RE.ict at the link for measurement information. For other information, please contact the corresponding authors Havala Pye (pye.havala@epa.gov) and Ron Cohen. \n\nThis dataset is associated with the following publication:\nZare, A., K. Fahey, G. Sarwar, R. Cohen, and H. Pye. Vapor-Pressure Pathways Initiate but Hydrolysis Products Dominate the Aerosol Estimated from Organic Nitrates.   ACS Earth and Space Chemistry. American Chemical Society, Washington, DC, USA, 3(8): 1426-1437, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503432/BLD_CMAQv52_newstruc_Aqcloud_Feb2019_V2-20190625T183020Z.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "BLD_CMAQv52_newstruc_Aqcloud_Feb2019_V2-20190625T183020Z.zip"
+                },
+                {
+                    "accessURL": "https://esrl.noaa.gov/csd/groups/csd7/measurements/2013senex/",
+                    "title": "https://esrl.noaa.gov/csd/groups/csd7/measurements/2013senex/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503432",
             "keyword": [
@@ -98350,24 +98358,10 @@
                 "Semivolatile Organic Compounds (SVOCs)",
                 "Biogenic VOC"
             ],
-            "contactPoint": {
-                "fn": "Havala Pye",
-                "hasEmail": "mailto:pye.havala@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "BLD_CMAQv52_newstruc_Aqcloud_Feb2019_V2-20190625T183020Z.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503432/BLD_CMAQv52_newstruc_Aqcloud_Feb2019_V2-20190625T183020Z.zip",
-                    "mediaType": "application/x-zip-compressed"
-                },
-                {
-                    "title": "https://esrl.noaa.gov/csd/groups/csd7/measurements/2013senex/",
-                    "accessURL": "https://esrl.noaa.gov/csd/groups/csd7/measurements/2013senex/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-25",
-            "references": [
-                "https://doi.org/10.1021/acsearthspacechem.9b00067"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98377,41 +98371,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acsearthspacechem.9b00067"
+            ],
+            "rights": null,
+            "title": "Vapor-pressure pathways initiate but hydrolysis products dominate the aerosol estimated from organic nitrates  "
         },
         {
-            "title": "CitySpace Dataset",
-            "description": "High frequency PM2.5 and meteorological data from a sensor network in the Memphis, TN geographic area. \n\nThis dataset is associated with the following publication:\nFeinberg, S., R. Williams, G. Hagler, J. Low, L. Smith, R. Brown, D. Garver, M. Davis, M. Morton, J. Schaefer, and J. Campbell. Examining spatiotemporal variability of urban particulate matter and application of high-time resolution data from a network of low-cost air pollution sensors.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 213: 579-584, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503287",
-            "keyword": [
-                "low cost sensor",
-                "CitySpace",
-                "Memphis TN",
-                "Fine Particulate Matter"
-            ],
             "contactPoint": {
                 "fn": "Ronald Williams",
                 "hasEmail": "mailto:williams.ronald@epa.gov"
             },
+            "description": "High frequency PM2.5 and meteorological data from a sensor network in the Memphis, TN geographic area. \n\nThis dataset is associated with the following publication:\nFeinberg, S., R. Williams, G. Hagler, J. Low, L. Smith, R. Brown, D. Garver, M. Davis, M. Morton, J. Schaefer, and J. Campbell. Examining spatiotemporal variability of urban particulate matter and application of high-time resolution data from a network of low-cost air pollution sensors.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 213: 579-584, (2019).",
             "distribution": [
                 {
-                    "title": "CitySpace_Database.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503287/CitySpace_Database.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CitySpace_Database.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503287",
+            "keyword": [
+                "low cost sensor",
+                "CitySpace",
+                "Memphis TN",
+                "Fine Particulate Matter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-10-01",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2019.06.026"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98421,19 +98415,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2019.06.026"
+            ],
+            "rights": null,
+            "title": "CitySpace Dataset"
         },
         {
-            "title": "Rubbertown NGEM Demo Project paper 1 dataset",
-            "description": "This dataset contains information used to develop the graphs contained in the journal article \"Rubbertown Next Generation Demonstration Project\"  It contains passive sampler data for one year and select SPod Fenceline senor and Gas Chromatograph data associated with two emissions events described in the paper. \n\nThis dataset is associated with the following publication:\nThoma, E., I. George, R. Duvall, T. Wu, D. Whitaker, K. Oliver, S. Mukerjee, H. Brantley, J. Spann, T. Bell, N. CarltonCarew, P. Deshmukh, J. Cansler, T. Cousett, T. Wei, A. Cooley, K. Zimmerman, B. Dewitt, and B. Parris. Rubbertown Next Generation Emissions Measurements Demonstration Project June 2019.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 16(11): 19, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Eben Thoma",
+                "hasEmail": "mailto:thoma.eben@epa.gov"
+            },
+            "description": "This dataset contains information used to develop the graphs contained in the journal article \"Rubbertown Next Generation Demonstration Project\"  It contains passive sampler data for one year and select SPod Fenceline senor and Gas Chromatograph data associated with two emissions events described in the paper. \n\nThis dataset is associated with the following publication:\nThoma, E., I. George, R. Duvall, T. Wu, D. Whitaker, K. Oliver, S. Mukerjee, H. Brantley, J. Spann, T. Bell, N. CarltonCarew, P. Deshmukh, J. Cansler, T. Cousett, T. Wei, A. Cooley, K. Zimmerman, B. Dewitt, and B. Parris. Rubbertown Next Generation Emissions Measurements Demonstration Project June 2019.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 16(11): 19, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503645/Rubbertown%20NGEM%20Paper%201_032619.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rubbertown NGEM Paper 1_032619.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503645",
             "keyword": [
@@ -98449,20 +98453,10 @@
                 "HAP",
                 "Odor"
             ],
-            "contactPoint": {
-                "fn": "Eben Thoma",
-                "hasEmail": "mailto:thoma.eben@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Rubbertown NGEM Paper 1_032619.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503645/Rubbertown%20NGEM%20Paper%201_032619.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-26",
-            "references": [
-                "https://doi.org/10.3390/ijerph16112041"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98472,68 +98466,68 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ijerph16112041"
+            ],
+            "rights": null,
+            "title": "Rubbertown NGEM Demo Project paper 1 dataset"
         },
         {
-            "title": "KC-TRAQS Methods and Measurements",
-            "description": "Data collected during the Kansas City Transportation and Local-Scale Air\nQuality Study (KC-TRAQS). \n\nThis dataset is associated with the following publication:\nKimbrough, S., S. Krabbe, R. Baldauf, T. Barzyk, M. Brown, S. Brown, C. Croghan, M. Davis, P. Deshmukh, R. Duvall, S. Feinberg, V. Isakov, R. Logan, T. McArthur, and A. Shields. Characterizing Community Air Pollution Impacts Near Complex Sources: The Kansas City Transportation and Local-Scale Air Quality Study (KC-TRAQS).   Chemosensors. MDPI AG, Basel,  SWITZERLAND, 7(2): x, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504005",
-            "keyword": [
-                "KC-TRAQS",
-                "near source",
-                "Black Carbon",
-                "pm2.5",
-                "Sensors",
-                "rail"
-            ],
             "contactPoint": {
                 "fn": "Evelyn Kimbrough",
                 "hasEmail": "mailto:kimbrough.sue@epa.gov"
             },
+            "description": "Data collected during the Kansas City Transportation and Local-Scale Air\nQuality Study (KC-TRAQS). \n\nThis dataset is associated with the following publication:\nKimbrough, S., S. Krabbe, R. Baldauf, T. Barzyk, M. Brown, S. Brown, C. Croghan, M. Davis, P. Deshmukh, R. Duvall, S. Feinberg, V. Isakov, R. Logan, T. McArthur, and A. Shields. Characterizing Community Air Pollution Impacts Near Complex Sources: The Kansas City Transportation and Local-Scale Air Quality Study (KC-TRAQS).   Chemosensors. MDPI AG, Basel,  SWITZERLAND, 7(2): x, (2019).",
             "distribution": [
                 {
-                    "title": "Figure2_meteorologicaldata.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504005/Figure2_meteorologicaldata.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Figure2_meteorologicaldata.zip"
                 },
                 {
-                    "title": "Figure3Data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504005/Figure3Data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure3Data.csv"
                 },
                 {
-                    "title": "Figure 4 BoxPlots pm25.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504005/Figure%204%20BoxPlots%20pm25.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 4 BoxPlots pm25.xlsx"
                 },
                 {
-                    "title": "Figure 5 BoxPlots BC.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504005/Figure%205%20BoxPlots%20BC.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 5 BoxPlots BC.xlsx"
                 },
                 {
-                    "title": "Figure 8 and 9 (SiteName, Hour).csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504005/Figure%208%20and%209%20%28SiteName%2C%20Hour%29.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure 8 and 9 (SiteName, Hour).csv"
                 },
                 {
-                    "title": "Figures 6 and 7.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504005/Figures%206%20and%207.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figures 6 and 7.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504005",
+            "keyword": [
+                "KC-TRAQS",
+                "near source",
+                "Black Carbon",
+                "pm2.5",
+                "Sensors",
+                "rail"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-26",
-            "references": [
-                "https://doi.org/10.3390/chemosensors7020026"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98543,19 +98537,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/chemosensors7020026"
+            ],
+            "rights": null,
+            "title": "KC-TRAQS Methods and Measurements"
         },
         {
-            "title": "Particulate matter, nitrogen oxides, ozone and select volatile organic compounds during a winter sampling period in Logan, Utah, USA",
-            "description": "Particulate matter mass (PM), trace gaseous pollutants, select volatile organic compounds, and meteorology. \n\nThis dataset is associated with the following publication:\nMukerjee, S., L. Smith, R. Long, W. Lonneman, S. Kaushik, M. Colon, K. Oliver, and D. Whitaker. Particulate matter, nitrogen oxides, ozone, and select volatile organic compounds during a winter sampling period in Logan, Utah, USA.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 69(6): 778-788, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Russell Long",
+                "hasEmail": "mailto:long.russell@epa.gov"
+            },
+            "description": "Particulate matter mass (PM), trace gaseous pollutants, select volatile organic compounds, and meteorology. \n\nThis dataset is associated with the following publication:\nMukerjee, S., L. Smith, R. Long, W. Lonneman, S. Kaushik, M. Colon, K. Oliver, and D. Whitaker. Particulate matter, nitrogen oxides, ozone, and select volatile organic compounds during a winter sampling period in Logan, Utah, USA.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 69(6): 778-788, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503057/utahPAMS_revised.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "utahPAMS_revised.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503057",
             "keyword": [
@@ -98566,20 +98570,10 @@
                 "Logan",
                 "Utah"
             ],
-            "contactPoint": {
-                "fn": "Russell Long",
-                "hasEmail": "mailto:long.russell@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "utahPAMS_revised.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503057/utahPAMS_revised.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-14",
-            "references": [
-                "https://doi.org/10.1080/10962247.2019.1587553"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98589,19 +98583,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10962247.2019.1587553"
+            ],
+            "rights": null,
+            "title": "Particulate matter, nitrogen oxides, ozone and select volatile organic compounds during a winter sampling period in Logan, Utah, USA"
         },
         {
-            "title": "Increasing importance of organosulfur species for aerosol properties and future air quality",
-            "description": "Link to IMPROVE network ambient data used in Figure 2a. \n\nThis dataset is associated with the following publication:\nRiva, M., Y. Chen, Y. Zhang, Z. Lei, N.E. Olson, H.C. Boyer, S. Narayan, L.D. Yee, H.S. Green, T. Cui, Z. Zhang, K. Baumann, M. Fort, E. Edgerton, S.H. Budisulistiorini, C.A. Rose, I.O. Ribeiro, R.L. e Oliveira, E.O. dos Santos, C.M.D. Machado, S. Szopa, Y. Zhao, E.G. Alves, S.S. de S\u00e1, W. Hu, E.M. Knipping, S.L. Shaw, S. Duvoisin Junior, R.A.F. de Souza, B.B. Palm, J. Jimenez, M. Glasius, A.H. Goldstein, H. Pye, A. Gold, B.J. Turpin, W. Vizuete, S.T. Martin, J.A. Thornton, C.S. Dutcher, A.P. Ault, and J.D. Surratt. Increasing Isoprene Epoxydiol-to-Inorganic Sulfate Aerosol Ratio Results in Extensive Conversion of Inorganic Sulfate to Organosulfur Forms: Implications for Aerosol Physicochemical Properties.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(15): 8682-8694, (2019).",
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
+            "description": "Link to IMPROVE network ambient data used in Figure 2a. \n\nThis dataset is associated with the following publication:\nRiva, M., Y. Chen, Y. Zhang, Z. Lei, N.E. Olson, H.C. Boyer, S. Narayan, L.D. Yee, H.S. Green, T. Cui, Z. Zhang, K. Baumann, M. Fort, E. Edgerton, S.H. Budisulistiorini, C.A. Rose, I.O. Ribeiro, R.L. e Oliveira, E.O. dos Santos, C.M.D. Machado, S. Szopa, Y. Zhao, E.G. Alves, S.S. de S\u00e1, W. Hu, E.M. Knipping, S.L. Shaw, S. Duvoisin Junior, R.A.F. de Souza, B.B. Palm, J. Jimenez, M. Glasius, A.H. Goldstein, H. Pye, A. Gold, B.J. Turpin, W. Vizuete, S.T. Martin, J.A. Thornton, C.S. Dutcher, A.P. Ault, and J.D. Surratt. Increasing Isoprene Epoxydiol-to-Inorganic Sulfate Aerosol Ratio Results in Extensive Conversion of Inorganic Sulfate to Organosulfur Forms: Implications for Aerosol Physicochemical Properties.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(15): 8682-8694, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://vista.cira.colostate.edu/Improve/data-page/",
+                    "title": "https://vista.cira.colostate.edu/Improve/data-page/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503133",
             "keyword": [
@@ -98617,19 +98620,10 @@
                 "Semivolatile Organic Compounds (SVOCs)",
                 "Biogenic VOC"
             ],
-            "contactPoint": {
-                "fn": "Havala Pye",
-                "hasEmail": "mailto:pye.havala@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://vista.cira.colostate.edu/Improve/data-page/",
-                    "accessURL": "https://vista.cira.colostate.edu/Improve/data-page/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-13",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b01019"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98639,41 +98633,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b01019"
+            ],
+            "rights": null,
+            "title": "Increasing importance of organosulfur species for aerosol properties and future air quality"
         },
         {
-            "title": "Exhaled Breath Aerosol Data for Paper and Plastic Mask Extracts",
-            "description": "This dataset contains the raw data for the paper and plastic mask extracts. The data include the features identified in positive and negative modes, including the abundance of each feature in the mask samples. \n\nThis dataset is associated with the following publication:\nWallace, M., J. Pleil, and M. Madden. Identifying organic compounds in exhaled breath aerosol: Non-invasive sampling from respirator surfaces and disposable hospital masks.   JOURNAL OF AEROSOL SCIENCE. Elsevier Science Ltd, New York, NY, USA, 137: 10544, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503741",
-            "keyword": [
-                "exhaled breath aerosol",
-                "respiratory masks",
-                "immunochemistry",
-                "liquid chromatography-mass spectrometry"
-            ],
             "contactPoint": {
                 "fn": "Joachim Pleil",
                 "hasEmail": "mailto:pleil.joachim@epa.gov"
             },
+            "description": "This dataset contains the raw data for the paper and plastic mask extracts. The data include the features identified in positive and negative modes, including the abundance of each feature in the mask samples. \n\nThis dataset is associated with the following publication:\nWallace, M., J. Pleil, and M. Madden. Identifying organic compounds in exhaled breath aerosol: Non-invasive sampling from respirator surfaces and disposable hospital masks.   JOURNAL OF AEROSOL SCIENCE. Elsevier Science Ltd, New York, NY, USA, 137: 10544, (2019).",
             "distribution": [
                 {
-                    "title": "EBA Supplemental Table 1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503741/EBA%20Supplemental%20Table%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EBA Supplemental Table 1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503741",
+            "keyword": [
+                "exhaled breath aerosol",
+                "respiratory masks",
+                "immunochemistry",
+                "liquid chromatography-mass spectrometry"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-01-30",
-            "references": [
-                "https://doi.org/10.1016/j.jaerosci.2019.105444"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98683,19 +98677,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jaerosci.2019.105444"
+            ],
+            "rights": null,
+            "title": "Exhaled Breath Aerosol Data for Paper and Plastic Mask Extracts"
         },
         {
-            "title": "PAH Published Dataset",
-            "description": "PAH Published Dataset. \n\nThis dataset is associated with the following publication:\nWallace, M., J. Pleil, D. Whitaker, and K. Oliver. Recovery and reactivity of polycyclic aromatic hydrocarbons collected on selected sorbent tubes and analyzed by thermal desorption-gas chromatography/mass spectrometry.   JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1602: 19-29, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Michelle Wallace",
+                "hasEmail": "mailto:wallace.ariel@epa.gov"
+            },
+            "description": "PAH Published Dataset. \n\nThis dataset is associated with the following publication:\nWallace, M., J. Pleil, D. Whitaker, and K. Oliver. Recovery and reactivity of polycyclic aromatic hydrocarbons collected on selected sorbent tubes and analyzed by thermal desorption-gas chromatography/mass spectrometry.   JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1602: 19-29, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503641/PAH%20Published%20Dataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PAH Published Dataset.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503641",
             "keyword": [
@@ -98706,20 +98710,10 @@
                 "gas chromatography-mass spectrometry (GC-MS)",
                 "XRO-440"
             ],
-            "contactPoint": {
-                "fn": "Michelle Wallace",
-                "hasEmail": "mailto:wallace.ariel@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "PAH Published Dataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503641/PAH%20Published%20Dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-12",
-            "references": [
-                "https://doi.org/10.1016/j.chroma.2019.05.030"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98729,19 +98723,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chroma.2019.05.030"
+            ],
+            "rights": null,
+            "title": "PAH Published Dataset"
         },
         {
-            "title": "Wetlands and Watershed Nutrients: Dataset for Manuscript",
-            "description": "The dataset includes information to make Figure 4 within the manuscript. \n\nThis dataset is associated with the following publication:\nGolden, H., A. Rajib, C. Lane, J. Christensen, Q. Wu, and S. Mengistu. Non-floodplain Wetlands Affect Watershed Nutrient Dynamics: A Critical Review.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(13): 7203-7214, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Heather Golden",
+                "hasEmail": "mailto:golden.heather@epa.gov"
+            },
+            "description": "The dataset includes information to make Figure 4 within the manuscript. \n\nThis dataset is associated with the following publication:\nGolden, H., A. Rajib, C. Lane, J. Christensen, Q. Wu, and S. Mengistu. Non-floodplain Wetlands Affect Watershed Nutrient Dynamics: A Critical Review.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(13): 7203-7214, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503205/Golden2019ES%26TScienceHubSubmission_12.18.18.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Golden2019ES&TScienceHubSubmission_12.18.18.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503205",
             "keyword": [
@@ -98752,20 +98756,10 @@
                 "nitrogen",
                 "phosphorus"
             ],
-            "contactPoint": {
-                "fn": "Heather Golden",
-                "hasEmail": "mailto:golden.heather@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Golden2019ES&TScienceHubSubmission_12.18.18.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503205/Golden2019ES%26TScienceHubSubmission_12.18.18.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-11-27",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b07270"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98775,19 +98769,32 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b07270"
+            ],
+            "rights": null,
+            "title": "Wetlands and Watershed Nutrients: Dataset for Manuscript"
         },
         {
-            "title": "Development, validation and integration of in silico models to identify androgen active chemicals",
-            "description": "A diverse data set of 1667 chemicals with AR experimental activity were provided by the U.S. EPA from the oxicity Forecaster (ToxCast) program which generates data using in vitro high-throughput screening (HTS) assays measuring activity of chemicals at multiple points along the androgen receptor (AR) activity pathway.  The Endocrine Disruptor Knowledgebase (EDKB) androgen receptor (AR) binding data set (Fang et al., 2003) was downloaded from the FDA website and was produced expressly as a training set designed for developing predictive models. The data is based on a validated assay using recombinant AR. The dataset contains 146 AR binders and 56 non-AR binders. These training set chemicals were selected for both chemical structure diversity and range of activity, both of which are essential to develop robust QSAR and other models (Perkins, 2003). \n\nThis dataset is associated with the following publication:\nManganelli, S., A. Roncaglioni, K. Mansouri, R. Judson, E. Benfenati, A. Manganaro, and P. Ruiz. Development, validation and integration of in silico models to identify androgen active chemicals.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 220: 204-215, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Richard Judson",
+                "hasEmail": "mailto:judson.richard@epa.gov"
+            },
+            "description": "A diverse data set of 1667 chemicals with AR experimental activity were provided by the U.S. EPA from the oxicity Forecaster (ToxCast) program which generates data using in vitro high-throughput screening (HTS) assays measuring activity of chemicals at multiple points along the androgen receptor (AR) activity pathway.  The Endocrine Disruptor Knowledgebase (EDKB) androgen receptor (AR) binding data set (Fang et al., 2003) was downloaded from the FDA website and was produced expressly as a training set designed for developing predictive models. The data is based on a validated assay using recombinant AR. The dataset contains 146 AR binders and 56 non-AR binders. These training set chemicals were selected for both chemical structure diversity and range of activity, both of which are essential to develop robust QSAR and other models (Perkins, 2003). \n\nThis dataset is associated with the following publication:\nManganelli, S., A. Roncaglioni, K. Mansouri, R. Judson, E. Benfenati, A. Manganaro, and P. Ruiz. Development, validation and integration of in silico models to identify androgen active chemicals.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 220: 204-215, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://cran.r-project.org/web/packages/tcpl/index.html",
+                    "title": "https://cran.r-project.org/web/packages/tcpl/index.html"
+                },
+                {
+                    "accessURL": "https://www.fda.gov/science-research/bioinformatics-tools/endocrine-disruptor-knowledge-base",
+                    "title": "https://www.fda.gov/science-research/bioinformatics-tools/endocrine-disruptor-knowledge-base"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503185",
             "keyword": [
@@ -98800,23 +98807,10 @@
                 "decision tree",
                 "ACToR"
             ],
-            "contactPoint": {
-                "fn": "Richard Judson",
-                "hasEmail": "mailto:judson.richard@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://cran.r-project.org/web/packages/tcpl/index.html",
-                    "accessURL": "https://cran.r-project.org/web/packages/tcpl/index.html"
-                },
-                {
-                    "title": "https://www.fda.gov/science-research/bioinformatics-tools/endocrine-disruptor-knowledge-base",
-                    "accessURL": "https://www.fda.gov/science-research/bioinformatics-tools/endocrine-disruptor-knowledge-base"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-06",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2018.12.131"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98826,19 +98820,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2018.12.131"
+            ],
+            "rights": null,
+            "title": "Development, validation and integration of in silico models to identify androgen active chemicals"
         },
         {
-            "title": "Predicting Estrogenicity of a Group of Substituted Phenols_IATA",
-            "description": "Data are summarized in a two-dimensional data matrix that was developed for each substance for hazard characterization (Tables S1\u2013S3). In the horizontal direction of the matrix, read-across of the target phenol to the source analogues was performed for the purpose of data-gap filling, whereas in the vertical direction, data from different streams (traditional and NAM) were compared and contrasted, to evaluate concordance of orthogonal approaches for evaluating potential estrogenicity. The greater the degree of agreement in orthogonal approaches for determining bioactivity, the greater the confidence one has in using the collective results of such NAMs in hazard characterization of the target phenol. \n\nThis dataset is associated with the following publication:\nWebster, F., M. Gagne, G. Patlewicz, P. Pradeep, N. Trefiak, R. Judson, and T. Barton-Maclaren. Predicting estrogen receptor activation by a group of substituted phenols: An integrated approach to testing and assessment case study.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 106: 278-291, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Richard Judson",
+                "hasEmail": "mailto:judson.richard@epa.gov"
+            },
+            "description": "Data are summarized in a two-dimensional data matrix that was developed for each substance for hazard characterization (Tables S1\u2013S3). In the horizontal direction of the matrix, read-across of the target phenol to the source analogues was performed for the purpose of data-gap filling, whereas in the vertical direction, data from different streams (traditional and NAM) were compared and contrasted, to evaluate concordance of orthogonal approaches for evaluating potential estrogenicity. The greater the degree of agreement in orthogonal approaches for determining bioactivity, the greater the confidence one has in using the collective results of such NAMs in hazard characterization of the target phenol. \n\nThis dataset is associated with the following publication:\nWebster, F., M. Gagne, G. Patlewicz, P. Pradeep, N. Trefiak, R. Judson, and T. Barton-Maclaren. Predicting estrogen receptor activation by a group of substituted phenols: An integrated approach to testing and assessment case study.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 106: 278-291, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503435/Supplemental%20Table%20S1.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental Table S1.xlsx"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503435/Supplemental%20Table%20S2.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental Table S2.xlsx"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503435/Supplemental%20Table%20S3.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental Table S3.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503435",
             "keyword": [
@@ -98855,30 +98869,10 @@
                 "Bioactivity exposure ratio (BER)",
                 "ACToR"
             ],
-            "contactPoint": {
-                "fn": "Richard Judson",
-                "hasEmail": "mailto:judson.richard@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Supplemental Table S1.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503435/Supplemental%20Table%20S1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "Supplemental Table S2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503435/Supplemental%20Table%20S2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "Supplemental Table S3.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503435/Supplemental%20Table%20S3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-28",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2019.05.017"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98888,40 +98882,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2019.05.017"
+            ],
+            "rights": null,
+            "title": "Predicting Estrogenicity of a Group of Substituted Phenols_IATA"
         },
         {
-            "title": "No data",
-            "description": "There is no dataset. \n\nThis dataset is associated with the following publication:\nLutes, C., C. Holton, R. Truesdale, J. Zimmerman, and B. Schumacher. Key Design Elements of Building Pressure Cycling for Evaluating Vapor Intrusion\u2014A Literature Review..   Groundwater Monitoring & Remediation. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 39(1): 66-72, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1390096",
-            "keyword": [
-                "vapor intrusion",
-                "remediation",
-                "indoor air"
-            ],
             "contactPoint": {
                 "fn": "Brian Schumacher",
                 "hasEmail": "mailto:schumacher.brian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1390096/documents/No%20EPA%20data%20note.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "There is no dataset. \n\nThis dataset is associated with the following publication:\nLutes, C., C. Holton, R. Truesdale, J. Zimmerman, and B. Schumacher. Key Design Elements of Building Pressure Cycling for Evaluating Vapor Intrusion\u2014A Literature Review..   Groundwater Monitoring & Remediation. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 39(1): 66-72, (2019).",
             "distribution": [
                 {
-                    "title": "No EPA data note.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390096/No%20EPA%20data%20note.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "No EPA data note.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390096",
+            "keyword": [
+                "vapor intrusion",
+                "remediation",
+                "indoor air"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-27",
-            "references": [
-                "https://doi.org/10.1111/gwmr.12310"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98932,38 +98928,36 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1390096/documents/No%20EPA%20data%20note.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1111/gwmr.12310"
+            ],
+            "rights": null,
+            "title": "No data"
         },
         {
-            "title": "ToxRefDB version 2.0: Improved utility for predictive and retrospective toxicology analyses",
-            "description": "ToxRefDB comprises information from over fifty years of in vivo toxicity data. The database includes information for over 1000 chemicals, and is being used as a primary source of data for evaluating efforts of the ToxCast program [4,5], as well as for numerous predictive and retrospective analyses. \n\nThis dataset is associated with the following publication:\nWatford, S., L. Pham, J. Wignall, R. Shin, M.T. Martin, and K. Friedman. ToxRefDB version 2.0: Improved utility for predictive and retrospective toxicology analyses.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 89: 145-158, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503734",
-            "keyword": [
-                "ACToR"
-            ],
             "contactPoint": {
                 "fn": "Richard Judson",
                 "hasEmail": "mailto:judson.richard@epa.gov"
             },
+            "description": "ToxRefDB comprises information from over fifty years of in vivo toxicity data. The database includes information for over 1000 chemicals, and is being used as a primary source of data for evaluating efforts of the ToxCast program [4,5], as well as for numerous predictive and retrospective analyses. \n\nThis dataset is associated with the following publication:\nWatford, S., L. Pham, J. Wignall, R. Shin, M.T. Martin, and K. Friedman. ToxRefDB version 2.0: Improved utility for predictive and retrospective toxicology analyses.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 89: 145-158, (2019).",
             "distribution": [
                 {
-                    "title": "https://github.com/USEPA/CompTox-ToxRefDB",
-                    "accessURL": "https://github.com/USEPA/CompTox-ToxRefDB"
+                    "accessURL": "https://github.com/USEPA/CompTox-ToxRefDB",
+                    "title": "https://github.com/USEPA/CompTox-ToxRefDB"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503734",
+            "keyword": [
+                "ACToR"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-31",
-            "references": [
-                "https://doi.org/10.1016/j.reprotox.2019.07.012"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -98973,19 +98967,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.reprotox.2019.07.012"
+            ],
+            "rights": null,
+            "title": "ToxRefDB version 2.0: Improved utility for predictive and retrospective toxicology analyses"
         },
         {
-            "title": "National Inventory of Reactive Nitrogen",
-            "description": "The effectiveness of management actions in reducing the release of excess nitrogen (N) to the environment is best assessed if N fluxes across air, land and water are regularly quantified at relevant scales.  This dataset contains comprehensive 2002, 2007, and 2012 inventories of inputs and non-hydrologic N losses along with fossil fuel emissions, food demand, and terrestrial N surpluses for all HUC-8 subbasins of the contiguous United States using peer-reviewed, publicly available datasets. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Christopher Clark",
+                "hasEmail": "mailto:clark.christopher@epa.gov"
+            },
+            "description": "The effectiveness of management actions in reducing the release of excess nitrogen (N) to the environment is best assessed if N fluxes across air, land and water are regularly quantified at relevant scales.  This dataset contains comprehensive 2002, 2007, and 2012 inventories of inputs and non-hydrologic N losses along with fossil fuel emissions, food demand, and terrestrial N surpluses for all HUC-8 subbasins of the contiguous United States using peer-reviewed, publicly available datasets. ",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1418976/National_Nitrogen_Inventory.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "National_Nitrogen_Inventory.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1418976",
             "keyword": [
@@ -98998,19 +99002,11 @@
                 "crop agriculture",
                 "nitrogen deposition"
             ],
-            "contactPoint": {
-                "fn": "Christopher Clark",
-                "hasEmail": "mailto:clark.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "National_Nitrogen_Inventory.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1418976/National_Nitrogen_Inventory.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": null,
+            "programCode": [
+                "020:097"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -99019,41 +99015,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "National Inventory of Reactive Nitrogen"
         },
         {
-            "title": "Mutagenicity Data of Water Extracts",
-            "description": "The dataset contain the primary mutagenicity data.  It consists of the number of mutant colonies (called revertants) per petri plate at each dose of the water extract as used in the Salmonella (Ames) bacterial mutagenicity assay.  The dataset also shows graphically the dose-response curves constructed from the primary data, as well as a table showing the slopes of those curves, which are the mutagenic potencies of the water expressed as revertants/ml-equivalents. \n\nThis dataset is associated with the following publication:\nBerninger, J., D. Demarini, S. Warren, J. Simmons, V. Wilson, J. Conley, M. Armstrong, D. Kolpin, K. Kuivila, T. Reilly, K. Romanok, D. Villeneuve, and P. Bradley. Predictive Analysis Using Chemical-Gene Interaction Networks Consistent with Observed Endocrine Activity and Mutagenicity of U.S. Streams.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(15): 8611-8620, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504446",
-            "keyword": [
-                "U.S. streams",
-                "Mutagenicity",
-                "chemical-gene networks",
-                "Ames assay"
-            ],
             "contactPoint": {
                 "fn": "David Demarini",
                 "hasEmail": "mailto:demarini.david@epa.gov"
             },
+            "description": "The dataset contain the primary mutagenicity data.  It consists of the number of mutant colonies (called revertants) per petri plate at each dose of the water extract as used in the Salmonella (Ames) bacterial mutagenicity assay.  The dataset also shows graphically the dose-response curves constructed from the primary data, as well as a table showing the slopes of those curves, which are the mutagenic potencies of the water expressed as revertants/ml-equivalents. \n\nThis dataset is associated with the following publication:\nBerninger, J., D. Demarini, S. Warren, J. Simmons, V. Wilson, J. Conley, M. Armstrong, D. Kolpin, K. Kuivila, T. Reilly, K. Romanok, D. Villeneuve, and P. Bradley. Predictive Analysis Using Chemical-Gene Interaction Networks Consistent with Observed Endocrine Activity and Mutagenicity of U.S. Streams.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(15): 8611-8620, (2019).",
             "distribution": [
                 {
-                    "title": "USGS Mutagenicity Data 7-2-18 .pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504446/USGS%20Mutagenicity%20Data%207-2-18%20.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "USGS Mutagenicity Data 7-2-18 .pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504446",
+            "keyword": [
+                "U.S. streams",
+                "Mutagenicity",
+                "chemical-gene networks",
+                "Ames assay"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-17",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b02990"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99063,19 +99057,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b02990"
+            ],
+            "rights": null,
+            "title": "Mutagenicity Data of Water Extracts"
         },
         {
-            "title": "Manuscript Data",
-            "description": "The current data set provides all of the data that was used to generate the figures produced in the manuscript. \n\nThis dataset is associated with the following publication:\nClar, J.G., W. Platten III, E. Baumann, A. Remsen, S.M. Harmon, K. Rogers, T.A. Thomas, J. Matheson, and T.P. Luxton. Release and transformation of ZnO nanoparticles used in outdoor surface coatings for UV protection.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 670: 78-86, (2019).",
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
+            "description": "The current data set provides all of the data that was used to generate the figures produced in the manuscript. \n\nThis dataset is associated with the following publication:\nClar, J.G., W. Platten III, E. Baumann, A. Remsen, S.M. Harmon, K. Rogers, T.A. Thomas, J. Matheson, and T.P. Luxton. Release and transformation of ZnO nanoparticles used in outdoor surface coatings for UV protection.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 670: 78-86, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500935/SciHubData.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHubData.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500935",
             "keyword": [
@@ -99087,20 +99091,10 @@
                 "XAFS",
                 "consumer products"
             ],
-            "contactPoint": {
-                "fn": "Todd Luxton",
-                "hasEmail": "mailto:luxton.todd@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SciHubData.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500935/SciHubData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-12-03",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2019.03.189"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99110,65 +99104,65 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2019.03.189"
+            ],
+            "rights": null,
+            "title": "Manuscript Data"
         },
         {
-            "title": "    Denitrification rates across a temperate North Pacific estuary, Yaquina Bay, Oregon",
-            "description": "The extent and temporal variability of denitrification activity was measured in Yaquina Bay, Oregon, over a year using sediment cores collected approximately monthly from August 2003 through August 31, 2004. Denitrification rates in sediments from a marine-dominated intertidal sand flat near the mouth of the estuary averaged 0.181 \u00b10.114 mmol m-2 d-1 whereas sediments in the estuary (5 stations) and river averaged 0.626 \u00b10.141 mmol m-2 d-1.   Sediment cores from all estuarine sites indicated denitrification activity throughout the year and were within the values reported for other temperate estuaries. Denitrification rates decreased with depth from 0.4 mmol m-2 d-1 in the upper 2 to 5 cm of sediment to 0.006 mmol m-2 d-1 at 28 cm sediment depth, indicating denitrification occurred primarily in the upper 5 cm. There was no relationship between denitrification rate and nitrate concentrations in the overlying water column (r2 = 0.16).  Denitrification rates were lowest in areas with low sediment carbon content, particularly in the sandy intertidal areas at the mouth of the estuary (r2 = 0.78). The results suggest that denitrification rates in this estuary were influenced primarily by the availability of organic carbon. \nThe amount of nitrogen removed by denitrification was estimated to be 8.7 percent of the annual Yaquina River load for August 2003 through August 2004. The relatively low percent lost via denitrification may be due to high river discharge when the nitrogen load was greatest during winter storm events and dissolved nitrogen was exported directly from the estuary into the Pacific Ocean. Stable isotopes were used to investigate the carbon source. The carbon isotope data increased from -27 \u03b413C in the freshwater river to -21.5 \u03b413C at the seawater site, reflecting a typical change from terrestrial plant vegetation to phytoplankton carbon sources. Similar values for \u03b413C between suspended and benthic sediments indicated resuspension and mixing occurred during tidal inflow. \n\nThis dataset is associated with the following publication:\nSigleo, A. Denitrification Rates Across a Temperate North Pacific Estuary, Yaquina Bay, Oregon.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 42(3): 655-664, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1430224",
-            "keyword": [
-                "denitrification",
-                "Estuaries",
-                "nitrate",
-                "Nitrogen Ctcle",
-                "Oregon Coast",
-                "Nitrogen and Co-pollutants",
-                "nutrients",
-                "Yaquina Bay"
-            ],
             "contactPoint": {
                 "fn": "Theodore Dewitt",
                 "hasEmail": "mailto:dewitt.ted@epa.gov"
             },
+            "description": "The extent and temporal variability of denitrification activity was measured in Yaquina Bay, Oregon, over a year using sediment cores collected approximately monthly from August 2003 through August 31, 2004. Denitrification rates in sediments from a marine-dominated intertidal sand flat near the mouth of the estuary averaged 0.181 \u00b10.114 mmol m-2 d-1 whereas sediments in the estuary (5 stations) and river averaged 0.626 \u00b10.141 mmol m-2 d-1.   Sediment cores from all estuarine sites indicated denitrification activity throughout the year and were within the values reported for other temperate estuaries. Denitrification rates decreased with depth from 0.4 mmol m-2 d-1 in the upper 2 to 5 cm of sediment to 0.006 mmol m-2 d-1 at 28 cm sediment depth, indicating denitrification occurred primarily in the upper 5 cm. There was no relationship between denitrification rate and nitrate concentrations in the overlying water column (r2 = 0.16).  Denitrification rates were lowest in areas with low sediment carbon content, particularly in the sandy intertidal areas at the mouth of the estuary (r2 = 0.78). The results suggest that denitrification rates in this estuary were influenced primarily by the availability of organic carbon. \nThe amount of nitrogen removed by denitrification was estimated to be 8.7 percent of the annual Yaquina River load for August 2003 through August 2004. The relatively low percent lost via denitrification may be due to high river discharge when the nitrogen load was greatest during winter storm events and dissolved nitrogen was exported directly from the estuary into the Pacific Ocean. Stable isotopes were used to investigate the carbon source. The carbon isotope data increased from -27 \u03b413C in the freshwater river to -21.5 \u03b413C at the seawater site, reflecting a typical change from terrestrial plant vegetation to phytoplankton carbon sources. Similar values for \u03b413C between suspended and benthic sediments indicated resuspension and mixing occurred during tidal inflow. \n\nThis dataset is associated with the following publication:\nSigleo, A. Denitrification Rates Across a Temperate North Pacific Estuary, Yaquina Bay, Oregon.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 42(3): 655-664, (2019).",
             "distribution": [
                 {
-                    "title": "Sigleo-A-nk9x-Figure5-SI Table.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430224/Sigleo-A-nk9x-Figure5-SI%20Table.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Sigleo-A-nk9x-Figure5-SI Table.xlsx"
                 },
                 {
-                    "title": "Sigleo-A-nk9x-Fugure 7-SI Table.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430224/Sigleo-A-nk9x-Fugure%207-SI%20Table.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Sigleo-A-nk9x-Fugure 7-SI Table.xlsx"
                 },
                 {
-                    "title": "Sigleo-A-nk9x-Figure1-SI Table.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430224/Sigleo-A-nk9x-Figure1-SI%20Table.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Sigleo-A-nk9x-Figure1-SI Table.xls"
                 },
                 {
-                    "title": "Sigleo-A-nk9x-Figure2-SI Table.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430224/Sigleo-A-nk9x-Figure2-SI%20Table.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Sigleo-A-nk9x-Figure2-SI Table.xls"
                 },
                 {
-                    "title": "Sigleo-A-nk9x-Figures 3&4-SI Table.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430224/Sigleo-A-nk9x-Figures%203%264-SI%20Table.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Sigleo-A-nk9x-Figures 3&4-SI Table.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1430224",
+            "keyword": [
+                "denitrification",
+                "Estuaries",
+                "nitrate",
+                "Nitrogen Ctcle",
+                "Oregon Coast",
+                "Nitrogen and Co-pollutants",
+                "nutrients",
+                "Yaquina Bay"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-18",
-            "references": [
-                "https://doi.org/10.1007/s12237-019-00516-2"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99178,40 +99172,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12237-019-00516-2"
+            ],
+            "rights": null,
+            "title": "    Denitrification rates across a temperate North Pacific estuary, Yaquina Bay, Oregon"
         },
         {
-            "title": "Data for Harrill et al, Testing for developmental neurotoxicity using a suite of assays for key cellular events in neurodevelopment",
-            "description": "This file contains the data on apoptosis, neurite outgrowth, synaptogenesis and proliferation. \n\nThis dataset is associated with the following publication:\nHarrill, J., T. Freudenrich, K. Wallace, K. Ball, T. Shafer, and W. Mundy. Testing for developmental neurotoxicity using a battery of in vitro assays for key cellular events in neurodevelopment.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 354(1): 24-39, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1407642",
-            "keyword": [
-                "neurodevelopment",
-                "in vitro assays",
-                "alternative methods"
-            ],
             "contactPoint": {
                 "fn": "Timothy Shafer",
                 "hasEmail": "mailto:shafer.tim@epa.gov"
             },
+            "description": "This file contains the data on apoptosis, neurite outgrowth, synaptogenesis and proliferation. \n\nThis dataset is associated with the following publication:\nHarrill, J., T. Freudenrich, K. Wallace, K. Ball, T. Shafer, and W. Mundy. Testing for developmental neurotoxicity using a battery of in vitro assays for key cellular events in neurodevelopment.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 354(1): 24-39, (2018).",
             "distribution": [
                 {
-                    "title": "Harrill et al DNT_Assay Dataset.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407642/Harrill%20et%20al%20DNT_Assay%20Dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Harrill et al DNT_Assay Dataset.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407642",
+            "keyword": [
+                "neurodevelopment",
+                "in vitro assays",
+                "alternative methods"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-21",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2018.04.001"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99221,19 +99215,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2018.04.001"
+            ],
+            "rights": null,
+            "title": "Data for Harrill et al, Testing for developmental neurotoxicity using a suite of assays for key cellular events in neurodevelopment"
         },
         {
-            "title": "Datasets used in RD-023418: Adverse Outcome Pathway-Driven Identification of Rat Hepatocarcinogens in Short-Term Assays ",
-            "description": "Datasets used in RD-023418: Adverse Outcome Pathway-Driven Identification of Rat Hepatocarcinogens in Short-Term Assays. \n\nThis dataset is associated with the following publication:\nRooney, J., T. Hill, C. Qin, F. Sistare, and C. Corton. Adverse outcome pathway-driven identification of rat liver tumorigens in short-term assays.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 356: 99-113, (2018).",
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
+            "description": "Datasets used in RD-023418: Adverse Outcome Pathway-Driven Identification of Rat Hepatocarcinogens in Short-Term Assays. \n\nThis dataset is associated with the following publication:\nRooney, J., T. Hill, C. Qin, F. Sistare, and C. Corton. Adverse outcome pathway-driven identification of rat liver tumorigens in short-term assays.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 356: 99-113, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407628/Data%20submission%20for%20A-dz0q.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-dz0q.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407628",
             "keyword": [
@@ -99248,20 +99252,10 @@
                 "genotoxicity",
                 "microarray"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data submission for A-dz0q.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407628/Data%20submission%20for%20A-dz0q.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-01",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2018.07.023"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99271,19 +99265,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2018.07.023"
+            ],
+            "rights": null,
+            "title": "Datasets used in RD-023418: Adverse Outcome Pathway-Driven Identification of Rat Hepatocarcinogens in Short-Term Assays "
         },
         {
-            "title": "Herb species occurrence data across the US",
-            "description": "This is a dataset of the abundance of herbaceous species across ~15,000 plots across the US, along with related site date (e.g. climate, soil pH, etc.). \n\nThis dataset is associated with the following publication:\nClark, C., S. Simkin, E. Allen, W. Bowman, J. Belnap, M. Brooks, S. Collins, L. Geiser, F. Gilliam, S. Jovan, L. Pardo, B. Schultz, C. Stevens, K. Suding, H. Throop, and D. Waller. Differential vulnerability of 348 herbaceous species to atmospheric deposition of nitrogen and sulfur across the contiguous U.S..   Nature Plants. Nature Publishing Group, New York, NY, USA,  697-705, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Christopher Clark",
+                "hasEmail": "mailto:clark.christopher@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500914/documents/Metadata_gram_forb_abund_and_site_attr_w_no_grad_or_soil_filter_31Mar2016_both_N_and_S.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This is a dataset of the abundance of herbaceous species across ~15,000 plots across the US, along with related site date (e.g. climate, soil pH, etc.). \n\nThis dataset is associated with the following publication:\nClark, C., S. Simkin, E. Allen, W. Bowman, J. Belnap, M. Brooks, S. Collins, L. Geiser, F. Gilliam, S. Jovan, L. Pardo, B. Schultz, C. Stevens, K. Suding, H. Throop, and D. Waller. Differential vulnerability of 348 herbaceous species to atmospheric deposition of nitrogen and sulfur across the contiguous U.S..   Nature Plants. Nature Publishing Group, New York, NY, USA,  697-705, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500914/Data_gram_forb_abund_and_site_attr_w_no_grad_or_soil_filter_31Mar2016_both_N_and_S.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Data_gram_forb_abund_and_site_attr_w_no_grad_or_soil_filter_31Mar2016_both_N_and_S.csv"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500914",
             "keyword": [
@@ -99297,20 +99303,10 @@
                 "native plants",
                 "critical loads"
             ],
-            "contactPoint": {
-                "fn": "Christopher Clark",
-                "hasEmail": "mailto:clark.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data_gram_forb_abund_and_site_attr_w_no_grad_or_soil_filter_31Mar2016_both_N_and_S.csv",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500914/Data_gram_forb_abund_and_site_attr_w_no_grad_or_soil_filter_31Mar2016_both_N_and_S.csv",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-31",
-            "references": [
-                "https://doi.org/10.1038/s41477-019-0442-8"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99321,20 +99317,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500914/documents/Metadata_gram_forb_abund_and_site_attr_w_no_grad_or_soil_filter_31Mar2016_both_N_and_S.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1038/s41477-019-0442-8"
+            ],
+            "rights": null,
+            "title": "Herb species occurrence data across the US"
         },
         {
-            "title": "WSON_Coweeta_Chen et al_2017",
-            "description": "Datasets describing bulk and speciated water soluble organic nitrogen and carbon species in 24 hour high volume PM samples. \n\nThis dataset is associated with the following publication:\nChen, X., X. Mingjie, M. Hays, E. Eric, D. Schwede, and J. Walker. Characterization of organic nitrogen in aerosols at a forest site in the southern Appalachian Mountains May 2018.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, issue}: 6829-6846, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Walker",
+                "hasEmail": "mailto:walker.johnt@epa.gov"
+            },
+            "description": "Datasets describing bulk and speciated water soluble organic nitrogen and carbon species in 24 hour high volume PM samples. \n\nThis dataset is associated with the following publication:\nChen, X., X. Mingjie, M. Hays, E. Eric, D. Schwede, and J. Walker. Characterization of organic nitrogen in aerosols at a forest site in the southern Appalachian Mountains May 2018.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, issue}: 6829-6846, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413517/Coweeta%20hi-vol%20Chen%20et%20al%20for%20science%20hub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Coweeta hi-vol Chen et al for science hub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1413517",
             "keyword": [
@@ -99349,20 +99353,10 @@
                 "sulfur",
                 "micrometeorology"
             ],
-            "contactPoint": {
-                "fn": "John Walker",
-                "hasEmail": "mailto:walker.johnt@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Coweeta hi-vol Chen et al for science hub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413517/Coweeta%20hi-vol%20Chen%20et%20al%20for%20science%20hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-6829-2018"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99372,41 +99366,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-18-6829-2018"
+            ],
+            "rights": null,
+            "title": "WSON_Coweeta_Chen et al_2017"
         },
         {
-            "title": "Pt-XR hyersensitivity data record",
-            "description": "Dataset for figures included in associated publication. \n\nThis dataset is associated with the following publication:\nLehmann, D., and W. Williams. Cross-reactivity between halogenated platinum salts in an immediate-type respiratory hypersensitivity model.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 30(11-12): 472-481, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1502453",
-            "keyword": [
-                "platinum",
-                "hypersenstivity",
-                "allergy",
-                "cross-reactivity"
-            ],
             "contactPoint": {
                 "fn": "David Lehmann",
                 "hasEmail": "mailto:lehmann.david@epa.gov"
             },
+            "description": "Dataset for figures included in associated publication. \n\nThis dataset is associated with the following publication:\nLehmann, D., and W. Williams. Cross-reactivity between halogenated platinum salts in an immediate-type respiratory hypersensitivity model.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 30(11-12): 472-481, (2019).",
             "distribution": [
                 {
-                    "title": "Pt_XR_hypersensitivity_Science Hub_ Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502453/Pt_XR_hypersensitivity_Science%20Hub_%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Pt_XR_hypersensitivity_Science Hub_ Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502453",
+            "keyword": [
+                "platinum",
+                "hypersenstivity",
+                "allergy",
+                "cross-reactivity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-27",
-            "references": [
-                "https://doi.org/10.1080/08958378.2018.1554015"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99416,78 +99410,78 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08958378.2018.1554015"
+            ],
+            "rights": null,
+            "title": "Pt-XR hyersensitivity data record"
         },
         {
-            "title": "Data used in multi-media lead (Pb) meta-analyses. ",
-            "description": "These data were extracted from published literature reporting lead (Pb) concentrations in multiple environmental media (soil, dust, air, water, and food) in the United States from 1996-2016. These data were used in research synthesis efforts. \n\nThis dataset is associated with the following publication:\nFrank, J., A. Poulakos, R. Tornero-Velez, and J. Xue. Systematic review and meta-analyses of lead (Pb) concentrations in environmental media (soil, dust, water, food, and air) reported in the United States from 1996 to 2016.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 694: 133489, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1504013",
-            "keyword": [
-                "multimeda exposure assessment",
-                "heavy metals",
-                "systematic review",
-                "meta-analysis",
-                "random effects model lead (Pb)",
-                "Children's Environmental Health"
-            ],
             "contactPoint": {
                 "fn": "Jessica Frank",
                 "hasEmail": "mailto:frank.jessica@epa.gov"
             },
+            "description": "These data were extracted from published literature reporting lead (Pb) concentrations in multiple environmental media (soil, dust, air, water, and food) in the United States from 1996-2016. These data were used in research synthesis efforts. \n\nThis dataset is associated with the following publication:\nFrank, J., A. Poulakos, R. Tornero-Velez, and J. Xue. Systematic review and meta-analyses of lead (Pb) concentrations in environmental media (soil, dust, water, food, and air) reported in the United States from 1996 to 2016.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 694: 133489, (2019).",
             "distribution": [
                 {
-                    "title": "Supplemental-A-Standards.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/Supplemental-A-Standards.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental-A-Standards.xlsx"
                 },
                 {
-                    "title": "supplemental-C-dust-loading-figures.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/supplemental-C-dust-loading-figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-C-dust-loading-figures.xlsx"
                 },
                 {
-                    "title": "supplemental-D-dust-concentration-figures.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/supplemental-D-dust-concentration-figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-D-dust-concentration-figures.xlsx"
                 },
                 {
-                    "title": "supplemental-F-food-figures.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/supplemental-F-food-figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-F-food-figures.xlsx"
                 },
                 {
-                    "title": "supplemental-B-soil-figures.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/supplemental-B-soil-figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-B-soil-figures.xlsx"
                 },
                 {
-                    "title": "supplemental-G-air-figures.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/supplemental-G-air-figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-G-air-figures.xlsx"
                 },
                 {
-                    "title": "supplemental-E-water.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/supplemental-E-water.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-E-water.xlsx"
                 },
                 {
-                    "title": "supplemental-H-superfund.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504013/supplemental-H-superfund.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-H-superfund.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504013",
+            "keyword": [
+                "multimeda exposure assessment",
+                "heavy metals",
+                "systematic review",
+                "meta-analysis",
+                "random effects model lead (Pb)",
+                "Children's Environmental Health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-01",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2019.07.295"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99497,68 +99491,68 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2019.07.295"
+            ],
+            "rights": null,
+            "title": "Data used in multi-media lead (Pb) meta-analyses. "
         },
         {
-            "title": "Exposure-response arrays for noncancer and cancer endpoints for p,p'-DDD and analogues ",
-            "description": "Data for the exposure-response arrays comparing effect levels for non-cancer and cancer endpoints for p,p'-DDD and analogues were sourced from the links provided. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1502620",
-            "keyword": [
-                "Read-across",
-                "quantitative risk assessment",
-                "toxicokinetics",
-                "in vitro high-throughput screening"
-            ],
             "contactPoint": {
                 "fn": "Lucina Lizarraga",
                 "hasEmail": "mailto:lizarraga.lucina@epa.gov"
             },
+            "description": "Data for the exposure-response arrays comparing effect levels for non-cancer and cancer endpoints for p,p'-DDD and analogues were sourced from the links provided. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "distribution": [
                 {
-                    "title": "https://www.atsdr.cdc.gov/toxprofiles/tp35.pdf",
-                    "accessURL": "https://www.atsdr.cdc.gov/toxprofiles/tp35.pdf"
+                    "accessURL": "https://www.atsdr.cdc.gov/toxprofiles/tp35.pdf",
+                    "title": "https://www.atsdr.cdc.gov/toxprofiles/tp35.pdf"
                 },
                 {
-                    "title": "https://www.atsdr.cdc.gov/toxprofiles/tp47.pdf",
-                    "accessURL": "https://www.atsdr.cdc.gov/toxprofiles/tp47.pdf"
+                    "accessURL": "https://www.atsdr.cdc.gov/toxprofiles/tp47.pdf",
+                    "title": "https://www.atsdr.cdc.gov/toxprofiles/tp47.pdf"
                 },
                 {
-                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0147_summary.pdf",
-                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0147_summary.pdf"
+                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0147_summary.pdf",
+                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0147_summary.pdf"
                 },
                 {
-                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0369_summary.pdf",
-                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0369_summary.pdf"
+                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0369_summary.pdf",
+                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0369_summary.pdf"
                 },
                 {
-                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0328_summary.pdf",
-                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0328_summary.pdf"
+                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0328_summary.pdf",
+                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0328_summary.pdf"
                 },
                 {
-                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0347_summary.pdf",
-                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0347_summary.pdf"
+                    "accessURL": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0347_summary.pdf",
+                    "title": "https://cfpub.epa.gov/ncea/iris/iris_documents/documents/subst/0347_summary.pdf"
                 },
                 {
-                    "title": "https://hhpprtv.ornl.gov/issue_papers/DDEpp.pdf",
-                    "accessURL": "https://hhpprtv.ornl.gov/issue_papers/DDEpp.pdf"
+                    "accessURL": "https://hhpprtv.ornl.gov/issue_papers/DDEpp.pdf",
+                    "title": "https://hhpprtv.ornl.gov/issue_papers/DDEpp.pdf"
                 },
                 {
-                    "title": "https://hhpprtv.ornl.gov/issue_papers/DDDpp.pdf",
-                    "accessURL": "https://hhpprtv.ornl.gov/issue_papers/DDDpp.pdf"
+                    "accessURL": "https://hhpprtv.ornl.gov/issue_papers/DDDpp.pdf",
+                    "title": "https://hhpprtv.ornl.gov/issue_papers/DDDpp.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502620",
+            "keyword": [
+                "Read-across",
+                "quantitative risk assessment",
+                "toxicokinetics",
+                "in vitro high-throughput screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-05",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99568,41 +99562,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            ],
+            "rights": null,
+            "title": "Exposure-response arrays for noncancer and cancer endpoints for p,p'-DDD and analogues "
         },
         {
-            "title": "Analogue search results for p,p'-DDD ",
-            "description": "The dataset contains the outputs for the analogue searches conducted for the chemical of interest, p,p'-DDD. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1502619",
-            "keyword": [
-                "Read-across",
-                "quantitative risk assessment",
-                "toxicokinetics",
-                "in vitro high-throughput screening"
-            ],
             "contactPoint": {
                 "fn": "Lucina Lizarraga",
                 "hasEmail": "mailto:lizarraga.lucina@epa.gov"
             },
+            "description": "The dataset contains the outputs for the analogue searches conducted for the chemical of interest, p,p'-DDD. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "distribution": [
                 {
-                    "title": "Analogue Search Results for pp'-DDD.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502619/Analogue%20Search%20Results%20for%20pp%27-DDD.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Analogue Search Results for pp'-DDD.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502619",
+            "keyword": [
+                "Read-across",
+                "quantitative risk assessment",
+                "toxicokinetics",
+                "in vitro high-throughput screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-05",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99612,48 +99606,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            ],
+            "rights": null,
+            "title": "Analogue search results for p,p'-DDD "
         },
         {
-            "title": "ToxCast bioactivity data for p,p'-DDD and analogues ",
-            "description": "Bioactivity data for p,p'-DDD and analogues from ToxCast assays conducted in liver cells were sourced from the EPA\u2019s CompTox Chemistry Dashboard. The links also provide access to the ToxCast assay information and annotation data user guide. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1502621",
-            "keyword": [
-                "Read-across",
-                "quantitative risk assessment",
-                "toxicokinetics",
-                "in vitro high-throughput screening"
-            ],
             "contactPoint": {
                 "fn": "Lucina Lizarraga",
                 "hasEmail": "mailto:lizarraga.lucina@epa.gov"
             },
+            "description": "Bioactivity data for p,p'-DDD and analogues from ToxCast assays conducted in liver cells were sourced from the EPA\u2019s CompTox Chemistry Dashboard. The links also provide access to the ToxCast assay information and annotation data user guide. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "distribution": [
                 {
-                    "title": "https://comptox.epa.gov/dashboard",
-                    "accessURL": "https://comptox.epa.gov/dashboard"
+                    "accessURL": "https://comptox.epa.gov/dashboard",
+                    "title": "https://comptox.epa.gov/dashboard"
                 },
                 {
-                    "title": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data",
-                    "accessURL": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data"
+                    "accessURL": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data",
+                    "title": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data"
                 },
                 {
-                    "title": "https://www.epa.gov/sites/production/files/2015-08/documents/toxcast_assay_annotation_data_users_guide_20141021.pdf",
-                    "accessURL": "https://www.epa.gov/sites/production/files/2015-08/documents/toxcast_assay_annotation_data_users_guide_20141021.pdf"
+                    "accessURL": "https://www.epa.gov/sites/production/files/2015-08/documents/toxcast_assay_annotation_data_users_guide_20141021.pdf",
+                    "title": "https://www.epa.gov/sites/production/files/2015-08/documents/toxcast_assay_annotation_data_users_guide_20141021.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502621",
+            "keyword": [
+                "Read-across",
+                "quantitative risk assessment",
+                "toxicokinetics",
+                "in vitro high-throughput screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-05",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99663,48 +99657,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            ],
+            "rights": null,
+            "title": "ToxCast bioactivity data for p,p'-DDD and analogues "
         },
         {
-            "title": "ToxCast bioactivity data and model predictions for the ER and AR pathways for p,p'-DDD and analogues ",
-            "description": "ToxCast bioactivity data and model predictions for the estrogen receptor (ER) and androgen receptor (AR) pathways were obtained from the inks provided. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1502622",
-            "keyword": [
-                "Read-across",
-                "quantitative risk assessment",
-                "toxicokinetics",
-                "in vitro high-throughput screening"
-            ],
             "contactPoint": {
                 "fn": "Lucina Lizarraga",
                 "hasEmail": "mailto:lizarraga.lucina@epa.gov"
             },
+            "description": "ToxCast bioactivity data and model predictions for the estrogen receptor (ER) and androgen receptor (AR) pathways were obtained from the inks provided. \n\nThis dataset is associated with the following publication:\nLizarraga, L., J. Dean, J. Kaiser, S. Wesselkamper, J. Lambert, and J. Zhao. A Case Study on the Application of An Expert-driven Read-Across Approach in Support of Quantitative Risk Assessment of p,p\u2019-Dichlorodiphenyldichloroethane.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 103: 301-313, (2019).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4635633/pdf/kfv168.pdf",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4635633/pdf/kfv168.pdf"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4635633/pdf/kfv168.pdf",
+                    "title": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4635633/pdf/kfv168.pdf"
                 },
                 {
-                    "title": "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0196963&type=printable",
-                    "accessURL": "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0196963&type=printable"
+                    "accessURL": "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0196963&type=printable",
+                    "title": "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0196963&type=printable"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5396026/pdf/tx6b00347.pdf",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5396026/pdf/tx6b00347.pdf"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5396026/pdf/tx6b00347.pdf",
+                    "title": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5396026/pdf/tx6b00347.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502622",
+            "keyword": [
+                "Read-across",
+                "quantitative risk assessment",
+                "toxicokinetics",
+                "in vitro high-throughput screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-05",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99714,138 +99708,138 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2019.02.010"
+            ],
+            "rights": null,
+            "title": "ToxCast bioactivity data and model predictions for the ER and AR pathways for p,p'-DDD and analogues "
         },
         {
-            "title": "Silica disrupts iron homeostasis in alveolar macrophages to impact a biological effect",
-            "description": "Cell investigation into mechanism of particle-related biological effect. \n\nThis dataset is associated with the following publication:\nGhio, A., J. Soukup, J. Stonehuerner , H. Tong, J. Richards, M. Gilmour, M. Madden, Z. Shen, and S.P. Kantrow. Quartz disrupts iron homeostasis in alveolar macrophages to impact a pro-inflammatory effect.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 32(9): 1737-1747, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503077",
-            "keyword": [
-                "particulate matter (PM)"
-            ],
             "contactPoint": {
                 "fn": "Andrew Ghio",
                 "hasEmail": "mailto:ghio.andy@epa.gov"
             },
+            "description": "Cell investigation into mechanism of particle-related biological effect. \n\nThis dataset is associated with the following publication:\nGhio, A., J. Soukup, J. Stonehuerner , H. Tong, J. Richards, M. Gilmour, M. Madden, Z. Shen, and S.P. Kantrow. Quartz disrupts iron homeostasis in alveolar macrophages to impact a pro-inflammatory effect.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 32(9): 1737-1747, (2019).",
             "distribution": [
                 {
-                    "title": "kantrow figure 1b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%201b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 1b.xlsx"
                 },
                 {
-                    "title": "kantrow figure 1d.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%201d.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 1d.xlsx"
                 },
                 {
-                    "title": "kantrow figure 1a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%201a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 1a.xlsx"
                 },
                 {
-                    "title": "kantrow figure 1e.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%201e.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 1e.xlsx"
                 },
                 {
-                    "title": "kantrow figure 2A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%202A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 2A.xlsx"
                 },
                 {
-                    "title": "kantrow figure 3a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%203a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 3a.xlsx"
                 },
                 {
-                    "title": "kantrow figure 3b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%203b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 3b.xlsx"
                 },
                 {
-                    "title": "kantrow figure 3c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%203c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 3c.xlsx"
                 },
                 {
-                    "title": "kantrow figure 3d.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%203d.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 3d.xlsx"
                 },
                 {
-                    "title": "kantrow figure 4a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%204a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 4a.xlsx"
                 },
                 {
-                    "title": "kantrow figure 4b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%204b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 4b.xlsx"
                 },
                 {
-                    "title": "kantrow figure 4c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%204c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 4c.xlsx"
                 },
                 {
-                    "title": "kantrow figure 4d.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%204d.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 4d.xlsx"
                 },
                 {
-                    "title": "kantrow figure 5a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%205a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 5a.xlsx"
                 },
                 {
-                    "title": "kantrow figure 5b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%205b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 5b.xlsx"
                 },
                 {
-                    "title": "kantrow figure 6a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%206a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 6a.xlsx"
                 },
                 {
-                    "title": "kantrow figure 6b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%206b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 6b.xlsx"
                 },
                 {
-                    "title": "kantrow figure 6c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%206c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 6c.xlsx"
                 },
                 {
-                    "title": "kantrow figure 7a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%207a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 7a.xlsx"
                 },
                 {
-                    "title": "kantrow figure 7b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%207b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 7b.xlsx"
                 },
                 {
-                    "title": "kantrow figure 7c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503077/kantrow%20figure%207c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "kantrow figure 7c.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503077",
+            "keyword": [
+                "particulate matter (PM)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-11-29",
-            "references": [
-                "https://doi.org/10.1021/acs.chemrestox.8b00301"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99855,19 +99849,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.chemrestox.8b00301"
+            ],
+            "rights": null,
+            "title": "Silica disrupts iron homeostasis in alveolar macrophages to impact a biological effect"
         },
         {
-            "title": "Commercial Waste National Totals by NAICS and US Satellite Tables for USEEIO",
-            "description": "Three tables are provided of US commercial waste generation by NAICS codes  for (1) Commercial non-hazardous waste (non-construction),\n(2) Commercial non-hazardous waste from construction, and\n(3) Commercial RCRA hazardous waste.\nThe unique waste types within these three tables are defined in referenced sources. \n\nThese national totals by NAICS are mapped to BEA (NAICS-based) detailed industries (388 total) from the BEA 2007 benchmark input-output tables. A crosswalk table is provided. \n\nThree satellite tables for the USEEIO model are provided using the mapped national waste totals and the industry gross output for the data year for that BEA industry after it has been adjusted to 2013 USD using the BEA industry-specific chain price index. See the associated manuscript for more details. The satellite table files are formatted for use in the USEEIO modeling framework (http://github.com/USEPA/useeio/) to incorporate into a USEEIO model. \n\nThis dataset is associated with the following publication:\nMeyer, D.E., M. Li, and W.W. Ingwersen. Analyzing economy-scale solid waste generation using the United States environmentally-extended input-output model.   Resources, Conservation and Recycling. Elsevier Science BV, Amsterdam,  NETHERLANDS, 157: 104795, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Wesley Ingwersen",
+                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
+            },
+            "description": "Three tables are provided of US commercial waste generation by NAICS codes  for (1) Commercial non-hazardous waste (non-construction),\n(2) Commercial non-hazardous waste from construction, and\n(3) Commercial RCRA hazardous waste.\nThe unique waste types within these three tables are defined in referenced sources. \n\nThese national totals by NAICS are mapped to BEA (NAICS-based) detailed industries (388 total) from the BEA 2007 benchmark input-output tables. A crosswalk table is provided. \n\nThree satellite tables for the USEEIO model are provided using the mapped national waste totals and the industry gross output for the data year for that BEA industry after it has been adjusted to 2013 USD using the BEA industry-specific chain price index. See the associated manuscript for more details. The satellite table files are formatted for use in the USEEIO modeling framework (http://github.com/USEPA/useeio/) to incorporate into a USEEIO model. \n\nThis dataset is associated with the following publication:\nMeyer, D.E., M. Li, and W.W. Ingwersen. Analyzing economy-scale solid waste generation using the United States environmentally-extended input-output model.   Resources, Conservation and Recycling. Elsevier Science BV, Amsterdam,  NETHERLANDS, 157: 104795, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503688/Commercial%20Waste%20National%20Totals%20by%20NAICS%20and%20US%20Satellite%20Tables%20for%20USEEIO.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Commercial Waste National Totals by NAICS and US Satellite Tables for USEEIO.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503688",
             "keyword": [
@@ -99878,20 +99882,10 @@
                 "sustainability",
                 "input-output data"
             ],
-            "contactPoint": {
-                "fn": "Wesley Ingwersen",
-                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Commercial Waste National Totals by NAICS and US Satellite Tables for USEEIO.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503688/Commercial%20Waste%20National%20Totals%20by%20NAICS%20and%20US%20Satellite%20Tables%20for%20USEEIO.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-25",
-            "references": [
-                "https://doi.org/10.1016/j.resconrec.2020.104795"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99901,63 +99895,63 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.resconrec.2020.104795"
+            ],
+            "rights": null,
+            "title": "Commercial Waste National Totals by NAICS and US Satellite Tables for USEEIO"
         },
         {
-            "title": "Ambient Particulate Matter and Acrolein Co-Exposure Increases Myocardial Dyssynchrony in Mice via TRPA1",
-            "description": "We have examined the potential for interactive cardiovascular effects of repeated, intermittent co-exposure to concentrated ambient particulate matter (CAPs) and acrolein, and the potential role of transient receptor potential cation channel A1 (TRPA1), which we previously linked to air pollution-induced cardiac arrhythmogenesis. Chemical and source characteristics of collected particles was evaluated, as well as wind and weather patterns during exposure. Female B6129 mice and Trpa1-/- mice (n=6) were exposed to filtered air (FA), CAPs (46 \u00b5g/m3 of PM2.5 approximately 160 nm diameter), Acrolein (0.42 ppm) or CAPs+Acrolein for 3hrs/day, 2days/week, for 4 weeks. Cardiac strain data, heart function and dimensions, and transmitral blood flow were investigated with echocardiography (40 MHz) before exposures, 1 day after the first exposure, and 1 day after the final exposure. Several other biological endpoints were evaluated but the key findings from ultrasound echocardiography assessments were: elapsed time between peak strain in adjacent wall segments (i.e. myocardial strain delay), a measure of myocardial dyssynchrony, increased by ~5-fold in B6129 mice after the final exposure to CAPs+Acrolein when compared to strain delay in B6129 mice exposed to FA, CAPs, or Acrolein alone, and when compared to strain delay in Trpa1-/- mice exposed to CAPs+Acrolein. There were no changes after the first exposure in any group. \n\nThis dataset is associated with the following publication:\nThompson, L., L. Walsh, B. Martin, J. Mcgee, C. Wood, K. Kovalcik, P. Pancras, N. Coates, A. Ledbetter, D. Davies, W. Cascio, M. Higuchi, M. Hazari, and A. Farraj. Ambient Particulate Matter and Acrolein Co-Exposure Increases Myocardial Dyssynchrony in Mice: Evidence for TRPA1 Involvement.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  167(2): 559-572, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1411215",
-            "keyword": [
-                "Ambient air quality",
-                "air pollution exposure",
-                "Fine Particulate Matter",
-                "acrolein",
-                "multiple pollutants",
-                "co-exposure",
-                "heart function",
-                "echocardiography",
-                "TRPA1",
-                "myocardial synchrony",
-                "myocardial dyssynchrony"
-            ],
             "contactPoint": {
                 "fn": "Leslie Thompson",
                 "hasEmail": "mailto:thompson.leslie@epa.gov"
             },
+            "description": "We have examined the potential for interactive cardiovascular effects of repeated, intermittent co-exposure to concentrated ambient particulate matter (CAPs) and acrolein, and the potential role of transient receptor potential cation channel A1 (TRPA1), which we previously linked to air pollution-induced cardiac arrhythmogenesis. Chemical and source characteristics of collected particles was evaluated, as well as wind and weather patterns during exposure. Female B6129 mice and Trpa1-/- mice (n=6) were exposed to filtered air (FA), CAPs (46 \u00b5g/m3 of PM2.5 approximately 160 nm diameter), Acrolein (0.42 ppm) or CAPs+Acrolein for 3hrs/day, 2days/week, for 4 weeks. Cardiac strain data, heart function and dimensions, and transmitral blood flow were investigated with echocardiography (40 MHz) before exposures, 1 day after the first exposure, and 1 day after the final exposure. Several other biological endpoints were evaluated but the key findings from ultrasound echocardiography assessments were: elapsed time between peak strain in adjacent wall segments (i.e. myocardial strain delay), a measure of myocardial dyssynchrony, increased by ~5-fold in B6129 mice after the final exposure to CAPs+Acrolein when compared to strain delay in B6129 mice exposed to FA, CAPs, or Acrolein alone, and when compared to strain delay in Trpa1-/- mice exposed to CAPs+Acrolein. There were no changes after the first exposure in any group. \n\nThis dataset is associated with the following publication:\nThompson, L., L. Walsh, B. Martin, J. Mcgee, C. Wood, K. Kovalcik, P. Pancras, N. Coates, A. Ledbetter, D. Davies, W. Cascio, M. Higuchi, M. Hazari, and A. Farraj. Ambient Particulate Matter and Acrolein Co-Exposure Increases Myocardial Dyssynchrony in Mice: Evidence for TRPA1 Involvement.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  167(2): 559-572, (2019).",
             "distribution": [
                 {
-                    "title": "CAPs Acrolein Source Apportionment.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411215/CAPs%20Acrolein%20Source%20Apportionment.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CAPs Acrolein Source Apportionment.xlsx"
                 },
                 {
-                    "title": "CAPs Acrolein Elemental Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411215/CAPs%20Acrolein%20Elemental%20Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CAPs Acrolein Elemental Analysis.xlsx"
                 },
                 {
-                    "title": "CAPs Acrolein Chamber and Weather Values.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411215/CAPs%20Acrolein%20Chamber%20and%20Weather%20Values.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CAPs Acrolein Chamber and Weather Values.xlsx"
                 },
                 {
-                    "title": "CAPs Acrolein Biological Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411215/CAPs%20Acrolein%20Biological%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CAPs Acrolein Biological Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1411215",
+            "keyword": [
+                "Ambient air quality",
+                "air pollution exposure",
+                "Fine Particulate Matter",
+                "acrolein",
+                "multiple pollutants",
+                "co-exposure",
+                "heart function",
+                "echocardiography",
+                "TRPA1",
+                "myocardial synchrony",
+                "myocardial dyssynchrony"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-11",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfy262"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -99967,19 +99961,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfy262"
+            ],
+            "rights": null,
+            "title": "Ambient Particulate Matter and Acrolein Co-Exposure Increases Myocardial Dyssynchrony in Mice via TRPA1"
         },
         {
-            "title": "Time series analysis of wintertime O3 and NOx formation",
-            "description": "Concentrations of 11 species are reported from continuous measurements taken during a wintertime field study in Utah. Time series data for measured species generally displayed strong diurnal patterns. Six species show a diurnal pattern of daytime maximums (NO, NOy, O3, H2O2, CH2O2, and Cl2), while five species show a diurnal pattern of night time maximums (NO2, HONO, ClNO2, HNO3, and N2O5). Vector autoregression analyses were completed to better understand important species influencing the formation of O3 and NOx. For the species studied, r2 values of predicted versus measured concentrations ranged from 0.82\u20130.99. Fitting parameters for the autoregressive matrix, Pi, indicated the importance of species precursors. In addition, values of fitting parameters for Pi were relatively insensitive to data size, with variations generally <10%. Variable causation was quantified using the Granger causation method. Assuming O3 and NOx behave as chemical products, reactants (in order of importance) are as follows: H2O2, N2O5, HONO, and ClNO2. \n\nThis dataset is associated with the following publication:\nOlson, D., T. Riedel, R. Long, J. Offenberg, M. Lewandowski, and T. Kleindienst. Time series analysis of wintertime O3 and NOx formation using vector autoregressions.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 218: 116988, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Michael Lewandowski",
+                "hasEmail": "mailto:lewandowski.michael@epa.gov"
+            },
+            "description": "Concentrations of 11 species are reported from continuous measurements taken during a wintertime field study in Utah. Time series data for measured species generally displayed strong diurnal patterns. Six species show a diurnal pattern of daytime maximums (NO, NOy, O3, H2O2, CH2O2, and Cl2), while five species show a diurnal pattern of night time maximums (NO2, HONO, ClNO2, HNO3, and N2O5). Vector autoregression analyses were completed to better understand important species influencing the formation of O3 and NOx. For the species studied, r2 values of predicted versus measured concentrations ranged from 0.82\u20130.99. Fitting parameters for the autoregressive matrix, Pi, indicated the importance of species precursors. In addition, values of fitting parameters for Pi were relatively insensitive to data size, with variations generally <10%. Variable causation was quantified using the Granger causation method. Assuming O3 and NOx behave as chemical products, reactants (in order of importance) are as follows: H2O2, N2O5, HONO, and ClNO2. \n\nThis dataset is associated with the following publication:\nOlson, D., T. Riedel, R. Long, J. Offenberg, M. Lewandowski, and T. Kleindienst. Time series analysis of wintertime O3 and NOx formation using vector autoregressions.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 218: 116988, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503977/Olson%20Utah%20Time%20Series%20Fig%201-5.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Olson Utah Time Series Fig 1-5.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503977",
             "keyword": [
@@ -99991,20 +99995,10 @@
                 "air toxics",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Michael Lewandowski",
-                "hasEmail": "mailto:lewandowski.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Olson Utah Time Series Fig 1-5.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503977/Olson%20Utah%20Time%20Series%20Fig%201-5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-22",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2019.116988"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100014,45 +100008,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2019.116988"
+            ],
+            "rights": null,
+            "title": "Time series analysis of wintertime O3 and NOx formation"
         },
         {
-            "title": "TracMyAir data",
-            "description": "This dataset consists of input and output data for sensitivity analysis of the model. \n\nThis dataset is associated with the following publication:\nBreen, M., C. Seppanen, V. Isakov, S. Arunachalam, M. Breen, J. Samet, and H. Tong. Development of TracMyAir Smartphone Application for Modeling Exposures to Ambient PM2.5 and Ozone.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 16(18): 3468, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504092",
-            "keyword": [
-                "human exposure modeling",
-                "fine particulate matter (PM2.5)",
-                "Ozone"
-            ],
             "contactPoint": {
                 "fn": "Michael Breen",
                 "hasEmail": "mailto:breen.michael@epa.gov"
             },
+            "description": "This dataset consists of input and output data for sensitivity analysis of the model. \n\nThis dataset is associated with the following publication:\nBreen, M., C. Seppanen, V. Isakov, S. Arunachalam, M. Breen, J. Samet, and H. Tong. Development of TracMyAir Smartphone Application for Modeling Exposures to Ambient PM2.5 and Ozone.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 16(18): 3468, (2019).",
             "distribution": [
                 {
-                    "title": "tracmyair_input_data.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504092/tracmyair_input_data.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "tracmyair_input_data.docx"
                 },
                 {
-                    "title": "tracmyair_output_data.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504092/tracmyair_output_data.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "tracmyair_output_data.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504092",
+            "keyword": [
+                "human exposure modeling",
+                "fine particulate matter (PM2.5)",
+                "Ozone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-01",
-            "references": [
-                "https://doi.org/10.3390/ijerph16183468"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100062,40 +100056,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ijerph16183468"
+            ],
+            "rights": null,
+            "title": "TracMyAir data"
         },
         {
-            "title": "Fetal and Postnatal Cortical Thyroid Hormone Levels and Bioindicators",
-            "description": "thyroid hormones in serum and in brain were measured in fetal and neonatal rat cortex after graded levels of a thyroid hormone synthesis inhibitor were administered to pregnant rat dams. A number of gene targets were assessed to look for measures of thyroid hormone action in these same tissues. \n\nThis dataset is associated with the following publication:\nOShaughnessy, K., C. Wood, R. Ford, P. Kosian, M. Hotchkiss, S. Degitz, and M. Gilbert. Thyroid hormone disruption in the fetal and neonatal rat: Predictive hormone measures and bioindicators of hormone action in the developing cortex- ToxSci.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,   163-179, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1420050",
-            "keyword": [
-                "thyroid",
-                "brain developoment",
-                "molecular markers"
-            ],
             "contactPoint": {
                 "fn": "Mary Gilbert",
                 "hasEmail": "mailto:gilbert.mary@epa.gov"
             },
+            "description": "thyroid hormones in serum and in brain were measured in fetal and neonatal rat cortex after graded levels of a thyroid hormone synthesis inhibitor were administered to pregnant rat dams. A number of gene targets were assessed to look for measures of thyroid hormone action in these same tissues. \n\nThis dataset is associated with the following publication:\nOShaughnessy, K., C. Wood, R. Ford, P. Kosian, M. Hotchkiss, S. Degitz, and M. Gilbert. Thyroid hormone disruption in the fetal and neonatal rat: Predictive hormone measures and bioindicators of hormone action in the developing cortex- ToxSci.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,   163-179, (2018).",
             "distribution": [
                 {
-                    "title": "OShaughnessyetalScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1420050/OShaughnessyetalScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OShaughnessyetalScienceHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1420050",
+            "keyword": [
+                "thyroid",
+                "brain developoment",
+                "molecular markers"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-09",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfy190"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100105,45 +100099,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfy190"
+            ],
+            "rights": null,
+            "title": "Fetal and Postnatal Cortical Thyroid Hormone Levels and Bioindicators"
         },
         {
-            "title": "Reconnaissance of Mixed Organic and Inorganic Chemicals in Private and Public Supply Tapwaters at Selected Residential and Workplace Sites in the United States",
-            "description": "In vitro bioactivity concentrations and chemical concentrations of estrogens, androgens, and glucocorticoids from a pilot study of US tapwaters. In vitro bioassays include T47D-Kbluc, MDA-kb2, and a CV-1 cell line transduced with human glucocorticoid receptor. \n\nThis dataset is associated with the following publication:\nBradley, P., D. Kolpin, K. Romanok, K. Smalling, M. Focaszio, J. Brown, M. Cardon, K. Carpenter, S. Corsi, L. DeCicco, J. Dietze, N. Evans, E. Furlong, C. Givens, J. Gray, D. Griffin, C. Higgins, M. Hladik, L. Iwanowicz, C. Journey, K. Kuivila, J. Masoner, C. McDonough, M. Meyer, J. Orlando, M. Strynar, C. Weis, and V. Wilson. Reconnaissance of Mixed Organic and Inorganic Chemicals in Private and Public Supply Tapwaters at Selected Residential and Workplace Sites in the United States.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA,  13972-13985, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503956",
-            "keyword": [
-                "tapwater",
-                "bioassay",
-                "contaminant mixtures",
-                "point of use drinking water"
-            ],
             "contactPoint": {
                 "fn": "Vickie Wilson",
                 "hasEmail": "mailto:wilson.vickie@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1503956/documents/Dataset%20Dictionary%20for%20ScID%20A-hqcg%20Bradley%20etal%20.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "In vitro bioactivity concentrations and chemical concentrations of estrogens, androgens, and glucocorticoids from a pilot study of US tapwaters. In vitro bioassays include T47D-Kbluc, MDA-kb2, and a CV-1 cell line transduced with human glucocorticoid receptor. \n\nThis dataset is associated with the following publication:\nBradley, P., D. Kolpin, K. Romanok, K. Smalling, M. Focaszio, J. Brown, M. Cardon, K. Carpenter, S. Corsi, L. DeCicco, J. Dietze, N. Evans, E. Furlong, C. Givens, J. Gray, D. Griffin, C. Higgins, M. Hladik, L. Iwanowicz, C. Journey, K. Kuivila, J. Masoner, C. McDonough, M. Meyer, J. Orlando, M. Strynar, C. Weis, and V. Wilson. Reconnaissance of Mixed Organic and Inorganic Chemicals in Private and Public Supply Tapwaters at Selected Residential and Workplace Sites in the United States.   Environmental Science & Technology Letters. American Chemical Society, Washington, DC, USA,  13972-13985, (2018).",
             "distribution": [
                 {
-                    "title": "Data link - Tap water pilot.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503956/Data%20link%20-%20Tap%20water%20pilot.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data link - Tap water pilot.docx"
                 },
                 {
-                    "title": "https://doi.org/10.5066/F7959GVJ",
-                    "accessURL": "https://doi.org/10.5066/F7959GVJ"
+                    "accessURL": "https://doi.org/10.5066/F7959GVJ",
+                    "title": "https://doi.org/10.5066/F7959GVJ"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503956",
+            "keyword": [
+                "tapwater",
+                "bioassay",
+                "contaminant mixtures",
+                "point of use drinking water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-18",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b04622"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100154,62 +100150,62 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1503956/documents/Dataset%20Dictionary%20for%20ScID%20A-hqcg%20Bradley%20etal%20.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b04622"
+            ],
+            "rights": null,
+            "title": "Reconnaissance of Mixed Organic and Inorganic Chemicals in Private and Public Supply Tapwaters at Selected Residential and Workplace Sites in the United States"
         },
         {
-            "title": "AWG and Bottled Water source data and results files",
-            "description": "Dataset of different AWG units and bottled water units for different scales were provided.  The LCA results of the different systems were provided as well. \n\nThis dataset is associated with the following publication:\nAbsar, M., S. Cashman, X. Ma, J. Garland, and M. Jahne. Life Cycle and Cost Assessments of Atmospheric Water Generation Technologies and Alternative Potable Water Emergency Response Options. U.S. Environmental Protection Agency, Washington, DC, USA.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503094",
-            "keyword": [
-                "Atmopheric Water Generation",
-                "Alternative potable water source",
-                "bottled water",
-                "Life cycle assessment (LCA)",
-                "Life Cycle Cost"
-            ],
             "contactPoint": {
                 "fn": "Xin Ma",
                 "hasEmail": "mailto:ma.cissy@epa.gov"
             },
+            "description": "Dataset of different AWG units and bottled water units for different scales were provided.  The LCA results of the different systems were provided as well. \n\nThis dataset is associated with the following publication:\nAbsar, M., S. Cashman, X. Ma, J. Garland, and M. Jahne. Life Cycle and Cost Assessments of Atmospheric Water Generation Technologies and Alternative Potable Water Emergency Response Options. U.S. Environmental Protection Agency, Washington, DC, USA.",
             "distribution": [
                 {
-                    "title": "AppendixA-AWG_BottledWaterDatav4_12.19.18.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503094/AppendixA-AWG_BottledWaterDatav4_12.19.18.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AppendixA-AWG_BottledWaterDatav4_12.19.18.xlsx"
                 },
                 {
-                    "title": "AppendixB-Results_Template_AWGBottledWaterv4_12.19.18.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503094/AppendixB-Results_Template_AWGBottledWaterv4_12.19.18.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AppendixB-Results_Template_AWGBottledWaterv4_12.19.18.xlsx"
                 },
                 {
-                    "title": "AWG_LCA_Report_Final_1.29.19.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503094/AWG_LCA_Report_Final_1.29.19.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "AWG_LCA_Report_Final_1.29.19.docx"
                 },
                 {
-                    "title": "AWG_LCA_Report_Final_1.29.19.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503094/AWG_LCA_Report_Final_1.29.19.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "AWG_LCA_Report_Final_1.29.19.pdf"
                 },
                 {
-                    "title": "Consolidated Comments & Response_3.12.19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503094/Consolidated%20Comments%20%26%20Response_3.12.19.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Consolidated Comments & Response_3.12.19.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503094",
+            "keyword": [
+                "Atmopheric Water Generation",
+                "Alternative potable water source",
+                "bottled water",
+                "Life cycle assessment (LCA)",
+                "Life Cycle Cost"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-01-29",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -100218,38 +100214,36 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "AWG and Bottled Water source data and results files"
         },
         {
-            "title": "Pollen and honeybee neonicotinoid exposure data and analyses",
-            "description": "Data on the presence of corn seed treatment insecticides in bee-collected pollen and increased honey bee mortality associated with corn planting, persistence of the insecticides inside honey bee colonies, and long-term growth of these colonies in central Ohio. We also constructed spatial models, based on empirical data of honey bee foraging and dispersion patterns of planter dust, and landscape compositions, to simulate hypothesized exposure routes via contamination of foraging resources and aerial exposure resulting from flight through localized dust plumes from planters and diffuse dust in the landscape over all resulting from widespread planting activity. Insecticide concentrations under different hypothesized exposure routes were then compared with the observed levels of contamination to evaluate these hypotheses. \n\nThis dataset is associated with the following publication:\nKuan, C., G. DeGrandi-Hoffman, R. Curry, K. Garber, A. Kanarek, M. Snyder, K. Wolfe, and T. Purucker. Sensitivity analyses for simulating pesticide impacts on honey bee colonies.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 376: 15-27, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1500923",
-            "keyword": [
-                "neonicotinoids",
-                "honeybees"
-            ],
             "contactPoint": {
                 "fn": "Steven Purucker",
                 "hasEmail": "mailto:purucker.tom@epa.gov"
             },
+            "description": "Data on the presence of corn seed treatment insecticides in bee-collected pollen and increased honey bee mortality associated with corn planting, persistence of the insecticides inside honey bee colonies, and long-term growth of these colonies in central Ohio. We also constructed spatial models, based on empirical data of honey bee foraging and dispersion patterns of planter dust, and landscape compositions, to simulate hypothesized exposure routes via contamination of foraging resources and aerial exposure resulting from flight through localized dust plumes from planters and diffuse dust in the landscape over all resulting from widespread planting activity. Insecticide concentrations under different hypothesized exposure routes were then compared with the observed levels of contamination to evaluate these hypotheses. \n\nThis dataset is associated with the following publication:\nKuan, C., G. DeGrandi-Hoffman, R. Curry, K. Garber, A. Kanarek, M. Snyder, K. Wolfe, and T. Purucker. Sensitivity analyses for simulating pesticide impacts on honey bee colonies.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 376: 15-27, (2018).",
             "distribution": [
                 {
-                    "title": "https://github.com/puruckertom/rare_pollen/",
-                    "accessURL": "https://github.com/puruckertom/rare_pollen/"
+                    "accessURL": "https://github.com/puruckertom/rare_pollen/",
+                    "title": "https://github.com/puruckertom/rare_pollen/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500923",
+            "keyword": [
+                "neonicotinoids",
+                "honeybees"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-04",
-            "references": [
-                "https://doi.org/10.1016/j.ecolmodel.2018.02.010"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100259,70 +100253,70 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolmodel.2018.02.010"
+            ],
+            "rights": null,
+            "title": "Pollen and honeybee neonicotinoid exposure data and analyses"
         },
         {
-            "title": "X-Ray diffraction of titanium dioxide nanoparticles and their inhibition of marine diatom growth",
-            "description": "The XRD text files show counts per second of X-ray diffraction as a function of diffraction angle for six nanomaterials: industrial TiO2, toothpaste TiO2, sunscreen TiO2 and these materials after algae toxicity test. Figure 1 in TiO2 paper shows the raw data for the inhibition (%) as a function of time (h) for the nanomaterials at 5 mg/L concentration. \n\nThis dataset is associated with the following publication:\nGalletti, A., S. Seo, S.H. Joo, C. Su, and P. Blackwelder. Effects of titanium dioxide nanoparticles derived from consumer products on the marine diatom Thalassiosira pseudonana.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 23: 21113-21122, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503202",
-            "keyword": [
-                "Nanoproducts . Commercial TiO2",
-                "Marine",
-                "environments . Toxicity . Exposure . Algae"
-            ],
             "contactPoint": {
                 "fn": "Chunming Su",
                 "hasEmail": "mailto:su.chunming@epa.gov"
             },
+            "description": "The XRD text files show counts per second of X-ray diffraction as a function of diffraction angle for six nanomaterials: industrial TiO2, toothpaste TiO2, sunscreen TiO2 and these materials after algae toxicity test. Figure 1 in TiO2 paper shows the raw data for the inhibition (%) as a function of time (h) for the nanomaterials at 5 mg/L concentration. \n\nThis dataset is associated with the following publication:\nGalletti, A., S. Seo, S.H. Joo, C. Su, and P. Blackwelder. Effects of titanium dioxide nanoparticles derived from consumer products on the marine diatom Thalassiosira pseudonana.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 23: 21113-21122, (2016).",
             "distribution": [
                 {
-                    "title": "Fig.1 in TiO2 paper.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503202/Fig.1%20in%20TiO2%20paper.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig.1 in TiO2 paper.xlsx"
                 },
                 {
-                    "title": "SunscreenTiO2.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503202/SunscreenTiO2.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "SunscreenTiO2.txt"
                 },
                 {
-                    "title": "IndustrialTiO2.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503202/IndustrialTiO2.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IndustrialTiO2.txt"
                 },
                 {
-                    "title": "ToothpasteTiO2.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503202/ToothpasteTiO2.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "ToothpasteTiO2.txt"
                 },
                 {
-                    "title": "ToxtestindustrialTiO2.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503202/ToxtestindustrialTiO2.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "ToxtestindustrialTiO2.txt"
                 },
                 {
-                    "title": "ToxtestsunscreenTiO2.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503202/ToxtestsunscreenTiO2.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "ToxtestsunscreenTiO2.txt"
                 },
                 {
-                    "title": "ToxtesttoothpasteTiO2.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503202/ToxtesttoothpasteTiO2.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "ToxtesttoothpasteTiO2.txt"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503202",
+            "keyword": [
+                "Nanoproducts . Commercial TiO2",
+                "Marine",
+                "environments . Toxicity . Exposure . Algae"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-11-27",
-            "references": [
-                "https://doi.org/10.1007/s11356-016-7556-6"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100332,61 +100326,61 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11356-016-7556-6"
+            ],
+            "rights": null,
+            "title": "X-Ray diffraction of titanium dioxide nanoparticles and their inhibition of marine diatom growth"
         },
         {
-            "title": "Growth inhibition of algae and X-ray diffractions of ZnO ",
-            "description": "The XRD text files show counts per second of X-ray diffraction as a function of diffraction angle for four nanomaterials: industrial ZnO, sunscreen ZnO, industrial ZnO after algae toxicity test, sunscreen ZnO after algae toxicity test. Figure 2 in ZnO paper shows the raw data for the inhibition (%) as a function of time (h) for the nanomaterials at 10 mg/L and 50 mg/L concentrations. \n\nThis dataset is associated with the following publication:\nSpisni, E., S. Seo, S.H. Joo, and C. Su. Release and toxicity comparison between industrial- and sunscreen-derived nano-ZnO particles.   International Journal of Environmental Science and Technology. Springer, Heidelburg,  GERMANY, 13: 2485-2494, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503200",
-            "keyword": [
-                "Thalassiosira pseudonana",
-                "Aggregation",
-                "Commercial ZnO",
-                "ecotoxicity"
-            ],
             "contactPoint": {
                 "fn": "Chunming Su",
                 "hasEmail": "mailto:su.chunming@epa.gov"
             },
+            "description": "The XRD text files show counts per second of X-ray diffraction as a function of diffraction angle for four nanomaterials: industrial ZnO, sunscreen ZnO, industrial ZnO after algae toxicity test, sunscreen ZnO after algae toxicity test. Figure 2 in ZnO paper shows the raw data for the inhibition (%) as a function of time (h) for the nanomaterials at 10 mg/L and 50 mg/L concentrations. \n\nThis dataset is associated with the following publication:\nSpisni, E., S. Seo, S.H. Joo, and C. Su. Release and toxicity comparison between industrial- and sunscreen-derived nano-ZnO particles.   International Journal of Environmental Science and Technology. Springer, Heidelburg,  GERMANY, 13: 2485-2494, (2016).",
             "distribution": [
                 {
-                    "title": "Fig. 2 in ZnO paper.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503200/Fig.%202%20in%20ZnO%20paper.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig. 2 in ZnO paper.xlsx"
                 },
                 {
-                    "title": "IndustrialZnO.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503200/IndustrialZnO.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IndustrialZnO.txt"
                 },
                 {
-                    "title": "SunscreenZnO.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503200/SunscreenZnO.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "SunscreenZnO.txt"
                 },
                 {
-                    "title": "ToxtestindustrialZnO.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503200/ToxtestindustrialZnO.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "ToxtestindustrialZnO.txt"
                 },
                 {
-                    "title": "ToxtestsunscreenZnO.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503200/ToxtestsunscreenZnO.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "ToxtestsunscreenZnO.txt"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503200",
+            "keyword": [
+                "Thalassiosira pseudonana",
+                "Aggregation",
+                "Commercial ZnO",
+                "ecotoxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-11-27",
-            "references": [
-                "https://doi.org/10.1007/s13762-016-1077-1"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100396,48 +100390,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s13762-016-1077-1"
+            ],
+            "rights": null,
+            "title": "Growth inhibition of algae and X-ray diffractions of ZnO "
         },
         {
-            "title": "PROPS model output for individual species",
-            "description": "There are two datasets. First, a dataset for the PROPS models (i.e. \u201cUS-PROPS_v2_models_May30_2019.xlsx,\u201d which describe the parameters for the PROPS models for the 1503 species that were included in the study. Metadata for this data is provided in the excel spreadsheet. Second, is a spreadsheet of the \u201ccritical load functions\u201d (CLF) that are derived from the PROPS models (i.e. \u201cPROPS-CLF_results_May30_2019.xlsx\u201d). Metadata for this dataset are also provided in the spreadhseet. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504252",
-            "keyword": [
-                "nitrogen deposition",
-                "sulfur deposition",
-                "biodiversity",
-                "native plants",
-                "critical loads",
-                "NAAQS",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Christopher Clark",
                 "hasEmail": "mailto:clark.christopher@epa.gov"
             },
+            "description": "There are two datasets. First, a dataset for the PROPS models (i.e. \u201cUS-PROPS_v2_models_May30_2019.xlsx,\u201d which describe the parameters for the PROPS models for the 1503 species that were included in the study. Metadata for this data is provided in the excel spreadsheet. Second, is a spreadsheet of the \u201ccritical load functions\u201d (CLF) that are derived from the PROPS models (i.e. \u201cPROPS-CLF_results_May30_2019.xlsx\u201d). Metadata for this dataset are also provided in the spreadhseet. ",
             "distribution": [
                 {
-                    "title": "US-PROPS_v2_models_May30_2019.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504252/US-PROPS_v2_models_May30_2019.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "US-PROPS_v2_models_May30_2019.xlsx"
                 },
                 {
-                    "title": "PROPS-CLF_results_May30_2019.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504252/PROPS-CLF_results_May30_2019.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PROPS-CLF_results_May30_2019.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504252",
+            "keyword": [
+                "nitrogen deposition",
+                "sulfur deposition",
+                "biodiversity",
+                "native plants",
+                "critical loads",
+                "NAAQS",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-29",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -100446,51 +100442,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "PROPS model output for individual species"
         },
         {
-            "title": "Data for Fluctuating Emissions and Availability of Health Reference Values: Implications for Estimating Acute Exposure and Health Risk (Manuscript)",
-            "description": "This the raw data that the manuscript: Fluctuating Emissions and Availability of Health Reference Values: Implications for Estimating Acute Exposure and Health Risk is based on. \n\nThis dataset is associated with the following publication:\nStewart, M., J. Hirtz, G. Woodall, C. Weitekamp, and K. Spence. A Comparison of Hourly with Annual Air Pollutant Emissions: Implications for Estimating Acute Exposure and Public Health Risk.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 69(7): 848-856, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1500906",
-            "keyword": [
-                "emissions",
-                "Risk Assessment",
-                "air toxics"
-            ],
             "contactPoint": {
                 "fn": "Michael Stewart",
                 "hasEmail": "mailto:stewart.michael@epa.gov"
             },
+            "description": "This the raw data that the manuscript: Fluctuating Emissions and Availability of Health Reference Values: Implications for Estimating Acute Exposure and Health Risk is based on. \n\nThis dataset is associated with the following publication:\nStewart, M., J. Hirtz, G. Woodall, C. Weitekamp, and K. Spence. A Comparison of Hourly with Annual Air Pollutant Emissions: Implications for Estimating Acute Exposure and Public Health Risk.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 69(7): 848-856, (2019).",
             "distribution": [
                 {
-                    "title": "https://www.regulations.gov/document?D=EPA-HQ-OAR-2012-0640-0089",
-                    "accessURL": "https://www.regulations.gov/document?D=EPA-HQ-OAR-2012-0640-0089"
+                    "accessURL": "https://www.regulations.gov/document?D=EPA-HQ-OAR-2012-0640-0089",
+                    "title": "https://www.regulations.gov/document?D=EPA-HQ-OAR-2012-0640-0089"
                 },
                 {
-                    "title": "https://www.epa.gov/airmarkets/clean-air-markets-data-resources",
-                    "accessURL": "https://www.epa.gov/airmarkets/clean-air-markets-data-resources"
+                    "accessURL": "https://www.epa.gov/airmarkets/clean-air-markets-data-resources",
+                    "title": "https://www.epa.gov/airmarkets/clean-air-markets-data-resources"
                 },
                 {
-                    "title": "https://www.epa.gov/air-emissions-inventories/2011-national-emissions-inventory-nei-data",
-                    "accessURL": "https://www.epa.gov/air-emissions-inventories/2011-national-emissions-inventory-nei-data"
+                    "accessURL": "https://www.epa.gov/air-emissions-inventories/2011-national-emissions-inventory-nei-data",
+                    "title": "https://www.epa.gov/air-emissions-inventories/2011-national-emissions-inventory-nei-data"
                 },
                 {
-                    "title": "https://www.epa.gov/fera/dose-response-assessment-assessing-health-risks-associated-exposure-hazardous-air-pollutants",
-                    "accessURL": "https://www.epa.gov/fera/dose-response-assessment-assessing-health-risks-associated-exposure-hazardous-air-pollutants"
+                    "accessURL": "https://www.epa.gov/fera/dose-response-assessment-assessing-health-risks-associated-exposure-hazardous-air-pollutants",
+                    "title": "https://www.epa.gov/fera/dose-response-assessment-assessing-health-risks-associated-exposure-hazardous-air-pollutants"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500906",
+            "keyword": [
+                "emissions",
+                "Risk Assessment",
+                "air toxics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": [
-                "https://doi.org/10.1080/10962247.2019.1593261"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100500,53 +100494,55 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10962247.2019.1593261"
+            ],
+            "rights": null,
+            "title": "Data for Fluctuating Emissions and Availability of Health Reference Values: Implications for Estimating Acute Exposure and Health Risk (Manuscript)"
         },
         {
-            "title": "References - 508 compliant",
-            "description": "Three files are available. The first contains a listing of references evaluated in this review article. The second and third contain data extracted from each of those references. Those data files contain details about error type, pollutant, bias, and coverage probability. \n\nThis dataset is associated with the following publication:\nRichmond-Bryant, J., and T. Long. Influence of Exposure Errors on Results from Epidemiologic Studies of Different Designs.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK,  1-10, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1500936",
-            "keyword": [
-                "exposure measurement error",
-                "particulate matter",
-                "nitrogen dioxide",
-                "sulfur dioxide",
-                "air pollution",
-                "epidemiology"
-            ],
             "contactPoint": {
                 "fn": "Jennifer Richmond-Bryant",
                 "hasEmail": "mailto:richmond-bryant.jennifer@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500936/documents/Data_Dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Three files are available. The first contains a listing of references evaluated in this review article. The second and third contain data extracted from each of those references. Those data files contain details about error type, pollutant, bias, and coverage probability. \n\nThis dataset is associated with the following publication:\nRichmond-Bryant, J., and T. Long. Influence of Exposure Errors on Results from Epidemiologic Studies of Different Designs.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK,  1-10, (2019).",
             "distribution": [
                 {
-                    "title": "bias_data_for_hclust_LT_avg_04232018_508.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500936/bias_data_for_hclust_LT_avg_04232018_508.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "bias_data_for_hclust_LT_avg_04232018_508.xlsx"
                 },
                 {
-                    "title": "bias_data_for_hclust_time-series_11052017_508.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500936/bias_data_for_hclust_time-series_11052017_508.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "bias_data_for_hclust_time-series_11052017_508.xlsx"
                 },
                 {
-                    "title": "implications_for_epi_508.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500936/implications_for_epi_508.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "implications_for_epi_508.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500936",
+            "keyword": [
+                "exposure measurement error",
+                "particulate matter",
+                "nitrogen dioxide",
+                "sulfur dioxide",
+                "air pollution",
+                "epidemiology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-11",
-            "references": [
-                "https://doi.org/10.1038/s41370-019-0164-z"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100557,21 +100553,23 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500936/documents/Data_Dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1038/s41370-019-0164-z"
+            ],
+            "rights": null,
+            "title": "References - 508 compliant"
         },
         {
-            "title": "Boreal bird body mass dataset (Holling 1992)",
-            "description": "The dataset provided by Holling(1922) includes species and body masses of boreal forest birds.  It is a commonly used dataset for discontinuity analysis. This dataset is not publicly accessible because: It is secondary data accessible online. It can be accessed through the following means: All data used are freely available and located in the appendix of Holling (1992):https://esajournals.onlinelibrary.wiley.com/doi/abs/10.2307/2937313. Format: Electronic text files. \n\nThis dataset is associated with the following publication:\nBarichievy, C., D. Angeler, T. Eason, A. Garmestani, K. Nash, C. Stow, S. Sundstrom, and C. Allen. A method to detect discontinuities in census data.   Ecology and Evolution. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 8(19): 9614-9623, (2018).",
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
+                "fn": "Tarsha Eason",
+                "hasEmail": "mailto:eason.tarsha@epa.gov"
+            },
+            "description": "The dataset provided by Holling(1922) includes species and body masses of boreal forest birds.  It is a commonly used dataset for discontinuity analysis. This dataset is not publicly accessible because: It is secondary data accessible online. It can be accessed through the following means: All data used are freely available and located in the appendix of Holling (1992):https://esajournals.onlinelibrary.wiley.com/doi/abs/10.2307/2937313. Format: Electronic text files. \n\nThis dataset is associated with the following publication:\nBarichievy, C., D. Angeler, T. Eason, A. Garmestani, K. Nash, C. Stow, S. Sundstrom, and C. Allen. A method to detect discontinuities in census data.   Ecology and Evolution. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 8(19): 9614-9623, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1504118",
             "keyword": [
                 "boreal forest birds",
@@ -100584,14 +100582,10 @@
                 "complex systems",
                 "law and policy"
             ],
-            "contactPoint": {
-                "fn": "Tarsha Eason",
-                "hasEmail": "mailto:eason.tarsha@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-11",
-            "references": [
-                "https://doi.org/10.1002/ece3.4297"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100601,19 +100595,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/ece3.4297"
+            ],
+            "rights": null,
+            "title": "Boreal bird body mass dataset (Holling 1992)"
         },
         {
-            "title": "MagnusonMatthew_A-fqzq_dataset_20191003.xlsx",
-            "description": "Data corresponding to graphs in paper. \n\nThis dataset is associated with the following publication:\nOster, C., M. Kaminski, J. Jerden, and Y. Franchini. Evaluating Solid Sorbents for Recycling Wash Waters Containing Strontium and Calcium.   Journal of Hazardous, Toxic, and Radioactive Waste. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 23(1): ., (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
+            "contactPoint": {
+                "fn": "Matthew Magnuson",
+                "hasEmail": "mailto:magnuson.matthew@epa.gov"
+            },
+            "description": "Data corresponding to graphs in paper. \n\nThis dataset is associated with the following publication:\nOster, C., M. Kaminski, J. Jerden, and Y. Franchini. Evaluating Solid Sorbents for Recycling Wash Waters Containing Strontium and Calcium.   Journal of Hazardous, Toxic, and Radioactive Waste. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 23(1): ., (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504541/MagnusonMatthew_A-fqzq_dataset_20191017.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MagnusonMatthew_A-fqzq_dataset_20191017.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504541",
             "keyword": [
@@ -100624,20 +100628,10 @@
                 "stronium",
                 "Sr-90"
             ],
-            "contactPoint": {
-                "fn": "Matthew Magnuson",
-                "hasEmail": "mailto:magnuson.matthew@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MagnusonMatthew_A-fqzq_dataset_20191017.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504541/MagnusonMatthew_A-fqzq_dataset_20191017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-10-17",
-            "references": [
-                "https://doi.org/10.1061/(asce)hz.2153-5515.0000425"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100647,49 +100641,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/(asce)hz.2153-5515.0000425"
+            ],
+            "rights": null,
+            "title": "MagnusonMatthew_A-fqzq_dataset_20191003.xlsx"
         },
         {
-            "title": "Observations of total phosphorous (TP) to support nearshore nutrient modeling, 2015.",
-            "description": "The USEPA participated in the 2015 Cooperative Science and Monitoring Initiative\n(CSMI) focus year for Lake Michigan.  This work is describd here:\nhttp://www.iiseagrant.org/pdf/LakeMichiganCSMI2015FullReport.pdf\n\nAs a small sub-component of this work EPA staff collected water quality data\nat the locations listed in grand_musk_tp.csv.  The fields in grand_musk_tp.csv\nare described in grand_musk_tp.metadata.csv.  This data was collected to\nsupport (provide validation data for) EPA nearshore nutrient modeling work\ndescribed in the paper (in prep.) \u201cNearshore Nutrient Circulation in the Great\nLakes - can a simple model provide transparency and utility?\u201d.\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503379",
-            "keyword": [
-                "nearshore",
-                "phosphorus",
-                "model"
-            ],
             "contactPoint": {
                 "fn": "Terry Brown",
                 "hasEmail": "mailto:brown.terryn@epa.gov"
             },
+            "description": "The USEPA participated in the 2015 Cooperative Science and Monitoring Initiative\n(CSMI) focus year for Lake Michigan.  This work is describd here:\nhttp://www.iiseagrant.org/pdf/LakeMichiganCSMI2015FullReport.pdf\n\nAs a small sub-component of this work EPA staff collected water quality data\nat the locations listed in grand_musk_tp.csv.  The fields in grand_musk_tp.csv\nare described in grand_musk_tp.metadata.csv.  This data was collected to\nsupport (provide validation data for) EPA nearshore nutrient modeling work\ndescribed in the paper (in prep.) \u201cNearshore Nutrient Circulation in the Great\nLakes - can a simple model provide transparency and utility?\u201d.\n",
             "distribution": [
                 {
-                    "title": "grand_musk_tp.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503379/grand_musk_tp.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "grand_musk_tp.csv"
                 },
                 {
-                    "title": "grand_musk_tp.readme.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503379/grand_musk_tp.readme.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "grand_musk_tp.readme.txt"
                 },
                 {
-                    "title": "grand_musk_tp.metadata.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503379/grand_musk_tp.metadata.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "grand_musk_tp.metadata.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503379",
+            "keyword": [
+                "nearshore",
+                "phosphorus",
+                "model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-15",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -100698,19 +100694,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Observations of total phosphorous (TP) to support nearshore nutrient modeling, 2015."
         },
         {
-            "title": "Wilkin et al. (2019) dataset",
-            "description": "The dataset contains chromatographic traces of samples containing thioarsenic species and solubility data for disordered orpiment (arsenic sulfide). \n\nThis dataset is associated with the following publication:\nWilkin, R.T., R.G. Ford, L.M. Costantino, R.R. Ross, D.G. Beak, and K.G. Scheckel. Thioarsenite Detection and Implications for Arsenic Transport in Groundwater.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(20): 11684-11693, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Richard Wilkin",
+                "hasEmail": "mailto:wilkin.rick@epa.gov"
+            },
+            "description": "The dataset contains chromatographic traces of samples containing thioarsenic species and solubility data for disordered orpiment (arsenic sulfide). \n\nThis dataset is associated with the following publication:\nWilkin, R.T., R.G. Ford, L.M. Costantino, R.R. Ross, D.G. Beak, and K.G. Scheckel. Thioarsenite Detection and Implications for Arsenic Transport in Groundwater.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(20): 11684-11693, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503989/Wilkin%20et%20al.%20%282019%29%20dataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Wilkin et al. (2019) dataset.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503989",
             "keyword": [
@@ -100724,20 +100728,10 @@
                 "iron sulfides",
                 "uranium"
             ],
-            "contactPoint": {
-                "fn": "Richard Wilkin",
-                "hasEmail": "mailto:wilkin.rick@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Wilkin et al. (2019) dataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503989/Wilkin%20et%20al.%20%282019%29%20dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-24",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b04478"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100747,41 +100741,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b04478"
+            ],
+            "rights": null,
+            "title": "Wilkin et al. (2019) dataset"
         },
         {
-            "title": "KC-TRAQS data fusion",
-            "description": "Data collected during the Kansas City Transportation and Local-Scale Air Quality Study (KC-TRAQS). \n\nThis dataset is associated with the following publication:\nIsakov, V., S. Arunachalam, R. Baldauf, M. Breen, P. Deshmukh, A. Hawkins, E. Kimbrough, S. Krabbe, B. Naess, M. Serre, and A. Valencia. Combining Dispersion Modeling and Monitoring Data for Community-Scale Air Quality Characterization.   ATMOSPHERE. MDPI AG, Basel,  SWITZERLAND, 10(10): 610, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1504143",
-            "keyword": [
-                "near-source",
-                "dispersion modeling",
-                "rail yard",
-                "air pollution"
-            ],
             "contactPoint": {
                 "fn": "Vladilen Isakov",
                 "hasEmail": "mailto:isakov.vlad@epa.gov"
             },
+            "description": "Data collected during the Kansas City Transportation and Local-Scale Air Quality Study (KC-TRAQS). \n\nThis dataset is associated with the following publication:\nIsakov, V., S. Arunachalam, R. Baldauf, M. Breen, P. Deshmukh, A. Hawkins, E. Kimbrough, S. Krabbe, B. Naess, M. Serre, and A. Valencia. Combining Dispersion Modeling and Monitoring Data for Community-Scale Air Quality Characterization.   ATMOSPHERE. MDPI AG, Basel,  SWITZERLAND, 10(10): 610, (2019).",
             "distribution": [
                 {
-                    "title": "KC-TRAQS_data_fusion.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504143/KC-TRAQS_data_fusion.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "KC-TRAQS_data_fusion.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504143",
+            "keyword": [
+                "near-source",
+                "dispersion modeling",
+                "rail yard",
+                "air pollution"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-24",
-            "references": [
-                "https://doi.org/10.3390/atmos10100610"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100791,20 +100785,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/atmos10100610"
+            ],
+            "rights": null,
+            "title": "KC-TRAQS data fusion"
         },
         {
-            "title": "Metadata for a manuscript entitled 'Treatment of reverse osmosis concentrate using an algal-based MBR combined with ozone pretreatment'",
-            "description": "No data is available because the raw data was not generated in EPA. This dataset is not publicly accessible because: All data for this manuscript were collected and managed by our collaborator, Sejong University in Seoul Korea. It can be accessed through the following means: Contact Dr. Hyunchul Kim (animaplus@hanmail.net). Format: N/A. \n\nThis dataset is associated with the following publication:\nWoo, H., H.S. Yang, T. Timmes, C. Han, J. Nam, S. Byun, S. Kim, H. Ryu, and H. Kim. Treatment of reverse osmosis concentrate using an algal-based MBR combined with ozone pretreatment.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 159: 164-175, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Hodon Ryu",
+                "hasEmail": "mailto:ryu.hodon@epa.gov"
+            },
+            "description": "No data is available because the raw data was not generated in EPA. This dataset is not publicly accessible because: All data for this manuscript were collected and managed by our collaborator, Sejong University in Seoul Korea. It can be accessed through the following means: Contact Dr. Hyunchul Kim (animaplus@hanmail.net). Format: N/A. \n\nThis dataset is associated with the following publication:\nWoo, H., H.S. Yang, T. Timmes, C. Han, J. Nam, S. Byun, S. Kim, H. Ryu, and H. Kim. Treatment of reverse osmosis concentrate using an algal-based MBR combined with ozone pretreatment.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 159: 164-175, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1504085",
             "keyword": [
                 "reverse osmosis concentrate",
@@ -100813,14 +100811,10 @@
                 "microfiltration",
                 "fouling"
             ],
-            "contactPoint": {
-                "fn": "Hodon Ryu",
-                "hasEmail": "mailto:ryu.hodon@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-10-07",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2019.05.003"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100830,42 +100824,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2019.05.003"
+            ],
+            "rights": null,
+            "title": "Metadata for a manuscript entitled 'Treatment of reverse osmosis concentrate using an algal-based MBR combined with ozone pretreatment'"
         },
         {
-            "title": "A runoff trading system to meet watershed-level stormwater reduction goals with parcel-level green infrastructure installation",
-            "description": "Data are estimated stormwater values based on curve numbers (CN) values are based on hydrologic soil groups (A, B, C, and D) and four land cover types in the study area, such as, grassland, forest land, impervious area, and other open space.  We apply SMPSS-TRAC to a watershed located in Hamilton County, Ohio, USA and develop five scenarios representing increasing use of GI.  We test the scenarios under a 5-year rainfall intensity and set a cap of runoff for each scenario at a level that is equal to the runoff from an undeveloped status (1.03-inch runoff depth for the watershed).  With the proposed SMPSS-TRAC, the watershed authority could encourage all parcel owners to install suitable GI or purchase credits from the market. \n\nThis dataset is associated with the following publication:\nFu, X., M. Hopton, X. Wang, H. Goddard, and H. Liu. A runoff trading system to meet watershed-level stormwater reduction goals with parcel-level green infrastructure installation.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 689: 1149-1159, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1504551",
-            "keyword": [
-                "stormwater management",
-                "stormwater trading",
-                "scenario planning",
-                "planning support system",
-                "Green Infrastructure"
-            ],
             "contactPoint": {
                 "fn": "Matthew Hopton",
                 "hasEmail": "mailto:hopton.matthew@epa.gov"
             },
+            "description": "Data are estimated stormwater values based on curve numbers (CN) values are based on hydrologic soil groups (A, B, C, and D) and four land cover types in the study area, such as, grassland, forest land, impervious area, and other open space.  We apply SMPSS-TRAC to a watershed located in Hamilton County, Ohio, USA and develop five scenarios representing increasing use of GI.  We test the scenarios under a 5-year rainfall intensity and set a cap of runoff for each scenario at a level that is equal to the runoff from an undeveloped status (1.03-inch runoff depth for the watershed).  With the proposed SMPSS-TRAC, the watershed authority could encourage all parcel owners to install suitable GI or purchase credits from the market. \n\nThis dataset is associated with the following publication:\nFu, X., M. Hopton, X. Wang, H. Goddard, and H. Liu. A runoff trading system to meet watershed-level stormwater reduction goals with parcel-level green infrastructure installation.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 689: 1149-1159, (2019).",
             "distribution": [
                 {
-                    "title": "Output of the paper SMPSS-TRAC to STICS.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504551/Output%20of%20the%20paper%20SMPSS-TRAC%20to%20STICS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Output of the paper SMPSS-TRAC to STICS.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504551",
+            "keyword": [
+                "stormwater management",
+                "stormwater trading",
+                "scenario planning",
+                "planning support system",
+                "Green Infrastructure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-01",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2019.06.439"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -100875,107 +100869,109 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2019.06.439"
+            ],
+            "rights": null,
+            "title": "A runoff trading system to meet watershed-level stormwater reduction goals with parcel-level green infrastructure installation"
         },
         {
-            "title": "Decentralized water reuse for San Francisco building and district scenarios",
-            "description": "The dataset included the inventories, impact assessments and cost analyses of different scenarios at the different scales (building and district) and with different water source being reuse (mixed wastewater, graywater).  And also inventoaries for thermal recovery and vertical flow wetland. \n\nThis dataset is associated with the following publication:\nMorelli, B., S. Cashman, X. Ma, J. Garland, D. Bless, and M. Jahne. Life Cycle Assessment and Cost Analysis of Distributed Mixed Wastewater and Graywater Treatment for Water Recycling in the Context of an Urban Case Study. U.S. Environmental Protection Agency, Washington, DC, USA, 2019.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503201",
-            "keyword": [
-                "water reuse"
-            ],
             "contactPoint": {
                 "fn": "Xin Ma",
                 "hasEmail": "mailto:ma.cissy@epa.gov"
             },
+            "description": "The dataset included the inventories, impact assessments and cost analyses of different scenarios at the different scales (building and district) and with different water source being reuse (mixed wastewater, graywater).  And also inventoaries for thermal recovery and vertical flow wetland. \n\nThis dataset is associated with the following publication:\nMorelli, B., S. Cashman, X. Ma, J. Garland, D. Bless, and M. Jahne. Life Cycle Assessment and Cost Analysis of Distributed Mixed Wastewater and Graywater Treatment for Water Recycling in the Context of an Urban Case Study. U.S. Environmental Protection Agency, Washington, DC, USA, 2019.",
             "distribution": [
                 {
-                    "title": "AeMBR Graywater Building Scale LCI Calcs_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/AeMBR%20Graywater%20Building%20Scale%20LCI%20Calcs_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AeMBR Graywater Building Scale LCI Calcs_SF Reuse.xlsx"
                 },
                 {
-                    "title": "AeMBR Mixed Wastewater Building Scale LCI Calcs_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/AeMBR%20Mixed%20Wastewater%20Building%20Scale%20LCI%20Calcs_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AeMBR Mixed Wastewater Building Scale LCI Calcs_SF Reuse.xlsx"
                 },
                 {
-                    "title": "AnMBR Mixed Wastewater Building Scale LCI Calcs_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/AnMBR%20Mixed%20Wastewater%20Building%20Scale%20LCI%20Calcs_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AnMBR Mixed Wastewater Building Scale LCI Calcs_SF Reuse.xlsx"
                 },
                 {
-                    "title": "Decentralized Disinfection Scenarios_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/Decentralized%20Disinfection%20Scenarios_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Decentralized Disinfection Scenarios_SF Reuse.xlsx"
                 },
                 {
-                    "title": "AeMBR Mixed Wastewater District Scale LCI Calcs_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/AeMBR%20Mixed%20Wastewater%20District%20Scale%20LCI%20Calcs_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AeMBR Mixed Wastewater District Scale LCI Calcs_SF Reuse.xlsx"
                 },
                 {
-                    "title": "AeMBR Mixed Wastewater District Scale Unsewered LCI Calcs_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/AeMBR%20Mixed%20Wastewater%20District%20Scale%20Unsewered%20LCI%20Calcs_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AeMBR Mixed Wastewater District Scale Unsewered LCI Calcs_SF Reuse.xlsx"
                 },
                 {
-                    "title": "AnMBR Graywater Building Scale LCI Calcs_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/AnMBR%20Graywater%20Building%20Scale%20LCI%20Calcs_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AnMBR Graywater Building Scale LCI Calcs_SF Reuse.xlsx"
                 },
                 {
-                    "title": "README.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/README.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "README.xlsx"
                 },
                 {
-                    "title": "AeMBR Graywater District Scale LCI Calcs_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/AeMBR%20Graywater%20District%20Scale%20LCI%20Calcs_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AeMBR Graywater District Scale LCI Calcs_SF Reuse.xlsx"
                 },
                 {
-                    "title": "Building and District Reuse Scenarios_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/Building%20and%20District%20Reuse%20Scenarios_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Building and District Reuse Scenarios_SF Reuse.xlsx"
                 },
                 {
-                    "title": "Decentralized Thermal Recovery Calculations_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/Decentralized%20Thermal%20Recovery%20Calculations_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Decentralized Thermal Recovery Calculations_SF Reuse.xlsx"
                 },
                 {
-                    "title": "LCA_LCCA_Distributed_GW_WW_Treatment.DraftFinal.6.7.2019.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/LCA_LCCA_Distributed_GW_WW_Treatment.DraftFinal.6.7.2019.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "LCA_LCCA_Distributed_GW_WW_Treatment.DraftFinal.6.7.2019.docx"
                 },
                 {
-                    "title": "LCA_LCCA_Distributed_GW_WW_Treatment.DraftFinal.6.7.2019_trackchanges.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/LCA_LCCA_Distributed_GW_WW_Treatment.DraftFinal.6.7.2019_trackchanges.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "LCA_LCCA_Distributed_GW_WW_Treatment.DraftFinal.6.7.2019_trackchanges.docx"
                 },
                 {
-                    "title": "Decentralized Life Cycle Cost Assessment_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/Decentralized%20Life%20Cycle%20Cost%20Assessment_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Decentralized Life Cycle Cost Assessment_SF Reuse.xlsx"
                 },
                 {
-                    "title": "Decentralized LCIA Results_SF Reuse.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503201/Decentralized%20LCIA%20Results_SF%20Reuse.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Decentralized LCIA Results_SF Reuse.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503201",
+            "keyword": [
+                "water reuse"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-17",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -100984,19 +100980,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Decentralized water reuse for San Francisco building and district scenarios"
         },
         {
-            "title": "Emergy tables of unit process involved in struvite and DAP productions",
-            "description": "This dataset compiled the emergy tables of different unit processes used in in struvite production and DAP production. \n\nThis dataset is associated with the following publication:\nTheregowda, R., A. Gonz\u00e1lez-Mej\u00eda, C. Ma, and J. Garland. Nutrient recovery from municipal wastewater for sustainable food production systems: An alternative to traditional fertilizers..   ENVIRONMENTAL ENGINEERING SCIENCE. Mary Ann Liebert, Inc., Larchmont, NY, USA, 36(7): 833-842, (2019).",
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
+            "description": "This dataset compiled the emergy tables of different unit processes used in in struvite production and DAP production. \n\nThis dataset is associated with the following publication:\nTheregowda, R., A. Gonz\u00e1lez-Mej\u00eda, C. Ma, and J. Garland. Nutrient recovery from municipal wastewater for sustainable food production systems: An alternative to traditional fertilizers..   ENVIRONMENTAL ENGINEERING SCIENCE. Mary Ann Liebert, Inc., Larchmont, NY, USA, 36(7): 833-842, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500946/P%20EMergy%202018_Latest.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "P EMergy 2018_Latest.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500946",
             "keyword": [
@@ -101008,20 +101012,10 @@
                 "resource recovery",
                 "fertilizer"
             ],
-            "contactPoint": {
-                "fn": "Xin Ma",
-                "hasEmail": "mailto:ma.cissy@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "P EMergy 2018_Latest.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500946/P%20EMergy%202018_Latest.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-12",
-            "references": [
-                "https://doi.org/10.1089/ees.2019.0053"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101031,41 +101025,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1089/ees.2019.0053"
+            ],
+            "rights": null,
+            "title": "Emergy tables of unit process involved in struvite and DAP productions"
         },
         {
-            "title": "Sequential Sampling Paper",
-            "description": "This work discusses drinking water sampling efforts for lead in Flint, MI. \n\nThis dataset is associated with the following publication:\nLytle, D., M. Schock, K. Wait, K. Cahalan, V. Bosscher, A. Porter, and M. Deltoral. SEQUENTIAL DRINKING WATER SAMPLING AS A TOOL FOR EVALUATING LEAD IN FLINT, MICHIGAN.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 157: 40-54, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500899",
-            "keyword": [
-                "lead",
-                "drinking water",
-                "sequential samples",
-                "Orthophosphate"
-            ],
             "contactPoint": {
                 "fn": "Darren Lytle",
                 "hasEmail": "mailto:lytle.darren@epa.gov"
             },
+            "description": "This work discusses drinking water sampling efforts for lead in Flint, MI. \n\nThis dataset is associated with the following publication:\nLytle, D., M. Schock, K. Wait, K. Cahalan, V. Bosscher, A. Porter, and M. Deltoral. SEQUENTIAL DRINKING WATER SAMPLING AS A TOOL FOR EVALUATING LEAD IN FLINT, MICHIGAN.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 157: 40-54, (2019).",
             "distribution": [
                 {
-                    "title": "CleanedData_3_4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500899/CleanedData_3_4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CleanedData_3_4.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500899",
+            "keyword": [
+                "lead",
+                "drinking water",
+                "sequential samples",
+                "Orthophosphate"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-22",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2019.03.042"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101075,40 +101069,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2019.03.042"
+            ],
+            "rights": null,
+            "title": "Sequential Sampling Paper"
         },
         {
-            "title": "Simulating Lightning NOX Production in CMAQv5.2: Performance Evaluations",
-            "description": "The description of the dataset and all relevant information are provided at the linked webpage. \n\nThis dataset is associated with the following publication:\nKang, D., K. Foley, R. Mathur, S. Roselle, K. Pickering, and D. Allen. Simulating Lightning NO Production in CMAQv5.2: Performance Evaluations.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 12(10): 4409\u20134424, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503744",
-            "keyword": [
-                "Lightning NOx emissions",
-                "Ozone",
-                "air quality",
-                "NOx emissions"
-            ],
             "contactPoint": {
                 "fn": "Daiwen Kang",
                 "hasEmail": "mailto:kang.daiwen@epa.gov"
             },
+            "description": "The description of the dataset and all relevant information are provided at the linked webpage. \n\nThis dataset is associated with the following publication:\nKang, D., K. Foley, R. Mathur, S. Roselle, K. Pickering, and D. Allen. Simulating Lightning NO Production in CMAQv5.2: Performance Evaluations.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 12(10): 4409\u20134424, (2019).",
             "distribution": [
                 {
-                    "title": "https://zenodo.org/record/3360744",
-                    "accessURL": "https://zenodo.org/record/3360744"
+                    "accessURL": "https://zenodo.org/record/3360744",
+                    "title": "https://zenodo.org/record/3360744"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503744",
+            "keyword": [
+                "Lightning NOx emissions",
+                "Ozone",
+                "air quality",
+                "NOx emissions"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-02",
-            "references": [
-                "https://doi.org/10.5194/gmd-12-4409-2019"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101118,41 +101112,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/gmd-12-4409-2019"
+            ],
+            "rights": null,
+            "title": "Simulating Lightning NOX Production in CMAQv5.2: Performance Evaluations"
         },
         {
-            "title": "Human Exposure Factors dataset",
-            "description": "This dataset consists of the data used to create the tables and figures for this paper. \n\nThis dataset is associated with the following publication:\nBaxter, L., K. Dionisio, P. Pradeep, K. Rappazzo, and L. Neas. Human exposure factors as potential determinants of the heterogeneity in city-specific associations between PM2.5 and mortality.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 29(4): 557-567, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1395252",
-            "keyword": [
-                "Fine Particulate Matter",
-                "Exposure factors",
-                "epidemiology",
-                "meta-regression"
-            ],
             "contactPoint": {
                 "fn": "Lisa Baxter",
                 "hasEmail": "mailto:baxter.lisa@epa.gov"
             },
+            "description": "This dataset consists of the data used to create the tables and figures for this paper. \n\nThis dataset is associated with the following publication:\nBaxter, L., K. Dionisio, P. Pradeep, K. Rappazzo, and L. Neas. Human exposure factors as potential determinants of the heterogeneity in city-specific associations between PM2.5 and mortality.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 29(4): 557-567, (2019).",
             "distribution": [
                 {
-                    "title": "Baxter A-zcsc datasets.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395252/Baxter%20A-zcsc%20datasets.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Baxter A-zcsc datasets.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1395252",
+            "keyword": [
+                "Fine Particulate Matter",
+                "Exposure factors",
+                "epidemiology",
+                "meta-regression"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-25",
-            "references": [
-                "https://doi.org/10.1038/s41370-018-0080-7"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101162,20 +101156,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-018-0080-7"
+            ],
+            "rights": null,
+            "title": "Human Exposure Factors dataset"
         },
         {
-            "title": "Application of a salivary immunoassay in a prospective community study of waterborne infections",
-            "description": "The data are stored as a SAS dataset containing PII. The dataset contains baseline questionnaire, monthly follow-up questionnaire data, and results and salivary antibody tests for IgG and IgA response to selected antigens of potentially waterborne pathogens. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: See above. Format: The study database include baseline questionnaire, monthly follow-up questionnaire, and results of salivary antibody tests for 1,986 study participants. The dataset contains PII data. The data are stored as a SAS database. \n\nThis dataset is associated with the following publication:\nEgorov, A., S. Griffin, H. Ward, K. Reilly, G.S. Fout, and T. Wade. Application of a salivary immunoassay in a prospective community study of waterborne infections.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 142: 289-300, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Andrey Egorov",
+                "hasEmail": "mailto:egorov.andrey@epa.gov"
+            },
+            "description": "The data are stored as a SAS dataset containing PII. The dataset contains baseline questionnaire, monthly follow-up questionnaire data, and results and salivary antibody tests for IgG and IgA response to selected antigens of potentially waterborne pathogens. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: See above. Format: The study database include baseline questionnaire, monthly follow-up questionnaire, and results of salivary antibody tests for 1,986 study participants. The dataset contains PII data. The data are stored as a SAS database. \n\nThis dataset is associated with the following publication:\nEgorov, A., S. Griffin, H. Ward, K. Reilly, G.S. Fout, and T. Wade. Application of a salivary immunoassay in a prospective community study of waterborne infections.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 142: 289-300, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1410987",
             "keyword": [
                 "waterborne infection",
@@ -101185,14 +101183,10 @@
                 "drinking water",
                 "recreational water"
             ],
-            "contactPoint": {
-                "fn": "Andrey Egorov",
-                "hasEmail": "mailto:egorov.andrey@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-30",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2018.05.030"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101202,51 +101196,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2018.05.030"
+            ],
+            "rights": null,
+            "title": "Application of a salivary immunoassay in a prospective community study of waterborne infections"
         },
         {
-            "title": "Cost modeling data",
-            "description": "The associated excel files hold the cost predictions for nitrate and perchlorate treatment based on a series of assumptions outlined in the paper.  No experimental data was generated in this project. \n\nThis dataset is associated with the following publication:\nLatham , M. SSWR FY14 Output Summary Report: Performance information and design tools are developed for innovative technologies and approaches for Small Drinking Water and Wastewater Systems. U.S. Environmental Protection Agency, Washington, DC, USA.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1504015",
-            "keyword": [
-                "nitrate",
-                "perchlorate",
-                "drinking water",
-                "treatment",
-                "cost"
-            ],
             "contactPoint": {
                 "fn": "Thomas Speth",
                 "hasEmail": "mailto:speth.thomas@epa.gov"
             },
+            "description": "The associated excel files hold the cost predictions for nitrate and perchlorate treatment based on a series of assumptions outlined in the paper.  No experimental data was generated in this project. \n\nThis dataset is associated with the following publication:\nLatham , M. SSWR FY14 Output Summary Report: Performance information and design tools are developed for innovative technologies and approaches for Small Drinking Water and Wastewater Systems. U.S. Environmental Protection Agency, Washington, DC, USA.",
             "distribution": [
                 {
-                    "title": "Copy of Perchlorate Figure 4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504015/Copy%20of%20Perchlorate%20Figure%204.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of Perchlorate Figure 4.xlsx"
                 },
                 {
-                    "title": "2019-04-26 Nitrate Figure 3 with FXB and 3 pct.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504015/2019-04-26%20Nitrate%20Figure%203%20with%20FXB%20and%203%20pct.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2019-04-26 Nitrate Figure 3 with FXB and 3 pct.xlsx"
                 },
                 {
-                    "title": "2019-04-15 Nitrate Figures 1 and 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504015/2019-04-15%20Nitrate%20Figures%201%20and%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2019-04-15 Nitrate Figures 1 and 2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504015",
+            "keyword": [
+                "nitrate",
+                "perchlorate",
+                "drinking water",
+                "treatment",
+                "cost"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-28",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -101255,19 +101251,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Cost modeling data"
         },
         {
-            "title": "Data used for Appendix B of A natural capital perspective on waterfront revitalization in Great Lakes Areas Concern: Goals, beneficiaries, and indicators",
-            "description": "Keyword analysis of nine IAGLR AOC case studies. \n\nThis dataset is associated with the following publication:\nAngradi, T., K. Williams, J. Hoffman, and D. Bolgrien. Goals, beneficiaries, and indicators  of waterfront revitalization in Great Lakes Areas of Concern and coastal communities.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 45(5): 851-863, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Theodore Angradi",
+                "hasEmail": "mailto:angradi.theodore@epa.gov"
+            },
+            "description": "Keyword analysis of nine IAGLR AOC case studies. \n\nThis dataset is associated with the following publication:\nAngradi, T., K. Williams, J. Hoffman, and D. Bolgrien. Goals, beneficiaries, and indicators  of waterfront revitalization in Great Lakes Areas of Concern and coastal communities.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 45(5): 851-863, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503303/Appendix%20B%20Keyword%20analysis.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Appendix B Keyword analysis.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503303",
             "keyword": [
@@ -101281,21 +101285,10 @@
                 "ecosystem indicators",
                 "Environmental Justice"
             ],
-            "contactPoint": {
-                "fn": "Theodore Angradi",
-                "hasEmail": "mailto:angradi.theodore@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Appendix B Keyword analysis.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503303/Appendix%20B%20Keyword%20analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-24",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2019.07.001",
-                "https://pasteur.epa.gov/uploads/10.23719/1503303/documents/Appendix%20B%20Keyword%20analysis.xlsx"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101305,44 +101298,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2019.07.001",
+                "https://pasteur.epa.gov/uploads/10.23719/1503303/documents/Appendix%20B%20Keyword%20analysis.xlsx"
+            ],
+            "rights": null,
+            "title": "Data used for Appendix B of A natural capital perspective on waterfront revitalization in Great Lakes Areas Concern: Goals, beneficiaries, and indicators"
         },
         {
-            "title": "Demodifying RNA for Transcriptomic Analyses of Archival Formalin-Fixed Paraffin-Embedded Samples",
-            "description": "Low RNA yield and quality limit use of formalin-fixed paraffin-embedded (FFPE) tissue samples for genomic analyses. In this study, we evaluated methods to demodify RNA highly fragmented and crosslinked by formalin fixation. Primary endpoints were RNA recovery, RNA-sequencing quality metrics, and target gene responses to a reference chemical (phenobarbital, PB). Frozen mouse liver samples from control and PB groups (n=6/group) were divided and preserved for 3 months as follows: frozen (FR); 70% ethanol (OH); 10% buffered formalin for 18 hours followed by ethanol (18F); and 10% buffered formalin (3F). Samples from OH, 18F, and 3F groups were processed to FFPE blocks and sectioned for RNA isolation. The latter group received no additional treatment (3F) or the following demodification protocols: short heated incubation with TAE buffer; overnight heated incubation with an organocatalyst using two different isolation kits; or overnight heated incubation without organocatalyst. TruSeq Stranded Total RNA libraries with Ribo-Zero were built and sequenced using the Illumina HiSeq platform. Extended incubation with or without organocatalyst increased RNA yield >3-fold and enhanced quality compared to 3F, as indicated by higher RNA integrity number (>1.5-fold) and fragment analysis values (>3.0-fold). Post-sequencing metrics showed reduced bias in gene coverage and deletion rates for all extended incubation groups. Following PB-induced differential gene expression analysis, all demodification groups showed increased overlap with FR in genes (73-83%) and pathways (91-94%) compared to 3F overlap with FR (60% and 63%, respectively). These results demonstrate simple changes in RNA isolation methods that can enhance genomic analyses of FFPE samples. \n\nThis dataset is associated with the following publication:\nWehmas, L., C. Wood, R. Gagne, A. Williams, C. Yauk, M. Gosink, D. Dalmas, R. Hao, R. O'Lone, and S. Hester. Demodifying RNA for Transcriptomic Analyses of Archival Formalin-Fixed Paraffin-Embedded Samples.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  162(2): 535-547, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503129",
-            "keyword": [
-                "RNA_Seq analysis",
-                "Formalin-fixed paraffin embedded samples",
-                "Demodification methods"
-            ],
             "contactPoint": {
                 "fn": "Susan Hester",
                 "hasEmail": "mailto:hester.susan@epa.gov"
             },
+            "description": "Low RNA yield and quality limit use of formalin-fixed paraffin-embedded (FFPE) tissue samples for genomic analyses. In this study, we evaluated methods to demodify RNA highly fragmented and crosslinked by formalin fixation. Primary endpoints were RNA recovery, RNA-sequencing quality metrics, and target gene responses to a reference chemical (phenobarbital, PB). Frozen mouse liver samples from control and PB groups (n=6/group) were divided and preserved for 3 months as follows: frozen (FR); 70% ethanol (OH); 10% buffered formalin for 18 hours followed by ethanol (18F); and 10% buffered formalin (3F). Samples from OH, 18F, and 3F groups were processed to FFPE blocks and sectioned for RNA isolation. The latter group received no additional treatment (3F) or the following demodification protocols: short heated incubation with TAE buffer; overnight heated incubation with an organocatalyst using two different isolation kits; or overnight heated incubation without organocatalyst. TruSeq Stranded Total RNA libraries with Ribo-Zero were built and sequenced using the Illumina HiSeq platform. Extended incubation with or without organocatalyst increased RNA yield >3-fold and enhanced quality compared to 3F, as indicated by higher RNA integrity number (>1.5-fold) and fragment analysis values (>3.0-fold). Post-sequencing metrics showed reduced bias in gene coverage and deletion rates for all extended incubation groups. Following PB-induced differential gene expression analysis, all demodification groups showed increased overlap with FR in genes (73-83%) and pathways (91-94%) compared to 3F overlap with FR (60% and 63%, respectively). These results demonstrate simple changes in RNA isolation methods that can enhance genomic analyses of FFPE samples. \n\nThis dataset is associated with the following publication:\nWehmas, L., C. Wood, R. Gagne, A. Williams, C. Yauk, M. Gosink, D. Dalmas, R. Hao, R. O'Lone, and S. Hester. Demodifying RNA for Transcriptomic Analyses of Archival Formalin-Fixed Paraffin-Embedded Samples.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  162(2): 535-547, (2018).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103440",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103440"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103440",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103440"
                 },
                 {
-                    "title": "Wehmas_to_Hester.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503129/Wehmas_to_Hester.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Wehmas_to_Hester.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503129",
+            "keyword": [
+                "RNA_Seq analysis",
+                "Formalin-fixed paraffin embedded samples",
+                "Demodification methods"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-11",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfx278"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101352,19 +101346,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfx278"
+            ],
+            "rights": null,
+            "title": "Demodifying RNA for Transcriptomic Analyses of Archival Formalin-Fixed Paraffin-Embedded Samples"
         },
         {
-            "title": "Early Proteome Shift and Serum Bioactivity Precede Diesel Exhaust-induced Impairment of Cardiovascular Recovery in Spontaneously Hypertensive Rats",
-            "description": "The dataset is an excel spreadsheet containing the raw data used to generate the tables and figures in the manuscript. \n\nThis dataset is associated with the following publication:\nThompson, L., J. Shanahan, C. Perez, N. Coates, C. King, M. Hazari, J. Brown, and A. Farraj. Early Proteome Shift and Serum Bioactivity Precede Diesel Exhaust-induced Impairment of Cardiovascular Recovery in Spontaneously Hypertensive Rats.   Scientific Reports. Nature Publishing Group, London,  UK, 9(1): 6885, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Leslie Thompson",
+                "hasEmail": "mailto:thompson.leslie@epa.gov"
+            },
+            "description": "The dataset is an excel spreadsheet containing the raw data used to generate the tables and figures in the manuscript. \n\nThis dataset is associated with the following publication:\nThompson, L., J. Shanahan, C. Perez, N. Coates, C. King, M. Hazari, J. Brown, and A. Farraj. Early Proteome Shift and Serum Bioactivity Precede Diesel Exhaust-induced Impairment of Cardiovascular Recovery in Spontaneously Hypertensive Rats.   Scientific Reports. Nature Publishing Group, London,  UK, 9(1): 6885, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500880/Thompson%20et%20al_All%20Data_Sci%20Reports_11-16-2018.docx.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Thompson et al_All Data_Sci Reports_11-16-2018.docx.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500880",
             "keyword": [
@@ -101378,20 +101382,10 @@
                 "proteomics",
                 "serum bioactivity"
             ],
-            "contactPoint": {
-                "fn": "Leslie Thompson",
-                "hasEmail": "mailto:thompson.leslie@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Thompson et al_All Data_Sci Reports_11-16-2018.docx.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500880/Thompson%20et%20al_All%20Data_Sci%20Reports_11-16-2018.docx.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-21",
-            "references": [
-                "https://doi.org/10.1038/s41598-019-43339-8"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101401,40 +101395,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-019-43339-8"
+            ],
+            "rights": null,
+            "title": "Early Proteome Shift and Serum Bioactivity Precede Diesel Exhaust-induced Impairment of Cardiovascular Recovery in Spontaneously Hypertensive Rats"
         },
         {
-            "title": "WRF-ACI-Paper-1",
-            "description": "Data for all tables and figures are in netCDF format. \n\nThis dataset is associated with the following publication:\nGlotfelty, T., K. Alapaty, J. He, P. Hawbecker, X. Song, and G. Zhang. The Weather Research and Forecasting Model with Aerosol\u2013Cloud Interactions (WRF-ACI): Development, Evaluation, and Initial Application.   Monthly Weather Review. American Meteorological Society, Boston, MA, USA, 147(5): 1491-1511, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1413202",
-            "keyword": [
-                "numerical weather prediction",
-                "aerosol radiative forcing",
-                "precipitation cloud life cloud cover",
-                "aerosol indirect effects"
-            ],
             "contactPoint": {
                 "fn": "Kirankumar Alapaty",
                 "hasEmail": "mailto:alapaty.kiran@epa.gov"
             },
+            "description": "Data for all tables and figures are in netCDF format. \n\nThis dataset is associated with the following publication:\nGlotfelty, T., K. Alapaty, J. He, P. Hawbecker, X. Song, and G. Zhang. The Weather Research and Forecasting Model with Aerosol\u2013Cloud Interactions (WRF-ACI): Development, Evaluation, and Initial Application.   Monthly Weather Review. American Meteorological Society, Boston, MA, USA, 147(5): 1491-1511, (2019).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/WRF-ACI-Part-1-Data/",
-                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/WRF-ACI-Part-1-Data/"
+                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/WRF-ACI-Part-1-Data/",
+                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/WRF-ACI-Part-1-Data/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1413202",
+            "keyword": [
+                "numerical weather prediction",
+                "aerosol radiative forcing",
+                "precipitation cloud life cloud cover",
+                "aerosol indirect effects"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-13",
-            "references": [
-                "https://doi.org/10.1175/mwr-d-18-0267.1"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101444,48 +101438,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1175/mwr-d-18-0267.1"
+            ],
+            "rights": null,
+            "title": "WRF-ACI-Paper-1"
         },
         {
-            "title": "Dataset: Smoldering and Flaming Biomass Wood Smoke Inhibit Respiratory Responses in Mice",
-            "description": "The dataset consists of 2 revised files. The excel file shows all of the individual data used in calculation of the tables and figures. Each table and figure has data stored on a separate tab of the file. The zip file consists of 5 GraphPad Prism files which show the statistics and graphs used in the paper. The names of the 5 files indicate which figures and tables are analyzed statistically and the graphs generated from the data. \n\nThis dataset is associated with the following publication:\nHargrove, M., Y.H. Kim, C. King, C. Wood, M. Gilmour, J. Dye, and S. Gavett. Smoldering and Flaming Biomass Wood Smoke Inhibit Respiratory Responses in Mice.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 31(6): 236-247, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503946",
-            "keyword": [
-                "wood smoke",
-                "asthma",
-                "biomass burning",
-                "pulmonary function",
-                "MICE",
-                "lung inflammation"
-            ],
             "contactPoint": {
                 "fn": "Stephen Gavett",
                 "hasEmail": "mailto:gavett.stephen@epa.gov"
             },
+            "description": "The dataset consists of 2 revised files. The excel file shows all of the individual data used in calculation of the tables and figures. Each table and figure has data stored on a separate tab of the file. The zip file consists of 5 GraphPad Prism files which show the statistics and graphs used in the paper. The names of the 5 files indicate which figures and tables are analyzed statistically and the graphs generated from the data. \n\nThis dataset is associated with the following publication:\nHargrove, M., Y.H. Kim, C. King, C. Wood, M. Gilmour, J. Dye, and S. Gavett. Smoldering and Flaming Biomass Wood Smoke Inhibit Respiratory Responses in Mice.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 31(6): 236-247, (2019).",
             "distribution": [
                 {
-                    "title": "Hargrove 2019 biomass Science Hub data rev2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503946/Hargrove%202019%20biomass%20Science%20Hub%20data%20rev2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Hargrove 2019 biomass Science Hub data rev2.xlsx"
                 },
                 {
-                    "title": "GraphPadPrism figures statistics rev.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503946/GraphPadPrism%20figures%20statistics%20rev.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "GraphPadPrism figures statistics rev.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503946",
+            "keyword": [
+                "wood smoke",
+                "asthma",
+                "biomass burning",
+                "pulmonary function",
+                "MICE",
+                "lung inflammation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-19",
-            "references": [
-                "https://doi.org/10.1080/08958378.2019.1654046"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101495,45 +101489,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08958378.2019.1654046"
+            ],
+            "rights": null,
+            "title": "Dataset: Smoldering and Flaming Biomass Wood Smoke Inhibit Respiratory Responses in Mice"
         },
         {
-            "title": "VOC Database and Supporting Data",
-            "description": "Continuous PM2.5 and tVOC sensor data paired with coincidental RH and temp measurements. \n\nThis dataset is associated with the following publication:\nClements, A., S. Reece, T. Conner, and R. Williams. Observed Data Quality Concerns Involving Low-Cost Air Sensors.   Atmospheric Environment: X. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 100034, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503153",
-            "keyword": [
-                "low cost sensor",
-                "pm2.5",
-                "tVOCs"
-            ],
             "contactPoint": {
                 "fn": "Ronald Williams",
                 "hasEmail": "mailto:williams.ronald@epa.gov"
             },
+            "description": "Continuous PM2.5 and tVOC sensor data paired with coincidental RH and temp measurements. \n\nThis dataset is associated with the following publication:\nClements, A., S. Reece, T. Conner, and R. Williams. Observed Data Quality Concerns Involving Low-Cost Air Sensors.   Atmospheric Environment: X. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 100034, (2019).",
             "distribution": [
                 {
-                    "title": "Short_Communications_VOCDatabase.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503153/Short_Communications_VOCDatabase.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Short_Communications_VOCDatabase.xlsx"
                 },
                 {
-                    "title": "ShortCommunication_SupportingData-PMexample.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503153/ShortCommunication_SupportingData-PMexample.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ShortCommunication_SupportingData-PMexample.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503153",
+            "keyword": [
+                "low cost sensor",
+                "pm2.5",
+                "tVOCs"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-10-24",
-            "references": [
-                "https://doi.org/10.1016/j.aeaoa.2019.100034"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101543,49 +101537,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.aeaoa.2019.100034"
+            ],
+            "rights": null,
+            "title": "VOC Database and Supporting Data"
         },
         {
-            "title": "Beta-2 adrenergic and glucocorticoid receptor agonists modulate ozone-induced pulmonary protein leakage and inflammation in healthy and adrenalectomized rats",
-            "description": "We have previously shown that neuroendocrine activation leading to increased circulating stress hormones was necessary for mediating ozone-induced lung injury and inflammation since adrenalectomy rats were protected from these ozone effects. Because adrenalectomy is invasive and also eliminates circulating mineralocorticoids along with stress hormones, one cannot rule out their contribution in diminution of ozone-induced lung effects. The goal of this study was to evaluate if agonists of stress hormone receptors \u03b22 adrenergic receptors and glucocorticoid receptors were able to restore ozone-induced lung injury, inflammation and innate immune cell trafficking in adrenalectomy rats, and exacerbate these effects in control rats with sham surgery. Here, we reconfirmed that the pulmonary and systemic effects of ozone inhalation, characterized by vascular leakage, neutrophilic inflammation, cytokine release in the lungs and peripheral vascular lymphopenia, were significantly diminished by adrenlectomy. The treatment with a combination of \u03b22 adrenergic receptor and glucocorticoid receptor agonists (Clenbuterol and dexamethasone) was able to restore these ozone effects in AD rats, and further exacerbate ozone-induced lung protein leakage, inflammation and lymphopenia in sham surgery rats. It was also noted that clenbuterol plus dexamethasone itself caused injury and cytokine increases in the lung. Although a variety of \u03b22 adrenergic receptor and glucocorticoid agonists have been widely used for the treatment of chronic lung diseases, \u03b22 adrenergic receptor agonists have been shown to exacerbate lung inflammation in asthmatics and epidemiological studies have indicated exacerbation of lung inflammation in asthmatics during increased air pollution episodes. Even though high concentrations of agonists were used, our study provides a potential causal mechanistic link between activation of stress hormone receptors in mediation of air pollution health effects, and how these effects might be exacerbated in those receiving asthma therapy. \n\nThis dataset is associated with the following publication:\nHenriquez, A., S. Snow, M. Schladweiler, C. Miller, J. Dye, A. Ledbetter, J. Richards, M. Hargrove, W. Williams, and U. Kodavanti. Beta-2 adrenergic and glucocorticoid receptor agonists modulate ozone-induced pulmonary protein leakage and inflammation in healthy and adrenalectomized rats.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  166(2): 288-305, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1407659",
-            "keyword": [
-                "Ozone",
-                "adrenalectomy",
-                "adrenergic receptor agonist",
-                "glucocorticoid receptor agonist",
-                "neuroendocrine stress axes",
-                "broncho dilators",
-                "steroids"
-            ],
             "contactPoint": {
                 "fn": "Urmila Kodavanti",
                 "hasEmail": "mailto:kodavanti.urmila@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407659/documents/Henriquez%20et%20al.%20-Adrex%20paper%20-%20STICS%201-6-2018.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "We have previously shown that neuroendocrine activation leading to increased circulating stress hormones was necessary for mediating ozone-induced lung injury and inflammation since adrenalectomy rats were protected from these ozone effects. Because adrenalectomy is invasive and also eliminates circulating mineralocorticoids along with stress hormones, one cannot rule out their contribution in diminution of ozone-induced lung effects. The goal of this study was to evaluate if agonists of stress hormone receptors \u03b22 adrenergic receptors and glucocorticoid receptors were able to restore ozone-induced lung injury, inflammation and innate immune cell trafficking in adrenalectomy rats, and exacerbate these effects in control rats with sham surgery. Here, we reconfirmed that the pulmonary and systemic effects of ozone inhalation, characterized by vascular leakage, neutrophilic inflammation, cytokine release in the lungs and peripheral vascular lymphopenia, were significantly diminished by adrenlectomy. The treatment with a combination of \u03b22 adrenergic receptor and glucocorticoid receptor agonists (Clenbuterol and dexamethasone) was able to restore these ozone effects in AD rats, and further exacerbate ozone-induced lung protein leakage, inflammation and lymphopenia in sham surgery rats. It was also noted that clenbuterol plus dexamethasone itself caused injury and cytokine increases in the lung. Although a variety of \u03b22 adrenergic receptor and glucocorticoid agonists have been widely used for the treatment of chronic lung diseases, \u03b22 adrenergic receptor agonists have been shown to exacerbate lung inflammation in asthmatics and epidemiological studies have indicated exacerbation of lung inflammation in asthmatics during increased air pollution episodes. Even though high concentrations of agonists were used, our study provides a potential causal mechanistic link between activation of stress hormone receptors in mediation of air pollution health effects, and how these effects might be exacerbated in those receiving asthma therapy. \n\nThis dataset is associated with the following publication:\nHenriquez, A., S. Snow, M. Schladweiler, C. Miller, J. Dye, A. Ledbetter, J. Richards, M. Hargrove, W. Williams, and U. Kodavanti. Beta-2 adrenergic and glucocorticoid receptor agonists modulate ozone-induced pulmonary protein leakage and inflammation in healthy and adrenalectomized rats.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  166(2): 288-305, (2018).",
             "distribution": [
                 {
-                    "title": "Henriquez 2017 Manuscript for Tox Sci - Data for ScienceHub - Kodavanti 9 21 17.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407659/Henriquez%202017%20Manuscript%20for%20Tox%20Sci%20-%20Data%20for%20ScienceHub%20-%20Kodavanti%209%2021%2017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Henriquez 2017 Manuscript for Tox Sci - Data for ScienceHub - Kodavanti 9 21 17.xlsx"
                 },
                 {
-                    "title": "Henriquez et al. -Adrex paper - STICS 1-6-2018.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407659/Henriquez%20et%20al.%20-Adrex%20paper%20-%20STICS%201-6-2018.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Henriquez et al. -Adrex paper - STICS 1-6-2018.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407659",
+            "keyword": [
+                "Ozone",
+                "adrenalectomy",
+                "adrenergic receptor agonist",
+                "glucocorticoid receptor agonist",
+                "neuroendocrine stress axes",
+                "broncho dilators",
+                "steroids"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-29",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfy198"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101596,43 +101592,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407659/documents/Henriquez%20et%20al.%20-Adrex%20paper%20-%20STICS%201-6-2018.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfy198"
+            ],
+            "rights": null,
+            "title": "Beta-2 adrenergic and glucocorticoid receptor agonists modulate ozone-induced pulmonary protein leakage and inflammation in healthy and adrenalectomized rats"
         },
         {
-            "title": "In vivo dermal absorption of pyrethroid pesticides in the rat",
-            "description": "Data includes disposition data of radiolabelled pyrethroids (bifenthrin, deltamethrin, cis-permethrin) following topical application.  One dataset is the disposition of pyrethroid-derived radioactivity 24 hr post-application.  The second dataset is the disposition of pyrethroid-derived radioactivity 120 hr post-application. \n\nThis dataset is associated with the following publication:\nHughes , M., and B. Edwards. In vivo dermal absorption of pyrethroid pesticides in the rat..   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH. Taylor & Francis, Inc., Philadelphia, PA, USA, 79(2): 83-91, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1390109",
-            "keyword": [
-                "pyrethroids",
-                "skin",
-                "absorption",
-                "in vivo",
-                "disposition"
-            ],
             "contactPoint": {
                 "fn": "Michael Hughes",
                 "hasEmail": "mailto:hughes.michaelf@epa.gov"
             },
+            "description": "Data includes disposition data of radiolabelled pyrethroids (bifenthrin, deltamethrin, cis-permethrin) following topical application.  One dataset is the disposition of pyrethroid-derived radioactivity 24 hr post-application.  The second dataset is the disposition of pyrethroid-derived radioactivity 120 hr post-application. \n\nThis dataset is associated with the following publication:\nHughes , M., and B. Edwards. In vivo dermal absorption of pyrethroid pesticides in the rat..   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH. Taylor & Francis, Inc., Philadelphia, PA, USA, 79(2): 83-91, (2016).",
             "distribution": [
                 {
-                    "title": "In vivo dermal absorption of pyrethroid pesticides in the rat.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390109/In%20vivo%20dermal%20absorption%20of%20pyrethroid%20pesticides%20in%20the%20rat.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "In vivo dermal absorption of pyrethroid pesticides in the rat.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390109",
+            "keyword": [
+                "pyrethroids",
+                "skin",
+                "absorption",
+                "in vivo",
+                "disposition"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-06",
-            "references": [
-                "https://doi.org/10.1080/15287394.2015.1109571"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101642,19 +101636,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/15287394.2015.1109571"
+            ],
+            "rights": null,
+            "title": "In vivo dermal absorption of pyrethroid pesticides in the rat"
         },
         {
-            "title": "Campy STICS data",
-            "description": "Campy STICS data. \n\nThis dataset is associated with the following publication:\nLye, D., I. Struewing, T. Gruber, K. Oshima, E. Villegas, and J. Lu. A Gallus gallus Model for Determining Infectivity of Zoonotic Campylobacter.   Frontiers in Microbiology. Frontiers, Lausanne,  SWITZERLAND, 10: 2292, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Jingrang Lu",
+                "hasEmail": "mailto:lu.jingrang@epa.gov"
+            },
+            "description": "Campy STICS data. \n\nThis dataset is associated with the following publication:\nLye, D., I. Struewing, T. Gruber, K. Oshima, E. Villegas, and J. Lu. A Gallus gallus Model for Determining Infectivity of Zoonotic Campylobacter.   Frontiers in Microbiology. Frontiers, Lausanne,  SWITZERLAND, 10: 2292, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503643/Campy%20STICS%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Campy STICS data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503643",
             "keyword": [
@@ -101665,20 +101669,10 @@
                 "gull",
                 "avian"
             ],
-            "contactPoint": {
-                "fn": "Jingrang Lu",
-                "hasEmail": "mailto:lu.jingrang@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Campy STICS data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503643/Campy%20STICS%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-06",
-            "references": [
-                "https://doi.org/10.3389/fmicb.2019.02292"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101688,59 +101682,59 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fmicb.2019.02292"
+            ],
+            "rights": null,
+            "title": "Campy STICS data"
         },
         {
-            "title": "Characterizing cleft palate toxicants using ToxCast data, chemical structure, and the biomedical literature",
-            "description": "A data set of 500 chemicals evaluated for their ability to induce cleft palate in animal prenatal developmental studies was compiled from Toxicity Reference Database and the biomedical literature, which included 63 cleft palate active and 437 inactive chemicals. To characterize the potential molecular targets for chemical\u2010induced cleft palate, we mined the ToxCast high\u2010throughput screening database for patterns and linkages in bioactivity profiles and chemical structural descriptors. The following datasets can be obtained via the links and files in the Data section: Phase II ToxCast assay data results (Judson et al., 2010); The Gene Score data set derived from ToxCast; ToxRefDB version 1 (Knudsen et al., 2009; Martin, Judson, et al., 2009); The ToxPrint chemotypes (Yang et al., 2015). \n\nThis dataset is associated with the following publication:\nBaker, N., N. Sipes, J. Franzosa, D. Belair, B. Abbott, R. Judson, and T. Knudsen. Characterizing cleft palate toxicants using ToxCast data, chemical structure, and the biomedical literature.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA,  1-21, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504179",
-            "keyword": [
-                "adverse outcome pathway",
-                "cleft palate",
-                "Developmental Toxicity",
-                "genes",
-                "machine learning",
-                "ToxCast",
-                "vEmbryo",
-                "virtual embryo",
-                "virtual tissues",
-                "tipping points"
-            ],
             "contactPoint": {
                 "fn": "Thomas Knudsen",
                 "hasEmail": "mailto:knudsen.thomas@epa.gov"
             },
+            "description": "A data set of 500 chemicals evaluated for their ability to induce cleft palate in animal prenatal developmental studies was compiled from Toxicity Reference Database and the biomedical literature, which included 63 cleft palate active and 437 inactive chemicals. To characterize the potential molecular targets for chemical\u2010induced cleft palate, we mined the ToxCast high\u2010throughput screening database for patterns and linkages in bioactivity profiles and chemical structural descriptors. The following datasets can be obtained via the links and files in the Data section: Phase II ToxCast assay data results (Judson et al., 2010); The Gene Score data set derived from ToxCast; ToxRefDB version 1 (Knudsen et al., 2009; Martin, Judson, et al., 2009); The ToxPrint chemotypes (Yang et al., 2015). \n\nThis dataset is associated with the following publication:\nBaker, N., N. Sipes, J. Franzosa, D. Belair, B. Abbott, R. Judson, and T. Knudsen. Characterizing cleft palate toxicants using ToxCast data, chemical structure, and the biomedical literature.   Birth Defects Research. John Wiley & Sons, Inc., Hoboken, NJ, USA,  1-21, (2019).",
             "distribution": [
                 {
-                    "title": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data",
-                    "accessURL": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data"
+                    "accessURL": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data",
+                    "title": "https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data"
                 },
                 {
-                    "title": "https://gaftp.epa.gov/comptox/High_Throughput_Screening_Data/Animal_Tox_Data/",
-                    "accessURL": "https://gaftp.epa.gov/comptox/High_Throughput_Screening_Data/Animal_Tox_Data/"
+                    "accessURL": "https://gaftp.epa.gov/comptox/High_Throughput_Screening_Data/Animal_Tox_Data/",
+                    "title": "https://gaftp.epa.gov/comptox/High_Throughput_Screening_Data/Animal_Tox_Data/"
                 },
                 {
-                    "title": "https://toxprint.org",
-                    "accessURL": "https://toxprint.org"
+                    "accessURL": "https://toxprint.org",
+                    "title": "https://toxprint.org"
                 },
                 {
-                    "title": "bdr21581-sup-0001-appendixs1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504179/bdr21581-sup-0001-appendixs1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "bdr21581-sup-0001-appendixs1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504179",
+            "keyword": [
+                "adverse outcome pathway",
+                "cleft palate",
+                "Developmental Toxicity",
+                "genes",
+                "machine learning",
+                "ToxCast",
+                "vEmbryo",
+                "virtual embryo",
+                "virtual tissues",
+                "tipping points"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-07",
-            "references": [
-                "https://doi.org/10.1002/bdr2.1581"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101750,19 +101744,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/bdr2.1581"
+            ],
+            "rights": null,
+            "title": "Characterizing cleft palate toxicants using ToxCast data, chemical structure, and the biomedical literature"
         },
         {
-            "title": "Limited chemical structural diversity found to modulate thyroid hormone receptor in the Tox21 chemical library",
-            "description": "The Tox21 chemical library (8,305 unique structures) was screened in a quantitative high-throughput, cell-based reporter gene assay for TR agonist or antagonist activity. Active compounds were further characterized using additional orthogonal assays, including mammalian one-hybrid assays, coactivator recruitment assays, and a high-throughput, fluorescent imaging, nuclear receptor translocation assay.  Results for the library are available at https://tripod.nih.gov/tox21/samples. \n\nThis dataset is associated with the following publication:\nPaul-Friedman, K., M. Martin, K. Crofton, C. Hsu, S. Sakamuru, J. Zhao, M. Xia, R. Huang, D. Stevreva, V. Soni, L. Varticovski, R. Raziuddin, G. Hager, and K. Houck. Limited chemical structural diversity found to modulate thyroid hormone receptor in the Tox21 chemical library.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 127(9): 1-16, (2019).",
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
+            "description": "The Tox21 chemical library (8,305 unique structures) was screened in a quantitative high-throughput, cell-based reporter gene assay for TR agonist or antagonist activity. Active compounds were further characterized using additional orthogonal assays, including mammalian one-hybrid assays, coactivator recruitment assays, and a high-throughput, fluorescent imaging, nuclear receptor translocation assay.  Results for the library are available at https://tripod.nih.gov/tox21/samples. \n\nThis dataset is associated with the following publication:\nPaul-Friedman, K., M. Martin, K. Crofton, C. Hsu, S. Sakamuru, J. Zhao, M. Xia, R. Huang, D. Stevreva, V. Soni, L. Varticovski, R. Raziuddin, G. Hager, and K. Houck. Limited chemical structural diversity found to modulate thyroid hormone receptor in the Tox21 chemical library.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 127(9): 1-16, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503082/SupplementalTables_clearance.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SupplementalTables_clearance.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503082",
             "keyword": [
@@ -101773,20 +101777,10 @@
                 "High throughput screening",
                 "high throughput toxicology"
             ],
-            "contactPoint": {
-                "fn": "Keith Houck",
-                "hasEmail": "mailto:houck.keith@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SupplementalTables_clearance.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503082/SupplementalTables_clearance.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-05",
-            "references": [
-                "https://doi.org/10.1289/ehp5314"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101796,19 +101790,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp5314"
+            ],
+            "rights": null,
+            "title": "Limited chemical structural diversity found to modulate thyroid hormone receptor in the Tox21 chemical library"
         },
         {
-            "title": "Data_averages_6-24-15_ESS_PEM_PFO_3_good_months",
-            "description": "Summary of all field data collected for wetlands denitrification project in Tampa Bay Watershed including denitrification enzyme activity potential rates, soil and pore water characteristics, and land use/cover percentages in upstream drainage basins.  DEA are averages for 3 different months where we had valid DEA incubations while soil and water are from single date. \n\nThis dataset is associated with the following publication:\nRussell, M., R. Fulford, K. Murphy, C. Lane, J. Harvey, D. Dantin, F. Alvarez, J. Nestlerode, A. Teague, M. Harwell, and A. Almario. Relative importance of landscape versus local wetland characteristics for estimating wetland denitrification potential.   WETLANDS. The Society of Wetland Scientists, McLean, VA, USA, 39(1): 127-137, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Marc Russell",
+                "hasEmail": "mailto:russell.marc@epa.gov"
+            },
+            "description": "Summary of all field data collected for wetlands denitrification project in Tampa Bay Watershed including denitrification enzyme activity potential rates, soil and pore water characteristics, and land use/cover percentages in upstream drainage basins.  DEA are averages for 3 different months where we had valid DEA incubations while soil and water are from single date. \n\nThis dataset is associated with the following publication:\nRussell, M., R. Fulford, K. Murphy, C. Lane, J. Harvey, D. Dantin, F. Alvarez, J. Nestlerode, A. Teague, M. Harwell, and A. Almario. Relative importance of landscape versus local wetland characteristics for estimating wetland denitrification potential.   WETLANDS. The Society of Wetland Scientists, McLean, VA, USA, 39(1): 127-137, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407609/Data_averages_6-24-15_ESS_PEM_PFO_3_good_months.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data_averages_6-24-15_ESS_PEM_PFO_3_good_months.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407609",
             "keyword": [
@@ -101821,20 +101825,10 @@
                 "Coastal Wetlands",
                 "land use"
             ],
-            "contactPoint": {
-                "fn": "Marc Russell",
-                "hasEmail": "mailto:russell.marc@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data_averages_6-24-15_ESS_PEM_PFO_3_good_months.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407609/Data_averages_6-24-15_ESS_PEM_PFO_3_good_months.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-06-26",
-            "references": [
-                "https://doi.org/10.1007/s13157-018-1078-6"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -101844,47 +101838,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s13157-018-1078-6"
+            ],
+            "rights": null,
+            "title": "Data_averages_6-24-15_ESS_PEM_PFO_3_good_months"
         },
         {
-            "title": "National Inventory of Phosphorus (v1, 8.30.19)",
-            "description": "This is a project assessing the state of major input and outputs of reactive nitrogen (Nr) and phosphorus across the coterminous US at the HUC 8 scale for three snapshots of time (2002, 2007, and 2012). ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1504278",
-            "keyword": [
-                "phosphorus",
-                "fertilizer P",
-                "stream water quality",
-                "Agriculture",
-                "nonpoint source pollution",
-                "Point source"
-            ],
             "contactPoint": {
                 "fn": "Robert Sabo",
                 "hasEmail": "mailto:sabo.robert@epa.gov"
             },
+            "description": "This is a project assessing the state of major input and outputs of reactive nitrogen (Nr) and phosphorus across the coterminous US at the HUC 8 scale for three snapshots of time (2002, 2007, and 2012). ",
             "distribution": [
                 {
-                    "title": "Master_Inventory_Final.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504278/Master_Inventory_Final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Master_Inventory_Final.xlsx"
                 },
                 {
-                    "title": "Master_Inventory_Final_v2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504278/Master_Inventory_Final_v2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Master_Inventory_Final_v2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504278",
+            "keyword": [
+                "phosphorus",
+                "fertilizer P",
+                "stream water quality",
+                "Agriculture",
+                "nonpoint source pollution",
+                "Point source"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-30",
-            "references": null,
+            "programCode": [
+                "020:097"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -101893,20 +101889,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "National Inventory of Phosphorus (v1, 8.30.19)"
         },
         {
-            "title": "North Carolina Blood Lead and Education Data",
-            "description": "The Children's Environmental Health Initiative (CEHI) at Rice University provided access to blood lead data from the North Carolina Childhood Lead Poisoning Prevention Program surveillance registry; data on end-of-grade standardized achievement tests in reading and mathematics from the North Carolina Education Research Data Center (NCERDC); and birth certificate data from the North Carolina Department of Health and Human Services. Test score, blood lead, and birth certificate data were linked using a common child identifier created by CEHI for matching purposes. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: The data was made available by the Children's Environmental Health Initiative (CEHI) at Rice University. Contact Claire Osgood (ceo1@rice.edu), CEHI's Data Manager, to learn how the data can be accessed. Format: The Children's Environmental Health Initiative (CEHI) at Rice University provided access to blood lead data from the North Carolina Childhood Lead Poisoning Prevention Program surveillance registry; data on end-of-grade standardized achievement tests in reading and mathematics from the North Carolina Education Research Data Center (NCERDC); and birth certificate data from the North Carolina Department of Health and Human Services. Test score, blood lead, and birth certificate data were linked using a common child identifier created by CEHI for matching purposes. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
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
+                "fn": "Heather Klemick",
+                "hasEmail": "mailto:klemick.heather@epa.gov"
+            },
+            "description": "The Children's Environmental Health Initiative (CEHI) at Rice University provided access to blood lead data from the North Carolina Childhood Lead Poisoning Prevention Program surveillance registry; data on end-of-grade standardized achievement tests in reading and mathematics from the North Carolina Education Research Data Center (NCERDC); and birth certificate data from the North Carolina Department of Health and Human Services. Test score, blood lead, and birth certificate data were linked using a common child identifier created by CEHI for matching purposes. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: The data was made available by the Children's Environmental Health Initiative (CEHI) at Rice University. Contact Claire Osgood (ceo1@rice.edu), CEHI's Data Manager, to learn how the data can be accessed. Format: The Children's Environmental Health Initiative (CEHI) at Rice University provided access to blood lead data from the North Carolina Childhood Lead Poisoning Prevention Program surveillance registry; data on end-of-grade standardized achievement tests in reading and mathematics from the North Carolina Education Research Data Center (NCERDC); and birth certificate data from the North Carolina Department of Health and Human Services. Test score, blood lead, and birth certificate data were linked using a common child identifier created by CEHI for matching purposes. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1506023",
             "keyword": [
                 "blood lead",
@@ -101914,89 +101912,87 @@
                 "education",
                 "cognitive development"
             ],
-            "contactPoint": {
-                "fn": "Heather Klemick",
-                "hasEmail": "mailto:klemick.heather@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-11",
-            "references": [
-                "https://dx.doi.org/10.1016/j.envres.2019.108643"
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
+                "https://dx.doi.org/10.1016/j.envres.2019.108643"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "North Carolina Blood Lead and Education Data"
         },
         {
-            "title": "Data for Adaptation, Sea Level Rise, and Property Prices in the Chesapeake Bay Watershed",
-            "description": "Property characteristics and parcel boundaries, shoreline features, and sea level rise inundation vulnerability for the state of Maryland. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: Data on property attributes and parcel boundaries from MdProperty View can be accessed at https://planning.maryland.gov/Pages/OurProducts/PropertyMapProducts/MDPropertyViewProducts.aspx \n\nData on shoreline features for Anne Arundel County can be accessed at http://ccrm.vims.edu/gis_data_maps/shoreline_inventories/maryland/anne_arundel/annearundel_disclaimer.html\n\nData on sea level rise inundation vulnerability for Maryland coastal counties can be accessed at https://imap.maryland.gov/ServicesMetadata/ClimMetAtm/SeaLevelRiseVul/ELEV_2FootInundation_CGIS.htm. Format: Property sales and attribute data were obtained from MdProperty View and include numeric data as well as georeferenced parcel data.\n\nGeoreferenced data on shoreline features, including adaptation structures, come from a joint program between the Virginia Institute of Marine Science, the Maryland Department of Natural Resources, and the National Oceanic and Atmospheric Agency (NOAA).\n\nGeoreferenced sea level rise inundation vulnerability data were produced in a joint project between NOAA, the Maryland Commission on Climate Change, and Towson University. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Heather Klemick",
+                "hasEmail": "mailto:klemick.heather@epa.gov"
+            },
+            "description": "Property characteristics and parcel boundaries, shoreline features, and sea level rise inundation vulnerability for the state of Maryland. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: Data on property attributes and parcel boundaries from MdProperty View can be accessed at https://planning.maryland.gov/Pages/OurProducts/PropertyMapProducts/MDPropertyViewProducts.aspx \n\nData on shoreline features for Anne Arundel County can be accessed at http://ccrm.vims.edu/gis_data_maps/shoreline_inventories/maryland/anne_arundel/annearundel_disclaimer.html\n\nData on sea level rise inundation vulnerability for Maryland coastal counties can be accessed at https://imap.maryland.gov/ServicesMetadata/ClimMetAtm/SeaLevelRiseVul/ELEV_2FootInundation_CGIS.htm. Format: Property sales and attribute data were obtained from MdProperty View and include numeric data as well as georeferenced parcel data.\n\nGeoreferenced data on shoreline features, including adaptation structures, come from a joint program between the Virginia Institute of Marine Science, the Maryland Department of Natural Resources, and the National Oceanic and Atmospheric Agency (NOAA).\n\nGeoreferenced sea level rise inundation vulnerability data were produced in a joint project between NOAA, the Maryland Commission on Climate Change, and Towson University. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1506083",
             "keyword": [
                 "sea level rise",
                 "climate adaptation",
                 "hedonic analysis"
             ],
-            "contactPoint": {
-                "fn": "Heather Klemick",
-                "hasEmail": "mailto:klemick.heather@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-03",
-            "references": [
-                "https://dx.doi.org/10.3368/le.95.1.19"
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
+                "https://dx.doi.org/10.3368/le.95.1.19"
+            ],
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "title": "Data for Adaptation, Sea Level Rise, and Property Prices in the Chesapeake Bay Watershed"
         },
         {
-            "title": "Analysis of proportional data in reproductive and developmental toxicity studies: comparison of logit transformation, arcsine square root transformation, and nonparametric analysis",
-            "description": "We conducted power calculations to compare different approaches (nonparametric, arcsine square root-transformed, logit-transformed, untransformed) for analyzing litter-based proportional data.  A reproductive toxicity study with a control and one treated group provided data for two endpoints: prenatal loss, and fertility by in utero insemination (IUI).  Type I error and power were estimated by 10,000 simulations based on two-sample one-tailed t-tests with varying numbers of litters per group.  To further compare the different approaches, we conducted additional analyses with the mean proportions shifted toward zero  to produce illustrative scenarios.  Analyses based on logit-transformed proportions had greater power than those based on untransformed or arcsine square root-transformed proportions, or nonparametric procedures.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503388",
-            "keyword": [
-                "statistical power",
-                "proportional data",
-                "logit transformation",
-                "arcsine square root transformation",
-                "Developmental Toxicity"
-            ],
             "contactPoint": {
                 "fn": "Michael Narotsky",
                 "hasEmail": "mailto:narotsky.michael@epa.gov"
             },
+            "description": "We conducted power calculations to compare different approaches (nonparametric, arcsine square root-transformed, logit-transformed, untransformed) for analyzing litter-based proportional data.  A reproductive toxicity study with a control and one treated group provided data for two endpoints: prenatal loss, and fertility by in utero insemination (IUI).  Type I error and power were estimated by 10,000 simulations based on two-sample one-tailed t-tests with varying numbers of litters per group.  To further compare the different approaches, we conducted additional analyses with the mean proportions shifted toward zero  to produce illustrative scenarios.  Analyses based on logit-transformed proportions had greater power than those based on untransformed or arcsine square root-transformed proportions, or nonparametric procedures.",
             "distribution": [
                 {
-                    "title": "PowerManuscriptTableFigureData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503388/PowerManuscriptTableFigureData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PowerManuscriptTableFigureData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503388",
+            "keyword": [
+                "statistical power",
+                "proportional data",
+                "logit transformation",
+                "arcsine square root transformation",
+                "Developmental Toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-15",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -102005,50 +102001,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Analysis of proportional data in reproductive and developmental toxicity studies: comparison of logit transformation, arcsine square root transformation, and nonparametric analysis"
         },
         {
-            "title": "4-Acetoxyphenol as a substrate for acetylcholinesterase-based sensor and its application for As(III) determination",
-            "description": "The supplementary data is used to support the interpretation of electrochemical reaction at the interface of working electrode, and reaction features of the immobilized enzyme. The formula for modeling the kinetics of immobilized enzyme was also given in the supplementary material. \n\nThis dataset is associated with the following publication:\nLi, T., E. Sahle-Demessie, E. Varughese, and J. Berberich. A disposable acetylcholine esterase sensor for As(iii) determination in groundwater matrix based on 4-acetoxyphenol hydrolysis.   Analytical Methods. RSC Publishing, Cambridge,  UK, 11(40): 5203-5213, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1435424",
-            "keyword": [
-                "cyclic voltametry",
-                "Voltammogram of hydroquinone",
-                "reversible first order reaction kinetics",
-                "Enzyme activity",
-                "biosensor",
-                "real time analysis",
-                "contaminant",
-                "amperometric assay"
-            ],
             "contactPoint": {
                 "fn": "Tao Li",
                 "hasEmail": "mailto:li.tao@epa.gov"
             },
+            "description": "The supplementary data is used to support the interpretation of electrochemical reaction at the interface of working electrode, and reaction features of the immobilized enzyme. The formula for modeling the kinetics of immobilized enzyme was also given in the supplementary material. \n\nThis dataset is associated with the following publication:\nLi, T., E. Sahle-Demessie, E. Varughese, and J. Berberich. A disposable acetylcholine esterase sensor for As(iii) determination in groundwater matrix based on 4-acetoxyphenol hydrolysis.   Analytical Methods. RSC Publishing, Cambridge,  UK, 11(40): 5203-5213, (2019).",
             "distribution": [
                 {
-                    "title": "Draft for AchE sensor.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435424/Draft%20for%20AchE%20sensor.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Draft for AchE sensor.docx"
                 },
                 {
-                    "title": "Supplementary material.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435424/Supplementary%20material.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary material.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435424",
+            "keyword": [
+                "cyclic voltametry",
+                "Voltammogram of hydroquinone",
+                "reversible first order reaction kinetics",
+                "Enzyme activity",
+                "biosensor",
+                "real time analysis",
+                "contaminant",
+                "amperometric assay"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-02",
-            "references": [
-                "https://doi.org/10.1039/c9ay01199d"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102058,19 +102052,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c9ay01199d"
+            ],
+            "rights": null,
+            "title": "4-Acetoxyphenol as a substrate for acetylcholinesterase-based sensor and its application for As(III) determination"
         },
         {
-            "title": "Part III. Scale-up Testing and Assessment of Selected Potential Operational Issues",
-            "description": "This study evaluated reuse of lime softening sludge, generated from drinking water treatment utilities, as an environmental sorbent for capturing SO2 and heavy metals in wet scrubbers of coal-fired power plants. Specifically, Part III evaluated viscosity and metal corrosion as practical issues in the transition from limestone to lime sludge at power plants. Results of Marsh funnel viscosity experiments conducted at different solids contents and temperatures indicated the limestone and lime sludge slurries and their gypsum counterparts had similar flow characteristics. Carbon-steel, stainless-steel, and Hastelloy coupons were tested for corrosion by lime sludge and limestone slurries. Both stainless steel and Hastelloy were resistive to corrosion in slurries made from lime sludge or limestone samples or their gypsum counterparts. A considerable but similar amount of corrosion was observed for carbon-steel coupons exposed to lime sludge and limestone slurries. Adding 5000 ppm of Cl to slurries considerably increased the corrosion rate of carbon steel. \n\nThis dataset is associated with the following publication:\nDastgheib, S., J. Mock, H. Salih, and C. Patterson. Utilization of Water Utility Lime Sludge for Flue Gas Desulfurization in Coal-Fired Power Plants: \nPart III. Testing at a Higher Scale and Assessment of Selected Potential Operational Issues.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA, 33(11): 11536-11543, (2019).",
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
+            "description": "This study evaluated reuse of lime softening sludge, generated from drinking water treatment utilities, as an environmental sorbent for capturing SO2 and heavy metals in wet scrubbers of coal-fired power plants. Specifically, Part III evaluated viscosity and metal corrosion as practical issues in the transition from limestone to lime sludge at power plants. Results of Marsh funnel viscosity experiments conducted at different solids contents and temperatures indicated the limestone and lime sludge slurries and their gypsum counterparts had similar flow characteristics. Carbon-steel, stainless-steel, and Hastelloy coupons were tested for corrosion by lime sludge and limestone slurries. Both stainless steel and Hastelloy were resistive to corrosion in slurries made from lime sludge or limestone samples or their gypsum counterparts. A considerable but similar amount of corrosion was observed for carbon-steel coupons exposed to lime sludge and limestone slurries. Adding 5000 ppm of Cl to slurries considerably increased the corrosion rate of carbon steel. \n\nThis dataset is associated with the following publication:\nDastgheib, S., J. Mock, H. Salih, and C. Patterson. Utilization of Water Utility Lime Sludge for Flue Gas Desulfurization in Coal-Fired Power Plants: \nPart III. Testing at a Higher Scale and Assessment of Selected Potential Operational Issues.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA, 33(11): 11536-11543, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504281/Data%20of%20Tables%20and%20Figures.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data of Tables and Figures.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504281",
             "keyword": [
@@ -102083,20 +102087,10 @@
                 "environmental impact assessment",
                 "mercury re-emission"
             ],
-            "contactPoint": {
-                "fn": "Craig Patterson",
-                "hasEmail": "mailto:patterson.craig@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data of Tables and Figures.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504281/Data%20of%20Tables%20and%20Figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-11",
-            "references": [
-                "https://doi.org/10.1021/acs.energyfuels.9b03132"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102106,121 +102100,130 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.energyfuels.9b03132"
+            ],
+            "rights": null,
+            "title": "Part III. Scale-up Testing and Assessment of Selected Potential Operational Issues"
         },
         {
-            "title": "2017 NAIS Work Order 7060851",
-            "description": "This data is in the form of a CSV file provided by the U.S. Coast Guard from their NAIS dataset.\nthe request period was: 01/01/2017-06/30/2017\nthe upper right bound of the data set is: 38.242\u00b0N,  \u2212116.796\u00b0W\nthe lower left bound of the data set is 32.6703\u00b0N, \u2212128.296\u00b0W\nThe data was delivered in 5 minute intervals\nThe fields contained in the data set are:\nMSG_TYPE,MMSI,NAME,PERIOD,LAT_AVG,LON_AVG,COG_DEG,SPEED_KNOTS,HEADING_DEG,IMO_NUMBER,CALL_SIGN,SHIP_AND_CARGO_TYPE,NAV_SENSOR,DRAUGHT,MMSI_COUNTRY_CD,DIM_BOW,DIM_STERN,DIM_STARBOARD,DIM_PORT,RECEIVER. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: Directions for requesting this data from the U.S. Coast Guard can be found at:\nhttps://www.navcen.uscg.gov/?pageName=AISdisclaimer. Format: This data is in the form of a CSV file provided by the U.S. Coast Guard from their NAIS dataset.\nthe request period was: 01/01/2017-06/30/2017\nthe upper right bound of the data set is: 38.242\u00b0N,  \u2212116.796\u00b0W\nthe lower left bound of the data set is 32.6703\u00b0N, \u2212128.296\u00b0W\nThe data was delivered in 5 minute intervals\nThe fields contained in the data set are:\nMSG_TYPE,MMSI,NAME,PERIOD,LAT_AVG,LON_AVG,COG_DEG,SPEED_KNOTS,HEADING_DEG,IMO_NUMBER,CALL_SIGN,SHIP_AND_CARGO_TYPE,NAV_SENSOR,DRAUGHT,MMSI_COUNTRY_CD,DIM_BOW,DIM_STERN,DIM_STARBOARD,DIM_PORT,RECEIVER. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504191",
-            "keyword": [
-                "AIS"
-            ],
             "contactPoint": {
                 "fn": "Michael Aldridge",
                 "hasEmail": "mailto:aldridge.michael@epa.gov"
             },
+            "description": "This data is in the form of a CSV file provided by the U.S. Coast Guard from their NAIS dataset.\nthe request period was: 01/01/2017-06/30/2017\nthe upper right bound of the data set is: 38.242\u00b0N,  \u2212116.796\u00b0W\nthe lower left bound of the data set is 32.6703\u00b0N, \u2212128.296\u00b0W\nThe data was delivered in 5 minute intervals\nThe fields contained in the data set are:\nMSG_TYPE,MMSI,NAME,PERIOD,LAT_AVG,LON_AVG,COG_DEG,SPEED_KNOTS,HEADING_DEG,IMO_NUMBER,CALL_SIGN,SHIP_AND_CARGO_TYPE,NAV_SENSOR,DRAUGHT,MMSI_COUNTRY_CD,DIM_BOW,DIM_STERN,DIM_STARBOARD,DIM_PORT,RECEIVER. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: Directions for requesting this data from the U.S. Coast Guard can be found at:\nhttps://www.navcen.uscg.gov/?pageName=AISdisclaimer. Format: This data is in the form of a CSV file provided by the U.S. Coast Guard from their NAIS dataset.\nthe request period was: 01/01/2017-06/30/2017\nthe upper right bound of the data set is: 38.242\u00b0N,  \u2212116.796\u00b0W\nthe lower left bound of the data set is 32.6703\u00b0N, \u2212128.296\u00b0W\nThe data was delivered in 5 minute intervals\nThe fields contained in the data set are:\nMSG_TYPE,MMSI,NAME,PERIOD,LAT_AVG,LON_AVG,COG_DEG,SPEED_KNOTS,HEADING_DEG,IMO_NUMBER,CALL_SIGN,SHIP_AND_CARGO_TYPE,NAV_SENSOR,DRAUGHT,MMSI_COUNTRY_CD,DIM_BOW,DIM_STERN,DIM_STARBOARD,DIM_PORT,RECEIVER. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1504191",
+            "keyword": [
+                "AIS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-25",
-            "references": [
-                "https://dx.doi.org/10.1080/10962247.2019.1580229"
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
+                "https://dx.doi.org/10.1080/10962247.2019.1580229"
+            ],
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "title": "2017 NAIS Work Order 7060851"
         },
         {
-            "title": "IHS Sea-web Ship Details and Technical Specifications",
-            "description": "This data is a CSV file containeing ship technical details from IHS Sea-web. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: The vessel details in this dataset can be accessed via a subscription to IHS Sea-web:\nhttps://maritime.ihs.com/EntitlementPortal/Home/Index. Format: This data set was compiled as a CSV file. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504192",
-            "keyword": [
-                "Commercial Marine Vessels"
-            ],
             "contactPoint": {
                 "fn": "Michael Aldridge",
                 "hasEmail": "mailto:aldridge.michael@epa.gov"
             },
+            "description": "This data is a CSV file containeing ship technical details from IHS Sea-web. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: The vessel details in this dataset can be accessed via a subscription to IHS Sea-web:\nhttps://maritime.ihs.com/EntitlementPortal/Home/Index. Format: This data set was compiled as a CSV file. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1504192",
+            "keyword": [
+                "Commercial Marine Vessels"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-05-29",
-            "references": [
-                "https://dx.doi.org/10.1080/10962247.2019.1580229"
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
+                "https://dx.doi.org/10.1080/10962247.2019.1580229"
+            ],
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "title": "IHS Sea-web Ship Details and Technical Specifications"
         },
         {
-            "title": "Ship Power Model Summary Data",
-            "description": "The dataset is contained in a .zip file containing the two .csv files with data, and a data dictionary file. \nsummedEmissionsSpeeds contains emissions estimates summed over several different modeling parameters, DwtSubtypes gives the mapping of shipType, and subtypes, to deadweight tonnage ranges as used in the linked publication. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1504194",
-            "keyword": [
-                "Marine Emissions"
-            ],
             "contactPoint": {
                 "fn": "Michael Aldridge",
                 "hasEmail": "mailto:aldridge.michael@epa.gov"
             },
+            "description": "The dataset is contained in a .zip file containing the two .csv files with data, and a data dictionary file. \nsummedEmissionsSpeeds contains emissions estimates summed over several different modeling parameters, DwtSubtypes gives the mapping of shipType, and subtypes, to deadweight tonnage ranges as used in the linked publication. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "MarineEmissionsSummaries.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504194/MarineEmissionsSummaries.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "MarineEmissionsSummaries.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504194",
+            "keyword": [
+                "Marine Emissions"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-01",
-            "references": [
-                "https://dx.doi.org/10.1080/10962247.2019.1580229"
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
+                "https://dx.doi.org/10.1080/10962247.2019.1580229"
+            ],
+            "rights": null,
+            "title": "Ship Power Model Summary Data"
         },
         {
-            "title": "HTTK: R Package for High-Throughput Toxicokinetics",
-            "description": "Functions and data tables for simulation and statistical analysis of chemical toxicokinetics (\"TK\") as in Pearce et al. (2017) <doi:10.18637/jss.v079.i04>. Chemical-specific in vitro data have been obtained from relatively high throughput experiments. Both physiologically-based (\"PBTK\") and empirical (e.g., one compartment) \"TK\" models can be parameterized for several hundred chemicals and multiple species. These models are solved efficiently, often using compiled (C-based) code. \n\nThis dataset is associated with the following publication:\nPearce , R., C. Strope , W. Setzer , N. Sipes , and J. Wambaugh. (Journal of Statistical Software) HTTK: R Package for High-Throughput Toxicokinetics.   Journal of Statistical Software. American Statistical Association, Alexandria, VA, USA, 79(4): 1-26, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "Functions and data tables for simulation and statistical analysis of chemical toxicokinetics (\"TK\") as in Pearce et al. (2017) <doi:10.18637/jss.v079.i04>. Chemical-specific in vitro data have been obtained from relatively high throughput experiments. Both physiologically-based (\"PBTK\") and empirical (e.g., one compartment) \"TK\" models can be parameterized for several hundred chemicals and multiple species. These models are solved efficiently, often using compiled (C-based) code. \n\nThis dataset is associated with the following publication:\nPearce , R., C. Strope , W. Setzer , N. Sipes , and J. Wambaugh. (Journal of Statistical Software) HTTK: R Package for High-Throughput Toxicokinetics.   Journal of Statistical Software. American Statistical Association, Alexandria, VA, USA, 79(4): 1-26, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://cran.r-project.org/web/packages/httk/index.html",
+                    "title": "https://cran.r-project.org/web/packages/httk/index.html"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504255",
             "keyword": [
@@ -102231,19 +102234,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://cran.r-project.org/web/packages/httk/index.html",
-                    "accessURL": "https://cran.r-project.org/web/packages/httk/index.html"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-17",
-            "references": [
-                "https://doi.org/10.18637/jss.v079.i04"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102253,88 +102247,88 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.18637/jss.v079.i04"
+            ],
+            "rights": null,
+            "title": "HTTK: R Package for High-Throughput Toxicokinetics"
         },
         {
-            "title": "Method 200.8: Plus 2 paper",
-            "description": "Method 200.8: Plus 2 paper. \n\nThis dataset is associated with the following publication:\nSmith, S., N. Hanks, P. Creed, K. Kovalcik, R. Wilson, K. Kubachka, J. Brisbin, J. Landero Figueroa, and J. Creed. Analytical considerations associated with implementing M2+ correction factors to address false positives on As and Se within U.S. EPA method 200.8.   JOURNAL OF ANALYTICAL ATOMIC SPECTROMETRY. Royal Society of Chemistry, Cambridge,  UK, 34(10): 2094-2104, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503162",
-            "keyword": [
-                "Method 200.8",
-                "Rare Earth Elements",
-                "ICP-MS",
-                "False Positives",
-                "M+2",
-                "Polyatomic"
-            ],
             "contactPoint": {
                 "fn": "John Creed",
                 "hasEmail": "mailto:creed.jack@epa.gov"
             },
+            "description": "Method 200.8: Plus 2 paper. \n\nThis dataset is associated with the following publication:\nSmith, S., N. Hanks, P. Creed, K. Kovalcik, R. Wilson, K. Kubachka, J. Brisbin, J. Landero Figueroa, and J. Creed. Analytical considerations associated with implementing M2+ correction factors to address false positives on As and Se within U.S. EPA method 200.8.   JOURNAL OF ANALYTICAL ATOMIC SPECTROMETRY. Royal Society of Chemistry, Cambridge,  UK, 34(10): 2094-2104, (2019).",
             "distribution": [
                 {
-                    "title": "Correction Factors applied to standard solutions  Fig 5 Table 1&2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/Correction%20Factors%20applied%20to%20standard%20solutions%20%20Fig%205%20Table%201%262.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Correction Factors applied to standard solutions  Fig 5 Table 1&2.xlsx"
                 },
                 {
-                    "title": "150-143 ratio and changing factor Fig 6.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/150-143%20ratio%20and%20changing%20factor%20Fig%206.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "150-143 ratio and changing factor Fig 6.xlsx"
                 },
                 {
-                    "title": "3-7-2018 Correction factors applied to standard table  Fig 5 Table 1&2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/3-7-2018%20Correction%20factors%20applied%20to%20standard%20table%20%20Fig%205%20Table%201%262.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "3-7-2018 Correction factors applied to standard table  Fig 5 Table 1&2.xlsx"
                 },
                 {
-                    "title": "Fig 3B & S1 Effect of Tune.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/Fig%203B%20%26%20S1%20Effect%20of%20Tune.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 3B & S1 Effect of Tune.xlsx"
                 },
                 {
-                    "title": "2-8-17 Correlating narrow & Std mode_Gd&Sm & Nd Ba Ho Fig 5 Table 1&2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/2-8-17%20Correlating%20narrow%20%26%20Std%20mode_Gd%26Sm%20%26%20Nd%20Ba%20Ho%20Fig%205%20Table%201%262.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2-8-17 Correlating narrow & Std mode_Gd&Sm & Nd Ba Ho Fig 5 Table 1&2.xlsx"
                 },
                 {
-                    "title": "Fig 2 - Illustration of problem.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/Fig%202%20-%20Illustration%20of%20problem.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 2 - Illustration of problem.xlsx"
                 },
                 {
-                    "title": "Fig 4 - Unit vs half mass and narrow vs standard resolution.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/Fig%204%20-%20Unit%20vs%20half%20mass%20and%20narrow%20vs%20standard%20resolution.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 4 - Unit vs half mass and narrow vs standard resolution.xlsx"
                 },
                 {
-                    "title": "Fig S2A Estimating M2  Correction Factor.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/Fig%20S2A%20Estimating%20M2%20%20Correction%20Factor.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig S2A Estimating M2  Correction Factor.xlsx"
                 },
                 {
-                    "title": "Fig S2B - 7-19-16 abundance sensitivity data 2.5 mL He.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/Fig%20S2B%20-%207-19-16%20abundance%20sensitivity%20data%202.5%20mL%20He.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig S2B - 7-19-16 abundance sensitivity data 2.5 mL He.xlsx"
                 },
                 {
-                    "title": "Regional Waters Half Mass Correction for Table 1 & 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503162/Regional%20Waters%20Half%20Mass%20Correction%20for%20Table%201%20%26%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Regional Waters Half Mass Correction for Table 1 & 2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503162",
+            "keyword": [
+                "Method 200.8",
+                "Rare Earth Elements",
+                "ICP-MS",
+                "False Positives",
+                "M+2",
+                "Polyatomic"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-07",
-            "references": [
-                "https://doi.org/10.1039/c9ja00086k"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102344,20 +102338,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c9ja00086k"
+            ],
+            "rights": null,
+            "title": "Method 200.8: Plus 2 paper"
         },
         {
-            "title": "Fruit and Vegetable Data",
-            "description": "Pyrethroid metabolite concentration data for fruits and vegetables. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact PI. Format: List of pyrethroids and pyrethroid degradation. \n\nThis dataset is associated with the following publication:\nLi, W., M. Morgan, S. Graham, and J. Starr. Measurement of pyrethroids and their environmental degradation products in fresh fruits and vegetables using a modification of the quick easy cheap effective rugged safe (QuEChERS) method.   TALANTA. Elsevier Science Ltd, New York, NY, USA, 151: 42-50, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "James Starr",
+                "hasEmail": "mailto:starr.james@epa.gov"
+            },
+            "description": "Pyrethroid metabolite concentration data for fruits and vegetables. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact PI. Format: List of pyrethroids and pyrethroid degradation. \n\nThis dataset is associated with the following publication:\nLi, W., M. Morgan, S. Graham, and J. Starr. Measurement of pyrethroids and their environmental degradation products in fresh fruits and vegetables using a modification of the quick easy cheap effective rugged safe (QuEChERS) method.   TALANTA. Elsevier Science Ltd, New York, NY, USA, 151: 42-50, (2016).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1506062",
             "keyword": [
                 "QuEChERS method",
@@ -102367,14 +102365,10 @@
                 "MDLs/MQLs",
                 "LC-MS/MS"
             ],
-            "contactPoint": {
-                "fn": "James Starr",
-                "hasEmail": "mailto:starr.james@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-08-22",
-            "references": [
-                "https://doi.org/10.1016/j.talanta.2016.01.009"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102384,19 +102378,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.talanta.2016.01.009"
+            ],
+            "rights": null,
+            "title": "Fruit and Vegetable Data"
         },
         {
-            "title": "Abstract Sifter: a comprehensive front-end system to PubMed ",
-            "description": "The Abstract Sifter is a Microsoft Excel based application that enhances existing search capabilities of PubMed. The Abstract Sifter assists researchers to search effectively, triage results, and keep track of articles of interest. The tool implements an innovative \u201csifter\u201d functionality for relevance ranking, giving the researcher a way to find articles of interest quickly. The tool also gives researchers a view of the literature landscape for a set of entities such as chemicals or genes. The Abstract Sifter is available as a Microsoft Excel macro-enabled workbook application. \n\nThis dataset is associated with the following publication:\nBaker, N., T. Knudsen, and A. Williams. Abstract Sifter: a comprehensive front-end system to PubMed (F1000 Research).   F1000 Research. Faculty of 1000, London,  UK, 6: 1-10, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "The Abstract Sifter is a Microsoft Excel based application that enhances existing search capabilities of PubMed. The Abstract Sifter assists researchers to search effectively, triage results, and keep track of articles of interest. The tool implements an innovative \u201csifter\u201d functionality for relevance ranking, giving the researcher a way to find articles of interest quickly. The tool also gives researchers a view of the literature landscape for a set of entities such as chemicals or genes. The Abstract Sifter is available as a Microsoft Excel macro-enabled workbook application. \n\nThis dataset is associated with the following publication:\nBaker, N., T. Knudsen, and A. Williams. Abstract Sifter: a comprehensive front-end system to PubMed (F1000 Research).   F1000 Research. Faculty of 1000, London,  UK, 6: 1-10, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/Chemistry_Dashboard/Abstract_Sifter/AbstractSifter.zip",
+                    "title": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/Chemistry_Dashboard/Abstract_Sifter/AbstractSifter.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504291",
             "keyword": [
@@ -102410,19 +102413,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/Chemistry_Dashboard/Abstract_Sifter/AbstractSifter.zip",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/Chemistry_Dashboard/Abstract_Sifter/AbstractSifter.zip"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-21",
-            "references": [
-                "https://doi.org/10.12688/f1000research.12865.1"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102432,19 +102426,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.12688/f1000research.12865.1"
+            ],
+            "rights": null,
+            "title": "Abstract Sifter: a comprehensive front-end system to PubMed "
         },
         {
-            "title": "The CompTox Chemistry Dashboard: a community data resource for environmental chemistry",
-            "description": "The contents of the chemistry database, presently containing ~ 760,000 substances, are available as public domain data for download. The chemistry content underpinning the Dashboard has been aggregated over the past 15 years by both manual and auto-curation techniques within EPA\u2019s DSSTox project.These data include physicochemical, environmental fate and transport, exposure, usage, in vivo toxicity, and in vitro bioassay data, surfaced through an integration hub with link-outs to additional EPA data and public domain online resources. \n\nThis dataset is associated with the following publication:\nWilliams, A., C. Grulke, J. Edwards, A. McEachran, K. Mansouri, N. Baker, G. Patlewicz, I. Shah, J. Wambaugh, R. Judson, and A. Richard. (Journal of Cheminformatics) The CompTox Chemistry Dashboard - A Community Data Resource for Environmental Chemistry.   Journal of Cheminformatics. Springer, New York, NY, USA, 9(61): 1-27, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "The contents of the chemistry database, presently containing ~ 760,000 substances, are available as public domain data for download. The chemistry content underpinning the Dashboard has been aggregated over the past 15 years by both manual and auto-curation techniques within EPA\u2019s DSSTox project.These data include physicochemical, environmental fate and transport, exposure, usage, in vivo toxicity, and in vitro bioassay data, surfaced through an integration hub with link-outs to additional EPA data and public domain online resources. \n\nThis dataset is associated with the following publication:\nWilliams, A., C. Grulke, J. Edwards, A. McEachran, K. Mansouri, N. Baker, G. Patlewicz, I. Shah, J. Wambaugh, R. Judson, and A. Richard. (Journal of Cheminformatics) The CompTox Chemistry Dashboard - A Community Data Resource for Environmental Chemistry.   Journal of Cheminformatics. Springer, New York, NY, USA, 9(61): 1-27, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://comptox.epa.gov/dashboard/downloads",
+                    "title": "https://comptox.epa.gov/dashboard/downloads"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504292",
             "keyword": [
@@ -102458,19 +102461,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://comptox.epa.gov/dashboard/downloads",
-                    "accessURL": "https://comptox.epa.gov/dashboard/downloads"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-28",
-            "references": [
-                "https://doi.org/10.1186/s13321-017-0247-6"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102480,40 +102474,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s13321-017-0247-6"
+            ],
+            "rights": null,
+            "title": "The CompTox Chemistry Dashboard: a community data resource for environmental chemistry"
         },
         {
-            "title": "Bisphenol A activates EGFR and ERK promoting proliferation, tumor spheroid formation and resistance to EGFR pathway inhibition in estrogen receptor-negative inflammatory breast cancer cells",
-            "description": "Raw data and figures for Bisphenol A activates EGFR and ERK promoting proliferation, tumor spheroid formation and resistance to EGFR pathway inhibition in estrogen receptor-negative inflammatory breast cancer cells manuscript. \n\nThis dataset is associated with the following publication:\nSauer, S.J., M. Tarpley, I. Shah , A.V. Save, H.K. Lyerly, S.R. Patierno, K.P. Williams, and G.R. Devi. (Carcinogenesis) Bisphenol A activates EGFR and ERK promoting proliferation, tumor spheroid formation and resistance to EGFR pathway inhibition in estrogen receptornegative inflammatory breast cancer cells.   CARCINOGENESIS. Oxford University Press, Cary, NC, USA, 38(3): 252\u2013260, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504293",
-            "keyword": [
-                "BPA",
-                "estrogen receptor",
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "Raw data and figures for Bisphenol A activates EGFR and ERK promoting proliferation, tumor spheroid formation and resistance to EGFR pathway inhibition in estrogen receptor-negative inflammatory breast cancer cells manuscript. \n\nThis dataset is associated with the following publication:\nSauer, S.J., M. Tarpley, I. Shah , A.V. Save, H.K. Lyerly, S.R. Patierno, K.P. Williams, and G.R. Devi. (Carcinogenesis) Bisphenol A activates EGFR and ERK promoting proliferation, tumor spheroid formation and resistance to EGFR pathway inhibition in estrogen receptornegative inflammatory breast cancer cells.   CARCINOGENESIS. Oxford University Press, Cary, NC, USA, 38(3): 252\u2013260, (2017).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/BPA_breast_cancer/Figure_Raw_Data.zip",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/BPA_breast_cancer/Figure_Raw_Data.zip"
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/BPA_breast_cancer/Figure_Raw_Data.zip",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/BPA_breast_cancer/Figure_Raw_Data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504293",
+            "keyword": [
+                "BPA",
+                "estrogen receptor",
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-25",
-            "references": [
-                "https://doi.org/10.1093/carcin/bgx003"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102523,38 +102517,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/carcin/bgx003"
+            ],
+            "rights": null,
+            "title": "Bisphenol A activates EGFR and ERK promoting proliferation, tumor spheroid formation and resistance to EGFR pathway inhibition in estrogen receptor-negative inflammatory breast cancer cells"
         },
         {
-            "title": "phase 2/3 oil agent ecotox sci hub data files",
-            "description": "The data set consists of ecotoxicity values for crude oils and spill response agents. \n\nThis dataset is associated with the following publications:\nConmy, R., M. Barron, D. Sundaravadivelu, R. Groser, R. Venkatapathy, A. Burkes, and E. Holder. SCREENING OF POTENTIAL REFERENCE OILS FOR THE NATIONAL CONTINGENCY PLAN PRODUCT SCHEUDLE. U.S. Environmental Protection Agency, Washington, DC, USA, 2019.\nBarron, M., A. Bejarano, R. Conmy, D. Sundaravadivelu, and P. Meyer. Toxicity of oil spill response agents and crude oils to five aquatic test species.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 153(110954): 110954, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1504211",
-            "keyword": [
-                "Acute Toxicity"
-            ],
             "contactPoint": {
                 "fn": "Mace Barron",
                 "hasEmail": "mailto:barron.mace@epa.gov"
             },
+            "description": "The data set consists of ecotoxicity values for crude oils and spill response agents. \n\nThis dataset is associated with the following publications:\nConmy, R., M. Barron, D. Sundaravadivelu, R. Groser, R. Venkatapathy, A. Burkes, and E. Holder. SCREENING OF POTENTIAL REFERENCE OILS FOR THE NATIONAL CONTINGENCY PLAN PRODUCT SCHEUDLE. U.S. Environmental Protection Agency, Washington, DC, USA, 2019.\nBarron, M., A. Bejarano, R. Conmy, D. Sundaravadivelu, and P. Meyer. Toxicity of oil spill response agents and crude oils to five aquatic test species.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 153(110954): 110954, (2020).",
             "distribution": [
                 {
-                    "title": "oil and agent toxicity data for sci hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504211/oil%20and%20agent%20toxicity%20data%20for%20sci%20hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "oil and agent toxicity data for sci hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504211",
+            "keyword": [
+                "Acute Toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-19",
-            "references": [
-                "https://doi.org/10.1016/j.marpolbul.2020.110954"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102564,19 +102558,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.marpolbul.2020.110954"
+            ],
+            "rights": null,
+            "title": "phase 2/3 oil agent ecotox sci hub data files"
         },
         {
-            "title": "In Silico Prediction of Physicochemical Properties of Environmental Chemicals Using Molecular Fingerprints and Machine Learning",
-            "description": "QSAR Model Reporting Formats. Examples of R code: feature selection and regression analysis. Figure S1: Data distribution of logBCF, BP, MP and logVP. Figures S2\u2013S5: Relationship between model complexity and prediction errors as well as the plots of estimated values versus experimental data for logBCF, BP, MP, and logVP, respectively. Figure S6: Plots of leverage versus standardized residuals for logBCF, BP, MP, and logVP models. Table S1: Chemical product classes for training and test sets. Tables S2\u2013S5: Regression statistics for logBCF, BP, MP, and logVP, respectively. Table S6: Applicability domains for logBCF, BP, MP, and logVP. Tables S7\u2013S12: Chemicals with large prediction residuals for the six properties (PDF)\n\nChemical names, CAS registry number and SMILES as well as experimentally measured and estimated property values of the training and test sets (XLSX). \n\nThis dataset is associated with the following publication:\nZang, Q., K. Mansouri, A. Williams, R. Judson, D. Allen, W.M. Casey, and N.C. Kleinstreuer. (Journal of Chemical Information and Modeling) In Silico Prediction of Physicochemical Properties of Environmental Chemicals Using Molecular Fingerprints and Machine Learning.   Journal of Chemical Information and Modeling. American Chemical Society, Washington, DC, USA, 57(1): 36-49, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "QSAR Model Reporting Formats. Examples of R code: feature selection and regression analysis. Figure S1: Data distribution of logBCF, BP, MP and logVP. Figures S2\u2013S5: Relationship between model complexity and prediction errors as well as the plots of estimated values versus experimental data for logBCF, BP, MP, and logVP, respectively. Figure S6: Plots of leverage versus standardized residuals for logBCF, BP, MP, and logVP models. Table S1: Chemical product classes for training and test sets. Tables S2\u2013S5: Regression statistics for logBCF, BP, MP, and logVP, respectively. Table S6: Applicability domains for logBCF, BP, MP, and logVP. Tables S7\u2013S12: Chemicals with large prediction residuals for the six properties (PDF)\n\nChemical names, CAS registry number and SMILES as well as experimentally measured and estimated property values of the training and test sets (XLSX). \n\nThis dataset is associated with the following publication:\nZang, Q., K. Mansouri, A. Williams, R. Judson, D. Allen, W.M. Casey, and N.C. Kleinstreuer. (Journal of Chemical Information and Modeling) In Silico Prediction of Physicochemical Properties of Environmental Chemicals Using Molecular Fingerprints and Machine Learning.   Journal of Chemical Information and Modeling. American Chemical Society, Washington, DC, USA, 57(1): 36-49, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://pubs.acs.org/doi/abs/10.1021%2Facs.jcim.6b00625",
+                    "title": "https://pubs.acs.org/doi/abs/10.1021%2Facs.jcim.6b00625"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504459",
             "keyword": [
@@ -102587,19 +102590,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://pubs.acs.org/doi/abs/10.1021%2Facs.jcim.6b00625",
-                    "accessURL": "https://pubs.acs.org/doi/abs/10.1021%2Facs.jcim.6b00625"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-22",
-            "references": [
-                "https://doi.org/10.1021/acs.jcim.6b00625"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102609,19 +102603,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.jcim.6b00625"
+            ],
+            "rights": null,
+            "title": "In Silico Prediction of Physicochemical Properties of Environmental Chemicals Using Molecular Fingerprints and Machine Learning"
         },
         {
-            "title": "Predictive Structure-Based Toxicology Approaches To Assess the Androgenic Potential of Chemicals",
-            "description": "Chemical structures, RMSD values, docking scores, additional tables and figures, and methodological details (PDF)\nAdditional information concerning the starting data set, EPA-ARDB.csv (CSV)\nAdditional information concerning V1, V1_SI.csv (CSV)\nAdditional information concerning V2, V2_SI.csv (CSV)\nAdditional information concerning V3, V3_SI.csv (CSV). \n\nThis dataset is associated with the following publication:\nTrisciuzzi, D., D. Alberga, K. Mansouri, R. Judson, E. Novellino, G.F. Mangiatordi, and O. Nicolotti. Predictive structure-based toxicology approaches to assess the androgenic potential of chemicals.   Journal of Chemical Information and Modeling. American Chemical Society, Washington, DC, USA, 57(11): 2874-2884, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "Chemical structures, RMSD values, docking scores, additional tables and figures, and methodological details (PDF)\nAdditional information concerning the starting data set, EPA-ARDB.csv (CSV)\nAdditional information concerning V1, V1_SI.csv (CSV)\nAdditional information concerning V2, V2_SI.csv (CSV)\nAdditional information concerning V3, V3_SI.csv (CSV). \n\nThis dataset is associated with the following publication:\nTrisciuzzi, D., D. Alberga, K. Mansouri, R. Judson, E. Novellino, G.F. Mangiatordi, and O. Nicolotti. Predictive structure-based toxicology approaches to assess the androgenic potential of chemicals.   Journal of Chemical Information and Modeling. American Chemical Society, Washington, DC, USA, 57(11): 2874-2884, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1021/acs.jcim.7b00420",
+                    "title": "https://doi.org/10.1021/acs.jcim.7b00420"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504460",
             "keyword": [
@@ -102631,19 +102634,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1021/acs.jcim.7b00420",
-                    "accessURL": "https://doi.org/10.1021/acs.jcim.7b00420"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-12",
-            "references": [
-                "https://doi.org/10.1021/acs.jcim.7b00420"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102653,19 +102647,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.jcim.7b00420"
+            ],
+            "rights": null,
+            "title": "Predictive Structure-Based Toxicology Approaches To Assess the Androgenic Potential of Chemicals"
         },
         {
-            "title": "A hybrid gene selection approach to create the S1500+ targeted gene sets for use in high-throughput transcriptomics",
-            "description": "The U.S. Tox21 Federal collaboration, which currently quantifies the biological effects of nearly 10,000 chemicals via quantitative high-throughput screening(qHTS) in in vitro model systems, is now making an effort to incorporate gene expression profiling into the existing battery of assays. Whole transcriptome analyses performed on large numbers of samples using microarrays or RNA-Seq is currently cost-prohibitive. Accordingly, the Tox21 Program is pursuing a high-throughput transcriptomics (HTT) method that focuses on the targeted detection of gene expression for a carefully selected subset of the transcriptome that potentially can reduce the cost by a factor of 10-fold, allowing for the analysis of larger numbers of samples. To identify the optimal transcriptome subset, genes were sought that are (1) representative of the highly diverse biological space, (2) capable of serving as a proxy for expression changes in unmeasured genes, and (3) sufficient to provide coverage of well described biological pathways. A hybrid method for gene selection is presented herein that combines data-driven and knowledge-driven concepts into one cohesive method. \n\nThis dataset is associated with the following publication:\nMav, D., R.R. Shah, B.E. Howard, S.S. Auerbach, P.R. Bushel, J.B. Collins, D.L. Gerhold, R. Judson, A.L. Karmaus, E.A. Maull, D.L. Mendrick, B.A. Merrick, N.S. Sipes, D. Svoboda, and R.S. Paules. A hybrid gene selection approach to create the S1500+ targeted gene sets for use in high-throughput transcriptomics.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 13(2): 1-17, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "The U.S. Tox21 Federal collaboration, which currently quantifies the biological effects of nearly 10,000 chemicals via quantitative high-throughput screening(qHTS) in in vitro model systems, is now making an effort to incorporate gene expression profiling into the existing battery of assays. Whole transcriptome analyses performed on large numbers of samples using microarrays or RNA-Seq is currently cost-prohibitive. Accordingly, the Tox21 Program is pursuing a high-throughput transcriptomics (HTT) method that focuses on the targeted detection of gene expression for a carefully selected subset of the transcriptome that potentially can reduce the cost by a factor of 10-fold, allowing for the analysis of larger numbers of samples. To identify the optimal transcriptome subset, genes were sought that are (1) representative of the highly diverse biological space, (2) capable of serving as a proxy for expression changes in unmeasured genes, and (3) sufficient to provide coverage of well described biological pathways. A hybrid method for gene selection is presented herein that combines data-driven and knowledge-driven concepts into one cohesive method. \n\nThis dataset is associated with the following publication:\nMav, D., R.R. Shah, B.E. Howard, S.S. Auerbach, P.R. Bushel, J.B. Collins, D.L. Gerhold, R. Judson, A.L. Karmaus, E.A. Maull, D.L. Mendrick, B.A. Merrick, N.S. Sipes, D. Svoboda, and R.S. Paules. A hybrid gene selection approach to create the S1500+ targeted gene sets for use in high-throughput transcriptomics.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 13(2): 1-17, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1371/journal.pone.0191105",
+                    "title": "https://doi.org/10.1371/journal.pone.0191105"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504520",
             "keyword": [
@@ -102678,19 +102681,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1371/journal.pone.0191105",
-                    "accessURL": "https://doi.org/10.1371/journal.pone.0191105"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-20",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0191105"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102700,19 +102694,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0191105"
+            ],
+            "rights": null,
+            "title": "A hybrid gene selection approach to create the S1500+ targeted gene sets for use in high-throughput transcriptomics"
         },
         {
-            "title": "Assessing bioactivity-exposure profiles of fruit and vegetable extracts in the BioMAP profiling system",
-            "description": "The ToxCast program has generated in vitro screening data on over a thousand chemicals to assess potential disruption of important biological processes and assist in hazard identification and chemical testing prioritization. Few results have been reported for complex mixtures. To extend these ToxCast efforts to mixtures, we tested extracts from 30 organically grown fruits and vegetables in concentration-response in the BioMAP\u00ae assays. BioMAP systems use human primary cells primed with endogenous pathway activators to identify phenotypic perturbations related to proliferation, inflammation, immunomodulation, and tissue remodeling. \n\nThis dataset is associated with the following publication:\nWetmore, B., R. Clewell, B. Cholewa, B. Parks, S. Pendse, M. Black, K. Mansouri, S. Haider, E. Berg, R. Judson, K. Houck, M. Martin, H. Clewell III, M. Andersen, R. Thomas, and P. McMullen. Assessing Bioactivity-Exposure Profiles of Fruits and Vegetables in the BioMAP Profiling System.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 54: 41-57, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "The ToxCast program has generated in vitro screening data on over a thousand chemicals to assess potential disruption of important biological processes and assist in hazard identification and chemical testing prioritization. Few results have been reported for complex mixtures. To extend these ToxCast efforts to mixtures, we tested extracts from 30 organically grown fruits and vegetables in concentration-response in the BioMAP\u00ae assays. BioMAP systems use human primary cells primed with endogenous pathway activators to identify phenotypic perturbations related to proliferation, inflammation, immunomodulation, and tissue remodeling. \n\nThis dataset is associated with the following publication:\nWetmore, B., R. Clewell, B. Cholewa, B. Parks, S. Pendse, M. Black, K. Mansouri, S. Haider, E. Berg, R. Judson, K. Houck, M. Martin, H. Clewell III, M. Andersen, R. Thomas, and P. McMullen. Assessing Bioactivity-Exposure Profiles of Fruits and Vegetables in the BioMAP Profiling System.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 54: 41-57, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1016/j.tiv.2018.09.006",
+                    "title": "https://doi.org/10.1016/j.tiv.2018.09.006"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504521",
             "keyword": [
@@ -102723,19 +102726,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1016/j.tiv.2018.09.006",
-                    "accessURL": "https://doi.org/10.1016/j.tiv.2018.09.006"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-19",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2018.09.006"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102745,19 +102739,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2018.09.006"
+            ],
+            "rights": null,
+            "title": "Assessing bioactivity-exposure profiles of fruit and vegetable extracts in the BioMAP profiling system"
         },
         {
-            "title": "NMReDATA, a standard to report the NMR assignment and parameters of organic compounds",
-            "description": "Data S1. Example of NMReDATA.sdf file including NMReDATA for benzo[a]pyrene\n\nData S2. Pure text translation of the NMReDATA.sdf of benzo[a]pyrene. \n\nThis dataset is associated with the following publication:\nPupier, M., J. Nuzillard, J. Wist, N.E. Schl\u00f6rer, S. Kuhn, M. Erdelyi, C. Steinbeck, A. Williams, C. Butts, T.D.W. Claridge, B. Mikhova, W. Robien, H. Dashti, H.R. Eghbalnia, C. Far\u00e8s, C. Adam, P. Kessler, F. Moriaud, M. Elyashberg, D. Argyropoulos, M. P\u00e9rez, P. Giraudeau, R.R. Gil, P. Trevorrow, and D. Jeannerat. NMReDATA, a standard to report the NMR assignment and parameters of organic compounds.   Magnetic Resonance in Chemistry. John Wiley & Sons, Inc., Hoboken, NJ, USA, 56(8): 703-715, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "Data S1. Example of NMReDATA.sdf file including NMReDATA for benzo[a]pyrene\n\nData S2. Pure text translation of the NMReDATA.sdf of benzo[a]pyrene. \n\nThis dataset is associated with the following publication:\nPupier, M., J. Nuzillard, J. Wist, N.E. Schl\u00f6rer, S. Kuhn, M. Erdelyi, C. Steinbeck, A. Williams, C. Butts, T.D.W. Claridge, B. Mikhova, W. Robien, H. Dashti, H.R. Eghbalnia, C. Far\u00e8s, C. Adam, P. Kessler, F. Moriaud, M. Elyashberg, D. Argyropoulos, M. P\u00e9rez, P. Giraudeau, R.R. Gil, P. Trevorrow, and D. Jeannerat. NMReDATA, a standard to report the NMR assignment and parameters of organic compounds.   Magnetic Resonance in Chemistry. John Wiley & Sons, Inc., Hoboken, NJ, USA, 56(8): 703-715, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1002/mrc.4737",
+                    "title": "https://doi.org/10.1002/mrc.4737"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504523",
             "keyword": [
@@ -102770,19 +102773,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1002/mrc.4737",
-                    "accessURL": "https://doi.org/10.1002/mrc.4737"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-14",
-            "references": [
-                "https://doi.org/10.1002/mrc.4737"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102792,19 +102786,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/mrc.4737"
+            ],
+            "rights": null,
+            "title": "NMReDATA, a standard to report the NMR assignment and parameters of organic compounds"
         },
         {
-            "title": "Identification of vascular disruptor compounds by analysis in zebrafish embryos and mouse embryonic endothelial cells",
-            "description": "In zebrafish, 161 compounds were screened and 34 were identified by visual inspection as VDCs, of which 28 were confirmed as VDCs by quantitative image analysis. Testing of the zebrafish VDCs for their capacity to inhibit endothelial tube formation in the murine yolk-sac-derived endothelial cell line C166 identified 22 compounds that both disrupted zebrafish vascular development and murine endothelial in vitro tubulogenesis. \n\nThis dataset is associated with the following publication:\nMcCollum, C., J. Conde Vancells, C. Hans, M. Vazquez-Chantada, N. Kleinstreuer, T. Tal , T. Knudsen, S. Shah, F. Merchant, R. Finnell, J. Gustafsson, R. Cabrera, and M. Bondesson. (Reproductive Toxicology) Identification of vascular disruptor compounds by a tiered analysis in zebrafish embryos and mouse embryonic endothelial cells.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 70: 60-69, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "In zebrafish, 161 compounds were screened and 34 were identified by visual inspection as VDCs, of which 28 were confirmed as VDCs by quantitative image analysis. Testing of the zebrafish VDCs for their capacity to inhibit endothelial tube formation in the murine yolk-sac-derived endothelial cell line C166 identified 22 compounds that both disrupted zebrafish vascular development and murine endothelial in vitro tubulogenesis. \n\nThis dataset is associated with the following publication:\nMcCollum, C., J. Conde Vancells, C. Hans, M. Vazquez-Chantada, N. Kleinstreuer, T. Tal , T. Knudsen, S. Shah, F. Merchant, R. Finnell, J. Gustafsson, R. Cabrera, and M. Bondesson. (Reproductive Toxicology) Identification of vascular disruptor compounds by a tiered analysis in zebrafish embryos and mouse embryonic endothelial cells.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 70: 60-69, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1016/j.reprotox.2016.11.005",
+                    "title": "https://doi.org/10.1016/j.reprotox.2016.11.005"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504524",
             "keyword": [
@@ -102815,19 +102818,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1016/j.reprotox.2016.11.005",
-                    "accessURL": "https://doi.org/10.1016/j.reprotox.2016.11.005"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-16",
-            "references": [
-                "https://doi.org/10.1016/j.reprotox.2016.11.005"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102837,19 +102831,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.reprotox.2016.11.005"
+            ],
+            "rights": null,
+            "title": "Identification of vascular disruptor compounds by analysis in zebrafish embryos and mouse embryonic endothelial cells"
         },
         {
-            "title": "Non\u2010animal assessment of skin sensitization hazard: Is an integrated testing strategy needed, and if so what should be integrated?",
-            "description": "Appendix Skin sensitization data and non\u2010animal test data for 271 chemicals. \n\nThis dataset is associated with the following publication:\nRoberts, D., and G. Patlewicz. Non\u2010animal assessment of skin sensitization hazard: Is an integrated testing strategy needed, and if so what should be integrated?.   JOURNAL OF APPLIED TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 38(1): 41-50, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Alexander Hanf",
+                "hasEmail": "mailto:hanf.alexander@epa.gov"
+            },
+            "description": "Appendix Skin sensitization data and non\u2010animal test data for 271 chemicals. \n\nThis dataset is associated with the following publication:\nRoberts, D., and G. Patlewicz. Non\u2010animal assessment of skin sensitization hazard: Is an integrated testing strategy needed, and if so what should be integrated?.   JOURNAL OF APPLIED TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 38(1): 41-50, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1002/jat.3479",
+                    "title": "https://doi.org/10.1002/jat.3479"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504548",
             "keyword": [
@@ -102863,19 +102866,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Alexander Hanf",
-                "hasEmail": "mailto:hanf.alexander@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1002/jat.3479",
-                    "accessURL": "https://doi.org/10.1002/jat.3479"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-24",
-            "references": [
-                "https://doi.org/10.1002/jat.3479"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102885,38 +102879,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/jat.3479"
+            ],
+            "rights": null,
+            "title": "Non\u2010animal assessment of skin sensitization hazard: Is an integrated testing strategy needed, and if so what should be integrated?"
         },
         {
-            "title": "Weaver's historic accessible collection of synthetic dyes: a cheminformatics analysis",
-            "description": "This is a subset of 150 chemical dyes that are housed in the Max Weaver Dye Library at North Carolina State University\nHISTORY. \n\nThis dataset is associated with the following publication:\nKuenemann, M., M. Szymczyk, Y. Chen, N. Sultana, D. Hinks, H. Freeman, A. Williams, D. Fourches, and N. Vinueza. Weaver\u2019s Historic Accessible Collection of Synthetic Dyes: A Cheminformatics Analysis.   Chemical Science. RSC Publishing, Cambridge,  UK, issue}: 4334-4339, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504550",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "This is a subset of 150 chemical dyes that are housed in the Max Weaver Dye Library at North Carolina State University\nHISTORY. \n\nThis dataset is associated with the following publication:\nKuenemann, M., M. Szymczyk, Y. Chen, N. Sultana, D. Hinks, H. Freeman, A. Williams, D. Fourches, and N. Vinueza. Weaver\u2019s Historic Accessible Collection of Synthetic Dyes: A Cheminformatics Analysis.   Chemical Science. RSC Publishing, Cambridge,  UK, issue}: 4334-4339, (2017).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.6084/m9.figshare.4590250",
-                    "accessURL": "https://doi.org/10.6084/m9.figshare.4590250"
+                    "accessURL": "https://doi.org/10.6084/m9.figshare.4590250",
+                    "title": "https://doi.org/10.6084/m9.figshare.4590250"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504550",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-02-07",
-            "references": [
-                "https://doi.org/10.1039/c7sc00567a"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102926,33 +102920,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c7sc00567a"
+            ],
+            "rights": null,
+            "title": "Weaver's historic accessible collection of synthetic dyes: a cheminformatics analysis"
         },
         {
-            "title": "(Toxicology) Identifying Environmental Chemicals as Agonists of the Androgen Receptor by Applying a Quantitative High-throughput Screening Platform",
-            "description": "The paper has data generated by NIH and the EPA coauthors provided input into the preparation of the manuscript. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: Data generated by NIH. Format: N/A. \n\nThis dataset is associated with the following publication:\nLynch, C., S. Sakamuru, R. Huang, D.A. Stavea, L. Varticovski, G.L. Hagar, R.S. Judson, K.A. Houck, N.C. Kleinstreuer, W. Casey, R.S. Paules, A. Simeonov, and M. Xia. (Toxicology) Identifying Environmental Chemicals as Agonists of the Androgen Receptor by Applying a Quantitative High-throughput Screening Platform.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 385: 48-58, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504595",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "The paper has data generated by NIH and the EPA coauthors provided input into the preparation of the manuscript. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: Data generated by NIH. Format: N/A. \n\nThis dataset is associated with the following publication:\nLynch, C., S. Sakamuru, R. Huang, D.A. Stavea, L. Varticovski, G.L. Hagar, R.S. Judson, K.A. Houck, N.C. Kleinstreuer, W. Casey, R.S. Paules, A. Simeonov, and M. Xia. (Toxicology) Identifying Environmental Chemicals as Agonists of the Androgen Receptor by Applying a Quantitative High-throughput Screening Platform.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 385: 48-58, (2017).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1504595",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-15",
-            "references": [
-                "https://doi.org/10.1016/j.tox.2017.05.001"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102962,33 +102956,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tox.2017.05.001"
+            ],
+            "rights": null,
+            "title": "(Toxicology) Identifying Environmental Chemicals as Agonists of the Androgen Receptor by Applying a Quantitative High-throughput Screening Platform"
         },
         {
-            "title": "Comprehensive analyses and prioritization of Tox21 10K chemicals affecting mitochondrial function by in-depth mechanistic studies",
-            "description": "All data is generated outside of EPA by NCATS, NIH. EPA coauthors assisted with writing the manuscript. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: Data generated by NIH. Format: N/A. \n\nThis dataset is associated with the following publication:\nXia, M., R. Huang, Q. Shi, W. Boyd, J. Zhao, N. Sun, J.R. Rice, P.E. Dunlap, A.J. Hackstadt, M.F. Bridge, M.V. Smith, S. Dai, W. Zheng, P. Chu, D. Gerhold, K.L. Witt, M. DeVito, J.H. Freeman, C.P. Austin, K. Houck, R. Thomas, R.S. Paules, R.B. Tice, and A. Simeonov. Comprehensive analyses and prioritization of Tox21 10K chemicals affecting mitochondrial function by in-depth mechanistic studies.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 126(7): 1-16, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504602",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "All data is generated outside of EPA by NCATS, NIH. EPA coauthors assisted with writing the manuscript. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: Data generated by NIH. Format: N/A. \n\nThis dataset is associated with the following publication:\nXia, M., R. Huang, Q. Shi, W. Boyd, J. Zhao, N. Sun, J.R. Rice, P.E. Dunlap, A.J. Hackstadt, M.F. Bridge, M.V. Smith, S. Dai, W. Zheng, P. Chu, D. Gerhold, K.L. Witt, M. DeVito, J.H. Freeman, C.P. Austin, K. Houck, R. Thomas, R.S. Paules, R.B. Tice, and A. Simeonov. Comprehensive analyses and prioritization of Tox21 10K chemicals affecting mitochondrial function by in-depth mechanistic studies.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 126(7): 1-16, (2018).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1504602",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-26",
-            "references": [
-                "https://doi.org/10.1289/ehp2589"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -102998,33 +102992,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp2589"
+            ],
+            "rights": null,
+            "title": "Comprehensive analyses and prioritization of Tox21 10K chemicals affecting mitochondrial function by in-depth mechanistic studies"
         },
         {
-            "title": "Confirmation of High-Throughput screening data and novel mechanistic insights into VDR-xenobiotic interactions by orthogonal assays",
-            "description": "All data is generated by the external authors or taken from public data sources. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: All data is generated by the external authors or taken from public data sources. Format: N/A. \n\nThis dataset is associated with the following publication:\nMahapatra, D., J.A. Franzosa, K. Roell, M.A. Kuenemann, K.A. Houck, D.M. Reif, D. Fourches, and S.W. Kullman. Confirmation of High-Throughput screening data and novel mechanistic insights into VDR-xenobiotic interactions by orthogonal assays.   Scientific Reports. Nature Publishing Group, London,  UK, 8(8883): 1-16, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504603",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "All data is generated by the external authors or taken from public data sources. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: All data is generated by the external authors or taken from public data sources. Format: N/A. \n\nThis dataset is associated with the following publication:\nMahapatra, D., J.A. Franzosa, K. Roell, M.A. Kuenemann, K.A. Houck, D.M. Reif, D. Fourches, and S.W. Kullman. Confirmation of High-Throughput screening data and novel mechanistic insights into VDR-xenobiotic interactions by orthogonal assays.   Scientific Reports. Nature Publishing Group, London,  UK, 8(8883): 1-16, (2018).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1504603",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-11",
-            "references": [
-                "https://doi.org/10.1038/s41598-018-27055-3"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103034,33 +103028,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-018-27055-3"
+            ],
+            "rights": null,
+            "title": "Confirmation of High-Throughput screening data and novel mechanistic insights into VDR-xenobiotic interactions by orthogonal assays"
         },
         {
-            "title": "(Crit. Rev. Tox.) Comparison of rat and rabbit embryo-fetal developmental toxicity data for 379 pharmaceuticals: on the nature and severity of developmental effects",
-            "description": "This paper uses EPA public data to build new datasets and analysis by non-EPA authors. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: This paper uses EPA public data to build new datasets and analysis by non-EPA authors. Format: N/A. \n\nThis dataset is associated with the following publication:\nTheunissen, P., S. Beken, B. Beyer, W. Breslin, G. Cappon, C. Chen, G. Chmielewski, L. De Schaepdrijver, B. Enright, J. Foreman, W. Harrouk, K. Hew, A. Hoberman, J. Hui, T. Knudsen , S. Laffan, S. Makris , M. Martin , M. McNerney, C. Siezen, D. Stanislaus, J. Stewart, K. Thompson, B. Tornesi, G. Weinbauer, S. Wood, J. Van der Laan, and A. Piersma. (Crit. Rev. Tox.) Comparison of rat and rabbit embryo-fetal developmental toxicity data for 379 pharmaceuticals: on the nature and severity of developmental effects.   CRITICAL REVIEWS IN TOXICOLOGY. CRC Press LLC, Boca Raton, FL, USA,  1-11, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1504604",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "This paper uses EPA public data to build new datasets and analysis by non-EPA authors. This dataset is not publicly accessible because: Data was not collected in EPA labs or paid for by EPA. It can be accessed through the following means: This paper uses EPA public data to build new datasets and analysis by non-EPA authors. Format: N/A. \n\nThis dataset is associated with the following publication:\nTheunissen, P., S. Beken, B. Beyer, W. Breslin, G. Cappon, C. Chen, G. Chmielewski, L. De Schaepdrijver, B. Enright, J. Foreman, W. Harrouk, K. Hew, A. Hoberman, J. Hui, T. Knudsen , S. Laffan, S. Makris , M. Martin , M. McNerney, C. Siezen, D. Stanislaus, J. Stewart, K. Thompson, B. Tornesi, G. Weinbauer, S. Wood, J. Van der Laan, and A. Piersma. (Crit. Rev. Tox.) Comparison of rat and rabbit embryo-fetal developmental toxicity data for 379 pharmaceuticals: on the nature and severity of developmental effects.   CRITICAL REVIEWS IN TOXICOLOGY. CRC Press LLC, Boca Raton, FL, USA,  1-11, (2016).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1504604",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-19",
-            "references": [
-                "https://doi.org/10.1080/10408444.2016.1224807"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103070,33 +103064,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10408444.2016.1224807"
+            ],
+            "rights": null,
+            "title": "(Crit. Rev. Tox.) Comparison of rat and rabbit embryo-fetal developmental toxicity data for 379 pharmaceuticals: on the nature and severity of developmental effects"
         },
         {
-            "title": "(Crit. Rev. Tox.) Comparing rat and rabbit embryo-fetal developmental toxicity studies for 379 pharmaceuticals: On systemic dose and developmental effects",
-            "description": "A database of embryo-fetal developmental toxicity (EFDT) studies of 379 pharmaceutical compounds in rat and rabbit. This dataset is not publicly accessible because: this paper uses EPA public data to build new datasets and analysis by non-EPA authors. It can be accessed through the following means: EPA data is publicly accessible. Format: N/A. \n\nThis dataset is associated with the following publication:\nTheunissen, P., S. Beken, B. Beyer, W. Breslin, G.D. Cappon, C. Chen, G. Chmielewski, L. De Schaepdrijver, B. Enright, J. Foreman, W. Harrouk, K. Hew, A. Hoberman, J. Hui, T. Knudsen , S. Laffan, S. Makris , and M. Martin. (Crit. Rev. Tox.) Comparing rat and rabbit embryo-fetal developmental toxicity studies for 379 pharmaceuticals: On systemic dose and developmental effects.   CRITICAL REVIEWS IN TOXICOLOGY. CRC Press LLC, Boca Raton, FL, USA,  1-13, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1505446",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "A database of embryo-fetal developmental toxicity (EFDT) studies of 379 pharmaceutical compounds in rat and rabbit. This dataset is not publicly accessible because: this paper uses EPA public data to build new datasets and analysis by non-EPA authors. It can be accessed through the following means: EPA data is publicly accessible. Format: N/A. \n\nThis dataset is associated with the following publication:\nTheunissen, P., S. Beken, B. Beyer, W. Breslin, G.D. Cappon, C. Chen, G. Chmielewski, L. De Schaepdrijver, B. Enright, J. Foreman, W. Harrouk, K. Hew, A. Hoberman, J. Hui, T. Knudsen , S. Laffan, S. Makris , and M. Martin. (Crit. Rev. Tox.) Comparing rat and rabbit embryo-fetal developmental toxicity studies for 379 pharmaceuticals: On systemic dose and developmental effects.   CRITICAL REVIEWS IN TOXICOLOGY. CRC Press LLC, Boca Raton, FL, USA,  1-13, (2016).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1505446",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-21",
-            "references": [
-                "https://doi.org/10.1080/10408444.2016.1224808"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103106,33 +103100,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10408444.2016.1224808"
+            ],
+            "rights": null,
+            "title": "(Crit. Rev. Tox.) Comparing rat and rabbit embryo-fetal developmental toxicity studies for 379 pharmaceuticals: On systemic dose and developmental effects"
         },
         {
-            "title": "Versatile synthetic alternatives to Matrigel for vascular toxicity screening and stem cell expansion",
-            "description": "Paper studying synthetic hydrogels as an alternative to matrigel. This dataset is not publicly accessible because: Research data consisted of secondary data only. It can be accessed through the following means: EPA's ToxCast Library. Format: N/A. \n\nThis dataset is associated with the following publication:\nNguyen, E., W. Daly, N.N.T. Le, M. Farnoodian, D. Belair, M. Schwartz, C. Lebakken, G. Ananiev, M. Saghiri, T. Knudsen, N. Sheibani, and W. Murphy. Versatile synthetic alternatives to Matrigel for vascular toxicity screening and stem cell expansion.   Nature Communications. Nature Publishing Group, London,  UK, 1(0096): 1-34, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1505447",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "Paper studying synthetic hydrogels as an alternative to matrigel. This dataset is not publicly accessible because: Research data consisted of secondary data only. It can be accessed through the following means: EPA's ToxCast Library. Format: N/A. \n\nThis dataset is associated with the following publication:\nNguyen, E., W. Daly, N.N.T. Le, M. Farnoodian, D. Belair, M. Schwartz, C. Lebakken, G. Ananiev, M. Saghiri, T. Knudsen, N. Sheibani, and W. Murphy. Versatile synthetic alternatives to Matrigel for vascular toxicity screening and stem cell expansion.   Nature Communications. Nature Publishing Group, London,  UK, 1(0096): 1-34, (2018).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1505447",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-11",
-            "references": [
-                "https://doi.org/10.1038/s41551-017-0096"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103142,33 +103136,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41551-017-0096"
+            ],
+            "rights": null,
+            "title": "Versatile synthetic alternatives to Matrigel for vascular toxicity screening and stem cell expansion"
         },
         {
-            "title": "(REPRODUCTIVE TOXICOLOGY)  EMBRYONIC VASCULAR DISRUPTION ADVERSE OUTCOMES: LINKING HIGH THROUGHPUT SIGNALING SIGNATURES WITH FUNCTIONAL CONSEQUENCES",
-            "description": "This study evaluated two anti-angiogenic agents, 5HPP-33 and TNP-470, across the ToxCastDB HTS assay platform and anchored the results to complex in vitro functional assays: the rat aortic explant assay (AEA), rat whole embryo culture (WEC), and the zebrafish embryotoxicity (ZET) assay. This dataset is not publicly accessible because: no EPA data; all the data generated by external organizations; EPA coauthors. It can be accessed through the following means: Data generated by external organizations. Format: N/A. \n\nThis dataset is associated with the following publication:\nEllis-Hutchings, R., R. Settivari, A. McCoy, N. Kleinstreuer, J. Franzosa, T. Knudsen, and E. Carney. (REPRODUCTIVE TOXICOLOGY)  EMBRYONIC VASCULAR DISRUPTION ADVERSE OUTCOMES: LINKING HIGH THROUGHPUT SIGNALING SIGNATURES WITH FUNCTIONAL CONSEQUENCES.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 70: 82-96, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1505448",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "This study evaluated two anti-angiogenic agents, 5HPP-33 and TNP-470, across the ToxCastDB HTS assay platform and anchored the results to complex in vitro functional assays: the rat aortic explant assay (AEA), rat whole embryo culture (WEC), and the zebrafish embryotoxicity (ZET) assay. This dataset is not publicly accessible because: no EPA data; all the data generated by external organizations; EPA coauthors. It can be accessed through the following means: Data generated by external organizations. Format: N/A. \n\nThis dataset is associated with the following publication:\nEllis-Hutchings, R., R. Settivari, A. McCoy, N. Kleinstreuer, J. Franzosa, T. Knudsen, and E. Carney. (REPRODUCTIVE TOXICOLOGY)  EMBRYONIC VASCULAR DISRUPTION ADVERSE OUTCOMES: LINKING HIGH THROUGHPUT SIGNALING SIGNATURES WITH FUNCTIONAL CONSEQUENCES.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 70: 82-96, (2017).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1505448",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-01",
-            "references": [
-                "https://doi.org/10.1016/j.reprotox.2017.05.005"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103178,33 +103172,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.reprotox.2017.05.005"
+            ],
+            "rights": null,
+            "title": "(REPRODUCTIVE TOXICOLOGY)  EMBRYONIC VASCULAR DISRUPTION ADVERSE OUTCOMES: LINKING HIGH THROUGHPUT SIGNALING SIGNATURES WITH FUNCTIONAL CONSEQUENCES"
         },
         {
-            "title": "(ALTEX) Use of High-throughput in vitro toxicity screening data in cancer hazard evaluations by the IARC Monograph Working Groups",
-            "description": "Three recent IARC Working Groups pioneered inclusion of the US Environmental Protection Agency (EPA) ToxCast program high-throughput screening (HTS) data to supplement other mechanistic evidence. In Monograph V110, HTS profiles were compared between perfluorooctanoic acid (PFOA) and prototypical activators across multiple nuclear receptors. For Monograph V112-113, HTS assays were mapped to 10 key characteristics of carcinogens identified by an IARC expert group, and systematically considered as an additional mechanistic data stream. This dataset is not publicly accessible because: The data is generated by external authors from existing public data sources. It can be accessed through the following means: Data is available in existing public data sources. Format: N/A. \n\nThis dataset is associated with the following publication:\nChiu, W., K. Guyton, M. Martin, D. Reif, and I. Rusyn. (ALTEX) Use of High-throughput in vitro toxicity screening data in cancer hazard evaluations by the IARC Monograph Working Groups.   ALTEX. Society ALTEX Edition, Kuesnacht,  SWITZERLAND, 35(1): 51-64, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1505449",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "Three recent IARC Working Groups pioneered inclusion of the US Environmental Protection Agency (EPA) ToxCast program high-throughput screening (HTS) data to supplement other mechanistic evidence. In Monograph V110, HTS profiles were compared between perfluorooctanoic acid (PFOA) and prototypical activators across multiple nuclear receptors. For Monograph V112-113, HTS assays were mapped to 10 key characteristics of carcinogens identified by an IARC expert group, and systematically considered as an additional mechanistic data stream. This dataset is not publicly accessible because: The data is generated by external authors from existing public data sources. It can be accessed through the following means: Data is available in existing public data sources. Format: N/A. \n\nThis dataset is associated with the following publication:\nChiu, W., K. Guyton, M. Martin, D. Reif, and I. Rusyn. (ALTEX) Use of High-throughput in vitro toxicity screening data in cancer hazard evaluations by the IARC Monograph Working Groups.   ALTEX. Society ALTEX Edition, Kuesnacht,  SWITZERLAND, 35(1): 51-64, (2018).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1505449",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-24",
-            "references": [
-                "https://doi.org/10.14573/altex.1703231"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103214,33 +103208,33 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.14573/altex.1703231"
+            ],
+            "rights": null,
+            "title": "(ALTEX) Use of High-throughput in vitro toxicity screening data in cancer hazard evaluations by the IARC Monograph Working Groups"
         },
         {
-            "title": "(Archives of Toxicology) Recommended approaches in the application of toxicogenomics to derive points of departure for chemical risk assessment",
-            "description": "To determine the best way to select predictive groups of genes, we used published microarray data from dose-response studies on six chemicals in rats exposed orally for 5, 14, 28, and 90 days. We evaluated eight approaches for selecting genes for POD derivation and three previously proposed approaches (the lowest pathway BMD, and the mean and median BMD of all genes). This dataset is not publicly accessible because: The research which produced this data was not funded by EPA. The EPA coauthor helped write the manuscript. It can be accessed through the following means: Data generated by other authors. Format: N/A. \n\nThis dataset is associated with the following publication:\nFarmahin, R., A. Williams, B. Kuo, N.L. Chepelev, R.S. Thomas, T.S. Burton-Maclaren, I.H. Curran, A. Nong, M.G. Wade, and C.L. Yauk. (Archives of Toxicology) Recommended approaches in the application of toxicogenomics to derive points of departure for chemical risk assessment.   Archives of Toxicology. Springer, New York, NY, USA, 91(5): 2045-2065, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1505450",
-            "keyword": [
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "Alexander Hanf",
                 "hasEmail": "mailto:hanf.alexander@epa.gov"
             },
+            "description": "To determine the best way to select predictive groups of genes, we used published microarray data from dose-response studies on six chemicals in rats exposed orally for 5, 14, 28, and 90 days. We evaluated eight approaches for selecting genes for POD derivation and three previously proposed approaches (the lowest pathway BMD, and the mean and median BMD of all genes). This dataset is not publicly accessible because: The research which produced this data was not funded by EPA. The EPA coauthor helped write the manuscript. It can be accessed through the following means: Data generated by other authors. Format: N/A. \n\nThis dataset is associated with the following publication:\nFarmahin, R., A. Williams, B. Kuo, N.L. Chepelev, R.S. Thomas, T.S. Burton-Maclaren, I.H. Curran, A. Nong, M.G. Wade, and C.L. Yauk. (Archives of Toxicology) Recommended approaches in the application of toxicogenomics to derive points of departure for chemical risk assessment.   Archives of Toxicology. Springer, New York, NY, USA, 91(5): 2045-2065, (2017).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1505450",
+            "keyword": [
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-12-07",
-            "references": [
-                "https://doi.org/10.1007/s00204-016-1886-5"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103250,42 +103244,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s00204-016-1886-5"
+            ],
+            "rights": null,
+            "title": "(Archives of Toxicology) Recommended approaches in the application of toxicogenomics to derive points of departure for chemical risk assessment"
         },
         {
-            "title": "Energy and Emissions Implications of Automated Vehicles in the U.S. Energy System",
-            "description": "This data includes model results generated using the MARKAL model and the EPA_US_9r database. Several scenarios involving automated vehicles were modeled. Results include emissions, fuel use, and fuel production under a variety of regimes of vehicle automation. \n\nThis dataset is associated with the following publication:\nDodder, R. Energy and emissions implications of automated vehicles in the U.S. energy system - December 2019.   Transportation Research Part D: Transport and Environment. Elsevier BV, AMSTERDAM,  NETHERLANDS, 77: 132-147, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503410",
-            "keyword": [
-                "automated vehicles",
-                "transportation",
-                "energy",
-                "externality",
-                "energy modeling"
-            ],
             "contactPoint": {
                 "fn": "Kristen Brown",
                 "hasEmail": "mailto:brown.kristen@epa.gov"
             },
+            "description": "This data includes model results generated using the MARKAL model and the EPA_US_9r database. Several scenarios involving automated vehicles were modeled. Results include emissions, fuel use, and fuel production under a variety of regimes of vehicle automation. \n\nThis dataset is associated with the following publication:\nDodder, R. Energy and emissions implications of automated vehicles in the U.S. energy system - December 2019.   Transportation Research Part D: Transport and Environment. Elsevier BV, AMSTERDAM,  NETHERLANDS, 77: 132-147, (2019).",
             "distribution": [
                 {
-                    "title": "SciHub_AV.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503410/SciHub_AV.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub_AV.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503410",
+            "keyword": [
+                "automated vehicles",
+                "transportation",
+                "energy",
+                "externality",
+                "energy modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-14",
-            "references": [
-                "https://doi.org/10.1016/j.trd.2019.09.003"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103295,46 +103289,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.trd.2019.09.003"
+            ],
+            "rights": null,
+            "title": "Energy and Emissions Implications of Automated Vehicles in the U.S. Energy System"
         },
         {
-            "title": "Salt Marsh Soil Salinity Data",
-            "description": "Data used to evaluate the use of apparent conductivity of salt marsh sediments as a rapid alternative to traditional methods of salinity determination that can be used to map soil salinity across a marsh surface. \n\nThis dataset is associated with the following publication:\nMckinney, R., A. Hanson, R. Johnson, and M. Charpentier. Seasonal variation in apparent conductivity and soil salinity at two Narragansett Bay, RI salt marshes.   PeerJ. PeerJ Inc., Corte Madera, CA, USA, 7: e8074, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503163",
-            "keyword": [
-                "soil salinity",
-                "Salt marsh",
-                "apparent conductivity",
-                "porewater"
-            ],
             "contactPoint": {
                 "fn": "Richard McKinney",
                 "hasEmail": "mailto:mckinney.rick@epa.gov"
             },
+            "description": "Data used to evaluate the use of apparent conductivity of salt marsh sediments as a rapid alternative to traditional methods of salinity determination that can be used to map soil salinity across a marsh surface. \n\nThis dataset is associated with the following publication:\nMckinney, R., A. Hanson, R. Johnson, and M. Charpentier. Seasonal variation in apparent conductivity and soil salinity at two Narragansett Bay, RI salt marshes.   PeerJ. PeerJ Inc., Corte Madera, CA, USA, 7: e8074, (2019).",
             "distribution": [
                 {
-                    "title": "Salt Marsh Soil Salinity Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503163/Salt%20Marsh%20Soil%20Salinity%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Salt Marsh Soil Salinity Data.xlsx"
                 },
                 {
-                    "title": "A9064 Metadata.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503163/A9064%20Metadata.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "A9064 Metadata.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503163",
+            "keyword": [
+                "soil salinity",
+                "Salt marsh",
+                "apparent conductivity",
+                "porewater"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-11-09",
-            "references": [
-                "https://doi.org/10.7717/peerj.8074"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103344,96 +103338,96 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.7717/peerj.8074"
+            ],
+            "rights": null,
+            "title": "Salt Marsh Soil Salinity Data"
         },
         {
-            "title": "Exploring the General Equilibrium Costs of Sector-Specific Environmental Regulations",
-            "description": "Code and data to replicate simulations used in \"Exploring the General Equilibrium Costs of Sector-Specific Environmental Regulations\" by Alex Marten, Richard Garbaccio, and Ann Wolverton, in the Journal of the Association of Environmental and Resource Economists. Some of the data used in the modeling is proprietary and cannot be posted. We provide instructions for obtaining the remaining data and creating the datasets in readme.txt. (2019-05-24). Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1506126",
-            "keyword": [
-                "general equilibrium",
-                "regulation",
-                "social costs"
-            ],
             "contactPoint": {
                 "fn": "Alex Marten",
                 "hasEmail": "mailto:marten.alex@epa.gov"
             },
+            "description": "Code and data to replicate simulations used in \"Exploring the General Equilibrium Costs of Sector-Specific Environmental Regulations\" by Alex Marten, Richard Garbaccio, and Ann Wolverton, in the Journal of the Association of Environmental and Resource Economists. Some of the data used in the modeling is proprietary and cannot be posted. We provide instructions for obtaining the remaining data and creating the datasets in readme.txt. (2019-05-24). Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GOB7NW",
-                    "accessURL": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GOB7NW"
+                    "accessURL": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GOB7NW",
+                    "title": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GOB7NW"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1506126",
+            "keyword": [
+                "general equilibrium",
+                "regulation",
+                "social costs"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-26",
-            "references": [
-                "https://dx.doi.org/10.1086/705593"
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
+                "https://dx.doi.org/10.1086/705593"
+            ],
+            "rights": null,
+            "title": "Exploring the General Equilibrium Costs of Sector-Specific Environmental Regulations"
         },
         {
-            "title": "Nationwide Reconnaissance of Contaminants of Emerging Concern in Source and Treated Drinking Waters of the United States",
-            "description": "Files are an overview of all data acquired in the study examining source and treated drinking water. \n\nThis dataset is associated with the following publication:\nGlassmeyer , S., E. Furlong, D. Kolpin, A. Batt , B. Benson , S. Boone , O. Conerly , M. Donohue , D. King , M. Kostich , H. Mash , S. Pfaller , K. Schenck , J.E. Simmons , E. Varughese , S. Vesper , E. Villegas , and V. Wilson. Nationwide reconnaissance of contaminants of emerging concern in source and treated drinking waters of the United States.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 581582: 909-922, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1390088",
-            "keyword": [
-                "drinking water",
-                "source water",
-                "pharmaceuticals",
-                "microorganisms",
-                "Per- and polyfluoroalkyl substances"
-            ],
             "contactPoint": {
                 "fn": "Susan Glassmeyer",
                 "hasEmail": "mailto:glassmeyer.susan@epa.gov"
             },
+            "description": "Files are an overview of all data acquired in the study examining source and treated drinking water. \n\nThis dataset is associated with the following publication:\nGlassmeyer , S., E. Furlong, D. Kolpin, A. Batt , B. Benson , S. Boone , O. Conerly , M. Donohue , D. King , M. Kostich , H. Mash , S. Pfaller , K. Schenck , J.E. Simmons , E. Varughese , S. Vesper , E. Villegas , and V. Wilson. Nationwide reconnaissance of contaminants of emerging concern in source and treated drinking waters of the United States.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 581582: 909-922, (2017).",
             "distribution": [
                 {
-                    "title": "overview paper for science hub..xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390088/overview%20paper%20for%20science%20hub..xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "overview paper for science hub..xlsx"
                 },
                 {
-                    "title": "overview paper table 3 top.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390088/overview%20paper%20table%203%20top.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "overview paper table 3 top.xlsx"
                 },
                 {
-                    "title": "overview paper table 3 bottom.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390088/overview%20paper%20table%203%20bottom.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "overview paper table 3 bottom.xlsx"
                 },
                 {
-                    "title": "Phase I and II final data for Sci Hub and other distribution.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390088/Phase%20I%20and%20II%20final%20data%20for%20Sci%20Hub%20and%20other%20distribution.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Phase I and II final data for Sci Hub and other distribution.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390088",
+            "keyword": [
+                "drinking water",
+                "source water",
+                "pharmaceuticals",
+                "microorganisms",
+                "Per- and polyfluoroalkyl substances"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-05",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.12.004"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103443,19 +103437,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.12.004"
+            ],
+            "rights": null,
+            "title": "Nationwide Reconnaissance of Contaminants of Emerging Concern in Source and Treated Drinking Waters of the United States"
         },
         {
-            "title": "Assessing the Impact of Wastewater Treatment Plant Effluent on Downstream Drinking Water-Source Quality Using a Zebrafish (Danio Rerio) Liver Cell-Based Metabolomics Approach",
-            "description": "The datafile presents the data used to create the figures in the manuscript.  These include: a) Two-component score plots of hydrophilic and lipophilic ZFL cell extracts analyzed with NMR and GC-MS, respectively; b) The t-test filtered difference spectra (exposed minus control) generated from binned 1H NMR spectra (0.5\u20135.0\u202fppm in chemical shift) of hydrophilic extracts of ZFL cells; c) Bar chart showing the fold change of 21 annotated metabolites from the lipophilic extracts that exhibited different normalized abundance at one or more of the six sites relative to the control as measured by GC-MS; d) The summed intensity values for significantly changed metabolites from the t-test filtered difference spectra for both hydrophilic  and lipophilic extracts across six sampling sites; and e) Relative normalized abundances for metabolites identified in the cholesterol and fatty acid synthesis pathways from lipophilic ZFL extracts. \n\nThis dataset is associated with the following publication:\nZhen, H., D. Ekman, T. Collette, S. Glassmeyer, M. Mills, E. Furlong, D. Kolpin, and Q. Teng. Assessing the impact of wastewater treatment plant effluent on downstream drinking water-source quality using a zebrafish (Danio Rerio) liver cell-based metabolomics approach.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 145: 198-209, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Susan Glassmeyer",
+                "hasEmail": "mailto:glassmeyer.susan@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502544/documents/Data%20Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The datafile presents the data used to create the figures in the manuscript.  These include: a) Two-component score plots of hydrophilic and lipophilic ZFL cell extracts analyzed with NMR and GC-MS, respectively; b) The t-test filtered difference spectra (exposed minus control) generated from binned 1H NMR spectra (0.5\u20135.0\u202fppm in chemical shift) of hydrophilic extracts of ZFL cells; c) Bar chart showing the fold change of 21 annotated metabolites from the lipophilic extracts that exhibited different normalized abundance at one or more of the six sites relative to the control as measured by GC-MS; d) The summed intensity values for significantly changed metabolites from the t-test filtered difference spectra for both hydrophilic  and lipophilic extracts across six sampling sites; and e) Relative normalized abundances for metabolites identified in the cholesterol and fatty acid synthesis pathways from lipophilic ZFL extracts. \n\nThis dataset is associated with the following publication:\nZhen, H., D. Ekman, T. Collette, S. Glassmeyer, M. Mills, E. Furlong, D. Kolpin, and Q. Teng. Assessing the impact of wastewater treatment plant effluent on downstream drinking water-source quality using a zebrafish (Danio Rerio) liver cell-based metabolomics approach.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 145: 198-209, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502544/Datasets%20for%20WW2DW%20manuscript-Metabolomics-Athens-081418.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Datasets for WW2DW manuscript-Metabolomics-Athens-081418.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502544",
             "keyword": [
@@ -103469,20 +103475,10 @@
                 "drinking water",
                 "de facto reuse"
             ],
-            "contactPoint": {
-                "fn": "Susan Glassmeyer",
-                "hasEmail": "mailto:glassmeyer.susan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Datasets for WW2DW manuscript-Metabolomics-Athens-081418.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502544/Datasets%20for%20WW2DW%20manuscript-Metabolomics-Athens-081418.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-13",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2018.08.028"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103493,43 +103489,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502544/documents/Data%20Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.watres.2018.08.028"
+            ],
+            "rights": null,
+            "title": "Assessing the Impact of Wastewater Treatment Plant Effluent on Downstream Drinking Water-Source Quality Using a Zebrafish (Danio Rerio) Liver Cell-Based Metabolomics Approach"
         },
         {
-            "title": "Lead and iron speciation results",
-            "description": "The data set comprises of two tables the show the linear combination fitting results for lead and iron speciation in samples collected for the study.  The tables show the names of samples pre- and post-treatment and the relative abundance of various lead and iron species present in each sample. \n\nThis dataset is associated with the following publication:\nKastury, F., E. Smith, E. Doelsh, E. Lombi, M. Donnelley, P. Cmielewski, D.W. Parsons, K.G. Scheckel, D. Paterson, M.D. de Jonge, C. Herde, and A.L. Juhasz. In Vitro, in Vivo, and Spectroscopic Assessment of Lead Exposure Reduction via Ingestion and Inhalation Pathways Using Phosphate and Iron Amendments..   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(17): 10329-10341, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1503436",
-            "keyword": [
-                "lead contaminated soil",
-                "bioavailability",
-                "synchrotron speciation",
-                "lead immobilzation",
-                "Bioaccessibility Soil"
-            ],
             "contactPoint": {
                 "fn": "Kirk Scheckel",
                 "hasEmail": "mailto:scheckel.kirk@epa.gov"
             },
+            "description": "The data set comprises of two tables the show the linear combination fitting results for lead and iron speciation in samples collected for the study.  The tables show the names of samples pre- and post-treatment and the relative abundance of various lead and iron species present in each sample. \n\nThis dataset is associated with the following publication:\nKastury, F., E. Smith, E. Doelsh, E. Lombi, M. Donnelley, P. Cmielewski, D.W. Parsons, K.G. Scheckel, D. Paterson, M.D. de Jonge, C. Herde, and A.L. Juhasz. In Vitro, in Vivo, and Spectroscopic Assessment of Lead Exposure Reduction via Ingestion and Inhalation Pathways Using Phosphate and Iron Amendments..   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(17): 10329-10341, (2019).",
             "distribution": [
                 {
-                    "title": "Table2-PbLCF and TableS2-FeLCF.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503436/Table2-PbLCF%20and%20TableS2-FeLCF.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table2-PbLCF and TableS2-FeLCF.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503436",
+            "keyword": [
+                "lead contaminated soil",
+                "bioavailability",
+                "synchrotron speciation",
+                "lead immobilzation",
+                "Bioaccessibility Soil"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-22",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b02448"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103539,19 +103533,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b02448"
+            ],
+            "rights": null,
+            "title": "Lead and iron speciation results"
         },
         {
-            "title": "Dissolution of Silver Nanoparticles in Consumer Products: Effects of Particle Size and Capping Agent",
-            "description": "The data set contains the details on the characterization of silver nanoparticles suspension, the dissolution of silver nanoparticles in consumer products based on the dissolved mass Ag+ at deionized water and tap water and particle size fluctuations in deionized water and tap. Also contains a comparison of dissolution patterns between silver consumer products and laboratory-synthesized silver nanoparticles. \n\nThis dataset is associated with the following publication:\nRadwan, I.M., A. Gitipour, P.M. Potter, D.D. Dionysiou, and S.R. Al-Abed. Dissolution of silver nanoparticles in colloidal consumer products: effects of particle size and capping agent.   Journal of Nanoparticle Research. Springer SBM, New York, NY, USA, 21: 155, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Souhail Al-Abed",
+                "hasEmail": "mailto:al-abed.souhail@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502492/documents/data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The data set contains the details on the characterization of silver nanoparticles suspension, the dissolution of silver nanoparticles in consumer products based on the dissolved mass Ag+ at deionized water and tap water and particle size fluctuations in deionized water and tap. Also contains a comparison of dissolution patterns between silver consumer products and laboratory-synthesized silver nanoparticles. \n\nThis dataset is associated with the following publication:\nRadwan, I.M., A. Gitipour, P.M. Potter, D.D. Dionysiou, and S.R. Al-Abed. Dissolution of silver nanoparticles in colloidal consumer products: effects of particle size and capping agent.   Journal of Nanoparticle Research. Springer SBM, New York, NY, USA, 21: 155, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502492/raw%20data.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "raw data.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502492",
             "keyword": [
@@ -103562,20 +103568,10 @@
                 "particle size",
                 "capping agent"
             ],
-            "contactPoint": {
-                "fn": "Souhail Al-Abed",
-                "hasEmail": "mailto:al-abed.souhail@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "raw data.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502492/raw%20data.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-08",
-            "references": [
-                "https://doi.org/10.1007/s11051-019-4597-z"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103586,43 +103582,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502492/documents/data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1007/s11051-019-4597-z"
+            ],
+            "rights": null,
+            "title": "Dissolution of Silver Nanoparticles in Consumer Products: Effects of Particle Size and Capping Agent"
         },
         {
-            "title": "Nichols et al._Biotransformation of PAH mixures by trout liver S9 fractions",
-            "description": "This Excel spreadsheet provides data that appear in Tables 1- 2 and Figures 1-4 of the main document, as well as data that appear in Figures S1-S3 of the Supplementary Information. \n\nThis dataset is associated with the following publication:\nNichols, J., M. Ladd, A. Hoffman, and P. Fitzsimmons. Biotransformation of polycyclic aromatic hydrocarbons by trout liver S9 fractions:  Evaluation of competitive inhibition using a substrate depletion approach.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 38(12): 2729-2739, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503786",
-            "keyword": [
-                "biotransformation",
-                "polycyclic aromatic hydrocarbons",
-                "chemical mixtures",
-                "bioaccumulation",
-                "Competitive inhibition"
-            ],
             "contactPoint": {
                 "fn": "John Nichols",
                 "hasEmail": "mailto:nichols.john@epa.gov"
             },
+            "description": "This Excel spreadsheet provides data that appear in Tables 1- 2 and Figures 1-4 of the main document, as well as data that appear in Figures S1-S3 of the Supplementary Information. \n\nThis dataset is associated with the following publication:\nNichols, J., M. Ladd, A. Hoffman, and P. Fitzsimmons. Biotransformation of polycyclic aromatic hydrocarbons by trout liver S9 fractions:  Evaluation of competitive inhibition using a substrate depletion approach.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 38(12): 2729-2739, (2019).",
             "distribution": [
                 {
-                    "title": "In vitro mixture paper ScienceHub entry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503786/In%20vitro%20mixture%20paper%20ScienceHub%20entry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "In vitro mixture paper ScienceHub entry.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503786",
+            "keyword": [
+                "biotransformation",
+                "polycyclic aromatic hydrocarbons",
+                "chemical mixtures",
+                "bioaccumulation",
+                "Competitive inhibition"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-20",
-            "references": [
-                "https://doi.org/10.1002/etc.4595"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103632,50 +103626,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4595"
+            ],
+            "rights": null,
+            "title": "Nichols et al._Biotransformation of PAH mixures by trout liver S9 fractions"
         },
         {
-            "title": "ShahSanjivkumar_HS7-53-05-146_Data-Metadata-Rev_Ftularensis RVPCR Method_Manuscript_20190830",
-            "description": "This is a short communication manuscript entitled, \u201cRapid Viability (RV) PCR Protocol for Detection of Francisella tularensis\u201d to be published in a peer-reviewed journal. This pathogen survives for many days in the environment and water. It is a very slow growing pathogen and can take several days to detect using the traditional microbiological culture methods. Therefore, a high-throughput RV-PCR protocol was developed and optimized by the EPA ORD\u2019s National Homeland Security Research Center (NHSRC) to relatively rapidly detect F. tularensis. The RV-PCR method combines relatively shorter sample enrichment in growth media, and highly specific and sensitive PCR assay-based detection and identification of F. tularensis. Using this method, results can be obtained in 36 hours as compared to several days by the traditional microbiological culture methods. This manuscript contains summarized data from multiple experimental results to show the method performance in various experimental conditions mimicking a real-world interference material. The data has been extracted from the final report for the project on Optimization of a Rapid Viability (RV) PCR Protocol for Detection of Francisella tularensis in water. \n\nThis dataset is associated with the following publication:\nKane, S., S. Shah, and T. Alfaro. Rapid Viability Polymerase Chain Reaction Method for Detection of Francisella tularensis.   JOURNAL OF MICROBIOLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 166: ., (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
-            "identifier": "https://doi.org/10.23719/1504213",
-            "keyword": [
-                "Indoor/Outdoor Contamination",
-                "detection",
-                "Francisella tularensis",
-                "tularemia",
-                "Rapid Viability PCR",
-                "Water Samples",
-                "biological agent",
-                "non-spore-forming biological agent"
-            ],
             "contactPoint": {
                 "fn": "Sanjivkumar Shah",
                 "hasEmail": "mailto:shah.sanjiv@epa.gov"
             },
+            "description": "This is a short communication manuscript entitled, \u201cRapid Viability (RV) PCR Protocol for Detection of Francisella tularensis\u201d to be published in a peer-reviewed journal. This pathogen survives for many days in the environment and water. It is a very slow growing pathogen and can take several days to detect using the traditional microbiological culture methods. Therefore, a high-throughput RV-PCR protocol was developed and optimized by the EPA ORD\u2019s National Homeland Security Research Center (NHSRC) to relatively rapidly detect F. tularensis. The RV-PCR method combines relatively shorter sample enrichment in growth media, and highly specific and sensitive PCR assay-based detection and identification of F. tularensis. Using this method, results can be obtained in 36 hours as compared to several days by the traditional microbiological culture methods. This manuscript contains summarized data from multiple experimental results to show the method performance in various experimental conditions mimicking a real-world interference material. The data has been extracted from the final report for the project on Optimization of a Rapid Viability (RV) PCR Protocol for Detection of Francisella tularensis in water. \n\nThis dataset is associated with the following publication:\nKane, S., S. Shah, and T. Alfaro. Rapid Viability Polymerase Chain Reaction Method for Detection of Francisella tularensis.   JOURNAL OF MICROBIOLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 166: ., (2019).",
             "distribution": [
                 {
-                    "title": "ShahSanjivkumar_HS7-53-05-146_Data-Metadata-Rev_Ftularensis RVPCR Method_Manuscript_20190830.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504213/ShahSanjivkumar_HS7-53-05-146_Data-Metadata-Rev_Ftularensis%20RVPCR%20Method_Manuscript_20190830.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "ShahSanjivkumar_HS7-53-05-146_Data-Metadata-Rev_Ftularensis RVPCR Method_Manuscript_20190830.docx"
                 },
                 {
-                    "title": "Manuscript Draft_FT_RVPCR Method_ForSTICS_SShah_20190828.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504213/Manuscript%20Draft_FT_RVPCR%20Method_ForSTICS_SShah_20190828.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Manuscript Draft_FT_RVPCR Method_ForSTICS_SShah_20190828.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504213",
+            "keyword": [
+                "Indoor/Outdoor Contamination",
+                "detection",
+                "Francisella tularensis",
+                "tularemia",
+                "Rapid Viability PCR",
+                "Water Samples",
+                "biological agent",
+                "non-spore-forming biological agent"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-30",
-            "references": [
-                "https://doi.org/10.1016/j.mimet.2019.105738"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103685,42 +103679,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.mimet.2019.105738"
+            ],
+            "rights": null,
+            "title": "ShahSanjivkumar_HS7-53-05-146_Data-Metadata-Rev_Ftularensis RVPCR Method_Manuscript_20190830"
         },
         {
-            "title": "Impacts of fire smoke plumes on regional air quality, 2006\u20132013 data",
-            "description": "Impacts of fire smoke plumes on regional air quality, 2006\u20132013 data. Shape files of smoke plumes that define the geographic extent of smoke are from the NOAA Hazard Mapping System (HMS), and O3, total PM2.5, and PM2.5 constituent measurements for 2006\u20132013 are from the U.S. Environmental Protection Agency\u2019s (EPA) Air Quality System database. \n\nThis dataset is associated with the following publication:\nLarsen, A., B. Reich, M. Ruminski, and A. Rappold. Impacts of wildfire smoke plumes on regional air quality, 2006-2013.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 28(4): 319-327, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503903",
-            "keyword": [
-                "Fire Smoke",
-                "air quality",
-                "AQI",
-                "HMS"
-            ],
             "contactPoint": {
                 "fn": "Alexandra Larsen",
                 "hasEmail": "mailto:larsen.alexandra@epa.gov"
             },
+            "description": "Impacts of fire smoke plumes on regional air quality, 2006\u20132013 data. Shape files of smoke plumes that define the geographic extent of smoke are from the NOAA Hazard Mapping System (HMS), and O3, total PM2.5, and PM2.5 constituent measurements for 2006\u20132013 are from the U.S. Environmental Protection Agency\u2019s (EPA) Air Quality System database. \n\nThis dataset is associated with the following publication:\nLarsen, A., B. Reich, M. Ruminski, and A. Rappold. Impacts of wildfire smoke plumes on regional air quality, 2006-2013.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 28(4): 319-327, (2018).",
             "distribution": [
                 {
-                    "title": "Impact Fire Smoke Plumes Data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503903/Impact%20Fire%20Smoke%20Plumes%20Data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Impact Fire Smoke Plumes Data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503903",
+            "keyword": [
+                "Fire Smoke",
+                "air quality",
+                "AQI",
+                "HMS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-29",
-            "references": [
-                "https://doi.org/10.1038/s41370-017-0013-x",
-                "https://www.epa.gov/aqs/aqs-data-dictionary"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103730,20 +103723,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-017-0013-x",
+                "https://www.epa.gov/aqs/aqs-data-dictionary"
+            ],
+            "rights": null,
+            "title": "Impacts of fire smoke plumes on regional air quality, 2006\u20132013 data"
         },
         {
-            "title": "Dietary Lead and Phosphate Interactions Affect Oral Bioavailability of Soil Lead in the Mouse",
-            "description": "Dietary Lead and Phosphate Interactions Affect Oral Bioavailability of Soil Lead in the Mouse. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: In the publication and supporting information. Format: These data were generated from US EPA soil samples.  All of the soil samples were provided to NERL for methods development based on the agreement that the specific sample identifiers not be released. \n\nThis dataset is associated with the following publication:\nBradham, K., C. Nelson, G.L. Diamond, W.C. Thayer, K.G. Scheckel, M. Noerpel, K. Herbin-Davis, B. Elek, and D. Thomas. Dietary Lead and Phosphate Interactions Affect Oral Bioavailability of Soil Lead in the Mouse.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(21): 12556-12564, (2019).",
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
+                "fn": "Karen Bradham",
+                "hasEmail": "mailto:bradham.karen@epa.gov"
+            },
+            "description": "Dietary Lead and Phosphate Interactions Affect Oral Bioavailability of Soil Lead in the Mouse. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: In the publication and supporting information. Format: These data were generated from US EPA soil samples.  All of the soil samples were provided to NERL for methods development based on the agreement that the specific sample identifiers not be released. \n\nThis dataset is associated with the following publication:\nBradham, K., C. Nelson, G.L. Diamond, W.C. Thayer, K.G. Scheckel, M. Noerpel, K. Herbin-Davis, B. Elek, and D. Thomas. Dietary Lead and Phosphate Interactions Affect Oral Bioavailability of Soil Lead in the Mouse.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(21): 12556-12564, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1503450",
             "keyword": [
                 "lead",
@@ -103751,14 +103749,10 @@
                 "soil",
                 "bioavailability"
             ],
-            "contactPoint": {
-                "fn": "Karen Bradham",
-                "hasEmail": "mailto:bradham.karen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-01-28",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b02803"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103768,55 +103762,57 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b02803"
+            ],
+            "rights": null,
+            "title": "Dietary Lead and Phosphate Interactions Affect Oral Bioavailability of Soil Lead in the Mouse"
         },
         {
-            "title": "Assessing Dungeness River BMP Effectiveness Using an Ecological Function Approach",
-            "description": "These data sets contain specific biophysical data (information) on the Dungeness River located in Washington State (USA) near Sequim, Washington and very  near the Jamestown S'Klallam Indian Reservation.  Data include water quality, river flow rates, rain fall amounts and other observational data.  The years covered for these data sets are the 1920s to the present. \n\nThis dataset is associated with the following publication:\nHall, E., R. Hall, S. Swanson, W. Yee, D. Kozlowski, M. Philbin, D. Heggem, J. Lin, J. Aron, R. Schafer, D. Guiliano, and E. Wilson. Assessing Dungeness River Functionality and Effectiveness of Best Management Practices (BMPs) Using an Ecological Functional Approach.   American Journal of Environmental Engineering. Scientific & Academic Publishing, Rosemead, CA, USA, 9(2): 36-54, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1407630",
-            "keyword": [
-                "Dugeness River",
-                "water quality",
-                "best management practices",
-                "proper functioning condition",
-                "Tribal Sustainability",
-                "ecological condition assessment",
-                "Environmenal health",
-                "Ecological Health",
-                "Vulnerable Groups"
-            ],
             "contactPoint": {
                 "fn": "Daniel Heggem",
                 "hasEmail": "mailto:heggem.daniel@epa.gov"
             },
+            "description": "These data sets contain specific biophysical data (information) on the Dungeness River located in Washington State (USA) near Sequim, Washington and very  near the Jamestown S'Klallam Indian Reservation.  Data include water quality, river flow rates, rain fall amounts and other observational data.  The years covered for these data sets are the 1920s to the present. \n\nThis dataset is associated with the following publication:\nHall, E., R. Hall, S. Swanson, W. Yee, D. Kozlowski, M. Philbin, D. Heggem, J. Lin, J. Aron, R. Schafer, D. Guiliano, and E. Wilson. Assessing Dungeness River Functionality and Effectiveness of Best Management Practices (BMPs) Using an Ecological Functional Approach.   American Journal of Environmental Engineering. Scientific & Academic Publishing, Rosemead, CA, USA, 9(2): 36-54, (2019).",
             "distribution": [
                 {
-                    "title": "Dungeness_Rainfall.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407630/Dungeness_Rainfall.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dungeness_Rainfall.xlsx"
                 },
                 {
-                    "title": "Dungeness_storet_Results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407630/Dungeness_storet_Results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dungeness_storet_Results.xlsx"
                 },
                 {
-                    "title": "Dungeness_usgs_results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407630/Dungeness_usgs_results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dungeness_usgs_results.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407630",
+            "keyword": [
+                "Dugeness River",
+                "water quality",
+                "best management practices",
+                "proper functioning condition",
+                "Tribal Sustainability",
+                "ecological condition assessment",
+                "Environmenal health",
+                "Ecological Health",
+                "Vulnerable Groups"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-12",
-            "references": null,
+            "programCode": [
+                "020:097"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -103825,19 +103821,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Assessing Dungeness River BMP Effectiveness Using an Ecological Function Approach"
         },
         {
-            "title": "Childhood Chemical Exposures & ADHD",
-            "description": "Odds ratio statistics for ADHD outcomes and chemical exposures. \n\nThis dataset is associated with the following publication:\nNilsen, F., and N. Tulve. A systematic review and meta-analysis examining the interrelationships between chemical and non-chemical stressors and inherent characteristics in children with ADHD.   ENVIRONMENTAL RESEARCH. Elsevier B.V., Amsterdam,  NETHERLANDS, 180: 108884, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Frances Nilsen",
+                "hasEmail": "mailto:nilsen.frances@epa.gov"
+            },
+            "description": "Odds ratio statistics for ADHD outcomes and chemical exposures. \n\nThis dataset is associated with the following publication:\nNilsen, F., and N. Tulve. A systematic review and meta-analysis examining the interrelationships between chemical and non-chemical stressors and inherent characteristics in children with ADHD.   ENVIRONMENTAL RESEARCH. Elsevier B.V., Amsterdam,  NETHERLANDS, 180: 108884, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504060/Childhood%20Chemical%20Exposures%20ADHD_SciHub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Childhood Chemical Exposures ADHD_SciHub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504060",
             "keyword": [
@@ -103848,20 +103852,10 @@
                 "well-being",
                 "One Health"
             ],
-            "contactPoint": {
-                "fn": "Frances Nilsen",
-                "hasEmail": "mailto:nilsen.frances@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Childhood Chemical Exposures ADHD_SciHub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504060/Childhood%20Chemical%20Exposures%20ADHD_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-10",
-            "references": [
-                "https://doi.org/10.1016/j.envres.2019.108884"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103871,20 +103865,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envres.2019.108884"
+            ],
+            "rights": null,
+            "title": "Childhood Chemical Exposures & ADHD"
         },
         {
-            "title": "Automotive Surface Coating NESHAP Surveys",
-            "description": "Surveys asked vehicle manufacturers to identify what HAP abatement controls were already in place prior to the 2004 NESHAP and what controls were put in afterwards to comply, as well as the costs associated with compliance. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: It cannot, as it is CBI. Summary information for the dataset is available in the published article as well as a NCEE working paper. Format: The data are in written form via survey responses. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Maryann Wolverton",
+                "hasEmail": "mailto:wolverton.ann@epa.gov"
+            },
+            "description": "Surveys asked vehicle manufacturers to identify what HAP abatement controls were already in place prior to the 2004 NESHAP and what controls were put in afterwards to comply, as well as the costs associated with compliance. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: It cannot, as it is CBI. Summary information for the dataset is available in the published article as well as a NCEE working paper. Format: The data are in written form via survey responses. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1510322",
             "keyword": [
                 "vehicle manufacturing",
@@ -103892,55 +103890,51 @@
                 "NESHAP",
                 "compliance costs"
             ],
-            "contactPoint": {
-                "fn": "Maryann Wolverton",
-                "hasEmail": "mailto:wolverton.ann@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2013-09-25",
-            "references": [
-                "https://dx.doi.org/10.1017/bca.2018.25"
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
+                "https://dx.doi.org/10.1017/bca.2018.25"
+            ],
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "title": "Automotive Surface Coating NESHAP Surveys"
         },
         {
-            "title": "Pb LCF data for Port Pirie soil",
-            "description": "The dataset shows the distribution of lead phases (as weighted percentages) within a soil sample from Port Pirie (South Australia) determined from linear combination fitting of X-ray absorption spectroscopy data, along with LCF statistical error. \n\nThis dataset is associated with the following publication:\nKastury, F., E. Smith, E. Lombi, M.W. Donnelley, P.L. Cmielewski, D.W. Parsons, M. Noerpel, K.G. Scheckel, A.M. Kingston, G.R. Myers, D. Paterson, M.D. de Jonge, and A.L. Juhasz. Dynamics of Lead Bioavailability and Speciation in Indoor Dust and X-ray Spectroscopic Investigation of the Link between Ingestion and Inhalation Pathways.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(19): 11486-11495, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1503884",
-            "keyword": [
-                "lead speciation",
-                "metal bioavailability",
-                "contaminated dust",
-                "synchrotron speciation"
-            ],
             "contactPoint": {
                 "fn": "Kirk Scheckel",
                 "hasEmail": "mailto:scheckel.kirk@epa.gov"
             },
+            "description": "The dataset shows the distribution of lead phases (as weighted percentages) within a soil sample from Port Pirie (South Australia) determined from linear combination fitting of X-ray absorption spectroscopy data, along with LCF statistical error. \n\nThis dataset is associated with the following publication:\nKastury, F., E. Smith, E. Lombi, M.W. Donnelley, P.L. Cmielewski, D.W. Parsons, M. Noerpel, K.G. Scheckel, A.M. Kingston, G.R. Myers, D. Paterson, M.D. de Jonge, and A.L. Juhasz. Dynamics of Lead Bioavailability and Speciation in Indoor Dust and X-ray Spectroscopic Investigation of the Link between Ingestion and Inhalation Pathways.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(19): 11486-11495, (2019).",
             "distribution": [
                 {
-                    "title": "Table.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503884/Table.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503884",
+            "keyword": [
+                "lead speciation",
+                "metal bioavailability",
+                "contaminated dust",
+                "synchrotron speciation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-05",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b03249"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103950,42 +103944,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b03249"
+            ],
+            "rights": null,
+            "title": "Pb LCF data for Port Pirie soil"
         },
         {
-            "title": "Per- and Polyfluoroalkyl Substances in Source and Treated Drinking Waters of the United States",
-            "description": "Data are the source water and treated drinking water concentrations for 17 PFAS. \n\nThis dataset is associated with the following publication:\nBoone, J.S., C. Vigo, T. Boone, C. Byrne, J. Ferrario, B. Benson, J. Donohue, J. Simmons, D. Kolpin, E. Furlong, and S. Glassmeyer. Per- and polyfluoroalkyl substances in source and treated drinking waters of the United States..   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 653: 359-369, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500933",
-            "keyword": [
-                "drinking water",
-                "source water",
-                "pharmaceuticals",
-                "microorganisms",
-                "Per- and polyfluoroalkyl substances"
-            ],
             "contactPoint": {
                 "fn": "Susan Glassmeyer",
                 "hasEmail": "mailto:glassmeyer.susan@epa.gov"
             },
+            "description": "Data are the source water and treated drinking water concentrations for 17 PFAS. \n\nThis dataset is associated with the following publication:\nBoone, J.S., C. Vigo, T. Boone, C. Byrne, J. Ferrario, B. Benson, J. Donohue, J. Simmons, D. Kolpin, E. Furlong, and S. Glassmeyer. Per- and polyfluoroalkyl substances in source and treated drinking waters of the United States..   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 653: 359-369, (2019).",
             "distribution": [
                 {
-                    "title": "Boone et al tables and figures for Sci Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500933/Boone%20et%20al%20tables%20and%20figures%20for%20Sci%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Boone et al tables and figures for Sci Hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500933",
+            "keyword": [
+                "drinking water",
+                "source water",
+                "pharmaceuticals",
+                "microorganisms",
+                "Per- and polyfluoroalkyl substances"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-12-18",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2018.10.245"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -103995,20 +103989,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2018.10.245"
+            ],
+            "rights": null,
+            "title": "Per- and Polyfluoroalkyl Substances in Source and Treated Drinking Waters of the United States"
         },
         {
-            "title": "Distribution, variability, and predictors of urinary BPA levels in adults",
-            "description": "Distribution, variability, and predictors of urinary bisphenol A levels in adults. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: This data contains PII and can not be released. Format: Distribution, variability, and predictors of urinary bisphenol A levels in adults.  Data were collected from 50 adults within a 40-mile radius of Chapel Hill NC, thus the combination of data collected could be identified by individual participants or their family or close friends, so data cannot be released to the public ever. \n\nThis dataset is associated with the following publication:\nMorgan, M., M. Nash, D. Boyd Barr, J. Starr, M. Clifton, and J. Sobus. Distribution, Variability, and Predictors of Urinary Bisphenol-A Levels in 50 North Carolina Adults over a Six-Week Monitoring Period.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 112: 85-99, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Marsha Morgan",
+                "hasEmail": "mailto:morgan.marsha@epa.gov"
+            },
+            "description": "Distribution, variability, and predictors of urinary bisphenol A levels in adults. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: This data contains PII and can not be released. Format: Distribution, variability, and predictors of urinary bisphenol A levels in adults.  Data were collected from 50 adults within a 40-mile radius of Chapel Hill NC, thus the combination of data collected could be identified by individual participants or their family or close friends, so data cannot be released to the public ever. \n\nThis dataset is associated with the following publication:\nMorgan, M., M. Nash, D. Boyd Barr, J. Starr, M. Clifton, and J. Sobus. Distribution, Variability, and Predictors of Urinary Bisphenol-A Levels in 50 North Carolina Adults over a Six-Week Monitoring Period.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 112: 85-99, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1504169",
             "keyword": [
                 "Bisphenol A (BPA)",
@@ -104021,14 +104019,10 @@
                 "determinanats",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Marsha Morgan",
-                "hasEmail": "mailto:morgan.marsha@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-01-30",
-            "references": [
-                "https://doi.org/10.1016/j.envint.2017.12.014"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104038,20 +104032,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envint.2017.12.014"
+            ],
+            "rights": null,
+            "title": "Distribution, variability, and predictors of urinary BPA levels in adults"
         },
         {
-            "title": "Predictors of 3-PBA levels in adults",
-            "description": "Non-chemical stressors that impact urinary pyrethroid metabolite levels. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Data were collected from 50 adults within a 40-mile radius of Chapel Hill NC, thus the combination of data collected could be identified by individual participants or their family or close friends, so data cannot be released to the public ever. Format: Non-chemical stressors that impact urinary pyrethroid metabolite levels. Data were collected from 50 adults within a 40-mile radius of Chapel Hill NC, thus the combination of data collected could be identified by individual participants or their family or close friends, so data cannot be released to the public ever. \n\nThis dataset is associated with the following publication:\nMorgan, M., P. Jones, J. Sobus, and D. Boyd Barr. Predictors of Urinary 3-Phenoxybenzoic Acid Levels in 50 North Carolina Adults.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 13(11): 1172, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Marsha Morgan",
+                "hasEmail": "mailto:morgan.marsha@epa.gov"
+            },
+            "description": "Non-chemical stressors that impact urinary pyrethroid metabolite levels. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Data were collected from 50 adults within a 40-mile radius of Chapel Hill NC, thus the combination of data collected could be identified by individual participants or their family or close friends, so data cannot be released to the public ever. Format: Non-chemical stressors that impact urinary pyrethroid metabolite levels. Data were collected from 50 adults within a 40-mile radius of Chapel Hill NC, thus the combination of data collected could be identified by individual participants or their family or close friends, so data cannot be released to the public ever. \n\nThis dataset is associated with the following publication:\nMorgan, M., P. Jones, J. Sobus, and D. Boyd Barr. Predictors of Urinary 3-Phenoxybenzoic Acid Levels in 50 North Carolina Adults.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 13(11): 1172, (2016).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1504170",
             "keyword": [
                 "adults",
@@ -104061,14 +104059,10 @@
                 "urine",
                 "biomarkers"
             ],
-            "contactPoint": {
-                "fn": "Marsha Morgan",
-                "hasEmail": "mailto:morgan.marsha@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-06-01",
-            "references": [
-                "https://doi.org/10.3390/ijerph13111172"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104078,205 +104072,217 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ijerph13111172"
+            ],
+            "rights": null,
+            "title": "Predictors of 3-PBA levels in adults"
         },
         {
-            "title": "Data Center Energy Efficiency Focus Groups and Interviews",
-            "description": "The data include transcripts prepared from audio recordings of six focus groups and seven interviews with managers who made equipment purchase or maintenance decisions for one or more U.S. data centers. The focus groups were conducted in New York City, Dallas, and Boston, and the seven interviews were conducted by telephone. Focus groups and interviewers were conducted between October 2014 and June 2015. Also included are questionnaires completed by focus group and interview participants. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1506133",
-            "keyword": [
-                "energy efficiency paradox",
-                "market failures",
-                "data centers",
-                "focus groups"
-            ],
             "contactPoint": {
                 "fn": "Heather Klemick",
                 "hasEmail": "mailto:klemick.heather@epa.gov"
             },
+            "description": "The data include transcripts prepared from audio recordings of six focus groups and seven interviews with managers who made equipment purchase or maintenance decisions for one or more U.S. data centers. The focus groups were conducted in New York City, Dallas, and Boston, and the seven interviews were conducted by telephone. Focus groups and interviewers were conducted between October 2014 and June 2015. Also included are questionnaires completed by focus group and interview participants. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "Boston Data Center FG1 Transcript 06_02_15 10AM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Boston%20Data%20Center%20FG1%20Transcript%2006_02_15%2010AM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Boston Data Center FG1 Transcript 06_02_15 10AM.docx"
                 },
                 {
-                    "title": "Boston Data Center FG2 Transcript 06_02_15 1PM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Boston%20Data%20Center%20FG2%20Transcript%2006_02_15%201PM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Boston Data Center FG2 Transcript 06_02_15 1PM.docx"
                 },
                 {
-                    "title": "Boston Focus Group Questionnaires - Survey Monkey.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Boston%20Focus%20Group%20Questionnaires%20-%20Survey%20Monkey.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Boston Focus Group Questionnaires - Survey Monkey.pdf"
                 },
                 {
-                    "title": "Boston Focus Group Questionnaires - paper.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Boston%20Focus%20Group%20Questionnaires%20-%20paper.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Boston Focus Group Questionnaires - paper.pdf"
                 },
                 {
-                    "title": "Dallas Data Center FG1 Transcript 12_09_14 9AM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Dallas%20Data%20Center%20FG1%20Transcript%2012_09_14%209AM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Dallas Data Center FG1 Transcript 12_09_14 9AM.docx"
                 },
                 {
-                    "title": "Dallas Data Center FG2 Transcript 12_09_14.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Dallas%20Data%20Center%20FG2%20Transcript%2012_09_14.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Dallas Data Center FG2 Transcript 12_09_14.docx"
                 },
                 {
-                    "title": "Dallas Data Center FG1 Questionnaires.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Dallas%20Data%20Center%20FG1%20Questionnaires.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Dallas Data Center FG1 Questionnaires.pdf"
                 },
                 {
-                    "title": "Dallas Data Center FG2 Questionnaires.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Dallas%20Data%20Center%20FG2%20Questionnaires.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Dallas Data Center FG2 Questionnaires.pdf"
                 },
                 {
-                    "title": "NYC Data Center FG1 Questionnaire 7.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG1%20Questionnaire%207.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "NYC Data Center FG1 Questionnaire 7.pdf"
                 },
                 {
-                    "title": "NYC Data Center FG1 Transcript 03_17_15 11_28AM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG1%20Transcript%2003_17_15%2011_28AM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "NYC Data Center FG1 Transcript 03_17_15 11_28AM.docx"
                 },
                 {
-                    "title": "NYC Data Center FG1 Questionnaire 14.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG1%20Questionnaire%2014.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "NYC Data Center FG1 Questionnaire 14.pdf"
                 },
                 {
-                    "title": "NYC Data Center FG1 Questionnaire 1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG1%20Questionnaire%201.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "NYC Data Center FG1 Questionnaire 1.docx"
                 },
                 {
-                    "title": "NYC Data Center FG2 Questionnaire 9.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG2%20Questionnaire%209.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "NYC Data Center FG2 Questionnaire 9.docx"
                 },
                 {
-                    "title": "NYC Data Center FG2 Questionnaire 16.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG2%20Questionnaire%2016.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "NYC Data Center FG2 Questionnaire 16.pdf"
                 },
                 {
-                    "title": "NYC Data Center FG2 Transcript 03_17_15 3_31PM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG2%20Transcript%2003_17_15%203_31PM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "NYC Data Center FG2 Transcript 03_17_15 3_31PM.docx"
                 },
                 {
-                    "title": "NYC Data Center FG2 Questionnaire 15.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/NYC%20Data%20Center%20FG2%20Questionnaire%2015.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "NYC Data Center FG2 Questionnaire 15.pdf"
                 },
                 {
-                    "title": "Questionnaire data centers interviews dec4_2014 2_02pm.doc",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Questionnaire%20data%20centers%20interviews%20dec4_2014%202_02pm.doc",
-                    "mediaType": "application/msword"
+                    "mediaType": "application/msword",
+                    "title": "Questionnaire data centers interviews dec4_2014 2_02pm.doc"
                 },
                 {
-                    "title": "Questionnaire data centers interviews dec4_2014 8_52am.doc",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Questionnaire%20data%20centers%20interviews%20dec4_2014%208_52am.doc",
-                    "mediaType": "application/msword"
+                    "mediaType": "application/msword",
+                    "title": "Questionnaire data centers interviews dec4_2014 8_52am.doc"
                 },
                 {
-                    "title": "Questionnaire data centers interviews may13_2015.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Questionnaire%20data%20centers%20interviews%20may13_2015.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Questionnaire data centers interviews may13_2015.docx"
                 },
                 {
-                    "title": "Questionnaire data centers interviews nov5_2014.doc",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Questionnaire%20data%20centers%20interviews%20nov5_2014.doc",
-                    "mediaType": "application/msword"
+                    "mediaType": "application/msword",
+                    "title": "Questionnaire data centers interviews nov5_2014.doc"
                 },
                 {
-                    "title": "Questionnaire data centers interviews nov26_2014.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Questionnaire%20data%20centers%20interviews%20nov26_2014.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Questionnaire data centers interviews nov26_2014.docx"
                 },
                 {
-                    "title": "Questionnaire data centers interviews oct03_2014.doc",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Questionnaire%20data%20centers%20interviews%20oct03_2014.doc",
-                    "mediaType": "application/msword"
+                    "mediaType": "application/msword",
+                    "title": "Questionnaire data centers interviews oct03_2014.doc"
                 },
                 {
-                    "title": "Questionnaire data centers interviews nov7_2014.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Questionnaire%20data%20centers%20interviews%20nov7_2014.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Questionnaire data centers interviews nov7_2014.pdf"
                 },
                 {
-                    "title": "Data Center Interview Transcript dec4_2014 2_02pm.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Data%20Center%20Interview%20Transcript%20dec4_2014%202_02pm.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Center Interview Transcript dec4_2014 2_02pm.docx"
                 },
                 {
-                    "title": "Data Center Interview Transcript dec4_2014 8_52am.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Data%20Center%20Interview%20Transcript%20dec4_2014%208_52am.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Center Interview Transcript dec4_2014 8_52am.docx"
                 },
                 {
-                    "title": "Data Center Interview Transcript may13_2015.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Data%20Center%20Interview%20Transcript%20may13_2015.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Center Interview Transcript may13_2015.docx"
                 },
                 {
-                    "title": "Data Center Interview Transcript nov5_2014.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Data%20Center%20Interview%20Transcript%20nov5_2014.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Center Interview Transcript nov5_2014.docx"
                 },
                 {
-                    "title": "Data Center Interview Transcript nov7_2014.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Data%20Center%20Interview%20Transcript%20nov7_2014.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Center Interview Transcript nov7_2014.docx"
                 },
                 {
-                    "title": "Data Center Interview Transcript nov26_2014.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Data%20Center%20Interview%20Transcript%20nov26_2014.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Center Interview Transcript nov26_2014.docx"
                 },
                 {
-                    "title": "Data Center Interview Transcript oct3_2014.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506133/Data%20Center%20Interview%20Transcript%20oct3_2014.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data Center Interview Transcript oct3_2014.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1506133",
+            "keyword": [
+                "energy efficiency paradox",
+                "market failures",
+                "data centers",
+                "focus groups"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-07",
-            "references": [
-                "https://dx.doi.org/10.1007/s12053-019-09782-2"
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
+                "https://dx.doi.org/10.1007/s12053-019-09782-2"
+            ],
+            "rights": null,
+            "title": "Data Center Energy Efficiency Focus Groups and Interviews"
         },
         {
-            "title": "NOx RACT and power plant employment",
-            "description": "Data on NOx RACT, ozone nonattainment, and power plant employment, and program files used in:\nGlenn Sheriff, Ann E. Ferris, and Ronald J. Shadbegian, \"How Did Air Quality Standards Affect Employment at US Power Plants? The Importance of Timing, Geography, and Stringency,\" Journal of the Association of Environmental and Resource Economists 6, no. 1 (January 2019): 111-149. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Ann Ferris",
+                "hasEmail": "mailto:ferris.ann@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1506073/documents/readme%20JAERE%20article%20Sheriff_Ferris_Shadbegian.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Data on NOx RACT, ozone nonattainment, and power plant employment, and program files used in:\nGlenn Sheriff, Ann E. Ferris, and Ronald J. Shadbegian, \"How Did Air Quality Standards Affect Employment at US Power Plants? The Importance of Timing, Geography, and Stringency,\" Journal of the Association of Environmental and Resource Economists 6, no. 1 (January 2019): 111-149. Citation information for this dataset can be found in the EDG's Metadata Reference Information section and Data.gov's References section.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506073/NOxRACT_power_plant_employment.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "NOxRACT_power_plant_employment.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1506073",
             "keyword": [
@@ -104287,20 +104293,10 @@
                 "NOx RACT",
                 "ozone nonattainment"
             ],
-            "contactPoint": {
-                "fn": "Ann Ferris",
-                "hasEmail": "mailto:ferris.ann@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "NOxRACT_power_plant_employment.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506073/NOxRACT_power_plant_employment.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-12",
-            "references": [
-                "https://dx.doi.org/10.1086/700929"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. Environmental Protection Agency",
@@ -104308,86 +104304,84 @@
                     "name": "U.S. Government"
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1506073/documents/readme%20JAERE%20article%20Sheriff_Ferris_Shadbegian.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://dx.doi.org/10.1086/700929"
+            ],
+            "rights": null,
+            "title": "NOx RACT and power plant employment"
         },
         {
-            "title": "An integrated agriculture, atmosphere, and hydrology modeling system for ecosystem assessments",
-            "description": "Human activities such as agricultural fertilization and fossil fuel combustion have introduced a massive amount of anthropogenic nitrogen (N) in reactive forms to the environment. As agricultural fertilization is the single largest anthropogenic N source, an integrated approach to understand the interactions among agriculture, atmosphere, and hydrology is essential in examining human-altered N cycling. We have developed an integrated modeling system with agriculture EPIC, atmosphere WRF/CMAQ, and hydrology SWAT. This integrated system is useful tool for scientists and policy-makers to answer many questions on cycling of water, carbon, and nutrients for sustaining the food production while protecting the environment. \n\nThis dataset is associated with the following publication:\nRan, L., Y. Yuan, E. Cooter, V. Benson, J. Pleim, R. Wang, and J. Williams. An Integrated Agriculture, Atmosphere, and Hydrology Modeling System for Ecosystem Assessments.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 11(12): 4645-4668, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504283",
-            "keyword": [
-                "IMS",
-                "FEST-C",
-                "EPIC",
-                "WRF-CMAQ",
-                "SWAT",
-                "nitrogen cycling",
-                "air quality",
-                "SWAT water quality"
-            ],
             "contactPoint": {
                 "fn": "Limei Ran",
                 "hasEmail": "mailto:ran.limei@epa.gov"
             },
+            "description": "Human activities such as agricultural fertilization and fossil fuel combustion have introduced a massive amount of anthropogenic nitrogen (N) in reactive forms to the environment. As agricultural fertilization is the single largest anthropogenic N source, an integrated approach to understand the interactions among agriculture, atmosphere, and hydrology is essential in examining human-altered N cycling. We have developed an integrated modeling system with agriculture EPIC, atmosphere WRF/CMAQ, and hydrology SWAT. This integrated system is useful tool for scientists and policy-makers to answer many questions on cycling of water, carbon, and nutrients for sustaining the food production while protecting the environment. \n\nThis dataset is associated with the following publication:\nRan, L., Y. Yuan, E. Cooter, V. Benson, J. Pleim, R. Wang, and J. Williams. An Integrated Agriculture, Atmosphere, and Hydrology Modeling System for Ecosystem Assessments.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 11(12): 4645-4668, (2019).",
             "distribution": [
                 {
-                    "title": "CMAQ_fig3b_CMAQv53_bidi_rs1_NH4_dep_NADP_spatial.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/CMAQ_fig3b_CMAQv53_bidi_rs1_NH4_dep_NADP_spatial.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CMAQ_fig3b_CMAQv53_bidi_rs1_NH4_dep_NADP_spatial.xlsx"
                 },
                 {
-                    "title": "CMAQ_fig12_AMON_NH3_scatter_plot_April_to_Sept_2011.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/CMAQ_fig12_AMON_NH3_scatter_plot_April_to_Sept_2011.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CMAQ_fig12_AMON_NH3_scatter_plot_April_to_Sept_2011.xlsx"
                 },
                 {
-                    "title": "CMAQ_fig13a_monthly_mean_NH4_dep.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/CMAQ_fig13a_monthly_mean_NH4_dep.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CMAQ_fig13a_monthly_mean_NH4_dep.xlsx"
                 },
                 {
-                    "title": "CMAQ_figs2_sndep_5yr_average.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/CMAQ_figs2_sndep_5yr_average.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CMAQ_figs2_sndep_5yr_average.xlsx"
                 },
                 {
-                    "title": "EPIC_fig3_table.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/EPIC_fig3_table.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPIC_fig3_table.xlsx"
                 },
                 {
-                    "title": "SWAT_fig15_Model_Performance_Evaluation_2010_2013_final_correct.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/SWAT_fig15_Model_Performance_Evaluation_2010_2013_final_correct.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SWAT_fig15_Model_Performance_Evaluation_2010_2013_final_correct.xlsx"
                 },
                 {
-                    "title": "EPIC_fig7_usgs_IGRA_2010_app_FIPS_Freqcounty.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/EPIC_fig7_usgs_IGRA_2010_app_FIPS_Freqcounty.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPIC_fig7_usgs_IGRA_2010_app_FIPS_Freqcounty.xlsx"
                 },
                 {
-                    "title": "EPIC_fig11_usgs_fert_2011_plot.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/EPIC_fig11_usgs_fert_2011_plot.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPIC_fig11_usgs_fert_2011_plot.xlsx"
                 },
                 {
-                    "title": "EPIC_run_summary_plots_2010_2011_2012.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504283/EPIC_run_summary_plots_2010_2011_2012.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPIC_run_summary_plots_2010_2011_2012.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504283",
+            "keyword": [
+                "IMS",
+                "FEST-C",
+                "EPIC",
+                "WRF-CMAQ",
+                "SWAT",
+                "nitrogen cycling",
+                "air quality",
+                "SWAT water quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-04",
-            "references": [
-                "https://doi.org/10.1029/2019ms001708"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104397,41 +104391,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2019ms001708"
+            ],
+            "rights": null,
+            "title": "An integrated agriculture, atmosphere, and hydrology modeling system for ecosystem assessments"
         },
         {
-            "title": "Characterization of M4 Carbine Rifle Emissions with Three Ammunition Types ARL paper 02 13 19",
-            "description": "Data for figures in paper that show emissions by ammunition type and time. \n\nThis dataset is associated with the following publication:\nAurell, J., A. Holder, B. Gullett, K. McNesby, and J. Weinstein. Characterization of M4 Carbine Rifle Emissions With Three Ammunition Types.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 254: 254, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504527",
-            "keyword": [
-                "rifle",
-                "emissions",
-                "firing",
-                "ammunition"
-            ],
             "contactPoint": {
                 "fn": "Brian Gullett",
                 "hasEmail": "mailto:gullett.brian@epa.gov"
             },
+            "description": "Data for figures in paper that show emissions by ammunition type and time. \n\nThis dataset is associated with the following publication:\nAurell, J., A. Holder, B. Gullett, K. McNesby, and J. Weinstein. Characterization of M4 Carbine Rifle Emissions With Three Ammunition Types.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 254: 254, (2019).",
             "distribution": [
                 {
-                    "title": "Data Set for Sci Hub ARL paper 02 13 19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504527/Data%20Set%20for%20Sci%20Hub%20ARL%20paper%2002%2013%2019.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Set for Sci Hub ARL paper 02 13 19.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504527",
+            "keyword": [
+                "rifle",
+                "emissions",
+                "firing",
+                "ammunition"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-13",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2019.112982"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104441,19 +104435,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2019.112982"
+            ],
+            "rights": null,
+            "title": "Characterization of M4 Carbine Rifle Emissions with Three Ammunition Types ARL paper 02 13 19"
         },
         {
-            "title": "PACOM DATA SET Gasifier Municipal Batch Emissions",
-            "description": "This dataset reports a variety of emissions from operation of a batch-fed waste gasifier with a combustor. \n\nThis dataset is associated with the following publication:\nAurell, J., M. Barnes, B. Gullett, A. Holder, and R. Eninger. Methodology for Characterizing Emissions from Small (0.5-2 MTD) Batch-Fed Gasification Systems Using Multiple Waste Compositions.   WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 87: 398-406, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Brian Gullett",
+                "hasEmail": "mailto:gullett.brian@epa.gov"
+            },
+            "description": "This dataset reports a variety of emissions from operation of a batch-fed waste gasifier with a combustor. \n\nThis dataset is associated with the following publication:\nAurell, J., M. Barnes, B. Gullett, A. Holder, and R. Eninger. Methodology for Characterizing Emissions from Small (0.5-2 MTD) Batch-Fed Gasification Systems Using Multiple Waste Compositions.   WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 87: 398-406, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503073/Data%20Set%20PaCOM%20paper.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Set PaCOM paper.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503073",
             "keyword": [
@@ -104465,20 +104469,10 @@
                 "municipal",
                 "waste composition"
             ],
-            "contactPoint": {
-                "fn": "Brian Gullett",
-                "hasEmail": "mailto:gullett.brian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data Set PaCOM paper.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503073/Data%20Set%20PaCOM%20paper.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-19",
-            "references": [
-                "https://doi.org/10.1016/j.wasman.2019.02.031"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104488,41 +104482,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.wasman.2019.02.031"
+            ],
+            "rights": null,
+            "title": "PACOM DATA SET Gasifier Municipal Batch Emissions"
         },
         {
-            "title": "Great Lakes fauna inventory as of 20 May 2019",
-            "description": "Dataset is an Excel file with 6 tabs as follows:\n1) Changelog: Documentation of additions and changes to file since its creation\n2) Citations: Listing of citations with full references used in other 4 tabs\n3-6) Fish, Herps, Zoops, Benthos: For each of these 4 groups, a listing where rows are unique taxa and columns are the attributes recorded for them as described in the journal manuscript. \n\nThis dataset is associated with the following publication:\nTrebitz, A., M. Sykes, and J. Barge. A reference inventory for aquatic fauna of the Laurentian Great Lakes.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 45(6): 1036-1046, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503853",
-            "keyword": [
-                "biodiversity",
-                "species occurrence",
-                "taxonomic literature",
-                "Great Lakes"
-            ],
             "contactPoint": {
                 "fn": "Anett Trebitz",
                 "hasEmail": "mailto:trebitz.anett@epa.gov"
             },
+            "description": "Dataset is an Excel file with 6 tabs as follows:\n1) Changelog: Documentation of additions and changes to file since its creation\n2) Citations: Listing of citations with full references used in other 4 tabs\n3-6) Fish, Herps, Zoops, Benthos: For each of these 4 groups, a listing where rows are unique taxa and columns are the attributes recorded for them as described in the journal manuscript. \n\nThis dataset is associated with the following publication:\nTrebitz, A., M. Sykes, and J. Barge. A reference inventory for aquatic fauna of the Laurentian Great Lakes.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 45(6): 1036-1046, (2019).",
             "distribution": [
                 {
-                    "title": "GLfaunainventory_forSciHub_20May2019.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503853/GLfaunainventory_forSciHub_20May2019.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GLfaunainventory_forSciHub_20May2019.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503853",
+            "keyword": [
+                "biodiversity",
+                "species occurrence",
+                "taxonomic literature",
+                "Great Lakes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-20",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2019.10.004"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104532,57 +104526,57 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2019.10.004"
+            ],
+            "rights": null,
+            "title": "Great Lakes fauna inventory as of 20 May 2019"
         },
         {
-            "title": "State-Level Drivers of Future Fine Particulate Matter Mortality in the United States",
-            "description": "Future fine particulate matter (PM2.5) concentrations and health impacts will be largely determined by factors such as energy use, fuel choices, emission controls, state and national policies, and demographics. In this study, a human-earth system model is used to estimate US state-level PM2.5 mortality costs from 2015 to 2050 considering current major air quality and energy regulations. The Logarithmic Mean Divisia Index is applied to quantify the contributions of socioeconomic and energy factors to future changes in PM2.5 mortality costs. National PM2.5 mortality costs are estimated to decrease by 25% from 2015 to 2050, primarily driven by decreases in energy intensity and decreases in PM2.5 mortality cost per unit consumption of electric sector coal and transportation liquids. These factors together contribute to 68% of the net decrease, primarily because of technology improvements and air pollutant emission regulations. Furthermore, the results suggest that states with greater population and economic growth, but with fewer clean energy resources, are more likely to face significant challenges in reducing future PM2.5 mortality costs. In contrast, states with larger projected decreases in mortality costs have smaller increases in population and per capita GDP and greater decreases in electric sector coal share and PM2.5 mortality cost per unit fuel consumption. \nThis dataset includes source code, input data, and model output from the Global Change Assessment Model (GCAM-USA) human-earth system model used in this study. It also includes Excel workbooks and R scripts used in producing the figures in the manuscript. \n\nThis dataset is associated with the following publication:\nOu, Y., S. Smith, J.J. West, C. Nolte, and D. Loughlin. State-level drivers of future fine particulate matter mortality in the United States..   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 14(12): 124071, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503444",
-            "keyword": [
-                "fine particulate matter (PM2.5)",
-                "emissions",
-                "air quality",
-                "GCAM-USA",
-                "integrated assessment modeling"
-            ],
             "contactPoint": {
                 "fn": "Christopher Nolte",
                 "hasEmail": "mailto:nolte.chris@epa.gov"
             },
+            "description": "Future fine particulate matter (PM2.5) concentrations and health impacts will be largely determined by factors such as energy use, fuel choices, emission controls, state and national policies, and demographics. In this study, a human-earth system model is used to estimate US state-level PM2.5 mortality costs from 2015 to 2050 considering current major air quality and energy regulations. The Logarithmic Mean Divisia Index is applied to quantify the contributions of socioeconomic and energy factors to future changes in PM2.5 mortality costs. National PM2.5 mortality costs are estimated to decrease by 25% from 2015 to 2050, primarily driven by decreases in energy intensity and decreases in PM2.5 mortality cost per unit consumption of electric sector coal and transportation liquids. These factors together contribute to 68% of the net decrease, primarily because of technology improvements and air pollutant emission regulations. Furthermore, the results suggest that states with greater population and economic growth, but with fewer clean energy resources, are more likely to face significant challenges in reducing future PM2.5 mortality costs. In contrast, states with larger projected decreases in mortality costs have smaller increases in population and per capita GDP and greater decreases in electric sector coal share and PM2.5 mortality cost per unit fuel consumption. \nThis dataset includes source code, input data, and model output from the Global Change Assessment Model (GCAM-USA) human-earth system model used in this study. It also includes Excel workbooks and R scripts used in producing the figures in the manuscript. \n\nThis dataset is associated with the following publication:\nOu, Y., S. Smith, J.J. West, C. Nolte, and D. Loughlin. State-level drivers of future fine particulate matter mortality in the United States..   Environmental Research Letters. IOP Publishing LIMITED, Bristol,  UK, 14(12): 124071, (2019).",
             "distribution": [
                 {
-                    "title": "README.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503444/README.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "README.txt"
                 },
                 {
-                    "title": "results.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503444/results.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "results.zip"
                 },
                 {
-                    "title": "EASIUR-input.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503444/EASIUR-input.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "EASIUR-input.zip"
                 },
                 {
-                    "title": "gcam-usa.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503444/gcam-usa.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "gcam-usa.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503444",
+            "keyword": [
+                "fine particulate matter (PM2.5)",
+                "emissions",
+                "air quality",
+                "GCAM-USA",
+                "integrated assessment modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-12",
-            "references": [
-                "https://doi.org/10.1088/1748-9326/ab59cb"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104592,19 +104586,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1748-9326/ab59cb"
+            ],
+            "rights": null,
+            "title": "State-Level Drivers of Future Fine Particulate Matter Mortality in the United States"
         },
         {
-            "title": "Data for Turley et al. \"Applying the RISK21 approach to assess predictivity of new approach methodologies...\"",
-            "description": "Data for publication Turley et al. \"Applying the RISK21 approach to assess predictivity of new approach methodologies in toxicity testing and exposure assessment: a case study on food contact chemicals\".  Includes food concentration predictions from the model of Biryol et al. (2017) and SHEDS-HT exposure predictions. \n\nThis dataset is associated with the following publication:\nTurley, A., K. Isaacs, B. Wetmore, A. Karmaus, M. Embry, and M. Krishan. Incorporating new approach methodologies in toxicity testing and exposure assessment for tiered risk assessment using the RISK21 approach: Case studies on food contact chemicals.   FOOD AND CHEMICAL TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 134: 110819, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Kristin Isaacs",
+                "hasEmail": "mailto:isaacs.kristin@epa.gov"
+            },
+            "description": "Data for publication Turley et al. \"Applying the RISK21 approach to assess predictivity of new approach methodologies in toxicity testing and exposure assessment: a case study on food contact chemicals\".  Includes food concentration predictions from the model of Biryol et al. (2017) and SHEDS-HT exposure predictions. \n\nThis dataset is associated with the following publication:\nTurley, A., K. Isaacs, B. Wetmore, A. Karmaus, M. Embry, and M. Krishan. Incorporating new approach methodologies in toxicity testing and exposure assessment for tiered risk assessment using the RISK21 approach: Case studies on food contact chemicals.   FOOD AND CHEMICAL TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 134: 110819, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503448/Turleyetal_for_sciencehub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Turleyetal_for_sciencehub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503448",
             "keyword": [
@@ -104616,20 +104620,10 @@
                 "ExpoCast",
                 "SHEDS"
             ],
-            "contactPoint": {
-                "fn": "Kristin Isaacs",
-                "hasEmail": "mailto:isaacs.kristin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Turleyetal_for_sciencehub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503448/Turleyetal_for_sciencehub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-07",
-            "references": [
-                "https://doi.org/10.1016/j.fct.2019.110819"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104639,42 +104633,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.fct.2019.110819"
+            ],
+            "rights": null,
+            "title": "Data for Turley et al. \"Applying the RISK21 approach to assess predictivity of new approach methodologies...\""
         },
         {
-            "title": "Use of qPCR and RT-qPCR for Monitoring Variations of Microcystin Producers and Early Warning Their Toxin Production in an Ohio Inland Lake",
-            "description": "qPCR and RT-qPCR. \n\nThis dataset is associated with the following publication:\nLu, J., I. Struewing, L. Wymer, D. Tettenhorst, J. Shoemaker, and J. Allen. Use of qPCR and RT-qPCR for monitoring variations of microcystin producers and as an early warning system to predict toxin production in an Ohio inland lake.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 170: 115262, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503449",
-            "keyword": [
-                "microcystin",
-                "Microcystis",
-                "harmful algal bloom",
-                "early warning",
-                "qPCR/RT-qPCR"
-            ],
             "contactPoint": {
                 "fn": "Jingrang Lu",
                 "hasEmail": "mailto:lu.jingrang@epa.gov"
             },
+            "description": "qPCR and RT-qPCR. \n\nThis dataset is associated with the following publication:\nLu, J., I. Struewing, L. Wymer, D. Tettenhorst, J. Shoemaker, and J. Allen. Use of qPCR and RT-qPCR for monitoring variations of microcystin producers and as an early warning system to predict toxin production in an Ohio inland lake.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 170: 115262, (2020).",
             "distribution": [
                 {
-                    "title": "qPCR_Dataset.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503449/qPCR_Dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "qPCR_Dataset.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503449",
+            "keyword": [
+                "microcystin",
+                "Microcystis",
+                "harmful algal bloom",
+                "early warning",
+                "qPCR/RT-qPCR"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-25",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2019.115262"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104684,42 +104678,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2019.115262"
+            ],
+            "rights": null,
+            "title": "Use of qPCR and RT-qPCR for Monitoring Variations of Microcystin Producers and Early Warning Their Toxin Production in an Ohio Inland Lake"
         },
         {
-            "title": "Optimizing hydrologic performance of green roof media data set",
-            "description": "Moisture holding capacity and other hydrologic attributes of various green roof planting substrates. \n\nThis dataset is associated with the following publication:\nBollman, M., G. DeSantis, R. DuChanois, M. Etten-Bohm, D. Olszyk, J. Lambrinos, and P. Mayer. A Framework for optimizing hydrologic performance of green roof media.   ECOLOGICAL ENGINEERING. Elsevier Science Ltd, New York, NY, USA, 140: 105589, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1502546",
-            "keyword": [
-                "water holding capacity",
-                "plant growth media",
-                "Green Infrastructure",
-                "stormwater management",
-                "green roof design"
-            ],
             "contactPoint": {
                 "fn": "Michael Bollman",
                 "hasEmail": "mailto:bollman.mike@epa.gov"
             },
+            "description": "Moisture holding capacity and other hydrologic attributes of various green roof planting substrates. \n\nThis dataset is associated with the following publication:\nBollman, M., G. DeSantis, R. DuChanois, M. Etten-Bohm, D. Olszyk, J. Lambrinos, and P. Mayer. A Framework for optimizing hydrologic performance of green roof media.   ECOLOGICAL ENGINEERING. Elsevier Science Ltd, New York, NY, USA, 140: 105589, (2019).",
             "distribution": [
                 {
-                    "title": "A framework for optimizing hydrologic performance of green roof media_Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502546/A%20framework%20for%20optimizing%20hydrologic%20performance%20of%20green%20roof%20media_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "A framework for optimizing hydrologic performance of green roof media_Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502546",
+            "keyword": [
+                "water holding capacity",
+                "plant growth media",
+                "Green Infrastructure",
+                "stormwater management",
+                "green roof design"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-02",
-            "references": [
-                "https://doi.org/10.1016/j.ecoleng.2019.105589"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104729,19 +104723,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecoleng.2019.105589"
+            ],
+            "rights": null,
+            "title": "Optimizing hydrologic performance of green roof media data set"
         },
         {
-            "title": "SCCWRP - STREAM CLASSIFICATION AND PRIORITY EXPLORER",
-            "description": "The data contain information on the biological condition of streams within California as well as geospatial/field indicators of watershed or water quality. \n\nThis dataset is associated with the following publication:\nBeck, M., R. Mazor, S. Johnson, K. Wisenbaker, J. Westfall, P. Ode, R. Hill, C. Loflen, M. Sutula, and E. Stein. Prioritizing management goals for stream biological integrity within the developed landscape context.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  38(4): 883-898, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Ryan Hill",
+                "hasEmail": "mailto:hill.ryan@epa.gov"
+            },
+            "description": "The data contain information on the biological condition of streams within California as well as geospatial/field indicators of watershed or water quality. \n\nThis dataset is associated with the following publication:\nBeck, M., R. Mazor, S. Johnson, K. Wisenbaker, J. Westfall, P. Ode, R. Hill, C. Loflen, M. Sutula, and E. Stein. Prioritizing management goals for stream biological integrity within the developed landscape context.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  38(4): 883-898, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://zenodo.org/record/1218121#.XeVW1uhKg-V",
+                    "title": "https://zenodo.org/record/1218121#.XeVW1uhKg-V"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1506090",
             "keyword": [
@@ -104756,19 +104759,10 @@
                 "data visualization",
                 "stakeholder group"
             ],
-            "contactPoint": {
-                "fn": "Ryan Hill",
-                "hasEmail": "mailto:hill.ryan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://zenodo.org/record/1218121#.XeVW1uhKg-V",
-                    "accessURL": "https://zenodo.org/record/1218121#.XeVW1uhKg-V"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-13",
-            "references": [
-                "https://doi.org/10.1086/705996"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104778,70 +104772,72 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1086/705996"
+            ],
+            "rights": null,
+            "title": "SCCWRP - STREAM CLASSIFICATION AND PRIORITY EXPLORER"
         },
         {
-            "title": "Hydrologic landscape groundwater modeling input parameters and results",
-            "description": "The files and data included in this archive allow readers to inspect and reproduce the model results reported in Neff et al. (2020). Please refer to the included ReadMe file for a further explanation of individual files and step-by-step instructions for running the models.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1504529",
-            "keyword": [
-                "streams",
-                "catchments",
-                "watersheds",
-                "watershed metrics",
-                "National Hydrography Dataset",
-                "National Hydrography Dataset Plus (NHDPlus)",
-                "spatial prediction",
-                "aquatic condition",
-                "National Aquatic Resource Surveys"
-            ],
             "contactPoint": {
                 "fn": "Scott Leibowitz",
                 "hasEmail": "mailto:leibowitz.scott@epa.gov"
             },
+            "description": "The files and data included in this archive allow readers to inspect and reproduce the model results reported in Neff et al. (2020). Please refer to the included ReadMe file for a further explanation of individual files and step-by-step instructions for running the models.",
             "distribution": [
                 {
-                    "title": "1 - Playa.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504529/1%20-%20Playa.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "1 - Playa.zip"
                 },
                 {
-                    "title": "2 - Plateau & High Plains.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504529/2%20-%20Plateau%20%26%20High%20Plains.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "2 - Plateau & High Plains.zip"
                 },
                 {
-                    "title": "3 - Mountain Valley.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504529/3%20-%20Mountain%20Valley.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "3 - Mountain Valley.zip"
                 },
                 {
-                    "title": "4 - Riverine Valley.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504529/4%20-%20Riverine%20Valley.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "4 - Riverine Valley.zip"
                 },
                 {
-                    "title": "5 - Coastal Terrain.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504529/5%20-%20Coastal%20Terrain.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "5 - Coastal Terrain.zip"
                 },
                 {
-                    "title": "ReadMe (epa).pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504529/ReadMe%20%28epa%29.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "ReadMe (epa).pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504529",
+            "keyword": [
+                "streams",
+                "catchments",
+                "watersheds",
+                "watershed metrics",
+                "National Hydrography Dataset",
+                "National Hydrography Dataset Plus (NHDPlus)",
+                "spatial prediction",
+                "aquatic condition",
+                "National Aquatic Resource Surveys"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-12-27",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -104850,59 +104846,57 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Hydrologic landscape groundwater modeling input parameters and results"
         },
         {
-            "title": "Simulating the Environmental Fate and Transport of Graphene Oxide Nanoparticles and Their Major Phototransformation Product in Surface Waters: ORD-024619",
-            "description": "There has been growing interest in simulating the fate and transport of engineered nanomaterials in the environment. The Water Quality Analysis Simulation Program (WASP) is one of the most widely used water quality models and has recently been upgraded to WASP8. WASP8 incorporates the algorithms to simulate the fate and transport of nanoparticles in surface waters. This study simulates the fate and transport of graphene oxide (GO) nanomaterials and their major phototransformation product, photoreduced graphene oxide (rGO), for Brier Creek, GA, USA. We specifically explored the influences of three important processes on the fate and transport of GO: (1) light attenuation, (2) phototransformation, and (3) heteroaggregation, and simulated their distributions in the river, including the water column and sediment. \n\nThis dataset is associated with the following publication:\nHan, Y., C. Knightes, D. Bouchard, R. Zepp, B. Avant, H. Hsieh, X. Chang, B. Acrey, M. Henderson, and J. Spear. Simulating graphene oxide nanomaterial phototransformation and transport in surface water.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 6: 180, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1434256",
-            "keyword": [
-                "nanomaterials",
-                "graphene oxide",
-                "reduced graphene oxide",
-                "water quality",
-                "Water Quality Analysis Simulation Program",
-                "WASP",
-                "modeling"
-            ],
             "contactPoint": {
                 "fn": "Christopher Knightes",
                 "hasEmail": "mailto:knightes.chris@epa.gov"
             },
+            "description": "There has been growing interest in simulating the fate and transport of engineered nanomaterials in the environment. The Water Quality Analysis Simulation Program (WASP) is one of the most widely used water quality models and has recently been upgraded to WASP8. WASP8 incorporates the algorithms to simulate the fate and transport of nanoparticles in surface waters. This study simulates the fate and transport of graphene oxide (GO) nanomaterials and their major phototransformation product, photoreduced graphene oxide (rGO), for Brier Creek, GA, USA. We specifically explored the influences of three important processes on the fate and transport of GO: (1) light attenuation, (2) phototransformation, and (3) heteroaggregation, and simulated their distributions in the river, including the water column and sediment. \n\nThis dataset is associated with the following publication:\nHan, Y., C. Knightes, D. Bouchard, R. Zepp, B. Avant, H. Hsieh, X. Chang, B. Acrey, M. Henderson, and J. Spear. Simulating graphene oxide nanomaterial phototransformation and transport in surface water.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 6: 180, (2019).",
             "distribution": [
                 {
-                    "title": "Data for Fig3 a and b.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434256/Data%20for%20Fig3%20a%20and%20b.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Data for Fig3 a and b.csv"
                 },
                 {
-                    "title": "Data for Fig3 c and d.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434256/Data%20for%20Fig3%20c%20and%20d.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Data for Fig3 c and d.csv"
                 },
                 {
-                    "title": "Figure 4A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434256/Figure%204A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 4A.xlsx"
                 },
                 {
-                    "title": "Figure 4B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434256/Figure%204B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 4B.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434256",
+            "keyword": [
+                "nanomaterials",
+                "graphene oxide",
+                "reduced graphene oxide",
+                "water quality",
+                "Water Quality Analysis Simulation Program",
+                "WASP",
+                "modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-02",
-            "references": [
-                "https://doi.org/10.1039/c8en01088a"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104912,40 +104906,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c8en01088a"
+            ],
+            "rights": null,
+            "title": "Simulating the Environmental Fate and Transport of Graphene Oxide Nanoparticles and Their Major Phototransformation Product in Surface Waters: ORD-024619"
         },
         {
-            "title": "Iron concentrations in exhaled breath condensate decrease in ever-smokers and COPD patients",
-            "description": "This is the data used in the manuscript. \n\nThis dataset is associated with the following publication:\nGhio, A., J. Soukup, J. Mcgee, M. Madden, and C. Esther Jr. Iron concentration in exhaled breath condensates decreases in ever-smokers and COPD patients.   Journal of Breath Research. Institute of Physics Publishing, Bristol,  UK, 12(4): 046009, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1432765",
-            "keyword": [
-                "particulate matter",
-                "smoking",
-                "oxidants"
-            ],
             "contactPoint": {
                 "fn": "Andrew Ghio",
                 "hasEmail": "mailto:ghio.andy@epa.gov"
             },
+            "description": "This is the data used in the manuscript. \n\nThis dataset is associated with the following publication:\nGhio, A., J. Soukup, J. Mcgee, M. Madden, and C. Esther Jr. Iron concentration in exhaled breath condensates decreases in ever-smokers and COPD patients.   Journal of Breath Research. Institute of Physics Publishing, Bristol,  UK, 12(4): 046009, (2018).",
             "distribution": [
                 {
-                    "title": "eclipse data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1432765/eclipse%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "eclipse data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1432765",
+            "keyword": [
+                "particulate matter",
+                "smoking",
+                "oxidants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-06",
-            "references": [
-                "https://doi.org/10.1088/1752-7163/aad825"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -104955,19 +104949,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1752-7163/aad825"
+            ],
+            "rights": null,
+            "title": "Iron concentrations in exhaled breath condensate decrease in ever-smokers and COPD patients"
         },
         {
-            "title": "HTF2015 Dietary Oils Effects on Mitochondrial Bioenergetics and Glial Morphology",
-            "description": "Effects of acute ozone exposure on mitochondrial complex enzyme activities in various brain regions and glial morphology reared on different dietary oils. \n\nThis dataset is associated with the following publication:\nValdez, M., D. Freeborn, J. Valdez, A. Johnstone, S. Snow, A. Tennant, U. Kodavanti, and P. Kodavanti. Mitochondrial Bioenergetics in Brain Following Ozone Exposure in Rats Maintained on Coconut, Fish, and Olive Oil-Rich Diets.   International Journal of Molecular Sciences. MDPI AG, Basel,  SWITZERLAND, 20(24): 6303, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Prasada Kodavanti",
+                "hasEmail": "mailto:kodavanti.prasada@epa.gov"
+            },
+            "description": "Effects of acute ozone exposure on mitochondrial complex enzyme activities in various brain regions and glial morphology reared on different dietary oils. \n\nThis dataset is associated with the following publication:\nValdez, M., D. Freeborn, J. Valdez, A. Johnstone, S. Snow, A. Tennant, U. Kodavanti, and P. Kodavanti. Mitochondrial Bioenergetics in Brain Following Ozone Exposure in Rats Maintained on Coconut, Fish, and Olive Oil-Rich Diets.   International Journal of Molecular Sciences. MDPI AG, Basel,  SWITZERLAND, 20(24): 6303, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504549/Mito%20Bioenergetics%20Ozone%20Dietary%20Oil%20Suppl_A-573z_dataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mito Bioenergetics Ozone Dietary Oil Suppl_A-573z_dataset.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504549",
             "keyword": [
@@ -104982,20 +104986,10 @@
                 "olive oil",
                 "Coconut oil"
             ],
-            "contactPoint": {
-                "fn": "Prasada Kodavanti",
-                "hasEmail": "mailto:kodavanti.prasada@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Mito Bioenergetics Ozone Dietary Oil Suppl_A-573z_dataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504549/Mito%20Bioenergetics%20Ozone%20Dietary%20Oil%20Suppl_A-573z_dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-12-01",
-            "references": [
-                "https://doi.org/10.3390/ijms20246303"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105005,42 +104999,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ijms20246303"
+            ],
+            "rights": null,
+            "title": "HTF2015 Dietary Oils Effects on Mitochondrial Bioenergetics and Glial Morphology"
         },
         {
-            "title": "Cell-Based Metabolomics for Untargeted Screening and Prioritization of Vertebrate-Active Stressors in Streams Across the United States",
-            "description": "Extents of impact, as measured by NMR spectroscopy, on the Zebrafish liver cell endogenous metabolite profiles resulting from exposure to the 38 stream waters, along with numbers of anthropogenic organic chemicals detected at each site. Also, a summary of chemicals detected by class is included, along with statistics on their occurances in the group of stressors that most-strongly covary with changes in endogenous metabolite profiles. \n\nThis dataset is associated with the following publication:\nCollette, T., D. Ekman, H. Zhen, H. Nguyen, P.M. Bradley, and Q. Teng. Cell-Based Metabolomics for Untargeted Screening and Prioritization of Vertebrate-Active Stressors in Streams Across the United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(15): 9232-9240, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503727",
-            "keyword": [
-                "metabolomics",
-                "in vitro bioassays",
-                "effects-based monitoring",
-                "NMR spectroscopy",
-                "zebrafish"
-            ],
             "contactPoint": {
                 "fn": "Drew Ekman",
                 "hasEmail": "mailto:ekman.drew@epa.gov"
             },
+            "description": "Extents of impact, as measured by NMR spectroscopy, on the Zebrafish liver cell endogenous metabolite profiles resulting from exposure to the 38 stream waters, along with numbers of anthropogenic organic chemicals detected at each site. Also, a summary of chemicals detected by class is included, along with statistics on their occurances in the group of stressors that most-strongly covary with changes in endogenous metabolite profiles. \n\nThis dataset is associated with the following publication:\nCollette, T., D. Ekman, H. Zhen, H. Nguyen, P.M. Bradley, and Q. Teng. Cell-Based Metabolomics for Untargeted Screening and Prioritization of Vertebrate-Active Stressors in Streams Across the United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(15): 9232-9240, (2019).",
             "distribution": [
                 {
-                    "title": "Collette Stream Metabolomics SciHub data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503727/Collette%20Stream%20Metabolomics%20SciHub%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Collette Stream Metabolomics SciHub data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503727",
+            "keyword": [
+                "metabolomics",
+                "in vitro bioassays",
+                "effects-based monitoring",
+                "NMR spectroscopy",
+                "zebrafish"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-22",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b02736"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105050,40 +105044,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b02736"
+            ],
+            "rights": null,
+            "title": "Cell-Based Metabolomics for Untargeted Screening and Prioritization of Vertebrate-Active Stressors in Streams Across the United States"
         },
         {
-            "title": "data",
-            "description": "Measurement and log removal values of spiked microbes to evaluate system performance. \n\nThis dataset is associated with the following publication:\nGassie, L., J. Englehardt, N. Brinkman, J. Garland, and M. Kusumitha Perera. Ozone-UV net-zero water wash station for remote emergency response healthcare Units: Design, operation, and results.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 6(11): 1971-1984, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500005",
-            "keyword": [
-                "net-zero water",
-                "direct potable reuse",
-                "remote emergency response"
-            ],
             "contactPoint": {
                 "fn": "Nichole Brinkman",
                 "hasEmail": "mailto:brinkman.nichole@epa.gov"
             },
+            "description": "Measurement and log removal values of spiked microbes to evaluate system performance. \n\nThis dataset is associated with the following publication:\nGassie, L., J. Englehardt, N. Brinkman, J. Garland, and M. Kusumitha Perera. Ozone-UV net-zero water wash station for remote emergency response healthcare Units: Design, operation, and results.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 6(11): 1971-1984, (2019).",
             "distribution": [
                 {
-                    "title": "Microbe-LRVs-SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500005/Microbe-LRVs-SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Microbe-LRVs-SciHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500005",
+            "keyword": [
+                "net-zero water",
+                "direct potable reuse",
+                "remote emergency response"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-26",
-            "references": [
-                "https://doi.org/10.1039/c9ew00126c"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105093,41 +105087,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c9ew00126c"
+            ],
+            "rights": null,
+            "title": "data"
         },
         {
-            "title": "O3-Noise CM2018 ScienceHub Data (uploaded 5-22-19, draft only",
-            "description": "Data set still under review (5-22-19). \n\nThis dataset is associated with the following publication:\nMiller, C., U. Kodavanti, E. Stewart, M. Schladweiler, J. Richards, S. Snow, A. Henriquez Coria, W. Oshiro, A. Farraj, M. Hazari, and J. Dye. Fetal Growth Outcomes Following Peri-Implantation Exposure of Long Evans Rats to Noise and Ozone Differ by Sex.   Biology of Sex Differences. BioMed Central Ltd, London,  UK, 10(1): 54, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503869",
-            "keyword": [
-                "Ozone",
-                "noise",
-                "intrauterine growth restriction",
-                "children's health"
-            ],
             "contactPoint": {
                 "fn": "Janice Dye",
                 "hasEmail": "mailto:dye.janice@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1503869/documents/O3-Noise-Dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Data set still under review (5-22-19). \n\nThis dataset is associated with the following publication:\nMiller, C., U. Kodavanti, E. Stewart, M. Schladweiler, J. Richards, S. Snow, A. Henriquez Coria, W. Oshiro, A. Farraj, M. Hazari, and J. Dye. Fetal Growth Outcomes Following Peri-Implantation Exposure of Long Evans Rats to Noise and Ozone Differ by Sex.   Biology of Sex Differences. BioMed Central Ltd, London,  UK, 10(1): 54, (2019).",
             "distribution": [
                 {
-                    "title": "O3Noise-CM2018 Datasheet.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503869/O3Noise-CM2018%20Datasheet.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "O3Noise-CM2018 Datasheet.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503869",
+            "keyword": [
+                "Ozone",
+                "noise",
+                "intrauterine growth restriction",
+                "children's health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-22",
-            "references": [
-                "https://doi.org/10.1186/s13293-019-0270-6"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105138,49 +105134,49 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1503869/documents/O3-Noise-Dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1186/s13293-019-0270-6"
+            ],
+            "rights": null,
+            "title": "O3-Noise CM2018 ScienceHub Data (uploaded 5-22-19, draft only"
         },
         {
-            "title": "Urban soil ecosystem services",
-            "description": "This dataset is representative of the subset of measured urban soil hydrologic, taxonomic, and fertility data that was used to support the results and conclusions of this paper. \n\nThis dataset is associated with the following publication:\nDustin, H., W. Shuster , and A. Garmestani. Vacant urban lot soils and their potential to support ecosystem services.   PLANT AND SOIL. Springer, New York, NY, USA, 179(2): 01-13, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1390083",
-            "keyword": [
-                "shrinking cities",
-                "urban soil ecosystem services",
-                "vacant lots",
-                "urban soils",
-                "soil hydrology",
-                "Green Infrastructure"
-            ],
             "contactPoint": {
                 "fn": "William Shuster",
                 "hasEmail": "mailto:shuster.william@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1390083/documents/Copy%20of%20DataDictionary_Shuster_UrbanSoilEcosystemServices.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This dataset is representative of the subset of measured urban soil hydrologic, taxonomic, and fertility data that was used to support the results and conclusions of this paper. \n\nThis dataset is associated with the following publication:\nDustin, H., W. Shuster , and A. Garmestani. Vacant urban lot soils and their potential to support ecosystem services.   PLANT AND SOIL. Springer, New York, NY, USA, 179(2): 01-13, (2016).",
             "distribution": [
                 {
-                    "title": "Copy of DataDictionary_Shuster_UrbanSoilEcosystemServices.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390083/Copy%20of%20DataDictionary_Shuster_UrbanSoilEcosystemServices.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of DataDictionary_Shuster_UrbanSoilEcosystemServices.xlsx"
                 },
                 {
-                    "title": "plsodata5.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390083/plsodata5.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "plsodata5.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390083",
+            "keyword": [
+                "shrinking cities",
+                "urban soil ecosystem services",
+                "vacant lots",
+                "urban soils",
+                "soil hydrology",
+                "Green Infrastructure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-29",
-            "references": [
-                "https://doi.org/10.1007/s11104-016-2874-5"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105191,47 +105187,45 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1390083/documents/Copy%20of%20DataDictionary_Shuster_UrbanSoilEcosystemServices.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1007/s11104-016-2874-5"
+            ],
+            "rights": null,
+            "title": "Urban soil ecosystem services"
         },
         {
-            "title": "PPIAvsLCMS",
-            "description": "Vender specific data. \n\nThis dataset is associated with the following publication:\nMash , H. Effect of chlorination on the protein phosphatase inhibition activity for several microcystins.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 95: 230-239, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407520",
-            "keyword": [
-                "microcystins",
-                "Algaltoxin",
-                "Protein phosphatase inhibition",
-                "chlorination"
-            ],
             "contactPoint": {
                 "fn": "Heath Mash",
                 "hasEmail": "mailto:mash.heath@epa.gov"
             },
+            "description": "Vender specific data. \n\nThis dataset is associated with the following publication:\nMash , H. Effect of chlorination on the protein phosphatase inhibition activity for several microcystins.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 95: 230-239, (2016).",
             "distribution": [
                 {
-                    "title": "160224-PPIA vs LC-MS Results - Summarized from the Excel data files1.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407520/160224-PPIA%20vs%20LC-MS%20Results%20-%20Summarized%20from%20the%20Excel%20data%20files1.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "160224-PPIA vs LC-MS Results - Summarized from the Excel data files1.pdf"
                 },
                 {
-                    "title": "160224-PPIA vs LC-MS Results - Summarized from the Excel data files2.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407520/160224-PPIA%20vs%20LC-MS%20Results%20-%20Summarized%20from%20the%20Excel%20data%20files2.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "160224-PPIA vs LC-MS Results - Summarized from the Excel data files2.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407520",
+            "keyword": [
+                "microcystins",
+                "Algaltoxin",
+                "Protein phosphatase inhibition",
+                "chlorination"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-28",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2016.03.024"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105241,42 +105235,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2016.03.024"
+            ],
+            "rights": null,
+            "title": "PPIAvsLCMS"
         },
         {
-            "title": "Impact of Reductions in Emissions from Major Source Sectors on Fine Particulate Matter Related Cardiovascular Mortality",
-            "description": "County-level annual cardiovascular mortality rates and annual average PM2.5 concentrations, 2132 U.S. counties, 1990-2010. Included national emissions by sectors and county-level confounders (annual COPD mortality rates, percent non-white population, and median income). \n\nThis dataset is associated with the following publication:\nPeterson, G., C. Hogrefe, L. Neas, A. Corrigan, R. Mathur, and A. Rappold. Impacts of Reductions in Emissions from Major Source Sectors on Fine Particulate Matter-Related Cardiovascular Mortality.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 128(1): 17005, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503961",
-            "keyword": [
-                "fine particulate matter (PM2.5)",
-                "cardiovascular mortality",
-                "CMAQ",
-                "long-term trends",
-                "health effects"
-            ],
             "contactPoint": {
                 "fn": "Geoffrey Peterson",
                 "hasEmail": "mailto:peterson.geoffrey@epa.gov"
             },
+            "describedBy": "https://www.cdc.gov/nchs/data-linkage/mortality-public.htm",
+            "description": "County-level annual cardiovascular mortality rates and annual average PM2.5 concentrations, 2132 U.S. counties, 1990-2010. Included national emissions by sectors and county-level confounders (annual COPD mortality rates, percent non-white population, and median income). \n\nThis dataset is associated with the following publication:\nPeterson, G., C. Hogrefe, L. Neas, A. Corrigan, R. Mathur, and A. Rappold. Impacts of Reductions in Emissions from Major Source Sectors on Fine Particulate Matter-Related Cardiovascular Mortality.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 128(1): 17005, (2020).",
             "distribution": [
                 {
-                    "title": "Datasets for A-z61z.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503961/Datasets%20for%20A-z61z.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Datasets for A-z61z.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503961",
+            "keyword": [
+                "fine particulate matter (PM2.5)",
+                "cardiovascular mortality",
+                "CMAQ",
+                "long-term trends",
+                "health effects"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-07",
-            "references": [
-                "https://doi.org/10.1289/ehp5692"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105287,19 +105282,28 @@
                     }
                 }
             },
-            "describedBy": "https://www.cdc.gov/nchs/data-linkage/mortality-public.htm"
+            "references": [
+                "https://doi.org/10.1289/ehp5692"
+            ],
+            "rights": null,
+            "title": "Impact of Reductions in Emissions from Major Source Sectors on Fine Particulate Matter Related Cardiovascular Mortality"
         },
         {
-            "title": "Regulating temperature and relative humidity in air-liquid interface in vitro systems ",
-            "description": "The raw data values used in all the tables and figures of the manuscript. \n\nThis dataset is associated with the following publication:\nZavala, J., R. Greenan, T. Krantz , D. DeMarini , M. Higuchi , I. Gilmour , and P.A. White. Regulating temperature and relative humidity in air-liquid interface in vitro systems eliminates cytotoxicity resulting from control air exposures.   Toxicology Research. Royal Society of Chemistry, London,  UK, 6(4): 448-459, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Mark Higuchi",
+                "hasEmail": "mailto:higuchi.mark@epa.gov"
+            },
+            "description": "The raw data values used in all the tables and figures of the manuscript. \n\nThis dataset is associated with the following publication:\nZavala, J., R. Greenan, T. Krantz , D. DeMarini , M. Higuchi , I. Gilmour , and P.A. White. Regulating temperature and relative humidity in air-liquid interface in vitro systems eliminates cytotoxicity resulting from control air exposures.   Toxicology Research. Royal Society of Chemistry, London,  UK, 6(4): 448-459, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517577/HiguchiMark_A-q57w_SDMP_20200108.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HiguchiMark_A-q57w_SDMP_20200108.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1517577",
             "keyword": [
@@ -105310,20 +105314,10 @@
                 "relative humidity",
                 "temperature"
             ],
-            "contactPoint": {
-                "fn": "Mark Higuchi",
-                "hasEmail": "mailto:higuchi.mark@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "HiguchiMark_A-q57w_SDMP_20200108.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517577/HiguchiMark_A-q57w_SDMP_20200108.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-01",
-            "references": [
-                "https://doi.org/10.1039/c7tx00109f"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105333,40 +105327,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c7tx00109f"
+            ],
+            "rights": null,
+            "title": "Regulating temperature and relative humidity in air-liquid interface in vitro systems "
         },
         {
-            "title": "Dataset - Donner Nanosilver PCP Table 3 LCF results",
-            "description": "Linear combination fitting results of the Ag K-edge XANES spectra using the standards listed, as percentage composition and variability (in parentheses) of the total. R-factor indicates the quality of the fit. \n\nThis dataset is associated with the following publication:\nKhaksar, M., S. Vasileiadis, R. Sekine, G. Brunetti, K.G. Scheckel, K. Vasilev, E. Lombi, and E. Donner. Chemical characterisation, antibacterial activity, and (nano)silver transformation of commercial personal care products exposed to household\ngreywater.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 6(10): 3027-3028, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503381",
-            "keyword": [
-                "synchrotron speciation",
-                "silver nanoparticles",
-                "antimicrobial activity"
-            ],
             "contactPoint": {
                 "fn": "Kirk Scheckel",
                 "hasEmail": "mailto:scheckel.kirk@epa.gov"
             },
+            "description": "Linear combination fitting results of the Ag K-edge XANES spectra using the standards listed, as percentage composition and variability (in parentheses) of the total. R-factor indicates the quality of the fit. \n\nThis dataset is associated with the following publication:\nKhaksar, M., S. Vasileiadis, R. Sekine, G. Brunetti, K.G. Scheckel, K. Vasilev, E. Lombi, and E. Donner. Chemical characterisation, antibacterial activity, and (nano)silver transformation of commercial personal care products exposed to household\ngreywater.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 6(10): 3027-3028, (2019).",
             "distribution": [
                 {
-                    "title": "Dataset-Donner Nanosilver PCP.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503381/Dataset-Donner%20Nanosilver%20PCP.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Dataset-Donner Nanosilver PCP.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503381",
+            "keyword": [
+                "synchrotron speciation",
+                "silver nanoparticles",
+                "antimicrobial activity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-12-14",
-            "references": [
-                "https://doi.org/10.1039/c9en00738e"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105376,45 +105370,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c9en00738e"
+            ],
+            "rights": null,
+            "title": "Dataset - Donner Nanosilver PCP Table 3 LCF results"
         },
         {
-            "title": "Riparian Wetness in the Upper Missouri Headwater basins - supporting data",
-            "description": "Includes data and derivations not publicly available used to create figures and tables for manuscript. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., J. Christensen, and L. Alexander. Influence of multi-decadal land use, irrigation practices and climate on riparian corridors across the Upper Missouri River headwaters basin, Montana.   HYDROLOGY AND EARTH SYSTEM SCIENCES. EGS,    23(10): 4269\u20134292, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503642",
-            "keyword": [
-                "center-pivot",
-                "discharge",
-                "Landsat",
-                "riparian wetness"
-            ],
             "contactPoint": {
                 "fn": "Jay Christensen",
                 "hasEmail": "mailto:christensen.jay@epa.gov"
             },
+            "description": "Includes data and derivations not publicly available used to create figures and tables for manuscript. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., J. Christensen, and L. Alexander. Influence of multi-decadal land use, irrigation practices and climate on riparian corridors across the Upper Missouri River headwaters basin, Montana.   HYDROLOGY AND EARTH SYSTEM SCIENCES. EGS,    23(10): 4269\u20134292, (2019).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.5066/P976LZ2G",
-                    "accessURL": "https://doi.org/10.5066/P976LZ2G"
+                    "accessURL": "https://doi.org/10.5066/P976LZ2G",
+                    "title": "https://doi.org/10.5066/P976LZ2G"
                 },
                 {
-                    "title": "Influence of multi-decadal land use, irrigation practices and climate on riparian corridors across the Upper Missouri River headwaters basin, Montana.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503642/Influence%20of%20multi-decadal%20land%20use%2C%20irrigation%20practices%20and%20climate%20on%20riparian%20corridors%20across%20the%20Upper%20Missouri%20River%20headwaters%20basin%2C%20Montana.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Influence of multi-decadal land use, irrigation practices and climate on riparian corridors across the Upper Missouri River headwaters basin, Montana.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503642",
+            "keyword": [
+                "center-pivot",
+                "discharge",
+                "Landsat",
+                "riparian wetness"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-21",
-            "references": [
-                "https://doi.org/10.5194/hess-23-4269-2019"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105424,20 +105418,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/hess-23-4269-2019"
+            ],
+            "rights": null,
+            "title": "Riparian Wetness in the Upper Missouri Headwater basins - supporting data"
         },
         {
-            "title": "Biophysical comparision  of four silver nanoparticles coatings using microscopy hyperspectral imaging and flow cytometry ",
-            "description": "hyperspectral imaging data, images , flow cytometry histograms. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: contact robert zucker by e-mail\nzucker.robert@epa.gov. Format: the imaging is in JP2 and ND 2 nikon files . the flow cytometry is in FSC3.0 format which is not uploadable. \n\nThis dataset is associated with the following publication:\nZucker, R., J. Ortenzio, L. Degn, J. Lerner , and W. Boyes. Biophysical Comparison of Four Silver Nanoparticles Coatings using Microscopy, Hyperspectral Imaging and Flow Cytometry..   PLoS ONE. Public Library of Science, San Francisco, CA, USA,  1-24, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Robert Zucker",
+                "hasEmail": "mailto:zucker.robert@epa.gov"
+            },
+            "description": "hyperspectral imaging data, images , flow cytometry histograms. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: contact robert zucker by e-mail\nzucker.robert@epa.gov. Format: the imaging is in JP2 and ND 2 nikon files . the flow cytometry is in FSC3.0 format which is not uploadable. \n\nThis dataset is associated with the following publication:\nZucker, R., J. Ortenzio, L. Degn, J. Lerner , and W. Boyes. Biophysical Comparison of Four Silver Nanoparticles Coatings using Microscopy, Hyperspectral Imaging and Flow Cytometry..   PLoS ONE. Public Library of Science, San Francisco, CA, USA,  1-24, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1517578",
             "keyword": [
                 "silver nanoparticles",
@@ -105450,14 +105448,10 @@
                 "Light scatter",
                 "plasmonic surface resonance"
             ],
-            "contactPoint": {
-                "fn": "Robert Zucker",
-                "hasEmail": "mailto:zucker.robert@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-08",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0219078"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105467,34 +105461,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0219078"
+            ],
+            "rights": null,
+            "title": "Biophysical comparision  of four silver nanoparticles coatings using microscopy hyperspectral imaging and flow cytometry "
         },
         {
-            "title": "US EPA Superfund Site Soil Samples",
-            "description": "US EPA Superfund site soil samples. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: In the publication and supporting information. Format: These data were generated from US EPA Superfund site soil samples. \n\nThis dataset is associated with the following publication:\nBradham, K., C. Nelson, P. Alava, J. Misenheimer, G. Diamond, W. Thayer, and D. Thomas. Estimating relative bioavailability of soil lead in the mouse.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 79(24): 1179-1182, (2016).",
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
+                "fn": "Karen Bradham",
+                "hasEmail": "mailto:bradham.karen@epa.gov"
+            },
+            "description": "US EPA Superfund site soil samples. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: In the publication and supporting information. Format: These data were generated from US EPA Superfund site soil samples. \n\nThis dataset is associated with the following publication:\nBradham, K., C. Nelson, P. Alava, J. Misenheimer, G. Diamond, W. Thayer, and D. Thomas. Estimating relative bioavailability of soil lead in the mouse.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 79(24): 1179-1182, (2016).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1506072",
             "keyword": [
                 "lead",
                 "bioavailability",
                 "soil"
             ],
-            "contactPoint": {
-                "fn": "Karen Bradham",
-                "hasEmail": "mailto:bradham.karen@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-01",
-            "references": [
-                "https://doi.org/10.1080/15287394.2016.1221789"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105504,41 +105498,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/15287394.2016.1221789"
+            ],
+            "rights": null,
+            "title": "US EPA Superfund Site Soil Samples"
         },
         {
-            "title": "SciHub Disinfectant Impact",
-            "description": "Contains Sample ID, Disinfectant type, Cold/Hot, Total Chlorine Residual, Genomic Target/L. \n\nThis dataset is associated with the following publication:\nDonohue, M., S. Vesper, J. Mistry, and J. Donohue. Impact of Chlorine and Chloramine on the Detection and Quantification of Legionella pneumophila and Mycobacterium Species.   APPLIED AND ENVIRONMENTAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 85(24): e01942-19, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503713",
-            "keyword": [
-                "legionella",
-                "Mycobacterium",
-                "disinfectant",
-                "total chlorine residual"
-            ],
             "contactPoint": {
                 "fn": "Maura Donohue",
                 "hasEmail": "mailto:donohue.maura@epa.gov"
             },
+            "description": "Contains Sample ID, Disinfectant type, Cold/Hot, Total Chlorine Residual, Genomic Target/L. \n\nThis dataset is associated with the following publication:\nDonohue, M., S. Vesper, J. Mistry, and J. Donohue. Impact of Chlorine and Chloramine on the Detection and Quantification of Legionella pneumophila and Mycobacterium Species.   APPLIED AND ENVIRONMENTAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 85(24): e01942-19, (2019).",
             "distribution": [
                 {
-                    "title": "SciHub (Final) Disinfectant Impact.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503713/SciHub%20%28Final%29%20Disinfectant%20Impact.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub (Final) Disinfectant Impact.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503713",
+            "keyword": [
+                "legionella",
+                "Mycobacterium",
+                "disinfectant",
+                "total chlorine residual"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-01-27",
-            "references": [
-                "https://doi.org/10.1128/aem.01942-19"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105548,20 +105542,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1128/aem.01942-19"
+            ],
+            "rights": null,
+            "title": "SciHub Disinfectant Impact"
         },
         {
-            "title": "metadata_A-280m",
-            "description": "The metadata describe the set of Landsat Thematic Mapper images used in this study. This dataset is not publicly accessible because: File size is too large. It can be accessed through the following means: See the data dictionary. Format: TIFF. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., J. Christensen , and L. Alexander. Patterns and drivers for wetland connections in the Prairie Pothole Region, United States.   Wetlands Ecology and Management. Springer Science and Business Media B.V;Formerly Kluwer Academic Publishers B.V.,   GERMANY, 25: 275-297, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Jay Christensen",
+                "hasEmail": "mailto:christensen.jay@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517582/documents/dd_A-280m.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The metadata describe the set of Landsat Thematic Mapper images used in this study. This dataset is not publicly accessible because: File size is too large. It can be accessed through the following means: See the data dictionary. Format: TIFF. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., J. Christensen , and L. Alexander. Patterns and drivers for wetland connections in the Prairie Pothole Region, United States.   Wetlands Ecology and Management. Springer Science and Business Media B.V;Formerly Kluwer Academic Publishers B.V.,   GERMANY, 25: 275-297, (2017).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1517582",
             "keyword": [
                 "Prairie Pothole Region",
@@ -105569,14 +105569,10 @@
                 "Landsat",
                 "wetlands"
             ],
-            "contactPoint": {
-                "fn": "Jay Christensen",
-                "hasEmail": "mailto:christensen.jay@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.1007/s11273-016-9516-9"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105587,21 +105583,25 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517582/documents/dd_A-280m.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1007/s11273-016-9516-9"
+            ],
+            "rights": null,
+            "title": "metadata_A-280m"
         },
         {
-            "title": "Lakes, Surface Water Dynamics, Prairie Pothole Region, Depressional wetlands, Wetland Loss, Landsat, Climate, Wetland Connectivity",
-            "description": "These data are processed Landsat images. This dataset is not publicly accessible because: The dataset is too large for Sciencehub upload. It can be accessed through the following means: Please contact Laurie Alexander, alexander.laurie@epa.gov. Format: These data are in OLI Full Resolution Browse (FRB) format. \n\nThis dataset is associated with the following publication:\nVanderhoof , M., and L. Alexander. The Role of Lake Expansion in Altering the Wetland Landscape of the Prairie Pothole Region, United States.   WETLANDS. The Society of Wetland Scientists, McLean, VA, USA, 36(Suppl 2): S309-S321, (2016).",
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
+                "fn": "Laurie Alexander",
+                "hasEmail": "mailto:alexander.laurie@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517579/documents/dd_A-rnj1.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "These data are processed Landsat images. This dataset is not publicly accessible because: The dataset is too large for Sciencehub upload. It can be accessed through the following means: Please contact Laurie Alexander, alexander.laurie@epa.gov. Format: These data are in OLI Full Resolution Browse (FRB) format. \n\nThis dataset is associated with the following publication:\nVanderhoof , M., and L. Alexander. The Role of Lake Expansion in Altering the Wetland Landscape of the Prairie Pothole Region, United States.   WETLANDS. The Society of Wetland Scientists, McLean, VA, USA, 36(Suppl 2): S309-S321, (2016).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1517579",
             "keyword": [
                 "lakes",
@@ -105613,14 +105613,10 @@
                 "climate",
                 "Wetland Connectivity"
             ],
-            "contactPoint": {
-                "fn": "Laurie Alexander",
-                "hasEmail": "mailto:alexander.laurie@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-01",
-            "references": [
-                "https://doi.org/10.1007/s13157-015-0728-1"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105631,20 +105627,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517579/documents/dd_A-rnj1.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1007/s13157-015-0728-1"
+            ],
+            "rights": null,
+            "title": "Lakes, Surface Water Dynamics, Prairie Pothole Region, Depressional wetlands, Wetland Loss, Landsat, Climate, Wetland Connectivity"
         },
         {
-            "title": "Reactivity of graphene oxide with reactive oxygen species",
-            "description": "Graphs of kinetic data on indirect photoreaction of graphene oxide with selected reactive oxygen species graphs. \n\nThis dataset is associated with the following publication:\nHsieh, H., and R. Zepp. Reactivity of graphene oxide with reactive oxygen species (hydroxyl radical, singlet oxygen, and superoxide anion).   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 6(12): 3734-3744, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Richard Zepp",
+                "hasEmail": "mailto:zepp.richard@epa.gov"
+            },
+            "description": "Graphs of kinetic data on indirect photoreaction of graphene oxide with selected reactive oxygen species graphs. \n\nThis dataset is associated with the following publication:\nHsieh, H., and R. Zepp. Reactivity of graphene oxide with reactive oxygen species (hydroxyl radical, singlet oxygen, and superoxide anion).   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 6(12): 3734-3744, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503905/Data%20for%20GO_ROS_Experiments.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data for GO_ROS_Experiments.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503905",
             "keyword": [
@@ -105655,20 +105659,10 @@
                 "aquatic environment",
                 "Reactive oxygen species"
             ],
-            "contactPoint": {
-                "fn": "Richard Zepp",
-                "hasEmail": "mailto:zepp.richard@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data for GO_ROS_Experiments.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503905/Data%20for%20GO_ROS_Experiments.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-30",
-            "references": [
-                "https://doi.org/10.1039/c9en00693a"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105678,19 +105672,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c9en00693a"
+            ],
+            "rights": null,
+            "title": "Reactivity of graphene oxide with reactive oxygen species"
         },
         {
-            "title": "ISO-Aging Data",
-            "description": "GC-MS chromatograms from chamber and field studies were generated in this study. \n\nThis dataset is associated with the following publication:\nJaoui, M., R. Szmigielski, K. Nestorowicz, A. Kolodziejczyk, K. Sarang, K.J. Rudzinski, A. Konopka, T. Kleindienst, E. Bulska, and M. Lewandowski. Organic Hydroxy Acids as Highly Oxygenated Molecular (HOM) Tracers for Aged Isoprene Aerosol.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(24): 14516-14527, (2019).",
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
+            "description": "GC-MS chromatograms from chamber and field studies were generated in this study. \n\nThis dataset is associated with the following publication:\nJaoui, M., R. Szmigielski, K. Nestorowicz, A. Kolodziejczyk, K. Sarang, K.J. Rudzinski, A. Konopka, T. Kleindienst, E. Bulska, and M. Lewandowski. Organic Hydroxy Acids as Highly Oxygenated Molecular (HOM) Tracers for Aged Isoprene Aerosol.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(24): 14516-14527, (2019).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503732/Part1_Iso-Aging_STICS_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Part1_Iso-Aging_STICS_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503732",
             "keyword": [
@@ -105703,20 +105707,10 @@
                 "LC-Orbitrap",
                 "mass spectrometry"
             ],
-            "contactPoint": {
-                "fn": "Mohammed Jaoui",
-                "hasEmail": "mailto:jaoui.mohammed@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Part1_Iso-Aging_STICS_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503732/Part1_Iso-Aging_STICS_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-23",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b05075"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105726,42 +105720,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b05075"
+            ],
+            "rights": null,
+            "title": "ISO-Aging Data"
         },
         {
-            "title": "Automated Retrieval and Evaluation of Precipitation Data Sources for Environmental Modeling",
-            "description": "36 years of daily precipitation data from NLDAS, GLDAS, PRISM, NCEI, and DAYMET. \n\nThis dataset is associated with the following publication:\nSitterson, J., S. Sinnathamby, R. Parmar, J. Koblich, K. Wolfe, and C. Knightes. Demonstration of an online web services tool incorporating automatic retrieval and comparison of precipitation data.   ENVIRONMENTAL MODELLING & SOFTWARE. Elsevier Science, New York, NY,   123: 104570, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503994",
-            "keyword": [
-                "Precipitation Data",
-                "precipitation",
-                "web services",
-                "Comparison",
-                "pre processing data"
-            ],
             "contactPoint": {
                 "fn": "Rajbir Parmar",
                 "hasEmail": "mailto:parmar.rajbir@epa.gov"
             },
+            "description": "36 years of daily precipitation data from NLDAS, GLDAS, PRISM, NCEI, and DAYMET. \n\nThis dataset is associated with the following publication:\nSitterson, J., S. Sinnathamby, R. Parmar, J. Koblich, K. Wolfe, and C. Knightes. Demonstration of an online web services tool incorporating automatic retrieval and comparison of precipitation data.   ENVIRONMENTAL MODELLING & SOFTWARE. Elsevier Science, New York, NY,   123: 104570, (2020).",
             "distribution": [
                 {
-                    "title": "Precip_Compare_Manuscript.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503994/Precip_Compare_Manuscript.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Precip_Compare_Manuscript.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503994",
+            "keyword": [
+                "Precipitation Data",
+                "precipitation",
+                "web services",
+                "Comparison",
+                "pre processing data"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-13",
-            "references": [
-                "https://doi.org/10.1016/j.envsoft.2019.104570"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105771,41 +105765,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envsoft.2019.104570"
+            ],
+            "rights": null,
+            "title": "Automated Retrieval and Evaluation of Precipitation Data Sources for Environmental Modeling"
         },
         {
-            "title": "Provides an overview of the analysis and associated files, scripts and datasets",
-            "description": "This dataset contains the files, scripts and data that were used to run the simulations and data analyses for the manuscript. \n\nThis dataset is associated with the following publication:\nBall, K., C. Grant, W. Mundy, and T. Shafer. A multivariate extension of mutual information for growing neural networks..   Neural Networks. Elsevier B.V., Amsterdam,  NETHERLANDS, 95: 29-43, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1375317",
-            "keyword": [
-                "neurotoxicity",
-                "screening",
-                "Microelectrode array",
-                "developmental neurotoxicity"
-            ],
             "contactPoint": {
                 "fn": "Timothy Shafer",
                 "hasEmail": "mailto:shafer.tim@epa.gov"
             },
+            "description": "This dataset contains the files, scripts and data that were used to run the simulations and data analyses for the manuscript. \n\nThis dataset is associated with the following publication:\nBall, K., C. Grant, W. Mundy, and T. Shafer. A multivariate extension of mutual information for growing neural networks..   Neural Networks. Elsevier B.V., Amsterdam,  NETHERLANDS, 95: 29-43, (2017).",
             "distribution": [
                 {
-                    "title": "Mutual Information Data and Scripts.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375317/Mutual%20Information%20Data%20and%20Scripts.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Mutual Information Data and Scripts.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1375317",
+            "keyword": [
+                "neurotoxicity",
+                "screening",
+                "Microelectrode array",
+                "developmental neurotoxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-19",
-            "references": [
-                "https://doi.org/10.1016/j.neunet.2017.07.009"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105815,40 +105809,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.neunet.2017.07.009"
+            ],
+            "rights": null,
+            "title": "Provides an overview of the analysis and associated files, scripts and datasets"
         },
         {
-            "title": "Data set for Vassallo et al",
-            "description": "The dataset contains data from MEA recordings for 6 different compounds that were tested in a concentration-response format. Multiple parameters of neural network function were evaluated. \n\nThis dataset is associated with the following publication:\nShafer , T., C. Mack , A. Johnstone , A. Vassallo, M. Chiappalone, R. De Camargo Lopes, B. Scelfo, A. Novellino, E. Defranchi, T. Palosaari, T. Weisschu, T. Ramirez, R. Landsiedel, S. Martinoia, M. Whealan, and A. Bal-Price. A multi-laboratory evaluation of microelectrode array-based measurements of neural network activity for acute neurotoxicity testing..   NEUROTOXICOLOGY. Elsevier B.V., Amsterdam,  NETHERLANDS, 60: 280-292, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1517583",
-            "keyword": [
-                "screening",
-                "Microelectrode array",
-                "cross laboratory comparison"
-            ],
             "contactPoint": {
                 "fn": "Timothy Shafer",
                 "hasEmail": "mailto:shafer.tim@epa.gov"
             },
+            "description": "The dataset contains data from MEA recordings for 6 different compounds that were tested in a concentration-response format. Multiple parameters of neural network function were evaluated. \n\nThis dataset is associated with the following publication:\nShafer , T., C. Mack , A. Johnstone , A. Vassallo, M. Chiappalone, R. De Camargo Lopes, B. Scelfo, A. Novellino, E. Defranchi, T. Palosaari, T. Weisschu, T. Ramirez, R. Landsiedel, S. Martinoia, M. Whealan, and A. Bal-Price. A multi-laboratory evaluation of microelectrode array-based measurements of neural network activity for acute neurotoxicity testing..   NEUROTOXICOLOGY. Elsevier B.V., Amsterdam,  NETHERLANDS, 60: 280-292, (2017).",
             "distribution": [
                 {
-                    "title": "Vassallo Data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517583/Vassallo%20Data.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Vassallo Data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517583",
+            "keyword": [
+                "screening",
+                "Microelectrode array",
+                "cross laboratory comparison"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-10",
-            "references": [
-                "https://doi.org/10.1016/j.neuro.2016.03.019"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105858,42 +105852,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.neuro.2016.03.019"
+            ],
+            "rights": null,
+            "title": "Data set for Vassallo et al"
         },
         {
-            "title": " Mutagenicity Emission Factors of canola Oil and Waste Vegetable Oil Biodiesel:  Comparison to Soy Biodiesel",
-            "description": "The data set show the number of bacterial mutant colonies (called revertants or rev) per petri plate and the dose of the extractable organic matter (EOM) in terms of micrograms/petri plate for the extracts of the various biodiesel samples evaluated. \n\nThis dataset is associated with the following publication:\nDemarini, D., E. Mutlu, S. Warren, C. King, M. Gilmour, and W. Linak. Mutagenicity Emission Factors of Canola Oil and Waste Vegetable Oil Biodiesel:  Comparison to Soy Biodiesel.   Mutation Research / Genetic Toxicology and Environmental Mutagenesis. Elsevier Science Ltd, New York, NY, USA, 846: 1-8, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1503522",
-            "keyword": [
-                "Mutagenicity",
-                "biodiesel",
-                "canola oil",
-                "waste vegetable oil",
-                "emission factors"
-            ],
             "contactPoint": {
                 "fn": "David Demarini",
                 "hasEmail": "mailto:demarini.david@epa.gov"
             },
+            "description": "The data set show the number of bacterial mutant colonies (called revertants or rev) per petri plate and the dose of the extractable organic matter (EOM) in terms of micrograms/petri plate for the extracts of the various biodiesel samples evaluated. \n\nThis dataset is associated with the following publication:\nDemarini, D., E. Mutlu, S. Warren, C. King, M. Gilmour, and W. Linak. Mutagenicity Emission Factors of Canola Oil and Waste Vegetable Oil Biodiesel:  Comparison to Soy Biodiesel.   Mutation Research / Genetic Toxicology and Environmental Mutagenesis. Elsevier Science Ltd, New York, NY, USA, 846: 1-8, (2019).",
             "distribution": [
                 {
-                    "title": "Biodiesel Mutagenicity Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503522/Biodiesel%20Mutagenicity%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biodiesel Mutagenicity Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503522",
+            "keyword": [
+                "Mutagenicity",
+                "biodiesel",
+                "canola oil",
+                "waste vegetable oil",
+                "emission factors"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-07",
-            "references": [
-                "https://doi.org/10.1016/j.mrgentox.2019.05.013"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105903,66 +105897,66 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.mrgentox.2019.05.013"
+            ],
+            "rights": null,
+            "title": " Mutagenicity Emission Factors of canola Oil and Waste Vegetable Oil Biodiesel:  Comparison to Soy Biodiesel"
         },
         {
-            "title": "Model output and data used for analysis",
-            "description": "The modeled data in these archives are in the NetCDF format (https://www.unidata.ucar.edu/software/netcdf/). NetCDF (Network Common Data Form) is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. It is also a community standard for sharing scientific data. The Unidata Program Center supports and maintains netCDF programming interfaces for C, C++, Java, and Fortran. Programming interfaces are also available for Python, IDL, MATLAB, R, Ruby, and Perl.\nData in netCDF format is:\n\u2022\tSelf-Describing. A netCDF file includes information about the data it contains.\n\u2022\tPortable. A netCDF file can be accessed by computers with different ways of storing integers, characters, and floating-point numbers.\n\u2022\tScalable. Small subsets of large datasets in various formats may be accessed efficiently through netCDF interfaces, even from remote servers.\n\u2022\tAppendable. Data may be appended to a properly structured netCDF file without copying the dataset or redefining its structure.\n\u2022\tSharable. One writer and multiple readers may simultaneously access the same netCDF file.\n\u2022\tArchivable. Access to all earlier forms of netCDF data will be supported by current and future versions of the software.\nPub_figures.tar.zip \nContains the NCL scripts for figures 1-5 and Chesapeake Bay Airshed shapefile. The directory structure of the archive is ./Pub_figures/Fig#_data. Where # is the figure number from 1-5. \nEMISS.data.tar.zip \nThis archive contains two NetCDF files that contain the emission totals for 2011ec and 2040ei emission inventories. The name of the files contain the year of the inventory and the file header contains a description of each variable and the variable units. \nEPIC.data.tar.zip contains the monthly mean EPIC data in NetCDF format for ammonium fertilizer application (files with ANH3 in the name) and soil ammonium concentration (files with NH3 in the name) for historical (Hist directory) and future (RCP-4.5 directory) simulations.\nWRF.data.tar.zip contains mean monthly and seasonal data from the 36km downscaled WRF simulations in the NetCDF format for the historical (Hist directory) and future (RCP-4.5 directory) simulations. \nCMAQ.data.tar.zip contains the mean monthly and seasonal data in NetCDF format from the 36km CMAQ simulations for the historical (Hist directory), future (RCP-4.5 directory) and future with historical emissions (RCP-4.5-hist-emiss directory). \n\nThis dataset is associated with the following publication:\nCampbell, P., J. Bash, C. Nolte, T. Spero, E. Cooter, K. Hinson, and L. Linker. Projections of Atmospheric Nitrogen Deposition to the Chesapeake Bay Watershed.   Journal of Geophysical Research - Biogeosciences. American Geophysical Union, Washington, DC, USA, 12(11): 3307-3326, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500447",
-            "keyword": [
-                "CMAQ",
-                "Chesapeake Bay",
-                "TMDL",
-                "Nitrogen and Co-pollutants"
-            ],
             "contactPoint": {
                 "fn": "Jesse Bash",
                 "hasEmail": "mailto:bash.jesse@epa.gov"
             },
+            "description": "The modeled data in these archives are in the NetCDF format (https://www.unidata.ucar.edu/software/netcdf/). NetCDF (Network Common Data Form) is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. It is also a community standard for sharing scientific data. The Unidata Program Center supports and maintains netCDF programming interfaces for C, C++, Java, and Fortran. Programming interfaces are also available for Python, IDL, MATLAB, R, Ruby, and Perl.\nData in netCDF format is:\n\u2022\tSelf-Describing. A netCDF file includes information about the data it contains.\n\u2022\tPortable. A netCDF file can be accessed by computers with different ways of storing integers, characters, and floating-point numbers.\n\u2022\tScalable. Small subsets of large datasets in various formats may be accessed efficiently through netCDF interfaces, even from remote servers.\n\u2022\tAppendable. Data may be appended to a properly structured netCDF file without copying the dataset or redefining its structure.\n\u2022\tSharable. One writer and multiple readers may simultaneously access the same netCDF file.\n\u2022\tArchivable. Access to all earlier forms of netCDF data will be supported by current and future versions of the software.\nPub_figures.tar.zip \nContains the NCL scripts for figures 1-5 and Chesapeake Bay Airshed shapefile. The directory structure of the archive is ./Pub_figures/Fig#_data. Where # is the figure number from 1-5. \nEMISS.data.tar.zip \nThis archive contains two NetCDF files that contain the emission totals for 2011ec and 2040ei emission inventories. The name of the files contain the year of the inventory and the file header contains a description of each variable and the variable units. \nEPIC.data.tar.zip contains the monthly mean EPIC data in NetCDF format for ammonium fertilizer application (files with ANH3 in the name) and soil ammonium concentration (files with NH3 in the name) for historical (Hist directory) and future (RCP-4.5 directory) simulations.\nWRF.data.tar.zip contains mean monthly and seasonal data from the 36km downscaled WRF simulations in the NetCDF format for the historical (Hist directory) and future (RCP-4.5 directory) simulations. \nCMAQ.data.tar.zip contains the mean monthly and seasonal data in NetCDF format from the 36km CMAQ simulations for the historical (Hist directory), future (RCP-4.5 directory) and future with historical emissions (RCP-4.5-hist-emiss directory). \n\nThis dataset is associated with the following publication:\nCampbell, P., J. Bash, C. Nolte, T. Spero, E. Cooter, K. Hinson, and L. Linker. Projections of Atmospheric Nitrogen Deposition to the Chesapeake Bay Watershed.   Journal of Geophysical Research - Biogeosciences. American Geophysical Union, Washington, DC, USA, 12(11): 3307-3326, (2019).",
             "distribution": [
                 {
-                    "title": "Pub_figures.tar.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500447/Pub_figures.tar.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Pub_figures.tar.zip"
                 },
                 {
-                    "title": "EMISS.data.tar.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500447/EMISS.data.tar.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "EMISS.data.tar.zip"
                 },
                 {
-                    "title": "EPIC.data.tar.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500447/EPIC.data.tar.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "EPIC.data.tar.zip"
                 },
                 {
-                    "title": "WRF.data.tar.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500447/WRF.data.tar.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "WRF.data.tar.zip"
                 },
                 {
-                    "title": "CMAQ.data.tar.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500447/CMAQ.data.tar.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQ.data.tar.zip"
                 },
                 {
-                    "title": "Science hub metadata.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500447/Science%20hub%20metadata.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Science hub metadata.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500447",
+            "keyword": [
+                "CMAQ",
+                "Chesapeake Bay",
+                "TMDL",
+                "Nitrogen and Co-pollutants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-26",
-            "references": [
-                "https://doi.org/10.1029/2019jg005203"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -105972,41 +105966,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2019jg005203"
+            ],
+            "rights": null,
+            "title": "Model output and data used for analysis"
         },
         {
-            "title": "serrano A-sf8c data",
-            "description": "This dataset contains raw and reduced GC and LC data in an excel file. \n\nThis dataset is associated with the following publication:\nSerrano, J., R. Kolanczyk, M. Tapper, T. Lahren, N. Dongari, D. Hammermeister, P. Kosian, P. Schmieder, B. Sheedy, K. Challis, and A. Kubatova. Characterization and analysis of estrogenic cyclic phenone metabolites produced in vitro by rainbow trout liver slices using GC-MS, LC-MS and LC-TOF-MS.   Journal of Chromatography B. Elsevier Science Ltd, New York, NY, USA, 1126-1127: 1-12, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1517585",
-            "keyword": [
-                "cyclic phenones",
-                "Metabolism",
-                "fish",
-                "Vtg gene expression"
-            ],
             "contactPoint": {
                 "fn": "Jose Serrano",
                 "hasEmail": "mailto:serrano.jose@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517585/documents/Serrano%20asf8c_data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This dataset contains raw and reduced GC and LC data in an excel file. \n\nThis dataset is associated with the following publication:\nSerrano, J., R. Kolanczyk, M. Tapper, T. Lahren, N. Dongari, D. Hammermeister, P. Kosian, P. Schmieder, B. Sheedy, K. Challis, and A. Kubatova. Characterization and analysis of estrogenic cyclic phenone metabolites produced in vitro by rainbow trout liver slices using GC-MS, LC-MS and LC-TOF-MS.   Journal of Chromatography B. Elsevier Science Ltd, New York, NY, USA, 1126-1127: 1-12, (2019).",
             "distribution": [
                 {
-                    "title": "mass calculator cpk metabolites Serrano A-sf8c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1517585/mass%20calculator%20cpk%20metabolites%20Serrano%20A-sf8c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "mass calculator cpk metabolites Serrano A-sf8c.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517585",
+            "keyword": [
+                "cyclic phenones",
+                "Metabolism",
+                "fish",
+                "Vtg gene expression"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-01-10",
-            "references": [
-                "https://doi.org/10.1016/j.jchromb.2019.121717"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106017,43 +106013,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1517585/documents/Serrano%20asf8c_data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.jchromb.2019.121717"
+            ],
+            "rights": null,
+            "title": "serrano A-sf8c data"
         },
         {
-            "title": "Dataset of the influence of temperature on the emissions of organophosphate flame retardants from polyisocyanurate foam: measurement and modelling. ",
-            "description": "Dataset of the influence of temperature on the emissions of organophosphate flame retardants from polyisocyanurate foam: measurement and modelling. \n\nThis dataset is associated with the following publication:\nLiang, Y., X. Liu, and M. Allen. The Influence of Temperature on the Emissions of Organophosphate Ester Flame Retardants from Polyisocyanurate Foam: Measurement and Modeling.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 233: 347-354, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503218",
-            "keyword": [
-                "Organophosphate flame retardants (OPFRs)",
-                "Semivolatile Organic Compounds (SVOCs)",
-                "Chamber testing",
-                "Emission mechanism",
-                "Temperature influence"
-            ],
             "contactPoint": {
                 "fn": "Xiaoyu Liu",
                 "hasEmail": "mailto:liu.xiaoyu@epa.gov"
             },
+            "description": "Dataset of the influence of temperature on the emissions of organophosphate flame retardants from polyisocyanurate foam: measurement and modelling. \n\nThis dataset is associated with the following publication:\nLiang, Y., X. Liu, and M. Allen. The Influence of Temperature on the Emissions of Organophosphate Ester Flame Retardants from Polyisocyanurate Foam: Measurement and Modeling.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 233: 347-354, (2019).",
             "distribution": [
                 {
-                    "title": "Data Tables&Dictionary-20181206.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503218/Data%20Tables%26Dictionary-20181206.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Tables&Dictionary-20181206.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503218",
+            "keyword": [
+                "Organophosphate flame retardants (OPFRs)",
+                "Semivolatile Organic Compounds (SVOCs)",
+                "Chamber testing",
+                "Emission mechanism",
+                "Temperature influence"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-05",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2019.05.289"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106063,41 +106057,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2019.05.289"
+            ],
+            "rights": null,
+            "title": "Dataset of the influence of temperature on the emissions of organophosphate flame retardants from polyisocyanurate foam: measurement and modelling. "
         },
         {
-            "title": "The Effects of Roadside Vegetation Barrier Characteristics on Near-Road Air Quality",
-            "description": "Air quality and meteorological measurements collected in Woodside, California along a heavily-trafficked highway with and without an existing vegetation barrier.  The data includes fixed and mobile monitoring data collected by an electric vehicle for CO, NO2, black carbon and ultrafine particles. \n\nThis dataset is associated with the following publication:\nDeshmukh, P., V. Isakov, A. Venkatram, B. Yang, K. Zhang, R. Logan, and R. Baldauf. The Effects of Roadside Vegetation Characteristics on Local, Near-Road Air Quality.   Air Quality, Atmosphere & Health. Springer Netherlands,   NETHERLANDS, 12(3): 259-270, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1407528",
-            "keyword": [
-                "air quality",
-                "traffic",
-                "near-road",
-                "vegetation"
-            ],
             "contactPoint": {
                 "fn": "Richard Baldauf",
                 "hasEmail": "mailto:baldauf.richard@epa.gov"
             },
+            "description": "Air quality and meteorological measurements collected in Woodside, California along a heavily-trafficked highway with and without an existing vegetation barrier.  The data includes fixed and mobile monitoring data collected by an electric vehicle for CO, NO2, black carbon and ultrafine particles. \n\nThis dataset is associated with the following publication:\nDeshmukh, P., V. Isakov, A. Venkatram, B. Yang, K. Zhang, R. Logan, and R. Baldauf. The Effects of Roadside Vegetation Characteristics on Local, Near-Road Air Quality.   Air Quality, Atmosphere & Health. Springer Netherlands,   NETHERLANDS, 12(3): 259-270, (2018).",
             "distribution": [
                 {
-                    "title": "California2014study.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407528/California2014study.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "California2014study.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407528",
+            "keyword": [
+                "air quality",
+                "traffic",
+                "near-road",
+                "vegetation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-25",
-            "references": [
-                "https://doi.org/10.1007/s11869-018-0651-8"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106107,20 +106101,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11869-018-0651-8"
+            ],
+            "rights": null,
+            "title": "The Effects of Roadside Vegetation Barrier Characteristics on Near-Road Air Quality"
         },
         {
-            "title": "These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834",
-            "description": "These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834.  As such, it is a violation of Federal Law to publish them. Format: These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834. \n\nThis dataset is associated with the following publication:\nStiegel, M., J. Pleil, J. Sobus, T. Stevens, and M. Madden. Linking physiological parameters to perturbations in the human exposome: Environmental exposures modify blood pressure and lung function via inflammatory cytokine pathway.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 80(9): 485-501, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Joachim Pleil",
+                "hasEmail": "mailto:pleil.joachim@epa.gov"
+            },
+            "description": "These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834.  As such, it is a violation of Federal Law to publish them. Format: These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834. \n\nThis dataset is associated with the following publication:\nStiegel, M., J. Pleil, J. Sobus, T. Stevens, and M. Madden. Linking physiological parameters to perturbations in the human exposome: Environmental exposures modify blood pressure and lung function via inflammatory cytokine pathway.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 80(9): 485-501, (2017).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1389051",
             "keyword": [
                 "cytokine",
@@ -106128,14 +106126,10 @@
                 "exposure data",
                 "inflammatory response"
             ],
-            "contactPoint": {
-                "fn": "Joachim Pleil",
-                "hasEmail": "mailto:pleil.joachim@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2012-04-15",
-            "references": [
-                "https://doi.org/10.1080/15287394.2017.1330578"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106145,20 +106139,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/15287394.2017.1330578"
+            ],
+            "rights": null,
+            "title": "These data are from a human study collected under IRB protocol:  ClinicalTrials.gov # NCT01874834"
         },
         {
-            "title": "Dataset of firefighters absorption of PAHs and benzene during training exercises",
-            "description": "The dataset contains concentrations of toxicants in breath and urine collected from study participants. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: By contacting CDC/NIOSH. Format: The dataset contains concentrations of toxicants in breath and urine collected from study participants. \n\nThis dataset is associated with the following publication:\nFent, K., C. Toennis, D. Sammons, S. Robertson, S. Bertke, A. Calafat, J. Pleil, A. Wallace, S. Kerber, D. Smith, and G. Horn. Firefighters' and instructors\u2019 absorption of PAHs and benzene during training exercises.   INTERNATIONAL JOURNAL OF HYGIENE AND ENVIRONMENTAL HEALTH. Elsevier B.V., Amsterdam,  NETHERLANDS, 222(7): 991-1000, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Michelle Wallace",
+                "hasEmail": "mailto:wallace.ariel@epa.gov"
+            },
+            "description": "The dataset contains concentrations of toxicants in breath and urine collected from study participants. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: By contacting CDC/NIOSH. Format: The dataset contains concentrations of toxicants in breath and urine collected from study participants. \n\nThis dataset is associated with the following publication:\nFent, K., C. Toennis, D. Sammons, S. Robertson, S. Bertke, A. Calafat, J. Pleil, A. Wallace, S. Kerber, D. Smith, and G. Horn. Firefighters' and instructors\u2019 absorption of PAHs and benzene during training exercises.   INTERNATIONAL JOURNAL OF HYGIENE AND ENVIRONMENTAL HEALTH. Elsevier B.V., Amsterdam,  NETHERLANDS, 222(7): 991-1000, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1503338",
             "keyword": [
                 "firefighters",
@@ -106168,14 +106166,10 @@
                 "polycyclic aromatic hydrocarbons",
                 "benzene"
             ],
-            "contactPoint": {
-                "fn": "Michelle Wallace",
-                "hasEmail": "mailto:wallace.ariel@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-10-31",
-            "references": [
-                "https://doi.org/10.1016/j.ijheh.2019.06.006"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106185,76 +106179,78 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ijheh.2019.06.006"
+            ],
+            "rights": null,
+            "title": "Dataset of firefighters absorption of PAHs and benzene during training exercises"
         },
         {
-            "title": "Datasets for figures and tables",
-            "description": "Software\n\nModel simulations were conducted using WRF version 3.8.1 (available at https://github.com/NCAR/WRFV3) and CMAQ version 5.2.1 (available at https://github.com/USEPA/CMAQ). The meteorological and concentration fields created using these models are too large to archive on ScienceHub, approximately 1 TB, and are archived on EPA\u2019s high performance computing archival system (ASM) at /asm/MOD3APP/pcc/02.NOAH.v.CLM.v.PX/. \n\nFigures\n\nFigures 1 \u2013 6 and Figure 8: Created using the NCAR Command Language (NCL) scripts (https://www.ncl.ucar.edu/get_started.shtml). NCLD code can be downloaded from the NCAR website (https://www.ncl.ucar.edu/Download/) at no cost. The data used for these figures are archived on EPA\u2019s ASM system and are available upon request.\n\nFigures 7, 8b-c, 8e-f, 8h-i, and 9 were created using the AMET utility developed by U.S. EPA/ORD. AMET can be freely downloaded and used at https://github.com/USEPA/AMET. The modeled data paired in space and time provided in this archive can be used to recreate these figures. \n\nThe data contained in the compressed zip files are organized in comma delimited files with descriptive headers or space delimited files that match tabular data in the manuscript. The data dictionary provides additional information about the files and their contents. \n\nThis dataset is associated with the following publication:\nCampbell, P., J. Bash, and T. Spero. Updates to the Noah Land Surface Model in WRF\u2010CMAQ to Improve Simulated Meteorology, Air Quality, and Deposition.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 11(1): 231-256, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500022",
-            "keyword": [
-                "air quality",
-                "CMAQ",
-                "WRF-CMAQ",
-                "chemistry-meteorology"
-            ],
             "contactPoint": {
                 "fn": "Jesse Bash",
                 "hasEmail": "mailto:bash.jesse@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500022/documents/Science%20hub%20metadata.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Software\n\nModel simulations were conducted using WRF version 3.8.1 (available at https://github.com/NCAR/WRFV3) and CMAQ version 5.2.1 (available at https://github.com/USEPA/CMAQ). The meteorological and concentration fields created using these models are too large to archive on ScienceHub, approximately 1 TB, and are archived on EPA\u2019s high performance computing archival system (ASM) at /asm/MOD3APP/pcc/02.NOAH.v.CLM.v.PX/. \n\nFigures\n\nFigures 1 \u2013 6 and Figure 8: Created using the NCAR Command Language (NCL) scripts (https://www.ncl.ucar.edu/get_started.shtml). NCLD code can be downloaded from the NCAR website (https://www.ncl.ucar.edu/Download/) at no cost. The data used for these figures are archived on EPA\u2019s ASM system and are available upon request.\n\nFigures 7, 8b-c, 8e-f, 8h-i, and 9 were created using the AMET utility developed by U.S. EPA/ORD. AMET can be freely downloaded and used at https://github.com/USEPA/AMET. The modeled data paired in space and time provided in this archive can be used to recreate these figures. \n\nThe data contained in the compressed zip files are organized in comma delimited files with descriptive headers or space delimited files that match tabular data in the manuscript. The data dictionary provides additional information about the files and their contents. \n\nThis dataset is associated with the following publication:\nCampbell, P., J. Bash, and T. Spero. Updates to the Noah Land Surface Model in WRF\u2010CMAQ to Improve Simulated Meteorology, Air Quality, and Deposition.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 11(1): 231-256, (2019).",
             "distribution": [
                 {
-                    "title": "A1_AMON.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/A1_AMON.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "A1_AMON.zip"
                 },
                 {
-                    "title": "A6_AMON.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/A6_AMON.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "A6_AMON.zip"
                 },
                 {
-                    "title": "A1_AQS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/A1_AQS.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "A1_AQS.zip"
                 },
                 {
-                    "title": "A1_IMPROVE.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/A1_IMPROVE.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "A1_IMPROVE.zip"
                 },
                 {
-                    "title": "A6_IMPROVE.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/A6_IMPROVE.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "A6_IMPROVE.zip"
                 },
                 {
-                    "title": "A6_AQS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/A6_AQS.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "A6_AQS.zip"
                 },
                 {
-                    "title": "A7_IMPROVE.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/A7_IMPROVE.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "A7_IMPROVE.zip"
                 },
                 {
-                    "title": "Soil_veg_data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500022/Soil_veg_data.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Soil_veg_data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500022",
+            "keyword": [
+                "air quality",
+                "CMAQ",
+                "WRF-CMAQ",
+                "chemistry-meteorology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-12-28",
-            "references": [
-                "https://doi.org/10.1029/2018ms001422"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106265,43 +106261,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500022/documents/Science%20hub%20metadata.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1029/2018ms001422"
+            ],
+            "rights": null,
+            "title": "Datasets for figures and tables"
         },
         {
-            "title": "Annual PM2.5 and cardiovascular mortality rate data: Trends modified by county socioeconomic status in 2,132 US counties",
-            "description": "Data on county socioeconomic status for 2,132 US counties and each county\u2019s average annual cardiovascular mortality rate (CMR) and total PM2.5 concentration for 21 years (1990-2010). County CMR, PM2.5, and socioeconomic data were obtained from the U.S. National Center for Health Statistics, U.S. Environmental Protection Agency\u2019s Community Multiscale Air Quality modeling system, and the U.S. Census, respectively. A socioeconomic index was created using seven county-level measures from the 1990 US census using factor analysis. Quintiles of this index were used to generate categories of county socioeconomic status. \n\nThis dataset is associated with the following publication:\nWyatt, L., G. Peterson, T. Wade, L. Neas, and A. Rappold. The contribution of improved air quality to reduced cardiovascular mortality: Declines in socioeconomic differences over time.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 136: 105430, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1506014",
-            "keyword": [
-                "mortality",
-                "cardiovascular",
-                "air pollution",
-                "particulate matter",
-                "socioeconomic status"
-            ],
             "contactPoint": {
                 "fn": "Ana Rappold",
                 "hasEmail": "mailto:rappold.ana@epa.gov"
             },
+            "description": "Data on county socioeconomic status for 2,132 US counties and each county\u2019s average annual cardiovascular mortality rate (CMR) and total PM2.5 concentration for 21 years (1990-2010). County CMR, PM2.5, and socioeconomic data were obtained from the U.S. National Center for Health Statistics, U.S. Environmental Protection Agency\u2019s Community Multiscale Air Quality modeling system, and the U.S. Census, respectively. A socioeconomic index was created using seven county-level measures from the 1990 US census using factor analysis. Quintiles of this index were used to generate categories of county socioeconomic status. \n\nThis dataset is associated with the following publication:\nWyatt, L., G. Peterson, T. Wade, L. Neas, and A. Rappold. The contribution of improved air quality to reduced cardiovascular mortality: Declines in socioeconomic differences over time.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 136: 105430, (2020).",
             "distribution": [
                 {
-                    "title": "SES_PM25_CMR_data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506014/SES_PM25_CMR_data.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "SES_PM25_CMR_data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1506014",
+            "keyword": [
+                "mortality",
+                "cardiovascular",
+                "air pollution",
+                "particulate matter",
+                "socioeconomic status"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-11-04",
-            "references": [
-                "https://doi.org/10.1016/j.envint.2019.105430"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106311,19 +106305,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envint.2019.105430"
+            ],
+            "rights": null,
+            "title": "Annual PM2.5 and cardiovascular mortality rate data: Trends modified by county socioeconomic status in 2,132 US counties"
         },
         {
-            "title": "Multigene biomarkers of pyrethroid exposure: exploratory experiments",
-            "description": "Gene expression microarray measurements in Pimephales promelas before and after pyrethroid exposure. \n\nThis dataset is associated with the following publication:\nKostich, M., D. Bencic, A. Batt, M. See, R. Flick, D. Gordon, J. Lazorchak, and A. Biales. Multigene Biomarkers of Pyrethroid Exposure: Exploratory Experiments.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 38(11): 2436-2466, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Mitchell Kostich",
+                "hasEmail": "mailto:kostich.mitchell@epa.gov"
+            },
+            "description": "Gene expression microarray measurements in Pimephales promelas before and after pyrethroid exposure. \n\nThis dataset is associated with the following publication:\nKostich, M., D. Bencic, A. Batt, M. See, R. Flick, D. Gordon, J. Lazorchak, and A. Biales. Multigene Biomarkers of Pyrethroid Exposure: Exploratory Experiments.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 38(11): 2436-2466, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE113286",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE113286"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500894",
             "keyword": [
@@ -106333,19 +106336,10 @@
                 "microarray",
                 "pyrethroid"
             ],
-            "contactPoint": {
-                "fn": "Mitchell Kostich",
-                "hasEmail": "mailto:kostich.mitchell@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE113286",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE113286"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-17",
-            "references": [
-                "https://doi.org/10.1002/etc.4552"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106355,20 +106349,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4552"
+            ],
+            "rights": null,
+            "title": "Multigene biomarkers of pyrethroid exposure: exploratory experiments"
         },
         {
-            "title": "Dataset for Exploring case-control samples with non-targeted analysis",
-            "description": "These data contain the results of GC-MS, LC-MS and immunochemistry analyses of mask sample extracts. The data include tentatively identified compounds through library searches and compound abundance. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: The data can not be accessed. Format: The dataset contains the identification of compounds found in the mask samples as well as the abundance of those compounds for individuals who participated in the trial. \n\nThis dataset is associated with the following publication:\nPleil, J., M. Wallace, J. McCord, M. Madden, J. Sobus, and G. Ferguson. How do cancer-sniffing dogs sort biological samples? Exploring case-control samples with non-targeted LC-Orbitrap, GC-MS, and immunochemistry methods.   Journal of Breath Research. Institute of Physics Publishing, Bristol,  UK, 14(1): 016006, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Joachim Pleil",
+                "hasEmail": "mailto:pleil.joachim@epa.gov"
+            },
+            "description": "These data contain the results of GC-MS, LC-MS and immunochemistry analyses of mask sample extracts. The data include tentatively identified compounds through library searches and compound abundance. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: The data can not be accessed. Format: The dataset contains the identification of compounds found in the mask samples as well as the abundance of those compounds for individuals who participated in the trial. \n\nThis dataset is associated with the following publication:\nPleil, J., M. Wallace, J. McCord, M. Madden, J. Sobus, and G. Ferguson. How do cancer-sniffing dogs sort biological samples? Exploring case-control samples with non-targeted LC-Orbitrap, GC-MS, and immunochemistry methods.   Journal of Breath Research. Institute of Physics Publishing, Bristol,  UK, 14(1): 016006, (2019).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1503685",
             "keyword": [
                 "Pre-clinical cancer",
@@ -106377,14 +106375,10 @@
                 "immunochemistry",
                 "case-control analysis"
             ],
-            "contactPoint": {
-                "fn": "Joachim Pleil",
-                "hasEmail": "mailto:pleil.joachim@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-15",
-            "references": [
-                "https://doi.org/10.1088/1752-7163/ab433a"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106394,62 +106388,62 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1752-7163/ab433a"
+            ],
+            "rights": null,
+            "title": "Dataset for Exploring case-control samples with non-targeted analysis"
         },
         {
-            "title": "data sets for Nano TiO2 & CeO2 effects on BEAS-2B cells",
-            "description": "Signaling pathways  from IPA:  canonical pathways obtained by uploading differentially expressed genes onto IPA to get the corresponding pathways altered by the chemicals.\n\nFigure 4 ABCDHILM ROS final:  Excel file with raw data and calculated fold change for the ROS (Deep Red) assay on 8 nanoparticles.\n\nData files for tables:  this file include physical-chemical properties of the 8 NPs (worksheet 1), sizing and zeta potential from zeta sizer (worksheet 2&3) and numbers of differentially expressed genes (DEGs) (worksheet 4).\n\nData files for figure 5 to 11:  physical -chemical properties of the NPs, raw data and calculation for ROS-RNS, 8-oxo-dG, AP sites, endogenous DNA adducts, 4-HNE, and MDA adducts. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, G. Nelson, B. Vallanat, M. Killius, J. Crooks, w. Ward, C. Blackman, and J. Ross. Differential effects of Nano TiO2 and CeO2 on normal human lung epithelial cells in vitro.   Journal of Nanoscience and Nanotechnology. American Scientific Publishers, VALENCIA, CA, USA, 19(11): 6907-6923, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1502468",
-            "keyword": [
-                "engineered nanomaterials",
-                "transcriptomics",
-                "signaling pathways analysis",
-                "DNA damage assays",
-                "Reactive oxygen species"
-            ],
             "contactPoint": {
                 "fn": "Sheau-Fung Thai",
                 "hasEmail": "mailto:thai.sheau-fung@epa.gov"
             },
+            "description": "Signaling pathways  from IPA:  canonical pathways obtained by uploading differentially expressed genes onto IPA to get the corresponding pathways altered by the chemicals.\n\nFigure 4 ABCDHILM ROS final:  Excel file with raw data and calculated fold change for the ROS (Deep Red) assay on 8 nanoparticles.\n\nData files for tables:  this file include physical-chemical properties of the 8 NPs (worksheet 1), sizing and zeta potential from zeta sizer (worksheet 2&3) and numbers of differentially expressed genes (DEGs) (worksheet 4).\n\nData files for figure 5 to 11:  physical -chemical properties of the NPs, raw data and calculation for ROS-RNS, 8-oxo-dG, AP sites, endogenous DNA adducts, 4-HNE, and MDA adducts. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, G. Nelson, B. Vallanat, M. Killius, J. Crooks, w. Ward, C. Blackman, and J. Ross. Differential effects of Nano TiO2 and CeO2 on normal human lung epithelial cells in vitro.   Journal of Nanoscience and Nanotechnology. American Scientific Publishers, VALENCIA, CA, USA, 19(11): 6907-6923, (2019).",
             "distribution": [
                 {
-                    "title": "data files for figures.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502468/data%20files%20for%20figures.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "data files for figures.xlsx"
                 },
                 {
-                    "title": "Figure 1-3.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502468/Figure%201-3.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Figure 1-3.docx"
                 },
                 {
-                    "title": "Copy of signaling pathways from IPA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502468/Copy%20of%20signaling%20pathways%20from%20IPA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of signaling pathways from IPA.xlsx"
                 },
                 {
-                    "title": "copy of table for 7 nano on BEAS2B 5-9-18.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502468/copy%20of%20table%20for%207%20nano%20on%20BEAS2B%205-9-18.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "copy of table for 7 nano on BEAS2B 5-9-18.xlsx"
                 },
                 {
-                    "title": "Copy of figur 4 Nano ABCDHILM ROS final.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502468/Copy%20of%20figur%204%20Nano%20ABCDHILM%20ROS%20final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of figur 4 Nano ABCDHILM ROS final.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502468",
+            "keyword": [
+                "engineered nanomaterials",
+                "transcriptomics",
+                "signaling pathways analysis",
+                "DNA damage assays",
+                "Reactive oxygen species"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-09",
-            "references": [
-                "https://doi.org/10.1166/jnn.2019.16737"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106459,93 +106453,93 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1166/jnn.2019.16737"
+            ],
+            "rights": null,
+            "title": "data sets for Nano TiO2 & CeO2 effects on BEAS-2B cells"
         },
         {
-            "title": "Arsenic Safe Drinking Water Information System (SDWIS) Federal Reports Advanced Search Tool ",
-            "description": "This data includes information on Arsenic violations in the US, including time patterns and spatial patterns in Arsenic violations, and people served by systems in violation. Most of the data is from the Safe Drinking Water Information System. \n\nThis dataset is associated with the following publication:\nFoster, S., M. Pennino, J. Compton, S. Leibowitz, and M. Kile. Arsenic Drinking Water Violations Decreased Across the United States Following Revision of the Maximum Contaminant Level..   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(19): 11478-11485, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1503345",
-            "keyword": [
-                "drinking water",
-                "nitrate",
-                "nitrate in groundwater",
-                "maximum contaminant level",
-                "surface water",
-                "public water systems"
-            ],
             "contactPoint": {
                 "fn": "Michael Pennino",
                 "hasEmail": "mailto:pennino.michael@epa.gov"
             },
+            "description": "This data includes information on Arsenic violations in the US, including time patterns and spatial patterns in Arsenic violations, and people served by systems in violation. Most of the data is from the Safe Drinking Water Information System. \n\nThis dataset is associated with the following publication:\nFoster, S., M. Pennino, J. Compton, S. Leibowitz, and M. Kile. Arsenic Drinking Water Violations Decreased Across the United States Following Revision of the Maximum Contaminant Level..   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(19): 11478-11485, (2019).",
             "distribution": [
                 {
-                    "title": "SDWIS_As_Violations_Over_Time_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_As_Violations_Over_Time_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_As_Violations_Over_Time_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_As_Violation_Duration_State_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_As_Violation_Duration_State_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_As_Violation_Duration_State_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_As_Pop_Served_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_As_Pop_Served_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_As_Pop_Served_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_As_Violations_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_As_Violations_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_As_Violations_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "Mean_Annual_As_Violations_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/Mean_Annual_As_Violations_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mean_Annual_As_Violations_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "Mean_Annual_As_Pop_Served_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/Mean_Annual_As_Pop_Served_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mean_Annual_As_Pop_Served_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_GW_As_Violations_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_GW_As_Violations_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_GW_As_Violations_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_Percent_GW_As_Violations_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_Percent_GW_As_Violations_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_Percent_GW_As_Violations_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_Percent_GWSW_As_Violations_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_Percent_GWSW_As_Violations_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_Percent_GWSW_As_Violations_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_Percent_SW_As_Violations_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_Percent_SW_As_Violations_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_Percent_SW_As_Violations_County_2006-2017_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_SW_As_Violations_County_2006-2017_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503345/SDWIS_SW_As_Violations_County_2006-2017_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_SW_As_Violations_County_2006-2017_FINAL.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503345",
+            "keyword": [
+                "drinking water",
+                "nitrate",
+                "nitrate in groundwater",
+                "maximum contaminant level",
+                "surface water",
+                "public water systems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-12-21",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b02358"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106555,47 +106549,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b02358"
+            ],
+            "rights": null,
+            "title": "Arsenic Safe Drinking Water Information System (SDWIS) Federal Reports Advanced Search Tool "
         },
         {
-            "title": "Hypothetical Aggregate Exposure Pathway Network",
-            "description": "This data set contains R code for a hypothetical exposure model described in the manuscript \"A quantitative source-to-outcome case study to demonstrate the integration of human health and ecological endpoints using the Aggregate Exposure Pathway and Adverse Outcome Pathway frameworks\".  Additionally, this data set contains an Excel file that provides the range of parameters used in Monte Carlo simulations to generate iterations of the exposure network. \n\nThis dataset is associated with the following publication:\nHines, D., R. Conolly, and A. Jarabek. A quantitative source-to-outcome case study to demonstrate the integration of human health and ecological endpoints using the Aggregate Exposure Pathway and Adverse Outcome Pathway frameworks.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(8): 11002-11012, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1502543",
-            "keyword": [
-                "Aggregate exposure",
-                "cumulative risk assessment",
-                "adverse outcome pathway",
-                "environmental exposure",
-                "Aggregate Exposure Pathway"
-            ],
             "contactPoint": {
                 "fn": "David Hines",
                 "hasEmail": "mailto:hines.david@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502543/documents/Data%20Dictionary_final.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This data set contains R code for a hypothetical exposure model described in the manuscript \"A quantitative source-to-outcome case study to demonstrate the integration of human health and ecological endpoints using the Aggregate Exposure Pathway and Adverse Outcome Pathway frameworks\".  Additionally, this data set contains an Excel file that provides the range of parameters used in Monte Carlo simulations to generate iterations of the exposure network. \n\nThis dataset is associated with the following publication:\nHines, D., R. Conolly, and A. Jarabek. A quantitative source-to-outcome case study to demonstrate the integration of human health and ecological endpoints using the Aggregate Exposure Pathway and Adverse Outcome Pathway frameworks.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(8): 11002-11012, (2019).",
             "distribution": [
                 {
-                    "title": "AEP_ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502543/AEP_ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AEP_ScienceHub.xlsx"
                 },
                 {
-                    "title": "AEP_SciHub.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502543/AEP_SciHub.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "AEP_SciHub.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502543",
+            "keyword": [
+                "Aggregate exposure",
+                "cumulative risk assessment",
+                "adverse outcome pathway",
+                "environmental exposure",
+                "Aggregate Exposure Pathway"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-08-06",
-            "references": [
-                "https://doi.org/10.1021/acs.est.9b04639"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106606,124 +106602,122 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502543/documents/Data%20Dictionary_final.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/acs.est.9b04639"
+            ],
+            "rights": null,
+            "title": "Hypothetical Aggregate Exposure Pathway Network"
         },
         {
-            "title": "Enhancement of RNA from  FFPE v27.2",
-            "description": "This data set is composed of Tables, Figures, zip file containing the whole manuscript individual datasets. \n\nThis dataset is associated with the following publication:\nWehmas, L., C. Wood, B. Chorley, C. Yauk, G. Nelson, and S. Hester. Enhanced Quality Metrics for Assessing RNA Derived From Archival Formalin-Fixed Paraffin-Embedded Tissue Samples.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  170(2): 357-373, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1506036",
-            "keyword": [
-                "quality metrics"
-            ],
             "contactPoint": {
                 "fn": "Susan Hester",
                 "hasEmail": "mailto:hester.susan@epa.gov"
             },
+            "description": "This data set is composed of Tables, Figures, zip file containing the whole manuscript individual datasets. \n\nThis dataset is associated with the following publication:\nWehmas, L., C. Wood, B. Chorley, C. Yauk, G. Nelson, and S. Hester. Enhanced Quality Metrics for Assessing RNA Derived From Archival Formalin-Fixed Paraffin-Embedded Tissue Samples.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  170(2): 357-373, (2019).",
             "distribution": [
                 {
-                    "title": "Wehmas_to_Linda_Adams Fig&text&tables.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Wehmas_to_Linda_Adams%20Fig%26text%26tables.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Wehmas_to_Linda_Adams Fig&text&tables.zip"
                 },
                 {
-                    "title": "Enhancement of RNA from FFPE_v27.2_clean_20171115.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Enhancement%20of%20RNA%20from%20FFPE_v27.2_clean_20171115.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Enhancement of RNA from FFPE_v27.2_clean_20171115.docx"
                 },
                 {
-                    "title": "Enhancement of RNA from FFPE_v27.2_marked_20171115.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Enhancement%20of%20RNA%20from%20FFPE_v27.2_marked_20171115.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Enhancement of RNA from FFPE_v27.2_marked_20171115.docx"
                 },
                 {
-                    "title": "Table_1_DEG_overlap_20171024.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_1_DEG_overlap_20171024.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_1_DEG_overlap_20171024.xlsx"
                 },
                 {
-                    "title": "Table_S1_triplex_RT-qPCR_primers_20170829.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S1_triplex_RT-qPCR_primers_20170829.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S1_triplex_RT-qPCR_primers_20170829.xlsx"
                 },
                 {
-                    "title": "Table_2_IPA_overlap_20170731.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_2_IPA_overlap_20170731.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_2_IPA_overlap_20170731.xlsx"
                 },
                 {
-                    "title": "Table_S2_Library_prep_fragmentation_times_20170731.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S2_Library_prep_fragmentation_times_20170731.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S2_Library_prep_fragmentation_times_20170731.xlsx"
                 },
                 {
-                    "title": "Table_S4_Actb_amplicon_summary_20170731.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S4_Actb_amplicon_summary_20170731.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S4_Actb_amplicon_summary_20170731.xlsx"
                 },
                 {
-                    "title": "Table_S5_sequencing_quality_metrics_20171031_clean.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S5_sequencing_quality_metrics_20171031_clean.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S5_sequencing_quality_metrics_20171031_clean.xlsx"
                 },
                 {
-                    "title": "Table_S3_RNA_and_RNA_quality_20171031_clean.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S3_RNA_and_RNA_quality_20171031_clean.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S3_RNA_and_RNA_quality_20171031_clean.xlsx"
                 },
                 {
-                    "title": "Table_S7_differentially_expressed_genes_20171031.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S7_differentially_expressed_genes_20171031.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S7_differentially_expressed_genes_20171031.xlsx"
                 },
                 {
-                    "title": "Table_S8_overlapping_deg_lists_vs_fr_20171031.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S8_overlapping_deg_lists_vs_fr_20171031.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S8_overlapping_deg_lists_vs_fr_20171031.xlsx"
                 },
                 {
-                    "title": "Table_S6_total_and_unique_raw_gene_ct_summary_20171031.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S6_total_and_unique_raw_gene_ct_summary_20171031.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S6_total_and_unique_raw_gene_ct_summary_20171031.xlsx"
                 },
                 {
-                    "title": "Table_S10_Canonical_pathways_ranked_20171031_rev.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S10_Canonical_pathways_ranked_20171031_rev.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S10_Canonical_pathways_ranked_20171031_rev.xlsx"
                 },
                 {
-                    "title": "Table_S9_raw_normalized_biomarker_counts_20171031.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S9_raw_normalized_biomarker_counts_20171031.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S9_raw_normalized_biomarker_counts_20171031.xlsx"
                 },
                 {
-                    "title": "Table_S11_Linear_regression_analysis_pathway_upstream_regulators_20171031.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S11_Linear_regression_analysis_pathway_upstream_regulators_20171031.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S11_Linear_regression_analysis_pathway_upstream_regulators_20171031.xlsx"
                 },
                 {
-                    "title": "Table_S12_Upstream_regulator_rank_20171031.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S12_Upstream_regulator_rank_20171031.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S12_Upstream_regulator_rank_20171031.xlsx"
                 },
                 {
-                    "title": "Table_S13_Casual_network_analysis_20171031.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506036/Table_S13_Casual_network_analysis_20171031.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_S13_Casual_network_analysis_20171031.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1506036",
+            "keyword": [
+                "quality metrics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-06-28",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfz113"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106733,19 +106727,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfz113"
+            ],
+            "rights": null,
+            "title": "Enhancement of RNA from  FFPE v27.2"
         },
         {
-            "title": "Datasets for PUC paper 09182018",
-            "description": "Datasets associated with the publication \"Establishing a System of Consumer Products Categories to Support Rapid Modeling of Human Exposure\". \n\nThis dataset is associated with the following publication:\nIsaacs, K., K. Dionisio, K. Phillips, C. Bevington, P. Egeghy, and P. Price. Establishing a system of consumer product use categories to support rapid modeling of human exposure.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 30: 171-183, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Kristin Isaacs",
+                "hasEmail": "mailto:isaacs.kristin@epa.gov"
+            },
+            "description": "Datasets associated with the publication \"Establishing a System of Consumer Products Categories to Support Rapid Modeling of Human Exposure\". \n\nThis dataset is associated with the following publication:\nIsaacs, K., K. Dionisio, K. Phillips, C. Bevington, P. Egeghy, and P. Price. Establishing a system of consumer product use categories to support rapid modeling of human exposure.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 30: 171-183, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503034/ScienceHub_Datasets_09182018.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHub_Datasets_09182018.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1503034",
             "keyword": [
@@ -106756,20 +106760,10 @@
                 "HEM",
                 "Exposure Assessment"
             ],
-            "contactPoint": {
-                "fn": "Kristin Isaacs",
-                "hasEmail": "mailto:isaacs.kristin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ScienceHub_Datasets_09182018.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503034/ScienceHub_Datasets_09182018.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-18",
-            "references": [
-                "https://doi.org/10.1038/s41370-019-0187-5"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106779,39 +106773,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-019-0187-5"
+            ],
+            "rights": null,
+            "title": "Datasets for PUC paper 09182018"
         },
         {
-            "title": "Model code, tech manual, and model input files",
-            "description": "The Agent-Based Model of Human Activity Patterns (ABMHAP): Documentation and Users Guide. \n\nThis dataset is associated with the following publication:\nBrandon, N., and P. Price. Calibrating an agent-based model of longitudinal human activity patterns using the Consolidated Human Activity Database.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 30: 194\u2013204, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1503651",
-            "keyword": [
-                "Computational exposure",
-                "agent based modeling",
-                "human behavior"
-            ],
             "contactPoint": {
                 "fn": "Paul Price",
                 "hasEmail": "mailto:price.pauls@epa.gov"
             },
+            "description": "The Agent-Based Model of Human Activity Patterns (ABMHAP): Documentation and Users Guide. \n\nThis dataset is associated with the following publication:\nBrandon, N., and P. Price. Calibrating an agent-based model of longitudinal human activity patterns using the Consolidated Human Activity Database.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 30: 194\u2013204, (2020).",
             "distribution": [
                 {
-                    "title": "https://github.com/HumanExposure/AgentBasedModel",
-                    "accessURL": "https://github.com/HumanExposure/AgentBasedModel"
+                    "accessURL": "https://github.com/HumanExposure/AgentBasedModel",
+                    "title": "https://github.com/HumanExposure/AgentBasedModel"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503651",
+            "keyword": [
+                "Computational exposure",
+                "agent based modeling",
+                "human behavior"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-03-14",
-            "references": [
-                "https://doi.org/10.1038/s41370-019-0156-z"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106821,39 +106815,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-019-0156-z"
+            ],
+            "rights": null,
+            "title": "Model code, tech manual, and model input files"
         },
         {
-            "title": "Model code, tech manual, and model input files",
-            "description": "The GitHub repository includes the model code, an annotated description of the code and technical manual. Copies of input files used to generate the published results are also included. This file also contains the data for the modeling reported in a second publication \"Brandon, Namdi, and Paul S. Price. \"Calibrating an agent-based model of longitudinal human activity patterns using the Consolidated Human Activity Database.\" Journal of exposure science & environmental epidemiology (2019): 1-11\". \n\nThis dataset is associated with the following publication:\nBrandon, N., K. Dionisio, K. Isaacs, R. Tornero-Velez, D. Kapraun, W. Setzer, and P. Price. Simulating exposure-related behaviors using agent-based models embedded with needs-based artificial intelligence.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 30: 184\u2013193, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1517574",
-            "keyword": [
-                "Agent-Based Model",
-                "Computational exposure",
-                "human behavior"
-            ],
             "contactPoint": {
                 "fn": "Paul Price",
                 "hasEmail": "mailto:price.pauls@epa.gov"
             },
+            "description": "The GitHub repository includes the model code, an annotated description of the code and technical manual. Copies of input files used to generate the published results are also included. This file also contains the data for the modeling reported in a second publication \"Brandon, Namdi, and Paul S. Price. \"Calibrating an agent-based model of longitudinal human activity patterns using the Consolidated Human Activity Database.\" Journal of exposure science & environmental epidemiology (2019): 1-11\". \n\nThis dataset is associated with the following publication:\nBrandon, N., K. Dionisio, K. Isaacs, R. Tornero-Velez, D. Kapraun, W. Setzer, and P. Price. Simulating exposure-related behaviors using agent-based models embedded with needs-based artificial intelligence.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 30: 184\u2013193, (2020).",
             "distribution": [
                 {
-                    "title": "https://github.com/HumanExposure/AgentBasedModel",
-                    "accessURL": "https://github.com/HumanExposure/AgentBasedModel"
+                    "accessURL": "https://github.com/HumanExposure/AgentBasedModel",
+                    "title": "https://github.com/HumanExposure/AgentBasedModel"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517574",
+            "keyword": [
+                "Agent-Based Model",
+                "Computational exposure",
+                "human behavior"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-25",
-            "references": [
-                "https://doi.org/10.1038/s41370-018-0052-y"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106863,19 +106857,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-018-0052-y"
+            ],
+            "rights": null,
+            "title": "Model code, tech manual, and model input files"
         },
         {
-            "title": "3rd gen wheat data repository",
-            "description": "Data show the effects of nano CeO2 particles on the nutrient contents and stable isotopes of wheat plants over 3 generations of exposure. \n\nThis dataset is associated with the following publication:\nRico, C.M., O.M. Abolade, D. Wagner, B. Lottes, J. Rodriguez, R. Biagioni, and C. Andersen. Wheat exposure to cerium oxide nanoparticles over three generations reveals transmissible changes in nutrition, biochemical pools, and response to soil N.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 384: 121364, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Christian Andersen",
+                "hasEmail": "mailto:andersen.christian@epa.gov"
+            },
+            "description": "Data show the effects of nano CeO2 particles on the nutrient contents and stable isotopes of wheat plants over 3 generations of exposure. \n\nThis dataset is associated with the following publication:\nRico, C.M., O.M. Abolade, D. Wagner, B. Lottes, J. Rodriguez, R. Biagioni, and C. Andersen. Wheat exposure to cerium oxide nanoparticles over three generations reveals transmissible changes in nutrition, biochemical pools, and response to soil N.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 384: 121364, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504184/3rd%20Gen%20Wheat%20Data%20Repository%20-%20USEPA.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "3rd Gen Wheat Data Repository - USEPA.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1504184",
             "keyword": [
@@ -106886,20 +106890,10 @@
                 "nitrogen",
                 "engineered nanomaterials (ENMs)"
             ],
-            "contactPoint": {
-                "fn": "Christian Andersen",
-                "hasEmail": "mailto:andersen.christian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "3rd Gen Wheat Data Repository - USEPA.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504184/3rd%20Gen%20Wheat%20Data%20Repository%20-%20USEPA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-12",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2019.121364"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106909,70 +106903,70 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2019.121364"
+            ],
+            "rights": null,
+            "title": "3rd gen wheat data repository"
         },
         {
-            "title": "New bidirectional ammonia flux model in an air quality model coupled with an agricultural model",
-            "description": "L1_cation.txt is a text dump of CEC data from EPIC output for the 12 km CMAQ grid for each of 42 crop types\n\nCMAQv53_bidi_fix_NH3_290871_scatterplot.csv is data table used for scatter plot of observed vs AMoN NH3 concentrations shown is fig 5 in the paper\n\nCMAQv53_bidi_fix_PM25_NH4_494657_spatialplot_diff.csv is the data table used to produce the spatial plot of the biases in modeled ammonium PM2.5 (\uf06dg m-3) compared to CSN (circles), CASTNet (triangles), and SEARCH (squares) networks averaged over May to September 2016 as shown in Fig6.\n\nCMAQv53_bidi_fix_PM25_SO4_886932_spatialplot_diff.csv   is the data table used to produce the spatial plot of the biases in modeled sulfate PM2.5 (\uf06dg m-3) compared to IMPROVE (circles), CSN (triangles), CASTNET (squares), and SEARCH (diamonds) networks averaged over May to September 2016. \n\nThis dataset is associated with the following publication:\nPleim, J., L. Ran, K. Appel, M. Shephard, and K. Cady-Pereira. New Bidirectional Ammonia Flux Model in an Air Quality Model Coupled With an Agricultural Model.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 11(9): 2934-2957, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504167",
-            "keyword": [
-                "Ammonia concentrations and fluxes",
-                "ammonia",
-                "Community Multi-scale Air Quality (CMAQ) model"
-            ],
             "contactPoint": {
                 "fn": "Jonathan Pleim",
                 "hasEmail": "mailto:pleim.jon@epa.gov"
             },
+            "description": "L1_cation.txt is a text dump of CEC data from EPIC output for the 12 km CMAQ grid for each of 42 crop types\n\nCMAQv53_bidi_fix_NH3_290871_scatterplot.csv is data table used for scatter plot of observed vs AMoN NH3 concentrations shown is fig 5 in the paper\n\nCMAQv53_bidi_fix_PM25_NH4_494657_spatialplot_diff.csv is the data table used to produce the spatial plot of the biases in modeled ammonium PM2.5 (\uf06dg m-3) compared to CSN (circles), CASTNet (triangles), and SEARCH (squares) networks averaged over May to September 2016 as shown in Fig6.\n\nCMAQv53_bidi_fix_PM25_SO4_886932_spatialplot_diff.csv   is the data table used to produce the spatial plot of the biases in modeled sulfate PM2.5 (\uf06dg m-3) compared to IMPROVE (circles), CSN (triangles), CASTNET (squares), and SEARCH (diamonds) networks averaged over May to September 2016. \n\nThis dataset is associated with the following publication:\nPleim, J., L. Ran, K. Appel, M. Shephard, and K. Cady-Pereira. New Bidirectional Ammonia Flux Model in an Air Quality Model Coupled With an Agricultural Model.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 11(9): 2934-2957, (2019).",
             "distribution": [
                 {
-                    "title": "L1_cation.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504167/L1_cation.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "L1_cation.txt"
                 },
                 {
-                    "title": "CMAQv53_bidi_fix_NH3_290871_scatterplot.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504167/CMAQv53_bidi_fix_NH3_290871_scatterplot.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CMAQv53_bidi_fix_NH3_290871_scatterplot.csv"
                 },
                 {
-                    "title": "CMAQv53_bidi_fix_PM25_NH4_494657_spatialplot_diff.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504167/CMAQv53_bidi_fix_PM25_NH4_494657_spatialplot_diff.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CMAQv53_bidi_fix_PM25_NH4_494657_spatialplot_diff.csv"
                 },
                 {
-                    "title": "CMAQv53_bidi_fix_PM25_SO4_886932_spatialplot_diff.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504167/CMAQv53_bidi_fix_PM25_SO4_886932_spatialplot_diff.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CMAQv53_bidi_fix_PM25_SO4_886932_spatialplot_diff.csv"
                 },
                 {
-                    "title": "Figures11_to_14_CrIS2016_cmaq12km.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504167/Figures11_to_14_CrIS2016_cmaq12km.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figures11_to_14_CrIS2016_cmaq12km.xlsx"
                 },
                 {
-                    "title": "Figures11_to_14_cma2016_Bidifix_NH3_1330_avg_allmonths.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504167/Figures11_to_14_cma2016_Bidifix_NH3_1330_avg_allmonths.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figures11_to_14_cma2016_Bidifix_NH3_1330_avg_allmonths.xlsx"
                 },
                 {
-                    "title": "Figure15_agLand_beld4_CMAQ12km_2011.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504167/Figure15_agLand_beld4_CMAQ12km_2011.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure15_agLand_beld4_CMAQ12km_2011.txt"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504167",
+            "keyword": [
+                "Ammonia concentrations and fluxes",
+                "ammonia",
+                "Community Multi-scale Air Quality (CMAQ) model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-03-08",
-            "references": [
-                "https://doi.org/10.1029/2019ms001728"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -106982,85 +106976,87 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2019ms001728"
+            ],
+            "rights": null,
+            "title": "New bidirectional ammonia flux model in an air quality model coupled with an agricultural model"
         },
         {
-            "title": "Modeling Spatiotemporal Patterns of Ecosystem Metabolism and Organic Carbon Dynamics Affecting Hypoxia on the Louisiana Continental Shelf.",
-            "description": "These data include field observations from Northern Gulf of Mexico research surveys, as well as hydrodynamic and water quality model data generated by the Coastal Generalized Ecosystem Model (CGEM) between 2003-2007.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1504209",
-            "keyword": [
-                "nutrients",
-                "Hypoxia",
-                "Gulf of Mexico",
-                "Water Quality Simulation Modeling"
-            ],
             "contactPoint": {
                 "fn": "Brandon Jarvis",
                 "hasEmail": "mailto:jarvis.brandon@epa.gov"
             },
+            "description": "These data include field observations from Northern Gulf of Mexico research surveys, as well as hydrodynamic and water quality model data generated by the Coastal Generalized Ecosystem Model (CGEM) between 2003-2007.",
             "distribution": [
                 {
-                    "title": "GIS_ModelDomain_StationLocations.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/GIS_ModelDomain_StationLocations.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "GIS_ModelDomain_StationLocations.zip"
                 },
                 {
-                    "title": "SurveyCalibrationData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/SurveyCalibrationData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SurveyCalibrationData.xlsx"
                 },
                 {
-                    "title": "ProductionRespiration_CalibrationData.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/ProductionRespiration_CalibrationData.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ProductionRespiration_CalibrationData.xls"
                 },
                 {
-                    "title": "Fig9_CarbonFlux.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/Fig9_CarbonFlux.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig9_CarbonFlux.xlsx"
                 },
                 {
-                    "title": "Fig2_HypoxiaTimeSeries.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/Fig2_HypoxiaTimeSeries.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig2_HypoxiaTimeSeries.xlsx"
                 },
                 {
-                    "title": "Fig4_LoessZoneData.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/Fig4_LoessZoneData.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Fig4_LoessZoneData.txt"
                 },
                 {
-                    "title": "Fig5through8_matlabfiles.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/Fig5through8_matlabfiles.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Fig5through8_matlabfiles.zip"
                 },
                 {
-                    "title": "Table2_sensitivity.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/Table2_sensitivity.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table2_sensitivity.xlsx"
                 },
                 {
-                    "title": "Table1_CalibrationError-Summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/Table1_CalibrationError-Summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table1_CalibrationError-Summary.xlsx"
                 },
                 {
-                    "title": "Table3_CarbonBudget.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504209/Table3_CarbonBudget.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table3_CarbonBudget.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504209",
+            "keyword": [
+                "nutrients",
+                "Hypoxia",
+                "Gulf of Mexico",
+                "Water Quality Simulation Modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-19",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -107069,19 +107065,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Modeling Spatiotemporal Patterns of Ecosystem Metabolism and Organic Carbon Dynamics Affecting Hypoxia on the Louisiana Continental Shelf."
         },
         {
-            "title": "Decision Analytic Aproach Survey Results",
-            "description": "An elicitation with 32 experts informed relative prioritization of risks from chemical properties and human use factors for consumer product-related chemicals. Three different versions of the model were evaluated using distinct weight profiles. \n\nThis dataset is associated with the following publication:\nWood, M., K. Plourde, S. Larkin, P. Egeghy, A. Williams, V. Zemba, I. Linkov, and D. Vallero. Advances on a Decision Analytic Approach to Exposure\u2010Based Chemical Prioritization.   RISK ANALYSIS. Blackwell Publishing, Malden, MA, USA, 40(1): 83-96, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Daniel Vallero",
+                "hasEmail": "mailto:vallero.daniel@epa.gov"
+            },
+            "description": "An elicitation with 32 experts informed relative prioritization of risks from chemical properties and human use factors for consumer product-related chemicals. Three different versions of the model were evaluated using distinct weight profiles. \n\nThis dataset is associated with the following publication:\nWood, M., K. Plourde, S. Larkin, P. Egeghy, A. Williams, V. Zemba, I. Linkov, and D. Vallero. Advances on a Decision Analytic Approach to Exposure\u2010Based Chemical Prioritization.   RISK ANALYSIS. Blackwell Publishing, Malden, MA, USA, 40(1): 83-96, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430498/ValleroDaniel_A-qvbg_17.02.12%20Survey%20Results%20v4_deidentified.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ValleroDaniel_A-qvbg_17.02.12 Survey Results v4_deidentified.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1430498",
             "keyword": [
@@ -107092,21 +107096,10 @@
                 "MCDA",
                 "multi-criteria decision analysis"
             ],
-            "contactPoint": {
-                "fn": "Daniel Vallero",
-                "hasEmail": "mailto:vallero.daniel@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ValleroDaniel_A-qvbg_17.02.12 Survey Results v4_deidentified.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430498/ValleroDaniel_A-qvbg_17.02.12%20Survey%20Results%20v4_deidentified.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-02",
-            "references": [
-                "https://doi.org/10.1111/risa.13001",
-                "https://pasteur.epa.gov/uploads/10.23719/1430498/documents/ADVANCES%20Appendix%201.pdf"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107116,61 +107109,64 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/risa.13001",
+                "https://pasteur.epa.gov/uploads/10.23719/1430498/documents/ADVANCES%20Appendix%201.pdf"
+            ],
+            "rights": null,
+            "title": "Decision Analytic Aproach Survey Results"
         },
         {
-            "title": "Low level hydrogen peroxide vapor data for Cary test house decontamination study, using a Bacillus anthracis surrogate",
-            "description": "The data set is comprised of five Excel spreadsheets, one for each of the tests described in the research article.  The data in the spreadsheets are the colony forming unit (CFU) data for each coupon material replicate and location. \n\nThis dataset is associated with the following publication:\nMickelsen, L., J. Wood, W. Calfee, S. Serre, S. Ryan, A. Touati, F. Delafield, and D. Aslett. Low\u2010concentration hydrogen peroxide decontamination for Bacillus spore contamination in buildings.   Remediation Journal. John Wiley & Sons, Inc., Hoboken, NJ, USA, 30(1): 47-56, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1500896",
-            "keyword": [
-                "hydrogen peroxide vapor",
-                "Bacillus anthracis",
-                "Decontamination",
-                "Sporicide"
-            ],
             "contactPoint": {
                 "fn": "Joseph Wood",
                 "hasEmail": "mailto:wood.joe@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500896/documents/Data%20dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The data set is comprised of five Excel spreadsheets, one for each of the tests described in the research article.  The data in the spreadsheets are the colony forming unit (CFU) data for each coupon material replicate and location. \n\nThis dataset is associated with the following publication:\nMickelsen, L., J. Wood, W. Calfee, S. Serre, S. Ryan, A. Touati, F. Delafield, and D. Aslett. Low\u2010concentration hydrogen peroxide decontamination for Bacillus spore contamination in buildings.   Remediation Journal. John Wiley & Sons, Inc., Hoboken, NJ, USA, 30(1): 47-56, (2019).",
             "distribution": [
                 {
-                    "title": "Test 0.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500896/Test%200.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Test 0.xlsx"
                 },
                 {
-                    "title": "Test 1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500896/Test%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Test 1.xlsx"
                 },
                 {
-                    "title": "Test 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500896/Test%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Test 2.xlsx"
                 },
                 {
-                    "title": "Test 4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500896/Test%204.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Test 4.xlsx"
                 },
                 {
-                    "title": "Test 3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500896/Test%203.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Test 3.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500896",
+            "keyword": [
+                "hydrogen peroxide vapor",
+                "Bacillus anthracis",
+                "Decontamination",
+                "Sporicide"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-25",
-            "references": [
-                "https://doi.org/10.1002/rem.21629"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107181,162 +107177,160 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500896/documents/Data%20dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1002/rem.21629"
+            ],
+            "rights": null,
+            "title": "Low level hydrogen peroxide vapor data for Cary test house decontamination study, using a Bacillus anthracis surrogate"
         },
         {
-            "title": "Volatile organic compound emissions from prescribed burning in tallgrass prairie ecosystems",
-            "description": "Measured concentrations of carbon monoxide, carbon dioxide, and voaltile organic compounds from downwind of prescribe fires in tallgrass prairie ecosystems. Data is in *.csv format. \n\nThis dataset is associated with the following publication:\nWhitehill, A., I. George, R. Long, K. Baker, and M. Landis. Volatile Organic Compound Emissions from Prescribed Burning in Tallgrass Prairie Ecosystems.   ATMOSPHERE. MDPI AG, Basel,  SWITZERLAND, 10(8): 464, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1504124",
-            "keyword": [
-                "carbon monoxide",
-                "carbon dioxide",
-                "fire",
-                "wildfire land",
-                "emission factor",
-                "tallgrass prairie",
-                "oozne production",
-                "hazardous air pollutant",
-                "volatile organic compounds"
-            ],
             "contactPoint": {
                 "fn": "Matthew Landis",
                 "hasEmail": "mailto:landis.matthew@epa.gov"
             },
+            "description": "Measured concentrations of carbon monoxide, carbon dioxide, and voaltile organic compounds from downwind of prescribe fires in tallgrass prairie ecosystems. Data is in *.csv format. \n\nThis dataset is associated with the following publication:\nWhitehill, A., I. George, R. Long, K. Baker, and M. Landis. Volatile Organic Compound Emissions from Prescribed Burning in Tallgrass Prairie Ecosystems.   ATMOSPHERE. MDPI AG, Basel,  SWITZERLAND, 10(8): 464, (2019).",
             "distribution": [
                 {
-                    "title": "TableS1.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504124/TableS1.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "TableS1.csv"
                 },
                 {
-                    "title": "TableS3.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504124/TableS3.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "TableS3.csv"
                 },
                 {
-                    "title": "TableS6.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504124/TableS6.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "TableS6.csv"
                 },
                 {
-                    "title": "TableS4.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504124/TableS4.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "TableS4.csv"
                 },
                 {
-                    "title": "TableS2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504124/TableS2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "TableS2.csv"
                 },
                 {
-                    "title": "TableS5.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504124/TableS5.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "TableS5.csv"
                 },
                 {
-                    "title": "FlintHillsBurn_DataDictionary.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504124/FlintHillsBurn_DataDictionary.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "FlintHillsBurn_DataDictionary.docx"
                 }
             ],
-            "modified": "2019-06-18",
-            "references": [
-                "https://doi.org/10.3390/atmos10080464"
-            ],
-            "publisher": {
-                "name": "U.S. EPA Office of Research and Development (ORD)",
-                "subOrganizationOf": {
-                    "name": "U.S. Environmental Protection Agency",
-                    "subOrganizationOf": {
-                        "name": "U.S. Government"
-                    }
-                }
+            "identifier": "https://doi.org/10.23719/1504124",
+            "keyword": [
+                "carbon monoxide",
+                "carbon dioxide",
+                "fire",
+                "wildfire land",
+                "emission factor",
+                "tallgrass prairie",
+                "oozne production",
+                "hazardous air pollutant",
+                "volatile organic compounds"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
+            "modified": "2019-06-18",
+            "programCode": [
+                "020:094"
+            ],
+            "publisher": {
+                "name": "U.S. EPA Office of Research and Development (ORD)",
+                "subOrganizationOf": {
+                    "name": "U.S. Environmental Protection Agency",
+                    "subOrganizationOf": {
+                        "name": "U.S. Government"
+                    }
                 }
             },
+            "references": [
+                "https://doi.org/10.3390/atmos10080464"
+            ],
+            "rights": null,
+            "title": "Volatile organic compound emissions from prescribed burning in tallgrass prairie ecosystems"
+        },
         {
-            "title": "Detection Limit Study",
-            "description": "Detection Limit Study. \n\nThis dataset is associated with the following publication:\nReddy, T., R. Flick , J. Lazorchak , M. Smith, B. Wiechman, and D. Lattier. Experimental paradigm for in-lab proxy aquatic studies under conditions of static, non flow through chemical exposures.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 34(12): 2796-2802, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1502606",
-            "keyword": [
-                "transcriptomics",
-                "contaminant of emerging concern",
-                "ecotoxicogenomic",
-                "endocrine-disrupting compound",
-                "estrongenic compound"
-            ],
             "contactPoint": {
                 "fn": "James Lazorchak",
                 "hasEmail": "mailto:lazorchak.jim@epa.gov"
             },
+            "description": "Detection Limit Study. \n\nThis dataset is associated with the following publication:\nReddy, T., R. Flick , J. Lazorchak , M. Smith, B. Wiechman, and D. Lattier. Experimental paradigm for in-lab proxy aquatic studies under conditions of static, non flow through chemical exposures.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 34(12): 2796-2802, (2015).",
             "distribution": [
                 {
-                    "title": "EDC data 2004.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/EDC%20data%202004.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "EDC data 2004.xls"
                 },
                 {
-                    "title": "EDC Data 2005.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/EDC%20Data%202005.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "EDC Data 2005.xls"
                 },
                 {
-                    "title": "EDCs graphs for SETAC-Continuoius addition.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/EDCs%20graphs%20for%20SETAC-Continuoius%20addition.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "EDCs graphs for SETAC-Continuoius addition.xls"
                 },
                 {
-                    "title": "EE2 Study # 10-02 Final Report 060710.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/EE2%20Study%20%23%2010-02%20Final%20Report%20060710.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "EE2 Study # 10-02 Final Report 060710.xls"
                 },
                 {
-                    "title": "SETAC EE2, E1 Vg & Chemistry from Manual exchange.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/SETAC%20EE2%2C%20E1%20Vg%20%26%20Chemistry%20from%20Manual%20exchange.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SETAC EE2, E1 Vg & Chemistry from Manual exchange.xls"
                 },
                 {
-                    "title": "Study # 10-01 EE2 Vg & 18s data.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/Study%20%23%2010-01%20EE2%20Vg%20%26%2018s%20data.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Study # 10-01 EE2 Vg & 18s data.xls"
                 },
                 {
-                    "title": "Study # 10-03 Final Report 060910.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/Study%20%23%2010-03%20Final%20Report%20060910.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Study # 10-03 Final Report 060910.xls"
                 },
                 {
-                    "title": "Study # 10-03 Vg & 18s RR Data.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/Study%20%23%2010-03%20Vg%20%26%2018s%20RR%20Data.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Study # 10-03 Vg & 18s RR Data.xls"
                 },
                 {
-                    "title": "TD # 1690-EE2 #1-15 Vg&18s.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502606/TD%20%23%201690-EE2%20%231-15%20Vg%2618s.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "TD # 1690-EE2 #1-15 Vg&18s.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502606",
+            "keyword": [
+                "transcriptomics",
+                "contaminant of emerging concern",
+                "ecotoxicogenomic",
+                "endocrine-disrupting compound",
+                "estrongenic compound"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2010-06-09",
-            "references": [
-                "https://doi.org/10.1002/etc.3121"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107346,54 +107340,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.3121"
+            ],
+            "rights": null,
+            "title": "Detection Limit Study"
         },
         {
-            "title": "National Stormwater Calculator Unit and Regional Cost Equations and Data Variables ",
-            "description": "The spreadsheets that provide the unit and regional cost variables and equations for all of the green infrastructure and low impact development controls programmed into the National Stormwater Calculator. \n\nThis dataset is associated with the following publications:\nRossman, L., and J. Bernagros. NATIONAL STORMWATER CALCULATOR WEB APP USER\u2019S GUIDE \u2013 VERSION 3.2.0 - manual. U.S. Environmental Protection Agency, Washington, DC, USA, 2019.\nBernagros, J., D. Pankani, S. Struck , and M. Deerhake. Estimating Regionalized Planning Costs of Green Infrastructure and Low-Impact Development Stormwater Management Practices: Updates to the US Environmental Protection Agency\u2019s National Stormwater Calculator.   Journal of Sustainable Water in the Built Environment. American Society of Civil Engineers (ASCE), New York, NY, USA, 7(2): 04020021-1, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1510483",
-            "keyword": [
-                "Green Infrastructure",
-                "low impact development",
-                "maintenance",
-                "costs",
-                "scenario planning",
-                "capital",
-                "stormwater management"
-            ],
             "contactPoint": {
                 "fn": "Jason Bernagros",
                 "hasEmail": "mailto:bernagros.jason@epa.gov"
             },
+            "description": "The spreadsheets that provide the unit and regional cost variables and equations for all of the green infrastructure and low impact development controls programmed into the National Stormwater Calculator. \n\nThis dataset is associated with the following publications:\nRossman, L., and J. Bernagros. NATIONAL STORMWATER CALCULATOR WEB APP USER\u2019S GUIDE \u2013 VERSION 3.2.0 - manual. U.S. Environmental Protection Agency, Washington, DC, USA, 2019.\nBernagros, J., D. Pankani, S. Struck , and M. Deerhake. Estimating Regionalized Planning Costs of Green Infrastructure and Low-Impact Development Stormwater Management Practices: Updates to the US Environmental Protection Agency\u2019s National Stormwater Calculator.   Journal of Sustainable Water in the Built Environment. American Society of Civil Engineers (ASCE), New York, NY, USA, 7(2): 04020021-1, (2021).",
             "distribution": [
                 {
-                    "title": "BLS_CPI_geographic_revision_area-Combined.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1510483/BLS_CPI_geographic_revision_area-Combined.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "BLS_CPI_geographic_revision_area-Combined.pdf"
                 },
                 {
-                    "title": "EPAStormWaterCalcCostComponent-EPA_07132016_dp_cmb-COMBINED.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1510483/EPAStormWaterCalcCostComponent-EPA_07132016_dp_cmb-COMBINED.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "EPAStormWaterCalcCostComponent-EPA_07132016_dp_cmb-COMBINED.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1510483",
+            "keyword": [
+                "Green Infrastructure",
+                "low impact development",
+                "maintenance",
+                "costs",
+                "scenario planning",
+                "capital",
+                "stormwater management"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-15",
-            "references": [
-                "https://www.epa.gov/water-research/national-stormwater-calculator-users-guide-mobile-web-based-app",
-                "https://doi.org/10.1061/jswbay.0000934",
-                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/LID%20Cost%20Analysis_Report_National%20SWC_2015.pdf",
-                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/LID%20SW%20Control%20Cost%20Estimation%20Analysis_Cost%20Estimation%20Procedure_APPENDICES.pdf",
-                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/Final%20Methodology%20and%20Results%20Report_Delivered08192016_Final_Feb_21_18-Edit.pdf",
-                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/TO-026_Task_4-3-B-2_QC_QC_Report_Final_08192016_RTI-Geosyntec.pdf"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107403,39 +107392,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.epa.gov/water-research/national-stormwater-calculator-users-guide-mobile-web-based-app",
+                "https://doi.org/10.1061/jswbay.0000934",
+                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/LID%20Cost%20Analysis_Report_National%20SWC_2015.pdf",
+                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/LID%20SW%20Control%20Cost%20Estimation%20Analysis_Cost%20Estimation%20Procedure_APPENDICES.pdf",
+                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/Final%20Methodology%20and%20Results%20Report_Delivered08192016_Final_Feb_21_18-Edit.pdf",
+                "https://pasteur.epa.gov/uploads/10.23719/1510483/documents/TO-026_Task_4-3-B-2_QC_QC_Report_Final_08192016_RTI-Geosyntec.pdf"
+            ],
+            "rights": null,
+            "title": "National Stormwater Calculator Unit and Regional Cost Equations and Data Variables "
         },
         {
-            "title": "California Central Valley PWC sensitivity analysis data",
-            "description": "This repository contains model input/output, R scripts and collated literature data as part of the model evaluation and sensitivity analysis process for the Pesticide Water Calculator. \n\nThis dataset is associated with the following publication:\nSinnathamby, S., J. Minucci, D. Denton, S. Raimondo, L. Oliver, Y. Yuan, D. Young, A. Pitchford, E. Waits, and T. Purucker. A sensitivity analysis of pesticide concentrations in California Central Valley vernal pools.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 257: 113486, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1435026",
-            "keyword": [
-                "pesticides",
-                "vernal pools",
-                "agricultural watersheds"
-            ],
             "contactPoint": {
                 "fn": "Steven Purucker",
                 "hasEmail": "mailto:purucker.tom@epa.gov"
             },
+            "description": "This repository contains model input/output, R scripts and collated literature data as part of the model evaluation and sensitivity analysis process for the Pesticide Water Calculator. \n\nThis dataset is associated with the following publication:\nSinnathamby, S., J. Minucci, D. Denton, S. Raimondo, L. Oliver, Y. Yuan, D. Young, A. Pitchford, E. Waits, and T. Purucker. A sensitivity analysis of pesticide concentrations in California Central Valley vernal pools.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 257: 113486, (2019).",
             "distribution": [
                 {
-                    "title": "https://github.com/puruckertom/sinnathamby_pwc/",
-                    "accessURL": "https://github.com/puruckertom/sinnathamby_pwc/"
+                    "accessURL": "https://github.com/puruckertom/sinnathamby_pwc/",
+                    "title": "https://github.com/puruckertom/sinnathamby_pwc/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435026",
+            "keyword": [
+                "pesticides",
+                "vernal pools",
+                "agricultural watersheds"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-04",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2019.113486"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107445,19 +107439,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2019.113486"
+            ],
+            "rights": null,
+            "title": "California Central Valley PWC sensitivity analysis data"
         },
         {
-            "title": "Droplet Digital PCR Quantification of Norovirus and Adenovirus in Decentralized Wastewater and Graywater Collections",
-            "description": "Provides droplet digital polymerase chain reaction (ddPCR) and quantitative PCR (qPCR) measurements of adenovirus and norovirus in three decentralized wastewater and graywater collection systems. \n\nThis dataset is associated with the following publication:\nJahne, M., N. Brinkman, S. Keely, B. Zimmerman, E. Wheaton, and J. Garland. Droplet Digital PCR Quantification of Norovirus and Adenovirus in Decentralized Wastewater and Graywater Collections: Implications for Onsite Reuse.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 169: 115213, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Michael Jahne",
+                "hasEmail": "mailto:jahne.michael@epa.gov"
+            },
+            "description": "Provides droplet digital polymerase chain reaction (ddPCR) and quantitative PCR (qPCR) measurements of adenovirus and norovirus in three decentralized wastewater and graywater collection systems. \n\nThis dataset is associated with the following publication:\nJahne, M., N. Brinkman, S. Keely, B. Zimmerman, E. Wheaton, and J. Garland. Droplet Digital PCR Quantification of Norovirus and Adenovirus in Decentralized Wastewater and Graywater Collections: Implications for Onsite Reuse.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 169: 115213, (2020).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502589/Dataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dataset.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502589",
             "keyword": [
@@ -107468,20 +107472,10 @@
                 "QMRA",
                 "water reuse"
             ],
-            "contactPoint": {
-                "fn": "Michael Jahne",
-                "hasEmail": "mailto:jahne.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Dataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502589/Dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-30",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2019.115213"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107491,77 +107485,79 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2019.115213"
+            ],
+            "rights": null,
+            "title": "Droplet Digital PCR Quantification of Norovirus and Adenovirus in Decentralized Wastewater and Graywater Collections"
         },
         {
-            "title": "Species sulfur sulfate raw data",
-            "description": "Measurements of water sulfate concentrations at the beginning and end of the exposures of the animals, initial \u03b4(34S/32S) ratios in the animals at the beginning and end of the exposures, and initial \u03b4(34S/32S) ratios of the exposure water. \n\nThis dataset is associated with the following publication:\nGriffith, M., J. Lazorchak, and H. Haring. Uptake of Sulfate from Ambient Water by Freshwater Animals.   WATER. MDPI AG, Basel,  SWITZERLAND, 12(5): 1496, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1504445",
-            "keyword": [
-                "water quality",
-                "Major Ions",
-                "sulfate",
-                "uptake",
-                "aquatic animals"
-            ],
             "contactPoint": {
                 "fn": "Michael Griffith",
                 "hasEmail": "mailto:griffith.michael@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1504445/documents/Data_Dictionary-SulfatePhysiology-508.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Measurements of water sulfate concentrations at the beginning and end of the exposures of the animals, initial \u03b4(34S/32S) ratios in the animals at the beginning and end of the exposures, and initial \u03b4(34S/32S) ratios of the exposure water. \n\nThis dataset is associated with the following publication:\nGriffith, M., J. Lazorchak, and H. Haring. Uptake of Sulfate from Ambient Water by Freshwater Animals.   WATER. MDPI AG, Basel,  SWITZERLAND, 12(5): 1496, (2020).",
             "distribution": [
                 {
-                    "title": "Pimephales_promelas_labSO4.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Pimephales_promelas_labSO4.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pimephales_promelas_labSO4.csv"
                 },
                 {
-                    "title": "Pimephales_promelas_stableisotope.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Pimephales_promelas_stableisotope.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pimephales_promelas_stableisotope.csv"
                 },
                 {
-                    "title": "Utterbackia_imbecillis_labSO4.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Utterbackia_imbecillis_labSO4.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utterbackia_imbecillis_labSO4.csv"
                 },
                 {
-                    "title": "Utterbackia_imbecillis_stableisotope.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Utterbackia_imbecillis_stableisotope.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utterbackia_imbecillis_stableisotope.csv"
                 },
                 {
-                    "title": "Hexagenia_bilineata_labSO4.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Hexagenia_bilineata_labSO4.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hexagenia_bilineata_labSO4.csv"
                 },
                 {
-                    "title": "Hexagenia_bilineata_stableisotope.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Hexagenia_bilineata_stableisotope.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hexagenia_bilineata_stableisotope.csv"
                 },
                 {
-                    "title": "Procambarus_clarkii_labSO4.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Procambarus_clarkii_labSO4.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Procambarus_clarkii_labSO4.csv"
                 },
                 {
-                    "title": "Procambarus_clarkii_stableisotope.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1504445/Procambarus_clarkii_stableisotope.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Procambarus_clarkii_stableisotope.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1504445",
+            "keyword": [
+                "water quality",
+                "Major Ions",
+                "sulfate",
+                "uptake",
+                "aquatic animals"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-09-12",
-            "references": [
-                "https://doi.org/10.3390/w12051496"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107572,73 +107568,71 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1504445/documents/Data_Dictionary-SulfatePhysiology-508.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.3390/w12051496"
+            ],
+            "rights": null,
+            "title": "Species sulfur sulfate raw data"
         },
         {
-            "title": "AAFEX Aircraft Emissions Field Campaign",
-            "description": "This dataset contains information from a 2009 research study of the fine particle emissions from two commercial aircraft engines as obtained 30-meters downstream of each engine. \n\nThis dataset is associated with the following publication:\nKinsey, J., W. Squier, and M. Timko. Characterization of the Fine Particle Emissions from the Use of Two Fischer-Tropsch Fuels in a CFM56-2C1 Commercial Aircraft Engine.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA,  33, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503398",
-            "keyword": [
-                "aircraft engines",
-                "emissions",
-                "Fine Particulate Matter",
-                "instrumentation",
-                "Speciation"
-            ],
             "contactPoint": {
                 "fn": "John Kinsey",
                 "hasEmail": "mailto:kinsey.john@epa.gov"
             },
+            "description": "This dataset contains information from a 2009 research study of the fine particle emissions from two commercial aircraft engines as obtained 30-meters downstream of each engine. \n\nThis dataset is associated with the following publication:\nKinsey, J., W. Squier, and M. Timko. Characterization of the Fine Particle Emissions from the Use of Two Fischer-Tropsch Fuels in a CFM56-2C1 Commercial Aircraft Engine.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA,  33, (2019).",
             "distribution": [
                 {
-                    "title": "Fig 3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503398/Fig%203.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 3.xlsx"
                 },
                 {
-                    "title": "Fig 2 & 9a_Revised 10-21-19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503398/Fig%202%20%26%209a_Revised%2010-21-19.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 2 & 9a_Revised 10-21-19.xlsx"
                 },
                 {
-                    "title": "Fig 4 & 9b_Revised 10-22-19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503398/Fig%204%20%26%209b_Revised%2010-22-19.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 4 & 9b_Revised 10-22-19.xlsx"
                 },
                 {
-                    "title": "Fig 5_Revised 10-22-19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503398/Fig%205_Revised%2010-22-19.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 5_Revised 10-22-19.xlsx"
                 },
                 {
-                    "title": "Fig 6_Revised 10-22-19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503398/Fig%206_Revised%2010-22-19.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 6_Revised 10-22-19.xlsx"
                 },
                 {
-                    "title": "Fig 7 & 8_Revised 10-22-19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503398/Fig%207%20%26%208_Revised%2010-22-19.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 7 & 8_Revised 10-22-19.xlsx"
                 },
                 {
-                    "title": "Fig 10_New 10-29-19.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503398/Fig%2010_New%2010-29-19.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fig 10_New 10-29-19.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503398",
+            "keyword": [
+                "aircraft engines",
+                "emissions",
+                "Fine Particulate Matter",
+                "instrumentation",
+                "Speciation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-02-07",
-            "references": [
-                "https://doi.org/10.1021/acs.energyfuels.9b00780"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107648,49 +107642,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.energyfuels.9b00780"
+            ],
+            "rights": null,
+            "title": "AAFEX Aircraft Emissions Field Campaign"
         },
         {
-            "title": "Biotrickle Filtration of Trihalomethanes",
-            "description": "This study involves the use of biofiltration, which is a control technique to degrade trihalomethanes using a bioreactor containing living material to capture and biologically degrade pollutants. Common uses include processing waste water, capturing harmful chemicals or silt from surface runoff, and microbiotic oxidation of contaminants in air. \n\nThis dataset is associated with the following publication:\nMezgebe, B., G. Sorial, D. Wendell, and E. Sahle-Demessie. Effectiveness of biosurfactant for the removal of trihalomethanes by biotrickling filter.   Wiley StatsRef: Statistics Reference Online. John Wiley & Sons, Inc., Hoboken, NJ, USA, 1(1): 12031, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1418809",
-            "keyword": [
-                "Biotrickling Filter",
-                "Biodegradation",
-                "Chloroform",
-                "Dichlorobromomethane",
-                "fungi",
-                "Microbial Analysis",
-                "trihalomethanes"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1418809/documents/Data%20Dictionary_BiotrickleFiltration.pdf",
+            "describedByType": "application/pdf",
+            "description": "This study involves the use of biofiltration, which is a control technique to degrade trihalomethanes using a bioreactor containing living material to capture and biologically degrade pollutants. Common uses include processing waste water, capturing harmful chemicals or silt from surface runoff, and microbiotic oxidation of contaminants in air. \n\nThis dataset is associated with the following publication:\nMezgebe, B., G. Sorial, D. Wendell, and E. Sahle-Demessie. Effectiveness of biosurfactant for the removal of trihalomethanes by biotrickling filter.   Wiley StatsRef: Statistics Reference Online. John Wiley & Sons, Inc., Hoboken, NJ, USA, 1(1): 12031, (2019).",
             "distribution": [
                 {
-                    "title": "BTF_PPR3_Supplemental material.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1418809/BTF_PPR3_Supplemental%20material.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "BTF_PPR3_Supplemental material.docx"
                 },
                 {
-                    "title": "Biotrickling_THMs- Removal efficiency_Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1418809/Biotrickling_THMs-%20Removal%20efficiency_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biotrickling_THMs- Removal efficiency_Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1418809",
+            "keyword": [
+                "Biotrickling Filter",
+                "Biodegradation",
+                "Chloroform",
+                "Dichlorobromomethane",
+                "fungi",
+                "Microbial Analysis",
+                "trihalomethanes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-12-01",
-            "references": [
-                "https://doi.org/10.1002/eng2.12031"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107701,41 +107697,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1418809/documents/Data%20Dictionary_BiotrickleFiltration.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1002/eng2.12031"
+            ],
+            "rights": null,
+            "title": "Biotrickle Filtration of Trihalomethanes"
         },
         {
-            "title": "Investigation of Factors Controlling PM2.5 Variability across the South Korean peninsula during KORUS-AQ",
-            "description": "Data collected for this research provides information on mixing layer heights at Olympic Park during the KORUS-AQ field campaign. \n\nThis dataset is associated with the following publication:\nJordan, C., J. Crawford, A. Beyersdorf, T. Eck, H. Halliday, B. Nault, L. Chang, J. Park, R. Park, G. Lee, H. Kim, J. Ahn, S. Cho, H.J. Shin, J.H. Lee, J. Jung, D. Kim, M. Lee, T. Lee, A. Whitehill, J. Szykman, M. Schueneman, P. Campuzano-Jost, J. Jimenez, J. DiGangi, G. Diskin, B. Anderson, R. Moore, L. Ziemba, M. Fenn, J. Hair, R. Kuehn, R. Holz, G. Chen, K. Travis, M. Shook, D. Peterson, K. Lamb, and J. Schwarz. Investigation of factors controlling PM2.5 variability across the South Korean Peninsula during KORUS-AQ.   Elementa: Science of the Anthropocene. University of California Press (UC Press), Oakland, CA, USA, 8(1): 28, (2020).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1517607",
-            "keyword": [
-                "KORUS-AQ",
-                "pm 2.5",
-                "air quality",
-                "Korea"
-            ],
             "contactPoint": {
                 "fn": "Andrew Whitehill",
                 "hasEmail": "mailto:whitehill.andrew@epa.gov"
             },
+            "description": "Data collected for this research provides information on mixing layer heights at Olympic Park during the KORUS-AQ field campaign. \n\nThis dataset is associated with the following publication:\nJordan, C., J. Crawford, A. Beyersdorf, T. Eck, H. Halliday, B. Nault, L. Chang, J. Park, R. Park, G. Lee, H. Kim, J. Ahn, S. Cho, H.J. Shin, J.H. Lee, J. Jung, D. Kim, M. Lee, T. Lee, A. Whitehill, J. Szykman, M. Schueneman, P. Campuzano-Jost, J. Jimenez, J. DiGangi, G. Diskin, B. Anderson, R. Moore, L. Ziemba, M. Fenn, J. Hair, R. Kuehn, R. Holz, G. Chen, K. Travis, M. Shook, D. Peterson, K. Lamb, and J. Schwarz. Investigation of factors controlling PM2.5 variability across the South Korean Peninsula during KORUS-AQ.   Elementa: Science of the Anthropocene. University of California Press (UC Press), Oakland, CA, USA, 8(1): 28, (2020).",
             "distribution": [
                 {
-                    "title": "https://www-air.larc.nasa.gov/missions/korus-aq/",
-                    "accessURL": "https://www-air.larc.nasa.gov/missions/korus-aq/"
+                    "accessURL": "https://www-air.larc.nasa.gov/missions/korus-aq/",
+                    "title": "https://www-air.larc.nasa.gov/missions/korus-aq/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1517607",
+            "keyword": [
+                "KORUS-AQ",
+                "pm 2.5",
+                "air quality",
+                "Korea"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-02",
-            "references": [
-                "https://doi.org/10.1525/elementa.424"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107745,43 +107739,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1525/elementa.424"
+            ],
+            "rights": null,
+            "title": "Investigation of Factors Controlling PM2.5 Variability across the South Korean peninsula during KORUS-AQ"
         },
         {
-            "title": "Characterization of Colloidal-size Copper based pesticides",
-            "description": "Data set provides the characterization of colloidal and nano-size copper pesticides, including properties related to their environmental fate, transport, sorption and degradation parameters. The study will inform whether nanoformulations can be evaluated within the current pesticide regulatory framework. \n\nThis dataset is associated with the following publication:\nTegenaw, A., G.A. Sorial, E. Sahle-Demessie, and C. Han. Characterization of colloid-size copper-based pesticide and its potential ecological implications..   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 253: 278-287, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1506122",
-            "keyword": [
-                ": Agriculture",
-                "bioavailability",
-                "Colloidal stability",
-                "Cu2O pesticide",
-                "Exposure pathways"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1506122/documents/Data%20Dictionary_Copper_Nanopesticide.pdf",
+            "describedByType": "application/pdf",
+            "description": "Data set provides the characterization of colloidal and nano-size copper pesticides, including properties related to their environmental fate, transport, sorption and degradation parameters. The study will inform whether nanoformulations can be evaluated within the current pesticide regulatory framework. \n\nThis dataset is associated with the following publication:\nTegenaw, A., G.A. Sorial, E. Sahle-Demessie, and C. Han. Characterization of colloid-size copper-based pesticide and its potential ecological implications..   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 253: 278-287, (2019).",
             "distribution": [
                 {
-                    "title": "Ayu_Cu-NPs_Supplemental Data_PPR3_Research.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1506122/Ayu_Cu-NPs_Supplemental%20Data_PPR3_Research.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Ayu_Cu-NPs_Supplemental Data_PPR3_Research.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1506122",
+            "keyword": [
+                ": Agriculture",
+                "bioavailability",
+                "Colloidal stability",
+                "Cu2O pesticide",
+                "Exposure pathways"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-12-02",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2019.07.036",
-                "https://pasteur.epa.gov/uploads/10.23719/1506122/documents/Ayu_Cu-NPs_Supplemental%20Data_PPR3_Research.docx"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -107792,20 +107787,32 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1506122/documents/Data%20Dictionary_Copper_Nanopesticide.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2019.07.036",
+                "https://pasteur.epa.gov/uploads/10.23719/1506122/documents/Ayu_Cu-NPs_Supplemental%20Data_PPR3_Research.docx"
+            ],
+            "rights": null,
+            "title": "Characterization of Colloidal-size Copper based pesticides"
         },
         {
-            "title": "Carbonaceous particulate matter emitted from a pellet-fired biomass boiler",
-            "description": "This data examines the chemical composition of particulate matter (PM) emitted from outdoor pellet boilers. Pellet boilers are often used in homes to generate hot water or heat.  The emissions of these boilers are compared with other hot water and heating technologies. Carbon composition of the emissions is the main focus. \n\nThis dataset is associated with the following publication:\nHays, M., J. Kinsey, I. George, W. Preston, C. Singer, and B. Patel. Carbonaceous particle matter emitted from a pellet-fired biomass boiler.   ATMOSPHERE. MDPI AG, Basel,  SWITZERLAND,  536, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Michael Hays",
+                "hasEmail": "mailto:hays.michael@epa.gov"
+            },
+            "description": "This data examines the chemical composition of particulate matter (PM) emitted from outdoor pellet boilers. Pellet boilers are often used in homes to generate hot water or heat.  The emissions of these boilers are compared with other hot water and heating technologies. Carbon composition of the emissions is the main focus. \n\nThis dataset is associated with the following publication:\nHays, M., J. Kinsey, I. George, W. Preston, C. Singer, and B. Patel. Carbonaceous particle matter emitted from a pellet-fired biomass boiler.   ATMOSPHERE. MDPI AG, Basel,  SWITZERLAND,  536, (2019).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.mdpi.com/2073-4433/10/9/536",
+                    "title": "https://www.mdpi.com/2073-4433/10/9/536"
+                },
+                {
+                    "accessURL": "https://www.mdpi.com/2073-4433/10/9/536/s1",
+                    "title": "https://www.mdpi.com/2073-4433/10/9/536/s1"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1517593",
             "keyword": [
@@ -107817,23 +107824,10 @@
                 "Combustion Emissions",
                 "polycyclic aromatic hydrocarbons"
             ],
-            "contactPoint": {
-                "fn": "Michael Hays",
-                "hasEmail": "mailto:hays.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.mdpi.com/2073-4433/10/9/536",
-                    "accessURL": "https://www.mdpi.com/2073-4433/10/9/536"
-                },
-                {
-                    "title": "https://www.mdpi.com/2073-4433/10/9/536/s1",
-                    "accessURL": "https://www.mdpi.com/2073-4433/10/9/536/s1"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-08-28",
-            "references": [
```

