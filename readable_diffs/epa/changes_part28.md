# Change History for epa.json (Part 28)

### Changes from 31606f9 to dd2190f (Part 18/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Mark Jankowski",
+                "hasEmail": "mailto:jankowski.mark@epa.gov"
+            },
+            "description": "A major challenge in ecotoxicology is accurately and sufficiently measuring chemical exposures and biological effects given the presence of complex and dynamic contaminant mixtures in surface waters. It is impractical to quantify all chemicals in such matrices over space and time, and even if it were practical, concomitant biological effects would not be elucidated. Our study examined the performance of the Daphnia magna transcriptome to detect distinct responses across three water sources in Minnesota: laboratory (well) waters, wetland waters, and storm waters. Pyriproxyfen was included as a gene expression and male neonate production positive control to examine whether gene expression resulting from exposure to this well-studied juvenoid hormone analog can be detected in complex matrices. Laboratory-reared (<24 h) D. magna were exposed to a water source and/or pyriproxyfen for 16 days to monitor phenotypic changes or 96 h to examine gene expression responses using Illumina HiSeq 2500 (10 million reads per library, 50-bp paired end [2 \u00d7 50]). The results indicated that a unique gene expression profile was produced for each water source. At 119 ng/L pyriproxyfen (~25% effect concentration) for male neonate production, as expected, the Doublesex1 gene was up-regulated. In descending order, gene expression patterns were most discernable with respect to pyriproxyfen exposure status, season of stormwater sample collection, and wetland quality, as indicated by the index of biological integrity. However, the biological implications of the affected genes were not broadly clear given limited genome resources for invertebrates. Our study provides support for the utility of short-term whole-organism transcriptomic testing in D. magna to discern sample type, but highlights the need for further work on invertebrate genomics. Citation information for this dataset can be found in Data.gov's References section.",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.13020/4hq3-v890",
+                    "title": "https://doi.org/10.13020/4hq3-v890"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529423",
             "keyword": [
@@ -179516,59 +179519,50 @@
                 "Invertebrate toxicology",
                 "Transcriptomics."
             ],
-            "contactPoint": {
-                "fn": "Mark Jankowski",
-                "hasEmail": "mailto:jankowski.mark@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.13020/4hq3-v890",
-                    "accessURL": "https://doi.org/10.13020/4hq3-v890"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-07-18",
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
+            "title": "Using the Daphnia magna Transcriptome to Distinguish Water Source: Wetland and Stormwater Case Studies"
         },
         {
-            "title": "Sorption modeling data for benzene in polyethylene pipe",
-            "description": "Benzene concentration time series data during uptake and release from polyethylene drinking water pipes. \n\nThis dataset is associated with the following publication:\nHaupert, L., L. Garcia-Bakarich, N. Sojda, D. Schupp, and M. Magnuson. Benzene Diffusion and Partitioning in Contaminated Drinking Water Pipes under Stagnant Conditions.   ACS ES&T Water. American Chemical Society, Washington, DC, USA, 3(8): 2247-2254, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528322",
-            "keyword": [
-                "Premise Plumbing",
-                "drinking water",
-                "water infrastructure",
-                "Decontamination",
-                "benzene"
-            ],
             "contactPoint": {
                 "fn": "Levi Haupert",
                 "hasEmail": "mailto:haupert.levi@epa.gov"
             },
+            "description": "Benzene concentration time series data during uptake and release from polyethylene drinking water pipes. \n\nThis dataset is associated with the following publication:\nHaupert, L., L. Garcia-Bakarich, N. Sojda, D. Schupp, and M. Magnuson. Benzene Diffusion and Partitioning in Contaminated Drinking Water Pipes under Stagnant Conditions.   ACS ES&T Water. American Chemical Society, Washington, DC, USA, 3(8): 2247-2254, (2023).",
             "distribution": [
                 {
-                    "title": "bz_pipe_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528322/bz_pipe_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "bz_pipe_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528322",
+            "keyword": [
+                "Premise Plumbing",
+                "drinking water",
+                "water infrastructure",
+                "Decontamination",
+                "benzene"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-06",
-            "references": [
-                "https://doi.org/10.1021/acsestwater.3c00040"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -179578,57 +179572,66 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acsestwater.3c00040"
+            ],
+            "rights": null,
+            "title": "Sorption modeling data for benzene in polyethylene pipe"
         },
         {
-            "title": "Differential gene expression reveals host factors for viral shedding variation in mallards (Anas platyrhynchos) infected with low-pathogenic avian influenza virus",
-            "description": "Intraspecific variation in pathogen shedding impacts disease transmission dynamics; therefore, understanding the host factors associated with individual variation in pathogen shedding is key to controlling and preventing outbreaks. In this study, ileum and bursa of Fabricius tissues of wild-bred mallards (Anas platyrhynchos) infected with low-pathogenic avian influenza (LPAIV) were evaluated at various post-infection time points to determine genetic host factors associated with intraspecific variation in viral shedding. By analysing transcriptome sequencing data (RNA-seq), we found that LPAIV-infected wild-bred mallards do not exhibit differential gene expression compared to uninfected birds, but that gene expression was associated with cloacal viral shedding quantity early in the infection. In both tissues, immune gene expression was higher in high/moderate shedding birds compared to low shedding birds, and significant positive relationships with viral shedding were observed. In the ileum, expression for host genes involved in viral cell entry was lower in low shedders compared to moderate shedders at 1 day post-infection (DPI), and expression for host genes promoting viral replication was higher in high shedders compared to low shedders at 2 DPI. Our findings indicate that viral shedding is a key factor for gene expression differences in LPAIV-infected wild-bred mallards, and the genes identified in this study could be important for understanding the molecular mechanisms driving intraspecific variation in pathogen shedding. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529426",
-            "keyword": [
-                "Influenza",
-                "shedding",
-                "transcriptomics",
-                "virus"
-            ],
             "contactPoint": {
                 "fn": "Mark Jankowski",
                 "hasEmail": "mailto:jankowski.mark@epa.gov"
             },
+            "description": "Intraspecific variation in pathogen shedding impacts disease transmission dynamics; therefore, understanding the host factors associated with individual variation in pathogen shedding is key to controlling and preventing outbreaks. In this study, ileum and bursa of Fabricius tissues of wild-bred mallards (Anas platyrhynchos) infected with low-pathogenic avian influenza (LPAIV) were evaluated at various post-infection time points to determine genetic host factors associated with intraspecific variation in viral shedding. By analysing transcriptome sequencing data (RNA-seq), we found that LPAIV-infected wild-bred mallards do not exhibit differential gene expression compared to uninfected birds, but that gene expression was associated with cloacal viral shedding quantity early in the infection. In both tissues, immune gene expression was higher in high/moderate shedding birds compared to low shedding birds, and significant positive relationships with viral shedding were observed. In the ileum, expression for host genes involved in viral cell entry was lower in low shedders compared to moderate shedders at 1 day post-infection (DPI), and expression for host genes promoting viral replication was higher in high shedders compared to low shedders at 2 DPI. Our findings indicate that viral shedding is a key factor for gene expression differences in LPAIV-infected wild-bred mallards, and the genes identified in this study could be important for understanding the molecular mechanisms driving intraspecific variation in pathogen shedding. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://zenodo.org/record/8252440",
-                    "accessURL": "https://zenodo.org/record/8252440"
+                    "accessURL": "https://zenodo.org/record/8252440",
+                    "title": "https://zenodo.org/record/8252440"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529426",
+            "keyword": [
+                "Influenza",
+                "shedding",
+                "transcriptomics",
+                "virus"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-03-30",
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
+            "title": "Differential gene expression reveals host factors for viral shedding variation in mallards (Anas platyrhynchos) infected with low-pathogenic avian influenza virus"
         },
         {
-            "title": "Host gene expression is associated with viral shedding magnitude in blue-winged teals (Spatula discors) infected with low-path avian influenza virus",
-            "description": "Intraspecific variation in host infectiousness affects disease transmission dynamics in human, domestic animal, and many wildlife host-pathogen systems including avian influenza virus (AIV); therefore, identifying host factors related to host infectiousness is important for understanding, controlling, and preventing future outbreaks. Toward this goal, we used RNA-seq data collected from low pathogenicity avian influenza virus (LPAIV)-infected blue-winged teal (Spatula discors) to determine the association between host gene expression and intraspecific variation in cloacal viral shedding magnitude, the transmissible fraction of virus. We found that host genes were differentially expressed between LPAIV-infected and uninfected birds early in the infection, host genes were differentially expressed between shed level groups at one-, three-, and five-days post-infection, host gene expression was associated with LPAIV infection patterns over time, and genes of the innate immune system had a positive linear relationship with cloacal viral shedding. This study provides important insights into host gene expression patterns associated with intraspecific LPAIV shedding variation and can serve as a foundation for future studies focused on the identification of host factors that drive or permit the emergence of high viral shedding individuals. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Mark Jankowski",
+                "hasEmail": "mailto:jankowski.mark@epa.gov"
+            },
+            "description": "Intraspecific variation in host infectiousness affects disease transmission dynamics in human, domestic animal, and many wildlife host-pathogen systems including avian influenza virus (AIV); therefore, identifying host factors related to host infectiousness is important for understanding, controlling, and preventing future outbreaks. Toward this goal, we used RNA-seq data collected from low pathogenicity avian influenza virus (LPAIV)-infected blue-winged teal (Spatula discors) to determine the association between host gene expression and intraspecific variation in cloacal viral shedding magnitude, the transmissible fraction of virus. We found that host genes were differentially expressed between LPAIV-infected and uninfected birds early in the infection, host genes were differentially expressed between shed level groups at one-, three-, and five-days post-infection, host gene expression was associated with LPAIV infection patterns over time, and genes of the innate immune system had a positive linear relationship with cloacal viral shedding. This study provides important insights into host gene expression patterns associated with intraspecific LPAIV shedding variation and can serve as a foundation for future studies focused on the identification of host factors that drive or permit the emergence of high viral shedding individuals. Citation information for this dataset can be found in Data.gov's References section.",
+            "distribution": [
+                {
+                    "accessURL": "https://zenodo.org/record/8252576",
+                    "title": "https://zenodo.org/record/8252576"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529427",
             "keyword": [
@@ -179639,60 +179642,51 @@
                 "Supershedders",
                 "viral shedding"
             ],
-            "contactPoint": {
-                "fn": "Mark Jankowski",
-                "hasEmail": "mailto:jankowski.mark@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://zenodo.org/record/8252576",
-                    "accessURL": "https://zenodo.org/record/8252576"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-11-07",
-            "references": [
-                "https://zenodo.org/record/8252600"
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
+                "https://zenodo.org/record/8252600"
+            ],
+            "rights": null,
+            "title": "Host gene expression is associated with viral shedding magnitude in blue-winged teals (Spatula discors) infected with low-path avian influenza virus"
         },
         {
-            "title": "Commercial Equipment Manuscript Dataset 2022",
-            "description": "Dataset of subject matter expert input and response to questions regarding commercial and municipal equipment survey and evaluation for use in large-scale biological incident response operations. \n\nThis dataset is associated with the following publication:\nHayes, C., M. Calfee, and T. Boe. Demonstration and Evaluation of Commercial and Municipal Equipment for Urban Biological Decontamination.   Remediation Journal. John Wiley & Sons, Inc., Hoboken, NJ, USA, 33(3): 249-261, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528091",
-            "keyword": [
-                "Decontamination",
-                "remediation",
-                "Bacillus anthracis",
-                "biological incident"
-            ],
             "contactPoint": {
                 "fn": "Michael Calfee",
                 "hasEmail": "mailto:calfee.worth@epa.gov"
             },
+            "description": "Dataset of subject matter expert input and response to questions regarding commercial and municipal equipment survey and evaluation for use in large-scale biological incident response operations. \n\nThis dataset is associated with the following publication:\nHayes, C., M. Calfee, and T. Boe. Demonstration and Evaluation of Commercial and Municipal Equipment for Urban Biological Decontamination.   Remediation Journal. John Wiley & Sons, Inc., Hoboken, NJ, USA, 33(3): 249-261, (2023).",
             "distribution": [
                 {
-                    "title": "Commercial Equipment Dataset 2022.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528091/Commercial%20Equipment%20Dataset%202022.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Commercial Equipment Dataset 2022.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528091",
+            "keyword": [
+                "Decontamination",
+                "remediation",
+                "Bacillus anthracis",
+                "biological incident"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-10-11",
-            "references": [
-                "https://doi.org/10.1002/rem.21751"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -179702,41 +179696,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/rem.21751"
+            ],
+            "rights": null,
+            "title": "Commercial Equipment Manuscript Dataset 2022"
         },
         {
-            "title": "Bench-scale testing of zeolite membranes for ethanol dehydration",
-            "description": "This Excel file contains the bench-scale testing conditions, fluxes, and calculated performance parameters for NaA, Chabazite, and T-type zeolite membranes in the removal of water from ethanol by pervaporation and vapor permeation. \n\nThis dataset is associated with the following publication:\nVane, L., F. Alvarez, V. Namboodiri, and M. Abar. Ethanol dehydration performance of three types of commercial-grade zeolite permselective membranes.   Journal of Chemical Technology and Biotechnology. John Wiley and Sons, LTD,   UK, 97(8): 1966-1977, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1524773",
-            "keyword": [
-                "Membrane Technology",
-                "solvent reclamation",
-                "materials management",
-                "solvent dehydration"
-            ],
             "contactPoint": {
                 "fn": "Leland Vane",
                 "hasEmail": "mailto:vane.leland@epa.gov"
             },
+            "description": "This Excel file contains the bench-scale testing conditions, fluxes, and calculated performance parameters for NaA, Chabazite, and T-type zeolite membranes in the removal of water from ethanol by pervaporation and vapor permeation. \n\nThis dataset is associated with the following publication:\nVane, L., F. Alvarez, V. Namboodiri, and M. Abar. Ethanol dehydration performance of three types of commercial-grade zeolite permselective membranes.   Journal of Chemical Technology and Biotechnology. John Wiley and Sons, LTD,   UK, 97(8): 1966-1977, (2022).",
             "distribution": [
                 {
-                    "title": "Zeolite Membrane Results-Values for Graphs.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524773/Zeolite%20Membrane%20Results-Values%20for%20Graphs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Zeolite Membrane Results-Values for Graphs.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1524773",
+            "keyword": [
+                "Membrane Technology",
+                "solvent reclamation",
+                "materials management",
+                "solvent dehydration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-03-17",
-            "references": [
-                "https://doi.org/10.1002/jctb.7141"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -179746,19 +179740,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/jctb.7141"
+            ],
+            "rights": null,
+            "title": "Bench-scale testing of zeolite membranes for ethanol dehydration"
         },
         {
-            "title": "Speciation of inorganic arsenic with LC-EIS-MS",
-            "description": "This is the manuscript and supplementary material for \"Speciation of Inorganic Arsenic with Mixed-Mode HPLC- Electrospray Ionization-Mass Spectrometry and Arsenite Oxidation\". \n\nThis dataset is associated with the following publication:\nLi, T. Speciation of inorganic arsenic with mixed mode HPLC-ESI-MS and Arsenite Oxidation.   TALANTA. Elsevier Science Ltd, New York, NY, USA, 259: 124487, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Tao Li",
+                "hasEmail": "mailto:li.tao@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529430/documents/Data%20dictionary%20for%20iAs%20specition%2021Aug2023.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This is the manuscript and supplementary material for \"Speciation of Inorganic Arsenic with Mixed-Mode HPLC- Electrospray Ionization-Mass Spectrometry and Arsenite Oxidation\". \n\nThis dataset is associated with the following publication:\nLi, T. Speciation of inorganic arsenic with mixed mode HPLC-ESI-MS and Arsenite Oxidation.   TALANTA. Elsevier Science Ltd, New York, NY, USA, 259: 124487, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529430/Speciation%20of%20iAs%2022Mar23%20clean%20copy.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Speciation of iAs 22Mar23 clean copy.pdf"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529430",
             "keyword": [
@@ -179770,22 +179776,10 @@
                 "groundwater",
                 "arsenic"
             ],
-            "contactPoint": {
-                "fn": "Tao Li",
-                "hasEmail": "mailto:li.tao@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Speciation of iAs 22Mar23 clean copy.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529430/Speciation%20of%20iAs%2022Mar23%20clean%20copy.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-21",
-            "references": [
-                "https://doi.org/10.1016/j.talanta.2023.124487",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10152742",
-                "https://pasteur.epa.gov/uploads/10.23719/1529430/documents/Supplementary%20material%20for%20iAs%2022Mar23.docx"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -179796,20 +179790,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529430/documents/Data%20dictionary%20for%20iAs%20specition%2021Aug2023.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.talanta.2023.124487",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10152742",
+                "https://pasteur.epa.gov/uploads/10.23719/1529430/documents/Supplementary%20material%20for%20iAs%2022Mar23.docx"
+            ],
+            "rights": null,
+            "title": "Speciation of inorganic arsenic with LC-EIS-MS"
         },
         {
-            "title": "Dataset for Method Development for Thermal Desorption-Gas Chromatography-Tandem Mass Spectrometry (TD-GC-MS/MS) Analysis of Trace Level Fluorotelomer Alcohols Emitted from Consumer Products",
-            "description": "The data presented in this data file is a product of a journal publication. The dataset contains FTOH concentrations detected in standards and consumer products and their emissions concentrations from consumer products. \n\nThis dataset is associated with the following publication:\nRobbins, Z., X. Liu, B. Schumacher, M. Smeltz, and H. Liberatore. Method Development for Thermal Desorption-Gas Chromatography-Tandem Mass Spectrometry (TD-GC-MS/MS) Analysis of Trace Level Fluorotelomer Alcohols Emitted from Consumer Products.   JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1705: NA, (2923).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Xiaoyu Liu",
+                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
+            },
+            "description": "The data presented in this data file is a product of a journal publication. The dataset contains FTOH concentrations detected in standards and consumer products and their emissions concentrations from consumer products. \n\nThis dataset is associated with the following publication:\nRobbins, Z., X. Liu, B. Schumacher, M. Smeltz, and H. Liberatore. Method Development for Thermal Desorption-Gas Chromatography-Tandem Mass Spectrometry (TD-GC-MS/MS) Analysis of Trace Level Fluorotelomer Alcohols Emitted from Consumer Products.   JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1705: NA, (2923).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528682/XiaoyuLiu_PFAS%20Analytical%20Paper_Data%20Tables%26Dictionary-03172023.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "XiaoyuLiu_PFAS Analytical Paper_Data Tables&Dictionary-03172023.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528682",
             "keyword": [
@@ -179820,20 +179824,10 @@
                 "thermal desorption",
                 "emissions"
             ],
-            "contactPoint": {
-                "fn": "Xiaoyu Liu",
-                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "XiaoyuLiu_PFAS Analytical Paper_Data Tables&Dictionary-03172023.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528682/XiaoyuLiu_PFAS%20Analytical%20Paper_Data%20Tables%26Dictionary-03172023.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-17",
-            "references": [
-                "https://doi.org/10.1016/j.chroma.2023.464204"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -179843,123 +179837,123 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chroma.2023.464204"
+            ],
+            "rights": null,
+            "title": "Dataset for Method Development for Thermal Desorption-Gas Chromatography-Tandem Mass Spectrometry (TD-GC-MS/MS) Analysis of Trace Level Fluorotelomer Alcohols Emitted from Consumer Products"
         },
         {
-            "title": "Combined NRSA benthic macroinvertebrate indices and landscape data for Random Forest Analysis.",
-            "description": "Combined benthic macroinvertebrate indices and landscape data used in random forest analysis. Data is from the 2008/2009 National Rivers and Streams Assessment. All data and meta data are also available on the US EPA NARS website. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529412",
-            "keyword": [
-                "Benthic Macroinvertebrate Index",
-                "Landscape data",
-                "Random Forest Analysis"
-            ],
             "contactPoint": {
                 "fn": "Richard Mitchell",
                 "hasEmail": "mailto:mitchell.richard@epa.gov"
             },
+            "description": "Combined benthic macroinvertebrate indices and landscape data used in random forest analysis. Data is from the 2008/2009 National Rivers and Streams Assessment. All data and meta data are also available on the US EPA NARS website. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "CombinedNRSA0809.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529412/CombinedNRSA0809.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "CombinedNRSA0809.csv"
                 },
                 {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529412",
+            "keyword": [
+                "Benthic Macroinvertebrate Index",
+                "Landscape data",
+                "Random Forest Analysis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-08-08",
-            "references": [
-                "https://dx.doi.org/10.1007/s13253-021-00479-7",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10442734"
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
+                "https://dx.doi.org/10.1007/s13253-021-00479-7",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10442734"
+            ],
+            "rights": null,
+            "title": "Combined NRSA benthic macroinvertebrate indices and landscape data for Random Forest Analysis."
         },
         {
-            "title": "Six-Year Review 3 Compliance Monitoring Data (2006-2011)",
-            "description": "In December 2016, EPA announced the review results for the Agency\u2019s third Six-Year Review (called Six-Year Review 3). EPA analyzed compliance monitoring data for the Six-Year Review 3 using data provided by states/primacy agencies through the Information Collection Request (ICR) for Six-Year Review 3 covering January 2006 through December 2011.\n\nEach zip file contains data for multiple contaminants and related information that can be unzipped into tab delimited text files. The number of records and associated systems in the data files and the size of the files range considerably from contaminant to contaminant, which may be attributed to many factors such as the applicability of monitoring requirements, the required sampling frequency and results from quality assurance/quality control (QA/QC) measures. \n \nA detailed description of the data fields and their definitions, notes about the data, and instructions for downloading and importing datasets into software applications such as Excel can be found in the User Guide. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529436",
-            "keyword": [
-                "water",
-                "National Primary Drinking Water Regulation",
-                "drinking water",
-                "drinking water quality"
-            ],
             "contactPoint": {
                 "fn": "Richard Weisman",
                 "hasEmail": "mailto:weisman.richard@epa.gov"
             },
+            "description": "In December 2016, EPA announced the review results for the Agency\u2019s third Six-Year Review (called Six-Year Review 3). EPA analyzed compliance monitoring data for the Six-Year Review 3 using data provided by states/primacy agencies through the Information Collection Request (ICR) for Six-Year Review 3 covering January 2006 through December 2011.\n\nEach zip file contains data for multiple contaminants and related information that can be unzipped into tab delimited text files. The number of records and associated systems in the data files and the size of the files range considerably from contaminant to contaminant, which may be attributed to many factors such as the applicability of monitoring requirements, the required sampling frequency and results from quality assurance/quality control (QA/QC) measures. \n \nA detailed description of the data fields and their definitions, notes about the data, and instructions for downloading and importing datasets into software applications such as Excel can be found in the User Guide. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://www.epa.gov/dwsixyearreview/six-year-review-3-compliance-monitoring-data-2006-2011",
-                    "accessURL": "https://www.epa.gov/dwsixyearreview/six-year-review-3-compliance-monitoring-data-2006-2011"
+                    "accessURL": "https://www.epa.gov/dwsixyearreview/six-year-review-3-compliance-monitoring-data-2006-2011",
+                    "title": "https://www.epa.gov/dwsixyearreview/six-year-review-3-compliance-monitoring-data-2006-2011"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529436",
+            "keyword": [
+                "water",
+                "National Primary Drinking Water Regulation",
+                "drinking water",
+                "drinking water quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-02-09",
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
+            "title": "Six-Year Review 3 Compliance Monitoring Data (2006-2011)"
         },
         {
-            "title": "National Criteria and Hazardous Air Pollutant Totals By Industry 2017 v2.0",
-            "description": "This is an update of v1.1 of this dataset (https://doi.org/10.1038/s41597-022-01293-7). This dataset distinguishes air emissions with more context information (e.g. urban vs. rural; release height categories) using secondary context descriptions from the Federal LCA Commons Elementary Flow List, and building of a new point-source release dataset from StEWI (https://github.com/USEPA/standardizedinventories).  This dataset was generated with FLOWSA v2.0.0. using the flow-by-sector attribution model CAP_HAP_national_2017_m2. The link for that model specification file and more metadata can be found in the associated metadata.json file. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529153",
-            "keyword": [
-                "criteria air pollutant emissions",
-                "hazardous air pollutant emissions",
-                "FLOWSA"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/f7fabfbf2cef3920780920d147ffbb089fbce9eb/format%20specs/FlowBySector.md",
+            "description": "This is an update of v1.1 of this dataset (https://doi.org/10.1038/s41597-022-01293-7). This dataset distinguishes air emissions with more context information (e.g. urban vs. rural; release height categories) using secondary context descriptions from the Federal LCA Commons Elementary Flow List, and building of a new point-source release dataset from StEWI (https://github.com/USEPA/standardizedinventories).  This dataset was generated with FLOWSA v2.0.0. using the flow-by-sector attribution model CAP_HAP_national_2017_m2. The link for that model specification file and more metadata can be found in the associated metadata.json file. ",
             "distribution": [
                 {
-                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CAP_HAP_national_2017_m2_v2.0.0_a52db57.parquet",
-                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CAP_HAP_national_2017_m2_v2.0.0_a52db57.parquet"
+                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CAP_HAP_national_2017_m2_v2.0.0_a52db57.parquet",
+                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CAP_HAP_national_2017_m2_v2.0.0_a52db57.parquet"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529153",
+            "keyword": [
+                "criteria air pollutant emissions",
+                "hazardous air pollutant emissions",
+                "FLOWSA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-22",
-            "references": [
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CAP_HAP_national_2017_m2_v2.0.0_a52db57_metadata.json",
-                "https://github.com/USEPA/flowsa/blob/a52db57a4f69feb1e4b7aa336a86a81eeae63c04/flowsa/methods/flowbysectormethods/CAP_HAP_national_2017_m2.yaml"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -179970,38 +179964,41 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/f7fabfbf2cef3920780920d147ffbb089fbce9eb/format%20specs/FlowBySector.md"
+            "references": [
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CAP_HAP_national_2017_m2_v2.0.0_a52db57_metadata.json",
+                "https://github.com/USEPA/flowsa/blob/a52db57a4f69feb1e4b7aa336a86a81eeae63c04/flowsa/methods/flowbysectormethods/CAP_HAP_national_2017_m2.yaml"
+            ],
+            "rights": null,
+            "title": "National Criteria and Hazardous Air Pollutant Totals By Industry 2017 v2.0"
         },
         {
-            "title": "DIO v2.0",
-            "description": "DIO is the Defense Input-Output Model, v2.0.  It was built using useeior v1.2.1. This is an export of that model in Excel format.  The source code can be found in https://github.com/USEPA/DIO. All tabs correspond to the useeior Model format.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529152",
-            "keyword": [
-                "USEEIO",
-                "input-output"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/useeior/blob/v1.2.1/format_specs/Model.md#model",
+            "description": "DIO is the Defense Input-Output Model, v2.0.  It was built using useeior v1.2.1. This is an export of that model in Excel format.  The source code can be found in https://github.com/USEPA/DIO. All tabs correspond to the useeior Model format.",
             "distribution": [
                 {
-                    "title": "DIOv2.0_w_metadata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529152/DIOv2.0_w_metadata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DIOv2.0_w_metadata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529152",
+            "keyword": [
+                "USEEIO",
+                "input-output"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-06-22",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -180011,42 +180008,39 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/useeior/blob/v1.2.1/format_specs/Model.md#model"
+            "references": null,
+            "rights": null,
+            "title": "DIO v2.0"
         },
         {
-            "title": "Roll Hill SciHUB 1-30-23",
-            "description": "\u201cHonest Broker\u201d accessed the Medicaid data for the Villages at Roll Hill at zip code 45225. A complete Ohio Medicaid data set was only available for the years 2013 through 2021. \u201cHonest Broker\u201d determined the diagnosis of asthma for 7-year-olds based on the International Classification of Diseases. Member cohort eligibility was based on continuous residence at zip code 45225 for 24 months, i.e., the cohort year and the previous year. \n\nThis dataset is associated with the following publication:\nBeck, A.F., L. Wymer, E. Pinzer, W. Friedman, P. Ashley, and S. Vesper. Reduced prevalence of childhood asthma after housing renovations in an under-resourced community.   Journal of Allergy and Clinical Immunology: Global. Elsevier B.V., Amsterdam,  NETHERLANDS, 2(4): 100143, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528526",
-            "keyword": [
-                "black",
-                "asthma",
-                "infants",
-                "green-building",
-                "African American"
-            ],
             "contactPoint": {
                 "fn": "Stephen Vesper",
                 "hasEmail": "mailto:vesper.stephen@epa.gov"
             },
+            "description": "\u201cHonest Broker\u201d accessed the Medicaid data for the Villages at Roll Hill at zip code 45225. A complete Ohio Medicaid data set was only available for the years 2013 through 2021. \u201cHonest Broker\u201d determined the diagnosis of asthma for 7-year-olds based on the International Classification of Diseases. Member cohort eligibility was based on continuous residence at zip code 45225 for 24 months, i.e., the cohort year and the previous year. \n\nThis dataset is associated with the following publication:\nBeck, A.F., L. Wymer, E. Pinzer, W. Friedman, P. Ashley, and S. Vesper. Reduced prevalence of childhood asthma after housing renovations in an under-resourced community.   Journal of Allergy and Clinical Immunology: Global. Elsevier B.V., Amsterdam,  NETHERLANDS, 2(4): 100143, (2023).",
             "distribution": [
                 {
-                    "title": "Roll Hill SciHUB 6-30-22.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528526/Roll%20Hill%20SciHUB%206-30-22.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Roll Hill SciHUB 6-30-22.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528526",
+            "keyword": [
+                "black",
+                "asthma",
+                "infants",
+                "green-building",
+                "African American"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-30",
-            "references": [
-                "https://doi.org/10.1016/j.jacig.2023.100143"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180056,20 +180050,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
             },
-        {
-            "title": "Human alterations of the global floodplains 1965-2019",
-            "description": "We developed the first publicly available spatially explicit estimates of the human alterations along the global floodplains during the recent 27 years (1992-2019) at 250-m resolution. To maximize the reuse of our datasets and advance the open science of human floodplain alteration, we developed three web-based programming tools: (1) Floodplain Mapping Tool, (2) Land Use Change Tool, and (3) Human Alteration Tool supported with tutorials and step-by-step audiovisual instructions. Our data reveal a significant loss of natural floodplains worldwide with 460,000 km2 of new agricultural and 140,000 km2 of new developed areas between 1992 and 2019. This dataset offers critical new insights into how floodplains are being destroyed, which will help decision-makers to reinforce strategies to conserve and restore floodplain functions and habitat. This dataset is not publicly accessible because: EPA scientists provided context and commentary but did not do any of the analyses or handle any of the data. It can be accessed through the following means: The entire data record can be downloaded as a single zip file from this web link: http://www.hydroshare.org/resource/cdb5fd97e0644a14b22e58d05299f69b.\r\n\r\nThe global floodplain alteration dataset is derived entirely through ArcGIS 10.5 and ENVI 5.1 geospatial analysis platforms. To assist in reuse and application of the dataset, we developed additional Python codes aggregated as three web-based tools:  \r\n\r\nFloodplain Mapping Tool: https://colab.research.google.com/drive/1xQlARZXKPexmDInYV-EMoJ-HZxmFL-eW?usp=sharing. \r\nLand Use Change Tool: https://colab.research.google.com/drive/1vmIaUCkL66CoTv4rNRIWpJXYXp4TlAKd?usp=sharing. \r\nHuman Alteration Tool: https://colab.research.google.com/drive/1r2zNJNpd3aWSuDV2Kc792qSEjvDbFtBy?usp=share_link   \r\n\r\nSee Usage Notes section in the journal article for details. Format: The global floodplain alteration dataset is available through the HydroShare open geospatial data platform. Our data record also includes all corresponding input data, intermediate calculations, and supporting information. \n\nThis dataset is associated with the following publication:\nRajib, A., Q. Zheng, C. Lane, H. Golden, J. Christensen, I. Isibor, and K. Johnson. Human alterations of the global floodplains 1992\u20132019.   Scientific Data. Springer Nature, New York, NY, USA, 10: 499, (2023).",
-            "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
+            "references": [
+                "https://doi.org/10.1016/j.jacig.2023.100143"
+            ],
+            "rights": null,
+            "title": "Roll Hill SciHUB 1-30-23"
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
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "We developed the first publicly available spatially explicit estimates of the human alterations along the global floodplains during the recent 27 years (1992-2019) at 250-m resolution. To maximize the reuse of our datasets and advance the open science of human floodplain alteration, we developed three web-based programming tools: (1) Floodplain Mapping Tool, (2) Land Use Change Tool, and (3) Human Alteration Tool supported with tutorials and step-by-step audiovisual instructions. Our data reveal a significant loss of natural floodplains worldwide with 460,000 km2 of new agricultural and 140,000 km2 of new developed areas between 1992 and 2019. This dataset offers critical new insights into how floodplains are being destroyed, which will help decision-makers to reinforce strategies to conserve and restore floodplain functions and habitat. This dataset is not publicly accessible because: EPA scientists provided context and commentary but did not do any of the analyses or handle any of the data. It can be accessed through the following means: The entire data record can be downloaded as a single zip file from this web link: http://www.hydroshare.org/resource/cdb5fd97e0644a14b22e58d05299f69b.\r\n\r\nThe global floodplain alteration dataset is derived entirely through ArcGIS 10.5 and ENVI 5.1 geospatial analysis platforms. To assist in reuse and application of the dataset, we developed additional Python codes aggregated as three web-based tools:  \r\n\r\nFloodplain Mapping Tool: https://colab.research.google.com/drive/1xQlARZXKPexmDInYV-EMoJ-HZxmFL-eW?usp=sharing. \r\nLand Use Change Tool: https://colab.research.google.com/drive/1vmIaUCkL66CoTv4rNRIWpJXYXp4TlAKd?usp=sharing. \r\nHuman Alteration Tool: https://colab.research.google.com/drive/1r2zNJNpd3aWSuDV2Kc792qSEjvDbFtBy?usp=share_link   \r\n\r\nSee Usage Notes section in the journal article for details. Format: The global floodplain alteration dataset is available through the HydroShare open geospatial data platform. Our data record also includes all corresponding input data, intermediate calculations, and supporting information. \n\nThis dataset is associated with the following publication:\nRajib, A., Q. Zheng, C. Lane, H. Golden, J. Christensen, I. Isibor, and K. Johnson. Human alterations of the global floodplains 1992\u20132019.   Scientific Data. Springer Nature, New York, NY, USA, 10: 499, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1528437",
             "keyword": [
                 "ecosystem services",
@@ -180078,15 +180076,10 @@
                 "floodplains",
                 "climate change"
             ],
-            "contactPoint": {
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-01-14",
-            "references": [
-                "https://doi.org/10.1038/s41597-023-02382-x",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10382548"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180096,19 +180089,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41597-023-02382-x",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10382548"
+            ],
+            "rights": null,
+            "title": "Human alterations of the global floodplains 1965-2019"
         },
         {
-            "title": "sptotal R package data",
-            "description": "The data are just illustrative tools to help users understand how the sptotal R package works. As a result, those interested in sptotal, which may include EPA and the general public, may be interested in the data. \n\nThis dataset is associated with the following publication:\nHigham, M., J. Ver Hoef, B. Frank, and M. Dumelle. sptotal: an R package for predicting totals and weighted sums from spatial data.   Journal of Open Source Software. Journal of Open Source Software,    8(85): 05363, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Michael Dumelle",
+                "hasEmail": "mailto:dumelle.michael@epa.gov"
+            },
+            "description": "The data are just illustrative tools to help users understand how the sptotal R package works. As a result, those interested in sptotal, which may include EPA and the general public, may be interested in the data. \n\nThis dataset is associated with the following publication:\nHigham, M., J. Ver Hoef, B. Frank, and M. Dumelle. sptotal: an R package for predicting totals and weighted sums from spatial data.   Journal of Open Source Software. Journal of Open Source Software,    8(85): 05363, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://CRAN.R-project.org/package=sptotal",
+                    "title": "https://CRAN.R-project.org/package=sptotal"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529130",
             "keyword": [
@@ -180118,19 +180121,10 @@
                 "prediction",
                 "Correlation"
             ],
-            "contactPoint": {
-                "fn": "Michael Dumelle",
-                "hasEmail": "mailto:dumelle.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://CRAN.R-project.org/package=sptotal",
-                    "accessURL": "https://CRAN.R-project.org/package=sptotal"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-12-11",
-            "references": [
-                "https://doi.org/10.21105/joss.05363"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180140,63 +180134,63 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.21105/joss.05363"
+            ],
+            "rights": null,
+            "title": "sptotal R package data"
         },
         {
-            "title": "Cognitive tests conducted in male and females offspring that were exposed to Manganese and/or stress during the perinatal period",
-            "description": "Cognitive tests included in this assessment.\nNovel object recognition (NOR) test data: habituation trial, training trial and test trial.\nMorris water maze (MWM): Acquisition, reference probe, and reversal challenge \nDifferential reinforcement of low rates (DRL): Autoshaping and efficiency data from DRL\nCued and uncued choice reaction time (CRT): Accuracy, Anticipatory responding, decision and movement time. \n\nThis dataset is associated with the following publication:\nOshiro, W., K. McDaniel, T. Beasley, G. Moser, and D. Herr. Impacts of a perinatal exposure to manganese coupled with maternal stress in rats: Learning, memory and attentional function in exposed offspring..   NEUROTOXICOLOGY AND TERATOLOGY. Elsevier Science Ltd, New York, NY, USA, 91(May-June 2022): 107077, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1523129",
-            "keyword": [
-                "perinatal stress",
-                "manganese",
-                "cognitive functions",
-                "neurodevelopmental neurotoxicity",
-                "Rats",
-                "Combined Effects"
-            ],
             "contactPoint": {
                 "fn": "Wendy Oshiro",
                 "hasEmail": "mailto:oshiro.wendy@epa.gov"
             },
+            "description": "Cognitive tests included in this assessment.\nNovel object recognition (NOR) test data: habituation trial, training trial and test trial.\nMorris water maze (MWM): Acquisition, reference probe, and reversal challenge \nDifferential reinforcement of low rates (DRL): Autoshaping and efficiency data from DRL\nCued and uncued choice reaction time (CRT): Accuracy, Anticipatory responding, decision and movement time. \n\nThis dataset is associated with the following publication:\nOshiro, W., K. McDaniel, T. Beasley, G. Moser, and D. Herr. Impacts of a perinatal exposure to manganese coupled with maternal stress in rats: Learning, memory and attentional function in exposed offspring..   NEUROTOXICOLOGY AND TERATOLOGY. Elsevier Science Ltd, New York, NY, USA, 91(May-June 2022): 107077, (2022).",
             "distribution": [
                 {
-                    "title": "MWM_SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523129/MWM_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MWM_SciHub.xlsx"
                 },
                 {
-                    "title": "UnCued CRT_SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523129/UnCued%20CRT_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "UnCued CRT_SciHub.xlsx"
                 },
                 {
-                    "title": "Cued CRT_SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523129/Cued%20CRT_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Cued CRT_SciHub.xlsx"
                 },
                 {
-                    "title": "AS_DRL_SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523129/AS_DRL_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AS_DRL_SciHub.xlsx"
                 },
                 {
-                    "title": "NOR_SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523129/NOR_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NOR_SciHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1523129",
+            "keyword": [
+                "perinatal stress",
+                "manganese",
+                "cognitive functions",
+                "neurodevelopmental neurotoxicity",
+                "Rats",
+                "Combined Effects"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-09-17",
-            "references": [
-                "https://doi.org/10.1016/j.ntt.2022.107077"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180206,19 +180200,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ntt.2022.107077"
+            ],
+            "rights": null,
+            "title": "Cognitive tests conducted in male and females offspring that were exposed to Manganese and/or stress during the perinatal period"
         },
         {
-            "title": "State IO Two-Region Economic Input-Output Models for 50 U.S. States 2012-2017",
-            "description": "These are economic models in Make and Use formats with variations of one and two-region versions where the one region is just a U.S. state of interest (SoI) and the two-region version include both the SoI and Rest of the U.S. (RoUS). Inudstry and Commodity output vectors are also provided. Models are available representing annual totals for each year for each state from 2012 to 2017. Variations for \"Domestic\" forms of models are available. See the associated publication, also available without fees in PubMed, for details. These models were created with stateior v0.1.0 (https://github.com/USEPA/stateior/releases/tag/0.1.0). and can be used in that R software.  See https://github.com/USEPA/stateior/tree/0.1.0 for usage details. The provided data link reveals many R Data Format (.RDS) files that can be read into R, along with metadata files in JSON format that provide information on provenance of the data. File names corresponded with the definitions in the associated data dictionary (for two-region files) and the associated supporting link (for one-region files). Other files are precursors to the one and two-region models with data that are used in the model building process and can be read into R.   All model files corresponding to the associated publication have the the text \"0.1.0\" in the filename, for example \"Census_StateExport_2013_0.1.0.rds\". Each file contains all states for the year in the file name with a year is included. \n\nThis dataset is associated with the following publication:\nLi, M., J. Ferreira, C.D. Court, D. Meyer, M. Li, and W.W. Ingwersen. StateIO - Open Source Economic Input-Output Models for the 50 States of the United States of America.   International Regional Science Review. SAGE Publications, THOUSAND OAKS, CA, USA, 46(4): 428-481, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Wesley Ingwersen",
+                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
+            },
+            "describedBy": "https://github.com/USEPA/stateior/blob/0.1.0/format_specs/TwoRegionData.md",
+            "description": "These are economic models in Make and Use formats with variations of one and two-region versions where the one region is just a U.S. state of interest (SoI) and the two-region version include both the SoI and Rest of the U.S. (RoUS). Inudstry and Commodity output vectors are also provided. Models are available representing annual totals for each year for each state from 2012 to 2017. Variations for \"Domestic\" forms of models are available. See the associated publication, also available without fees in PubMed, for details. These models were created with stateior v0.1.0 (https://github.com/USEPA/stateior/releases/tag/0.1.0). and can be used in that R software.  See https://github.com/USEPA/stateior/tree/0.1.0 for usage details. The provided data link reveals many R Data Format (.RDS) files that can be read into R, along with metadata files in JSON format that provide information on provenance of the data. File names corresponded with the definitions in the associated data dictionary (for two-region files) and the associated supporting link (for one-region files). Other files are precursors to the one and two-region models with data that are used in the model building process and can be read into R.   All model files corresponding to the associated publication have the the text \"0.1.0\" in the filename, for example \"Census_StateExport_2013_0.1.0.rds\". Each file contains all states for the year in the file name with a year is included. \n\nThis dataset is associated with the following publication:\nLi, M., J. Ferreira, C.D. Court, D. Meyer, M. Li, and W.W. Ingwersen. StateIO - Open Source Economic Input-Output Models for the 50 States of the United States of America.   International Regional Science Review. SAGE Publications, THOUSAND OAKS, CA, USA, 46(4): 428-481, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/index.html?prefix=stateio/",
+                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/index.html?prefix=stateio/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529442",
             "keyword": [
@@ -180229,21 +180233,10 @@
                 "interstate trade",
                 "regional science"
             ],
-            "contactPoint": {
-                "fn": "Wesley Ingwersen",
-                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/index.html?prefix=stateio/",
-                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/index.html?prefix=stateio/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-16",
-            "references": [
-                "https://doi.org/10.1177/01600176221145874",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10324549",
-                "https://github.com/USEPA/stateior/blob/0.1.0/format_specs/OneRegionData.md"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180254,45 +180247,46 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/stateior/blob/0.1.0/format_specs/TwoRegionData.md"
+            "references": [
+                "https://doi.org/10.1177/01600176221145874",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10324549",
+                "https://github.com/USEPA/stateior/blob/0.1.0/format_specs/OneRegionData.md"
+            ],
+            "rights": null,
+            "title": "State IO Two-Region Economic Input-Output Models for 50 U.S. States 2012-2017"
         },
         {
-            "title": "Characterizing surface water concentrations of hundreds of organic chemicals in United States for environmental risk prioritization",
-            "description": "The initial analysis set was downloaded from https://www.waterqualitydata.us/ using queries described in the file load_water_data.py, hosted at https://github.com/USEPA/EcoSEEM-Consensus-Model-for-Chemicals-in-Surface-Water/tree/master/observation_data. The representative concentration ranges and bioactivity:exposure ratio results are available at the same GitHub repo in the file all_chem_res.csv. \n\nThis dataset is associated with the following publication:\nSayre, R., R. Setzer, M. Serre, and J. Wambaugh. Characterizing surface water concentrations of hundreds of organic chemicals in United States for environmental risk prioritization.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 33: 610-619, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528953",
-            "keyword": [
-                "chemicals",
-                "exposure",
-                "environmental statistics",
-                "water",
-                "ExpoCast"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "The initial analysis set was downloaded from https://www.waterqualitydata.us/ using queries described in the file load_water_data.py, hosted at https://github.com/USEPA/EcoSEEM-Consensus-Model-for-Chemicals-in-Surface-Water/tree/master/observation_data. The representative concentration ranges and bioactivity:exposure ratio results are available at the same GitHub repo in the file all_chem_res.csv. \n\nThis dataset is associated with the following publication:\nSayre, R., R. Setzer, M. Serre, and J. Wambaugh. Characterizing surface water concentrations of hundreds of organic chemicals in United States for environmental risk prioritization.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 33: 610-619, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.waterqualitydata.us/",
-                    "accessURL": "https://www.waterqualitydata.us/"
+                    "accessURL": "https://www.waterqualitydata.us/",
+                    "title": "https://www.waterqualitydata.us/"
                 },
                 {
-                    "title": "https://github.com/USEPA/EcoSEEM-Consensus-Model-for-Chemicals-in-Surface-Water/tree/master/observation_data",
-                    "accessURL": "https://github.com/USEPA/EcoSEEM-Consensus-Model-for-Chemicals-in-Surface-Water/tree/master/observation_data"
+                    "accessURL": "https://github.com/USEPA/EcoSEEM-Consensus-Model-for-Chemicals-in-Surface-Water/tree/master/observation_data",
+                    "title": "https://github.com/USEPA/EcoSEEM-Consensus-Model-for-Chemicals-in-Surface-Water/tree/master/observation_data"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528953",
+            "keyword": [
+                "chemicals",
+                "exposure",
+                "environmental statistics",
+                "water",
+                "ExpoCast"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-11-08",
-            "references": [
-                "https://doi.org/10.1038/s41370-022-00501-1"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180302,41 +180296,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41370-022-00501-1"
+            ],
+            "rights": null,
+            "title": "Characterizing surface water concentrations of hundreds of organic chemicals in United States for environmental risk prioritization"
         },
         {
-            "title": "Science Hub for Stoner et al. 2021_V1",
-            "description": "This dataset details the types of pollen collected by honey bees located on the grounds of two ornamental plant nurseries in Connecticut. \n\nThis dataset is associated with the following publication:\nStoner, K., A. Nurse, R. Richardson, R. Koethe, and D. Lehmann. Where Does Honey Bee (Apis mellifera L.) Pollen Come from? A Study of Pollen Collected from Colonies at Ornamental Plant Nurseries.   Insects. MDPI, Basel,  SWITZERLAND, 13(8): 744, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1523381",
-            "keyword": [
-                "pollinator",
-                "honey bee",
-                "Apis"
-            ],
             "contactPoint": {
                 "fn": "David Lehmann",
                 "hasEmail": "mailto:lehmann.david@epa.gov"
             },
+            "description": "This dataset details the types of pollen collected by honey bees located on the grounds of two ornamental plant nurseries in Connecticut. \n\nThis dataset is associated with the following publication:\nStoner, K., A. Nurse, R. Richardson, R. Koethe, and D. Lehmann. Where Does Honey Bee (Apis mellifera L.) Pollen Come from? A Study of Pollen Collected from Colonies at Ornamental Plant Nurseries.   Insects. MDPI, Basel,  SWITZERLAND, 13(8): 744, (2022).",
             "distribution": [
                 {
-                    "title": "Science Hub file 7-17-2023_FINAL.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523381/Science%20Hub%20file%207-17-2023_FINAL.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science Hub file 7-17-2023_FINAL.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1523381",
+            "keyword": [
+                "pollinator",
+                "honey bee",
+                "Apis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-10-10",
-            "references": [
-                "https://doi.org/10.3390/insects13080744",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9409349"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180346,45 +180339,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/insects13080744",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9409349"
+            ],
+            "rights": null,
+            "title": "Science Hub for Stoner et al. 2021_V1"
         },
         {
-            "title": "A proposed approach to defining per- and polyfluoroalkyl substances (PFAS) based on molecular structure and formula",
-            "description": "Dataset for \"Gaines LGT, Sinclair G, Williams AJ. A proposed approach to defining per- and polyfluoroalkyl substances (PFAS) based on molecular structure and formula. Integr Environ Assess Manag. 2023 Jan 11. doi: 10.1002/ieam.4735. Epub ahead of print. PMID: 36628931\". \n\nThis dataset is associated with the following publication:\nGaines, L., G. Sinclair, and A. Williams. A proposed approach to defining per- and polyfluoroalkyl substances (PFAS) based on molecular structure and formula.   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 19(5): 1333-1347, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528954",
-            "keyword": [
-                "Environmental chemistry",
-                "cheminformatics",
-                "PFAS",
-                "Per- and Polyfluoroalkyl"
-            ],
             "contactPoint": {
                 "fn": "Antony Williams",
                 "hasEmail": "mailto:williams.antony@epa.gov"
             },
+            "description": "Dataset for \"Gaines LGT, Sinclair G, Williams AJ. A proposed approach to defining per- and polyfluoroalkyl substances (PFAS) based on molecular structure and formula. Integr Environ Assess Manag. 2023 Jan 11. doi: 10.1002/ieam.4735. Epub ahead of print. PMID: 36628931\". \n\nThis dataset is associated with the following publication:\nGaines, L., G. Sinclair, and A. Williams. A proposed approach to defining per- and polyfluoroalkyl substances (PFAS) based on molecular structure and formula.   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 19(5): 1333-1347, (2023).",
             "distribution": [
                 {
-                    "title": "https://comptox.epa.gov/dashboard/",
-                    "accessURL": "https://comptox.epa.gov/dashboard/"
+                    "accessURL": "https://comptox.epa.gov/dashboard/",
+                    "title": "https://comptox.epa.gov/dashboard/"
                 },
                 {
-                    "title": "ieam4735-sup-0001-dashboard_refinement_paper_si.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528954/ieam4735-sup-0001-dashboard_refinement_paper_si.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "ieam4735-sup-0001-dashboard_refinement_paper_si.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528954",
+            "keyword": [
+                "Environmental chemistry",
+                "cheminformatics",
+                "PFAS",
+                "Per- and Polyfluoroalkyl"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-02",
-            "references": [
-                "https://doi.org/10.1002/ieam.4735"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180394,19 +180388,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/ieam.4735"
+            ],
+            "rights": null,
+            "title": "A proposed approach to defining per- and polyfluoroalkyl substances (PFAS) based on molecular structure and formula"
         },
         {
-            "title": "ZIP Code-level data on daily temperature, Medicare cardiovascular hospitalizations, and urban heat island intensity, contiguous United States, 2000-2017 ",
-            "description": "These datasets are associated with the manuscript \"Urban Heat Island Impacts on Heat-Related Cardiovascular Morbidity: A Time Series Analysis of Older Adults in US Metropolitan Areas.\" The datasets include (1) ZIP code-level daily average temperature for 2000-2017, (2) ZIP code-level daily counts of Medicare hospitalizations for cardiovascular disease for 2000-2017, and (3) ZIP code-level population-weighted urban heat island intensity (UHII). There are 9,917 ZIP codes included in the datasets, which are located in the urban cores of 120 metropolitan statistical areas across the contiguous United States.\n\n(1) The ZIP code-level daily temperature data is publicly available at: https://doi.org/10.15139/S3/ZL4UF9. A data dictionary is also available at this link. \n\n(2) The ZIP code-level daily counts of Medicare hospitalizations cannot be uploaded to ScienceHub because of privacy requirements in the data use agreement with Medicare.\n\n(3) The ZIP code-level UHII data is attached, along with a data dictionary describing the dataset. Portions of this dataset are inaccessible because: The ZIP code-level daily counts of Medicare cardiovascular disease hospitalizations cannot be uploaded to ScienceHub due to privacy requirements in data use agreements with Medicare. They can be accessed through the following means: The Medicare data can only be accessed internally at EPA with the correct permissions. Format: The Medicare data includes counts of the number of cardiovascular disease hospitalizations in each ZIP code on each day between 2000-2017. \n\nThis dataset is associated with the following publication:\nCleland, S., W. Steinhardt, L. Neas, J. West, and A. Rappold. Urban Heat Island Impacts on Heat-Related Cardiovascular Morbidity: A Time Series Analysis of Older Adults in US Metropolitan Areas.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 178(108005): 1, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Stephanie Cleland",
+                "hasEmail": "mailto:cleland.stephanie@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1528343/documents/Data_Dictionary_zip_UHII.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "These datasets are associated with the manuscript \"Urban Heat Island Impacts on Heat-Related Cardiovascular Morbidity: A Time Series Analysis of Older Adults in US Metropolitan Areas.\" The datasets include (1) ZIP code-level daily average temperature for 2000-2017, (2) ZIP code-level daily counts of Medicare hospitalizations for cardiovascular disease for 2000-2017, and (3) ZIP code-level population-weighted urban heat island intensity (UHII). There are 9,917 ZIP codes included in the datasets, which are located in the urban cores of 120 metropolitan statistical areas across the contiguous United States.\n\n(1) The ZIP code-level daily temperature data is publicly available at: https://doi.org/10.15139/S3/ZL4UF9. A data dictionary is also available at this link. \n\n(2) The ZIP code-level daily counts of Medicare hospitalizations cannot be uploaded to ScienceHub because of privacy requirements in the data use agreement with Medicare.\n\n(3) The ZIP code-level UHII data is attached, along with a data dictionary describing the dataset. Portions of this dataset are inaccessible because: The ZIP code-level daily counts of Medicare cardiovascular disease hospitalizations cannot be uploaded to ScienceHub due to privacy requirements in data use agreements with Medicare. They can be accessed through the following means: The Medicare data can only be accessed internally at EPA with the correct permissions. Format: The Medicare data includes counts of the number of cardiovascular disease hospitalizations in each ZIP code on each day between 2000-2017. \n\nThis dataset is associated with the following publication:\nCleland, S., W. Steinhardt, L. Neas, J. West, and A. Rappold. Urban Heat Island Impacts on Heat-Related Cardiovascular Morbidity: A Time Series Analysis of Older Adults in US Metropolitan Areas.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 178(108005): 1, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.15139/S3/ZL4UF9",
+                    "title": "https://doi.org/10.15139/S3/ZL4UF9"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528343/zip_UHII.csv",
+                    "mediaType": "text/csv",
+                    "title": "zip_UHII.csv"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528343",
             "keyword": [
@@ -180419,24 +180429,10 @@
                 "Metropolitan Statistical Area",
                 "contiguous United States"
             ],
-            "contactPoint": {
-                "fn": "Stephanie Cleland",
-                "hasEmail": "mailto:cleland.stephanie@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.15139/S3/ZL4UF9",
-                    "accessURL": "https://doi.org/10.15139/S3/ZL4UF9"
-                },
-                {
-                    "title": "zip_UHII.csv",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528343/zip_UHII.csv",
-                    "mediaType": "text/csv"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-13",
-            "references": [
-                "https://doi.org/10.1016/j.envint.2023.108005"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180447,42 +180443,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1528343/documents/Data_Dictionary_zip_UHII.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.envint.2023.108005"
+            ],
+            "rights": null,
+            "title": "ZIP Code-level data on daily temperature, Medicare cardiovascular hospitalizations, and urban heat island intensity, contiguous United States, 2000-2017 "
         },
         {
-            "title": "Adaptations of HAEC to ISOPOOH - METADATA v1 112522",
-            "description": "This metadata excel file contains the primary data collected for this project. Each sheet represents the data that corresponds to each individual figure and supplemental data set. \n\nThis dataset is associated with the following publication:\nPennington, E., S. Masood, S. Simmons, L. Dailey, P. Bromberg, R. Rice, A. Gold, Z. Zhang, W. Wu, Y. Yang, and J. Samet. Real-Time Redox Adaptations in Human Airway Epithelial Cells Exposed to Isoprene Hydroxy Hydroperoxide.   Redox Biology. Elsevier B.V., Amsterdam,  NETHERLANDS, 61(102646): 1, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528301",
-            "keyword": [
-                "air pollution",
-                "oxidative stress",
-                "live cell imaging"
-            ],
             "contactPoint": {
                 "fn": "Edward Pennington",
                 "hasEmail": "mailto:pennington.edward@epa.gov"
             },
+            "description": "This metadata excel file contains the primary data collected for this project. Each sheet represents the data that corresponds to each individual figure and supplemental data set. \n\nThis dataset is associated with the following publication:\nPennington, E., S. Masood, S. Simmons, L. Dailey, P. Bromberg, R. Rice, A. Gold, Z. Zhang, W. Wu, Y. Yang, and J. Samet. Real-Time Redox Adaptations in Human Airway Epithelial Cells Exposed to Isoprene Hydroxy Hydroperoxide.   Redox Biology. Elsevier B.V., Amsterdam,  NETHERLANDS, 61(102646): 1, (2023).",
             "distribution": [
                 {
-                    "title": "Adaptations of HAEC to ISOPOOH - METADATA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528301/Adaptations%20of%20HAEC%20to%20ISOPOOH%20-%20METADATA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Adaptations of HAEC to ISOPOOH - METADATA.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528301",
+            "keyword": [
+                "air pollution",
+                "oxidative stress",
+                "live cell imaging"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-11-25",
-            "references": [
-                "https://doi.org/10.1016/j.redox.2023.102646",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10011437"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180492,45 +180485,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.redox.2023.102646",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10011437"
+            ],
+            "rights": null,
+            "title": "Adaptations of HAEC to ISOPOOH - METADATA v1 112522"
         },
         {
-            "title": "Evaluating structure-based activity in a high-throughput assay for steroid biosynthesis",
-            "description": "Dataset from Foster, M.J., et al., Evaluating structure-based activity in a high-throughput assay for steroid biosynthesis, Computational Toxicology, Vol 24, No. 100245, Nov 2022, DOI https://doi.org/10.1016/j.comtox.2022.100245\n\nThe work described herein was conducted in R software (version 4.0.2) and is available at GitHub (https://github.com/USEPA/CompTox-HTH295R-SAR) and the US EPA Clowder repository as well as in Supplemental File 1 as an html file including code and resultant output. \n\nThis dataset is associated with the following publication:\nFoster, M., G. Patlewicz, I. Shah, D. Haggard, R. Judson, and K. Friedman. Evaluating structure-based activity in a high-throughput assay for steroid biosynthesis.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 24: 100245, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529362",
-            "keyword": [
-                "steroidogenesis",
-                "chemotypes",
-                "structure-activity relationships",
-                "Read-across",
-                "in silico screening"
-            ],
             "contactPoint": {
                 "fn": "Katie Friedman",
                 "hasEmail": "mailto:paul-friedman.katie@epa.gov"
             },
+            "description": "Dataset from Foster, M.J., et al., Evaluating structure-based activity in a high-throughput assay for steroid biosynthesis, Computational Toxicology, Vol 24, No. 100245, Nov 2022, DOI https://doi.org/10.1016/j.comtox.2022.100245\n\nThe work described herein was conducted in R software (version 4.0.2) and is available at GitHub (https://github.com/USEPA/CompTox-HTH295R-SAR) and the US EPA Clowder repository as well as in Supplemental File 1 as an html file including code and resultant output. \n\nThis dataset is associated with the following publication:\nFoster, M., G. Patlewicz, I. Shah, D. Haggard, R. Judson, and K. Friedman. Evaluating structure-based activity in a high-throughput assay for steroid biosynthesis.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 24: 100245, (2022).",
             "distribution": [
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/62680e42e4b0e232136663ff",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/62680e42e4b0e232136663ff"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/62680e42e4b0e232136663ff",
+                    "title": "https://clowder.edap-cluster.com/datasets/62680e42e4b0e232136663ff"
                 },
                 {
-                    "title": "https://ccte-bitbucket.epa.gov/users/kpaulfri/repos/hth295r_sar/browse",
-                    "accessURL": "https://ccte-bitbucket.epa.gov/users/kpaulfri/repos/hth295r_sar/browse"
+                    "accessURL": "https://ccte-bitbucket.epa.gov/users/kpaulfri/repos/hth295r_sar/browse",
+                    "title": "https://ccte-bitbucket.epa.gov/users/kpaulfri/repos/hth295r_sar/browse"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529362",
+            "keyword": [
+                "steroidogenesis",
+                "chemotypes",
+                "structure-activity relationships",
+                "Read-across",
+                "in silico screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-23",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2022.100245"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180540,92 +180534,94 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2022.100245"
+            ],
+            "rights": null,
+            "title": "Evaluating structure-based activity in a high-throughput assay for steroid biosynthesis"
         },
         {
-            "title": "Improving the Characterization of several Natural Emissions in CMAQ",
-            "description": "These datasets contains all the data used to make the figures in the associated paper. The excel files are self-explanatory and can be directly used. While the other files in netcdf format, need a visualization tool (such as VERDI) or statistical software (such as R) to make statistical summary or plots. Portions of this dataset are inaccessible because: data will be uploaded when paper will be accepted by journal. They can be accessed through the following means: For excel files, the data can be directly used to make summary or plots. For netcdf files, another visualization tool or statistical package (such as R) can be used. All the netcdf files can be visualized using VERDI. Format: Two types of data formats. One is the excel files which are self-explanatory. The other type is netcdf files which are used to make the spatial plots in the paper. \n\nThis dataset is associated with the following publication:\nKang, D., J. Willison, G. Sarwar, M. Madden, C. Hogrefe, R. Mathur, B. Gantt, and S. Alfonso. Improving the Characterization of the Natural Emissions in CMAQ.   EM Magazine. Air and Waste Management Association, Pittsburgh, PA, USA, (10): 1-7, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1522615",
-            "keyword": [
-                "Lightning NOx emissions",
-                "natural emissions",
-                "MEGAN",
-                "BVOCs",
-                "Halogen",
-                "BEIS"
-            ],
             "contactPoint": {
                 "fn": "Daiwen Kang",
                 "hasEmail": "mailto:kang.daiwen@epa.gov"
             },
+            "description": "These datasets contains all the data used to make the figures in the associated paper. The excel files are self-explanatory and can be directly used. While the other files in netcdf format, need a visualization tool (such as VERDI) or statistical software (such as R) to make statistical summary or plots. Portions of this dataset are inaccessible because: data will be uploaded when paper will be accepted by journal. They can be accessed through the following means: For excel files, the data can be directly used to make summary or plots. For netcdf files, another visualization tool or statistical package (such as R) can be used. All the netcdf files can be visualized using VERDI. Format: Two types of data formats. One is the excel files which are self-explanatory. The other type is netcdf files which are used to make the spatial plots in the paper. \n\nThis dataset is associated with the following publication:\nKang, D., J. Willison, G. Sarwar, M. Madden, C. Hogrefe, R. Mathur, B. Gantt, and S. Alfonso. Improving the Characterization of the Natural Emissions in CMAQ.   EM Magazine. Air and Waste Management Association, Pittsburgh, PA, USA, (10): 1-7, (2021).",
             "distribution": [
                 {
-                    "title": "Region_Mthly_PARMvsNLDN_LNO.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/Region_Mthly_PARMvsNLDN_LNO.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Region_Mthly_PARMvsNLDN_LNO.xlsx"
                 },
                 {
-                    "title": "PARM_LNOx_Monthly_mean_2016_07.ncf.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/PARM_LNOx_Monthly_mean_2016_07.ncf.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "PARM_LNOx_Monthly_mean_2016_07.ncf.zip"
                 },
                 {
-                    "title": "NLDN_LNOx_Monthly_mean_2016_07.ncf.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/NLDN_LNOx_Monthly_mean_2016_07.ncf.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "NLDN_LNOx_Monthly_mean_2016_07.ncf.zip"
                 },
                 {
-                    "title": "megan_july_avg_no_and_isop.nc.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/megan_july_avg_no_and_isop.nc.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "megan_july_avg_no_and_isop.nc.zip"
                 },
                 {
-                    "title": "COMBINE_O3_IMPACT_WINTER_AVG.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/COMBINE_O3_IMPACT_WINTER_AVG.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "COMBINE_O3_IMPACT_WINTER_AVG.zip"
                 },
                 {
-                    "title": "COMBINE_O3_IMPACT_SUMMER_AVG.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/COMBINE_O3_IMPACT_SUMMER_AVG.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "COMBINE_O3_IMPACT_SUMMER_AVG.zip"
                 },
                 {
-                    "title": "COMBINE_O3_IMPACT_SPRING_AVG.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/COMBINE_O3_IMPACT_SPRING_AVG.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "COMBINE_O3_IMPACT_SPRING_AVG.zip"
                 },
                 {
-                    "title": "COMBINE_O3_IMPACT_FALL_AVG.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/COMBINE_O3_IMPACT_FALL_AVG.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "COMBINE_O3_IMPACT_FALL_AVG.zip"
                 },
                 {
-                    "title": "beis_july_avg_no_and_isop.nc.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/beis_july_avg_no_and_isop.nc.zip",
-                    "mediaType": "application/x-netcdf"
+                    "mediaType": "application/x-netcdf",
+                    "title": "beis_july_avg_no_and_isop.nc.zip"
                 },
                 {
-                    "title": "AQS_Daily_O3_v53_INTEL_12US1_2016_CON_MG3.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/AQS_Daily_O3_v53_INTEL_12US1_2016_CON_MG3.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "AQS_Daily_O3_v53_INTEL_12US1_2016_CON_MG3.csv"
                 },
                 {
-                    "title": "AQS_Daily_O3_v53_INTEL_12US1_2016_CON_BE3.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1522615/AQS_Daily_O3_v53_INTEL_12US1_2016_CON_BE3.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "AQS_Daily_O3_v53_INTEL_12US1_2016_CON_BE3.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1522615",
+            "keyword": [
+                "Lightning NOx emissions",
+                "natural emissions",
+                "MEGAN",
+                "BVOCs",
+                "Halogen",
+                "BEIS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-30",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -180634,42 +180630,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Improving the Characterization of several Natural Emissions in CMAQ"
         },
         {
-            "title": "The benthic food web connects the estuarine habitat mosaic to adjacent ecosystems",
-            "description": "Supplementary data for \"Ester Dias, Pedro Morais, Carlos Antunes, Joel C. Hoffman, The benthic food web connects the estuarine habitat mosaic to adjacent ecosystems, Food Webs, Volume 35, 2023, e00282, ISSN 2352-2496, https://doi.org/10.1016/j.fooweb.2023.e00282.\". \n\nThis dataset is associated with the following publication:\nDias, E., P. Morais, C. Antunes, and J. Hoffman. The benthic food web connects the estuarine habitat mosaic to adjacent ecosystems.   Food Webs. Elsevier B.V., Amsterdam,  NETHERLANDS, 35: e00282, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529443",
-            "keyword": [
-                "Detritus",
-                "connectivity",
-                "River discharge",
-                "Food Chain",
-                "stables isotopes"
-            ],
             "contactPoint": {
                 "fn": "Joel Hoffman",
                 "hasEmail": "mailto:hoffman.joel@epa.gov"
             },
+            "description": "Supplementary data for \"Ester Dias, Pedro Morais, Carlos Antunes, Joel C. Hoffman, The benthic food web connects the estuarine habitat mosaic to adjacent ecosystems, Food Webs, Volume 35, 2023, e00282, ISSN 2352-2496, https://doi.org/10.1016/j.fooweb.2023.e00282.\". \n\nThis dataset is associated with the following publication:\nDias, E., P. Morais, C. Antunes, and J. Hoffman. The benthic food web connects the estuarine habitat mosaic to adjacent ecosystems.   Food Webs. Elsevier B.V., Amsterdam,  NETHERLANDS, 35: e00282, (2023).",
             "distribution": [
                 {
-                    "title": "Supplementary data.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529443/Supplementary%20data.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary data.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529443",
+            "keyword": [
+                "Detritus",
+                "connectivity",
+                "River discharge",
+                "Food Chain",
+                "stables isotopes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-02",
-            "references": [
-                "https://doi.org/10.1016/j.fooweb.2023.e00282"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180679,19 +180673,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.fooweb.2023.e00282"
+            ],
+            "rights": null,
+            "title": "The benthic food web connects the estuarine habitat mosaic to adjacent ecosystems"
         },
         {
-            "title": "Matched Sentinel-2 spectral data and chlorophyll a concentrations 2015-2020",
-            "description": "The dataset includes Sentinel-2 spectral data for all bands spatiotemporally matched with available chlorophyll a concentration data from several data sources including the Water Quality Portal.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Wilson Salls",
+                "hasEmail": "mailto:salls.wilson@epa.gov"
+            },
+            "description": "The dataset includes Sentinel-2 spectral data for all bands spatiotemporally matched with available chlorophyll a concentration data from several data sources including the Water Quality Portal.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529420/S2_chla_matchups.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S2_chla_matchups.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529420",
             "keyword": [
@@ -180706,19 +180710,11 @@
                 "Algorithms",
                 "matchups"
             ],
-            "contactPoint": {
-                "fn": "Wilson Salls",
-                "hasEmail": "mailto:salls.wilson@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "S2_chla_matchups.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529420/S2_chla_matchups.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-21",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -180727,41 +180723,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Matched Sentinel-2 spectral data and chlorophyll a concentrations 2015-2020"
         },
         {
-            "title": "Legends, Methods and Supplementary data files.",
-            "description": "The meta data for the tables and figures are described in the Legends, Methods and Supplementary data files. \n\nThis dataset is associated with the following publication:\nSurette, M., D.M. Mitrano, and K. Rogers. Extraction and Concentration of Nanoplastic Particles from Aqueous Suspensions using Functionalized Magnetic Nanoparticles and a Magnetic Flow Cell.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,   ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1524806",
-            "keyword": [
-                "microplastics",
-                "environmental method",
-                "Separation",
-                "nanoplastics"
-            ],
             "contactPoint": {
                 "fn": "Kim Rogers",
                 "hasEmail": "mailto:rogers.kim@epa.gov"
             },
+            "description": "The meta data for the tables and figures are described in the Legends, Methods and Supplementary data files. \n\nThis dataset is associated with the following publication:\nSurette, M., D.M. Mitrano, and K. Rogers. Extraction and Concentration of Nanoplastic Particles from Aqueous Suspensions using Functionalized Magnetic Nanoparticles and a Magnetic Flow Cell.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,   ",
             "distribution": [
                 {
-                    "title": "Nanoplastic_Data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524806/Nanoplastic_Data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Nanoplastic_Data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1524806",
+            "keyword": [
+                "microplastics",
+                "environmental method",
+                "Separation",
+                "nanoplastics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-08-01",
-            "references": [
-                "https://doi.org/10.1186/s43591-022-00051-1"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180771,19 +180765,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s43591-022-00051-1"
+            ],
+            "rights": null,
+            "title": "Legends, Methods and Supplementary data files."
         },
         {
-            "title": "All additional data associated with this publication can be accessed in the supplemental file",
-            "description": "EPA employee associated with this research has retired. Supplemental material for this article contains additional information about the data, but for additional information on the data please contact the first author. \n\nThis dataset is associated with the following publication:\nTedla, G., and K. Rogers. Characterization of 3D printing filaments containing metal additives and their particulate emissions.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 875: 162648, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Kim Rogers",
+                "hasEmail": "mailto:rogers.kim@epa.gov"
+            },
+            "description": "EPA employee associated with this research has retired. Supplemental material for this article contains additional information about the data, but for additional information on the data please contact the first author. \n\nThis dataset is associated with the following publication:\nTedla, G., and K. Rogers. Characterization of 3D printing filaments containing metal additives and their particulate emissions.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 875: 162648, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1016/j.scitotenv.2023.162648",
+                    "title": "https://doi.org/10.1016/j.scitotenv.2023.162648"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528545",
             "keyword": [
@@ -180794,19 +180797,10 @@
                 "3D printing",
                 "Trace metals"
             ],
-            "contactPoint": {
-                "fn": "Kim Rogers",
-                "hasEmail": "mailto:rogers.kim@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1016/j.scitotenv.2023.162648",
-                    "accessURL": "https://doi.org/10.1016/j.scitotenv.2023.162648"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-04-15",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.162648"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180816,54 +180810,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.162648"
+            ],
+            "rights": null,
+            "title": "All additional data associated with this publication can be accessed in the supplemental file"
         },
         {
-            "title": "NARS DATA WOOD STOCK IN NEOTROPICAL STREAMS: QUANTIFYING AND COMPARING IN-STREAM WOOD AMONG BIOMES AND REGIONS",
-            "description": "National Rivers and Streams Assessment (NRSA) physical habitat and ancillary GIS data from NRSA 2008-2009, and 2013-2014. Portions of this dataset are inaccessible because: Data is available in the attached excel file. They can be accessed through the following means: Data is available in the attached excel file. Format: Data is available in the attached excel file. \n\nThis dataset is associated with the following publication:\nSaraiva, S.O., I. Rutherfurd, P. Kaufmann, C.G. Leal, D.R. Macedo, and P.S. Pompeu. WOOD STOCK IN NEOTROPICAL STREAMS: QUANTIFYING AND COMPARING INSTREAM WOOD AMONG BIOMES AND REGIONS.   PLOS ONE. Public Library of Science, San Francisco, CA, USA,  0275464, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528120",
-            "keyword": [
-                "Riparian Forest",
-                "Cerrado streams",
-                "wood assessment",
-                "Amazon streams",
-                "temperate streams",
-                "NARS (USA National Aquatic Resource Surveys)",
-                "physical habitat"
-            ],
             "contactPoint": {
                 "fn": "Philip Kaufmann",
                 "hasEmail": "mailto:kaufmann.phil@epa.gov"
             },
+            "description": "National Rivers and Streams Assessment (NRSA) physical habitat and ancillary GIS data from NRSA 2008-2009, and 2013-2014. Portions of this dataset are inaccessible because: Data is available in the attached excel file. They can be accessed through the following means: Data is available in the attached excel file. Format: Data is available in the attached excel file. \n\nThis dataset is associated with the following publication:\nSaraiva, S.O., I. Rutherfurd, P. Kaufmann, C.G. Leal, D.R. Macedo, and P.S. Pompeu. WOOD STOCK IN NEOTROPICAL STREAMS: QUANTIFYING AND COMPARING INSTREAM WOOD AMONG BIOMES AND REGIONS.   PLOS ONE. Public Library of Science, San Francisco, CA, USA,  0275464, (2022).",
             "distribution": [
                 {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
                 },
                 {
-                    "title": "journal.pone.0275464.s001.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528120/journal.pone.0275464.s001.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "journal.pone.0275464.s001.docx"
                 },
                 {
-                    "title": "journal.pone.0275464.s005.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528120/journal.pone.0275464.s005.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "journal.pone.0275464.s005.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528120",
+            "keyword": [
+                "Riparian Forest",
+                "Cerrado streams",
+                "wood assessment",
+                "Amazon streams",
+                "temperate streams",
+                "NARS (USA National Aquatic Resource Surveys)",
+                "physical habitat"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-04-23",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0275464",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9534444"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -180873,73 +180866,83 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0275464",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9534444"
+            ],
+            "rights": null,
+            "title": "NARS DATA WOOD STOCK IN NEOTROPICAL STREAMS: QUANTIFYING AND COMPARING IN-STREAM WOOD AMONG BIOMES AND REGIONS"
         },
         {
-            "title": "Data for \"Relating Climate Change and Vibriosis in the United States: Projected Health and Economic Impacts for the 21st Century\"",
-            "description": "This paper represents, to our knowledge, the first national-level (United States) estimate of the economic impacts of vibriosis cases as exacerbated by climate change. Vibriosis is an illness contracted through food- and waterborne exposures to various Vibrio species (e.g., non-V. cholerae O1 and O139 serotypes) found in estuarine and marine environments, including within aquatic life, such as shellfish and finfish.\n\nData include all variables included in the regression models (\"cleaned all\"), climate variables (\"cleaned climate vars\"), county in which exposure occurred (\"expcty\"), county that reported diagnosis (\"rptcty\"), and sea surface temperature projections (identified by \"SST\"). Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529453",
-            "keyword": [
-                "vibrio",
-                "vibrio vulnificus",
-                "climate change",
-                "CIRA",
-                "human health",
-                "One Health",
-                "public health",
-                "vibrio parahaemolyticus"
-            ],
             "contactPoint": {
                 "fn": "Caitlin Gould",
                 "hasEmail": "mailto:gould.caitlin@epa.gov"
             },
+            "description": "This paper represents, to our knowledge, the first national-level (United States) estimate of the economic impacts of vibriosis cases as exacerbated by climate change. Vibriosis is an illness contracted through food- and waterborne exposures to various Vibrio species (e.g., non-V. cholerae O1 and O139 serotypes) found in estuarine and marine environments, including within aquatic life, such as shellfish and finfish.\n\nData include all variables included in the regression models (\"cleaned all\"), climate variables (\"cleaned climate vars\"), county in which exposure occurred (\"expcty\"), county that reported diagnosis (\"rptcty\"), and sea surface temperature projections (identified by \"SST\"). Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "repcty.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529453/repcty.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "repcty.txt"
                 },
                 {
-                    "title": "expcty.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529453/expcty.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "expcty.txt"
                 },
                 {
-                    "title": "Data_All combined for regression.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529453/Data_All%20combined%20for%20regression.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Data_All combined for regression.txt"
                 },
                 {
-                    "title": "climvarshist.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529453/climvarshist.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "climvarshist.txt"
                 },
                 {
-                    "title": "ProjectedSST_GCMrawSSTdelta_forHI_ONLY_v1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529453/ProjectedSST_GCMrawSSTdelta_forHI_ONLY_v1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ProjectedSST_GCMrawSSTdelta_forHI_ONLY_v1.xlsx"
                 },
                 {
-                    "title": "ProjectedSST_Coastline_Alaska.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529453/ProjectedSST_Coastline_Alaska.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ProjectedSST_Coastline_Alaska.xlsx"
                 },
                 {
-                    "title": "ProjectedSST_Coastline.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529453/ProjectedSST_Coastline.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ProjectedSST_Coastline.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529453",
+            "keyword": [
+                "vibrio",
+                "vibrio vulnificus",
+                "climate change",
+                "CIRA",
+                "human health",
+                "One Health",
+                "public health",
+                "vibrio parahaemolyticus"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-30",
+            "programCode": [
+                "020:000"
+            ],
+            "publisher": {
+                "name": "U.S. Environmental Protection Agency",
+                "subOrganizationOf": {
+                    "name": "U.S. Government"
+                }
+            },
             "references": [
                 "https://dx.doi.org/10.1289/ehp9999a",
                 "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9422303",
@@ -180948,54 +180951,45 @@
                 "https://pasteur.epa.gov/uploads/10.23719/1529453/documents/MergeAll.txt",
                 "https://pasteur.epa.gov/uploads/10.23719/1529453/documents/Projections_Valuation.txt"
             ],
-            "publisher": {
-                "name": "U.S. Environmental Protection Agency",
-                "subOrganizationOf": {
-                    "name": "U.S. Government"
-                }
-            }
+            "rights": null,
+            "title": "Data for \"Relating Climate Change and Vibriosis in the United States: Projected Health and Economic Impacts for the 21st Century\""
         },
         {
-            "title": "NaKnowBase Interoperability Tools",
-            "description": "This dataset is associated with the manuscript \"Translating nanoEHS data using EPA NaKnowBase and the Resource Description Framework\"\nmortensen h, Williams A, Beach B, Slaughter W, Senn J and Boyes W\nsubmitted 8/3/2023 to F1000:Nanotoxicology.\nThe dataset includes and RDF mapping of EPA NaKnowBase (NKB), the OntoSearcher code used to produce the file NKB RDF, as well as training materials and example files for the user. Portions of this dataset are inaccessible because: this data includes partner data and old code that has been modified since 2021. They can be accessed through the following means:  OntoSearcher_Training_Materials.zip. Format: The file entitled \"OntoSearcher_Training_Materials.zip\" includes updated materials as of 07/11/23. These files include the Ontosearcher tool materials, sample NKB dataset and corresponding training documentation on how to run the tool with the sample dataset, and apply to the users own data. This directory also includes the current RDF mapping of the NKB (NKB_RDF_V3.ttl).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529457",
-            "keyword": [
-                "nanoEHS",
-                "nanomaterials",
-                "ontology",
-                "database"
-            ],
             "contactPoint": {
                 "fn": "Holly Mortensen",
                 "hasEmail": "mailto:mortensen.holly@epa.gov"
             },
+            "description": "This dataset is associated with the manuscript \"Translating nanoEHS data using EPA NaKnowBase and the Resource Description Framework\"\nmortensen h, Williams A, Beach B, Slaughter W, Senn J and Boyes W\nsubmitted 8/3/2023 to F1000:Nanotoxicology.\nThe dataset includes and RDF mapping of EPA NaKnowBase (NKB), the OntoSearcher code used to produce the file NKB RDF, as well as training materials and example files for the user. Portions of this dataset are inaccessible because: this data includes partner data and old code that has been modified since 2021. They can be accessed through the following means:  OntoSearcher_Training_Materials.zip. Format: The file entitled \"OntoSearcher_Training_Materials.zip\" includes updated materials as of 07/11/23. These files include the Ontosearcher tool materials, sample NKB dataset and corresponding training documentation on how to run the tool with the sample dataset, and apply to the users own data. This directory also includes the current RDF mapping of the NKB (NKB_RDF_V3.ttl).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/NaKnowBase/",
-                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NaKnowBase/"
+                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NaKnowBase/",
+                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/NaKnowBase/"
                 },
                 {
-                    "title": "https://doi.org/10.23719/1523156",
-                    "accessURL": "https://doi.org/10.23719/1523156"
+                    "accessURL": "https://doi.org/10.23719/1523156",
+                    "title": "https://doi.org/10.23719/1523156"
                 },
                 {
-                    "title": "OntoSearcher_Training_Materials.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529457/OntoSearcher_Training_Materials.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "OntoSearcher_Training_Materials.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529457",
+            "keyword": [
+                "nanoEHS",
+                "nanomaterials",
+                "ontology",
+                "database"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-08-23",
-            "references": [
-                "https://pasteur.epa.gov/uploads/10.23719/1529457/documents/OntoSearcher_Training_Materials.zip"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181005,36 +180999,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://pasteur.epa.gov/uploads/10.23719/1529457/documents/OntoSearcher_Training_Materials.zip"
+            ],
+            "rights": null,
+            "title": "NaKnowBase Interoperability Tools"
         },
         {
-            "title": "Metadata",
-            "description": "Supplementary, illustrative data to follow along with the publication.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529445",
-            "keyword": [
-                "Spatial Statistics"
-            ],
             "contactPoint": {
                 "fn": "Michael Dumelle",
                 "hasEmail": "mailto:dumelle.michael@epa.gov"
             },
+            "description": "Supplementary, illustrative data to follow along with the publication.",
             "distribution": [
                 {
-                    "title": "https://zenodo.org/record/7636130",
-                    "accessURL": "https://zenodo.org/record/7636130"
+                    "accessURL": "https://zenodo.org/record/7636130",
+                    "title": "https://zenodo.org/record/7636130"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529445",
+            "keyword": [
+                "Spatial Statistics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-07",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -181043,40 +181039,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Metadata"
         },
         {
-            "title": "Captain Jack Data",
-            "description": "This article uses a data set of geochemical tracers collected from the Captain Jack Mill Superfund Site in Colorado. The journal article is the result of a collaboration between U.S. EPA and the USGS. The data and analysis describes water-rock interactions and examines implications about mine water remediation. Portions of this dataset are inaccessible because: The data is publicly accessible on the USGS website. They can be accessed through the following means: Please see the USGS link above for the data. \r\nhttps://www.usgs.gov/data/hydrologic-and-geochemical-data-and-models-supporting-integrated-evaluation-captain-jack. Format: The data is publicly accessible on the USGS website. \n\nThis dataset is associated with the following publication:\nNewman, C., K. Walton-Day, R. Runkel, and R. Wilkin. Mechanisms of water-rock interaction and implications for remediating flooded mine workings elucidated from environmental tracers, stable isotopes, and rare earth elements.   APPLIED GEOCHEMISTRY. Elsevier Science Ltd, New York, NY, USA, 157(October 2023): 105769, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529454",
-            "keyword": [
-                "acid mine drainage",
-                "Rare Earth Elements",
-                "stable isotopes",
-                "Groundwater Contaminant"
-            ],
             "contactPoint": {
                 "fn": "Richard Wilkin",
                 "hasEmail": "mailto:wilkin.rick@epa.gov"
             },
+            "description": "This article uses a data set of geochemical tracers collected from the Captain Jack Mill Superfund Site in Colorado. The journal article is the result of a collaboration between U.S. EPA and the USGS. The data and analysis describes water-rock interactions and examines implications about mine water remediation. Portions of this dataset are inaccessible because: The data is publicly accessible on the USGS website. They can be accessed through the following means: Please see the USGS link above for the data. \r\nhttps://www.usgs.gov/data/hydrologic-and-geochemical-data-and-models-supporting-integrated-evaluation-captain-jack. Format: The data is publicly accessible on the USGS website. \n\nThis dataset is associated with the following publication:\nNewman, C., K. Walton-Day, R. Runkel, and R. Wilkin. Mechanisms of water-rock interaction and implications for remediating flooded mine workings elucidated from environmental tracers, stable isotopes, and rare earth elements.   APPLIED GEOCHEMISTRY. Elsevier Science Ltd, New York, NY, USA, 157(October 2023): 105769, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.usgs.gov/data/hydrologic-and-geochemical-data-and-models-supporting-integrated-evaluation-captain-jack",
-                    "accessURL": "https://www.usgs.gov/data/hydrologic-and-geochemical-data-and-models-supporting-integrated-evaluation-captain-jack"
+                    "accessURL": "https://www.usgs.gov/data/hydrologic-and-geochemical-data-and-models-supporting-integrated-evaluation-captain-jack",
+                    "title": "https://www.usgs.gov/data/hydrologic-and-geochemical-data-and-models-supporting-integrated-evaluation-captain-jack"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529454",
+            "keyword": [
+                "acid mine drainage",
+                "Rare Earth Elements",
+                "stable isotopes",
+                "Groundwater Contaminant"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-31",
-            "references": [
-                "https://doi.org/10.1016/j.apgeochem.2023.105769"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181086,35 +181080,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apgeochem.2023.105769"
+            ],
+            "rights": null,
+            "title": "Captain Jack Data"
         },
         {
-            "title": "Mortality in US Hemodialysis Patients Following Exposure to Wildfire Smoke; Data description",
-            "description": "Data contains daily counts of mortality across continental US. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact Wade.tim@epa.gov. Format: Data is contains PII. \n\nThis dataset is associated with the following publication:\nXi, Y., L.A. Wyatt, A. Kshirsagar, T. Wade, D.B. Richardson, M.A. Brookhart, and A. Rappold. Mortality in US Hemodialysis Patients Following Exposure to Wildfire Smoke.   Journal of the American Society of Nephrology. American Society of Nephrology (ASN), Washington, DC, USA, 31(8): 1824-35, (2020).",
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
+                "fn": "Ana Rappold",
+                "hasEmail": "mailto:rappold.ana@epa.gov"
+            },
+            "description": "Data contains daily counts of mortality across continental US. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact Wade.tim@epa.gov. Format: Data is contains PII. \n\nThis dataset is associated with the following publication:\nXi, Y., L.A. Wyatt, A. Kshirsagar, T. Wade, D.B. Richardson, M.A. Brookhart, and A. Rappold. Mortality in US Hemodialysis Patients Following Exposure to Wildfire Smoke.   Journal of the American Society of Nephrology. American Society of Nephrology (ASN), Washington, DC, USA, 31(8): 1824-35, (2020).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1503883",
             "keyword": [
                 "wildfire",
                 "kidney disease",
                 "mortality"
             ],
-            "contactPoint": {
-                "fn": "Ana Rappold",
-                "hasEmail": "mailto:rappold.ana@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-05-22",
-            "references": [
-                "https://doi.org/10.1681/asn.2019101066",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7460895"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181124,34 +181117,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1681/asn.2019101066",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7460895"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Mortality in US Hemodialysis Patients Following Exposure to Wildfire Smoke; Data description"
         },
         {
-            "title": "Mediation Analysis Annual Mortality",
-            "description": "Annual mortality rates for US counties, air pollution concentrations. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Please contact corresponding author. Format: Data is saved in Ascii and netcdf format. \n\nThis dataset is associated with the following publication:\nPeterson, G., C. Hogrefe, L. Neas, A. Corrigan, R. Mathur, and A. Rappold. Impacts of Reductions in Emissions from Major Source Sectors on Fine Particulate Matter-Related Cardiovascular Mortality.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 128(1): 17005, (2020).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1502463",
-            "keyword": [
-                "air quality",
-                "cardiovascular mortality"
-            ],
             "contactPoint": {
                 "fn": "Ana Rappold",
                 "hasEmail": "mailto:rappold.ana@epa.gov"
             },
+            "description": "Annual mortality rates for US counties, air pollution concentrations. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Please contact corresponding author. Format: Data is saved in Ascii and netcdf format. \n\nThis dataset is associated with the following publication:\nPeterson, G., C. Hogrefe, L. Neas, A. Corrigan, R. Mathur, and A. Rappold. Impacts of Reductions in Emissions from Major Source Sectors on Fine Particulate Matter-Related Cardiovascular Mortality.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 128(1): 17005, (2020).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1502463",
+            "keyword": [
+                "air quality",
+                "cardiovascular mortality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-02",
-            "references": [
-                "https://doi.org/10.1289/ehp5692",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7015538"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181161,41 +181154,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp5692",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7015538"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Mediation Analysis Annual Mortality"
         },
         {
-            "title": "Headwater Invertebrate Stream Study invertebrate datasets",
-            "description": "Aquatic and terrestrial invertebrate density and biomass datasets at genus and family taxonomic levels. \n\nThis dataset is associated with the following publication:\nFritz, K., R. Kashuba, G. Pond, J. Christensen, L. Alexander, B.J. Washington, B. Johnson, D. Walters, W. Thoeny, and P. Weaver. Identifying invertebrate indicators for streamflow duration assessments in forested headwater streams.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  42(3): 247-267, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527802",
-            "keyword": [
-                "flow classification",
-                "perennial",
-                "intermittent",
-                "indicators"
-            ],
             "contactPoint": {
                 "fn": "Ken Fritz",
                 "hasEmail": "mailto:fritz.ken@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1527802/documents/Data%20Dictionary%20for%20Headwater%20Invertebrate%20Stream%20Study%20invertebrate%20datasets.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Aquatic and terrestrial invertebrate density and biomass datasets at genus and family taxonomic levels. \n\nThis dataset is associated with the following publication:\nFritz, K., R. Kashuba, G. Pond, J. Christensen, L. Alexander, B.J. Washington, B. Johnson, D. Walters, W. Thoeny, and P. Weaver. Identifying invertebrate indicators for streamflow duration assessments in forested headwater streams.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  42(3): 247-267, (2023).",
             "distribution": [
                 {
-                    "title": "Headwater Invertebrate Stream Study invertebrate datasets.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527802/Headwater%20Invertebrate%20Stream%20Study%20invertebrate%20datasets.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Headwater Invertebrate Stream Study invertebrate datasets.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527802",
+            "keyword": [
+                "flow classification",
+                "perennial",
+                "intermittent",
+                "indicators"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-25",
-            "references": [
-                "https://doi.org/10.1086/726081"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181206,20 +181202,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1527802/documents/Data%20Dictionary%20for%20Headwater%20Invertebrate%20Stream%20Study%20invertebrate%20datasets.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1086/726081"
+            ],
+            "rights": null,
+            "title": "Headwater Invertebrate Stream Study invertebrate datasets"
         },
         {
-            "title": "ESF2012_PairedSaltRecipesStudy_AllData_SciInv",
-            "description": "Water chemistry, periphyton measures, periphytic algae taxonomy and cell counts, benthic macroinvertebrate taxaonomy and counts, invertebrate drift, insect emergence, and single-species toxicity test data. \n\nThis dataset is associated with the following publication:\nNietch, C., N. Smucker, L. Gains-Germain, C. Peck, S. Guglielmi, S. Decelles, J. Lazorchak, B. Johnson, and P. Weaver. Using Single-Species and Whole Community Stream Mesocosm Exposures for Identifying Major Ion Effects in Doses Mimicking Resource Extraction Wastewaters.   WATER. MDPI, Basel,  SWITZERLAND, 15(2): 249, (2023).",
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
+            "description": "Water chemistry, periphyton measures, periphytic algae taxonomy and cell counts, benthic macroinvertebrate taxaonomy and counts, invertebrate drift, insect emergence, and single-species toxicity test data. \n\nThis dataset is associated with the following publication:\nNietch, C., N. Smucker, L. Gains-Germain, C. Peck, S. Guglielmi, S. Decelles, J. Lazorchak, B. Johnson, and P. Weaver. Using Single-Species and Whole Community Stream Mesocosm Exposures for Identifying Major Ion Effects in Doses Mimicking Resource Extraction Wastewaters.   WATER. MDPI, Basel,  SWITZERLAND, 15(2): 249, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528518/ESF2012_PairedSaltRecipesStudy_AllData_SciInv.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ESF2012_PairedSaltRecipesStudy_AllData_SciInv.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528518",
             "keyword": [
@@ -181236,20 +181240,10 @@
                 "Stream Mesocosm",
                 "Whole Community Data"
             ],
-            "contactPoint": {
-                "fn": "Christopher Nietch",
-                "hasEmail": "mailto:nietch.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ESF2012_PairedSaltRecipesStudy_AllData_SciInv.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528518/ESF2012_PairedSaltRecipesStudy_AllData_SciInv.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-01",
-            "references": [
-                "https://doi.org/10.3390/w15020249"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181259,19 +181253,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/w15020249"
+            ],
+            "rights": null,
+            "title": "ESF2012_PairedSaltRecipesStudy_AllData_SciInv"
         },
         {
-            "title": "Lightning NOx Emissions in CMAQ Data",
-            "description": "Meta Data of the dataset for \u201cAssessing the Impact of Lightning NOx Emissions in CMAQ Using Lightning Flash Data from WWLLN over the Contiguous United States\u201d\n\nFigure 2: ThreeYear_NLDN2WWLLN_byNOAAcr_Region_anal.xlsx. The names of the variable are self-explanatory and the original figure is included.\nFigure 3: NLDN_flash_Monthly_mean_2016_07.ncf.gz,  WWLLN_flash_Monthly_mean_2016_07.ncf.gz, WWLLNs_flash_Monthly_mean_2016_07.ncf.gz. These netcdf files contain the monthly mean values of gridded lightning flash rate for all the cases and the figure can be created using any netcdf visualization tool (such as VERDI) or statistical package (such as R).\n\nFigures 4,5,6: CMAQ_*_.rds.gz files. These files contain the paired observation-model O3 concentrations from all the model cases for hourly, daily max-8hr, and other statistics. The rds datasets can be read into R as data frame to make these figures.\n\nFigure 7 & 8: CCTM_CONC*.nc.gz. The vertical profiles (CONC) contain model data to make Figures 7 and 8. While the observation data are available publicly.\n\nFigure 9: NADP_v532_intel18_0_2016_CONUS_*.csv. \nFigure 10: avg*_DEP_concentrations*.nc.gz. These files contain the monthly mean vet deposition of NO3.\nFigure 11: NADP_v532_intel18_0_2016_CONUS_*.csv. \nFigure 12: *DDEP_TNO3_*.nc.gz. These files contain hourly dry deposition of TNO3 over the CONUS domain\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Daiwen Kang",
+                "hasEmail": "mailto:kang.daiwen@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1527715/documents/Description%20of%20the%20dataset.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Meta Data of the dataset for \u201cAssessing the Impact of Lightning NOx Emissions in CMAQ Using Lightning Flash Data from WWLLN over the Contiguous United States\u201d\n\nFigure 2: ThreeYear_NLDN2WWLLN_byNOAAcr_Region_anal.xlsx. The names of the variable are self-explanatory and the original figure is included.\nFigure 3: NLDN_flash_Monthly_mean_2016_07.ncf.gz,  WWLLN_flash_Monthly_mean_2016_07.ncf.gz, WWLLNs_flash_Monthly_mean_2016_07.ncf.gz. These netcdf files contain the monthly mean values of gridded lightning flash rate for all the cases and the figure can be created using any netcdf visualization tool (such as VERDI) or statistical package (such as R).\n\nFigures 4,5,6: CMAQ_*_.rds.gz files. These files contain the paired observation-model O3 concentrations from all the model cases for hourly, daily max-8hr, and other statistics. The rds datasets can be read into R as data frame to make these figures.\n\nFigure 7 & 8: CCTM_CONC*.nc.gz. The vertical profiles (CONC) contain model data to make Figures 7 and 8. While the observation data are available publicly.\n\nFigure 9: NADP_v532_intel18_0_2016_CONUS_*.csv. \nFigure 10: avg*_DEP_concentrations*.nc.gz. These files contain the monthly mean vet deposition of NO3.\nFigure 11: NADP_v532_intel18_0_2016_CONUS_*.csv. \nFigure 12: *DDEP_TNO3_*.nc.gz. These files contain hourly dry deposition of TNO3 over the CONUS domain\n",
+            "distribution": [
+                {
+                    "accessURL": "https://www.google.com/",
+                    "title": "https://www.google.com/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1527715",
             "keyword": [
@@ -181281,17 +181286,20 @@
                 "Ozone",
                 "NOx"
             ],
-            "contactPoint": {
-                "fn": "Daiwen Kang",
-                "hasEmail": "mailto:kang.daiwen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.google.com/",
-                    "accessURL": "https://www.google.com/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-06",
+            "programCode": [
+                "020:000"
+            ],
+            "publisher": {
+                "name": "U.S. EPA Office of Research and Development (ORD)",
+                "subOrganizationOf": {
+                    "name": "U.S. Environmental Protection Agency",
+                    "subOrganizationOf": {
+                        "name": "U.S. Government"
+                    }
+                }
+            },
             "references": [
                 "https://pasteur.epa.gov/uploads/10.23719/1527715/documents/avg_NLDN_DEP_concentrations_v532_intel18.0_2016_CONUS_201607.nc.zip",
                 "https://pasteur.epa.gov/uploads/10.23719/1527715/documents/avg_WWLLLNs_DEP_concentrations_v532_intel18.0_2016_CONUS_201607.nc.zip",
@@ -181326,152 +181334,137 @@
                 "https://pasteur.epa.gov/uploads/10.23719/1527715/documents/WWLLNs_DDEP_TNO3_v532_intel18.0_2016_CONUS_201607.nc.zip",
                 "https://pasteur.epa.gov/uploads/10.23719/1527715/documents/WWLLN_DDEP_TNO3_v532_intel18.0_2016_CONUS_201607.nc.zip"
             ],
-            "publisher": {
-                "name": "U.S. EPA Office of Research and Development (ORD)",
-                "subOrganizationOf": {
-                    "name": "U.S. Environmental Protection Agency",
-                    "subOrganizationOf": {
-                        "name": "U.S. Government"
-                    }
-                }
-            },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1527715/documents/Description%20of%20the%20dataset.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "rights": null,
+            "title": "Lightning NOx Emissions in CMAQ Data"
         },
         {
-            "title": "Datasets for manuscript: Multi-scale techno-economic assessment of nitrogen recovery systems for livestock operations",
-            "description": "The datasets contain data required to determine the recovery efficiency and nitrogen losses of each of the six studied technologies and nitrogen recovery cost, as well as an environmental cost-benefit analysis to compare the nitrogen recovery cost versus the economic losses derived from its uncontrolled release into the environment. Also, the Tower flooding capacity correlation considering the packing pressure drop (Figure 3), the relative flows of inorganic nitrogen in the studied processes (Figure 4), the processing and nitrogen recovery costs of the assessed nitrogen recovery technologies for different livestock facility sizes, including the cost of pretreatment and AD stages (Figure 5), the processing and nitrogen recovery costs of the assessed nitrogen recovery technologies for different livestock facility sizes, excluding the cost of anaerobic digestion stage (Figure 6), and the other datasets to obtain the supplemental information figures. \n\nThis dataset is associated with the following publication:\nMartin-Hernandez, E., C. Montero-Rueda, G.J. Ruiz-Mercado, C. Vaneeckhaute, and M. Martin. Multi-scale techno-economic assessment of nitrogen recovery systems for livestock operations.   Sustainable Production and Consumption. Elsevier B.V., Amsterdam,  NETHERLANDS, 41: 49-63, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528489",
-            "keyword": [
-                "Nitrogen and Co-pollutants",
-                "Nitrogen Recovery",
-                "Livestock Industry",
-                "Techno-economic assessment"
-            ],
             "contactPoint": {
                 "fn": "Gerardo Ruiz-Mercado",
                 "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
             },
+            "description": "The datasets contain data required to determine the recovery efficiency and nitrogen losses of each of the six studied technologies and nitrogen recovery cost, as well as an environmental cost-benefit analysis to compare the nitrogen recovery cost versus the economic losses derived from its uncontrolled release into the environment. Also, the Tower flooding capacity correlation considering the packing pressure drop (Figure 3), the relative flows of inorganic nitrogen in the studied processes (Figure 4), the processing and nitrogen recovery costs of the assessed nitrogen recovery technologies for different livestock facility sizes, including the cost of pretreatment and AD stages (Figure 5), the processing and nitrogen recovery costs of the assessed nitrogen recovery technologies for different livestock facility sizes, excluding the cost of anaerobic digestion stage (Figure 6), and the other datasets to obtain the supplemental information figures. \n\nThis dataset is associated with the following publication:\nMartin-Hernandez, E., C. Montero-Rueda, G.J. Ruiz-Mercado, C. Vaneeckhaute, and M. Martin. Multi-scale techno-economic assessment of nitrogen recovery systems for livestock operations.   Sustainable Production and Consumption. Elsevier B.V., Amsterdam,  NETHERLANDS, 41: 49-63, (2023).",
             "distribution": [
                 {
-                    "title": "Fig 2S ScrewPressCost.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%202S%20ScrewPressCost.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 2S ScrewPressCost.csv"
                 },
                 {
-                    "title": "Fig1S_a AD_size_cost.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig1S_a%20AD_size_cost.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig1S_a AD_size_cost.csv"
                 },
                 {
-                    "title": "Fig 1S_b OM_Unit_cost_ratio.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%201S_b%20OM_Unit_cost_ratio.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 1S_b OM_Unit_cost_ratio.csv"
                 },
                 {
-                    "title": "Figs_5_6.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Figs_5_6.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Figs_5_6.csv"
                 },
                 {
-                    "title": "Figs 4S_5S.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Figs%204S_5S.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Figs 4S_5S.csv"
                 },
                 {
-                    "title": "Fig 4 ScrubbingAmmoniaEvaporation_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20ScrubbingAmmoniaEvaporation_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 ScrubbingAmmoniaEvaporation_balances.csv"
                 },
                 {
-                    "title": "Fig 4 ScrubbingAirStrippingPacked_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20ScrubbingAirStrippingPacked_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 ScrubbingAirStrippingPacked_balances.csv"
                 },
                 {
-                    "title": "Fig 4 Scrubbing_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20Scrubbing_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 Scrubbing_balances.csv"
                 },
                 {
-                    "title": "Fig 4 ScrewPress_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20ScrewPress_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 ScrewPress_balances.csv"
                 },
                 {
-                    "title": "Fig 4 MULTIFORM_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20MULTIFORM_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 MULTIFORM_balances.csv"
                 },
                 {
-                    "title": "Fig 4 mixer_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20mixer_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 mixer_balances.csv"
                 },
                 {
-                    "title": "Fig 4 Membrane_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20Membrane_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 Membrane_balances.csv"
                 },
                 {
-                    "title": "Fig 4 MAPHEX_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20MAPHEX_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 MAPHEX_balances.csv"
                 },
                 {
-                    "title": "Fig 4 CHP_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20CHP_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 CHP_balances.csv"
                 },
                 {
-                    "title": "Fig 4 Centrifuge_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20Centrifuge_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 Centrifuge_balances.csv"
                 },
                 {
-                    "title": "Fig 4 BiogasConditioning_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20BiogasConditioning_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 BiogasConditioning_balances.csv"
                 },
                 {
-                    "title": "Fig 4 AmmoniaEvaporation_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20AmmoniaEvaporation_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 AmmoniaEvaporation_balances.csv"
                 },
                 {
-                    "title": "Fig 4 AirStrippingPacked_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20AirStrippingPacked_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 AirStrippingPacked_balances.csv"
                 },
                 {
-                    "title": "Fig 4 AD_balances.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%204%20AD_balances.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 4 AD_balances.csv"
                 },
                 {
-                    "title": "Fig 3S.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig%203S.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig 3S.csv"
                 },
                 {
-                    "title": "Fig3.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528489/Fig3.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Fig3.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528489",
+            "keyword": [
+                "Nitrogen and Co-pollutants",
+                "Nitrogen Recovery",
+                "Livestock Industry",
+                "Techno-economic assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-02-01",
-            "references": [
-                "https://doi.org/10.1016/j.spc.2023.07.028",
-                "https://pasteur.epa.gov/uploads/10.23719/1528489/documents/Sup%20Info%20Manuscript%20Nitrogen_Revision%20for%20RAPID%2002-01-23.pdf"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181481,19 +181474,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.spc.2023.07.028",
+                "https://pasteur.epa.gov/uploads/10.23719/1528489/documents/Sup%20Info%20Manuscript%20Nitrogen_Revision%20for%20RAPID%2002-01-23.pdf"
+            ],
+            "rights": null,
+            "title": "Datasets for manuscript: Multi-scale techno-economic assessment of nitrogen recovery systems for livestock operations"
         },
         {
-            "title": "Forshay et al. 2022 Biogeochemistry https://doi.org/10.23719/1520759",
-            "description": "Soil properties, processing rates, and water chemistry data. \n\nThis dataset is associated with the following publication:\nForshay, K., J. Weitzman, J. Wilhelm, J. Hartranft, D. Merritts, M. Rahnis, R. Walter, and P. Mayer. Unearthing a stream-wetland floodplain system: increased denitrification and nitrate retention at a legacy sediment removal restoration site, Big Spring Run, PA, USA.   BIOGEOCHEMISTRY. Springer, New York, NY, USA, (161): 171-191, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Kenneth Forshay",
+                "hasEmail": "mailto:forshay.ken@epa.gov"
+            },
+            "description": "Soil properties, processing rates, and water chemistry data. \n\nThis dataset is associated with the following publication:\nForshay, K., J. Weitzman, J. Wilhelm, J. Hartranft, D. Merritts, M. Rahnis, R. Walter, and P. Mayer. Unearthing a stream-wetland floodplain system: increased denitrification and nitrate retention at a legacy sediment removal restoration site, Big Spring Run, PA, USA.   BIOGEOCHEMISTRY. Springer, New York, NY, USA, (161): 171-191, (2022).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529460/ScienceHubDataSetBSRBiogeochemistry.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHubDataSetBSRBiogeochemistry.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529460",
             "keyword": [
@@ -181508,20 +181512,10 @@
                 "restoration",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Kenneth Forshay",
-                "hasEmail": "mailto:forshay.ken@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ScienceHubDataSetBSRBiogeochemistry.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529460/ScienceHubDataSetBSRBiogeochemistry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-05",
-            "references": [
-                "https://doi.org/10.1007/s10533-022-00975-z"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181531,42 +181525,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10533-022-00975-z"
+            ],
+            "rights": null,
+            "title": "Forshay et al. 2022 Biogeochemistry https://doi.org/10.23719/1520759"
         },
         {
-            "title": "Evaluating adaptive stress response gene signatures using transcriptomics- Data for Figures 1-4",
-            "description": "The construction of SRP consensus signatures sets was completed in three steps. First, we constructed consensus signatures by merging and pruning relevant gene sets from the MSigDB v7.1. Second, we developed an independent gene expression validation set by identifying reference perturbagens from the literature and curating their transcriptomic profiles from publicly available sources. Third, we used gene set enrichment analysis (GSEA) to score matches between signatures and transcriptomic profiles. Lastly, we evaluated the performance of GSEA scores as classifiers of SRP activity within reference perturbagen transcriptomic profiles using ROC AUC analysis. \n\nThis dataset is associated with the following publication:\nChambers, B., and I. Shah. Evaluating adaptive stress response gene signatures using transcriptomics.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 20: 100179, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1523149",
-            "keyword": [
-                "stress response pathways",
-                "transcriptomics",
-                "gene signatures",
-                "receiver operating characteristic",
-                "computational toxicology"
-            ],
             "contactPoint": {
                 "fn": "Imran Shah",
                 "hasEmail": "mailto:shah.imran@epa.gov"
             },
+            "description": "The construction of SRP consensus signatures sets was completed in three steps. First, we constructed consensus signatures by merging and pruning relevant gene sets from the MSigDB v7.1. Second, we developed an independent gene expression validation set by identifying reference perturbagens from the literature and curating their transcriptomic profiles from publicly available sources. Third, we used gene set enrichment analysis (GSEA) to score matches between signatures and transcriptomic profiles. Lastly, we evaluated the performance of GSEA scores as classifiers of SRP activity within reference perturbagen transcriptomic profiles using ROC AUC analysis. \n\nThis dataset is associated with the following publication:\nChambers, B., and I. Shah. Evaluating adaptive stress response gene signatures using transcriptomics.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 20: 100179, (2021).",
             "distribution": [
                 {
-                    "title": "supplemental-materials-tables-v4.21.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523149/supplemental-materials-tables-v4.21.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "supplemental-materials-tables-v4.21.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1523149",
+            "keyword": [
+                "stress response pathways",
+                "transcriptomics",
+                "gene signatures",
+                "receiver operating characteristic",
+                "computational toxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-09-22",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2021.100179"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181576,39 +181570,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2021.100179"
+            ],
+            "rights": null,
+            "title": "Evaluating adaptive stress response gene signatures using transcriptomics- Data for Figures 1-4"
         },
         {
-            "title": "Steubenville, OH phosphorus in event wet-only precipitation data from October 15, 2002 - March 7, 2008.",
-            "description": "Steubenville, OH Phosphorous in event wet-only precipitation data from October 15, 2002 - March 7, 2008. \n\nThis dataset is associated with the following publication:\nLynam, M., L. Oriol, T. Mann, J.T. Dvonch, J. Barres, L. Gratz, E. White, M. Landis, N. Mahowald, C. Xi, and A. Steiner. Atmospheric Dry and Wet Deposition of Total Phosphorus to the Great Lakes.   Atmospheric Environment: X. Elsevier B.V., Amsterdam,  NETHERLANDS, 313: 0, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528981",
-            "keyword": [
-                "Great Lakes",
-                "phosphorus",
-                "wet deposition"
-            ],
             "contactPoint": {
                 "fn": "Matthew Landis",
                 "hasEmail": "mailto:landis.matthew@epa.gov"
             },
+            "description": "Steubenville, OH Phosphorous in event wet-only precipitation data from October 15, 2002 - March 7, 2008. \n\nThis dataset is associated with the following publication:\nLynam, M., L. Oriol, T. Mann, J.T. Dvonch, J. Barres, L. Gratz, E. White, M. Landis, N. Mahowald, C. Xi, and A. Steiner. Atmospheric Dry and Wet Deposition of Total Phosphorus to the Great Lakes.   Atmospheric Environment: X. Elsevier B.V., Amsterdam,  NETHERLANDS, 313: 0, (2023).",
             "distribution": [
                 {
-                    "title": "Steubenville_Phosphorus_Data_2023_05_10.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528981/Steubenville_Phosphorus_Data_2023_05_10.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Steubenville_Phosphorus_Data_2023_05_10.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528981",
+            "keyword": [
+                "Great Lakes",
+                "phosphorus",
+                "wet deposition"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-10",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -181617,41 +181613,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Steubenville, OH phosphorus in event wet-only precipitation data from October 15, 2002 - March 7, 2008."
         },
         {
-            "title": "Data set associated with benzyl alcohol paper 2022",
-            "description": "Benzyl alcohol paper data set. \n\nThis dataset is associated with the following publication:\nJaoui, M., K. Docherty, M. Lewandowski, and T. Kleindienst. Yields and molecular composition of gas-phase and secondary organic aerosol from the photooxidation of the volatile consumer product benzyl alcohol: formation of highly oxygenated and hydroxy nitro-aromatic compounds.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 23(8): 4637\u20134661, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527893",
-            "keyword": [
-                "SOA",
-                "yield",
-                "consumer products",
-                "Nitroaromatic compounds"
-            ],
             "contactPoint": {
                 "fn": "Mohammed Jaoui",
                 "hasEmail": "mailto:jaoui.mohammed@epa.gov"
             },
+            "description": "Benzyl alcohol paper data set. \n\nThis dataset is associated with the following publication:\nJaoui, M., K. Docherty, M. Lewandowski, and T. Kleindienst. Yields and molecular composition of gas-phase and secondary organic aerosol from the photooxidation of the volatile consumer product benzyl alcohol: formation of highly oxygenated and hydroxy nitro-aromatic compounds.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 23(8): 4637\u20134661, (2023).",
             "distribution": [
                 {
-                    "title": "BnOH_paper_STICS_8-23-22_MJaoui.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527893/BnOH_paper_STICS_8-23-22_MJaoui.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "BnOH_paper_STICS_8-23-22_MJaoui.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527893",
+            "keyword": [
+                "SOA",
+                "yield",
+                "consumer products",
+                "Nitroaromatic compounds"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-24",
-            "references": [
-                "https://doi.org/10.5194/acp-23-4637-2023"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181661,41 +181655,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-23-4637-2023"
+            ],
+            "rights": null,
+            "title": "Data set associated with benzyl alcohol paper 2022"
         },
         {
-            "title": "Data associated with Dual Site Study Analytic Element Domain Boundary Conditions for Site-Scale Groundwater Flow Modeling Los Angeles Basin",
-            "description": "The zip file contains the model files supporting the paper:\n\nKraemer, S.R. 2023. Analytic element domain boundary conditions for site-scale groundwater flow modeling Los Angeles basin, Groundwater, doi: 10.1111/gwat.13322. \n\nThis dataset is associated with the following publication:\nKraemer, S. Analytic Element Domain Boundary Conditions for Site-Scale Groundwater Flow Modeling Los Angeles Basin.   Groundwater. Wiley-Blackwell, Hoboken, NJ, USA, 61(5): 743-753, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528968",
-            "keyword": [
-                "groundwater modeling",
-                "boundary conditions",
-                "hydraulic containment",
-                "analytic element method"
-            ],
             "contactPoint": {
                 "fn": "Stephen Kraemer",
                 "hasEmail": "mailto:kraemer.stephen@epa.gov"
             },
+            "description": "The zip file contains the model files supporting the paper:\n\nKraemer, S.R. 2023. Analytic element domain boundary conditions for site-scale groundwater flow modeling Los Angeles basin, Groundwater, doi: 10.1111/gwat.13322. \n\nThis dataset is associated with the following publication:\nKraemer, S. Analytic Element Domain Boundary Conditions for Site-Scale Groundwater Flow Modeling Los Angeles Basin.   Groundwater. Wiley-Blackwell, Hoboken, NJ, USA, 61(5): 743-753, (2023).",
             "distribution": [
                 {
-                    "title": "DualSiteStudy_supporting_model_files.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528968/DualSiteStudy_supporting_model_files.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "DualSiteStudy_supporting_model_files.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528968",
+            "keyword": [
+                "groundwater modeling",
+                "boundary conditions",
+                "hydraulic containment",
+                "analytic element method"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-01",
-            "references": [
-                "https://doi.org/10.1111/gwat.13322"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181705,53 +181699,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/gwat.13322"
+            ],
+            "rights": null,
+            "title": "Data associated with Dual Site Study Analytic Element Domain Boundary Conditions for Site-Scale Groundwater Flow Modeling Los Angeles Basin"
         },
         {
-            "title": "Influence of Methylene Blue or Dimethyl Sulfoxide on Larval Zebrafish Development and Behavior",
-            "description": "Data for Joan M. Hedge, et al., Influence of Methylene Blue or Dimethyl Sulfoxide on Larval Zebrafish Development and Behavior.\nZebrafish.   http://doi.org/10.1089/zeb.2023.0017. \n\nThis dataset is associated with the following publication:\nHedge, J., D. Hunter, E. Sanders, K. Jarema, J. Olin, K. Britton, M. Lowery, B. Knapp, S. Padilla, and B. Hill. Influence of Methylene Blue or Dimethyl Sulfoxide on Larval Zebrafish Development and Behavior.   Zebrafish. Mary Ann Liebert, Inc., New Rochelle, NY, USA, 20(4): 132-145, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529355",
-            "keyword": [
-                "zebrafish",
-                "behavior",
-                "larvae",
-                "methylene blue",
-                "DMSO",
-                "Developmental Toxicity"
-            ],
             "contactPoint": {
                 "fn": "Joan Hedge",
                 "hasEmail": "mailto:hedge.joan@epa.gov"
             },
+            "description": "Data for Joan M. Hedge, et al., Influence of Methylene Blue or Dimethyl Sulfoxide on Larval Zebrafish Development and Behavior.\nZebrafish.   http://doi.org/10.1089/zeb.2023.0017. \n\nThis dataset is associated with the following publication:\nHedge, J., D. Hunter, E. Sanders, K. Jarema, J. Olin, K. Britton, M. Lowery, B. Knapp, S. Padilla, and B. Hill. Influence of Methylene Blue or Dimethyl Sulfoxide on Larval Zebrafish Development and Behavior.   Zebrafish. Mary Ann Liebert, Inc., New Rochelle, NY, USA, 20(4): 132-145, (2023).",
             "distribution": [
                 {
-                    "title": "HedgeHillSupplementalData3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529355/HedgeHillSupplementalData3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HedgeHillSupplementalData3.xlsx"
                 },
                 {
-                    "title": "HedgeHillSupplementalData2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529355/HedgeHillSupplementalData2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HedgeHillSupplementalData2.xlsx"
                 },
                 {
-                    "title": "HedgeHillSupplementalData1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529355/HedgeHillSupplementalData1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HedgeHillSupplementalData1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529355",
+            "keyword": [
+                "zebrafish",
+                "behavior",
+                "larvae",
+                "methylene blue",
+                "DMSO",
+                "Developmental Toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-11",
-            "references": [
-                "https://doi.org/10.1089/zeb.2023.0017"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181761,41 +181755,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1089/zeb.2023.0017"
+            ],
+            "rights": null,
+            "title": "Influence of Methylene Blue or Dimethyl Sulfoxide on Larval Zebrafish Development and Behavior"
         },
         {
-            "title": "Effect of membrane performance variability with temperature and feed composition on pervaporation and vapor permeation system design for solvent drying",
-            "description": "Dataset provides all of the values presented in figures in the associated manuscript \"Effect of membrane performance variability with temperature and feed composition on pervaporation and vapor permeation system design for solvent drying\". \n\nThis dataset is associated with the following publication:\nVane, L. Effect of membrane performance variability with temperature and feed composition on pervaporation and vapor permeation system design for solvent drying.   Journal of Chemical Technology and Biotechnology. John Wiley and Sons, LTD,   UK, 97(10): 2706-2719, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526074",
-            "keyword": [
-                "Membrane Technology",
-                "materials management",
-                "solvent re",
-                "solvent dehydration"
-            ],
             "contactPoint": {
                 "fn": "Leland Vane",
                 "hasEmail": "mailto:vane.leland@epa.gov"
             },
+            "description": "Dataset provides all of the values presented in figures in the associated manuscript \"Effect of membrane performance variability with temperature and feed composition on pervaporation and vapor permeation system design for solvent drying\". \n\nThis dataset is associated with the following publication:\nVane, L. Effect of membrane performance variability with temperature and feed composition on pervaporation and vapor permeation system design for solvent drying.   Journal of Chemical Technology and Biotechnology. John Wiley and Sons, LTD,   UK, 97(10): 2706-2719, (2022).",
             "distribution": [
                 {
-                    "title": "Calculated Values for Variable Permeability Graphs.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526074/Calculated%20Values%20for%20Variable%20Permeability%20Graphs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Calculated Values for Variable Permeability Graphs.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526074",
+            "keyword": [
+                "Membrane Technology",
+                "materials management",
+                "solvent re",
+                "solvent dehydration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-04-04",
-            "references": [
-                "https://doi.org/10.1002/jctb.7161"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181805,41 +181799,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/jctb.7161"
+            ],
+            "rights": null,
+            "title": "Effect of membrane performance variability with temperature and feed composition on pervaporation and vapor permeation system design for solvent drying"
         },
         {
-            "title": "PFAS flushing from home plumbing and impacts of stagnation",
-            "description": "Per- and polyfluoroalkyl substances (PFAS) from aqueous film forming foam (AFFF) can be accidentally backflushed into drinking water systems during firefighting operations or at industrial facilities.  If this contaminated water enters household plumbing systems, homeowners may need to decontaminate their plumbing.  This study examines the persistence of PFAS from AFFF on home plumbing, along with the effects of flushing and stagnation.  Two sources of AFFF were investigated, representing older formulations (that contain longer chain PFAS) and newer formulations (that contain shorter chain PFAS). Experiments were conducted in copper, polyvinyl chloride (PVC), and cross-linked polyethylene (PEX) pipes with flushing after contamination followed by intermittent flow and periods of stagnation meant to mimic typical household use.  Flushing immediately reduced the PFAS concentration in water leaving the pipe by 99.95 to 99.99%. However, PFAS concentration increased after periods of stagnation, corresponding to slow release of adhered PFAS. \n\nThis dataset is associated with the following publication:\nSzabo, J., S. Witt, N. Sojda, D. Schupp, and M. Magnuson. Flushing Home Plumbing Pipes Contaminated with Aqueous Film-Forming Foam Containing Per- and Polyfluoroalkyl Substances.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(9): 05023007-(1-8), (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526359",
-            "keyword": [
-                "Premise Plumbing",
-                "PFAS",
-                "drinking water",
-                "Decontamination"
-            ],
             "contactPoint": {
                 "fn": "Jeffrey Szabo",
                 "hasEmail": "mailto:szabo.jeff@epa.gov"
             },
+            "description": "Per- and polyfluoroalkyl substances (PFAS) from aqueous film forming foam (AFFF) can be accidentally backflushed into drinking water systems during firefighting operations or at industrial facilities.  If this contaminated water enters household plumbing systems, homeowners may need to decontaminate their plumbing.  This study examines the persistence of PFAS from AFFF on home plumbing, along with the effects of flushing and stagnation.  Two sources of AFFF were investigated, representing older formulations (that contain longer chain PFAS) and newer formulations (that contain shorter chain PFAS). Experiments were conducted in copper, polyvinyl chloride (PVC), and cross-linked polyethylene (PEX) pipes with flushing after contamination followed by intermittent flow and periods of stagnation meant to mimic typical household use.  Flushing immediately reduced the PFAS concentration in water leaving the pipe by 99.95 to 99.99%. However, PFAS concentration increased after periods of stagnation, corresponding to slow release of adhered PFAS. \n\nThis dataset is associated with the following publication:\nSzabo, J., S. Witt, N. Sojda, D. Schupp, and M. Magnuson. Flushing Home Plumbing Pipes Contaminated with Aqueous Film-Forming Foam Containing Per- and Polyfluoroalkyl Substances.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(9): 05023007-(1-8), (2023).",
             "distribution": [
                 {
-                    "title": "PFAS Flushing Data SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526359/PFAS%20Flushing%20Data%20SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PFAS Flushing Data SciHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526359",
+            "keyword": [
+                "Premise Plumbing",
+                "PFAS",
+                "drinking water",
+                "Decontamination"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-04-18",
-            "references": [
-                "https://doi.org/10.1061/joeedu.eeeng-7315"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181849,19 +181843,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/joeedu.eeeng-7315"
+            ],
+            "rights": null,
+            "title": "PFAS flushing from home plumbing and impacts of stagnation"
         },
         {
-            "title": "Assessment of Ohio Landfill Moisture Contents",
-            "description": "Data from the manuscript regarding the analysis of leachate volumes at Ohio landfills to assess sources of moisture. Data includes moisture contents, precipitation, evaportranspiration, and leachate volumes or masses. \n\nThis dataset is associated with the following publication:\nKrause, M., W. Eades, N. Detwiler, D. Marro, A. Schwarber, and T. Tolaymat. Assessing moisture contributions from precipitation, waste, and leachate for active municipal solid waste landfills.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 344: 118443, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Max Krause",
+                "hasEmail": "mailto:krause.max@epa.gov"
+            },
+            "description": "Data from the manuscript regarding the analysis of leachate volumes at Ohio landfills to assess sources of moisture. Data includes moisture contents, precipitation, evaportranspiration, and leachate volumes or masses. \n\nThis dataset is associated with the following publication:\nKrause, M., W. Eades, N. Detwiler, D. Marro, A. Schwarber, and T. Tolaymat. Assessing moisture contributions from precipitation, waste, and leachate for active municipal solid waste landfills.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 344: 118443, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526474/Water%20balance%20Science%20Hub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Water balance Science Hub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1526474",
             "keyword": [
@@ -181872,20 +181876,10 @@
                 "precipitation",
                 "moisture content"
             ],
-            "contactPoint": {
-                "fn": "Max Krause",
-                "hasEmail": "mailto:krause.max@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Water balance Science Hub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526474/Water%20balance%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-05-25",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2023.118443"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181895,19 +181889,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2023.118443"
+            ],
+            "rights": null,
+            "title": "Assessment of Ohio Landfill Moisture Contents"
         },
         {
-            "title": "Culture-experiment dataset ",
-            "description": "The dataset including qPCR and microcystin is used for assessment of treatment. \n\nThis dataset is associated with the following publication:\nStruewing, I., N. Sienkiewicz, C. Zhang, N. Dugan, and J. Lu. Effective Early Treatment of Microcystis Exponential Growth and Microcystin Production with Hydrogen Peroxide and Hydroxyapatite.   Toxins. MDPI, Basel,  SWITZERLAND, 15(1): 3, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jingrang Lu",
+                "hasEmail": "mailto:lu.jingrang@epa.gov"
+            },
+            "description": "The dataset including qPCR and microcystin is used for assessment of treatment. \n\nThis dataset is associated with the following publication:\nStruewing, I., N. Sienkiewicz, C. Zhang, N. Dugan, and J. Lu. Effective Early Treatment of Microcystis Exponential Growth and Microcystin Production with Hydrogen Peroxide and Hydroxyapatite.   Toxins. MDPI, Basel,  SWITZERLAND, 15(1): 3, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529458/Culture-experiment%20dataset%20.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Culture-experiment dataset .xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529458",
             "keyword": [
@@ -181919,21 +181923,10 @@
                 "mitigation",
                 "microcystis aeruginosa"
             ],
-            "contactPoint": {
-                "fn": "Jingrang Lu",
-                "hasEmail": "mailto:lu.jingrang@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Culture-experiment dataset .xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529458/Culture-experiment%20dataset%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-01",
-            "references": [
-                "https://doi.org/10.3390/toxins15010003",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9864239"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181943,19 +181936,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/toxins15010003",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9864239"
+            ],
+            "rights": null,
+            "title": "Culture-experiment dataset "
         },
         {
-            "title": "River basin simulations reveal wide-ranging wetland-mediated nitrate load reductions",
-            "description": "Supporting information for \"River basin simulations reveal wide-ranging wetland-mediated nitrate load reductions\". Supporting information includes the calibrated baseline model and the modified Soil and Water Assessment Tool (SWAT) source code and executable file. The supporting information also provides metadata -- and download links -- for the model input and output files for all model runs described in the manuscript. \n\nThis dataset is associated with the following publication:\nEvenson, G., H. Golden, J. Christensen, C. Lane, M. Kalcic, A. Rajib, Q. Wu, D.T. Mahoney, E. White, and E. D'Amico. River Basin Simulations Reveal Wide-Ranging Wetland-Mediated Nitrate Reductions.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 27(26): 9822-9831, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Grey Evenson",
+                "hasEmail": "mailto:evenson.grey@epa.gov"
+            },
+            "description": "Supporting information for \"River basin simulations reveal wide-ranging wetland-mediated nitrate load reductions\". Supporting information includes the calibrated baseline model and the modified Soil and Water Assessment Tool (SWAT) source code and executable file. The supporting information also provides metadata -- and download links -- for the model input and output files for all model runs described in the manuscript. \n\nThis dataset is associated with the following publication:\nEvenson, G., H. Golden, J. Christensen, C. Lane, M. Kalcic, A. Rajib, Q. Wu, D.T. Mahoney, E. White, and E. D'Amico. River Basin Simulations Reveal Wide-Ranging Wetland-Mediated Nitrate Reductions.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 27(26): 9822-9831, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529537/Evenson_etal_ES%26T_SciHub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Evenson_etal_ES&T_SciHub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529537",
             "keyword": [
@@ -181966,20 +181970,10 @@
                 "best management practices (BMPs)",
                 "wetlands"
             ],
-            "contactPoint": {
-                "fn": "Grey Evenson",
-                "hasEmail": "mailto:evenson.grey@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Evenson_etal_ES&T_SciHub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529537/Evenson_etal_ES%26T_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-11-15",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c02161"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -181989,41 +181983,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c02161"
+            ],
+            "rights": null,
+            "title": "River basin simulations reveal wide-ranging wetland-mediated nitrate load reductions"
         },
         {
-            "title": "FengChang et al_ML Output.xlsx",
-            "description": "Outputs from WRF, EPIC, VIC. Outputs and analysis from the ML-based model described in the paper. \n\nThis dataset is associated with the following publication:\nFeng Chang, C., M. Astitha, Y. Yuan, C. Tang, P. Vlahos, V. Garcia, and U. Khaira. A New Approach to Predict Tributary Phosphorus Loads Using Machine Learning\u2013 and Physics-Based Modeling Systems.    Artificial Intelligence for the Earth Systems. American Meteorological Society, Boston, MA, USA, 2(3): 1-43, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529548",
-            "keyword": [
-                "tributary phosphorus loads",
-                "machine learning",
-                "eutrophication",
-                "numerical prediction models"
-            ],
             "contactPoint": {
                 "fn": "Yongping Yuan",
                 "hasEmail": "mailto:yuan.yongping@epa.gov"
             },
+            "description": "Outputs from WRF, EPIC, VIC. Outputs and analysis from the ML-based model described in the paper. \n\nThis dataset is associated with the following publication:\nFeng Chang, C., M. Astitha, Y. Yuan, C. Tang, P. Vlahos, V. Garcia, and U. Khaira. A New Approach to Predict Tributary Phosphorus Loads Using Machine Learning\u2013 and Physics-Based Modeling Systems.    Artificial Intelligence for the Earth Systems. American Meteorological Society, Boston, MA, USA, 2(3): 1-43, (2023).",
             "distribution": [
                 {
-                    "title": "FengChang et al_ML Outputs.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529548/FengChang%20et%20al_ML%20Outputs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FengChang et al_ML Outputs.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529548",
+            "keyword": [
+                "tributary phosphorus loads",
+                "machine learning",
+                "eutrophication",
+                "numerical prediction models"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-06",
-            "references": [
-                "https://doi.org/10.1175/aies-d-22-0049.1"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182033,19 +182027,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1175/aies-d-22-0049.1"
+            ],
+            "rights": null,
+            "title": "FengChang et al_ML Output.xlsx"
         },
         {
-            "title": "Data used in the manuscript \"An Analysis of CMAQ Gas Phase Dry Deposition over North America Through Grid-Scale and Land-Use Specific Diagnostics in the Context of AQMEII4\"",
-            "description": "This dataset contains the data used to generate the figures in the manuscript \"An Analysis of CMAQ Gas Phase Dry Deposition over North America Through Grid-Scale and Land-Use Specific Diagnostics in the Context of AQMEII4\". It also contains the data used to generate teh figures in the supplemental material. \n\nThis dataset is associated with the following publication:\nHogrefe, C., J. Bash, J. Pleim, D. Schwede, R. Gilliam, K. Foley, K. Appel, and R. Mathur. An Analysis of CMAQ Gas Phase Dry Deposition over North America Through Grid-Scale and Land-Use Specific Diagnostics in the Context of AQMEII4.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 23(14): 8119\u20138147, (2023).",
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
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1528362/documents/DataDictionary_HogrefeEtAl.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This dataset contains the data used to generate the figures in the manuscript \"An Analysis of CMAQ Gas Phase Dry Deposition over North America Through Grid-Scale and Land-Use Specific Diagnostics in the Context of AQMEII4\". It also contains the data used to generate teh figures in the supplemental material. \n\nThis dataset is associated with the following publication:\nHogrefe, C., J. Bash, J. Pleim, D. Schwede, R. Gilliam, K. Foley, K. Appel, and R. Mathur. An Analysis of CMAQ Gas Phase Dry Deposition over North America Through Grid-Scale and Land-Use Specific Diagnostics in the Context of AQMEII4.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 23(14): 8119\u20138147, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528362/HogrefeEtAl_ACP2023_10_FigureData.zip",
+                    "mediaType": "application/zip",
+                    "title": "HogrefeEtAl_ACP2023_10_FigureData.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528362",
             "keyword": [
@@ -182056,20 +182062,10 @@
                 "CMAQ",
                 "AQMEII"
             ],
-            "contactPoint": {
-                "fn": "Christian Hogrefe",
-                "hasEmail": "mailto:hogrefe.christian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "HogrefeEtAl_ACP2023_10_FigureData.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528362/HogrefeEtAl_ACP2023_10_FigureData.zip",
-                    "mediaType": "application/zip"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-15",
-            "references": [
-                "https://doi.org/10.5194/acp-23-8119-2023"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182080,48 +182076,46 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1528362/documents/DataDictionary_HogrefeEtAl.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/acp-23-8119-2023"
+            ],
+            "rights": null,
+            "title": "Data used in the manuscript \"An Analysis of CMAQ Gas Phase Dry Deposition over North America Through Grid-Scale and Land-Use Specific Diagnostics in the Context of AQMEII4\""
         },
         {
-            "title": "Water quality data",
-            "description": "The ZTRAX data is a national database of property sales collected by Zillow.  The data is available to researchers who submit a research proposal to Zillow. Portions of this dataset are inaccessible because: Not publicly available. They can be accessed through the following means: Requires a data sharing agreement with Zillow. Format: National property sales database\r\n\r\nhttps://www.zillow.com/research/ztrax/. \n\nThis dataset is associated with the following publication:\nMamun, S., A. Castillo, K. Swedberg, J. Zhang, K.J. Boyle, D. Cardoso, C.L. King, C. Nolte, M. Papenfus, D. Phaneuf, and S. Polasky. Valuing water quality in the United States using a national dataset on property values.   PNAS  (PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES). National Academy of Sciences, WASHINGTON, DC, USA, 120(5): e2210417120, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526547",
-            "keyword": [
-                "water quality",
-                "property values",
-                "national study",
-                "economics",
-                "economic benefits",
-                "spatial heterogeneity"
-            ],
             "contactPoint": {
                 "fn": "Michael Papenfus",
                 "hasEmail": "mailto:papenfus.michael@epa.gov"
             },
+            "describedBy": "https://github.com/WaterResourceEconomics/PNAS-NWH",
+            "description": "The ZTRAX data is a national database of property sales collected by Zillow.  The data is available to researchers who submit a research proposal to Zillow. Portions of this dataset are inaccessible because: Not publicly available. They can be accessed through the following means: Requires a data sharing agreement with Zillow. Format: National property sales database\r\n\r\nhttps://www.zillow.com/research/ztrax/. \n\nThis dataset is associated with the following publication:\nMamun, S., A. Castillo, K. Swedberg, J. Zhang, K.J. Boyle, D. Cardoso, C.L. King, C. Nolte, M. Papenfus, D. Phaneuf, and S. Polasky. Valuing water quality in the United States using a national dataset on property values.   PNAS  (PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES). National Academy of Sciences, WASHINGTON, DC, USA, 120(5): e2210417120, (2023).",
             "distribution": [
                 {
-                    "title": "https://lagoslakes.org/",
-                    "accessURL": "https://lagoslakes.org/"
+                    "accessURL": "https://lagoslakes.org/",
+                    "title": "https://lagoslakes.org/"
                 },
                 {
-                    "title": "https://www.waterqualitydata.us/",
-                    "accessURL": "https://www.waterqualitydata.us/"
+                    "accessURL": "https://www.waterqualitydata.us/",
+                    "title": "https://www.waterqualitydata.us/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526547",
+            "keyword": [
+                "water quality",
+                "property values",
+                "national study",
+                "economics",
+                "economic benefits",
+                "spatial heterogeneity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-10-24",
-            "references": [
-                "https://doi.org/10.1073/pnas.2210417120",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10104588"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182132,33 +182126,33 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/WaterResourceEconomics/PNAS-NWH"
+            "references": [
+                "https://doi.org/10.1073/pnas.2210417120",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10104588"
+            ],
+            "rights": null,
+            "title": "Water quality data"
         },
         {
-            "title": "Data for AQMEII-4 Activity 2 Technical Note - version 1",
-            "description": "The data set consists of measurements obtained during ozone flux studies. This dataset is not publicly accessible because: The data is not publicly available and is only available to activity participants via a password protected site. It can be accessed through the following means: Some data sets are available publicly as cited in the references.  Other data sets must be obtained directly from the principal investigator who conducted the experimental study. Format: The data files are in text format. \n\nThis dataset is associated with the following publication:\nClifton, O., D. Schwede, C. Hogrefe, J. Bash, S. Bland, P. Cheung, M. Coyle, L. Emberson, J. Fleming, E. Fredj, S. Galmarini, L. Ganzeveld, O. Gazetas, I. Goded, C. Holmes, L. Horv\u00e1th, V. Huijnen, Q. Li, P. Makar, I. Mammarella, G. Manca, W. Munger, J. P\u00e9rez-Camanyo, J. Pleim, L. Limei Ran, R. San Jose, S. Silva, R. Staebler, S. Sun, A. Tai, E. Tas, T. Vesala, T. Weidinger, Z. Wu, and L. Zhang. A single-point modeling approach for the intercomparison and evaluation of ozone dry deposition across chemical transport models (Activity 2 of AQMEII4).   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 23(17): 9911\u20139961, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1523122",
-            "keyword": [
-                "atmospheric deposition",
-                "Ozone"
-            ],
             "contactPoint": {
                 "fn": "Donna Schwede",
                 "hasEmail": "mailto:schwede.donna@epa.gov"
             },
+            "description": "The data set consists of measurements obtained during ozone flux studies. This dataset is not publicly accessible because: The data is not publicly available and is only available to activity participants via a password protected site. It can be accessed through the following means: Some data sets are available publicly as cited in the references.  Other data sets must be obtained directly from the principal investigator who conducted the experimental study. Format: The data files are in text format. \n\nThis dataset is associated with the following publication:\nClifton, O., D. Schwede, C. Hogrefe, J. Bash, S. Bland, P. Cheung, M. Coyle, L. Emberson, J. Fleming, E. Fredj, S. Galmarini, L. Ganzeveld, O. Gazetas, I. Goded, C. Holmes, L. Horv\u00e1th, V. Huijnen, Q. Li, P. Makar, I. Mammarella, G. Manca, W. Munger, J. P\u00e9rez-Camanyo, J. Pleim, L. Limei Ran, R. San Jose, S. Silva, R. Staebler, S. Sun, A. Tai, E. Tas, T. Vesala, T. Weidinger, Z. Wu, and L. Zhang. A single-point modeling approach for the intercomparison and evaluation of ozone dry deposition across chemical transport models (Activity 2 of AQMEII4).   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 23(17): 9911\u20139961, (2023).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1523122",
+            "keyword": [
+                "atmospheric deposition",
+                "Ozone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-09-15",
-            "references": [
-                "https://doi.org/10.5194/acp-23-9911-2023"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182168,19 +182162,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-23-9911-2023"
+            ],
+            "rights": null,
+            "title": "Data for AQMEII-4 Activity 2 Technical Note - version 1"
         },
         {
-            "title": "National Lakes Assessment (NLA) 2007 Report: Archived Data",
-            "description": "National Lakes Assessment 2007 Datafiles for Report \u201cNational Lakes Assessment: A Collaborative Survey of the Nation\u2019s Lakes\u201d: \n\nThe National Lakes Assessment (NLA) is a statistical survey of the condition of our nation's lakes, ponds, and reservoirs. It is designed to provide information on the extent of lakes that support healthy biological condition and recreation, estimate how widespread major stressors are that impact lake quality, and provide insight into whether lakes nationwide are getting cleaner. The first NLA was conducted in 2007. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NLA report. Sampling was conducted in the summer of 2007 at approximately 1000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic macroinvertebrates, physical habitat, landscape metrics, phytoplankton data, secchi depth, data, tropic status, water isotopes, zooplankton, etc.  Users are encouraged to visit the NARS data webpage for potential updates to data files and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys\n\nCitation for the NLA 2007 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Lakes Assessment 2007 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/national-lakes-assessment-2007-report. DOI: 10.23719/1529550\n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation.  EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Lakes Assessment 2007 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d\n\nAdditional information: NLA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Sarah Lehmann",
+                "hasEmail": "mailto:lehmann.sarah@epa.gov"
+            },
+            "description": "National Lakes Assessment 2007 Datafiles for Report \u201cNational Lakes Assessment: A Collaborative Survey of the Nation\u2019s Lakes\u201d: \n\nThe National Lakes Assessment (NLA) is a statistical survey of the condition of our nation's lakes, ponds, and reservoirs. It is designed to provide information on the extent of lakes that support healthy biological condition and recreation, estimate how widespread major stressors are that impact lake quality, and provide insight into whether lakes nationwide are getting cleaner. The first NLA was conducted in 2007. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NLA report. Sampling was conducted in the summer of 2007 at approximately 1000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic macroinvertebrates, physical habitat, landscape metrics, phytoplankton data, secchi depth, data, tropic status, water isotopes, zooplankton, etc.  Users are encouraged to visit the NARS data webpage for potential updates to data files and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys\n\nCitation for the NLA 2007 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Lakes Assessment 2007 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/national-lakes-assessment-2007-report. DOI: 10.23719/1529550\n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation.  EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Lakes Assessment 2007 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d\n\nAdditional information: NLA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/national-lakes-assessment-2007-report",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/national-lakes-assessment-2007-report"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529550",
             "keyword": [
@@ -182200,36 +182203,36 @@
                 "biological",
                 "assessment"
             ],
-            "contactPoint": {
-                "fn": "Sarah Lehmann",
-                "hasEmail": "mailto:lehmann.sarah@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/national-lakes-assessment-2007-report",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/national-lakes-assessment-2007-report"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2013-07-11",
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
+            "title": "National Lakes Assessment (NLA) 2007 Report: Archived Data"
         },
         {
-            "title": "Dataset for journal article 'Determinants of gene expression in the human liver: Impact of aging and sex on xenobiotic metabolism'",
-            "description": "Gene array data files compared gene expression profiles in liver samples from young (21-45 years) and old (69+ years) men and women to determine changes in the expression of xenobiotic metabolism enzymes and transporters. We identified genes that were differentially expressed in males only, females only, or in all individuals between the young and old using microarray. \n\nThis dataset is associated with the following publication:\nCorton, J., J. Lee, J. Liu, H. Ren, B. Vallanat, and M. Devito. Determinants of Gene Expression in the Human Liver: Impact of Aging and Sex on Xenobiotic Metabolism.   Experimental Gerontology. Elsevier Science Ltd, New York, NY, USA, 169: 111976, (2022).",
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
+            "description": "Gene array data files compared gene expression profiles in liver samples from young (21-45 years) and old (69+ years) men and women to determine changes in the expression of xenobiotic metabolism enzymes and transporters. We identified genes that were differentially expressed in males only, females only, or in all individuals between the young and old using microarray. \n\nThis dataset is associated with the following publication:\nCorton, J., J. Lee, J. Liu, H. Ren, B. Vallanat, and M. Devito. Determinants of Gene Expression in the Human Liver: Impact of Aging and Sex on Xenobiotic Metabolism.   Experimental Gerontology. Elsevier Science Ltd, New York, NY, USA, 169: 111976, (2022).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133815",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133815"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528717",
             "keyword": [
@@ -182240,19 +182243,10 @@
                 "P450 enzyme activities",
                 "Xenobiotic metabolizing genes"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133815",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE133815"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2019-07-06",
-            "references": [
-                "https://doi.org/10.1016/j.exger.2022.111976"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182262,88 +182256,88 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.exger.2022.111976"
+            ],
+            "rights": null,
+            "title": "Dataset for journal article 'Determinants of gene expression in the human liver: Impact of aging and sex on xenobiotic metabolism'"
         },
         {
-            "title": "Differential expressed mRNA and microRNA from expression profiling by RNA and small RNA sequencing",
-            "description": "data was from HepG2 cells treated with nano-silver particles using silver nitrate as negative controls.    Differentially expressed messenger RNA and microRNA were obtained by RNA sequencing and data analysis.  Differentially expressed RNA and microRNA lists were than uploaded to Ingenuity Pathway Analysis to find the pathways altered by the differentially expressed genes. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, B. Robinette, H. Ren, B. Vallanat, A. Fisher, and K. Kitchin. Effects of Silver Nanoparticles and Silver Nitrate on mRNA and microRNA Expression in Human Hepatocellular Carcinoma Cells (HepG2).   Journal of Nanoscience and Nanotechnology. American Scientific Publishers, VALENCIA, CA, USA, 21(11): 5414-5428, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1520580",
-            "keyword": [
-                "nano silver",
-                "silver nitrate",
-                "transcriptomics",
-                "microRNA expression",
-                "Target Filter Analysis",
-                "signaling pathways"
-            ],
             "contactPoint": {
                 "fn": "Sheau-Fung Thai",
                 "hasEmail": "mailto:thai.sheau-fung@epa.gov"
             },
+            "description": "data was from HepG2 cells treated with nano-silver particles using silver nitrate as negative controls.    Differentially expressed messenger RNA and microRNA were obtained by RNA sequencing and data analysis.  Differentially expressed RNA and microRNA lists were than uploaded to Ingenuity Pathway Analysis to find the pathways altered by the differentially expressed genes. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, B. Robinette, H. Ren, B. Vallanat, A. Fisher, and K. Kitchin. Effects of Silver Nanoparticles and Silver Nitrate on mRNA and microRNA Expression in Human Hepatocellular Carcinoma Cells (HepG2).   Journal of Nanoscience and Nanotechnology. American Scientific Publishers, VALENCIA, CA, USA, 21(11): 5414-5428, (2021).",
             "distribution": [
                 {
-                    "title": "DEG-0.05-result_AgNO3_1_8.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgNO3_1_8.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgNO3_1_8.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-result_AgNO3_1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgNO3_1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgNO3_1.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-result_AgNO3_0_25.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgNO3_0_25.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgNO3_0_25.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-result_AgNO3_0_5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgNO3_0_5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgNO3_0_5.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-result_AgS_40.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgS_40.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgS_40.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-result_AgS_20.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgS_20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgS_20.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-result_AgS_10.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgS_10.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgS_10.xlsx"
                 },
                 {
-                    "title": "DEG-0.05-result_AgS_5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/DEG-0.05-result_AgS_5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DEG-0.05-result_AgS_5.xlsx"
                 },
                 {
-                    "title": "AgNO3 miR lists.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/AgNO3%20miR%20lists.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AgNO3 miR lists.csv"
                 },
                 {
-                    "title": "AgS miRNA lists.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520580/AgS%20miRNA%20lists.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AgS miRNA lists.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520580",
+            "keyword": [
+                "nano silver",
+                "silver nitrate",
+                "transcriptomics",
+                "microRNA expression",
+                "Target Filter Analysis",
+                "signaling pathways"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-04-01",
-            "references": [
-                "https://doi.org/10.1166/jnn.2021.19481"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182353,41 +182347,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1166/jnn.2021.19481"
+            ],
+            "rights": null,
+            "title": "Differential expressed mRNA and microRNA from expression profiling by RNA and small RNA sequencing"
         },
         {
-            "title": "AUV and a Remotely Operated Vehicle Gulper Chemistry Data",
-            "description": "Data from underwater oil detection technologies are provided (1) A Remote Environmental Monitoring UnitS (REMUS-600) AUV equipped with fluorescence and backscatter SeaOWL UV-A (Oil-in-Water Locator; Sea-Bird Scientific WET Labs Inc.), holographic imager (HoloCam; SeaScan, Inc), hydrographic information, video camera, CTD and a water/oil sampler.  (2) A tethered ROV system (DTG2, Deep Trekker Inc.) equipped with video camera, UviLux (Chelsea Technologies Group, Inc) fluorometer, a CTD and water/oil sampler.  Calibration and validation tests of the sensor suite were conducted at the Coastal Response Research Center flume tank (NH, USA). Oil concentration estimates were verified by chemical analysis of hydrocarbons and particle size analysis (LISST 200X, Sequoia, Inc). Operational performance of the ROV platform and sensors was evaluated at the Ohmsett wave tank (NJ, USA). Field performance of the REMUS and sensor suite was evaluated at natural seeps near Santa Barbara, CA. \n\nThis dataset is associated with the following publication:\nGomez-Ibanez, D., A. Kukulya, A. Belani, R. Conmy, D. Sundaravadivelu, and L. DiPinto. Autonomous water sampler for oil spill response.   Journal of Marine Science and Engineering. MDPI, Basel,  SWITZERLAND, 10(4): 526, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529583",
-            "keyword": [
-                "environmental cleanup",
-                "Oil and Gas",
-                "chemicals",
-                "emergency response"
-            ],
             "contactPoint": {
                 "fn": "Robyn Conmy",
                 "hasEmail": "mailto:conmy.robyn@epa.gov"
             },
+            "description": "Data from underwater oil detection technologies are provided (1) A Remote Environmental Monitoring UnitS (REMUS-600) AUV equipped with fluorescence and backscatter SeaOWL UV-A (Oil-in-Water Locator; Sea-Bird Scientific WET Labs Inc.), holographic imager (HoloCam; SeaScan, Inc), hydrographic information, video camera, CTD and a water/oil sampler.  (2) A tethered ROV system (DTG2, Deep Trekker Inc.) equipped with video camera, UviLux (Chelsea Technologies Group, Inc) fluorometer, a CTD and water/oil sampler.  Calibration and validation tests of the sensor suite were conducted at the Coastal Response Research Center flume tank (NH, USA). Oil concentration estimates were verified by chemical analysis of hydrocarbons and particle size analysis (LISST 200X, Sequoia, Inc). Operational performance of the ROV platform and sensors was evaluated at the Ohmsett wave tank (NJ, USA). Field performance of the REMUS and sensor suite was evaluated at natural seeps near Santa Barbara, CA. \n\nThis dataset is associated with the following publication:\nGomez-Ibanez, D., A. Kukulya, A. Belani, R. Conmy, D. Sundaravadivelu, and L. DiPinto. Autonomous water sampler for oil spill response.   Journal of Marine Science and Engineering. MDPI, Basel,  SWITZERLAND, 10(4): 526, (2022).",
             "distribution": [
                 {
-                    "title": "AUV Gulper Chemistry Data Summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529583/AUV%20Gulper%20Chemistry%20Data%20Summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AUV Gulper Chemistry Data Summary.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529583",
+            "keyword": [
+                "environmental cleanup",
+                "Oil and Gas",
+                "chemicals",
+                "emergency response"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-04-30",
-            "references": [
-                "https://doi.org/10.3390/jmse10040526"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182397,41 +182391,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/jmse10040526"
+            ],
+            "rights": null,
+            "title": "AUV and a Remotely Operated Vehicle Gulper Chemistry Data"
         },
         {
-            "title": "Geographical and Seasonal Patterns in the Carbonate Chemistry of Narragansett Bay, RI",
-            "description": "This data comprises geographical and seasonal patterns in water quality and carbonate chemistry parameters in Narragansett Bay, RI, USA. Direct measurements of salinity, temperature, dissolved oxygen concentration, dissolved oxygen percent saturation, pH on the NBS scale, dissolved inorganic carbon concentration, and total alkalinity concentration were performed during monthly sampling cruises carried out over three years. The information provided by carbonate chemistry analysis allowed for the characterization of acidification in this estuary. Portions of this dataset are inaccessible because: NA. They can be accessed through the following means: NA. Format: NA. \n\nThis dataset is associated with the following publication:\nPimenta, A.R., A. Oczkowski, R. McKinney, and J. Grear. Geographical and seasonal patterns in the carbonate chemistry of Narragansett Bay, RI.   Regional Studies in Marine Science. Elsevier B.V., Amsterdam,  NETHERLANDS, 62(September 2023): 102903, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1523131",
-            "keyword": [
-                "Nitrogen and Co-pollutants",
-                "aragonite saturation",
-                "carbonate chemistry",
-                "coastal acidification"
-            ],
             "contactPoint": {
                 "fn": "Adam Pimenta",
                 "hasEmail": "mailto:pimenta.adam@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1523131/documents/Water%20Quality%20and%20Carbonate%20Chemistry%20Parameters%20In%20Narragansett%20Bay%2C%20RI%2C%20USA%20-%20Data%20Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This data comprises geographical and seasonal patterns in water quality and carbonate chemistry parameters in Narragansett Bay, RI, USA. Direct measurements of salinity, temperature, dissolved oxygen concentration, dissolved oxygen percent saturation, pH on the NBS scale, dissolved inorganic carbon concentration, and total alkalinity concentration were performed during monthly sampling cruises carried out over three years. The information provided by carbonate chemistry analysis allowed for the characterization of acidification in this estuary. Portions of this dataset are inaccessible because: NA. They can be accessed through the following means: NA. Format: NA. \n\nThis dataset is associated with the following publication:\nPimenta, A.R., A. Oczkowski, R. McKinney, and J. Grear. Geographical and seasonal patterns in the carbonate chemistry of Narragansett Bay, RI.   Regional Studies in Marine Science. Elsevier B.V., Amsterdam,  NETHERLANDS, 62(September 2023): 102903, (2023).",
             "distribution": [
                 {
-                    "title": "Water Quality and Carbonate Chemistry Parameters In Narragansett Bay, RI, USA.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523131/Water%20Quality%20and%20Carbonate%20Chemistry%20Parameters%20In%20Narragansett%20Bay%2C%20RI%2C%20USA.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Water Quality and Carbonate Chemistry Parameters In Narragansett Bay, RI, USA.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1523131",
+            "keyword": [
+                "Nitrogen and Co-pollutants",
+                "aragonite saturation",
+                "carbonate chemistry",
+                "coastal acidification"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-13",
-            "references": [
-                "https://doi.org/10.1016/j.rsma.2023.102903"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182442,46 +182438,46 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1523131/documents/Water%20Quality%20and%20Carbonate%20Chemistry%20Parameters%20In%20Narragansett%20Bay%2C%20RI%2C%20USA%20-%20Data%20Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.rsma.2023.102903"
+            ],
+            "rights": null,
+            "title": "Geographical and Seasonal Patterns in the Carbonate Chemistry of Narragansett Bay, RI"
         },
         {
-            "title": "Performance data for enhanced Innovative/Alternative (I/A) septic systems for nitrogen removal installed in a field demonstration in Barnstable, Massachusetts (2021 - 2023)",
-            "description": "Performance data for enhanced I/A septic systems designed for nitrogen removal that were installed during a demonstration project in Barnstable, MA. Includes 1) field and laboratory measurements of water quality parameters in influent, effluent, and lysimeters below leach fields (where available) and 2) metered flow to each system. The initial release (Version 1) includes data collected from 2021-12-10 through 2023-05-03. The second release (Version 2) adds data through 2023-12-04. The README file contains additional details, including notes on data limitations and a change log.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529539",
-            "keyword": [
-                "wastewater monitoring",
-                "Nitrogen and Co-pollutants",
-                "septic systems",
-                "wastewater treatment"
-            ],
             "contactPoint": {
                 "fn": "Laura Erban",
                 "hasEmail": "mailto:erban.laura@epa.gov"
             },
+            "description": "Performance data for enhanced I/A septic systems designed for nitrogen removal that were installed during a demonstration project in Barnstable, MA. Includes 1) field and laboratory measurements of water quality parameters in influent, effluent, and lysimeters below leach fields (where available) and 2) metered flow to each system. The initial release (Version 1) includes data collected from 2021-12-10 through 2023-05-03. The second release (Version 2) adds data through 2023-12-04. The README file contains additional details, including notes on data limitations and a change log.",
             "distribution": [
                 {
-                    "title": "V1 data release.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529539/V1%20data%20release.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "V1 data release.zip"
                 },
                 {
-                    "title": "V2 data release.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529539/V2%20data%20release.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "V2 data release.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529539",
+            "keyword": [
+                "wastewater monitoring",
+                "Nitrogen and Co-pollutants",
+                "septic systems",
+                "wastewater treatment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2024-03-21",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -182490,35 +182486,32 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Performance data for enhanced Innovative/Alternative (I/A) septic systems for nitrogen removal installed in a field demonstration in Barnstable, Massachusetts (2021 - 2023)"
         },
         {
-            "title": "SDR2022",
-            "description": "Qualitative interviews related to experiences with the nutrients solutions-driven research pilot based out of EPA-ORD-ACESD. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Only people with CITI Training and associated with the project can access the raw data due to human subject research ethics requirements. Format: Word documents and NVivo file. \n\nThis dataset is associated with the following publication:\nCanfield, K.N., K. Mulvaney, and C.D. Chatelain. Using researcher and stakeholder perspectives to develop promising practices to improve stakeholder engagement in the solutions-driven research process.   Socio-Ecological Practice Research. Springer Nature, New York, NY,  4(3): 189-203, (2022).",
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
+            "description": "Qualitative interviews related to experiences with the nutrients solutions-driven research pilot based out of EPA-ORD-ACESD. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Only people with CITI Training and associated with the project can access the raw data due to human subject research ethics requirements. Format: Word documents and NVivo file. \n\nThis dataset is associated with the following publication:\nCanfield, K.N., K. Mulvaney, and C.D. Chatelain. Using researcher and stakeholder perspectives to develop promising practices to improve stakeholder engagement in the solutions-driven research process.   Socio-Ecological Practice Research. Springer Nature, New York, NY,  4(3): 189-203, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529547",
             "keyword": [
                 "nutrients",
                 "applied social science",
                 "stakeholder engagement"
             ],
-            "contactPoint": {
-                "fn": "Katherine Canfield",
-                "hasEmail": "mailto:canfield.katherine@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-23",
-            "references": [
-                "https://doi.org/10.1007/s42532-022-00119-5",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9281378"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182528,50 +182521,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s42532-022-00119-5",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9281378"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "SDR2022"
         },
         {
-            "title": "FHM reference genome, annotation, and all associated DNA and RNA-sequencing data   ",
-            "description": "The dataset contains the full fathead minnow (FHM) reference genome and annotation data as well all DNA sequencing data (PacBio long reads and Illumina paired-end reads) and RNA-seq data that were used to create the fathead minnow genome reference. \n\nThis dataset is associated with the following publication:\nMartinson, J., D. Bencic, G. Toth, R. Flick, M. Kostich, M.J. See, D. Lattier, A. Biales, and W. Huang. De Novo Assembly of the Nearly Complete Fathead Minnow Reference Genome Reveals a Repetitive but Compact Genome.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(2): 448-461, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1520933",
-            "keyword": [
-                "Clean Water Act",
-                "complete genome",
-                "Fathead minnows",
-                "aquatic toxicity",
-                "zebrafish"
-            ],
             "contactPoint": {
                 "fn": "Weichun Huang",
                 "hasEmail": "mailto:huang.weichun@epa.gov"
             },
+            "description": "The dataset contains the full fathead minnow (FHM) reference genome and annotation data as well all DNA sequencing data (PacBio long reads and Illumina paired-end reads) and RNA-seq data that were used to create the fathead minnow genome reference. \n\nThis dataset is associated with the following publication:\nMartinson, J., D. Bencic, G. Toth, R. Flick, M. Kostich, M.J. See, D. Lattier, A. Biales, and W. Huang. De Novo Assembly of the Nearly Complete Fathead Minnow Reference Genome Reveals a Repetitive but Compact Genome.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(2): 448-461, (2022).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/assembly/GCF_016745375.1/",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/assembly/GCF_016745375.1/"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/assembly/GCF_016745375.1/",
+                    "title": "https://www.ncbi.nlm.nih.gov/assembly/GCF_016745375.1/"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA565199/",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA565199/"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA565199/",
+                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA565199/"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN12875914/",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN12875914/"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN12875914/",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN12875914/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520933",
+            "keyword": [
+                "Clean Water Act",
+                "complete genome",
+                "Fathead minnows",
+                "aquatic toxicity",
+                "zebrafish"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-03-01",
-            "references": [
-                "https://doi.org/10.1002/etc.5266",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9560796"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182581,41 +182574,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5266",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9560796"
+            ],
+            "rights": null,
+            "title": "FHM reference genome, annotation, and all associated DNA and RNA-sequencing data   "
         },
         {
-            "title": "Effects of metformin and its metabolite guanylurea on fathead minnow (Pimephales promelas) reproduction",
-            "description": "Data associated with exposures of fathead minnows to varying concentrations of metformin and/or guanylurea. Includes three individual studies: ex vivo steroidogenesis assay, 96 h time course assay, 23 d reproduction assay. \n\nThis dataset is associated with the following publication:\nBlackwell, B., G. Ankley, A. Biales, J. Cavallin, A. Cole, T. Collette, D. Ekman, R. Hofer, W. Huang, K. Jensen, M. Kahl, A. Kittelson, S. Romano, M. See, Q. Teng, C. Tilton, and D. Villeneuve. Effects of Metformin and its Metabolite Guanylurea on Fathead Minnow (Pimephales promelas) Reproduction (FY22 Manuscript).   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(11): 2708-2720, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526538",
-            "keyword": [
-                "reproduction",
-                "aquatic toxicity",
-                "pharmaceuticals",
-                "endocrine disruption"
-            ],
             "contactPoint": {
                 "fn": "Brett Blackwell",
                 "hasEmail": "mailto:blackwell.brett@epa.gov"
             },
+            "description": "Data associated with exposures of fathead minnows to varying concentrations of metformin and/or guanylurea. Includes three individual studies: ex vivo steroidogenesis assay, 96 h time course assay, 23 d reproduction assay. \n\nThis dataset is associated with the following publication:\nBlackwell, B., G. Ankley, A. Biales, J. Cavallin, A. Cole, T. Collette, D. Ekman, R. Hofer, W. Huang, K. Jensen, M. Kahl, A. Kittelson, S. Romano, M. See, Q. Teng, C. Tilton, and D. Villeneuve. Effects of Metformin and its Metabolite Guanylurea on Fathead Minnow (Pimephales promelas) Reproduction (FY22 Manuscript).   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(11): 2708-2720, (2022).",
             "distribution": [
                 {
-                    "title": "SciHub_metformin effects_final.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526538/SciHub_metformin%20effects_final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub_metformin effects_final.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526538",
+            "keyword": [
+                "reproduction",
+                "aquatic toxicity",
+                "pharmaceuticals",
+                "endocrine disruption"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-07-01",
-            "references": [
-                "https://doi.org/10.1002/etc.5450"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182625,40 +182619,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5450"
+            ],
+            "rights": null,
+            "title": "Effects of metformin and its metabolite guanylurea on fathead minnow (Pimephales promelas) reproduction"
         },
         {
-            "title": "Dataset Correction and Accuracy of PurpleAir PM2.5 Measurements for Extreme Wildfire Smoke",
-            "description": "This dataset provides the dataset used in the paper \"Correction and Accuracy of PurpleAir PM2.5 Measurements for Extreme Wildfire Smoke\".",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528138",
-            "keyword": [
-                "air sensor",
-                "pm2.5",
-                "air quality",
-                "smoke"
-            ],
             "contactPoint": {
                 "fn": "Karoline Barkjohn",
                 "hasEmail": "mailto:barkjohn.karoline@epa.gov"
             },
+            "description": "This dataset provides the dataset used in the paper \"Correction and Accuracy of PurpleAir PM2.5 Measurements for Extreme Wildfire Smoke\".",
             "distribution": [
                 {
-                    "title": "Dataset_PurpleAirSmoke_Barkjohn_3_15_23.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528138/Dataset_PurpleAirSmoke_Barkjohn_3_15_23.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Dataset_PurpleAirSmoke_Barkjohn_3_15_23.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528138",
+            "keyword": [
+                "air sensor",
+                "pm2.5",
+                "air quality",
+                "smoke"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-10-28",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -182667,76 +182663,74 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Dataset Correction and Accuracy of PurpleAir PM2.5 Measurements for Extreme Wildfire Smoke"
         },
         {
-            "title": "Evaluation of a Multiplexed, Multispecies Nuclear Receptor Assay for Chemical Hazard Assessment",
-            "description": "Table S1. All chemicals and AC50 from invitrodb v3 for human FACTORIAL-TRANS assay endpoints.\nTable S2. Agreement with OECD reference AR agonists.\nTable S3. Agreement with OECD reference ER agonists.\nTable S4. Agreement with OECD reference ER antagonists.\nTable S5. Summary results of 191 test chemicals AC50 agreements\nTable S6. Curve fitting parameters for all endpoints.\nWord File: Supplementary data. \n\nThis dataset is associated with the following publication:\nHouck, K., A. Simha, A. Bone, J. Doering, S. Vliet, C. LaLone, A. Medvedev, and S. Makarov. Evaluation of a Multiplexed, Multispecies Nuclear Receptor Assay for Chemical Hazard Assessment.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 72: 105016, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1518765",
-            "keyword": [
-                "Endocrine Disruptors",
-                "nuclear receptor",
-                "multiplexed assay",
-                "ecotoxicoloty",
-                "reporter gene",
-                "zebrafish",
-                "ToxCast",
-                "High throughput screening",
-                "high throughput toxicology"
-            ],
             "contactPoint": {
                 "fn": "Keith Houck",
                 "hasEmail": "mailto:houck.keith@epa.gov"
             },
+            "description": "Table S1. All chemicals and AC50 from invitrodb v3 for human FACTORIAL-TRANS assay endpoints.\nTable S2. Agreement with OECD reference AR agonists.\nTable S3. Agreement with OECD reference ER agonists.\nTable S4. Agreement with OECD reference ER antagonists.\nTable S5. Summary results of 191 test chemicals AC50 agreements\nTable S6. Curve fitting parameters for all endpoints.\nWord File: Supplementary data. \n\nThis dataset is associated with the following publication:\nHouck, K., A. Simha, A. Bone, J. Doering, S. Vliet, C. LaLone, A. Medvedev, and S. Makarov. Evaluation of a Multiplexed, Multispecies Nuclear Receptor Assay for Chemical Hazard Assessment.   TOXICOLOGY IN VITRO. Elsevier Science Ltd, New York, NY, USA, 72: 105016, (2021).",
             "distribution": [
                 {
-                    "title": "Supplemental Data, S1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518765/Supplemental%20Data%2C%20S1.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplemental Data, S1.docx"
                 },
                 {
-                    "title": "TableS6.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518765/TableS6.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS6.xlsx"
                 },
                 {
-                    "title": "TableS5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518765/TableS5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS5.xlsx"
                 },
                 {
-                    "title": "TableS4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518765/TableS4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS4.xlsx"
                 },
                 {
-                    "title": "TableS3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518765/TableS3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS3.xlsx"
                 },
                 {
-                    "title": "TableS2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518765/TableS2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS2.xlsx"
                 },
                 {
-                    "title": "TableS1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518765/TableS1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518765",
+            "keyword": [
+                "Endocrine Disruptors",
+                "nuclear receptor",
+                "multiplexed assay",
+                "ecotoxicoloty",
+                "reporter gene",
+                "zebrafish",
+                "ToxCast",
+                "High throughput screening",
+                "high throughput toxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-09-21",
-            "references": [
-                "https://doi.org/10.1016/j.tiv.2020.105016"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182746,19 +182740,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tiv.2020.105016"
+            ],
+            "rights": null,
+            "title": "Evaluation of a Multiplexed, Multispecies Nuclear Receptor Assay for Chemical Hazard Assessment"
         },
         {
-            "title": "Data for \"Thyroid Hormone Action Controls Multiple Components of Cell Junctions at the Ventricular Zone in the Newborn Rat Brain\"",
-            "description": "Raw data accompanying \"Thyroid Hormone Action Controls Multiple Components of Cell Junctions at the Ventricular Zone in the Newborn Rat Brain\". \n\nThis dataset is associated with the following publication:\nO'Shaughnessy, K., B. McMichael, A. Sasser, K. Bell, C. Riutta, J. Ford, T. Stoker, R. Grindstaff, A. Pandiri, and M. Gilbert. Thyroid Hormone Action Controls Multiple Components of Cell Junctions at the Ventricular Zone in the Newborn Rat Brain.   Frontiers in Endocrinology. Frontiers, Lausanne,  SWITZERLAND, 14: 1090081, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Katherine O'Shaughnessy",
+                "hasEmail": "mailto:oshaughnessy.katie@epa.gov"
+            },
+            "description": "Raw data accompanying \"Thyroid Hormone Action Controls Multiple Components of Cell Junctions at the Ventricular Zone in the Newborn Rat Brain\". \n\nThis dataset is associated with the following publication:\nO'Shaughnessy, K., B. McMichael, A. Sasser, K. Bell, C. Riutta, J. Ford, T. Stoker, R. Grindstaff, A. Pandiri, and M. Gilbert. Thyroid Hormone Action Controls Multiple Components of Cell Junctions at the Ventricular Zone in the Newborn Rat Brain.   Frontiers in Endocrinology. Frontiers, Lausanne,  SWITZERLAND, 14: 1090081, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527871/OShaughnessyetalScienceHub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OShaughnessyetalScienceHub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1527871",
             "keyword": [
@@ -182770,21 +182774,10 @@
                 "children's health",
                 "developmental neurotoxicity"
             ],
-            "contactPoint": {
-                "fn": "Katherine O'Shaughnessy",
-                "hasEmail": "mailto:oshaughnessy.katie@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "OShaughnessyetalScienceHub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527871/OShaughnessyetalScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-17",
-            "references": [
-                "https://doi.org/10.3389/fendo.2023.1090081",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9950412"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182794,53 +182787,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fendo.2023.1090081",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9950412"
+            ],
+            "rights": null,
+            "title": "Data for \"Thyroid Hormone Action Controls Multiple Components of Cell Junctions at the Ventricular Zone in the Newborn Rat Brain\""
         },
         {
-            "title": "Male Fathead Minnow Transcriptomes and Associated Chemical Analytes in Milwaukee Estuary System",
-            "description": "This dataset presents the full hepatic transcriptomes of fathead minnows (Pimephales promelas) caged for four days at multiple sites within the Milwaukee Estuary area of concern and additional control sites. At these same sites over the same period of exposure, time integrated water samples were collected and assessed for the presence of over 170 relevant chemical analytes. Access to both full sequencing of fish samples as well as water contaminant data will allow others to explore the health of these ecosystems. \n\nThis dataset is associated with the following publication:\nGarcia-Reyero, N., M. Arick II, A. Woolard, M. Wilbanks, J. Mylroie, K. Jensen, M. Kahl, D. Feifarek, S. Poole, E. Randolph, J. Cavallin, B. Blackwell, D. Villeneuve, G. Ankley, and E. Perkins. Male fathead minnow transcriptomes and associated chemical analytes in the Milwaukee estuary system.   Scientific Data. Springer Nature, New York, NY, USA, 9: 476, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1518645",
-            "keyword": [
-                "fathead minnow",
-                "transcriptome",
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
+            "description": "This dataset presents the full hepatic transcriptomes of fathead minnows (Pimephales promelas) caged for four days at multiple sites within the Milwaukee Estuary area of concern and additional control sites. At these same sites over the same period of exposure, time integrated water samples were collected and assessed for the presence of over 170 relevant chemical analytes. Access to both full sequencing of fish samples as well as water contaminant data will allow others to explore the health of these ecosystems. \n\nThis dataset is associated with the following publication:\nGarcia-Reyero, N., M. Arick II, A. Woolard, M. Wilbanks, J. Mylroie, K. Jensen, M. Kahl, D. Feifarek, S. Poole, E. Randolph, J. Cavallin, B. Blackwell, D. Villeneuve, G. Ankley, and E. Perkins. Male fathead minnow transcriptomes and associated chemical analytes in the Milwaukee estuary system.   Scientific Data. Springer Nature, New York, NY, USA, 9: 476, (2022).",
             "distribution": [
                 {
-                    "title": "GLTED Milwaukee 2017 Fish Collection Data (Woolard et al).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518645/GLTED%20Milwaukee%202017%20Fish%20Collection%20Data%20%28Woolard%20et%20al%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GLTED Milwaukee 2017 Fish Collection Data (Woolard et al).xlsx"
                 },
                 {
-                    "title": "https://zenodo.org/record/3608341#.XqsTrGhKjcs",
-                    "accessURL": "https://zenodo.org/record/3608341#.XqsTrGhKjcs"
+                    "accessURL": "https://zenodo.org/record/3608341#.XqsTrGhKjcs",
+                    "title": "https://zenodo.org/record/3608341#.XqsTrGhKjcs"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE144301",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE144301"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE144301",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE144301"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1518645",
+            "keyword": [
+                "fathead minnow",
+                "transcriptome",
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "endocrine disruption",
+                "screening and prioritization",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-04-30",
-            "references": [
-                "https://doi.org/10.1038/s41597-022-01553-6",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9352792"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182850,138 +182843,139 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41597-022-01553-6",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9352792"
+            ],
+            "rights": null,
+            "title": "Male Fathead Minnow Transcriptomes and Associated Chemical Analytes in Milwaukee Estuary System"
         },
         {
-            "title": "Results of CAMx photochemical air quality model simulations",
-            "description": "The Western States Air Partnership and their consultant Ramboll Corporation perform photochemical air quality modeling simulations to evaluate emissions sources that contribute to regional haze at Class I areas.  Complete model input and output datasets (many terrabytes of data on hard drives) are available through the Intermountain West Data Warehouse.  A summary of the key modeling results used in the publications is included in a spreadsheet. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529609",
-            "keyword": [
-                "Regional Haze",
-                "Anthropogenic Visibility Impairment",
-                "source apportionment",
-                "photochemical modeling"
-            ],
             "contactPoint": {
                 "fn": "Gail Tonnesen",
                 "hasEmail": "mailto:tonnesen.gail@epa.gov"
             },
+            "description": "The Western States Air Partnership and their consultant Ramboll Corporation perform photochemical air quality modeling simulations to evaluate emissions sources that contribute to regional haze at Class I areas.  Complete model input and output datasets (many terrabytes of data on hard drives) are available through the Intermountain West Data Warehouse.  A summary of the key modeling results used in the publications is included in a spreadsheet. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://views.cira.colostate.edu/tssv2/Express/ModelingTools.aspx",
-                    "accessURL": "https://views.cira.colostate.edu/tssv2/Express/ModelingTools.aspx"
+                    "accessURL": "https://views.cira.colostate.edu/tssv2/Express/ModelingTools.aspx",
+                    "title": "https://views.cira.colostate.edu/tssv2/Express/ModelingTools.aspx"
                 },
                 {
-                    "title": "12WUS2_barchart_worst_MID_extinction_v2_20200218_addDec31.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529609/12WUS2_barchart_worst_MID_extinction_v2_20200218_addDec31.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "12WUS2_barchart_worst_MID_extinction_v2_20200218_addDec31.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529609",
+            "keyword": [
+                "Regional Haze",
+                "Anthropogenic Visibility Impairment",
+                "source apportionment",
+                "photochemical modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-04-07",
-            "references": [
-                "https://dx.doi.org/10.1080/10962247.2022.2126556"
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
+                "https://dx.doi.org/10.1080/10962247.2022.2126556"
+            ],
+            "rights": null,
+            "title": "Results of CAMx photochemical air quality model simulations"
         },
         {
-            "title": "supporting data for publication",
-            "description": "The xcel spreadsheet includes results of photochemical model simulations of regional haze that were used to develop the tables and figures included in the publication. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529593",
-            "keyword": [
-                "Visibility",
-                "Regional Haze",
-                "IMPROVE",
-                "particulates",
-                "Western US wildfires"
-            ],
             "contactPoint": {
                 "fn": "Gail Tonnesen",
                 "hasEmail": "mailto:tonnesen.gail@epa.gov"
             },
+            "description": "The xcel spreadsheet includes results of photochemical model simulations of regional haze that were used to develop the tables and figures included in the publication. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://views.cira.colostate.edu/iwdw/RequestData/Default.aspx",
-                    "accessURL": "https://views.cira.colostate.edu/iwdw/RequestData/Default.aspx"
+                    "accessURL": "https://views.cira.colostate.edu/iwdw/RequestData/Default.aspx",
+                    "title": "https://views.cira.colostate.edu/iwdw/RequestData/Default.aspx"
                 },
                 {
-                    "title": "12WUS2_barchart_worst_MID_extinction_v2_20200218_addDec31.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529593/12WUS2_barchart_worst_MID_extinction_v2_20200218_addDec31.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "12WUS2_barchart_worst_MID_extinction_v2_20200218_addDec31.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529593",
+            "keyword": [
+                "Visibility",
+                "Regional Haze",
+                "IMPROVE",
+                "particulates",
+                "Western US wildfires"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2020-04-17",
-            "references": [
-                "https://dx.doi.org/10.1080/10962247.2022.2131653"
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
+                "https://dx.doi.org/10.1080/10962247.2022.2131653"
+            ],
+            "rights": null,
+            "title": "supporting data for publication"
         },
         {
-            "title": "ToxCast data and SeqAPASS results related to case study chemicals and targets referenced in Leveraging New Approach Methodologies to Complement Aquatic Life Criteria Derivation",
-            "description": "Excel file containing ToxCast bioactivity data for carbaryl, celecoxib, chromium triacetate,  HgCl2, nonylphenol, pentachlorophenol, PFOA, PFOS, pioglitazone, sodium dichromate, TCDD.\nThe .zip file contains SeqAPASS results for multiple protein targets. \n\nThis dataset is associated with the following publication:\nSchaupp, C., C. Lalone, B. Blackwell, G. Ankley, and D. Villeneuve. Leveraging ToxCast data and protein sequence conservation to complement aquatic life criteria derivation.   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 19(1): 224-238, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1524425",
-            "keyword": [
-                "aquatic life criteria",
-                "Adverse Outcome Pathways (AOPs)",
-                "ToxCast",
-                "New Approach Methods (Alternatives to Animal Testi",
-                "new approach methodologies"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Excel file containing ToxCast bioactivity data for carbaryl, celecoxib, chromium triacetate,  HgCl2, nonylphenol, pentachlorophenol, PFOA, PFOS, pioglitazone, sodium dichromate, TCDD.\nThe .zip file contains SeqAPASS results for multiple protein targets. \n\nThis dataset is associated with the following publication:\nSchaupp, C., C. Lalone, B. Blackwell, G. Ankley, and D. Villeneuve. Leveraging ToxCast data and protein sequence conservation to complement aquatic life criteria derivation.   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 19(1): 224-238, (2023).",
             "distribution": [
                 {
-                    "title": "OW NAMs_SeqAPASS Data for Science Hub.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524425/OW%20NAMs_SeqAPASS%20Data%20for%20Science%20Hub.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "OW NAMs_SeqAPASS Data for Science Hub.zip"
                 },
                 {
-                    "title": "OW NAMs Case Study_ToxCast Data for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524425/OW%20NAMs%20Case%20Study_ToxCast%20Data%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OW NAMs Case Study_ToxCast Data for Science Hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1524425",
+            "keyword": [
+                "aquatic life criteria",
+                "Adverse Outcome Pathways (AOPs)",
+                "ToxCast",
+                "New Approach Methods (Alternatives to Animal Testi",
+                "new approach methodologies"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-12-06",
-            "references": [
-                "https://doi.org/10.1002/ieam.4617"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -182991,41 +182985,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/ieam.4617"
+            ],
+            "rights": null,
+            "title": "ToxCast data and SeqAPASS results related to case study chemicals and targets referenced in Leveraging New Approach Methodologies to Complement Aquatic Life Criteria Derivation"
         },
         {
-            "title": "Dataset of Biota-Sediment Accumulation Factors for PFAS, Version 1",
-            "description": "The file is a compilation of reported Biota-Sediment Accumulation Factors (BSAFs) for PFAS for aquatic species.  The file has the BSAFs as reported in the source and then, adjusted to units of kg-OC/kg-ww.  File also contains location information (where the measurement was done), an evaluation of its study quality, citation, number of samples used in determining the BSAF, complete taxonomic information, kinetic information when available, and when available, concentrations in the sediment and organism used to determine the BSAF. \n\nThis dataset is associated with the following publication:\nBurkhard, L., and L. Votava. Biota-Sediment Accumulation Factors for Per- and Polyfluoroalkyl Substances.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 277-295, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1524668",
-            "keyword": [
-                "bioaccumulation",
-                "PFAS",
-                "BSAF",
-                "bioconcentration"
-            ],
             "contactPoint": {
                 "fn": "Lawrence Burkhard",
                 "hasEmail": "mailto:burkhard.lawrence@epa.gov"
             },
+            "description": "The file is a compilation of reported Biota-Sediment Accumulation Factors (BSAFs) for PFAS for aquatic species.  The file has the BSAFs as reported in the source and then, adjusted to units of kg-OC/kg-ww.  File also contains location information (where the measurement was done), an evaluation of its study quality, citation, number of samples used in determining the BSAF, complete taxonomic information, kinetic information when available, and when available, concentrations in the sediment and organism used to determine the BSAF. \n\nThis dataset is associated with the following publication:\nBurkhard, L., and L. Votava. Biota-Sediment Accumulation Factors for Per- and Polyfluoroalkyl Substances.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 277-295, (2022).",
             "distribution": [
                 {
-                    "title": "PFAS_BSAF_DATA_(2).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524668/PFAS_BSAF_DATA_%282%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PFAS_BSAF_DATA_(2).xlsx"
                 }
             ],
-            "modified": "2021-12-21",
-            "references": [
-                "https://doi.org/10.1002/etc.5526"
+            "identifier": "https://doi.org/10.23719/1524668",
+            "keyword": [
+                "bioaccumulation",
+                "PFAS",
+                "BSAF",
+                "bioconcentration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
+            "modified": "2021-12-21",
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183035,41 +183029,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5526"
+            ],
+            "rights": null,
+            "title": "Dataset of Biota-Sediment Accumulation Factors for PFAS, Version 1"
         },
         {
-            "title": "Impact of Filter Material and Holding Time on Spore Sampling Efficiency in Water",
-            "description": "Complete dataset for \"Impact of Filter Material and Holding Time on Spore Sampling Efficiency in Water\". \n\nThis dataset is associated with the following publication:\nRatliff, K., A. Abdel-Hady, M. Monge, A. Mikelonis, and A. Touati. Impact of Filter Material and Holding Time on Spore Sampling Efficiency in Water.   Letters in Applied Microbiology. Blackwell Publishing, Malden, MA, USA, 76(2): ovad005, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527803",
-            "keyword": [
-                "Bacillus anthracis",
-                "eDNA",
-                "filter sampling",
-                "remediation"
-            ],
             "contactPoint": {
                 "fn": "Katherine Ratliff",
                 "hasEmail": "mailto:ratliff.katherine@epa.gov"
             },
+            "description": "Complete dataset for \"Impact of Filter Material and Holding Time on Spore Sampling Efficiency in Water\". \n\nThis dataset is associated with the following publication:\nRatliff, K., A. Abdel-Hady, M. Monge, A. Mikelonis, and A. Touati. Impact of Filter Material and Holding Time on Spore Sampling Efficiency in Water.   Letters in Applied Microbiology. Blackwell Publishing, Malden, MA, USA, 76(2): ovad005, (2023).",
             "distribution": [
                 {
-                    "title": "filter sample manuscript data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527803/filter%20sample%20manuscript%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "filter sample manuscript data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527803",
+            "keyword": [
+                "Bacillus anthracis",
+                "eDNA",
+                "filter sampling",
+                "remediation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-03",
-            "references": [
-                "https://doi.org/10.1093/lambio/ovad005"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183079,55 +183073,57 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/lambio/ovad005"
+            ],
+            "rights": null,
+            "title": "Impact of Filter Material and Holding Time on Spore Sampling Efficiency in Water"
         },
         {
-            "title": "PFNA mouse body weight",
-            "description": "Body weight of mice exposed to PFNA.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529407",
-            "keyword": [
-                "Mouse Model",
-                "PFNA",
-                "Human Health Risk",
-                "in vivo"
-            ],
             "contactPoint": {
                 "fn": "Christopher Lau",
                 "hasEmail": "mailto:lau.christopher@epa.gov"
             },
+            "description": "Body weight of mice exposed to PFNA.",
             "distribution": [
                 {
-                    "title": "Wolf et al 2010 PFNA_PPARa.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529407/Wolf%20et%20al%202010%20PFNA_PPARa.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Wolf et al 2010 PFNA_PPARa.xlsx"
                 },
                 {
-                    "title": "Rogers et al 2014_LTE- Postnatal BW Males Stats Ctrls combined.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529407/Rogers%20et%20al%202014_LTE-%20Postnatal%20BW%20Males%20Stats%20Ctrls%20combined.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rogers et al 2014_LTE- Postnatal BW Males Stats Ctrls combined.xls"
                 },
                 {
-                    "title": "Rogers et al 2014_LTE- Postnatal BW Females Stats Ctrls combined.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529407/Rogers%20et%20al%202014_LTE-%20Postnatal%20BW%20Females%20Stats%20Ctrls%20combined.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rogers et al 2014_LTE- Postnatal BW Females Stats Ctrls combined.xls"
                 },
                 {
-                    "title": "Das et al 2015 Developmental PFNA data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529407/Das%20et%20al%202015%20Developmental%20PFNA%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Das et al 2015 Developmental PFNA data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529407",
+            "keyword": [
+                "Mouse Model",
+                "PFNA",
+                "Human Health Risk",
+                "in vivo"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-06",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -183136,48 +183132,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "PFNA mouse body weight"
         },
         {
-            "title": "Data and code for Olson et al. Wildfires in the western United States are mobilizing PM2.5-associated nutrients and may be contributing to downwind cyanobacteria blooms",
-            "description": "Data and code for Olson et al. Wildfires in the western United States are mobilizing PM2.5-associated nutrients and may be contributing to downwind cyanobacteria blooms. \n\nThis dataset is associated with the following publication:\nOlson, N., K. Boaggio, R. Rice, K. Foley, and S. Leduc. Wildfires in the western United States are mobilizing PM2.5-associated nutrients and may be contributing to downwind cyanobacteria blooms.   Environmental Science: Processes & Impacts. Royal Society of Chemistry, Cambridge,  UK, 25: 1049-1066, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529004",
-            "keyword": [
-                "fire",
-                "cyanobacteria",
-                "water quality",
-                "air quality",
-                "Nitrogen and Co-pollutants",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Nicole Olson",
                 "hasEmail": "mailto:olson.nicole@epa.gov"
             },
+            "description": "Data and code for Olson et al. Wildfires in the western United States are mobilizing PM2.5-associated nutrients and may be contributing to downwind cyanobacteria blooms. \n\nThis dataset is associated with the following publication:\nOlson, N., K. Boaggio, R. Rice, K. Foley, and S. Leduc. Wildfires in the western United States are mobilizing PM2.5-associated nutrients and may be contributing to downwind cyanobacteria blooms.   Environmental Science: Processes & Impacts. Royal Society of Chemistry, Cambridge,  UK, 25: 1049-1066, (2023).",
             "distribution": [
                 {
-                    "title": "Description of data and files for Olson et al.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529004/Description%20of%20data%20and%20files%20for%20Olson%20et%20al.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Description of data and files for Olson et al.docx"
                 },
                 {
-                    "title": "Code files for Olson et al.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529004/Code%20files%20for%20Olson%20et%20al.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Code files for Olson et al.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529004",
+            "keyword": [
+                "fire",
+                "cyanobacteria",
+                "water quality",
+                "air quality",
+                "Nitrogen and Co-pollutants",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-24",
-            "references": [
-                "https://doi.org/10.1039/d3em00042g"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183187,19 +183181,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d3em00042g"
+            ],
+            "rights": null,
+            "title": "Data and code for Olson et al. Wildfires in the western United States are mobilizing PM2.5-associated nutrients and may be contributing to downwind cyanobacteria blooms"
         },
         {
-            "title": "SARS-CoV-2 Disinfection Manuscript Data - Task 4A",
-            "description": "Testing data, efficacy evaluations (recovery, log10 reductions, tissue culture assay results, etc). Common disinfectants were evaluated for efficacy against SARS-CoV-2 on common surfaces. \n\nThis dataset is associated with the following publication:\nHardison, R.L., S.W. Nelson, R. Limmer, J. Marx, B.M. Taylor, R.R. James, M.J. Stewart, S. Lee, M. Calfee, S. Ryan, and M. Howard. Efficacy of Chemical Disinfectants Against SARS-CoV-2 on High-Touch Surface Materials.   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 134(1): lxac020, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Michael Calfee",
+                "hasEmail": "mailto:calfee.worth@epa.gov"
+            },
+            "description": "Testing data, efficacy evaluations (recovery, log10 reductions, tissue culture assay results, etc). Common disinfectants were evaluated for efficacy against SARS-CoV-2 on common surfaces. \n\nThis dataset is associated with the following publication:\nHardison, R.L., S.W. Nelson, R. Limmer, J. Marx, B.M. Taylor, R.R. James, M.J. Stewart, S. Lee, M. Calfee, S. Ryan, and M. Howard. Efficacy of Chemical Disinfectants Against SARS-CoV-2 on High-Touch Surface Materials.   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 134(1): lxac020, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527804/Summary%20Data%20for%204A%20SARS.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Summary Data for 4A SARS.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1527804",
             "keyword": [
@@ -183211,20 +183215,10 @@
                 "public health",
                 "analytical method"
             ],
-            "contactPoint": {
-                "fn": "Michael Calfee",
-                "hasEmail": "mailto:calfee.worth@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Summary Data for 4A SARS.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527804/Summary%20Data%20for%204A%20SARS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-07-27",
-            "references": [
-                "https://doi.org/10.1093/jambio/lxac020"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183234,42 +183228,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/jambio/lxac020"
+            ],
+            "rights": null,
+            "title": "SARS-CoV-2 Disinfection Manuscript Data - Task 4A"
         },
         {
-            "title": "Gestational Exposure to Perchlorate in the rat: Thyroid Hormones in Fetal Thyroid Gland, Serum, and Brain",
-            "description": "This dataset contains results from rodent study. Thyroid hormones and brain endpoints are reported for pregnant rat dams and progeny on gestational day 20 following drinking water exposure to the dams. Several dose levels were examined. \n\nThis dataset is associated with the following publication:\nGilbert, M., I. Hassan, C. Wood, K. O'Shaughnessy, S. Spring, S. Thomas, and J. Ford. Gestational Exposure to Perchlorate in the rat: Thyroid Hormones in Fetal Thyroid Gland, Serum, and Brain.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  188(1): 117-130, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529598",
-            "keyword": [
-                "thyroid",
-                "in vivo",
-                "Children's Environmental Health",
-                "developmental neurotoxicity",
-                "Adverse Outcome Pathways (AOPs)"
-            ],
             "contactPoint": {
                 "fn": "Mary Gilbert",
                 "hasEmail": "mailto:gilbert.mary@epa.gov"
             },
+            "description": "This dataset contains results from rodent study. Thyroid hormones and brain endpoints are reported for pregnant rat dams and progeny on gestational day 20 following drinking water exposure to the dams. Several dose levels were examined. \n\nThis dataset is associated with the following publication:\nGilbert, M., I. Hassan, C. Wood, K. O'Shaughnessy, S. Spring, S. Thomas, and J. Ford. Gestational Exposure to Perchlorate in the rat: Thyroid Hormones in Fetal Thyroid Gland, Serum, and Brain.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  188(1): 117-130, (2022).",
             "distribution": [
                 {
-                    "title": "M0516 ScienceHub Files.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529598/M0516%20ScienceHub%20Files.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "M0516 ScienceHub Files.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529598",
+            "keyword": [
+                "thyroid",
+                "in vivo",
+                "Children's Environmental Health",
+                "developmental neurotoxicity",
+                "Adverse Outcome Pathways (AOPs)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-03-14",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfac038"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183279,19 +183273,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfac038"
+            ],
+            "rights": null,
+            "title": "Gestational Exposure to Perchlorate in the rat: Thyroid Hormones in Fetal Thyroid Gland, Serum, and Brain"
         },
         {
-            "title": "National Lakes Assessment 2012 Datafiles for Report \u201cNational Lakes Assessment 2012: A collaborative survey of lakes in the United States\"",
-            "description": "National Lakes Assessment 2012 Datafiles for Report \u201cNational Lakes Assessment 2012: A Collaborative Survey of lakes in the United States\u201d: The National Lakes Assessment (NLA) is a statistical survey of the condition of our nation's lakes, ponds, and reservoirs. It is designed to provide information on the extent of lakes that support healthy biological condition and recreation, estimate how widespread major stressors are that impact lake quality, and provide insight into whether lakes nationwide are getting cleaner. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NLA 2012 report. Sampling was conducted in the summer of 2012 at approximately 1000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic macroinvertebrates, physical habitat, landscape metrics, phytoplankton data, secchi depth, data, tropic status, zooplankton, etc. Users are encouraged to visit the NARS data webpage for updates to data files (e.g., for example updated zooplankton files) and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys \n\nCitation for the NLA 2012 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Lakes Assessment 2012 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/national-results-and-regional-highlights-national-lakes. DOI: 10.23719/1529584 \n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Lakes Assessment 2012 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d \n\nAdditional information: NLA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Lareina Guenzel",
+                "hasEmail": "mailto:guenzel.lareina@epa.gov"
+            },
+            "description": "National Lakes Assessment 2012 Datafiles for Report \u201cNational Lakes Assessment 2012: A Collaborative Survey of lakes in the United States\u201d: The National Lakes Assessment (NLA) is a statistical survey of the condition of our nation's lakes, ponds, and reservoirs. It is designed to provide information on the extent of lakes that support healthy biological condition and recreation, estimate how widespread major stressors are that impact lake quality, and provide insight into whether lakes nationwide are getting cleaner. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NLA 2012 report. Sampling was conducted in the summer of 2012 at approximately 1000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic macroinvertebrates, physical habitat, landscape metrics, phytoplankton data, secchi depth, data, tropic status, zooplankton, etc. Users are encouraged to visit the NARS data webpage for updates to data files (e.g., for example updated zooplankton files) and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys \n\nCitation for the NLA 2012 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Lakes Assessment 2012 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/national-results-and-regional-highlights-national-lakes. DOI: 10.23719/1529584 \n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Lakes Assessment 2012 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d \n\nAdditional information: NLA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/national-results-and-regional-highlights-national-lakes",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/national-results-and-regional-highlights-national-lakes"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529584",
             "keyword": [
@@ -183310,36 +183313,36 @@
                 "biological",
                 "assessment"
             ],
-            "contactPoint": {
-                "fn": "Lareina Guenzel",
-                "hasEmail": "mailto:guenzel.lareina@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/national-results-and-regional-highlights-national-lakes",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/national-results-and-regional-highlights-national-lakes"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-02-23",
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
+            "title": "National Lakes Assessment 2012 Datafiles for Report \u201cNational Lakes Assessment 2012: A collaborative survey of lakes in the United States\""
         },
         {
-            "title": "National Lakes Assessment 2017 Datafiles for Report \u201cNational Lakes Assessment 2017:  The third collaborative survey of lakes in the United States\"",
-            "description": "The National Lakes Assessment (NLA) is a statistical survey of the condition of our nation's lakes, ponds, and reservoirs. It is designed to provide information on the extent of lakes that support healthy biological condition and recreation, estimate how widespread major stressors are that impact lake quality, and provide insight into whether lakes nationwide are getting cleaner. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NLA 2017 report. Sampling was conducted in the summer of 2017 at approximately 1000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic macroinvertebrates, physical habitat, landscape metrics, phytoplankton data, secchi depth, data, tropic status, zooplankton, etc. Users are encouraged to visit the NARS data webpage for updates to data files (e.g., for example updated zooplankton files) and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys \n\nCitation for the NLA 2017 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Lakes Assessment 2017 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-lakes-assessment-2017. DOI: 10.23719/1529585 \n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Lakes Assessment 2017 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d \n\nAdditional information: NLA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Lareina Guenzel",
+                "hasEmail": "mailto:guenzel.lareina@epa.gov"
+            },
+            "description": "The National Lakes Assessment (NLA) is a statistical survey of the condition of our nation's lakes, ponds, and reservoirs. It is designed to provide information on the extent of lakes that support healthy biological condition and recreation, estimate how widespread major stressors are that impact lake quality, and provide insight into whether lakes nationwide are getting cleaner. \n\nThis dataset is an archived (zipped) file comprised of chemical, physical and biological files used in developing the NLA 2017 report. Sampling was conducted in the summer of 2017 at approximately 1000 sites in the conterminous U.S. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic macroinvertebrates, physical habitat, landscape metrics, phytoplankton data, secchi depth, data, tropic status, zooplankton, etc. Users are encouraged to visit the NARS data webpage for updates to data files (e.g., for example updated zooplankton files) and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys \n\nCitation for the NLA 2017 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Lakes Assessment 2017 Report. Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-lakes-assessment-2017. DOI: 10.23719/1529585 \n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Lakes Assessment 2017 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d \n\nAdditional information: NLA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-lakes-assessment-2017",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-lakes-assessment-2017"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529585",
             "keyword": [
@@ -183358,64 +183361,54 @@
                 "Tribes",
                 "EPA"
             ],
-            "contactPoint": {
-                "fn": "Lareina Guenzel",
-                "hasEmail": "mailto:guenzel.lareina@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-lakes-assessment-2017",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-lakes-assessment-2017"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-07-05",
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
+            "title": "National Lakes Assessment 2017 Datafiles for Report \u201cNational Lakes Assessment 2017:  The third collaborative survey of lakes in the United States\""
         },
         {
-            "title": "Risk-Based Prioritization of Organic Chemicals and Locations of Ecological Concern in Sediment From Great Lakes Tributaries",
-            "description": "Data from \"Baldwin AK, Corsi SR, Stefaniak OM, Loken LC, Villeneuve DL, Ankley GT, Blackwell BR, Lenaker PL, Nott MA, Mills MA. Risk-Based Prioritization of Organic Chemicals and Locations of Ecological Concern in Sediment From Great Lakes Tributaries. Environ Toxicol Chem. 2022 Apr;41(4):1016-1041. doi: 10.1002/etc.5286. Epub 2022 Feb 28. PMID: 35170813; PMCID: PMC9306483.\". \n\nThis dataset is associated with the following publication:\nBaldwin, A., S. Corsi, O. Stefaniak, L. Loken, D. Villeneuve, G. Ankley, B. Blackwell, P. Lenaker, M. Nott, and M. Mills. Risk-Based Prioritization of Organic Chemicals and Locations of Ecological Concern in Sediment From Great Lakes Tributaries.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(4): 1016-1041, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529752",
-            "keyword": [
-                "sediment",
-                "prioritization",
-                "Great Lakes Restoration Initiative",
-                "chemical mixtures"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Data from \"Baldwin AK, Corsi SR, Stefaniak OM, Loken LC, Villeneuve DL, Ankley GT, Blackwell BR, Lenaker PL, Nott MA, Mills MA. Risk-Based Prioritization of Organic Chemicals and Locations of Ecological Concern in Sediment From Great Lakes Tributaries. Environ Toxicol Chem. 2022 Apr;41(4):1016-1041. doi: 10.1002/etc.5286. Epub 2022 Feb 28. PMID: 35170813; PMCID: PMC9306483.\". \n\nThis dataset is associated with the following publication:\nBaldwin, A., S. Corsi, O. Stefaniak, L. Loken, D. Villeneuve, G. Ankley, B. Blackwell, P. Lenaker, M. Nott, and M. Mills. Risk-Based Prioritization of Organic Chemicals and Locations of Ecological Concern in Sediment From Great Lakes Tributaries.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(4): 1016-1041, (2022).",
             "distribution": [
                 {
-                    "title": "Supporting Information 1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529752/Supporting%20Information%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supporting Information 1.xlsx"
                 },
                 {
-                    "title": "Supporting Information 2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529752/Supporting%20Information%202.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supporting Information 2.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529752",
+            "keyword": [
+                "sediment",
+                "prioritization",
+                "Great Lakes Restoration Initiative",
+                "chemical mixtures"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2021-12-31",
-            "references": [
-                "https://doi.org/10.1002/etc.5286",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9306483"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183425,101 +183418,101 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5286",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9306483"
+            ],
+            "rights": null,
+            "title": "Risk-Based Prioritization of Organic Chemicals and Locations of Ecological Concern in Sediment From Great Lakes Tributaries"
         },
         {
-            "title": "Predicting nonlinear relationships between external and internal concentrations with physiologically based pharmacokinetic modeling",
-            "description": "Generic physiologically-based pharmacokinetic (PBPK) models were used to explore how saturable absorption or clearance can influence the shape of the internal to external concentration (IEC) relationship. The models were used for hypothetical chemicals to show how differences in kinetic parameters can impact the shape of an IEC relationship; and the models for styrene and caffeine were used to explore how exposure route, frequency, and duration impact the IEC relationships in rat and human exposures. We also analyzed available plasma concentration data for 2,4-dichlorophenoxyacetic acid (data from Saghir et al. 2013; https://doi.org/10.1093/toxsci/kft212) to demonstrate how a PBPK modeling approach can be an alternative to common statistical methods for analyzing dose proportionality. \n\nThese files contain the model code and utilized parameters for each of these case studies as well as a link to the publicly available dataset from Saghir et al. 2013 (https://doi.org/10.1093/toxsci/kft212). Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529607",
-            "keyword": [
-                "Physiologically based pharmacokinetic (PBPK)",
-                "animal study design",
-                "internal concentrations",
-                "nonlinear pharmacokinetics",
-                "saturation of absorption",
-                "saturation of clearance"
-            ],
             "contactPoint": {
                 "fn": "Daniel Hoer",
                 "hasEmail": "mailto:hoer.daniel@epa.gov"
             },
+            "description": "Generic physiologically-based pharmacokinetic (PBPK) models were used to explore how saturable absorption or clearance can influence the shape of the internal to external concentration (IEC) relationship. The models were used for hypothetical chemicals to show how differences in kinetic parameters can impact the shape of an IEC relationship; and the models for styrene and caffeine were used to explore how exposure route, frequency, and duration impact the IEC relationships in rat and human exposures. We also analyzed available plasma concentration data for 2,4-dichlorophenoxyacetic acid (data from Saghir et al. 2013; https://doi.org/10.1093/toxsci/kft212) to demonstrate how a PBPK modeling approach can be an alternative to common statistical methods for analyzing dose proportionality. \n\nThese files contain the model code and utilized parameters for each of these case studies as well as a link to the publicly available dataset from Saghir et al. 2013 (https://doi.org/10.1093/toxsci/kft212). Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/toxsci/136/2/10.1093_toxsci_kft212/4/kft212_Supplementary_Data.zip?Expires=1698755797&Signature=xThd-p7pMZ9vu6ZMkJ1zQmnpH8l9kkbA04m0BU0wjWqwvL4ozIB73GqDwSmhPW6i2bFUoN5EKUSUbNV5QDkk0Sonp4Ar-3cexfZfiFd3d~iYBqKAWWpe~Twu2C50wbSL7VJ3B6iwwsAvtzWy0jIDJxxEpbWMeEfUqcB9gHeC9gWnJBnbz6Pntf~C5qL8A449LeDrpJXwtzdPzYY9ZMWImUKCtgyB3RQl10-rOVO4htqtqQHuzpR5Wy9vcVb7d5POEWuIPtqW7NN~DeLCiJ~y8jTS0Hpir8TM~biTh1KzA-sXEiRcsrxLw5Hpy4umJb3sqA2lGYNp1nAqIRA0QUkeTw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA",
-                    "accessURL": "https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/toxsci/136/2/10.1093_toxsci_kft212/4/kft212_Supplementary_Data.zip?Expires=1698755797&Signature=xThd-p7pMZ9vu6ZMkJ1zQmnpH8l9kkbA04m0BU0wjWqwvL4ozIB73GqDwSmhPW6i2bFUoN5EKUSUbNV5QDkk0Sonp4Ar-3cexfZfiFd3d~iYBqKAWWpe~Twu2C50wbSL7VJ3B6iwwsAvtzWy0jIDJxxEpbWMeEfUqcB9gHeC9gWnJBnbz6Pntf~C5qL8A449LeDrpJXwtzdPzYY9ZMWImUKCtgyB3RQl10-rOVO4htqtqQHuzpR5Wy9vcVb7d5POEWuIPtqW7NN~DeLCiJ~y8jTS0Hpir8TM~biTh1KzA-sXEiRcsrxLw5Hpy4umJb3sqA2lGYNp1nAqIRA0QUkeTw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"
+                    "accessURL": "https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/toxsci/136/2/10.1093_toxsci_kft212/4/kft212_Supplementary_Data.zip?Expires=1698755797&Signature=xThd-p7pMZ9vu6ZMkJ1zQmnpH8l9kkbA04m0BU0wjWqwvL4ozIB73GqDwSmhPW6i2bFUoN5EKUSUbNV5QDkk0Sonp4Ar-3cexfZfiFd3d~iYBqKAWWpe~Twu2C50wbSL7VJ3B6iwwsAvtzWy0jIDJxxEpbWMeEfUqcB9gHeC9gWnJBnbz6Pntf~C5qL8A449LeDrpJXwtzdPzYY9ZMWImUKCtgyB3RQl10-rOVO4htqtqQHuzpR5Wy9vcVb7d5POEWuIPtqW7NN~DeLCiJ~y8jTS0Hpir8TM~biTh1KzA-sXEiRcsrxLw5Hpy4umJb3sqA2lGYNp1nAqIRA0QUkeTw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA",
+                    "title": "https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/toxsci/136/2/10.1093_toxsci_kft212/4/kft212_Supplementary_Data.zip?Expires=1698755797&Signature=xThd-p7pMZ9vu6ZMkJ1zQmnpH8l9kkbA04m0BU0wjWqwvL4ozIB73GqDwSmhPW6i2bFUoN5EKUSUbNV5QDkk0Sonp4Ar-3cexfZfiFd3d~iYBqKAWWpe~Twu2C50wbSL7VJ3B6iwwsAvtzWy0jIDJxxEpbWMeEfUqcB9gHeC9gWnJBnbz6Pntf~C5qL8A449LeDrpJXwtzdPzYY9ZMWImUKCtgyB3RQl10-rOVO4htqtqQHuzpR5Wy9vcVb7d5POEWuIPtqW7NN~DeLCiJ~y8jTS0Hpir8TM~biTh1KzA-sXEiRcsrxLw5Hpy4umJb3sqA2lGYNp1nAqIRA0QUkeTw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"
                 },
                 {
-                    "title": "Supplemental_materials_18Jan2022.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529607/Supplemental_materials_18Jan2022.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplemental_materials_18Jan2022.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529607",
+            "keyword": [
+                "Physiologically based pharmacokinetic (PBPK)",
+                "animal study design",
+                "internal concentrations",
+                "nonlinear pharmacokinetics",
+                "saturation of absorption",
+                "saturation of clearance"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-26",
-            "references": [
-                "https://dx.doi.org/10.1016/j.taap.2022.115922",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10519136"
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
+                "https://dx.doi.org/10.1016/j.taap.2022.115922",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10519136"
+            ],
+            "rights": null,
+            "title": "Predicting nonlinear relationships between external and internal concentrations with physiologically based pharmacokinetic modeling"
         },
         {
-            "title": "Sahle_SDMP_FRAGMENTATION Epoxy-with MWCNT",
-            "description": "Data include changes in aging of weathered materials using optical macroscopy, Raman and FTIR spectroscopy, thermogravimetric analysis and Scanning electron microscopy. The release of fragments and particles were determined using imaging methods. The influence NPs interaction with the polymer matrix on their environmental release has not been well studied. The current paper focuses on some analytical techniques suitable for evaluating the effects of weathering on the detection and characterization of NPs, including Fourier transforms infrared spectroscopy (FT-IR), optical microscopy, contact angle measurements, gravimetric analysis, confocal microscopy, transmission electron microscopy (TEM), scanning electron microscopy (SEM) and Raman spectroscopy. The study also includes the toxicity of released particles and organic compounds. \n\nThis dataset is associated with the following publication:\nSahle-Demessie, E., C. Han, E. Varughese, B. Acrey, and R. Zepp. Fragmentation and release of pristine and functionalized carbon nanotubes from epoxy-nanocomposites during accelerated weathering.   Environmental Science: Nano. Royal Society of Chemistry, Cambridge,  UK, 10(7): 1812-1827, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529756",
-            "keyword": [
-                "Epoxy nanocomposite",
-                "Functionalized CNT",
-                "weathering",
-                "degradation",
-                "Fragment Release",
-                "Toxicity Assessment"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "description": "Data include changes in aging of weathered materials using optical macroscopy, Raman and FTIR spectroscopy, thermogravimetric analysis and Scanning electron microscopy. The release of fragments and particles were determined using imaging methods. The influence NPs interaction with the polymer matrix on their environmental release has not been well studied. The current paper focuses on some analytical techniques suitable for evaluating the effects of weathering on the detection and characterization of NPs, including Fourier transforms infrared spectroscopy (FT-IR), optical microscopy, contact angle measurements, gravimetric analysis, confocal microscopy, transmission electron microscopy (TEM), scanning electron microscopy (SEM) and Raman spectroscopy. The study also includes the toxicity of released particles and organic compounds. \n\nThis dataset is associated with the following publication:\nSahle-Demessie, E., C. Han, E. Varughese, B. Acrey, and R. Zepp. Fragmentation and release of pristine and functionalized carbon nanotubes from epoxy-nanocomposites during accelerated weathering.   Environmental Science: Nano. Royal Society of Chemistry, Cambridge,  UK, 10(7): 1812-1827, (2023).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.1039/D2EN01014C",
-                    "accessURL": "https://doi.org/10.1039/D2EN01014C"
+                    "accessURL": "https://doi.org/10.1039/D2EN01014C",
+                    "title": "https://doi.org/10.1039/D2EN01014C"
                 },
                 {
-                    "title": "Raw Base Sample TGA data.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529756/Raw%20Base%20Sample%20TGA%20data.xls",
-                    "mediaType": "application/x-ole-storage"
+                    "mediaType": "application/x-ole-storage",
+                    "title": "Raw Base Sample TGA data.xls"
                 },
                 {
-                    "title": "Base Project aged TGA data.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529756/Base%20Project%20aged%20TGA%20data.xls",
-                    "mediaType": "application/x-ole-storage"
+                    "mediaType": "application/x-ole-storage",
+                    "title": "Base Project aged TGA data.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529756",
+            "keyword": [
+                "Epoxy nanocomposite",
+                "Functionalized CNT",
+                "weathering",
+                "degradation",
+                "Fragment Release",
+                "Toxicity Assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-08",
-            "references": [
-                "https://doi.org/10.1039/d2en01014c",
-                "https://pasteur.epa.gov/uploads/10.23719/1529756/documents/Composite_Fragmentation_Supplemental%20Information_Final.docx"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183529,20 +183522,25 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d2en01014c",
+                "https://pasteur.epa.gov/uploads/10.23719/1529756/documents/Composite_Fragmentation_Supplemental%20Information_Final.docx"
+            ],
+            "rights": null,
+            "title": "Sahle_SDMP_FRAGMENTATION Epoxy-with MWCNT"
         },
         {
-            "title": "Biodesalination_Supplemental Information",
-            "description": "Data include on the characterization of saline water composition, algal growth, salt sequestration  and changes in water conductivity. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: https://doi.org/10.1016/j.chemosphere.2022.136082. Format: Data collected by Al-Ain University. \n\nThis dataset is associated with the following publication:\nZafar, A.M., M.A. Javed , A.A. Hassan, E. Sahle-Demessie, and S. Harmon. Biodesalination using halophytic cyanobacterium Phormidium keutzingianum from brackish to the hypersaline water.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 307: 136082, (2022).",
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
+                "fn": "Endalkac Sahle-Demessie",
+                "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
+            },
+            "description": "Data include on the characterization of saline water composition, algal growth, salt sequestration  and changes in water conductivity. This dataset is not publicly accessible because: EPA cannot release CBI, or data protected by copyright, patent, or otherwise subject to trade secret restrictions. Request for access to CBI data may be directed to the dataset owner by an authorized person by contacting the party listed. It can be accessed through the following means: https://doi.org/10.1016/j.chemosphere.2022.136082. Format: Data collected by Al-Ain University. \n\nThis dataset is associated with the following publication:\nZafar, A.M., M.A. Javed , A.A. Hassan, E. Sahle-Demessie, and S. Harmon. Biodesalination using halophytic cyanobacterium Phormidium keutzingianum from brackish to the hypersaline water.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 307: 136082, (2022).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529759",
             "keyword": [
                 "salinity",
@@ -183551,14 +183549,10 @@
                 "Biosorption Bioaccumulation",
                 "Biodesalination"
             ],
-            "contactPoint": {
-                "fn": "Endalkac Sahle-Demessie",
-                "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-02-01",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2022.136082"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183568,20 +183562,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2022.136082"
+            ],
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "title": "Biodesalination_Supplemental Information"
         },
         {
-            "title": "GLIMR_viewing",
-            "description": "Code and viewing geometries for computing sun glint, wind speed, sun and satellite position, spatial resolution, signal-to-noise, and hours per day of observation. This dataset is not publicly accessible because: File is in excess of 8GB and is not able to be uploaded. It can be accessed through the following means: Contact the corresponding author Blake Schaeffer at schaeffer.blake@epa.gov. Format: GLIMR's proposed sampling design information. \n\nThis dataset is associated with the following publication:\nSchaeffer, B., P. Whitman, R. Vandermeulen, C. Hu, A. Mannino, J. Salisbury, B. Efremova, R. Conmy, M. Coffer, W. Salls, H. Ferriby, and N. Reynolds. Assessing potential of the Geostationary Littoral Imaging and Monitoring Radiometer (GLIMR) for water quality monitoring across the coastal United States.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 196: 115558, (2023).",
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
+                "fn": "Blake Schaeffer",
+                "hasEmail": "mailto:schaeffer.blake@epa.gov"
+            },
+            "description": "Code and viewing geometries for computing sun glint, wind speed, sun and satellite position, spatial resolution, signal-to-noise, and hours per day of observation. This dataset is not publicly accessible because: File is in excess of 8GB and is not able to be uploaded. It can be accessed through the following means: Contact the corresponding author Blake Schaeffer at schaeffer.blake@epa.gov. Format: GLIMR's proposed sampling design information. \n\nThis dataset is associated with the following publication:\nSchaeffer, B., P. Whitman, R. Vandermeulen, C. Hu, A. Mannino, J. Salisbury, B. Efremova, R. Conmy, M. Coffer, W. Salls, H. Ferriby, and N. Reynolds. Assessing potential of the Geostationary Littoral Imaging and Monitoring Radiometer (GLIMR) for water quality monitoring across the coastal United States.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 196: 115558, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529553",
             "keyword": [
                 "geostationary satellite remote sensing",
@@ -183591,14 +183589,10 @@
                 "monitoring",
                 "oil spill"
             ],
-            "contactPoint": {
-                "fn": "Blake Schaeffer",
-                "hasEmail": "mailto:schaeffer.blake@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-31",
-            "references": [
-                "https://doi.org/10.1016/j.marpolbul.2023.115558"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183608,42 +183602,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.marpolbul.2023.115558"
+            ],
+            "rights": null,
+            "title": "GLIMR_viewing"
         },
         {
-            "title": "RI Mo-DO-N study sampling locations",
-            "description": "Dates and locations where sediment samples were collected and notes of any observations at the time. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529766",
-            "keyword": [
-                "sediments",
-                "Hypoxia",
-                "Rhode Island",
-                "Narragansett Bay"
-            ],
             "contactPoint": {
                 "fn": "Warren Boothman",
                 "hasEmail": "mailto:boothman.warren@epa.gov"
             },
+            "description": "Dates and locations where sediment samples were collected and notes of any observations at the time. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
             "distribution": [
                 {
-                    "title": "RI embayment sampling locations.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529766/RI%20embayment%20sampling%20locations.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "RI embayment sampling locations.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529766",
+            "keyword": [
+                "sediments",
+                "Hypoxia",
+                "Rhode Island",
+                "Narragansett Bay"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-03",
-            "references": [
-                "https://doi.org/10.1007/s12237-023-01215-9",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183653,33 +183646,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12237-023-01215-9",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            ],
+            "rights": null,
+            "title": "RI Mo-DO-N study sampling locations"
         },
         {
-            "title": "Focus group data for factors in homeowners\u2019 willingness to adopt IA systems",
-            "description": "Dataset is a Microsoft Word file that contains the transcripts of five focus groups of adopters and prospective adopters of innovative/alternative septic systems. Focus group participants were asked a series of questions to better understand why they would or would not choose to adopt the alternative and innovative septic systems. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact Kate Mulvaney, mulvaney.kate@epa.gov. Format: This is EPA-owned data, but SDMP was generated post clearance due to pre-RAPID/SciHub integration.\r\n\r\nDataset is a Microsoft Word file that contains the transcripts of five focus groups of adopters and prospective adopters of innovative/alternative septic systems. Focus group participants were asked a series of questions to better understand why they would or would not choose to adopt the alternative and innovative septic systems. \n\nThis dataset is associated with the following publication:\nRudman, A., K. Mulvaney, N. Merrill, and K. Canfield. Factors in homeowners\u2019 willingness to adopt nitrogen-reducing innovative/alternative septic systems.   Frontiers in Marine Science. Frontiers, Lausanne,  SWITZERLAND, 10: 1069599, (2023).",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529608",
-            "keyword": [
-                "innovative septic systems",
-                "innovation adoption"
-            ],
             "contactPoint": {
                 "fn": "Kate Mulvaney",
                 "hasEmail": "mailto:mulvaney.kate@epa.gov"
             },
+            "description": "Dataset is a Microsoft Word file that contains the transcripts of five focus groups of adopters and prospective adopters of innovative/alternative septic systems. Focus group participants were asked a series of questions to better understand why they would or would not choose to adopt the alternative and innovative septic systems. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Contact Kate Mulvaney, mulvaney.kate@epa.gov. Format: This is EPA-owned data, but SDMP was generated post clearance due to pre-RAPID/SciHub integration.\r\n\r\nDataset is a Microsoft Word file that contains the transcripts of five focus groups of adopters and prospective adopters of innovative/alternative septic systems. Focus group participants were asked a series of questions to better understand why they would or would not choose to adopt the alternative and innovative septic systems. \n\nThis dataset is associated with the following publication:\nRudman, A., K. Mulvaney, N. Merrill, and K. Canfield. Factors in homeowners\u2019 willingness to adopt nitrogen-reducing innovative/alternative septic systems.   Frontiers in Marine Science. Frontiers, Lausanne,  SWITZERLAND, 10: 1069599, (2023).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1529608",
+            "keyword": [
+                "innovative septic systems",
+                "innovation adoption"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-09-25",
-            "references": [
-                "https://doi.org/10.3389/fmars.2023.1069599"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183689,19 +183683,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fmars.2023.1069599"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "title": "Focus group data for factors in homeowners\u2019 willingness to adopt IA systems"
         },
         {
-            "title": "Modelling data for RI embayments",
-            "description": "Nitrogen loading, estuarine volume and flushing data  derived from land use and hydrodynamic models and used in study. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Warren Boothman",
+                "hasEmail": "mailto:boothman.warren@epa.gov"
+            },
+            "description": "Nitrogen loading, estuarine volume and flushing data  derived from land use and hydrodynamic models and used in study. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529767/RI%20embayment%20model%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "RI embayment model data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529767",
             "keyword": [
@@ -183714,21 +183718,10 @@
                 "Narragansett Bay",
                 "Rhode Island"
             ],
-            "contactPoint": {
-                "fn": "Warren Boothman",
-                "hasEmail": "mailto:boothman.warren@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "RI embayment model data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529767/RI%20embayment%20model%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-03",
-            "references": [
-                "https://doi.org/10.1007/s12237-023-01215-9",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183738,42 +183731,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12237-023-01215-9",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            ],
+            "rights": null,
+            "title": "Modelling data for RI embayments"
         },
         {
-            "title": "RI Dock & mooring data",
-            "description": "Compilation of mooring and dock numbers for RI embayments. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529769",
-            "keyword": [
-                "Docks",
-                "Slips",
-                "Moorings",
-                "density"
-            ],
             "contactPoint": {
                 "fn": "Warren Boothman",
                 "hasEmail": "mailto:boothman.warren@epa.gov"
             },
+            "description": "Compilation of mooring and dock numbers for RI embayments. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
             "distribution": [
                 {
-                    "title": "RI Dock & mooring data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529769/RI%20Dock%20%26%20mooring%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "RI Dock & mooring data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529769",
+            "keyword": [
+                "Docks",
+                "Slips",
+                "Moorings",
+                "density"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-03",
-            "references": [
-                "https://doi.org/10.1007/s12237-023-01215-9",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183783,42 +183776,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12237-023-01215-9",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            ],
+            "rights": null,
+            "title": "RI Dock & mooring data"
         },
         {
-            "title": "RI Mo-DO-N analyses",
-            "description": "Mo and Al analytical data, statistical analysisof relation to hypoxia and nitrogen loading. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529768",
-            "keyword": [
-                "Molybdenum",
-                "Aluminum",
-                "lithogenic",
-                "authigenic"
-            ],
             "contactPoint": {
                 "fn": "Warren Boothman",
                 "hasEmail": "mailto:boothman.warren@epa.gov"
             },
+            "description": "Mo and Al analytical data, statistical analysisof relation to hypoxia and nitrogen loading. \n\nThis dataset is associated with the following publication:\nBoothman, W.S., and L. Coiro. Mapping Hypoxia Response to Estuarine Nitrogen Loading Using Molybdenum in Sediments.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 46(5): 1363\u20131374, (2023).",
             "distribution": [
                 {
-                    "title": "Ri Mo-DO-N analyses.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529768/Ri%20Mo-DO-N%20analyses.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Ri Mo-DO-N analyses.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529768",
+            "keyword": [
+                "Molybdenum",
+                "Aluminum",
+                "lithogenic",
+                "authigenic"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-03",
-            "references": [
-                "https://doi.org/10.1007/s12237-023-01215-9",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183828,19 +183821,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12237-023-01215-9",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10355058"
+            ],
+            "rights": null,
+            "title": "RI Mo-DO-N analyses"
         },
         {
-            "title": "Glassmeyer et al Geo Health Figure Data June 2023",
-            "description": "This is the data underlying the figures in Glassmeyer et al published in GeoHealth.  Figures 2, 3, and 5 are the counts of papers from a given chemical class.  Figure 4 is concentration data pulled from the Supporting Information Tables, which are summaries of the literature.  This is only a secondary analysis of the literature. No novel concentration data was measured by the paper team.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Susan Glassmeyer",
+                "hasEmail": "mailto:glassmeyer.susan@epa.gov"
+            },
+            "description": "This is the data underlying the figures in Glassmeyer et al published in GeoHealth.  Figures 2, 3, and 5 are the counts of papers from a given chemical class.  Figure 4 is concentration data pulled from the Supporting Information Tables, which are summaries of the literature.  This is only a secondary analysis of the literature. No novel concentration data was measured by the paper team.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529175/Glassmeyer%20et%20al%20Geo%20Health%20Figures%20.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Glassmeyer et al Geo Health Figures .xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529175",
             "keyword": [
@@ -183853,19 +183857,11 @@
                 "Drinking water contaminants",
                 "climate change"
             ],
-            "contactPoint": {
-                "fn": "Susan Glassmeyer",
-                "hasEmail": "mailto:glassmeyer.susan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Glassmeyer et al Geo Health Figures .xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529175/Glassmeyer%20et%20al%20Geo%20Health%20Figures%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-11",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -183874,76 +183870,74 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Glassmeyer et al Geo Health Figure Data June 2023"
         },
         {
-            "title": "Weathering Effects on Degradation of Low-Density Polyethylene-Nanosilica Composite with Added Pro-oxidant",
-            "description": "Nanomaterials are increasingly used in polymer composites to enhance the properties of these materials.  Data are presented from a study of sunlight-induced weathering on potential release of nanosilica from a composite with low-density polyethylene (LDPE). Weathering of the composites was determined by quantifying changes in infrared spectroscopic properties (Fourier transform infrared spectroscopy / FTIR); mechanical properties, atomic force microscopy (AFM), scanning electron microscopy and other procedures. \n\nThis dataset is associated with the following publication:\nZepp, R., B. Acrey, M. Davis, A. Andrady, J. Locklin, R. Arnold, O. Okungbowa, and A. Commodore. Weathering Effects on Degradation of Low-Density Polyethylene-Nanosilica Composite with Added Pro-oxidant.   Journal of Polymers and the Environment. Springer Nature, New York, NY, USA, 31: 4184\u20134192, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1502554",
-            "keyword": [
-                "polyethylene",
-                "nanosilica",
-                "composites",
-                "weathering",
-                "model",
-                "nanomaterials",
-                "weathering rates",
-                "low-density polyethylene",
-                "sunlight"
-            ],
             "contactPoint": {
                 "fn": "Richard Zepp",
                 "hasEmail": "mailto:zepp.richard@epa.gov"
             },
+            "description": "Nanomaterials are increasingly used in polymer composites to enhance the properties of these materials.  Data are presented from a study of sunlight-induced weathering on potential release of nanosilica from a composite with low-density polyethylene (LDPE). Weathering of the composites was determined by quantifying changes in infrared spectroscopic properties (Fourier transform infrared spectroscopy / FTIR); mechanical properties, atomic force microscopy (AFM), scanning electron microscopy and other procedures. \n\nThis dataset is associated with the following publication:\nZepp, R., B. Acrey, M. Davis, A. Andrady, J. Locklin, R. Arnold, O. Okungbowa, and A. Commodore. Weathering Effects on Degradation of Low-Density Polyethylene-Nanosilica Composite with Added Pro-oxidant.   Journal of Polymers and the Environment. Springer Nature, New York, NY, USA, 31: 4184\u20134192, (2023).",
             "distribution": [
                 {
-                    "title": "AFM changes.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502554/AFM%20changes.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "AFM changes.docx"
                 },
                 {
-                    "title": "Description of Dataset files LDPE-nanoSi.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502554/Description%20of%20Dataset%20files%20LDPE-nanoSi.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Description of Dataset files LDPE-nanoSi.docx"
                 },
                 {
-                    "title": "Irradiance with cutoffs.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502554/Irradiance%20with%20cutoffs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Irradiance with cutoffs.xlsx"
                 },
                 {
-                    "title": "mechanical property changes.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502554/mechanical%20property%20changes.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "mechanical property changes.docx"
                 },
                 {
-                    "title": "rate contants mechanical change.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502554/rate%20contants%20mechanical%20change.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "rate contants mechanical change.docx"
                 },
                 {
-                    "title": "Wavelength effects on FTIR carbonyl increase.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502554/Wavelength%20effects%20on%20FTIR%20carbonyl%20increase.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Wavelength effects on FTIR carbonyl increase.docx"
                 },
                 {
-                    "title": "SCID_B-0zpk_FIGURE LEGENDS with supplemental figures.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502554/SCID_B-0zpk_FIGURE%20LEGENDS%20with%20supplemental%20figures.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "SCID_B-0zpk_FIGURE LEGENDS with supplemental figures.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502554",
+            "keyword": [
+                "polyethylene",
+                "nanosilica",
+                "composites",
+                "weathering",
+                "model",
+                "nanomaterials",
+                "weathering rates",
+                "low-density polyethylene",
+                "sunlight"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-08-13",
-            "references": [
-                "https://doi.org/10.1007/s10924-023-02864-4"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -183953,19 +183947,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10924-023-02864-4"
+            ],
+            "rights": null,
+            "title": "Weathering Effects on Degradation of Low-Density Polyethylene-Nanosilica Composite with Added Pro-oxidant"
         },
         {
-            "title": "Tapwater Exposures, Effects Potential, and Residential Risk Management in Northern Plains Nations Bioassay Summary Data",
-            "description": "ABSTRACT: In the United States (US), private-supply tapwater (TW) is rarely monitored. This data gap undermines individual and community risk management decision making, leading to increased probability of unrecognized contaminant exposures in rural and remote locations that rely on private wells. We assessed point-of-use (POU) TW in three Northern Plains Tribal Nations, where ongoing TW arsenic (As) interventions include expansion of small community water systems and POU adsorptive-media treatment for remote homes   participating in the ongoing Strong Heart Water Study. TW samples from 34 private-well and 22 public-supply sites were analyzed for 3 field parameters, 476 organics, 34 inorganics, and 3 in vitro bioactivities. Health benchmark weighted cumulative Hazard Indices (HI) and ratios of organic contaminant in vitro exposure-activity cutoffs were assessed for detected contaminants. Sixty-three organics and 30 inorganics were detected in TW. Arsenic, uranium (U), and lead (Pb) were detected in 54%, 43%, and 20% of samples, respectively. Concentrations equivalent to public supply Maximum Contaminant Level(s) (MCL) were exceeded only in untreated private-well samples (As 47%, U 3%). Precautionary health based HI screening levels were exceeded frequently and attributed primarily to inorganics in private supplies and chlorine  -based disinfection byproducts (DBP) in public supplies. The results support ongoing interventions to reduce TW As exposures and indicate that simultaneous exposures to other co-occurring TW contaminants are common, warranting consideration of expanded source, point-of-entry (POE), or POU treatment(s). This study supports the need for increased monitoring of private-well TW employing a broad, environmentally informative analytical scope to reduce the risks of unrecognized contaminant exposures and to identify possible additional targets for simultaneous TW risk mitigation (e.g., U, Pb, DBP in this study). \n\nThis dataset is associated with the following publication:\nBradley, P.M., E. Medlock Kakaley, K.M. Romanok, K. Smalling, M. Focazio, R. Charboneau, C.M. George, A. Navas-Acien, M. O'Leary, R. Red Cloud, T. Zacher, S.E. Breitmeyer, M. Cardon, C. Cuny, G. Ducheneaux, K. Enright, N. Evans, J.L. Gray, D.O. Harvey, M.L. Hladik, K.A. Loftin, R.B. McClesky, S. Meppelink, J.F. Valder, C.P. Weiss, and L. White. Tapwater Exposures, Effects Potential, and Residential Risk Management in Northern Plains Nations.   ACS ES&T Water. American Chemical Society, Washington, DC, USA, 2(10): 1772-1788, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Elizabeth Medlock Kakaley",
+                "hasEmail": "mailto:medlockkakaley.elizabeth@epa.gov"
+            },
+            "description": "ABSTRACT: In the United States (US), private-supply tapwater (TW) is rarely monitored. This data gap undermines individual and community risk management decision making, leading to increased probability of unrecognized contaminant exposures in rural and remote locations that rely on private wells. We assessed point-of-use (POU) TW in three Northern Plains Tribal Nations, where ongoing TW arsenic (As) interventions include expansion of small community water systems and POU adsorptive-media treatment for remote homes   participating in the ongoing Strong Heart Water Study. TW samples from 34 private-well and 22 public-supply sites were analyzed for 3 field parameters, 476 organics, 34 inorganics, and 3 in vitro bioactivities. Health benchmark weighted cumulative Hazard Indices (HI) and ratios of organic contaminant in vitro exposure-activity cutoffs were assessed for detected contaminants. Sixty-three organics and 30 inorganics were detected in TW. Arsenic, uranium (U), and lead (Pb) were detected in 54%, 43%, and 20% of samples, respectively. Concentrations equivalent to public supply Maximum Contaminant Level(s) (MCL) were exceeded only in untreated private-well samples (As 47%, U 3%). Precautionary health based HI screening levels were exceeded frequently and attributed primarily to inorganics in private supplies and chlorine  -based disinfection byproducts (DBP) in public supplies. The results support ongoing interventions to reduce TW As exposures and indicate that simultaneous exposures to other co-occurring TW contaminants are common, warranting consideration of expanded source, point-of-entry (POE), or POU treatment(s). This study supports the need for increased monitoring of private-well TW employing a broad, environmentally informative analytical scope to reduce the risks of unrecognized contaminant exposures and to identify possible additional targets for simultaneous TW risk mitigation (e.g., U, Pb, DBP in this study). \n\nThis dataset is associated with the following publication:\nBradley, P.M., E. Medlock Kakaley, K.M. Romanok, K. Smalling, M. Focazio, R. Charboneau, C.M. George, A. Navas-Acien, M. O'Leary, R. Red Cloud, T. Zacher, S.E. Breitmeyer, M. Cardon, C. Cuny, G. Ducheneaux, K. Enright, N. Evans, J.L. Gray, D.O. Harvey, M.L. Hladik, K.A. Loftin, R.B. McClesky, S. Meppelink, J.F. Valder, C.P. Weiss, and L. White. Tapwater Exposures, Effects Potential, and Residential Risk Management in Northern Plains Nations.   ACS ES&T Water. American Chemical Society, Washington, DC, USA, 2(10): 1772-1788, (2022).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526429/Strongheart%20Bioassay%20Summary%20Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Strongheart Bioassay Summary Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1526429",
             "keyword": [
@@ -183977,21 +183981,10 @@
                 "Domestic Well",
                 "Environmental Justice"
             ],
-            "contactPoint": {
-                "fn": "Elizabeth Medlock Kakaley",
-                "hasEmail": "mailto:medlockkakaley.elizabeth@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Strongheart Bioassay Summary Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526429/Strongheart%20Bioassay%20Summary%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-05-12",
-            "references": [
-                "https://doi.org/10.1021/acsestwater.2c00293",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9578051"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184001,19 +183994,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acsestwater.2c00293",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9578051"
+            ],
+            "rights": null,
+            "title": "Tapwater Exposures, Effects Potential, and Residential Risk Management in Northern Plains Nations Bioassay Summary Data"
         },
         {
-            "title": "Sex-specific respiratory and systemic stress effects of acute acrolein and trichloroethylene inhalation",
-            "description": "Employing acrolein, a potent airway irritant, and TCE, with low irritancy, authors hypothesized that airway injury and inflammation would be involved in eliciting neuroendocrine-mediated systemic alterations. Male and female Wistar-Kyoto rats were exposed nose-only to air, acrolein or trichloroethylene (TCE) in incremental concentrations over 30 min, followed by 3.5-hr exposure to the highest concentration (acrolein - 0.0, 0.1, 0.316, 1, 3.16 ppm; TCE - 0.0, 3.16, 10, 31.6, 100 ppm) while performing head-out plethysmography (HOP), and animals were necropsied immediately post-exposure to assess nasal and lung injury/inflammation, systemic neurohormones, circulating stress hormones and also metabolic hormones. \n\nThis dataset is associated with the following publication:\nAlewel, D., T. Jackson, S. Vance, M. Schladweiler, P. Evansky, A. Henriquez, R. Grindstaff, S. Gavett, and U. Kodavanti. Sex-specific respiratory and systemic endocrine effects of acute acrolein and trichloroethylene inhalation.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 382: 22-32, (2023).",
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
+            "description": "Employing acrolein, a potent airway irritant, and TCE, with low irritancy, authors hypothesized that airway injury and inflammation would be involved in eliciting neuroendocrine-mediated systemic alterations. Male and female Wistar-Kyoto rats were exposed nose-only to air, acrolein or trichloroethylene (TCE) in incremental concentrations over 30 min, followed by 3.5-hr exposure to the highest concentration (acrolein - 0.0, 0.1, 0.316, 1, 3.16 ppm; TCE - 0.0, 3.16, 10, 31.6, 100 ppm) while performing head-out plethysmography (HOP), and animals were necropsied immediately post-exposure to assess nasal and lung injury/inflammation, systemic neurohormones, circulating stress hormones and also metabolic hormones. \n\nThis dataset is associated with the following publication:\nAlewel, D., T. Jackson, S. Vance, M. Schladweiler, P. Evansky, A. Henriquez, R. Grindstaff, S. Gavett, and U. Kodavanti. Sex-specific respiratory and systemic endocrine effects of acute acrolein and trichloroethylene inhalation.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 382: 22-32, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528189/Alewel%20et%20al_Toxicology_Sciencehub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Alewel et al_Toxicology_Sciencehub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528189",
             "keyword": [
@@ -184024,20 +184028,10 @@
                 "Nitrogen and Co-pollutants",
                 "acrolein"
             ],
-            "contactPoint": {
-                "fn": "Urmila Kodavanti",
-                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Alewel et al_Toxicology_Sciencehub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528189/Alewel%20et%20al_Toxicology_Sciencehub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-11-07",
-            "references": [
-                "https://doi.org/10.1016/j.toxlet.2023.05.005"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184047,41 +184041,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.toxlet.2023.05.005"
+            ],
+            "rights": null,
+            "title": "Sex-specific respiratory and systemic stress effects of acute acrolein and trichloroethylene inhalation"
         },
         {
-            "title": "Head on Liner raw data",
-            "description": "Data used for the manuscript collected form landfill reports. \n\nThis dataset is associated with the following publication:\nJain, P., K. Winslow, T. Townsend, M. Krause, and T. Tolaymat. Assessment of Municipal Solid-Waste Landfill Liner Performance.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(9): 04023055, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527722",
-            "keyword": [
-                "Landfill",
-                "Solid Waste",
-                "liner system",
-                "leachate"
-            ],
             "contactPoint": {
                 "fn": "Thabet Tolaymat",
                 "hasEmail": "mailto:tolaymat.thabet@epa.gov"
             },
+            "description": "Data used for the manuscript collected form landfill reports. \n\nThis dataset is associated with the following publication:\nJain, P., K. Winslow, T. Townsend, M. Krause, and T. Tolaymat. Assessment of Municipal Solid-Waste Landfill Liner Performance.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(9): 04023055, (2023).",
             "distribution": [
                 {
-                    "title": "Leakage Rate data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527722/Leakage%20Rate%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Leakage Rate data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527722",
+            "keyword": [
+                "Landfill",
+                "Solid Waste",
+                "liner system",
+                "leachate"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-07-07",
-            "references": [
-                "https://doi.org/10.1061/joeedu.eeeng-7218"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184091,41 +184085,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/joeedu.eeeng-7218"
+            ],
+            "rights": null,
+            "title": "Head on Liner raw data"
         },
         {
-            "title": "Model Results",
-            "description": "The data is an output from SLOPE/W that looks at slope failure as a result of landfill pressures. \n\nThis dataset is associated with the following publication:\nJain, P., A. Kanneganti, T. Townsend, M. Krause, and T. Tolaymat. Isothermal Dual-Phase Flow Modeling to Assess the Impact of Gas Collection on Geotechnical and Hydraulic Performance of Landfills.   JOURNAL OF GEOTECHNICAL AND GEOENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(8): 04023061, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526326",
-            "keyword": [
-                "materials management",
-                "landfills",
-                "food waste",
-                "Waste Management"
-            ],
             "contactPoint": {
                 "fn": "Thabet Tolaymat",
                 "hasEmail": "mailto:tolaymat.thabet@epa.gov"
             },
+            "description": "The data is an output from SLOPE/W that looks at slope failure as a result of landfill pressures. \n\nThis dataset is associated with the following publication:\nJain, P., A. Kanneganti, T. Townsend, M. Krause, and T. Tolaymat. Isothermal Dual-Phase Flow Modeling to Assess the Impact of Gas Collection on Geotechnical and Hydraulic Performance of Landfills.   JOURNAL OF GEOTECHNICAL AND GEOENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(8): 04023061, (2023).",
             "distribution": [
                 {
-                    "title": "Raw data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526326/Raw%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Raw data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526326",
+            "keyword": [
+                "materials management",
+                "landfills",
+                "food waste",
+                "Waste Management"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-03-22",
-            "references": [
-                "https://doi.org/10.1061/jggefk.gteng-11260"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184135,47 +184129,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/jggefk.gteng-11260"
+            ],
+            "rights": null,
+            "title": "Model Results"
         },
         {
-            "title": "Meta-Dataset for property values and water quality",
-            "description": "We conduct a comprehensive literature review and meta-analysis of studies that examine the effects of water quality on waterfront and non-waterfront housing values. We identify 36 studies that yield 665 observations. The rows of the dataset include each observation from the hedonic studies and the columns include the variables we created from each study (e.g., year of publication, type of publication, water quality measure, location, waterbody type, elasticities).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529758",
-            "keyword": [
-                "lake",
-                "meta-analysis",
-                "property value",
-                "benefit transfer",
-                "hedonic",
-                "water clarity"
-            ],
             "contactPoint": {
                 "fn": "Matthew Heberling",
                 "hasEmail": "mailto:heberling.matt@epa.gov"
             },
+            "description": "We conduct a comprehensive literature review and meta-analysis of studies that examine the effects of water quality on waterfront and non-waterfront housing values. We identify 36 studies that yield 665 observations. The rows of the dataset include each observation from the hedonic studies and the columns include the variables we created from each study (e.g., year of publication, type of publication, water quality measure, location, waterbody type, elasticities).",
             "distribution": [
                 {
-                    "title": "Meta-dataset_for_property_values_and_water_quality.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529758/Meta-dataset_for_property_values_and_water_quality.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Meta-dataset_for_property_values_and_water_quality.csv"
                 },
                 {
-                    "title": "Metadata_Dictionary_for_Meta-dataset_for_property_values_and_water_quality.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529758/Metadata_Dictionary_for_Meta-dataset_for_property_values_and_water_quality.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Metadata_Dictionary_for_Meta-dataset_for_property_values_and_water_quality.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529758",
+            "keyword": [
+                "lake",
+                "meta-analysis",
+                "property value",
+                "benefit transfer",
+                "hedonic",
+                "water clarity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-10-12",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -184184,61 +184180,59 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Meta-Dataset for property values and water quality"
         },
         {
-            "title": "Characterizing variations in ambient PM2.5 concentrations at the U.S. Embassy in Dhaka, Bangladesh using observations and the CMAQ modeling system",
-            "description": "Excel data files containing model and ambient PM2.5 concentrations at the U.S. Embassy in Dhaka. \n\nThis dataset is associated with the following publication:\nSarwar, G., C. Hogrefe, B. Henderson, K. Foley, R. Mathur, B. Murphy, and S. Ahmed. Characterizing variations in ambient PM2.5 concentrations at the U.S. Embassy in Dhaka, Bangladesh using observations and the CMAQ modeling system.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 296: N/A, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528454",
-            "keyword": [
-                "Transboundary Pollution",
-                "organic aerosol",
-                "pm2.5",
-                "Dhaka"
-            ],
             "contactPoint": {
                 "fn": "Golam Sarwar",
                 "hasEmail": "mailto:sarwar.golam@epa.gov"
             },
+            "description": "Excel data files containing model and ambient PM2.5 concentrations at the U.S. Embassy in Dhaka. \n\nThis dataset is associated with the following publication:\nSarwar, G., C. Hogrefe, B. Henderson, K. Foley, R. Mathur, B. Murphy, and S. Ahmed. Characterizing variations in ambient PM2.5 concentrations at the U.S. Embassy in Dhaka, Bangladesh using observations and the CMAQ modeling system.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 296: N/A, (2023).",
             "distribution": [
                 {
-                    "title": "Figure_5_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528454/Figure_5_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_5_data.xlsx"
                 },
                 {
-                    "title": "Figure_4_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528454/Figure_4_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_4_data.xlsx"
                 },
                 {
-                    "title": "Figure_3_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528454/Figure_3_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_3_data.xlsx"
                 },
                 {
-                    "title": "Figure_2_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528454/Figure_2_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_2_data.xlsx"
                 },
                 {
-                    "title": "Figure_1_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528454/Figure_1_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure_1_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528454",
+            "keyword": [
+                "Transboundary Pollution",
+                "organic aerosol",
+                "pm2.5",
+                "Dhaka"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-23",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2023.119587"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184248,42 +184242,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2023.119587"
+            ],
+            "rights": null,
+            "title": "Characterizing variations in ambient PM2.5 concentrations at the U.S. Embassy in Dhaka, Bangladesh using observations and the CMAQ modeling system"
         },
         {
-            "title": "A Framework for Prioritizing Chemicals in Retrospective Ecological Assessments: Application to a Great Lakes Area of Concern",
-            "description": "Anthropogenic activities including industrialization, urbanization, and agriculture have resulted in frequent detection of contaminants of emerging concern (CECs) across Great Lakes tributaries. Thus, there is a need to identify CECs of high and low ecotoxicological concern to help focus risk assessment and regulatory efforts. Here we present a weight-of-evidence framework developed to prioritize organic contaminants detected within the Milwaukee Estuary Area of Concern (AOC) (Milwaukee, WI). Chemical prioritization was carried out using experimental data (in vivo, in vitro, and analytical data) generated in 2017 -2018 Milwaukee AOC caged-fish studies, and chemical-specific data collated from US EPA databases (CompTox Chemicals Dashboard, ECOTOXicology Knowledgebase, ToxCast database) and/or estimated using quantitative structure-activity relationships. Overall prioritization was based on multiple lines of evidence: Detection Characteristics (spatial frequency, temporal frequency, environmental distribution), Environmental Fate (persistence, bioaccumulation, biomagnification), Ecotoxicological Potential (exceedence of water quality, in vivo, and in vitro toxicity benchmarks), and Effect Covariance (covariance with effects in caged fish studies). Results indicated within the Milwaukee Estuary AOC, 19/83 CECs were high priority, 13/83 were low priority, and 19/83 were data limited, requiring further investigation for prioritization efforts. Overall, this study presents an effect-based weight-of-evidence strategy that can be employed for CEC prioritization, and highlights several chemicals of ecotoxicological interest within the Milwaukee Estuary AOC. \n\nThis dataset is associated with the following publication:\nMaloney, E., D. Villeneuve, B. Blackwell, K. Vitense, S. Corsi, M. Pronschinske, K. Jensen, and G. Ankley. A framework for prioritizing contaminants in retrospective ecological assessments: Application in the Milwaukee Estuary (Milwaukee, WI).   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 19(5): 1276-96, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1523386",
-            "keyword": [
-                "weight of evidence",
-                "ecological risk assessment",
-                "effects-based monitoring",
-                "contaminants of emerging concern (CEC)",
-                "freshwater ecotoxicology"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Anthropogenic activities including industrialization, urbanization, and agriculture have resulted in frequent detection of contaminants of emerging concern (CECs) across Great Lakes tributaries. Thus, there is a need to identify CECs of high and low ecotoxicological concern to help focus risk assessment and regulatory efforts. Here we present a weight-of-evidence framework developed to prioritize organic contaminants detected within the Milwaukee Estuary Area of Concern (AOC) (Milwaukee, WI). Chemical prioritization was carried out using experimental data (in vivo, in vitro, and analytical data) generated in 2017 -2018 Milwaukee AOC caged-fish studies, and chemical-specific data collated from US EPA databases (CompTox Chemicals Dashboard, ECOTOXicology Knowledgebase, ToxCast database) and/or estimated using quantitative structure-activity relationships. Overall prioritization was based on multiple lines of evidence: Detection Characteristics (spatial frequency, temporal frequency, environmental distribution), Environmental Fate (persistence, bioaccumulation, biomagnification), Ecotoxicological Potential (exceedence of water quality, in vivo, and in vitro toxicity benchmarks), and Effect Covariance (covariance with effects in caged fish studies). Results indicated within the Milwaukee Estuary AOC, 19/83 CECs were high priority, 13/83 were low priority, and 19/83 were data limited, requiring further investigation for prioritization efforts. Overall, this study presents an effect-based weight-of-evidence strategy that can be employed for CEC prioritization, and highlights several chemicals of ecotoxicological interest within the Milwaukee Estuary AOC. \n\nThis dataset is associated with the following publication:\nMaloney, E., D. Villeneuve, B. Blackwell, K. Vitense, S. Corsi, M. Pronschinske, K. Jensen, and G. Ankley. A framework for prioritizing contaminants in retrospective ecological assessments: Application in the Milwaukee Estuary (Milwaukee, WI).   Integrated Environmental Assessment and Management. Allen Press, Inc., Lawrence, KS, USA, 19(5): 1276-96, (2023).",
             "distribution": [
                 {
-                    "title": "Milwaukee_Prioritization_Science_Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523386/Milwaukee_Prioritization_Science_Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Milwaukee_Prioritization_Science_Hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1523386",
+            "keyword": [
+                "weight of evidence",
+                "ecological risk assessment",
+                "effects-based monitoring",
+                "contaminants of emerging concern (CEC)",
+                "freshwater ecotoxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-27",
-            "references": [
-                "https://doi.org/10.1002/ieam.4725"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184293,19 +184287,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/ieam.4725"
+            ],
+            "rights": null,
+            "title": "A Framework for Prioritizing Chemicals in Retrospective Ecological Assessments: Application to a Great Lakes Area of Concern"
         },
         {
-            "title": "Rapid assessment of Dreissena population in Lake Erie using underwater videography",
-            "description": "The data for \"Rapid assessment of Dreissena population in Lake Erie using underwater videography\" came from \"Density data for Lake Ontario benthic invertebrate assemblages from 1964 to 2018\". \n\nThis dataset is associated with the following publication:\nKaratayev, A., L.E. Burlakova, K. Mehler, E. Hinchey, M. Wick, M. Bakowska, and N. Mrozinska. Rapid assessment of Dreissena population in Lake Erie using underwater videography.   HYDROBIOLOGIA. Springer, New York, NY, USA, 848: 2421-2436, (2021).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Molly Wick",
+                "hasEmail": "mailto:wick.molly@epa.gov"
+            },
+            "description": "The data for \"Rapid assessment of Dreissena population in Lake Erie using underwater videography\" came from \"Density data for Lake Ontario benthic invertebrate assemblages from 1964 to 2018\". \n\nThis dataset is associated with the following publication:\nKaratayev, A., L.E. Burlakova, K. Mehler, E. Hinchey, M. Wick, M. Bakowska, and N. Mrozinska. Rapid assessment of Dreissena population in Lake Erie using underwater videography.   HYDROBIOLOGIA. Springer, New York, NY, USA, 848: 2421-2436, (2021).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526405/Data%20on%202019%20Lake%20Erie%20Dreissena%20and%20BIS%20data%20for%20Science%20Hub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data on 2019 Lake Erie Dreissena and BIS data for Science Hub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1526405",
             "keyword": [
@@ -184316,20 +184320,10 @@
                 "Quagga mussels",
                 "Lake Erie"
             ],
-            "contactPoint": {
-                "fn": "Molly Wick",
-                "hasEmail": "mailto:wick.molly@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data on 2019 Lake Erie Dreissena and BIS data for Science Hub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526405/Data%20on%202019%20Lake%20Erie%20Dreissena%20and%20BIS%20data%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-09-01",
-            "references": [
-                "https://doi.org/10.1007/s10750-020-04481-x"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184339,46 +184333,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10750-020-04481-x"
+            ],
+            "rights": null,
+            "title": "Rapid assessment of Dreissena population in Lake Erie using underwater videography"
         },
         {
-            "title": "MSX Nicotine modeling",
-            "description": "Model input data in InputData.xls.\nTable and figure data in stored_results.xls. \n\nThis dataset is associated with the following publication:\nBurkhardt, J., B. Burkhart, and F. Shang. Modeling Nicotine-Induced Chlorine Loss in Drinking Water Using Updated EPANET-MSX.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(12): 04023086, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528598",
-            "keyword": [
-                "water quality",
-                "Drinking water distribution system",
-                "EPANET",
-                "Dispersion"
-            ],
             "contactPoint": {
                 "fn": "Feng Shang",
                 "hasEmail": "mailto:shang.feng@epa.gov"
             },
+            "description": "Model input data in InputData.xls.\nTable and figure data in stored_results.xls. \n\nThis dataset is associated with the following publication:\nBurkhardt, J., B. Burkhart, and F. Shang. Modeling Nicotine-Induced Chlorine Loss in Drinking Water Using Updated EPANET-MSX.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 149(12): 04023086, (2023).",
             "distribution": [
                 {
-                    "title": "stored_results.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528598/stored_results.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "stored_results.xlsx"
                 },
                 {
-                    "title": "InputData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528598/InputData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "InputData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528598",
+            "keyword": [
+                "water quality",
+                "Drinking water distribution system",
+                "EPANET",
+                "Dispersion"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-27",
-            "references": [
-                "https://doi.org/10.1061/joeedu.eeeng-7433"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184388,41 +184382,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/joeedu.eeeng-7433"
+            ],
+            "rights": null,
+            "title": "MSX Nicotine modeling"
         },
         {
-            "title": "Impact of Co-disposal with Ash",
-            "description": "Data used in the manuscript to creat the tables and figures. \n\nThis dataset is associated with the following publication:\nLiu, Y., P. Mendoza-Perilla, K. Clavier, T. Tolaymat, J. Bowden, H. Solo-Gabriele, and T. Townsend. Municipal solid waste incineration (MSWI) ash co-disposal: Influence on per- and polyfluoroalkyl substances (PFAS) concentration in landfill leachate.   WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 144(1): 49-56, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529747",
-            "keyword": [
-                "PFAS",
-                "Bottom Ash",
-                "Coal Refuse Disposal Pile"
-            ],
             "contactPoint": {
                 "fn": "Thabet Tolaymat",
                 "hasEmail": "mailto:tolaymat.thabet@epa.gov"
             },
+            "description": "Data used in the manuscript to creat the tables and figures. \n\nThis dataset is associated with the following publication:\nLiu, Y., P. Mendoza-Perilla, K. Clavier, T. Tolaymat, J. Bowden, H. Solo-Gabriele, and T. Townsend. Municipal solid waste incineration (MSWI) ash co-disposal: Influence on per- and polyfluoroalkyl substances (PFAS) concentration in landfill leachate.   WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 144(1): 49-56, (2022).",
             "distribution": [
                 {
-                    "title": "Table and Figures data from Liu et al 2022.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529747/Table%20and%20Figures%20data%20from%20Liu%20et%20al%202022.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table and Figures data from Liu et al 2022.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529747",
+            "keyword": [
+                "PFAS",
+                "Bottom Ash",
+                "Coal Refuse Disposal Pile"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-10",
-            "references": [
-                "https://doi.org/10.1016/j.wasman.2022.03.009",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10536760"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184432,44 +184425,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.wasman.2022.03.009",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10536760"
+            ],
+            "rights": null,
+            "title": "Impact of Co-disposal with Ash"
         },
         {
-            "title": "Conterminous US modeled stream channel widths and depths",
-            "description": "The data were generated by modeling wetted width, thalweg depth, bankfull width, and bankfull depth measurements from the USEPA's National Rivers and Streams Assessments. Models were developed with StreamCat data (https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset-0) as predictor variables in random forest models. Models were then applied to perennial NHDPlus (version 2.1) stream segments to produce 1.1 million estimated values across the conterminous US. The data, upon publication of the companion journal article, will be also distributed as part of the StreamCat dataset. \n\nThis dataset is associated with the following publication:\nDoyle, J., R. Hill, S. Leibowitz, and J. Ebersole. Random forest models to estimate bankfull and low flow channel widths and depths across the conterminous United States.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA, 59(5): 1099-1114, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1522926",
-            "keyword": [
-                "StreamCat",
-                "National Rivers and Streams Assessment",
-                "wetted width",
-                "thalweg depth",
-                "bankfull width",
-                "bankfull depth",
-                "random forest modeling",
-                "National Hydrography Dataset Plus (NHDPlus)"
-            ],
             "contactPoint": {
                 "fn": "Ryan Hill",
                 "hasEmail": "mailto:hill.ryan@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1522926/documents/Doyle-ChannelDimensions-ScienceHubDataDictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The data were generated by modeling wetted width, thalweg depth, bankfull width, and bankfull depth measurements from the USEPA's National Rivers and Streams Assessments. Models were developed with StreamCat data (https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset-0) as predictor variables in random forest models. Models were then applied to perennial NHDPlus (version 2.1) stream segments to produce 1.1 million estimated values across the conterminous US. The data, upon publication of the companion journal article, will be also distributed as part of the StreamCat dataset. \n\nThis dataset is associated with the following publication:\nDoyle, J., R. Hill, S. Leibowitz, and J. Ebersole. Random forest models to estimate bankfull and low flow channel widths and depths across the conterminous United States.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA, 59(5): 1099-1114, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset-0",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset-0"
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset-0",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset-0"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1522926",
+            "keyword": [
+                "StreamCat",
+                "National Rivers and Streams Assessment",
+                "wetted width",
+                "thalweg depth",
+                "bankfull width",
+                "bankfull depth",
+                "random forest modeling",
+                "National Hydrography Dataset Plus (NHDPlus)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-07-16",
-            "references": [
-                "https://doi.org/10.1111/1752-1688.13116"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184480,89 +184476,91 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1522926/documents/Doyle-ChannelDimensions-ScienceHubDataDictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1111/1752-1688.13116"
+            ],
+            "rights": null,
+            "title": "Conterminous US modeled stream channel widths and depths"
         },
         {
-            "title": "Data to support Reactive organic carbon air emissions from mobile sources in the United States",
-            "description": "This data were used to generate the figures in the peer-reviewed publication \"Reactive organic carbon air emissions from mobile sources in the United States\" published by Atmospheric Chemistry and Physics in 2023. \n\nThe data were produced by analyses of the Motor Vehicle Emissions Simulator (MOVES) and the Community Multiscale Air Quality (CMAQ) model, both developed by EPA (OTAQ and ORD respectively). The analysis focuses on the impact of adjustments to national-level mobile source emissions when considering artifacts from filter measurements and inclusion of intermediate volatility organic compounds which are potent precursors of particulate matter.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529789",
-            "keyword": [
-                "MOVES",
-                "Nitrogen and Co-pollutants",
-                "POA",
-                "reactive organic carbon",
-                "NMOG",
-                "VOC",
-                "PM",
-                "EQUATES",
-                "CMAQ",
-                "SOA",
-                "mobile emissions",
-                "PM Filter Artifacts"
-            ],
             "contactPoint": {
                 "fn": "Benjamin Murphy",
                 "hasEmail": "mailto:murphy.benjamin@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529789/documents/data_dict.txt",
+            "describedByType": "text/plain",
+            "description": "This data were used to generate the figures in the peer-reviewed publication \"Reactive organic carbon air emissions from mobile sources in the United States\" published by Atmospheric Chemistry and Physics in 2023. \n\nThe data were produced by analyses of the Motor Vehicle Emissions Simulator (MOVES) and the Community Multiscale Air Quality (CMAQ) model, both developed by EPA (OTAQ and ORD respectively). The analysis focuses on the impact of adjustments to national-level mobile source emissions when considering artifacts from filter measurements and inclusion of intermediate volatility organic compounds which are potent precursors of particulate matter.",
             "distribution": [
                 {
-                    "title": "mobile_soa.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_soa.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_soa.csv"
                 },
                 {
-                    "title": "mobile_poa.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_poa.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_poa.csv"
                 },
                 {
-                    "title": "mobile_oa.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_oa.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_oa.csv"
                 },
                 {
-                    "title": "mobile_lon.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_lon.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_lon.csv"
                 },
                 {
-                    "title": "mobile_lat.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_lat.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_lat.csv"
                 },
                 {
-                    "title": "mobile_fsoa.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_fsoa.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_fsoa.csv"
                 },
                 {
-                    "title": "mobile_fpoa.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_fpoa.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_fpoa.csv"
                 },
                 {
-                    "title": "mobile_foa.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/mobile_foa.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "mobile_foa.csv"
                 },
                 {
-                    "title": "Murphy_MobileROC_ScienceHubData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529789/Murphy_MobileROC_ScienceHubData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Murphy_MobileROC_ScienceHubData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529789",
+            "keyword": [
+                "MOVES",
+                "Nitrogen and Co-pollutants",
+                "POA",
+                "reactive organic carbon",
+                "NMOG",
+                "VOC",
+                "PM",
+                "EQUATES",
+                "CMAQ",
+                "SOA",
+                "mobile emissions",
+                "PM Filter Artifacts"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-26",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -184572,21 +184570,21 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529789/documents/data_dict.txt",
-            "describedByType": "text/plain"
+            "references": null,
+            "rights": null,
+            "title": "Data to support Reactive organic carbon air emissions from mobile sources in the United States"
         },
         {
-            "title": "Data Description for ORD-055921",
-            "description": "This dataset contains data on epigenetic aging variables, medium and long-term air temperature exposure, and relevant confounders as described in the associated manuscript. This dataset is not publicly accessible because: This data is from a project in which the EPA participated in only an advisory role. The EPA does not own or possess this data. It can be accessed through the following means: The data can be accessed by making a request to Dr. Wenli Ni, the corresponding author for the manuscript. Format: The data is in text files stored in common formats (.csv, .txt). Observations are represented as rows with variables (including the outcome, exposure, and all confounders) represented as columns. \n\nThis dataset is associated with the following publication:\nNi, W., N. Nikolaou, C. Ward-Caviness, S.  Breitner, K. Wolf, S. Zhang, R. Wilson, M. Waldenberger, A. Peters, and A. Schneider. Associations between medium- and long-term exposure to air temperature and epigenetic age acceleration.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 178: 108109, (2023).",
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
+            "description": "This dataset contains data on epigenetic aging variables, medium and long-term air temperature exposure, and relevant confounders as described in the associated manuscript. This dataset is not publicly accessible because: This data is from a project in which the EPA participated in only an advisory role. The EPA does not own or possess this data. It can be accessed through the following means: The data can be accessed by making a request to Dr. Wenli Ni, the corresponding author for the manuscript. Format: The data is in text files stored in common formats (.csv, .txt). Observations are represented as rows with variables (including the outcome, exposure, and all confounders) represented as columns. \n\nThis dataset is associated with the following publication:\nNi, W., N. Nikolaou, C. Ward-Caviness, S.  Breitner, K. Wolf, S. Zhang, R. Wilson, M. Waldenberger, A. Peters, and A. Schneider. Associations between medium- and long-term exposure to air temperature and epigenetic age acceleration.   ENVIRONMENT INTERNATIONAL. Elsevier B.V., Amsterdam,  NETHERLANDS, 178: 108109, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529792",
             "keyword": [
                 "epigenetic aging",
@@ -184594,14 +184592,10 @@
                 "heat",
                 "Aging"
             ],
-            "contactPoint": {
-                "fn": "Cavin Ward-Caviness",
-                "hasEmail": "mailto:ward-caviness.cavin@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-20",
-            "references": [
-                "https://doi.org/10.1016/j.envint.2023.108109"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184611,83 +184605,83 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envint.2023.108109"
+            ],
+            "rights": null,
+            "title": "Data Description for ORD-055921"
         },
         {
-            "title": "Massachusetts Eelgrass Blue Carbon Data",
-            "description": "Sediment cores taken from 5 eelgrass meadows in Massachusetts.  Cores analyzed for carbon content. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529798",
-            "keyword": [
-                "Blue Carbon",
-                "eelgrass"
-            ],
             "contactPoint": {
                 "fn": "Philip Colarusso",
                 "hasEmail": "mailto:colarusso.phil@epa.gov"
             },
+            "description": "Sediment cores taken from 5 eelgrass meadows in Massachusetts.  Cores analyzed for carbon content. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "Julie Simpson's sheet.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529798/Julie%20Simpson%27s%20sheet.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Julie Simpson's sheet.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529798",
+            "keyword": [
+                "Blue Carbon",
+                "eelgrass"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2015-12-07",
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
+            "title": "Massachusetts Eelgrass Blue Carbon Data"
         },
         {
-            "title": "Toxicity by descent: a comparative approach for chemical hazard assessment",
-            "description": "Data for \"John K. Colbourne, Joseph R. Shaw, Elena Sostare, Claudia Rivetti, Romain Derelle, Rosemary Barnett, Bruno Campos, Carlie LaLone, Mark R. Viant, Geoff Hodges, Toxicity by descent: A comparative approach for chemical hazard assessment, Environmental Advances, Volume 9, 2022, 100287, ISSN 2666-7657, https://doi.org/10.1016/j.envadv.2022.100287\". \n\nThis dataset is associated with the following publication:\nColbourne, J., J. Shaw, E. Sostare, C. Rivetti, R. Derelle, R. Barnett, B. Campos, C. Lalone, M. Viant, and G. Hodges. Toxicity by descent: a comparative approach for chemical hazard assessment.   Environmental Advances. Elsevier B.V., Amsterdam,  NETHERLANDS, 9: 100287, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529750",
-            "keyword": [
-                "non-animal approaches",
-                "conservation",
-                "homology",
-                "disease"
-            ],
             "contactPoint": {
                 "fn": "Carlie LaLone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Data for \"John K. Colbourne, Joseph R. Shaw, Elena Sostare, Claudia Rivetti, Romain Derelle, Rosemary Barnett, Bruno Campos, Carlie LaLone, Mark R. Viant, Geoff Hodges, Toxicity by descent: A comparative approach for chemical hazard assessment, Environmental Advances, Volume 9, 2022, 100287, ISSN 2666-7657, https://doi.org/10.1016/j.envadv.2022.100287\". \n\nThis dataset is associated with the following publication:\nColbourne, J., J. Shaw, E. Sostare, C. Rivetti, R. Derelle, R. Barnett, B. Campos, C. Lalone, M. Viant, and G. Hodges. Toxicity by descent: a comparative approach for chemical hazard assessment.   Environmental Advances. Elsevier B.V., Amsterdam,  NETHERLANDS, 9: 100287, (2022).",
             "distribution": [
                 {
-                    "title": "Supplemental Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529750/Supplemental%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental Data.xlsx"
                 },
                 {
-                    "title": "Supplemental Materials.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529750/Supplemental%20Materials.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supplemental Materials.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529750",
+            "keyword": [
+                "non-animal approaches",
+                "conservation",
+                "homology",
+                "disease"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-09-05",
-            "references": [
-                "https://doi.org/10.1016/j.envadv.2022.100287"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184697,47 +184691,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envadv.2022.100287"
+            ],
+            "rights": null,
+            "title": "Toxicity by descent: a comparative approach for chemical hazard assessment"
         },
         {
-            "title": "Demonstration of the Sequence Alignment to Predict Across Species Susceptibility Tool for Rapid Assessment of Protein Conservation",
-            "description": "Data file for \"Vliet SMF, Hazemi M, Blatz D, Jensen M, Mayasich S, Transue TR, Simmons C, Wilkinson A, LaLone CA. Demonstration of the Sequence Alignment to Predict Across Species Susceptibility Tool for Rapid Assessment of Protein Conservation. J Vis Exp. 2023 Feb 10;(192). doi: 10.3791/63970. PMID: 36847398.\". \n\nThis dataset is associated with the following publication:\nVliet, S., M. Hazemi, D. Blatz, M. Jensen, S. Mayasich, T. Transue, C. Simmons, A. Wilkinson, and C. Lalone. Demonstration of the Sequence Alignment to Predict Across Species Susceptibility Tool for Rapid Assessment of Protein Conservation.   Journal of Visualized Experiments. JoVE, Somerville, MA, USA,  192, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529755",
-            "keyword": [
-                "transthyretin",
-                "\u03bc opioid receptor",
-                "SeqAPASS",
-                "Cross species extrapolation",
-                "bioinformatics"
-            ],
             "contactPoint": {
                 "fn": "Carlie LaLone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Data file for \"Vliet SMF, Hazemi M, Blatz D, Jensen M, Mayasich S, Transue TR, Simmons C, Wilkinson A, LaLone CA. Demonstration of the Sequence Alignment to Predict Across Species Susceptibility Tool for Rapid Assessment of Protein Conservation. J Vis Exp. 2023 Feb 10;(192). doi: 10.3791/63970. PMID: 36847398.\". \n\nThis dataset is associated with the following publication:\nVliet, S., M. Hazemi, D. Blatz, M. Jensen, S. Mayasich, T. Transue, C. Simmons, A. Wilkinson, and C. Lalone. Demonstration of the Sequence Alignment to Predict Across Species Susceptibility Tool for Rapid Assessment of Protein Conservation.   Journal of Visualized Experiments. JoVE, Somerville, MA, USA,  192, (2023).",
             "distribution": [
                 {
-                    "title": "Supplemental File.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529755/Supplemental%20File.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental File.xlsx"
                 },
                 {
-                    "title": "Data Dictionary.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529755/Data%20Dictionary.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Data Dictionary.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529755",
+            "keyword": [
+                "transthyretin",
+                "\u03bc opioid receptor",
+                "SeqAPASS",
+                "Cross species extrapolation",
+                "bioinformatics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-02-10",
-            "references": [
-                "https://doi.org/10.3791/63970"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184747,48 +184741,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3791/63970"
+            ],
+            "rights": null,
+            "title": "Demonstration of the Sequence Alignment to Predict Across Species Susceptibility Tool for Rapid Assessment of Protein Conservation"
         },
         {
-            "title": "Prioritizing Pesticides of Potential Concern and Identifying Potential Mixture Effects in Great Lakes Tributaries Using Passive Samplers",
-            "description": "Dataset for \"Loken LC, Corsi SR, Alvarez DA, Ankley GT, Baldwin AK, Blackwell BR, De Cicco LA, Nott MA, Oliver SK, Villeneuve DL. Prioritizing Pesticides of Potential Concern and Identifying Potential Mixture Effects in Great Lakes Tributaries Using Passive Samplers. Environ Toxicol Chem. 2023 Feb;42(2):340-366. doi: 10.1002/etc.5491. Epub 2022 Dec 23. PMID: 36165576; PMCID: PMC10107608.\". \n\nThis dataset is associated with the following publication:\nLoken, L., S. Corsi, D. Alvarez, G. Ankley, A. Baldwin, B. Blackwell, L. DeCicco, M. Nott, S. Oliver, and D. Villeneuve. Prioritizing Pesticides of Potential Concern and Identifying Potential Mixture Effects in Great Lakes Tributaries Using Passive Samplers.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 340-366, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529772",
-            "keyword": [
-                "rivers",
-                "Passive Samplers",
-                "pesticides",
-                "contaminants",
-                "Great Lakes"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Dataset for \"Loken LC, Corsi SR, Alvarez DA, Ankley GT, Baldwin AK, Blackwell BR, De Cicco LA, Nott MA, Oliver SK, Villeneuve DL. Prioritizing Pesticides of Potential Concern and Identifying Potential Mixture Effects in Great Lakes Tributaries Using Passive Samplers. Environ Toxicol Chem. 2023 Feb;42(2):340-366. doi: 10.1002/etc.5491. Epub 2022 Dec 23. PMID: 36165576; PMCID: PMC10107608.\". \n\nThis dataset is associated with the following publication:\nLoken, L., S. Corsi, D. Alvarez, G. Ankley, A. Baldwin, B. Blackwell, L. DeCicco, M. Nott, S. Oliver, and D. Villeneuve. Prioritizing Pesticides of Potential Concern and Identifying Potential Mixture Effects in Great Lakes Tributaries Using Passive Samplers.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 340-366, (2023).",
             "distribution": [
                 {
-                    "title": "Supporting File 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529772/Supporting%20File%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supporting File 2.xlsx"
                 },
                 {
-                    "title": "Supporting File 1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529772/Supporting%20File%201.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supporting File 1.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529772",
+            "keyword": [
+                "rivers",
+                "Passive Samplers",
+                "pesticides",
+                "contaminants",
+                "Great Lakes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-09-22",
-            "references": [
-                "https://doi.org/10.1002/etc.5491",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10107608"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184798,19 +184791,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5491",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10107608"
+            ],
+            "rights": null,
+            "title": "Prioritizing Pesticides of Potential Concern and Identifying Potential Mixture Effects in Great Lakes Tributaries Using Passive Samplers"
         },
         {
-            "title": "Human well-being and natural capital indicators for Great Lakes waterfront revitalization",
-            "description": "Dataset for \"Ted R. Angradi, Jonathon J. Launspach, Molly J. Wick, Human well-being and natural capital indicators for Great Lakes waterfront revitalization, Journal of Great Lakes Research, Volume 48, Issue 4, 2022, Pages 1104-1120, ISSN 0380-1330, https://doi.org/10.1016/j.jglr.2022.04.016.\". \n\nThis dataset is associated with the following publication:\nAngradi, T., J. Launspach, and M. Wick. Human well-being and natural capital indicators for Great Lakes waterfront revitalization.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 48(4): 1104-1120, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Molly Wick",
+                "hasEmail": "mailto:wick.molly@epa.gov"
+            },
+            "description": "Dataset for \"Ted R. Angradi, Jonathon J. Launspach, Molly J. Wick, Human well-being and natural capital indicators for Great Lakes waterfront revitalization, Journal of Great Lakes Research, Volume 48, Issue 4, 2022, Pages 1104-1120, ISSN 0380-1330, https://doi.org/10.1016/j.jglr.2022.04.016.\". \n\nThis dataset is associated with the following publication:\nAngradi, T., J. Launspach, and M. Wick. Human well-being and natural capital indicators for Great Lakes waterfront revitalization.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 48(4): 1104-1120, (2022).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529773/Supplementary_Data_AngradiEtAl_2022.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary_Data_AngradiEtAl_2022.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529773",
             "keyword": [
@@ -184821,20 +184825,10 @@
                 "Natural capital",
                 "indicators"
             ],
-            "contactPoint": {
-                "fn": "Molly Wick",
-                "hasEmail": "mailto:wick.molly@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Supplementary_Data_AngradiEtAl_2022.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529773/Supplementary_Data_AngradiEtAl_2022.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-04-25",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2022.04.016"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184844,48 +184838,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2022.04.016"
+            ],
+            "rights": null,
+            "title": "Human well-being and natural capital indicators for Great Lakes waterfront revitalization"
         },
         {
-            "title": "Prioritizing Pharmaceutical Contaminants in Great Lakes Tributaries Using Risk-Based Screening Techniques",
-            "description": "Dataset for \"Pronschinske, M.A., Corsi, S.R., DeCicco, L.A., Furlong, E.T., Ankley, G.T., Blackwell, B.R., Villeneuve, D.L., Lenaker, P.L. and Nott, M.A. (2022), Prioritizing Pharmaceutical Contaminants in Great Lakes Tributaries Using Risk-Based Screening Techniques. Environ Toxicol Chem, 41: 2221-2239. https://doi.org/10.1002/etc.5403\". \n\nThis dataset is associated with the following publication:\nPronschinske, M., S. Corsi, L. DeCicco, E. Furlong, G. Ankley, B. Blackwell, D. Villeneuve, P. Lenaker, and M. Nott. Prioritizing Pharmaceutical Contaminants in Great Lakes Tributaries Using Risk-Based Screening Techniques..   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(9): 2221-2239, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529774",
-            "keyword": [
-                "surface water",
-                "Great Lakes Restoration Initiative",
-                "aquatic toxicity",
-                "pharmaceuticals",
-                "screening and prioritization"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Dataset for \"Pronschinske, M.A., Corsi, S.R., DeCicco, L.A., Furlong, E.T., Ankley, G.T., Blackwell, B.R., Villeneuve, D.L., Lenaker, P.L. and Nott, M.A. (2022), Prioritizing Pharmaceutical Contaminants in Great Lakes Tributaries Using Risk-Based Screening Techniques. Environ Toxicol Chem, 41: 2221-2239. https://doi.org/10.1002/etc.5403\". \n\nThis dataset is associated with the following publication:\nPronschinske, M., S. Corsi, L. DeCicco, E. Furlong, G. Ankley, B. Blackwell, D. Villeneuve, P. Lenaker, and M. Nott. Prioritizing Pharmaceutical Contaminants in Great Lakes Tributaries Using Risk-Based Screening Techniques..   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 41(9): 2221-2239, (2022).",
             "distribution": [
                 {
-                    "title": "Supporting Information 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529774/Supporting%20Information%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supporting Information 2.xlsx"
                 },
                 {
-                    "title": "Supporting Information 1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529774/Supporting%20Information%201.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supporting Information 1.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529774",
+            "keyword": [
+                "surface water",
+                "Great Lakes Restoration Initiative",
+                "aquatic toxicity",
+                "pharmaceuticals",
+                "screening and prioritization"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-06",
-            "references": [
-                "https://doi.org/10.1002/etc.5403",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9542422"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184895,48 +184888,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5403",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9542422"
+            ],
+            "rights": null,
+            "title": "Prioritizing Pharmaceutical Contaminants in Great Lakes Tributaries Using Risk-Based Screening Techniques"
         },
         {
-            "title": "Pesticide Prioritization by Potential Biological Effects in Tributaries of the Laurentian Great Lakes",
-            "description": "Data files for \"Oliver, S.K., Corsi, S.R., Baldwin, A.K., Nott, M.A., Ankley, G.T., Blackwell, B.R., Villeneuve, D.L., Hladik, M.L., Kolpin, D.W., Loken, L., DeCicco, L.A., Meyer, M.T. and Loftin, K.A. (2023), Pesticide Prioritization by Potential Biological Effects in Tributaries of the Laurentian Great Lakes. Environ Toxicol Chem, 42: 367-384. https://doi.org/10.1002/etc.5522\". \n\nThis dataset is associated with the following publication:\nOliver, S., S. Corsi, A. Baldwin, M. Nott, G. Ankley, B. Blackwell, D. Villeneuve, M. Hladik, D. Kolpin, L. Loken, L. DeCicco, M. Meyer, and K. Loftin. Pesticide Prioritization by Potential Biological Effects in Tributaries of the Laurentian Great Lakes.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 367-384, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529775",
-            "keyword": [
-                "high-throughput screening",
-                "pesticides",
-                "Laurentian Great Lakes",
-                "biological effects",
-                "neonicotinoids"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Data files for \"Oliver, S.K., Corsi, S.R., Baldwin, A.K., Nott, M.A., Ankley, G.T., Blackwell, B.R., Villeneuve, D.L., Hladik, M.L., Kolpin, D.W., Loken, L., DeCicco, L.A., Meyer, M.T. and Loftin, K.A. (2023), Pesticide Prioritization by Potential Biological Effects in Tributaries of the Laurentian Great Lakes. Environ Toxicol Chem, 42: 367-384. https://doi.org/10.1002/etc.5522\". \n\nThis dataset is associated with the following publication:\nOliver, S., S. Corsi, A. Baldwin, M. Nott, G. Ankley, B. Blackwell, D. Villeneuve, M. Hladik, D. Kolpin, L. Loken, L. DeCicco, M. Meyer, and K. Loftin. Pesticide Prioritization by Potential Biological Effects in Tributaries of the Laurentian Great Lakes.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(2): 367-384, (2023).",
             "distribution": [
                 {
-                    "title": "Supporting Information 2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529775/Supporting%20Information%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supporting Information 2.xlsx"
                 },
                 {
-                    "title": "Supporting Information 1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529775/Supporting%20Information%201.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supporting Information 1.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529775",
+            "keyword": [
+                "high-throughput screening",
+                "pesticides",
+                "Laurentian Great Lakes",
+                "biological effects",
+                "neonicotinoids"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-11-07",
-            "references": [
-                "https://doi.org/10.1002/etc.5522",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10107260"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184946,40 +184939,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5522",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10107260"
+            ],
+            "rights": null,
+            "title": "Pesticide Prioritization by Potential Biological Effects in Tributaries of the Laurentian Great Lakes"
         },
         {
-            "title": "Autonomous underwater glider observations in southern Lake Ontario and Niagara River plume",
-            "description": "Glider data for \"Paul McKinney, Tom Hollenhorst, and Joel Hoffman \"Autonomous underwater glider observations in southern Lake Ontario and Niagara River plume,\" Aquatic Ecosystem Health & Management 25(1), 102-113, (13 June 2022). https://doi.org/10.14321/aehm.025.01.102\". \n\nThis dataset is associated with the following publication:\nMcKinney, P., T. Hollenhorst, and J. Hoffman. Autonomous underwater glider observations in southern Lake Ontario and Niagara River plume.   Aquatic Ecosystem Health and Management. Taylor & Francis, Inc., Philadelphia, PA, USA, 25(1): 102-113, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529748",
-            "keyword": [
-                "coastal",
-                "conductance",
-                "Great Lakes",
-                "water quality"
-            ],
             "contactPoint": {
                 "fn": "Thomas Hollenhorst",
                 "hasEmail": "mailto:hollenhorst.tom@epa.gov"
             },
+            "description": "Glider data for \"Paul McKinney, Tom Hollenhorst, and Joel Hoffman \"Autonomous underwater glider observations in southern Lake Ontario and Niagara River plume,\" Aquatic Ecosystem Health & Management 25(1), 102-113, (13 June 2022). https://doi.org/10.14321/aehm.025.01.102\". \n\nThis dataset is associated with the following publication:\nMcKinney, P., T. Hollenhorst, and J. Hoffman. Autonomous underwater glider observations in southern Lake Ontario and Niagara River plume.   Aquatic Ecosystem Health and Management. Taylor & Francis, Inc., Philadelphia, PA, USA, 25(1): 102-113, (2022).",
             "distribution": [
                 {
-                    "title": "https://gliders.ioos.us/",
-                    "accessURL": "https://gliders.ioos.us/"
+                    "accessURL": "https://gliders.ioos.us/",
+                    "title": "https://gliders.ioos.us/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529748",
+            "keyword": [
+                "coastal",
+                "conductance",
+                "Great Lakes",
+                "water quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-06-13",
-            "references": [
-                "https://doi.org/10.14321/aehm.025.01.102"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -184989,40 +184983,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.14321/aehm.025.01.102"
+            ],
+            "rights": null,
+            "title": "Autonomous underwater glider observations in southern Lake Ontario and Niagara River plume"
         },
         {
-            "title": "Stable isotope data for Seasonal variation in triple oxygen isotope ratios of precipitation and rivers",
-            "description": "Stable water isotopes of precipitation across the USA and from summer and winter.  Additionally isotopic data was included for river water within the Willamette River in Oregon.  The d18O and d2H were previously published data (references given in the table), while the d17O values were measured on those archived samples, and published in this paper.  ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529786",
-            "keyword": [
-                "precipitation",
-                "water stable isotope",
-                "Willamette River",
-                "seasonal variation"
-            ],
             "contactPoint": {
                 "fn": "Jacqueline Brooks",
                 "hasEmail": "mailto:brooks.reneej@epa.gov"
             },
+            "description": "Stable water isotopes of precipitation across the USA and from summer and winter.  Additionally isotopic data was included for river water within the Willamette River in Oregon.  The d18O and d2H were previously published data (references given in the table), while the d17O values were measured on those archived samples, and published in this paper.  ",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.1029/2022PA004458",
-                    "accessURL": "https://doi.org/10.1029/2022PA004458"
+                    "accessURL": "https://doi.org/10.1029/2022PA004458",
+                    "title": "https://doi.org/10.1029/2022PA004458"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529786",
+            "keyword": [
+                "precipitation",
+                "water stable isotope",
+                "Willamette River",
+                "seasonal variation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-13",
-            "references": [
-                "https://doi.org/10.1029/2022PA004458"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185032,44 +185026,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2022PA004458"
+            ],
+            "rights": null,
+            "title": "Stable isotope data for Seasonal variation in triple oxygen isotope ratios of precipitation and rivers"
         },
         {
-            "title": "Reproducibility of organ-level effects in repeat dose animal studies",
-            "description": "This work estimates benchmarks for new approach method (NAM) performance in predicting organ-level effects in repeat dose studies of adult animals based on variability in replicate animal studies. Data for Paul Friedman et al., \u2018Reproducibility of organ-level effects in repeat dose animal studies\u2019, Computational Toxicology, Vol 28, 100287, Nov 2023, https://doi.org/10.1016/j.comtox.2023.100287. \n\nThis dataset is associated with the following publication:\nFriedman, K., M. Foster, L.L. Pham, M. Feshuk, S. Watford, J. Wambaugh, R. Judson, R. Setzer, and R. Thomas. Reproducibility of organ-level effects in repeat dose animal studies.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 28: 100287, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529446",
-            "keyword": [
-                "variability",
-                "Organ",
-                "Repeat dose",
-                "ToxRefDB"
-            ],
             "contactPoint": {
                 "fn": "Katie Friedman",
                 "hasEmail": "mailto:paul-friedman.katie@epa.gov"
             },
+            "description": "This work estimates benchmarks for new approach method (NAM) performance in predicting organ-level effects in repeat dose studies of adult animals based on variability in replicate animal studies. Data for Paul Friedman et al., \u2018Reproducibility of organ-level effects in repeat dose animal studies\u2019, Computational Toxicology, Vol 28, 100287, Nov 2023, https://doi.org/10.1016/j.comtox.2023.100287. \n\nThis dataset is associated with the following publication:\nFriedman, K., M. Foster, L.L. Pham, M. Feshuk, S. Watford, J. Wambaugh, R. Judson, R. Setzer, and R. Thomas. Reproducibility of organ-level effects in repeat dose animal studies.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 28: 100287, (2023).",
             "distribution": [
                 {
-                    "title": "https://github.com/USEPA/CompTox-Reproducibility-Organ-Effects",
-                    "accessURL": "https://github.com/USEPA/CompTox-Reproducibility-Organ-Effects"
+                    "accessURL": "https://github.com/USEPA/CompTox-Reproducibility-Organ-Effects",
+                    "title": "https://github.com/USEPA/CompTox-Reproducibility-Organ-Effects"
                 },
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/646d247fe4b08a6b394d2853",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/646d247fe4b08a6b394d2853"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/646d247fe4b08a6b394d2853",
+                    "title": "https://clowder.edap-cluster.com/datasets/646d247fe4b08a6b394d2853"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529446",
+            "keyword": [
+                "variability",
+                "Organ",
+                "Repeat dose",
+                "ToxRefDB"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-24",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2023.100287"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185079,20 +185073,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2023.100287"
+            ],
+            "rights": null,
+            "title": "Reproducibility of organ-level effects in repeat dose animal studies"
         },
         {
-            "title": "A Novel Method for the Quantitative Assessment of Fitted Containment Efficiency of Face Coverings",
-            "description": "Excel files containing data shown on graphs and tables that appear in the research article evaluating the efficacy of disposable face coverings in containing aerosols from the wearer. This dataset is not publicly accessible because: EPA does not own these data. It can be accessed through the following means: Contact corresponding author of the published article, William_Bennett@med.unc.edu. Format: Excel files. \n\nThis dataset is associated with the following publication:\nBennett, W., S. Prince, K. Zeman, H. Chen, and J. Samet. A Novel Method for the Quantitative Assessment of Fitted Containment Efficiency of Face Coverings.   INFECTION CONTROL AND HOSPITAL EPIDEMIOLOGY. Slack Incorporated,    13(1-4): 1481-1484, (2023).",
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
+                "fn": "James Samet",
+                "hasEmail": "mailto:samet.james@epa.gov"
+            },
+            "description": "Excel files containing data shown on graphs and tables that appear in the research article evaluating the efficacy of disposable face coverings in containing aerosols from the wearer. This dataset is not publicly accessible because: EPA does not own these data. It can be accessed through the following means: Contact corresponding author of the published article, William_Bennett@med.unc.edu. Format: Excel files. \n\nThis dataset is associated with the following publication:\nBennett, W., S. Prince, K. Zeman, H. Chen, and J. Samet. A Novel Method for the Quantitative Assessment of Fitted Containment Efficiency of Face Coverings.   INFECTION CONTROL AND HOSPITAL EPIDEMIOLOGY. Slack Incorporated,    13(1-4): 1481-1484, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1528087",
             "keyword": [
                 "COVID-19",
@@ -185100,15 +185098,10 @@
                 "respiratory masks",
                 "Infection control"
             ],
-            "contactPoint": {
-                "fn": "James Samet",
-                "hasEmail": "mailto:samet.james@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-08-25",
-            "references": [
-                "https://doi.org/10.1017/ice.2022.316",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10507493"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185118,91 +185111,92 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1017/ice.2022.316",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10507493"
+            ],
+            "rights": null,
+            "title": "A Novel Method for the Quantitative Assessment of Fitted Containment Efficiency of Face Coverings"
         },
         {
-            "title": "Scientific journal article",
-            "description": "Files associated with the manuscript: Proteome profiling of rat brain cortical changes during early postnatal brain development. \n\nThis dataset is associated with the following publication:\nWinnik, W., W. Padgett, E. Pitzer, and D. Herr. Proteome profiling of rat brain cortical changes during early postnatal brain development.   Journal of Proteome Research. American Chemical Society, Washington, DC, USA, 22(7): 2460-2476, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528533",
-            "keyword": [
-                "Brain Cortex",
-                "Children's Environmental Health",
-                "Protein Analysis",
-                "development"
-            ],
             "contactPoint": {
                 "fn": "Witold Winnik",
                 "hasEmail": "mailto:winnik.witold@epa.gov"
             },
+            "description": "Files associated with the manuscript: Proteome profiling of rat brain cortical changes during early postnatal brain development. \n\nThis dataset is associated with the following publication:\nWinnik, W., W. Padgett, E. Pitzer, and D. Herr. Proteome profiling of rat brain cortical changes during early postnatal brain development.   Journal of Proteome Research. American Chemical Society, Washington, DC, USA, 22(7): 2460-2476, (2023).",
             "distribution": [
                 {
-                    "title": "The original instrument data files used in this subproduct.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/The%20original%20instrument%20data%20files%20used%20in%20this%20subproduct.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "The original instrument data files used in this subproduct.docx"
                 },
                 {
-                    "title": "Technical Review Form EPA-363 W. Winnik manuscript reviewer 2.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/Technical%20Review%20Form%20EPA-363%20W.%20Winnik%20manuscript%20reviewer%202.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Technical Review Form EPA-363 W. Winnik manuscript reviewer 2.pdf"
                 },
                 {
-                    "title": "Technical Review Form EPA-363 W. Winnik manuscript reviewer 1.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/Technical%20Review%20Form%20EPA-363%20W.%20Winnik%20manuscript%20reviewer%201.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Technical Review Form EPA-363 W. Winnik manuscript reviewer 1.pdf"
                 },
                 {
-                    "title": "Supplementary Figures for the manuscript Witold Winnik 2_6_23.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/Supplementary%20Figures%20for%20the%20manuscript%20Witold%20Winnik%202_6_23.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supplementary Figures for the manuscript Witold Winnik 2_6_23.pdf"
                 },
                 {
-                    "title": "Subproduct_submitted_files_information W Winnik.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/Subproduct_submitted_files_information%20W%20Winnik.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Subproduct_submitted_files_information W Winnik.docx"
                 },
                 {
-                    "title": "S-Table-Processing.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/S-Table-Processing.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "S-Table-Processing.docx"
                 },
                 {
-                    "title": "S-Table-Consensus.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/S-Table-Consensus.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "S-Table-Consensus.docx"
                 },
                 {
-                    "title": "S-Data-Table-2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/S-Data-Table-2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S-Data-Table-2.xlsx"
                 },
                 {
-                    "title": "S-Data-Table-1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/S-Data-Table-1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "S-Data-Table-1.xlsx"
                 },
                 {
-                    "title": "Rat Rostral Cortex sample processing worksheet.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/Rat%20Rostral%20Cortex%20sample%20processing%20worksheet.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rat Rostral Cortex sample processing worksheet.xlsx"
                 },
                 {
-                    "title": "Proteome profiling of rat brain cortical changes during early PND_Witold Winnik J Proteom Res 2_9_23.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528533/Proteome%20profiling%20of%20rat%20brain%20cortical%20changes%20during%20early%20PND_Witold%20Winnik%20J%20Proteom%20Res%202_9_23.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Proteome profiling of rat brain cortical changes during early PND_Witold Winnik J Proteom Res 2_9_23.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528533",
+            "keyword": [
+                "Brain Cortex",
+                "Children's Environmental Health",
+                "Protein Analysis",
+                "development"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-02-10",
-            "references": [
-                "https://doi.org/10.1021/acs.jproteome.3c00172"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185212,40 +185206,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.jproteome.3c00172"
+            ],
+            "rights": null,
+            "title": "Scientific journal article"
         },
         {
-            "title": "Ohio landfill leachate volumes and surface areas 1988-2020",
-            "description": "Monthly landfill leachate volumes and annual 2-dimensional planar surface areas. \n\nThis dataset is associated with the following publication:\nKrause, M., N. Detwiler, W. Eades, D. Marro, A. Schwarber, and T. Tolaymat. Dataset of leachate volumes and surface areas for municipal solid waste (MSW) landfills in Ohio, USA from 1988-2020.   Data in Brief. Elsevier B.V., Amsterdam,  NETHERLANDS, 47: 108961, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528156",
-            "keyword": [
-                "Municipal Solid Waste Landfill",
-                "leachate",
-                "Active Landfill"
-            ],
             "contactPoint": {
                 "fn": "Max Krause",
                 "hasEmail": "mailto:krause.max@epa.gov"
             },
+            "description": "Monthly landfill leachate volumes and annual 2-dimensional planar surface areas. \n\nThis dataset is associated with the following publication:\nKrause, M., N. Detwiler, W. Eades, D. Marro, A. Schwarber, and T. Tolaymat. Dataset of leachate volumes and surface areas for municipal solid waste (MSW) landfills in Ohio, USA from 1988-2020.   Data in Brief. Elsevier B.V., Amsterdam,  NETHERLANDS, 47: 108961, (2023).",
             "distribution": [
                 {
-                    "title": "https://data.mendeley.com/datasets/rmn843c3bk/draft?a=2d6b81fe-d6f5-4cb2-93e0-4d60267b59d8",
-                    "accessURL": "https://data.mendeley.com/datasets/rmn843c3bk/draft?a=2d6b81fe-d6f5-4cb2-93e0-4d60267b59d8"
+                    "accessURL": "https://data.mendeley.com/datasets/rmn843c3bk/draft?a=2d6b81fe-d6f5-4cb2-93e0-4d60267b59d8",
+                    "title": "https://data.mendeley.com/datasets/rmn843c3bk/draft?a=2d6b81fe-d6f5-4cb2-93e0-4d60267b59d8"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528156",
+            "keyword": [
+                "Municipal Solid Waste Landfill",
+                "leachate",
+                "Active Landfill"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-11-03",
-            "references": [
-                "https://doi.org/10.1016/j.dib.2023.108961",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9969286"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185255,41 +185248,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.dib.2023.108961",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9969286"
+            ],
+            "rights": null,
+            "title": "Ohio landfill leachate volumes and surface areas 1988-2020"
         },
         {
-            "title": "Surface Washing Agent toxicity",
-            "description": "This dataset consists of aquatic toxicity data for oil spill surface washing agents. \n\nThis dataset is associated with the following publication:\nAlloy, M., D. Sundaravadivelu, R. Conmy, P. Meyer, and M. Barron. Determination of Aquatic Hazard Concentrations for the Oil Spill Response Product Class of Surface Washing Agents using Species Sensitivity Distributions.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 193: 115063, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528294",
-            "keyword": [
-                "oil",
-                "toxicity",
-                "hazard",
-                "Surface Washing Agent"
-            ],
             "contactPoint": {
                 "fn": "Mace Barron",
                 "hasEmail": "mailto:barron.mace@epa.gov"
             },
+            "description": "This dataset consists of aquatic toxicity data for oil spill surface washing agents. \n\nThis dataset is associated with the following publication:\nAlloy, M., D. Sundaravadivelu, R. Conmy, P. Meyer, and M. Barron. Determination of Aquatic Hazard Concentrations for the Oil Spill Response Product Class of Surface Washing Agents using Species Sensitivity Distributions.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 193: 115063, (2023).",
             "distribution": [
                 {
-                    "title": "Dataset_Alloy et al. SWA toxicity.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528294/Dataset_Alloy%20et%20al.%20SWA%20toxicity.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dataset_Alloy et al. SWA toxicity.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528294",
+            "keyword": [
+                "oil",
+                "toxicity",
+                "hazard",
+                "Surface Washing Agent"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-11-21",
-            "references": [
-                "https://doi.org/10.1016/j.marpolbul.2023.115063"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185299,20 +185293,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.marpolbul.2023.115063"
+            ],
+            "rights": null,
+            "title": "Surface Washing Agent toxicity"
         },
         {
-            "title": "Metadata",
-            "description": "CMAQ predicted results containing ozone, oxides of nitrogen and other chemical species. This dataset is not publicly accessible because: EPA does not have the dataset as it was created by the Universidad Polit\u00e9cnica de Madrid, Spain. It can be accessed through the following means: The Universidad Polit\u00e9cnica de Madrid created the dataset. Please contact Rafael Borge for the dataset. Email - rafael.borge@upm.es. Format: Dataset includes CMAQ output files in netcdf format. \n\nThis dataset is associated with the following publication:\nPaz, D.d.l., R. Borge, J.M.d. Andr&eacute;s, L. Tovar, G. Sarwar, and S. Napelenok. Summertime tropospheric ozone source apportionment study in Madrid (Spain).   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY,  N/A, (2023).",
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
+            "description": "CMAQ predicted results containing ozone, oxides of nitrogen and other chemical species. This dataset is not publicly accessible because: EPA does not have the dataset as it was created by the Universidad Polit\u00e9cnica de Madrid, Spain. It can be accessed through the following means: The Universidad Polit\u00e9cnica de Madrid created the dataset. Please contact Rafael Borge for the dataset. Email - rafael.borge@upm.es. Format: Dataset includes CMAQ output files in netcdf format. \n\nThis dataset is associated with the following publication:\nPaz, D.d.l., R. Borge, J.M.d. Andr&eacute;s, L. Tovar, G. Sarwar, and S. Napelenok. Summertime tropospheric ozone source apportionment study in Madrid (Spain).   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY,  N/A, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529595",
             "keyword": [
                 "ISAM",
@@ -185321,14 +185319,10 @@
                 "CMAQ",
                 "air quality modeling"
             ],
-            "contactPoint": {
-                "fn": "Golam Sarwar",
-                "hasEmail": "mailto:sarwar.golam@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-09-07",
-            "references": [
-                "https://doi.org/10.5194/egusphere-2023-2056"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185338,41 +185332,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/egusphere-2023-2056"
+            ],
+            "rights": null,
+            "title": "Metadata"
         },
         {
-            "title": "The ToxCast pipeline: updates to curve-fitting approaches and database structure",
-            "description": "Supplemental files to accompany the manuscript: Feshuk et al., \"The ToxCast Pipeline: Updates to Curve-fitting Approaches and Database Structure\", DOI https://doi.org/10.3389/ftox.2023.1275980, PMC10552852. \n\nThis dataset is associated with the following publication:\nFeshuk, M., L. Kolaczkowski, K. Dunham, S. Davidson-Fritz, K. Carstens, J. Brown, R. Judson, and K. Friedman. The ToxCast Pipeline: Updates to Curve-fitting Approaches and Database Structure.   Frontiers in Toxicology. Frontiers, Lausanne,  SWITZERLAND, 5: 1275980, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529812",
-            "keyword": [
-                "InVitroDB",
-                "bioactivity",
-                "ToxCast",
-                "CompTox blueprint"
-            ],
             "contactPoint": {
                 "fn": "Katie Friedman",
                 "hasEmail": "mailto:paul-friedman.katie@epa.gov"
             },
+            "description": "Supplemental files to accompany the manuscript: Feshuk et al., \"The ToxCast Pipeline: Updates to Curve-fitting Approaches and Database Structure\", DOI https://doi.org/10.3389/ftox.2023.1275980, PMC10552852. \n\nThis dataset is associated with the following publication:\nFeshuk, M., L. Kolaczkowski, K. Dunham, S. Davidson-Fritz, K. Carstens, J. Brown, R. Judson, and K. Friedman. The ToxCast Pipeline: Updates to Curve-fitting Approaches and Database Structure.   Frontiers in Toxicology. Frontiers, Lausanne,  SWITZERLAND, 5: 1275980, (2023).",
             "distribution": [
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/6451716ce4b08a6b3942fc66",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/6451716ce4b08a6b3942fc66"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/6451716ce4b08a6b3942fc66",
+                    "title": "https://clowder.edap-cluster.com/datasets/6451716ce4b08a6b3942fc66"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529812",
+            "keyword": [
+                "InVitroDB",
+                "bioactivity",
+                "ToxCast",
+                "CompTox blueprint"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-09-13",
-            "references": [
-                "https://doi.org/10.3389/ftox.2023.1275980",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10552852"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185382,79 +185375,79 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/ftox.2023.1275980",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10552852"
+            ],
+            "rights": null,
+            "title": "The ToxCast pipeline: updates to curve-fitting approaches and database structure"
         },
         {
-            "title": "Advancing the estimation of future climate impacts within the United States",
-            "description": "Data and code for Advancing the estimation of future climate impacts within the United States. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529813",
-            "keyword": [
-                "climate change",
-                "impacts",
-                "net present value"
-            ],
             "contactPoint": {
                 "fn": "Corinne Hartin",
                 "hasEmail": "mailto:hartin.corinne@epa.gov"
             },
+            "description": "Data and code for Advancing the estimation of future climate impacts within the United States. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://github.com/USEPA/FrEDI_NPD",
-                    "accessURL": "https://github.com/USEPA/FrEDI_NPD"
+                    "accessURL": "https://github.com/USEPA/FrEDI_NPD",
+                    "title": "https://github.com/USEPA/FrEDI_NPD"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529813",
+            "keyword": [
+                "climate change",
+                "impacts",
+                "net present value"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-04",
-            "references": [
-                "https://dx.doi.org/10.5194/esd-14-1015-2023"
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
+                "https://dx.doi.org/10.5194/esd-14-1015-2023"
+            ],
+            "rights": null,
+            "title": "Advancing the estimation of future climate impacts within the United States"
         },
         {
-            "title": "Sentinel-1 and Sentinel-2 based frequency of open and vegetated water across the United States (2017-2021)",
-            "description": "High-frequency observations of surface water at fine spatial scales are critical to effectively manage aquatic habitat, flood risk and water quality. We developed inundation algorithms for Sentinel-1 and Sentinel-2 across 12 sites within the conterminous United States (CONUS) covering >536,000 km2 and representing diverse hydrologic and vegetation landscapes. These algorithms were trained on data from 13,412 points spread throughout the 12 sites. Each scene in the 5-year (2017-2021) time series was classified into open water, vegetated water, and non-water at 20 m resolution using variables not only from Sentinel-1 and Sentinel-2, but also variables derived from topographic and weather datasets. The Sentinel-1 model was developed distinct from the Sentinel-2 model to enable the two time series to be integrated into a single high-frequency time series, while open water and vegetated water were both mapped to retain mixed pixel inundation. Results were validated against 7,200 visually inspected points derived from WorldView and PlanetScope imagery. Classification accuracy for open water was high across the 5-year period, with an omission and commission error of only 3.1% and 0.9% for Sentinel-1 and 3.1% and 0.5% for Sentinel-2, respectively. Vegetated water accuracy was lower, as expected given that the class represents mixed pixels. Sentinel-2 showed higher accuracy (10.7% omission and 7.9% commission error) relative to Sentinel-1 (28.4% omission and 16.0% commission error). Our results demonstrated that Sentinel-1 and Sentinel-2 time series can be integrated to improve the temporal resolution when mapping open and vegetated waters, although sensor-specific differences, such as sensitivity to vegetation structure versus pixel color, complicate the data integration for subpixel, vegetated water compared with open water. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., L. Alexander, J. Christensen, K. Solvik, P. Nieuwlandt, and M. Sagehorn. High-frequency time series comparison of Sentinel-1 and Sentinel-2 satellites for mapping open and vegetated water across the United States (2017\u20132021).   REMOTE SENSING OF ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 288: 113498, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529092",
-            "keyword": [
-                "climate",
-                "inundation frequency",
-                "Google Earth Engine"
-            ],
             "contactPoint": {
                 "fn": "Laurie Alexander",
                 "hasEmail": "mailto:alexander.laurie@epa.gov"
             },
+            "description": "High-frequency observations of surface water at fine spatial scales are critical to effectively manage aquatic habitat, flood risk and water quality. We developed inundation algorithms for Sentinel-1 and Sentinel-2 across 12 sites within the conterminous United States (CONUS) covering >536,000 km2 and representing diverse hydrologic and vegetation landscapes. These algorithms were trained on data from 13,412 points spread throughout the 12 sites. Each scene in the 5-year (2017-2021) time series was classified into open water, vegetated water, and non-water at 20 m resolution using variables not only from Sentinel-1 and Sentinel-2, but also variables derived from topographic and weather datasets. The Sentinel-1 model was developed distinct from the Sentinel-2 model to enable the two time series to be integrated into a single high-frequency time series, while open water and vegetated water were both mapped to retain mixed pixel inundation. Results were validated against 7,200 visually inspected points derived from WorldView and PlanetScope imagery. Classification accuracy for open water was high across the 5-year period, with an omission and commission error of only 3.1% and 0.9% for Sentinel-1 and 3.1% and 0.5% for Sentinel-2, respectively. Vegetated water accuracy was lower, as expected given that the class represents mixed pixels. Sentinel-2 showed higher accuracy (10.7% omission and 7.9% commission error) relative to Sentinel-1 (28.4% omission and 16.0% commission error). Our results demonstrated that Sentinel-1 and Sentinel-2 time series can be integrated to improve the temporal resolution when mapping open and vegetated waters, although sensor-specific differences, such as sensitivity to vegetation structure versus pixel color, complicate the data integration for subpixel, vegetated water compared with open water. \n\nThis dataset is associated with the following publication:\nVanderhoof, M., L. Alexander, J. Christensen, K. Solvik, P. Nieuwlandt, and M. Sagehorn. High-frequency time series comparison of Sentinel-1 and Sentinel-2 satellites for mapping open and vegetated water across the United States (2017\u20132021).   REMOTE SENSING OF ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 288: 113498, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.sciencebase.gov/catalog/item/62c5c6ecd34eeb1417bafe09",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/62c5c6ecd34eeb1417bafe09"
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/62c5c6ecd34eeb1417bafe09",
+                    "title": "https://www.sciencebase.gov/catalog/item/62c5c6ecd34eeb1417bafe09"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529092",
+            "keyword": [
+                "climate",
+                "inundation frequency",
+                "Google Earth Engine"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-05-15",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2023.113498",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10303792"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185464,19 +185457,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2023.113498",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10303792"
+            ],
+            "rights": null,
+            "title": "Sentinel-1 and Sentinel-2 based frequency of open and vegetated water across the United States (2017-2021)"
         },
         {
-            "title": "Martin et al Sleep x Eucalyptus Meta Data_Science Hub",
-            "description": "Meta data for all figures and tables that appear in manuscript including Supplementary section. \n\nThis dataset is associated with the following publication:\nMartin, W.K., M. Schladweiler, W. Oshiro, J. Smoot, A. Fisher, W. Williams, M. Valdez, C. Miller, T. Jackson, D. Freeborn, Y.H. Kim, D. Davies, M. Gilmour, U. Kodavanti, P. Kodavanti, M. Hazari, and A. Farraj. Wildfire-related smoke inhalation worsens cardiovascular risk in sleep disrupted rats.   Frontiers in Environmental Health. Frontiers, Lausanne,  SWITZERLAND, 2: 1166918, (2023).",
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
+            "description": "Meta data for all figures and tables that appear in manuscript including Supplementary section. \n\nThis dataset is associated with the following publication:\nMartin, W.K., M. Schladweiler, W. Oshiro, J. Smoot, A. Fisher, W. Williams, M. Valdez, C. Miller, T. Jackson, D. Freeborn, Y.H. Kim, D. Davies, M. Gilmour, U. Kodavanti, P. Kodavanti, M. Hazari, and A. Farraj. Wildfire-related smoke inhalation worsens cardiovascular risk in sleep disrupted rats.   Frontiers in Environmental Health. Frontiers, Lausanne,  SWITZERLAND, 2: 1166918, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528119/Martin%20et%20al%20Sleep%20x%20Eucalyptus%20Meta%20Data_Science%20Hub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Martin et al Sleep x Eucalyptus Meta Data_Science Hub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528119",
             "keyword": [
@@ -185488,20 +185492,10 @@
                 "blood pressure",
                 "modifiable risk factor"
             ],
-            "contactPoint": {
-                "fn": "Aimen Farraj",
-                "hasEmail": "mailto:farraj.aimen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Martin et al Sleep x Eucalyptus Meta Data_Science Hub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528119/Martin%20et%20al%20Sleep%20x%20Eucalyptus%20Meta%20Data_Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-10-24",
-            "references": [
-                "https://doi.org/10.3389/fenvh.2023.1166918"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185511,40 +185505,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fenvh.2023.1166918"
+            ],
+            "rights": null,
+            "title": "Martin et al Sleep x Eucalyptus Meta Data_Science Hub"
         },
         {
-            "title": "Datasets for manuscript: A Graph-Based Modeling Framework for Tracing Hydrological Pollutant Transport in Surface Waters",
-            "description": "Hydrology Graphs\nThis repository contains the code for the manuscript \"A Graph Formulation for Tracing Hydrological Pollutant Transport in Surface Waters.\" There are three main folders containing code and data, and these are outlined below. We call the framework for building a graph of these hydrological systems \"Hydrology Graphs\".\nSeveral of the datafiles for building this framework are large and cannot be stored on Github. To conserve space, the notebook get_and_unpack_data.ipynb or the script get_and_unpack_data.py can be used to download the data from the Watershed Boundary Dataset (WBD), the National Hydrography Dataset (NHDPlusV2), and the agricultural land dataset for the state of Wisconsin. The files WILakes.df and WIRivers.df metnioend in section 1 below are contained within the WI_lakes_rivers.zip folder, and the files 24k Hydro Waterbodies dataset are contained in a zip file under the directory DNR_data/Hydro_Waterbodies. These files can also be unpacked by running the corresponding cells in the notebook get_and_unpack_data.ipynb or get_and_unpack_data.py.\n1. graph_construction\nThis folder contains the data and code for building a graph of the watershed-river-waterbody hydrological system. It uses data from the Watershed Boundary Dataset (link here) and the National Hydrography Dataset (link here) as a basis and builds a list of directed edges. We use NetworkX to build and visualize the list as a graph.\n\n2. case_studies\nThis folder contains three .ipynb files for three separate case studies. These three case studies focus on how \"Hydrology Graphs\" can be used to analyze pollutant impacts in surface waters. Details of these case studies can be found in the manuscript above.\n\n3. DNR_data\nThis folder contains data from the Wisconsin Department of Natural Resources (DNR) on water quality in several Wisconsin lakes. The data was obtained from here using the file Web_scraping_script.py. The original downloaded reports are found in the folder original_lake_reports. These reports were then cleaned and reformatted using the script DNR_data_filter.ipynb. The resulting, cleaned reports are found in the Lakes folder. Each subfolder of the Lakes folder contains data for a single lake. The two .csvs lake_index_WBIC.csv contain an index for what lake each numbered subfolder corresponds. In addition, we added the corresponding COMID in lake_index_WBIC_COMID.csv by matching the NHDPlusV2 data to the Wisconsin DNR's 24k Hydro Waterbodies dataset which we downloaded from here. The DNR's reported data only matches lakes to a waterbody identification code (WBIC), so we use HYDROLakes (indexed by WBIC) to match to the COMID. This is done in the DNR_data_filter.ipynb script as well.\n\nPython Versions\nThe .py files in graph_construction/ were run using Python version 3.9.7. The scripts used the following packages and version numbers:\ngeopandas (0.10.2) \nshapely (1.8.1.post1) \ntqdm (4.63.0) \nnetworkx (2.7.1) \npandas (1.4.1)\nnumpy (1.21.2). \n\nThis dataset is associated with the following publication:\nCole, D.L., G.J. Ruiz-Mercado, and V.M. Zavala. A graph-based modeling framework for tracing hydrological pollutant transport in surface waters.   COMPUTERS AND CHEMICAL ENGINEERING. Elsevier Science Ltd, New York, NY, USA, 179: 108457, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528420",
-            "keyword": [
-                "watersheds",
-                "Graph Theory",
-                "hydrology",
-                "nutrients"
-            ],
             "contactPoint": {
                 "fn": "Gerardo Ruiz-Mercado",
                 "hasEmail": "mailto:ruiz-mercado.gerardo@epa.gov"
             },
+            "description": "Hydrology Graphs\nThis repository contains the code for the manuscript \"A Graph Formulation for Tracing Hydrological Pollutant Transport in Surface Waters.\" There are three main folders containing code and data, and these are outlined below. We call the framework for building a graph of these hydrological systems \"Hydrology Graphs\".\nSeveral of the datafiles for building this framework are large and cannot be stored on Github. To conserve space, the notebook get_and_unpack_data.ipynb or the script get_and_unpack_data.py can be used to download the data from the Watershed Boundary Dataset (WBD), the National Hydrography Dataset (NHDPlusV2), and the agricultural land dataset for the state of Wisconsin. The files WILakes.df and WIRivers.df metnioend in section 1 below are contained within the WI_lakes_rivers.zip folder, and the files 24k Hydro Waterbodies dataset are contained in a zip file under the directory DNR_data/Hydro_Waterbodies. These files can also be unpacked by running the corresponding cells in the notebook get_and_unpack_data.ipynb or get_and_unpack_data.py.\n1. graph_construction\nThis folder contains the data and code for building a graph of the watershed-river-waterbody hydrological system. It uses data from the Watershed Boundary Dataset (link here) and the National Hydrography Dataset (link here) as a basis and builds a list of directed edges. We use NetworkX to build and visualize the list as a graph.\n\n2. case_studies\nThis folder contains three .ipynb files for three separate case studies. These three case studies focus on how \"Hydrology Graphs\" can be used to analyze pollutant impacts in surface waters. Details of these case studies can be found in the manuscript above.\n\n3. DNR_data\nThis folder contains data from the Wisconsin Department of Natural Resources (DNR) on water quality in several Wisconsin lakes. The data was obtained from here using the file Web_scraping_script.py. The original downloaded reports are found in the folder original_lake_reports. These reports were then cleaned and reformatted using the script DNR_data_filter.ipynb. The resulting, cleaned reports are found in the Lakes folder. Each subfolder of the Lakes folder contains data for a single lake. The two .csvs lake_index_WBIC.csv contain an index for what lake each numbered subfolder corresponds. In addition, we added the corresponding COMID in lake_index_WBIC_COMID.csv by matching the NHDPlusV2 data to the Wisconsin DNR's 24k Hydro Waterbodies dataset which we downloaded from here. The DNR's reported data only matches lakes to a waterbody identification code (WBIC), so we use HYDROLakes (indexed by WBIC) to match to the COMID. This is done in the DNR_data_filter.ipynb script as well.\n\nPython Versions\nThe .py files in graph_construction/ were run using Python version 3.9.7. The scripts used the following packages and version numbers:\ngeopandas (0.10.2) \nshapely (1.8.1.post1) \ntqdm (4.63.0) \nnetworkx (2.7.1) \npandas (1.4.1)\nnumpy (1.21.2). \n\nThis dataset is associated with the following publication:\nCole, D.L., G.J. Ruiz-Mercado, and V.M. Zavala. A graph-based modeling framework for tracing hydrological pollutant transport in surface waters.   COMPUTERS AND CHEMICAL ENGINEERING. Elsevier Science Ltd, New York, NY, USA, 179: 108457, (2023).",
             "distribution": [
                 {
-                    "title": "https://github.com/zavalab/JuliaBox/tree/master/HydroGraphs",
-                    "accessURL": "https://github.com/zavalab/JuliaBox/tree/master/HydroGraphs"
+                    "accessURL": "https://github.com/zavalab/JuliaBox/tree/master/HydroGraphs",
+                    "title": "https://github.com/zavalab/JuliaBox/tree/master/HydroGraphs"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528420",
+            "keyword": [
+                "watersheds",
+                "Graph Theory",
+                "hydrology",
+                "nutrients"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-01-06",
-            "references": [
-                "https://doi.org/10.1016/j.compchemeng.2023.108457"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185554,45 +185548,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.compchemeng.2023.108457"
+            ],
+            "rights": null,
+            "title": "Datasets for manuscript: A Graph-Based Modeling Framework for Tracing Hydrological Pollutant Transport in Surface Waters"
         },
         {
-            "title": "Using Geospatial Data and Random Forest To Predict PFAS Contamination in Fish Tissue in the Columbia River Basin, United States",
-            "description": "Publicly available data about potential PFAS sources and PFAS measurements in fish tissue. \n\nThis dataset is associated with the following publication:\nDeLuca, N., A. Mullikin, P. Brumm, A. Rappold, and E. Hubal. Using Geospatial Data and Random Forest To Predict PFAS Contamination in Fish Tissue in the Columbia River Basin, United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57: 14024-14035, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529825",
-            "keyword": [
-                "PFAS",
-                "fish",
-                "exposure",
-                "Columbia River Basin"
-            ],
             "contactPoint": {
                 "fn": "Nicole Deluca",
                 "hasEmail": "mailto:deluca.nikki@epa.gov"
             },
+            "description": "Publicly available data about potential PFAS sources and PFAS measurements in fish tissue. \n\nThis dataset is associated with the following publication:\nDeLuca, N., A. Mullikin, P. Brumm, A. Rappold, and E. Hubal. Using Geospatial Data and Random Forest To Predict PFAS Contamination in Fish Tissue in the Columbia River Basin, United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57: 14024-14035, (2023).",
             "distribution": [
                 {
-                    "title": "https://echo.epa.gov/trends/pfas-tools",
-                    "accessURL": "https://echo.epa.gov/trends/pfas-tools"
+                    "accessURL": "https://echo.epa.gov/trends/pfas-tools",
+                    "title": "https://echo.epa.gov/trends/pfas-tools"
                 },
                 {
-                    "title": "https://ecology.wa.gov/Research-Data/Data-resources/Environmental-Information-Management-database",
-                    "accessURL": "https://ecology.wa.gov/Research-Data/Data-resources/Environmental-Information-Management-database"
+                    "accessURL": "https://ecology.wa.gov/Research-Data/Data-resources/Environmental-Information-Management-database",
+                    "title": "https://ecology.wa.gov/Research-Data/Data-resources/Environmental-Information-Management-database"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529825",
+            "keyword": [
+                "PFAS",
+                "fish",
+                "exposure",
+                "Columbia River Basin"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-30",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c03670",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10515492"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185602,41 +185595,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c03670",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10515492"
+            ],
+            "rights": null,
+            "title": "Using Geospatial Data and Random Forest To Predict PFAS Contamination in Fish Tissue in the Columbia River Basin, United States"
         },
         {
-            "title": "INLA_CONUS_forecast",
-            "description": "OLCI satellite data with CI_cyano algorithm quantify cyanobacteria. Air temperature, precipitation data from PRISM Climate group. \n\nThis dataset is associated with the following publication:\nSchaeffer, B., N. Reynolds, H. Ferriby, W. Salls, D. Smith, J. Johnston, and M. Myer. Forecasting freshwater cyanobacterial harmful algal blooms for Sentinel-3 satellite resolved U.S. lakes and reservoirs.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 349: 119518, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529140",
-            "keyword": [
-                "water quality",
-                "harmful algal bloom",
-                "satellite",
-                "cyanobacteria"
-            ],
             "contactPoint": {
                 "fn": "Blake Schaeffer",
                 "hasEmail": "mailto:schaeffer.blake@epa.gov"
             },
+            "description": "OLCI satellite data with CI_cyano algorithm quantify cyanobacteria. Air temperature, precipitation data from PRISM Climate group. \n\nThis dataset is associated with the following publication:\nSchaeffer, B., N. Reynolds, H. Ferriby, W. Salls, D. Smith, J. Johnston, and M. Myer. Forecasting freshwater cyanobacterial harmful algal blooms for Sentinel-3 satellite resolved U.S. lakes and reservoirs.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 349: 119518, (2024).",
             "distribution": [
                 {
-                    "title": "INLA_CONUS_forecast.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529140/INLA_CONUS_forecast.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "INLA_CONUS_forecast.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529140",
+            "keyword": [
+                "water quality",
+                "harmful algal bloom",
+                "satellite",
+                "cyanobacteria"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-06-06",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2023.119518"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185646,113 +185640,113 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2023.119518"
+            ],
+            "rights": null,
+            "title": "INLA_CONUS_forecast"
         },
         {
-            "title": "Differential effects of four nano and one micro CeO2 particles on HepG2 cells",
-            "description": "Differential expressed gene lists and altered canonical pathways  in HepG2  cells after CeO2 particle treatment. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, B. Robinette, H. Ren, B. Vallanat, A. Astriab Fisher, and K. Kitchin. Differential genomic effects of four nano-sized and one micro-sized CeO2 particles on HepG2 cells.   Materials Express. American Scientific Publishers, VALENCIA, CA, USA, 13(10): 1799-1811, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1523018",
-            "keyword": [
-                "CeO2 nanoparticles",
-                "transcriptomics",
-                "HepG2 cells",
-                "signaling pathways",
-                "oxidative stress",
-                "fatty acid accumulation"
-            ],
             "contactPoint": {
                 "fn": "Sheau-Fung Thai",
                 "hasEmail": "mailto:thai.sheau-fung@epa.gov"
             },
+            "description": "Differential expressed gene lists and altered canonical pathways  in HepG2  cells after CeO2 particle treatment. \n\nThis dataset is associated with the following publication:\nThai, S., C. Jones, B. Robinette, H. Ren, B. Vallanat, A. Astriab Fisher, and K. Kitchin. Differential genomic effects of four nano-sized and one micro-sized CeO2 particles on HepG2 cells.   Materials Express. American Scientific Publishers, VALENCIA, CA, USA, 13(10): 1799-1811, (2023).",
             "distribution": [
                 {
-                    "title": "Q 300 gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Q%20300%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Q 300 gene list.xlsx"
                 },
                 {
-                    "title": "Q 30 gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Q%2030%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Q 30 gene list.xlsx"
                 },
                 {
-                    "title": "Q 3 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Q%203%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Q 3 ugml gene list.xlsx"
                 },
                 {
-                    "title": "W4 100 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/W4%20100%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "W4 100 ugml gene list.xlsx"
                 },
                 {
-                    "title": "W4 30 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/W4%2030%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "W4 30 ugml gene list.xlsx"
                 },
                 {
-                    "title": "W4 3 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/W4%203%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "W4 3 ugml gene list.xlsx"
                 },
                 {
-                    "title": "X5 30 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/X5%2030%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "X5 30 ugml gene list.xlsx"
                 },
                 {
-                    "title": "X5 3ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/X5%203ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "X5 3ugml gene list.xlsx"
                 },
                 {
-                    "title": "GRC280_X5_0_3ugml.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/GRC280_X5_0_3ugml.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GRC280_X5_0_3ugml.xlsx"
                 },
                 {
-                    "title": "Y6 30 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Y6%2030%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Y6 30 ugml gene list.xlsx"
                 },
                 {
-                    "title": "Y6 3 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Y6%203%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Y6 3 ugml gene list.xlsx"
                 },
                 {
-                    "title": "Z7 30 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Z7%2030%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Z7 30 ugml gene list.xlsx"
                 },
                 {
-                    "title": "Z7 3 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Z7%203%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Z7 3 ugml gene list.xlsx"
                 },
                 {
-                    "title": "Z7 0.3 ugml gene list.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/Z7%200.3%20ugml%20gene%20list.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Z7 0.3 ugml gene list.xlsx"
                 },
                 {
-                    "title": "canonical pathways p less than 0.05.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1523018/canonical%20pathways%20p%20less%20than%200.05.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "canonical pathways p less than 0.05.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1523018",
+            "keyword": [
+                "CeO2 nanoparticles",
+                "transcriptomics",
+                "HepG2 cells",
+                "signaling pathways",
+                "oxidative stress",
+                "fatty acid accumulation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-08-12",
-            "references": [
-                "https://doi.org/10.1166/mex.2023.2527"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185762,41 +185756,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1166/mex.2023.2527"
+            ],
+            "rights": null,
+            "title": "Differential effects of four nano and one micro CeO2 particles on HepG2 cells"
         },
         {
-            "title": "Complete Dataset for TEG (Grignard Pure) Manuscript",
-            "description": "Complete dataset for \"Efficacy of Triethylene Glycol (Grignard Pure) against Bacteriophage MS2 in the Air and on Surfaces\". \n\nThis dataset is associated with the following publication:\nRatliff, K., L. Oudejans, J. Archer, M. Calfee, J. Gilberry, D. Hook, W. Schoppman, R. Yaga, L. Brooks, and S. Ryan. Impact of test methodology on the efficacy of triethylene glycol (Grignard Pure) against bacteriophage MS2.   AEROSOL SCIENCE AND TECHNOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 57(12): 1178\u20131185, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528421",
-            "keyword": [
-                "Air Treatment",
-                "Grignard Pure",
-                "bacteriophage MS2",
-                "Triethylene Glycol"
-            ],
             "contactPoint": {
                 "fn": "Katherine Ratliff",
                 "hasEmail": "mailto:ratliff.katherine@epa.gov"
             },
+            "description": "Complete dataset for \"Efficacy of Triethylene Glycol (Grignard Pure) against Bacteriophage MS2 in the Air and on Surfaces\". \n\nThis dataset is associated with the following publication:\nRatliff, K., L. Oudejans, J. Archer, M. Calfee, J. Gilberry, D. Hook, W. Schoppman, R. Yaga, L. Brooks, and S. Ryan. Impact of test methodology on the efficacy of triethylene glycol (Grignard Pure) against bacteriophage MS2.   AEROSOL SCIENCE AND TECHNOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 57(12): 1178\u20131185, (2023).",
             "distribution": [
                 {
-                    "title": "grignard pure manuscript data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528421/grignard%20pure%20manuscript%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "grignard pure manuscript data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528421",
+            "keyword": [
+                "Air Treatment",
+                "Grignard Pure",
+                "bacteriophage MS2",
+                "Triethylene Glycol"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-01-12",
-            "references": [
-                "https://doi.org/10.1080/02786826.2023.2262004"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185806,139 +185800,138 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/02786826.2023.2262004"
+            ],
+            "rights": null,
+            "title": "Complete Dataset for TEG (Grignard Pure) Manuscript"
         },
         {
-            "title": "Assessing residential activity in a home plumbing system simulator: monitoring the occurrence and relationship of major opportunistic pathogens and phagocytic amoebas (FM)",
-            "description": "The raw sequence reads have been submitted to the NCBI Sequence Read Archive (SRA) under the BioProject PRJNA961987 with the following BioSample numbers: SAMN34376234, SAMN34376235, SAMN34376236, SAMN34376237, SAMN34376238, SAMN34376239, SAMN34376240, SAMN34376241, SAMN34376242, SAMN34376243, SAMN34376244, SAMN34376245, SAMN34376246, SAMN34376247, SAMN34376248, SAMN34376249, SAMN34376250, SAMN34376251, SAMN34376252, SAMN34376253, SAMN34376254, SAMN34376255, and SAMN34376256.\n\nAn abundance matrix (Table_taxonomy.xlsx) contains rows as taxonomic lineage, columns as samples, and entries representing the abundance of each lineage as a number of reads and percentage of all reads obtained for each individual location and residential activity.\n\nA table (Table_water_quality_parameters.xlsx) contains rows as residential activity with date sampled, columns as Temp (\u00b0C), Free Chlorine (Cl2/L), pH, L. pneumophila, M. intracellulare, P. aeruginosa, and V. vermiformis for each HPS section. \n\nThis dataset is associated with the following publication:\nGomez-Alvarez, V., H. Ryu, M. Tang, M. McNeely, C. Muhlen, M. Urbanic, D. Williams, D. Lytle, and L. Boczek. Assessing residential activity in a home plumbing system simulator: monitoring the occurrence and relationship of major opportunistic pathogens and phagocytic amoebas.   Frontiers in Microbiology. Frontiers, Lausanne,  SWITZERLAND, 14: 1260460, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529129",
-            "keyword": [
-                "legionella",
-                "Drinking water distribution system",
-                "Premise Plumbing",
-                "Home Plumbing Systems"
-            ],
             "contactPoint": {
                 "fn": "Vicente Gomez-Alvarez",
                 "hasEmail": "mailto:gomez-alvarez.vicente@epa.gov"
             },
+            "description": "The raw sequence reads have been submitted to the NCBI Sequence Read Archive (SRA) under the BioProject PRJNA961987 with the following BioSample numbers: SAMN34376234, SAMN34376235, SAMN34376236, SAMN34376237, SAMN34376238, SAMN34376239, SAMN34376240, SAMN34376241, SAMN34376242, SAMN34376243, SAMN34376244, SAMN34376245, SAMN34376246, SAMN34376247, SAMN34376248, SAMN34376249, SAMN34376250, SAMN34376251, SAMN34376252, SAMN34376253, SAMN34376254, SAMN34376255, and SAMN34376256.\n\nAn abundance matrix (Table_taxonomy.xlsx) contains rows as taxonomic lineage, columns as samples, and entries representing the abundance of each lineage as a number of reads and percentage of all reads obtained for each individual location and residential activity.\n\nA table (Table_water_quality_parameters.xlsx) contains rows as residential activity with date sampled, columns as Temp (\u00b0C), Free Chlorine (Cl2/L), pH, L. pneumophila, M. intracellulare, P. aeruginosa, and V. vermiformis for each HPS section. \n\nThis dataset is associated with the following publication:\nGomez-Alvarez, V., H. Ryu, M. Tang, M. McNeely, C. Muhlen, M. Urbanic, D. Williams, D. Lytle, and L. Boczek. Assessing residential activity in a home plumbing system simulator: monitoring the occurrence and relationship of major opportunistic pathogens and phagocytic amoebas.   Frontiers in Microbiology. Frontiers, Lausanne,  SWITZERLAND, 14: 1260460, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376234",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376234"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376234",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376234"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376235",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376235"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376235",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376235"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376236",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376236"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376236",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376236"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376237",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376237"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376237",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376237"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376238",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376238"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376238",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376238"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376239",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376239"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376239",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376239"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376240",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376240"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376240",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376240"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376241",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376241"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376241",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376241"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376242",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376242"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376242",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376242"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376243",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376243"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376243",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376243"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376244",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376244"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376244",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376244"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376245",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376245"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376245",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376245"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376246",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376246"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376246",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376246"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376247",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376247"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376247",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376247"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376248",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376248"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376248",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376248"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376249",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376249"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376249",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376249"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376250",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376250"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376250",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376250"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376251",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376251"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376251",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376251"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376252",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376252"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376252",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376252"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376253",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376253"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376253",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376253"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376254",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376254"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376254",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376254"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376255",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376255"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376255",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376255"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376256",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376256"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376256",
+                    "title": "https://www.ncbi.nlm.nih.gov/biosample/SAMN34376256"
                 },
                 {
-                    "title": "Table_water_quality_parameters.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529129/Table_water_quality_parameters.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_water_quality_parameters.xlsx"
                 },
                 {
-                    "title": "Table_taxonomy.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529129/Table_taxonomy.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table_taxonomy.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529129",
+            "keyword": [
+                "legionella",
+                "Drinking water distribution system",
+                "Premise Plumbing",
+                "Home Plumbing Systems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-04",
-            "references": [
-                "https://doi.org/10.3389/fmicb.2023.1260460",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10616306"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -185948,19 +185941,32 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fmicb.2023.1260460",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10616306"
+            ],
+            "rights": null,
+            "title": "Assessing residential activity in a home plumbing system simulator: monitoring the occurrence and relationship of major opportunistic pathogens and phagocytic amoebas (FM)"
         },
         {
-            "title": "Potassium jarosite seeding of soils decreases Pb and As bioaccessibility: A path toward concomitant remediation.",
-            "description": "X-ray absorption spectroscopy raw data files",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Tyler Sowers",
+                "hasEmail": "mailto:sowers.tyler@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529831/documents/2023_Data%20Dictionary_TEB.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "X-ray absorption spectroscopy raw data files",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529831/2023_2022_Figures%20and%20Tables_Kjarosite_MS2.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2023_2022_Figures and Tables_Kjarosite_MS2.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529831",
             "keyword": [
@@ -185973,19 +185979,11 @@
                 "spectra",
                 "XAS"
             ],
-            "contactPoint": {
-                "fn": "Tyler Sowers",
-                "hasEmail": "mailto:sowers.tyler@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "2023_2022_Figures and Tables_Kjarosite_MS2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529831/2023_2022_Figures%20and%20Tables_Kjarosite_MS2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-04",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -185995,43 +185993,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529831/documents/2023_Data%20Dictionary_TEB.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": null,
+            "rights": null,
+            "title": "Potassium jarosite seeding of soils decreases Pb and As bioaccessibility: A path toward concomitant remediation."
         },
         {
-            "title": "Phosphate VOC study PFAS breakthrough and modeling data",
-            "description": "Time series breakthrough data for PFAS on pilot systems compared to model predictions. \n\nThis dataset is associated with the following publication:\nHaupert, L., A. Redding, M. Gray, J. Civardi, B. Datsov, T. Sanan, M. Mills, T. Speth, and J. Burkhardt. Impact of phosphate addition on PFAS treatment performance for drinking water.   AWWA Water Science. John Wiley & Sons, Inc., Hoboken, NJ, USA, 5(6): e1361, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529105",
-            "keyword": [
-                "per and polyfluoroalkyl substances (PFAS)",
-                "anion exchange",
-                "GAC",
-                "drinking water"
-            ],
             "contactPoint": {
                 "fn": "Levi Haupert",
                 "hasEmail": "mailto:haupert.levi@epa.gov"
             },
+            "description": "Time series breakthrough data for PFAS on pilot systems compared to model predictions. \n\nThis dataset is associated with the following publication:\nHaupert, L., A. Redding, M. Gray, J. Civardi, B. Datsov, T. Sanan, M. Mills, T. Speth, and J. Burkhardt. Impact of phosphate addition on PFAS treatment performance for drinking water.   AWWA Water Science. John Wiley & Sons, Inc., Hoboken, NJ, USA, 5(6): e1361, (2023).",
             "distribution": [
                 {
-                    "title": "Phos_VOC_SciHubDataset.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529105/Phos_VOC_SciHubDataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Phos_VOC_SciHubDataset.xlsx"
                 }
             ],
-            "modified": "2023-05-08",
-            "references": [
-                "https://doi.org/10.1002/aws2.1361"
-            ],
+            "identifier": "https://doi.org/10.23719/1529105",
+            "keyword": [
+                "per and polyfluoroalkyl substances (PFAS)",
+                "anion exchange",
+                "GAC",
+                "drinking water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
+            "modified": "2023-05-08",
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -186040,20 +186034,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/aws2.1361"
+            ],
+            "rights": null,
+            "title": "Phosphate VOC study PFAS breakthrough and modeling data"
         },
         {
-            "title": "Machine learning to predict tributary phosphorus loads data",
-            "description": "The water and climate data for Lake Erie, including:\nSoil moisture, streamflow, water temperature, evaporation, baseflow. NOTE: This dataset has been removed from public access due to revocation. Please refer inquiries regarding this dataset to the listed contact person.",
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
+                "fn": "Chunling Tang",
+                "hasEmail": "mailto:tang.chunling@epa.gov"
+            },
+            "description": "The water and climate data for Lake Erie, including:\nSoil moisture, streamflow, water temperature, evaporation, baseflow. NOTE: This dataset has been removed from public access due to revocation. Please refer inquiries regarding this dataset to the listed contact person.",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1527723",
             "keyword": [
                 "Nitrogen and Co-pollutants",
@@ -186062,13 +186060,11 @@
                 "eutrophication",
                 "Nutrient use"
             ],
-            "contactPoint": {
-                "fn": "Chunling Tang",
-                "hasEmail": "mailto:tang.chunling@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-08",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -186077,20 +186073,22 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Machine learning to predict tributary phosphorus loads data"
         },
         {
-            "title": "Freshwater Salinization Syndrome Alters Nitrogen Transport in Urban Watersheds",
-            "description": "A synthesis of data mined from USGS publicly available data. This dataset is not publicly accessible because: Data is owned by University of Maryland. It can be accessed through the following means: contact primary authors: josephgalella@gmail.com. Format: Excel spreadsheet. \n\nThis dataset is associated with the following publication:\nGalella, J., S. Kaushal, P. Mayer, C. Maas, R. Shatkay, S. Inamdar, and K. Belt. Freshwater Salinization Syndrome Alters Nitrogen Transport in Urban Watersheds.   WATER. MDPI, Basel,  SWITZERLAND, 15(22): 3956, (2023).",
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
+                "fn": "Paul Mayer",
+                "hasEmail": "mailto:mayer.paul@epa.gov"
+            },
+            "description": "A synthesis of data mined from USGS publicly available data. This dataset is not publicly accessible because: Data is owned by University of Maryland. It can be accessed through the following means: contact primary authors: josephgalella@gmail.com. Format: Excel spreadsheet. \n\nThis dataset is associated with the following publication:\nGalella, J., S. Kaushal, P. Mayer, C. Maas, R. Shatkay, S. Inamdar, and K. Belt. Freshwater Salinization Syndrome Alters Nitrogen Transport in Urban Watersheds.   WATER. MDPI, Basel,  SWITZERLAND, 15(22): 3956, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529837",
             "keyword": [
                 "Nitrogen and Co-pollutants",
@@ -186099,14 +186097,10 @@
                 "Ion",
                 "salinity"
             ],
-            "contactPoint": {
-                "fn": "Paul Mayer",
-                "hasEmail": "mailto:mayer.paul@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-11-14",
-            "references": [
-                "https://doi.org/10.3390/w15223956"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186116,20 +186110,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/w15223956"
+            ],
+            "rights": null,
+            "title": "Freshwater Salinization Syndrome Alters Nitrogen Transport in Urban Watersheds"
         },
         {
-            "title": "Freshwater Salinization Syndrome limits management efforts to improve water quality",
-            "description": "water chemistry collected across multiple streams in the Chesapeake Bay area. This dataset is not publicly accessible because: data maintained and owned by University of Maryland. It can be accessed through the following means: by contacting corresponding author. Format: excel spreadsheets. \n\nThis dataset is associated with the following publication:\nMaas, C., S. Kaushal, M. Rippy, P. Mayer, S. Grant, R. Shatkay, J. Malin, S.V. Bhide, P. Vikesland, L. Krauss, J.E. Reimer, and A.M. Yaculak. Freshwater Salinization Syndrome limits management efforts to improve water quality.   Frontiers in Environmental Science. Frontiers, Lausanne,  SWITZERLAND, 11: 1106581, (2023).",
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
+                "fn": "Paul Mayer",
+                "hasEmail": "mailto:mayer.paul@epa.gov"
+            },
+            "description": "water chemistry collected across multiple streams in the Chesapeake Bay area. This dataset is not publicly accessible because: data maintained and owned by University of Maryland. It can be accessed through the following means: by contacting corresponding author. Format: excel spreadsheets. \n\nThis dataset is associated with the following publication:\nMaas, C., S. Kaushal, M. Rippy, P. Mayer, S. Grant, R. Shatkay, J. Malin, S.V. Bhide, P. Vikesland, L. Krauss, J.E. Reimer, and A.M. Yaculak. Freshwater Salinization Syndrome limits management efforts to improve water quality.   Frontiers in Environmental Science. Frontiers, Lausanne,  SWITZERLAND, 11: 1106581, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529606",
             "keyword": [
                 "Urban Watersheds",
@@ -186139,15 +186137,10 @@
                 "Green Infrastructure",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Paul Mayer",
-                "hasEmail": "mailto:mayer.paul@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-01",
-            "references": [
-                "https://doi.org/10.3389/fenvs.2023.1106581",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10568995"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186157,51 +186150,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3389/fenvs.2023.1106581",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10568995"
+            ],
+            "rights": null,
+            "title": "Freshwater Salinization Syndrome limits management efforts to improve water quality"
         },
         {
-            "title": "Identifying candidate reference chemicals for in vitro testing of the retinoid pathway for predictive developmental toxicity",
-            "description": "Dataset for Baker, et al., Identifying candidate reference chemicals for in vitro testing of the retinoid pathway for predictive developmental toxicity, published in journal Altex, https://doi.org/10.14573/altex.2202231\n\nThe two zip files are Excel Macro files, but could not be loaded into SciHub unless they were converted to zip files. \n\nThis tool was built using the EPA's LitDB, a database of MeSH terms from PubMed/Medline records downloaded from NLM.\n1. A set of MeSH terms for targets of interest was assembled.\n2.  The database was searched for occurrences of those terms with antagonist OR agonist subheading in PubMed citations.\n3.  Non-protein chemicals annotated as major topics in that set of articles was extracted. \n4.  The chemical MeSH term and the protein target MeSH term were output to Excel in a long format (Detail sheet) and pivot table format (Overview sheet). \n5. VBA code was added that allows navigation between the Overview sheet and the Detail sheet. \n\nThis dataset is associated with the following publication:\nBaker, N., J. Pierro, L. Taylor, and T. Knudsen. Identifying candidate reference chemicals for in vitro testing of the retinoid pathway for predictive developmental toxicity.   ALTEX. Society ALTEX Edition, Kuesnacht,  SWITZERLAND, 40(2): 217-236, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529822",
-            "keyword": [
-                "In vitro profiling",
-                "Developmental Toxicity",
-                "Retinoid signaling pathway",
-                "Predictive Toxicology"
-            ],
             "contactPoint": {
                 "fn": "Thomas Knudsen",
                 "hasEmail": "mailto:knudsen.thomas@epa.gov"
             },
+            "description": "Dataset for Baker, et al., Identifying candidate reference chemicals for in vitro testing of the retinoid pathway for predictive developmental toxicity, published in journal Altex, https://doi.org/10.14573/altex.2202231\n\nThe two zip files are Excel Macro files, but could not be loaded into SciHub unless they were converted to zip files. \n\nThis tool was built using the EPA's LitDB, a database of MeSH terms from PubMed/Medline records downloaded from NLM.\n1. A set of MeSH terms for targets of interest was assembled.\n2.  The database was searched for occurrences of those terms with antagonist OR agonist subheading in PubMed citations.\n3.  Non-protein chemicals annotated as major topics in that set of articles was extracted. \n4.  The chemical MeSH term and the protein target MeSH term were output to Excel in a long format (Detail sheet) and pivot table format (Overview sheet). \n5. VBA code was added that allows navigation between the Overview sheet and the Detail sheet. \n\nThis dataset is associated with the following publication:\nBaker, N., J. Pierro, L. Taylor, and T. Knudsen. Identifying candidate reference chemicals for in vitro testing of the retinoid pathway for predictive developmental toxicity.   ALTEX. Society ALTEX Edition, Kuesnacht,  SWITZERLAND, 40(2): 217-236, (2023).",
             "distribution": [
                 {
-                    "title": "SupplementalMaterial_altex.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529822/SupplementalMaterial_altex.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "SupplementalMaterial_altex.docx"
                 },
                 {
-                    "title": "LitDB_RetinoidPathway_altex.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529822/LitDB_RetinoidPathway_altex.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "LitDB_RetinoidPathway_altex.zip"
                 },
                 {
-                    "title": "AbstractSifter_retinoid.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529822/AbstractSifter_retinoid.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "AbstractSifter_retinoid.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529822",
+            "keyword": [
+                "In vitro profiling",
+                "Developmental Toxicity",
+                "Retinoid signaling pathway",
+                "Predictive Toxicology"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-08",
-            "references": [
-                "https://doi.org/10.14573/altex.2202231"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186211,41 +186205,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.14573/altex.2202231"
+            ],
+            "rights": null,
+            "title": "Identifying candidate reference chemicals for in vitro testing of the retinoid pathway for predictive developmental toxicity"
         },
         {
-            "title": "Aerated contactors depth profiles",
-            "description": "Water quality and microbial community data from pilot-scale biologically active aerated contactors and filters treating groundwater for drinking water. \n\nThis dataset is associated with the following publication:\nKeithley, A., V. Gomez-Alvarez, D. Williams, H. Ryu, and D. Lytle. Depth profiles of biological aerated contactors: Characterizing microbial activity treating reduced contaminants.   Journal of Water Process Engineering. Elsevier B.V., Amsterdam,  NETHERLANDS, 56: 104360, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528785",
-            "keyword": [
-                "Biofilter",
-                "aerated contactor",
-                "nitrification",
-                "Drinking water (Groundwater)"
-            ],
             "contactPoint": {
                 "fn": "Asher Keithley",
                 "hasEmail": "mailto:keithley.asher@epa.gov"
             },
+            "description": "Water quality and microbial community data from pilot-scale biologically active aerated contactors and filters treating groundwater for drinking water. \n\nThis dataset is associated with the following publication:\nKeithley, A., V. Gomez-Alvarez, D. Williams, H. Ryu, and D. Lytle. Depth profiles of biological aerated contactors: Characterizing microbial activity treating reduced contaminants.   Journal of Water Process Engineering. Elsevier B.V., Amsterdam,  NETHERLANDS, 56: 104360, (2023).",
             "distribution": [
                 {
-                    "title": "SciHub Aerated Contactor Depth Profiles.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528785/SciHub%20Aerated%20Contactor%20Depth%20Profiles.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub Aerated Contactor Depth Profiles.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528785",
+            "keyword": [
+                "Biofilter",
+                "aerated contactor",
+                "nitrification",
+                "Drinking water (Groundwater)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-18",
-            "references": [
-                "https://doi.org/10.1016/j.jwpe.2023.104360"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186255,41 +186249,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jwpe.2023.104360"
+            ],
+            "rights": null,
+            "title": "Aerated contactors depth profiles"
         },
         {
-            "title": "Nitrogen-Sparging Assisted Anoxic Biological Drinking Water Treatment System",
-            "description": "data comparing denitrification reactors operated in the lab. \n\nThis dataset is associated with the following publication:\nKeithley, A., P. Woodruff, D. Williams, N. Dugan, and D. Lytle. Nitrogen-Sparging Assisted Anoxic Biological  Drinking Water Treatment System.   AWWA Water Science. John Wiley & Sons, Inc., Hoboken, NJ, USA, 5(5): e1359, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528699",
-            "keyword": [
-                "nitrate",
-                "Drinking water (Groundwater)",
-                "denitrification",
-                "biological treatment"
-            ],
             "contactPoint": {
                 "fn": "Asher Keithley",
                 "hasEmail": "mailto:keithley.asher@epa.gov"
             },
+            "description": "data comparing denitrification reactors operated in the lab. \n\nThis dataset is associated with the following publication:\nKeithley, A., P. Woodruff, D. Williams, N. Dugan, and D. Lytle. Nitrogen-Sparging Assisted Anoxic Biological  Drinking Water Treatment System.   AWWA Water Science. John Wiley & Sons, Inc., Hoboken, NJ, USA, 5(5): e1359, (2023).",
             "distribution": [
                 {
-                    "title": "NO3 Pilot SciHub 2023-05-23.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528699/NO3%20Pilot%20SciHub%202023-05-23.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NO3 Pilot SciHub 2023-05-23.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528699",
+            "keyword": [
+                "nitrate",
+                "Drinking water (Groundwater)",
+                "denitrification",
+                "biological treatment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-22",
-            "references": [
-                "https://doi.org/10.1002/aws2.1359"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186299,90 +186293,90 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/aws2.1359"
+            ],
+            "rights": null,
+            "title": "Nitrogen-Sparging Assisted Anoxic Biological Drinking Water Treatment System"
         },
         {
-            "title": "Data for manuscript titled 'PM2.5-attributable mortality burden variability in the continental U.S.'",
-            "description": "Data used for manuscript available at https://www.sciencedirect.com/science/article/pii/S1352231023005575.\n\nIncludes a 'README' file briefly explaining how to combine this data with BenMAP-CE to reproduce the results. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529841",
-            "keyword": [
-                "Air quality and health",
-                "Fine Particulate Matter",
-                "Exposure modeling",
-                "Environmental Justice"
-            ],
             "contactPoint": {
                 "fn": "Elizabeth Chan",
                 "hasEmail": "mailto:chan.elizabeth@epa.gov"
             },
+            "description": "Data used for manuscript available at https://www.sciencedirect.com/science/article/pii/S1352231023005575.\n\nIncludes a 'README' file briefly explaining how to combine this data with BenMAP-CE to reproduce the results. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "Zipped.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529841/Zipped.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Zipped.zip"
                 },
                 {
-                    "title": "README_Command Line Script Instructions.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529841/README_Command%20Line%20Script%20Instructions.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "README_Command Line Script Instructions.docx"
                 },
                 {
-                    "title": "Health Impact Functions.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529841/Health%20Impact%20Functions.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Health Impact Functions.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529841",
+            "keyword": [
+                "Air quality and health",
+                "Fine Particulate Matter",
+                "Exposure modeling",
+                "Environmental Justice"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-13",
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
+            "title": "Data for manuscript titled 'PM2.5-attributable mortality burden variability in the continental U.S.'"
         },
         {
-            "title": "removal of strontium by ion exchange and lime softening at eight drinking water treatment plants",
-            "description": "Strontium concentrations and relevant water chemistry data from 8 ion exchange and lime softening treatment plants. \n\nThis dataset is associated with the following publication:\nLytle, D., A. Keithley, and D. Williams. Removal of Strontium by Ion Exchange and Lime Softening  at Eight Drinking Water Treatment Plants.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 9(8): 2140-2151, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527629",
-            "keyword": [
-                "Strontium",
-                "Drinking water contaminants",
-                "Lime softening",
-                "ion exchange"
-            ],
             "contactPoint": {
                 "fn": "Darren Lytle",
                 "hasEmail": "mailto:lytle.darren@epa.gov"
             },
+            "description": "Strontium concentrations and relevant water chemistry data from 8 ion exchange and lime softening treatment plants. \n\nThis dataset is associated with the following publication:\nLytle, D., A. Keithley, and D. Williams. Removal of Strontium by Ion Exchange and Lime Softening  at Eight Drinking Water Treatment Plants.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 9(8): 2140-2151, (2023).",
             "distribution": [
                 {
-                    "title": "SciHub - Full Scale Sr Removal.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527629/SciHub%20-%20Full%20Scale%20Sr%20Removal.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub - Full Scale Sr Removal.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527629",
+            "keyword": [
+                "Strontium",
+                "Drinking water contaminants",
+                "Lime softening",
+                "ion exchange"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-02-24",
-            "references": [
-                "https://doi.org/10.1039/d2ew00987k"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186392,40 +186386,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/d2ew00987k"
+            ],
+            "rights": null,
+            "title": "removal of strontium by ion exchange and lime softening at eight drinking water treatment plants"
         },
         {
-            "title": "Understanding drivers of mercury in lake trout (Salvelinus namaycush), a top-predator fish in southwest Alaska's parklands",
-            "description": "Supplementary data for \"Understanding drivers of mercury in lake trout (Salvelinus namaycush), a top-predator fish in southwest Alaska's parklands\". \n\nThis dataset is associated with the following publication:\nBartz, K., M. Hannam, T. Wilson, R. Lepak, J. Ogorek, D. Young, C. Eagles-Smith, and D. Krabbenhoft. Understanding drivers of mercury in lake trout (Salvelinus namaycush), a top-predator fish in southwest Alaska\u2019s parklands.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 330: 121678, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529601",
-            "keyword": [
-                "Bayesian model",
-                "mercury",
-                "Alaska",
-                "fish"
-            ],
             "contactPoint": {
                 "fn": "Ryan Lepak",
                 "hasEmail": "mailto:lepak.ryan@epa.gov"
             },
+            "description": "Supplementary data for \"Understanding drivers of mercury in lake trout (Salvelinus namaycush), a top-predator fish in southwest Alaska's parklands\". \n\nThis dataset is associated with the following publication:\nBartz, K., M. Hannam, T. Wilson, R. Lepak, J. Ogorek, D. Young, C. Eagles-Smith, and D. Krabbenhoft. Understanding drivers of mercury in lake trout (Salvelinus namaycush), a top-predator fish in southwest Alaska\u2019s parklands.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 330: 121678, (2023).",
             "distribution": [
                 {
-                    "title": "https://www.sciencebase.gov/catalog/item/611e5b9fd34e40dd9c0196a3",
-                    "accessURL": "https://www.sciencebase.gov/catalog/item/611e5b9fd34e40dd9c0196a3"
+                    "accessURL": "https://www.sciencebase.gov/catalog/item/611e5b9fd34e40dd9c0196a3",
+                    "title": "https://www.sciencebase.gov/catalog/item/611e5b9fd34e40dd9c0196a3"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529601",
+            "keyword": [
+                "Bayesian model",
+                "mercury",
+                "Alaska",
+                "fish"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-19",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2023.121678"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186435,19 +186429,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2023.121678"
+            ],
+            "rights": null,
+            "title": "Understanding drivers of mercury in lake trout (Salvelinus namaycush), a top-predator fish in southwest Alaska's parklands"
         },
         {
-            "title": "Conservation Prioritization Nov2023",
-            "description": "This file contains data associated with the paper \"Our national nutrient reduction needs: Applying a conservation prioritization framework to US agricultural lands\" by  Kirk et al.  This analysis uses data summarized by 8-digit hydrologic unit code, or HUC8, to prioritize conservation activities based on needs and opportunities for in-field and edge-of-field conservation practices.  HUC8-level subwatersheds were prioritized across the conterminous US using national nutrient inventory and agricultural landscape metrics. By utilizing nutrient surplus and nutrient use efficiency, the paper identifies where conservation efforts can focus, but also which types of conservation practices, singularly or in combination, might mitigate the excess nutrients. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jana Compton",
+                "hasEmail": "mailto:compton.jana@epa.gov"
+            },
+            "description": "This file contains data associated with the paper \"Our national nutrient reduction needs: Applying a conservation prioritization framework to US agricultural lands\" by  Kirk et al.  This analysis uses data summarized by 8-digit hydrologic unit code, or HUC8, to prioritize conservation activities based on needs and opportunities for in-field and edge-of-field conservation practices.  HUC8-level subwatersheds were prioritized across the conterminous US using national nutrient inventory and agricultural landscape metrics. By utilizing nutrient surplus and nutrient use efficiency, the paper identifies where conservation efforts can focus, but also which types of conservation practices, singularly or in combination, might mitigate the excess nutrients. ",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529848/Conservation_Prioritization_Nov2023.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Conservation_Prioritization_Nov2023.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529848",
             "keyword": [
@@ -186458,19 +186462,11 @@
                 "conservation",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Jana Compton",
-                "hasEmail": "mailto:compton.jana@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Conservation_Prioritization_Nov2023.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529848/Conservation_Prioritization_Nov2023.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-20",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -186479,52 +186475,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Conservation Prioritization Nov2023"
         },
         {
-            "title": "Flickr Photo Analysis, On site surveys, and Station Assessments for Tillamook Bay and Tampa Bay ",
-            "description": "Data analysis results of Flickr photos from Tillamook Bay and Tampa Bay cross-walking photos with beneficiary classes and environmental end point classes from the National Ecosystem Services Plus classification system. Data of onsite user observations in Tillamook Bay and Tampa Bay capturing environmental conditions, counts of individuals observed, and information on any beneficiary classes (using the National Ecosystem Services Plus classification system) observed. Data from environmental station assessment in Tillamook Bay and Tampa Bay on potential people access or utilization of the space (e.g., access for boats, viewscapes). \n\nThis dataset is associated with the following publication:\nLittles, C.J., N.S. Lewis, T. Dewitt, and M. Harwell. Recreational Beneficiaries and their Landscape Dependencies across National Estuary Program Sites: Tillamook Bay (OR) and Tampa Bay (FL), USA.   Ecosystems and People. Taylor & Francis Group, London,  UK, 19(1): 2276756, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529843",
-            "keyword": [
-                "recreational benefits",
-                "ecosystem services",
-                "Tillamook (Oregon)",
-                "national estuary program",
-                "Tamppa (Florida)"
-            ],
             "contactPoint": {
                 "fn": "Matthew Harwell",
                 "hasEmail": "mailto:harwell.matthew@epa.gov"
             },
+            "description": "Data analysis results of Flickr photos from Tillamook Bay and Tampa Bay cross-walking photos with beneficiary classes and environmental end point classes from the National Ecosystem Services Plus classification system. Data of onsite user observations in Tillamook Bay and Tampa Bay capturing environmental conditions, counts of individuals observed, and information on any beneficiary classes (using the National Ecosystem Services Plus classification system) observed. Data from environmental station assessment in Tillamook Bay and Tampa Bay on potential people access or utilization of the space (e.g., access for boats, viewscapes). \n\nThis dataset is associated with the following publication:\nLittles, C.J., N.S. Lewis, T. Dewitt, and M. Harwell. Recreational Beneficiaries and their Landscape Dependencies across National Estuary Program Sites: Tillamook Bay (OR) and Tampa Bay (FL), USA.   Ecosystems and People. Taylor & Francis Group, London,  UK, 19(1): 2276756, (2023).",
             "distribution": [
                 {
-                    "title": "LittlesEtAl_DATA_StationAssessments.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529843/LittlesEtAl_DATA_StationAssessments.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LittlesEtAl_DATA_StationAssessments.xlsx"
                 },
                 {
-                    "title": "LittlesEtAl_DATA_OnsiteSurveys.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529843/LittlesEtAl_DATA_OnsiteSurveys.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LittlesEtAl_DATA_OnsiteSurveys.xlsx"
                 },
                 {
-                    "title": "LittlesEtAl_DATA_FlickrPhotoAnalysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529843/LittlesEtAl_DATA_FlickrPhotoAnalysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LittlesEtAl_DATA_FlickrPhotoAnalysis.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529843",
+            "keyword": [
+                "recreational benefits",
+                "ecosystem services",
+                "Tillamook (Oregon)",
+                "national estuary program",
+                "Tamppa (Florida)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-11-01",
-            "references": [
-                "https://doi.org/10.1080/26395916.2023.2276756"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186534,41 +186528,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/26395916.2023.2276756"
+            ],
+            "rights": null,
+            "title": "Flickr Photo Analysis, On site surveys, and Station Assessments for Tillamook Bay and Tampa Bay "
         },
         {
-            "title": "Insect-Mediated Contaminant Flux model parameters and outputs",
-            "description": "Insect-Mediated Contaminant Flux model parameters and outputs. \n\nThis dataset is associated with the following publication:\nOlson, C.I., G.B. Beaubien, R.R. Otter, D.M. Walters, and M.A. Mills. Ecotoxicological Studies Indicate That Sublethal and Lethal Processes Limit Insect-Mediated Contaminant Flux.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(9): 1982-1992, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529846",
-            "keyword": [
-                "invertebrates",
-                "metals",
-                "Flux",
-                "bioaccumulation"
-            ],
             "contactPoint": {
                 "fn": "Gale Beaubien",
                 "hasEmail": "mailto:beaubien.gale@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529846/documents/Data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Insect-Mediated Contaminant Flux model parameters and outputs. \n\nThis dataset is associated with the following publication:\nOlson, C.I., G.B. Beaubien, R.R. Otter, D.M. Walters, and M.A. Mills. Ecotoxicological Studies Indicate That Sublethal and Lethal Processes Limit Insect-Mediated Contaminant Flux.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(9): 1982-1992, (2023).",
             "distribution": [
                 {
-                    "title": "Metadata for scihub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529846/Metadata%20for%20scihub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Metadata for scihub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529846",
+            "keyword": [
+                "invertebrates",
+                "metals",
+                "Flux",
+                "bioaccumulation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-09-01",
-            "references": [
-                "https://doi.org/10.1002/etc.5574"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186579,61 +186575,63 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1529846/documents/Data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1002/etc.5574"
+            ],
+            "rights": null,
+            "title": "Insect-Mediated Contaminant Flux model parameters and outputs"
         },
         {
-            "title": "Clean Air Status and Trends Network (CASTNET) hourly temperature and other meteorological data (1990 - present)",
-            "description": "Hourly temperature data and other meteorological data (e.g., relative humidity, solar radiation, precipitation, wind direction) are provided at long-term rural air monitoring sites. There are more than 90 CASTNET sites reporting hourly temperature data throughout the United States. These data can be used to assess climate impacts on air quality and trends in temperature from long-term monitoring sites. Meteorological sensors are calibrated to NIST traceable standards. Site location information is included with this dataset. The QAPP and associated SOPs can be found on the CASTNET website: www.epa.gov/castnet/documents-reports. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529853",
-            "keyword": [
-                "Clean Air Status and Trends Network (CASTNET)",
-                "air quality",
-                "air temperature",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Melissa Puchalski",
                 "hasEmail": "mailto:puchalski.melissa@epa.gov"
             },
+            "description": "Hourly temperature data and other meteorological data (e.g., relative humidity, solar radiation, precipitation, wind direction) are provided at long-term rural air monitoring sites. There are more than 90 CASTNET sites reporting hourly temperature data throughout the United States. These data can be used to assess climate impacts on air quality and trends in temperature from long-term monitoring sites. Meteorological sensors are calibrated to NIST traceable standards. Site location information is included with this dataset. The QAPP and associated SOPs can be found on the CASTNET website: www.epa.gov/castnet/documents-reports. Citation information for this dataset can be found in Data.gov's References section.",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/castnet/CASTNET_Outgoing/data/metdata.zip",
-                    "accessURL": "https://gaftp.epa.gov/castnet/CASTNET_Outgoing/data/metdata.zip"
+                    "accessURL": "https://gaftp.epa.gov/castnet/CASTNET_Outgoing/data/metdata.zip",
+                    "title": "https://gaftp.epa.gov/castnet/CASTNET_Outgoing/data/metdata.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529853",
+            "keyword": [
+                "Clean Air Status and Trends Network (CASTNET)",
+                "air quality",
+                "air temperature",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-21",
-            "references": [
-                "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/site.zip"
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
+                "https://gaftp.epa.gov/Castnet/CASTNET_Outgoing/data/site.zip"
+            ],
+            "rights": null,
+            "title": "Clean Air Status and Trends Network (CASTNET) hourly temperature and other meteorological data (1990 - present)"
         },
         {
-            "title": "Anthropogenic salt cycle",
-            "description": "synthesis of global salt quantities and fluxes. This dataset is not publicly accessible because: maintained and owned by University of Maryland. It can be accessed through the following means: by contacting senior author. Format: excel spreadsheets of global salt quantities and fluxes. \n\nThis dataset is associated with the following publication:\nKaushal, S., G. Likens, P. Mayer, R. Shatkay, S. Shelton, S. Grant, R. Utz, A. Yaculak, C. Maas, J. Reimer, S. Bhide, J. Malin, and M. Rippy. The Anthropogenic Salt Cycle.   NATURE. Nature Publishing Group, New York, NY, USA, 4: 770-784, (2023).",
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
+                "fn": "Paul Mayer",
+                "hasEmail": "mailto:mayer.paul@epa.gov"
+            },
+            "description": "synthesis of global salt quantities and fluxes. This dataset is not publicly accessible because: maintained and owned by University of Maryland. It can be accessed through the following means: by contacting senior author. Format: excel spreadsheets of global salt quantities and fluxes. \n\nThis dataset is associated with the following publication:\nKaushal, S., G. Likens, P. Mayer, R. Shatkay, S. Shelton, S. Grant, R. Utz, A. Yaculak, C. Maas, J. Reimer, S. Bhide, J. Malin, and M. Rippy. The Anthropogenic Salt Cycle.   NATURE. Nature Publishing Group, New York, NY, USA, 4: 770-784, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529605",
             "keyword": [
                 "Freshwater",
@@ -186642,14 +186640,10 @@
                 "salt",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Paul Mayer",
-                "hasEmail": "mailto:mayer.paul@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-09-01",
-            "references": [
-                "https://doi.org/10.1038/s43017-023-00485-y"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186659,20 +186653,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s43017-023-00485-y"
+            ],
+            "rights": null,
+            "title": "Anthropogenic salt cycle"
         },
         {
-            "title": "Analysis of Microcystis aeruginosa physiology by spectral flow cytometry: Impact of chemical and light exposure",
-            "description": "Analysis of Microcystis aeruginosa physiology by spectral flow cytometry: Impact of chemical and light exposure. new technique to observe photosynthesis to monitor the health or cyanobacteria and their reaction to hydrogen peroxide. This dataset is not publicly accessible because: The public would require specialized software in order to view and interpret files. It can be accessed through the following means: Email zucker.robert@epa.gov. Format: The data in the paper is acquired in proprietary format from the manufacturer of the equipment. This data presented in the paper can be read only by using the software from the manufacturer which is quite costly and not feasible to purchase unless the  scientist owns the equipment. \n\nThis dataset is associated with the following publication:\nBrentjens, E., E. Beall, and R. Zucker. Analysis of Microcystis aeruginosa physiology by spectral flow cytometry: Impact of chemical and light exposure.   PLOS Water. Public Library of Science, San Francisco, CA, USA, 2(10): e0000177, (2023).",
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
+                "fn": "Robert Zucker",
+                "hasEmail": "mailto:zucker.robert@epa.gov"
+            },
+            "description": "Analysis of Microcystis aeruginosa physiology by spectral flow cytometry: Impact of chemical and light exposure. new technique to observe photosynthesis to monitor the health or cyanobacteria and their reaction to hydrogen peroxide. This dataset is not publicly accessible because: The public would require specialized software in order to view and interpret files. It can be accessed through the following means: Email zucker.robert@epa.gov. Format: The data in the paper is acquired in proprietary format from the manufacturer of the equipment. This data presented in the paper can be read only by using the software from the manufacturer which is quite costly and not feasible to purchase unless the  scientist owns the equipment. \n\nThis dataset is associated with the following publication:\nBrentjens, E., E. Beall, and R. Zucker. Analysis of Microcystis aeruginosa physiology by spectral flow cytometry: Impact of chemical and light exposure.   PLOS Water. Public Library of Science, San Francisco, CA, USA, 2(10): e0000177, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1527900",
             "keyword": [
                 "flow cytometry",
@@ -186683,14 +186681,10 @@
                 "Light scatter",
                 "Autofluoresence"
             ],
-            "contactPoint": {
-                "fn": "Robert Zucker",
-                "hasEmail": "mailto:zucker.robert@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-29",
-            "references": [
-                "https://doi.org/10.1371/journal.pwat.0000177"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186700,19 +186694,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pwat.0000177"
+            ],
+            "rights": null,
+            "title": "Analysis of Microcystis aeruginosa physiology by spectral flow cytometry: Impact of chemical and light exposure"
         },
         {
-            "title": "Spatial and Temporal Variability in Stream Thermal Regime Drivers for Three River Networks During the Summer Growing Season",
-            "description": "Many aquatic organisms adapted to cold-water habitats are suffering habitat losses and population declines during warm seasons when water temperatures are increasing above thermal tolerances. Therefore, identifying the mechanisms driving local and regional stream temperature regimes are useful for implementing targeted restoration and management activities at appropriate scales to help mitigate cold-water habitat loss. Controls on stream temperature vary across landscapes but also temporally within basins during ecologically important growing seasons. We developed a modeling process that identified statistical relationships between potential drivers of stream temperature and incorporated management-related covariates that could be adjusted as part of restoration planning scenarios. We tested this model development process in three river networks of the Pacific Northwest with pre-existing temperature total maximum daily loads for protecting cold-water habitat during three months of the growing season (May [start], August [warmest], and September [end]). When averaged across months and the three river networks, the covariates in our models with the highest relative importance represented the physical landscape (elevation [1st], catchment area [3rd], main channel slope [5th]) and temporally-variable climate covariates (mean monthly air temperature [2nd], and mean monthly discharge [4th]). Management-related covariates such as ground water use (6th) and riparian shade (7th) were of lesser but still significant relative importance. However, variation in the importance of covariates through time and among the river networks indicates that local nuances are important and should be addressed when planning restoration activities. The modeling process we developed demonstrated its ability to identify regional (similar across study areas) and local (unique to each study area) relationships among multiple drivers of stream temperature across complex landscapes. The data included provides the necessary inputs, code, and metadata for reproducing the models and output from this study. \n\nThis dataset is associated with the following publication:\nFuller, M., N. Detenbeck, P. Leinenbach, R. Labiosa, and D. Isaak. Spatial and temporal variability in stream thermal regime drivers for three river networks during the summer growing season.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA,  1-22, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Matthew Fuller",
+                "hasEmail": "mailto:fuller.matthew@epa.gov"
+            },
+            "description": "Many aquatic organisms adapted to cold-water habitats are suffering habitat losses and population declines during warm seasons when water temperatures are increasing above thermal tolerances. Therefore, identifying the mechanisms driving local and regional stream temperature regimes are useful for implementing targeted restoration and management activities at appropriate scales to help mitigate cold-water habitat loss. Controls on stream temperature vary across landscapes but also temporally within basins during ecologically important growing seasons. We developed a modeling process that identified statistical relationships between potential drivers of stream temperature and incorporated management-related covariates that could be adjusted as part of restoration planning scenarios. We tested this model development process in three river networks of the Pacific Northwest with pre-existing temperature total maximum daily loads for protecting cold-water habitat during three months of the growing season (May [start], August [warmest], and September [end]). When averaged across months and the three river networks, the covariates in our models with the highest relative importance represented the physical landscape (elevation [1st], catchment area [3rd], main channel slope [5th]) and temporally-variable climate covariates (mean monthly air temperature [2nd], and mean monthly discharge [4th]). Management-related covariates such as ground water use (6th) and riparian shade (7th) were of lesser but still significant relative importance. However, variation in the importance of covariates through time and among the river networks indicates that local nuances are important and should be addressed when planning restoration activities. The modeling process we developed demonstrated its ability to identify regional (similar across study areas) and local (unique to each study area) relationships among multiple drivers of stream temperature across complex landscapes. The data included provides the necessary inputs, code, and metadata for reproducing the models and output from this study. \n\nThis dataset is associated with the following publication:\nFuller, M., N. Detenbeck, P. Leinenbach, R. Labiosa, and D. Isaak. Spatial and temporal variability in stream thermal regime drivers for three river networks during the summer growing season.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA,  1-22, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524755/JAWRAms_EPAImpactStatement_ScienceHubDOImetadatafields.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "JAWRAms_EPAImpactStatement_ScienceHubDOImetadatafields.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1524755",
             "keyword": [
@@ -186723,21 +186727,10 @@
                 "information criterion",
                 "covariate relative importance"
             ],
-            "contactPoint": {
-                "fn": "Matthew Fuller",
-                "hasEmail": "mailto:fuller.matthew@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "JAWRAms_EPAImpactStatement_ScienceHubDOImetadatafields.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524755/JAWRAms_EPAImpactStatement_ScienceHubDOImetadatafields.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-03-11",
-            "references": [
-                "https://doi.org/10.1111/1752-1688.13158",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10631548"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186747,19 +186740,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/1752-1688.13158",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10631548"
+            ],
+            "rights": null,
+            "title": "Spatial and Temporal Variability in Stream Thermal Regime Drivers for Three River Networks During the Summer Growing Season"
         },
         {
-            "title": "National Coastal Condition Assessment 2015 Datafiles for Report \u201cNational Coastal Condition Assessment: A Collaborative Survey of the Nation's Estuaries and Nearshore Great Lakes\u201d",
-            "description": "National Coastal Condition Assessment 2015 Datafiles for Report \u201cNational Coastal Condition Assessment: A Collaborative Survey of the Nation's Estuaries and Nearshore Great Lakes\u201d: The National Coastal Condition Assessment (NCCA) is a statistical survey of the condition of our nation's estuaries and nearshore Great Lake waters. It is designed to provide information on the extent of coastal waters that support healthy biological condition and recreation, estimate how widespread major stressors are that impact estuarine and Great Lake nearshore water quality, and provide insight into whether these resources nationwide are getting cleaner. These datasets are archived (zipped) files comprised of chemical, physical and biological files used in developing the NCCA 2015 report. There is a zipped file for estuaries and one for Great Lakes. \nSampling was conducted in the summer of 2015 at approximately 1000 sites in the conterminous United States. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic invertebrates, physical habitat, secchi/PAR data, sediment chemistry, sediment toxicity, contaminants in fish tissue, microcystins, etc. Users are encouraged to visit the NARS data webpage for updates to data files  and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys\n\nCitation for the NCCA 2015 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Coastal Condition Assessment 2015 Report. Great Lakes Archived Data OR Estuarine Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-coastal-condition-assessment-2015. DOI: 10.23719/1529844\n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Coastal Condition Assessment 2015 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d\n\nAdditional information: NCCA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Hugh Sullivan",
+                "hasEmail": "mailto:sullivan.hugh@epa.gov"
+            },
+            "description": "National Coastal Condition Assessment 2015 Datafiles for Report \u201cNational Coastal Condition Assessment: A Collaborative Survey of the Nation's Estuaries and Nearshore Great Lakes\u201d: The National Coastal Condition Assessment (NCCA) is a statistical survey of the condition of our nation's estuaries and nearshore Great Lake waters. It is designed to provide information on the extent of coastal waters that support healthy biological condition and recreation, estimate how widespread major stressors are that impact estuarine and Great Lake nearshore water quality, and provide insight into whether these resources nationwide are getting cleaner. These datasets are archived (zipped) files comprised of chemical, physical and biological files used in developing the NCCA 2015 report. There is a zipped file for estuaries and one for Great Lakes. \nSampling was conducted in the summer of 2015 at approximately 1000 sites in the conterminous United States. Sites were selected using a statistical survey (probabilistic) design. The files include water chemistry, profile data, benthic invertebrates, physical habitat, secchi/PAR data, sediment chemistry, sediment toxicity, contaminants in fish tissue, microcystins, etc. Users are encouraged to visit the NARS data webpage for updates to data files  and data from other surveys. https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys\n\nCitation for the NCCA 2015 archived data: U.S. Environmental Protection Agency. National Aquatic Resource Surveys. National Coastal Condition Assessment 2015 Report. Great Lakes Archived Data OR Estuarine Archived Data. (INSERT data and metadata files used). Available from U.S. EPA web page: https://www.epa.gov/national-aquatic-resource-surveys/reports-and-data-national-coastal-condition-assessment-2015. DOI: 10.23719/1529844\n\nEPA encourages users who are publishing subsets of the data (say as part of a journal article publication) to include the above citation. EPA also encourages users of the data to include the following acknowledgement: \u201cThe National Coastal Condition Assessment 2015 data were a result of the collective efforts of dedicated field crews, laboratory staff, data management and quality control staff, analysts and many others from EPA, states, tribes, federal agencies, universities, and other organizations. Please contact nars-hq@epa.gov with any questions.\u201d\n\nAdditional information: NCCA is part of the National Aquatic Resource Surveys, an EPA/State/Tribal partnership. The National Aquatic Resource Surveys (NARS) are statistical surveys designed to assess the status of and changes in quality of the nation\u2019s coastal waters, lakes and reservoirs, rivers and streams, and wetlands. Using sample sites selected at random, these surveys provide a snapshot of the overall condition of the nation\u2019s water. Because the surveys use standardized field and lab methods, we can compare results from different parts of the country and between years. Citation information for this dataset can be found in Data.gov's References section.",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529844/ncca_2015_greatlakes_alldatafiles.zip",
+                    "mediaType": "application/zip",
+                    "title": "ncca_2015_greatlakes_alldatafiles.zip"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529844/ncca_2015_estuarine_alldatafiles-1.zip",
+                    "mediaType": "application/zip",
+                    "title": "ncca_2015_estuarine_alldatafiles-1.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529844",
             "keyword": [
@@ -186779,46 +186792,36 @@
                 "nearshore",
                 "EPA"
             ],
-            "contactPoint": {
-                "fn": "Hugh Sullivan",
-                "hasEmail": "mailto:sullivan.hugh@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
-                },
-                {
-                    "title": "ncca_2015_greatlakes_alldatafiles.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529844/ncca_2015_greatlakes_alldatafiles.zip",
-                    "mediaType": "application/zip"
-                },
-                {
-                    "title": "ncca_2015_estuarine_alldatafiles-1.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529844/ncca_2015_estuarine_alldatafiles-1.zip",
-                    "mediaType": "application/zip"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-11-01",
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
+            "title": "National Coastal Condition Assessment 2015 Datafiles for Report \u201cNational Coastal Condition Assessment: A Collaborative Survey of the Nation's Estuaries and Nearshore Great Lakes\u201d"
         },
         {
-            "title": "Datasets for Spatial and Temporal Variations of Estuarine Stratification and Flushing Time across the Continental U.S.",
-            "description": "These datasets provide the raw and preprocessed data required to calculate estuarine stratification indices and estimates of flushing time for estuaries across the United States, as well as time series of the indices themselves.  Data are available through the EPA's Estuary Data Mapper. \n\nThis dataset is associated with the following publication:\nShen, X., N. Detenbeck, and M. You. Spatial and temporal variations of estuarine stratification and flushing time across the continental U.S..   Estuarine Coastal and Shelf Science. Elsevier Science Ltd, New York, NY, USA, 279: 108147, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "These datasets provide the raw and preprocessed data required to calculate estuarine stratification indices and estimates of flushing time for estuaries across the United States, as well as time series of the indices themselves.  Data are available through the EPA's Estuary Data Mapper. \n\nThis dataset is associated with the following publication:\nShen, X., N. Detenbeck, and M. You. Spatial and temporal variations of estuarine stratification and flushing time across the continental U.S..   Estuarine Coastal and Shelf Science. Elsevier Science Ltd, New York, NY, USA, 279: 108147, (2022).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/edm",
+                    "title": "https://www.epa.gov/edm"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529836",
             "keyword": [
@@ -186830,20 +186833,10 @@
                 "Nitrogen and Co-pollutants",
                 "variability"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/edm",
-                    "accessURL": "https://www.epa.gov/edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-02-25",
-            "references": [
-                "https://doi.org/10.1016/j.ecss.2022.108147",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9762436"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186853,19 +186846,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecss.2022.108147",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9762436"
+            ],
+            "rights": null,
+            "title": "Datasets for Spatial and Temporal Variations of Estuarine Stratification and Flushing Time across the Continental U.S."
         },
         {
-            "title": "Data for Use of historical isoscapes to develop an estuarine nutrient baseline",
-            "description": "Coastal eutrophication is a prevalent threat to the healthy functioning of ecosystems globally. While degraded water quality can be detected by monitoring oxygen, nutrient concentrations, and algal abundance, establishing regulatory guidelines is complicated by a lack of baseline data (e.g., pre-Anthropocene). We use historical carbon and nitrogen isoscapes from sediment cores to reconstruct spatial and temporal changes in nutrient dynamics for a central California estuary, where development and agriculture dramatically enhanced nutrient inputs over the past century. We found strong contrasts between current sediment stable isotopes and those from the recent past, demonstrating shifts exceeding those in previously studied eutrophic estuaries and substantial increases in nutrient inputs. Comparisons of contemporary with historical isoscapes also revealed that nitrogen sources shifted from a marine-terrestrial gradient to amplified denitrification at the head and mouth of the estuary. Geospatial analysis of historical data suggests that an increase in fertilizer application \u2013 rather than population growth or increases in the extent of cultivated land \u2013 is chiefly responsible for increasing nutrient loads during the 20th century. This study demonstrates the ability of isotopic and stoichiometric maps to provide important perspectives on long-term shifts and spatial patterns of nutrients that can be used to improve management of nutrient pollution. \n\nThis dataset is associated with the following publication:\nChamplin, L., A. Woolfolk, A. Oczkowski, A. Rittenhouse, A. Gray, K. Wasson, F. Rahman, P. Zelanko, N. Quintana Krupinski, R. Jeppesen, J. Haskins, and E. Watson. Use of historical isoscapes to develop an estuarine nutrient baseline.   Frontiers in Marine Science. Frontiers, Lausanne,  SWITZERLAND, 10: 1257015, (2023).",
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
+            "describedBy": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.3ffbg79q6",
+            "description": "Coastal eutrophication is a prevalent threat to the healthy functioning of ecosystems globally. While degraded water quality can be detected by monitoring oxygen, nutrient concentrations, and algal abundance, establishing regulatory guidelines is complicated by a lack of baseline data (e.g., pre-Anthropocene). We use historical carbon and nitrogen isoscapes from sediment cores to reconstruct spatial and temporal changes in nutrient dynamics for a central California estuary, where development and agriculture dramatically enhanced nutrient inputs over the past century. We found strong contrasts between current sediment stable isotopes and those from the recent past, demonstrating shifts exceeding those in previously studied eutrophic estuaries and substantial increases in nutrient inputs. Comparisons of contemporary with historical isoscapes also revealed that nitrogen sources shifted from a marine-terrestrial gradient to amplified denitrification at the head and mouth of the estuary. Geospatial analysis of historical data suggests that an increase in fertilizer application \u2013 rather than population growth or increases in the extent of cultivated land \u2013 is chiefly responsible for increasing nutrient loads during the 20th century. This study demonstrates the ability of isotopic and stoichiometric maps to provide important perspectives on long-term shifts and spatial patterns of nutrients that can be used to improve management of nutrient pollution. \n\nThis dataset is associated with the following publication:\nChamplin, L., A. Woolfolk, A. Oczkowski, A. Rittenhouse, A. Gray, K. Wasson, F. Rahman, P. Zelanko, N. Quintana Krupinski, R. Jeppesen, J. Haskins, and E. Watson. Use of historical isoscapes to develop an estuarine nutrient baseline.   Frontiers in Marine Science. Frontiers, Lausanne,  SWITZERLAND, 10: 1257015, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.3ffbg79q6",
+                    "title": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.3ffbg79q6"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529782",
             "keyword": [
@@ -186878,20 +186882,10 @@
                 "estuary",
                 "Nitrogen and Co-pollutants"
             ],
-            "contactPoint": {
-                "fn": "Autumn Oczkowski",
-                "hasEmail": "mailto:oczkowski.autumn@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.3ffbg79q6",
-                    "accessURL": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.3ffbg79q6"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-16",
-            "references": [
-                "https://doi.org/10.3389/fmars.2023.1257015",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10563801"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186902,42 +186896,42 @@
                     }
                 }
             },
-            "describedBy": "https://datadryad.org/stash/dataset/doi:10.5061/dryad.3ffbg79q6"
+            "references": [
+                "https://doi.org/10.3389/fmars.2023.1257015",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10563801"
+            ],
+            "rights": null,
+            "title": "Data for Use of historical isoscapes to develop an estuarine nutrient baseline"
         },
         {
-            "title": "Persistence and decontamination efficacy data of select chemical warfare agent simulants",
-            "description": "Persistence and decontamination efficacy data of three select chemical warfare agent simulants. \n\nThis dataset is associated with the following publication:\nOudejans, L., B. Wyrzykowska, E. Morris, S. Jackson, A. Touati, J. Sawyer, A. Mikelonis, and S. Serre. Evaluation of Malathion, DIMP, and Strawberry Furanone as CWA Simulants for Consideration in Field-Level Interior Building Remediation Exercises.   ACS Chemical Health & Safety. American Chemical Society, Washington, DC, USA, 30(5): 270-278, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528643",
-            "keyword": [
-                "simulant",
-                "Persistence",
-                "Decontamination",
-                "Indoor outdoor decontamination",
-                "Exercise"
-            ],
             "contactPoint": {
                 "fn": "Lukas Oudejans",
                 "hasEmail": "mailto:oudejans.lukas@epa.gov"
             },
+            "description": "Persistence and decontamination efficacy data of three select chemical warfare agent simulants. \n\nThis dataset is associated with the following publication:\nOudejans, L., B. Wyrzykowska, E. Morris, S. Jackson, A. Touati, J. Sawyer, A. Mikelonis, and S. Serre. Evaluation of Malathion, DIMP, and Strawberry Furanone as CWA Simulants for Consideration in Field-Level Interior Building Remediation Exercises.   ACS Chemical Health & Safety. American Chemical Society, Washington, DC, USA, 30(5): 270-278, (2023).",
             "distribution": [
                 {
-                    "title": "Simulant Selection Manuscript_Complete Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528643/Simulant%20Selection%20Manuscript_Complete%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Simulant Selection Manuscript_Complete Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528643",
+            "keyword": [
+                "simulant",
+                "Persistence",
+                "Decontamination",
+                "Indoor outdoor decontamination",
+                "Exercise"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-05",
-            "references": [
-                "https://doi.org/10.1021/acs.chas.3c00029"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -186947,51 +186941,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.chas.3c00029"
+            ],
+            "rights": null,
+            "title": "Persistence and decontamination efficacy data of select chemical warfare agent simulants"
         },
         {
-            "title": "Supporting dataset for manuscript \"Spatial analysis of future climate risk to stormwater infrastructure\"",
-            "description": "This dataset contains model simulation results described in the article \"Spatial analysis of future climate risk to stormwater infrastructure\". Simulations were  conducted for 2,509 weather stations located across the U.S. where NOAA Atlas 14 precipitation statistics are available. Simulations were not conducted in northwest States because the methodology requires NOAA Atlas 14 statistics which are not available in this region. Climate change scenarios are based on LOCA-downscaled CMIP5 GCM output for mid-century. Scenarios evaluated represent the 90th, median, and 10th percentile GCMs across the LOCA ensemble for each Atlas 14 location and recurrence interval, for event durations from 1 to 24 hours and recurrence intervals from 2 to 100 years. Future precipitation estimates are converted to runoff with EPA\u2019s Storm Water Management Model version 5 (SWMM5) on a unit-area basis for a simple generic catchment.  We evaluate the effects of changes in specific duration-frequency events on wet detention and bioretention based stormwater BMPs. \n\nThis dataset is associated with the following publication:\nButcher, J., S. Sarkar, T. Johnson, and A. Shabani. Spatial Analysis of Future Climate Risk to Stormwater Infrastructure.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA,  1-14, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1524746",
-            "keyword": [
-                "stormwater",
-                "adaptation",
-                "bmp",
-                "climate change"
-            ],
             "contactPoint": {
                 "fn": "Thomas Johnson",
                 "hasEmail": "mailto:johnson.thomas@epa.gov"
             },
+            "description": "This dataset contains model simulation results described in the article \"Spatial analysis of future climate risk to stormwater infrastructure\". Simulations were  conducted for 2,509 weather stations located across the U.S. where NOAA Atlas 14 precipitation statistics are available. Simulations were not conducted in northwest States because the methodology requires NOAA Atlas 14 statistics which are not available in this region. Climate change scenarios are based on LOCA-downscaled CMIP5 GCM output for mid-century. Scenarios evaluated represent the 90th, median, and 10th percentile GCMs across the LOCA ensemble for each Atlas 14 location and recurrence interval, for event durations from 1 to 24 hours and recurrence intervals from 2 to 100 years. Future precipitation estimates are converted to runoff with EPA\u2019s Storm Water Management Model version 5 (SWMM5) on a unit-area basis for a simple generic catchment.  We evaluate the effects of changes in specific duration-frequency events on wet detention and bioretention based stormwater BMPs. \n\nThis dataset is associated with the following publication:\nButcher, J., S. Sarkar, T. Johnson, and A. Shabani. Spatial Analysis of Future Climate Risk to Stormwater Infrastructure.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA,  1-14, (2023).",
             "distribution": [
                 {
-                    "title": "DetentionAnalysis_ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524746/DetentionAnalysis_ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DetentionAnalysis_ScienceHub.xlsx"
                 },
                 {
-                    "title": "BioretentionAnalysis_ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524746/BioretentionAnalysis_ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "BioretentionAnalysis_ScienceHub.xlsx"
                 },
                 {
-                    "title": "StationLocations_ScienceHub_v2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1524746/StationLocations_ScienceHub_v2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StationLocations_ScienceHub_v2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1524746",
+            "keyword": [
+                "stormwater",
+                "adaptation",
+                "bmp",
+                "climate change"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-03-08",
-            "references": [
-                "https://doi.org/10.1111/1752-1688.13132"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187001,41 +186995,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/1752-1688.13132"
+            ],
+            "rights": null,
+            "title": "Supporting dataset for manuscript \"Spatial analysis of future climate risk to stormwater infrastructure\""
         },
         {
-            "title": "Pesticide Residues in Honey Bee (Apis mellifera) Pollen collected in Two Ornamental Plant Nurseries in Connecticut: Implications for Bee Health and Risk Assessment",
-            "description": "These data were collected as part of RARE project with the Connecticut Agricultural Experiment Station. For this work, pollen was collected from honey bee colonies located at two ornamental plant nurseries in Connecticut. The pollen was analyzed for pesticide residues (type and quantity). Aggregate risk quotients for honey bee adults and larvae were calculated using these data. \n\nThis dataset is associated with the following publication:\nHester, K., K. Stoner, B. Eitzer, R. Koethe, and D. Lehmann. Pesticide Residues in Honey Bee (Apis mellifera) Pollen collected in Two Ornamental Plant Nurseries in Connecticut: Implications for Bee Health and Risk Assessment.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 333: 122037, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528641",
-            "keyword": [
-                "Risk Assessment",
-                "honey bee",
-                "pesticide",
-                "ornamental plant nursery"
-            ],
             "contactPoint": {
                 "fn": "David Lehmann",
                 "hasEmail": "mailto:lehmann.david@epa.gov"
             },
+            "description": "These data were collected as part of RARE project with the Connecticut Agricultural Experiment Station. For this work, pollen was collected from honey bee colonies located at two ornamental plant nurseries in Connecticut. The pollen was analyzed for pesticide residues (type and quantity). Aggregate risk quotients for honey bee adults and larvae were calculated using these data. \n\nThis dataset is associated with the following publication:\nHester, K., K. Stoner, B. Eitzer, R. Koethe, and D. Lehmann. Pesticide Residues in Honey Bee (Apis mellifera) Pollen collected in Two Ornamental Plant Nurseries in Connecticut: Implications for Bee Health and Risk Assessment.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 333: 122037, (2023).",
             "distribution": [
                 {
-                    "title": "SciHub_DataEntry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528641/SciHub_DataEntry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub_DataEntry.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528641",
+            "keyword": [
+                "Risk Assessment",
+                "honey bee",
+                "pesticide",
+                "ornamental plant nursery"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-03-03",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2023.122037"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187045,19 +187039,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2023.122037"
+            ],
+            "rights": null,
+            "title": "Pesticide Residues in Honey Bee (Apis mellifera) Pollen collected in Two Ornamental Plant Nurseries in Connecticut: Implications for Bee Health and Risk Assessment"
         },
         {
-            "title": "2016 EPA National Wetland Condition Assessment water quality data",
-            "description": "EPA's 2016 National Wetland Condition Assessment sampled wetlands across the conterminous USA for vegetation, soils, water chemistry, and anthropogenic impacts.  Data for all of these elements of the 2016 NWCA survey are available from the EPA NARS website.  This particular publication uses the water chemistry data and the anthropogenic impacts data, as well as the general site data that describes sampling locations, wetland type classifications, etc. \n\nThis dataset is associated with the following publication:\nTrebitz, A., and A. Herlihy. Wetland water quality patterns and anthropogenic pressure associations across the continental USA.   WETLANDS. The Society of Wetland Scientists, McLean, VA, USA,  N/A, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Anett Trebitz",
+                "hasEmail": "mailto:trebitz.anett@epa.gov"
+            },
+            "description": "EPA's 2016 National Wetland Condition Assessment sampled wetlands across the conterminous USA for vegetation, soils, water chemistry, and anthropogenic impacts.  Data for all of these elements of the 2016 NWCA survey are available from the EPA NARS website.  This particular publication uses the water chemistry data and the anthropogenic impacts data, as well as the general site data that describes sampling locations, wetland type classifications, etc. \n\nThis dataset is associated with the following publication:\nTrebitz, A., and A. Herlihy. Wetland water quality patterns and anthropogenic pressure associations across the continental USA.   WETLANDS. The Society of Wetland Scientists, McLean, VA, USA,  N/A, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529864",
             "keyword": [
@@ -187070,19 +187073,10 @@
                 "spatial scale",
                 "connectivity"
             ],
-            "contactPoint": {
-                "fn": "Anett Trebitz",
-                "hasEmail": "mailto:trebitz.anett@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-01",
-            "references": [
-                "https://doi.org/10.1007/s13157-023-01754-8"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187092,121 +187086,123 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s13157-023-01754-8"
+            ],
+            "rights": null,
+            "title": "2016 EPA National Wetland Condition Assessment water quality data"
         },
         {
-            "title": "Dynamically Downscaled Projections of Phenological Changes across the Contiguous United States ",
-            "description": "This study examines how phenological indicators, which track the life cycles of plants and animals, could change from 2025\u20132100 as simulated in a regional climate model over the contiguous U.S.  Chilling units quantify the presence of cooler weather that can benefit plants prior to their growing season.  They are projected to decrease in the southern U.S., possibly inhibiting agricultural production.  Spring onset is projected to occur earlier in the year, advancing by 1\u20134 days on average over each future decade.  Risk of false springs (damaging hard freezes after spring onset) increases in the western U.S.  Our findings highlight the need to understand effects of climate change during transitional seasons, which can impact agriculture and ecosystems. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528766",
-            "keyword": [
-                "Spring onset",
-                "regional climate model",
-                "dynamical downscaling",
-                "Chilling Requirement"
-            ],
             "contactPoint": {
                 "fn": "Megan Mallard",
                 "hasEmail": "mailto:mallard.megan@epa.gov"
             },
+            "description": "This study examines how phenological indicators, which track the life cycles of plants and animals, could change from 2025\u20132100 as simulated in a regional climate model over the contiguous U.S.  Chilling units quantify the presence of cooler weather that can benefit plants prior to their growing season.  They are projected to decrease in the southern U.S., possibly inhibiting agricultural production.  Spring onset is projected to occur earlier in the year, advancing by 1\u20134 days on average over each future decade.  Risk of false springs (damaging hard freezes after spring onset) increases in the western U.S.  Our findings highlight the need to understand effects of climate change during transitional seasons, which can impact agriculture and ecosystems. ",
             "distribution": [
                 {
-                    "title": "https://www2.mmm.ucar.edu/wrf/users/download/get_source.html",
-                    "accessURL": "https://www2.mmm.ucar.edu/wrf/users/download/get_source.html"
+                    "accessURL": "https://www2.mmm.ucar.edu/wrf/users/download/get_source.html",
+                    "title": "https://www2.mmm.ucar.edu/wrf/users/download/get_source.html"
                 },
                 {
-                    "title": "https://www.usanpn.org/geoserver-request-builder",
-                    "accessURL": "https://www.usanpn.org/geoserver-request-builder"
+                    "accessURL": "https://www.usanpn.org/geoserver-request-builder",
+                    "title": "https://www.usanpn.org/geoserver-request-builder"
                 },
                 {
-                    "title": "https://github.com/usa-npn/gridded_models",
-                    "accessURL": "https://github.com/usa-npn/gridded_models"
+                    "accessURL": "https://github.com/usa-npn/gridded_models",
+                    "title": "https://github.com/usa-npn/gridded_models"
                 },
                 {
-                    "title": "https://prism.oregonstate.edu/",
-                    "accessURL": "https://prism.oregonstate.edu/"
+                    "accessURL": "https://prism.oregonstate.edu/",
+                    "title": "https://prism.oregonstate.edu/"
                 },
                 {
-                    "title": "Fig5.spring_index.gfdl_rcp8.5.part2.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5.spring_index.gfdl_rcp8.5.part2.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5.spring_index.gfdl_rcp8.5.part2.tar"
                 },
                 {
-                    "title": "Fig5.spring_index.gfdl_rcp8.5.part1.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5.spring_index.gfdl_rcp8.5.part1.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5.spring_index.gfdl_rcp8.5.part1.tar"
                 },
                 {
-                    "title": "Fig5.spring_index.cesm_rcp8.5.part2.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5.spring_index.cesm_rcp8.5.part2.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5.spring_index.cesm_rcp8.5.part2.tar"
                 },
                 {
-                    "title": "Fig5.spring_index.cesm_rcp8.5.part1.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5.spring_index.cesm_rcp8.5.part1.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5.spring_index.cesm_rcp8.5.part1.tar"
                 },
                 {
-                    "title": "Fig5.spring_index.cesm_rcp4.5.part2.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5.spring_index.cesm_rcp4.5.part2.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5.spring_index.cesm_rcp4.5.part2.tar"
                 },
                 {
-                    "title": "Fig5.spring_index.cesm_rcp4.5.part1.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5.spring_index.cesm_rcp4.5.part1.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5.spring_index.cesm_rcp4.5.part1.tar"
                 },
                 {
-                    "title": "Fig5_wrf-gfdl_historical.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5_wrf-gfdl_historical.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5_wrf-gfdl_historical.tar"
                 },
                 {
-                    "title": "Fig5_wrf-cesm_historical.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig5_wrf-cesm_historical.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig5_wrf-cesm_historical.tar"
                 },
                 {
-                    "title": "tables.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/tables.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "tables.tar"
                 },
                 {
-                    "title": "Fig6.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig6.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig6.tar"
                 },
                 {
-                    "title": "Fig4.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig4.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig4.tar"
                 },
                 {
-                    "title": "Fig3.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig3.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig3.tar"
                 },
                 {
-                    "title": "Fig2.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/Fig2.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "Fig2.tar"
                 },
                 {
-                    "title": "fig1.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528766/fig1.tar",
-                    "mediaType": "application/x-gtar"
+                    "mediaType": "application/x-gtar",
+                    "title": "fig1.tar"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528766",
+            "keyword": [
+                "Spring onset",
+                "regional climate model",
+                "dynamical downscaling",
+                "Chilling Requirement"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-04",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -187215,19 +187211,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Dynamically Downscaled Projections of Phenological Changes across the Contiguous United States "
         },
         {
-            "title": "Large Mid Columbia Spatial Stream Data",
-            "description": "This is the Mid Columbia stream network used in the application section of the journal article. \n\nThis dataset is associated with the following publication:\nVer Hoef, J., M. Dumelle, M. Higham, E. Peterson, and D. Isaak. Indexing and Partitioning the Spatial Linear Model for Large Data Sets.   PLOS ONE. Public Library of Science, San Francisco, CA, USA, 18(11): e0291906, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Michael Dumelle",
+                "hasEmail": "mailto:dumelle.michael@epa.gov"
+            },
+            "description": "This is the Mid Columbia stream network used in the application section of the journal article. \n\nThis dataset is associated with the following publication:\nVer Hoef, J., M. Dumelle, M. Higham, E. Peterson, and D. Isaak. Indexing and Partitioning the Spatial Linear Model for Large Data Sets.   PLOS ONE. Public Library of Science, San Francisco, CA, USA, 18(11): e0291906, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://github.com/jayverhoef/midColumbiaLSN",
+                    "title": "https://github.com/jayverhoef/midColumbiaLSN"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529840",
             "keyword": [
@@ -187237,20 +187240,10 @@
                 "spatial data",
                 "Correlation"
             ],
-            "contactPoint": {
-                "fn": "Michael Dumelle",
-                "hasEmail": "mailto:dumelle.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://github.com/jayverhoef/midColumbiaLSN",
-                    "accessURL": "https://github.com/jayverhoef/midColumbiaLSN"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-11-14",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0291906",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619847"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187260,50 +187253,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0291906",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619847"
+            ],
+            "rights": null,
+            "title": "Large Mid Columbia Spatial Stream Data"
         },
         {
-            "title": "Lead and Arsenic X-ray absorption spectral models fit as linear combination of known standards",
-            "description": "In this study, smelter contaminated soil was treated with various soil amendments (ferric sulphate [Fe2(SO4)3], triple superphosphate [TSP] and biochar) to determine their efficacy in immobilizing soil lead (Pb) and arsenic (As). \nXAS were collected on soils and mine waste materials at the Materials Research Collaborative Access Team 10-BM for As and 10-ID for Pb, Advanced Photon Source at Argonne National Laboratory. \nArsenic XAS data collection at 10-BM was measured at the As K edge (11867 eV) using a 4-element Vortex fluorescence detector. Four layers of aluminum foil to filter out background fluorescence from iron and other elements in the samples. Three to five step scans were collected in fluorescence by Vortex detector at 45\u00b0 incident to sample and down beam transmission on energy calibration standard. Energy was calibrated to set at the 1st derivative inflection point zero of sodium arsenate standard to 11874 eV. Data were then background subtracted and converted to k space for EXAFS region analysis. Data processed for EXAFS analysis were k3-weighted and all e0 set to 11870 eV for uniform k range start energy. Spline range was 0.5-12 k. \nLead XAS data collection at 10-ID utilized a Si(111) mono to tune energy to the Pb L3-edge (13035 eV). Samples were measured in fluorescence using a Mirion-Canberra 7-element Ge detector at 45\u00b0 incident to the sample. For each sample, three to five scans were collected in both transmission and fluorescence mode with a Pb foil for reference sample. Calibration was performed by assigning the first derivative inflection point of Pb foil scan to 13035 eV. \nAnalysis of Pb spectra utilized LCF of the 1st derivative norm(E) from -20 to 80 eV from e0, constraints of all weights between 0 and 1 and sum of weights normalized to 1. Standards were sequentially removed based on statistical improvement of fit. Components contributing less than ten percent were removed, followed by refitting with remaining components. The combination of standards resulting in the lowest R-factor results for each sample was reported. Arsenic spectra were analyzed LCF utilizing the EXAFS range of spectra. Preliminary data checking indicated As oxidation states of all samples contained only AsV as confirmed by matching edge position with the sodium arsenate pellet used for energy calibration. As EXAFS range were utilized for quantitative speciation from a k-range of 3-10 \u00c5-1. \n\nThis dataset is associated with the following publication:\nAlankarage, D., A. Betts, K.G. Scheckel, C. Herde, M. Cavallaro, and A.L. Juhasz. Remediation options to reduce bioaccessible and bioavailable lead and arsenic at a smelter impacted site - consideration of treatment efficacy.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 341: 122881, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529350",
-            "keyword": [
-                "biochar",
-                "Bioaccessibility",
-                "arsenic",
-                "lead",
-                "relative bioavailability",
-                "immobilization",
-                "plumbojarosite",
-                "TSP"
-            ],
             "contactPoint": {
                 "fn": "Aaron Betts",
                 "hasEmail": "mailto:betts.aaron@epa.gov"
             },
+            "description": "In this study, smelter contaminated soil was treated with various soil amendments (ferric sulphate [Fe2(SO4)3], triple superphosphate [TSP] and biochar) to determine their efficacy in immobilizing soil lead (Pb) and arsenic (As). \nXAS were collected on soils and mine waste materials at the Materials Research Collaborative Access Team 10-BM for As and 10-ID for Pb, Advanced Photon Source at Argonne National Laboratory. \nArsenic XAS data collection at 10-BM was measured at the As K edge (11867 eV) using a 4-element Vortex fluorescence detector. Four layers of aluminum foil to filter out background fluorescence from iron and other elements in the samples. Three to five step scans were collected in fluorescence by Vortex detector at 45\u00b0 incident to sample and down beam transmission on energy calibration standard. Energy was calibrated to set at the 1st derivative inflection point zero of sodium arsenate standard to 11874 eV. Data were then background subtracted and converted to k space for EXAFS region analysis. Data processed for EXAFS analysis were k3-weighted and all e0 set to 11870 eV for uniform k range start energy. Spline range was 0.5-12 k. \nLead XAS data collection at 10-ID utilized a Si(111) mono to tune energy to the Pb L3-edge (13035 eV). Samples were measured in fluorescence using a Mirion-Canberra 7-element Ge detector at 45\u00b0 incident to the sample. For each sample, three to five scans were collected in both transmission and fluorescence mode with a Pb foil for reference sample. Calibration was performed by assigning the first derivative inflection point of Pb foil scan to 13035 eV. \nAnalysis of Pb spectra utilized LCF of the 1st derivative norm(E) from -20 to 80 eV from e0, constraints of all weights between 0 and 1 and sum of weights normalized to 1. Standards were sequentially removed based on statistical improvement of fit. Components contributing less than ten percent were removed, followed by refitting with remaining components. The combination of standards resulting in the lowest R-factor results for each sample was reported. Arsenic spectra were analyzed LCF utilizing the EXAFS range of spectra. Preliminary data checking indicated As oxidation states of all samples contained only AsV as confirmed by matching edge position with the sodium arsenate pellet used for energy calibration. As EXAFS range were utilized for quantitative speciation from a k-range of 3-10 \u00c5-1. \n\nThis dataset is associated with the following publication:\nAlankarage, D., A. Betts, K.G. Scheckel, C. Herde, M. Cavallaro, and A.L. Juhasz. Remediation options to reduce bioaccessible and bioavailable lead and arsenic at a smelter impacted site - consideration of treatment efficacy.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 341: 122881, (2024).",
             "distribution": [
                 {
-                    "title": "Pb_Dileepa_XAS_LCF.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529350/Pb_Dileepa_XAS_LCF.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Pb_Dileepa_XAS_LCF.zip"
                 },
                 {
-                    "title": "As_Dileepa_XAS_LCF.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529350/As_Dileepa_XAS_LCF.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "As_Dileepa_XAS_LCF.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529350",
+            "keyword": [
+                "biochar",
+                "Bioaccessibility",
+                "arsenic",
+                "lead",
+                "relative bioavailability",
+                "immobilization",
+                "plumbojarosite",
+                "TSP"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-24",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2023.122881"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187313,45 +187307,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2023.122881"
+            ],
+            "rights": null,
+            "title": "Lead and Arsenic X-ray absorption spectral models fit as linear combination of known standards"
         },
         {
-            "title": "Source Code for Evaluating Impact of Anatomical and Physiological Variability on Human Equivalent Doses Using PBPK Models",
-            "description": "The dataset includes source code that was used to perform analyses described in the manuscript \"Evaluating Impact of Anatomical and Physiological Variability on Human Equivalent Doses Using PBPK Models\" by Schacht et al.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529827",
-            "keyword": [
-                "pbpk",
-                "modeling",
-                "Human Health Risk",
-                "Risk Assessment"
-            ],
             "contactPoint": {
                 "fn": "Dustin Kapraun",
                 "hasEmail": "mailto:kapraun.dustin@epa.gov"
             },
+            "description": "The dataset includes source code that was used to perform analyses described in the manuscript \"Evaluating Impact of Anatomical and Physiological Variability on Human Equivalent Doses Using PBPK Models\" by Schacht et al.",
             "distribution": [
                 {
-                    "title": "Source_Code_PBPK_HED_Distributions_20231108.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529827/Source_Code_PBPK_HED_Distributions_20231108.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Source_Code_PBPK_HED_Distributions_20231108.zip"
                 },
                 {
-                    "title": "Instructions.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529827/Instructions.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Instructions.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529827",
+            "keyword": [
+                "pbpk",
+                "modeling",
+                "Human Health Risk",
+                "Risk Assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-08",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -187360,52 +187356,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Source Code for Evaluating Impact of Anatomical and Physiological Variability on Human Equivalent Doses Using PBPK Models"
         },
         {
-            "title": "Data and code for Rice et al. \u201cWildfires increase concentrations of hazardous air pollutants in downwind communities.\u201d",
-            "description": "This dataset provides the data and code associated with the publication Rice et al. \"Wildfires increase concentrations of hazardous air pollutants in downwind communities\". \n\nThis dataset is associated with the following publication:\nRice, R., K. Boaggio, N. Olson, K. Foley, C. Weaver, J. Sacks, S. McDow, A. Holder, and S. Leduc. Wildfires increase concentrations of hazardous air pollutants in downwind communities.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  14, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529861",
-            "keyword": [
-                "Wildland Fire",
-                "hazardous air pollutants",
-                "smoke",
-                "climate change",
-                "particulate matter"
-            ],
             "contactPoint": {
                 "fn": "Richard Rice",
                 "hasEmail": "mailto:rice.byron@epa.gov"
             },
+            "description": "This dataset provides the data and code associated with the publication Rice et al. \"Wildfires increase concentrations of hazardous air pollutants in downwind communities\". \n\nThis dataset is associated with the following publication:\nRice, R., K. Boaggio, N. Olson, K. Foley, C. Weaver, J. Sacks, S. McDow, A. Holder, and S. Leduc. Wildfires increase concentrations of hazardous air pollutants in downwind communities.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  14, (2023).",
             "distribution": [
                 {
-                    "title": "Data and code description for Rice et al 2023.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529861/Data%20and%20code%20description%20for%20Rice%20et%20al%202023.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data and code description for Rice et al 2023.docx"
                 },
                 {
-                    "title": "code.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529861/code.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "code.zip"
                 },
                 {
-                    "title": "data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529861/data.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "data.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529861",
+            "keyword": [
+                "Wildland Fire",
+                "hazardous air pollutants",
+                "smoke",
+                "climate change",
+                "particulate matter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-29",
-            "references": [
-                "https://doi.org/10.1021/acs.est.3c04153"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187415,19 +187409,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.3c04153"
+            ],
+            "rights": null,
+            "title": "Data and code for Rice et al. \u201cWildfires increase concentrations of hazardous air pollutants in downwind communities.\u201d"
         },
         {
-            "title": "Strong Base Anion Exchange Selectivity of Nine Perfluoroalkyl Chemicals Relevant to Drinking Water Figure Data (V1)",
-            "description": "Data for figures associated with the manuscript entitled Strong Base Anion Exchange Selectivity of Nine Perfluoroalkyl Chemicals Relevant to Drinking Water. \n\nThis dataset is associated with the following publication:\nWahman, D., S. Smith, E. Kleiner, G. Abulikemu, E. Stebel, B. Gray, B. Crone, R. Taylor, E. Womack, C. Gastaldo, T. Sanan, J. Pressman, and L. Haupert. Strong Base Anion Exchange Selectivity of Nine Perfluoroalkyl Chemicals Relevant to Drinking Water.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 3(12): 3967\u22123979, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "David Wahman",
+                "hasEmail": "mailto:wahman.david@epa.gov"
+            },
+            "description": "Data for figures associated with the manuscript entitled Strong Base Anion Exchange Selectivity of Nine Perfluoroalkyl Chemicals Relevant to Drinking Water. \n\nThis dataset is associated with the following publication:\nWahman, D., S. Smith, E. Kleiner, G. Abulikemu, E. Stebel, B. Gray, B. Crone, R. Taylor, E. Womack, C. Gastaldo, T. Sanan, J. Pressman, and L. Haupert. Strong Base Anion Exchange Selectivity of Nine Perfluoroalkyl Chemicals Relevant to Drinking Water.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 3(12): 3967\u22123979, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529095/AEX_PFAS_figure_data_V1.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AEX_PFAS_figure_data_V1.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529095",
             "keyword": [
@@ -187440,21 +187444,10 @@
                 "internal mass transfer",
                 "homogeneous surface diffusion model"
             ],
-            "contactPoint": {
-                "fn": "David Wahman",
-                "hasEmail": "mailto:wahman.david@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "AEX_PFAS_figure_data_V1.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529095/AEX_PFAS_figure_data_V1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-05-22",
-            "references": [
-                "https://doi.org/10.1021/acsestwater.3c00396",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10324599"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187464,39 +187457,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acsestwater.3c00396",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10324599"
+            ],
+            "rights": null,
+            "title": "Strong Base Anion Exchange Selectivity of Nine Perfluoroalkyl Chemicals Relevant to Drinking Water Figure Data (V1)"
         },
         {
-            "title": "Model code and modeling results for the Inorganic Arsenic IRIS Assessment (External Review Draft)",
-            "description": "These files contain the model code as well as modeling results for the draft inorganic arsenic assessment (external review draft)",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529909",
-            "keyword": [
-                "inorganic arsenic",
-                "toxicity values",
-                "IRIS assessments",
-                "Environmental Justice"
-            ],
             "contactPoint": {
                 "fn": "Jeffrey Gift",
                 "hasEmail": "mailto:gift.jeff@epa.gov"
             },
+            "description": "These files contain the model code as well as modeling results for the draft inorganic arsenic assessment (external review draft)",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/DRAFTiAsToxReview/",
-                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/DRAFTiAsToxReview/"
+                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/DRAFTiAsToxReview/",
+                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/DRAFTiAsToxReview/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529909",
+            "keyword": [
+                "inorganic arsenic",
+                "toxicity values",
+                "IRIS assessments",
+                "Environmental Justice"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-01",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -187505,19 +187501,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Model code and modeling results for the Inorganic Arsenic IRIS Assessment (External Review Draft)"
         },
         {
-            "title": "Dataset for Computational Fluid Dynamics Analysis of a Micro-scale Chamber for Measuring Organic Chemical Emission Parameters",
-            "description": "The data presented in this data file is a product of journal publication. The dataset contains air velocity of testing chambers, and convective mass transfer coefficient, diffusion coefficient, and material / air partition coefficient of formaldehyde with different building materials. Portions of this dataset are inaccessible because: CFD data was generated and stored by North Carolina State University because the files are too big and need specific software to open. They can be accessed through the following means: Please contact Jack Edwards <jredward@ncsu.edu> at North Carolina State University. Format: CFD modeling data files. \n\nThis dataset is associated with the following publication:\nEdwards, J., C. Huang, and X. Liu. Computational Fluid Dynamics Analysis of a Micro-scale Chamber for Measuring Organic Chemical Emission Parameters.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA,  0, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Xiaoyu Liu",
+                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
+            },
+            "description": "The data presented in this data file is a product of journal publication. The dataset contains air velocity of testing chambers, and convective mass transfer coefficient, diffusion coefficient, and material / air partition coefficient of formaldehyde with different building materials. Portions of this dataset are inaccessible because: CFD data was generated and stored by North Carolina State University because the files are too big and need specific software to open. They can be accessed through the following means: Please contact Jack Edwards <jredward@ncsu.edu> at North Carolina State University. Format: CFD modeling data files. \n\nThis dataset is associated with the following publication:\nEdwards, J., C. Huang, and X. Liu. Computational Fluid Dynamics Analysis of a Micro-scale Chamber for Measuring Organic Chemical Emission Parameters.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA,  0, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529277/XiaoyuLiu_CFD%20Paper_Data%20Tables%26Dictionary-07192023.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "XiaoyuLiu_CFD Paper_Data Tables&Dictionary-07192023.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529277",
             "keyword": [
@@ -187528,20 +187532,10 @@
                 "material / air partition coefficient",
                 "Formaldehyde"
             ],
-            "contactPoint": {
-                "fn": "Xiaoyu Liu",
-                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "XiaoyuLiu_CFD Paper_Data Tables&Dictionary-07192023.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529277/XiaoyuLiu_CFD%20Paper_Data%20Tables%26Dictionary-07192023.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-19",
-            "references": [
-                "https://www.sciencedirect.com/science/article/pii/S0304389423021167"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187551,19 +187545,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.sciencedirect.com/science/article/pii/S0304389423021167"
+            ],
+            "rights": null,
+            "title": "Dataset for Computational Fluid Dynamics Analysis of a Micro-scale Chamber for Measuring Organic Chemical Emission Parameters"
         },
         {
-            "title": "Dataset for Draft ASTM Standard Test Method for Determination of Fluorotelomer Alcohols in Air by Thermal Desorption - Gas Chromatography Triple Quadrupole Tandem Mass Spectrometry",
-            "description": "The data presented in this data file is a product of a draft ASTM standard. The dataset contains FTOH concentrations measured in thermal desorption tube stability evaluation. It is also published in J Chromatogr. A, 1705 (2023) 464204. \n\nThis dataset is associated with the following publication:\nLiu, X., and Z. Robbins. ASTM Standard Test Method for Determination of Fluorotelomer Alcohols in Air by Thermal Desorption - Gas Chromatography Triple Quadrupole Tandem Mass Spectrometry. U.S. EPA Office of Research and Development, Washington, DC, USA, 2023.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Xiaoyu Liu",
+                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
+            },
+            "description": "The data presented in this data file is a product of a draft ASTM standard. The dataset contains FTOH concentrations measured in thermal desorption tube stability evaluation. It is also published in J Chromatogr. A, 1705 (2023) 464204. \n\nThis dataset is associated with the following publication:\nLiu, X., and Z. Robbins. ASTM Standard Test Method for Determination of Fluorotelomer Alcohols in Air by Thermal Desorption - Gas Chromatography Triple Quadrupole Tandem Mass Spectrometry. U.S. EPA Office of Research and Development, Washington, DC, USA, 2023.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529534/XiaoyuLiu_ASTM%20Methodr_Data%20Tables%26Dictionary-09042023.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "XiaoyuLiu_ASTM Methodr_Data Tables&Dictionary-09042023.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529534",
             "keyword": [
@@ -187574,19 +187578,11 @@
                 "emissions",
                 "fluorotelomer alcohol"
             ],
-            "contactPoint": {
-                "fn": "Xiaoyu Liu",
-                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "XiaoyuLiu_ASTM Methodr_Data Tables&Dictionary-09042023.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529534/XiaoyuLiu_ASTM%20Methodr_Data%20Tables%26Dictionary-09042023.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-09-04",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -187595,19 +187591,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Dataset for Draft ASTM Standard Test Method for Determination of Fluorotelomer Alcohols in Air by Thermal Desorption - Gas Chromatography Triple Quadrupole Tandem Mass Spectrometry"
         },
         {
-            "title": "LP Manuscript CFU Data final",
-            "description": "Reported average CFU/lung based on bacterial enumeration of homogenized lungs.  ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jingrang Lu",
+                "hasEmail": "mailto:lu.jingrang@epa.gov"
+            },
+            "description": "Reported average CFU/lung based on bacterial enumeration of homogenized lungs.  ",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529545/LP%20Manuscript%20CFU%20Data%20final.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LP Manuscript CFU Data final.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529545",
             "keyword": [
@@ -187619,19 +187623,11 @@
                 "excel",
                 "lung"
             ],
-            "contactPoint": {
-                "fn": "Jingrang Lu",
-                "hasEmail": "mailto:lu.jingrang@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "LP Manuscript CFU Data final.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529545/LP%20Manuscript%20CFU%20Data%20final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-08",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -187640,19 +187636,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "LP Manuscript CFU Data final"
         },
         {
-            "title": "Magnesium activation affects the properties and phosphate sorption capacity of poultry litter biochar",
-            "description": "Biochars with a high affinity for phosphorus (P) are promising soil amendments for reducing P in agricultural runoff. Poultry litter (PL) is an abundant biochar feedstock. However, PL-derived biochars are typically high in soluble P and therefore require chemical modification to become effective P sorbents. This study investigated the effect of magnesium (Mg) activation on extractable P (EP) and P sorption capacities of PL-derived biochars. Biochar was produced at 500\u2013900 \u00b0C from PL activated with 0\u20131 M Mg. Three differentially aged PL feedstocks were evaluated (1-, 3\u20135-, and 7\u20139-year-old)\nhas context menu. \n\nThis dataset is associated with the following publication:\nPadilla, J.T., D. Watts, J. Novak, V. Cerven, J. Ippolito, A.A. Szogi, and M. Johnson. Magnesium activation affects the properties and phosphate sorption capacity of poultry litter biochar.   Biochar. Springer Nature, New York, NY, USA, 5: 64, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Mark Johnson",
+                "hasEmail": "mailto:johnson.markg@epa.gov"
+            },
+            "description": "Biochars with a high affinity for phosphorus (P) are promising soil amendments for reducing P in agricultural runoff. Poultry litter (PL) is an abundant biochar feedstock. However, PL-derived biochars are typically high in soluble P and therefore require chemical modification to become effective P sorbents. This study investigated the effect of magnesium (Mg) activation on extractable P (EP) and P sorption capacities of PL-derived biochars. Biochar was produced at 500\u2013900 \u00b0C from PL activated with 0\u20131 M Mg. Three differentially aged PL feedstocks were evaluated (1-, 3\u20135-, and 7\u20139-year-old)\nhas context menu. \n\nThis dataset is associated with the following publication:\nPadilla, J.T., D. Watts, J. Novak, V. Cerven, J. Ippolito, A.A. Szogi, and M. Johnson. Magnesium activation affects the properties and phosphate sorption capacity of poultry litter biochar.   Biochar. Springer Nature, New York, NY, USA, 5: 64, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.5061/dryad.pc866t1w7",
+                    "title": "https://doi.org/10.5061/dryad.pc866t1w7"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529911",
             "keyword": [
@@ -187662,19 +187665,10 @@
                 "eutrophication",
                 "phosphorous"
             ],
-            "contactPoint": {
-                "fn": "Mark Johnson",
-                "hasEmail": "mailto:johnson.markg@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.5061/dryad.pc866t1w7",
-                    "accessURL": "https://doi.org/10.5061/dryad.pc866t1w7"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-10-07",
-            "references": [
-                "https://doi.org/10.1007/s42773-023-00263-5"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187684,73 +187678,73 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s42773-023-00263-5"
+            ],
+            "rights": null,
+            "title": "Magnesium activation affects the properties and phosphate sorption capacity of poultry litter biochar"
         },
         {
-            "title": "Formosa Mine Studies",
-            "description": "Greenhouse screening of plants using a variety of combinations of amendments to provide information for a full-scale on-site revegetation study. \n\nThis dataset is associated with the following publication:\nJohnson, M., D. Olszyk, T. Shiroyama, M. Bollman, M. Nash, V. Manning, K. Trippe, D. Watts, and J. Novak. Designing Amendments to Improve Plant Performance for Mine Tailings Revegetation.   Agrosystems, Geosciences & Environment. John Wiley & Sons, Inc., Hoboken, NJ, USA, 6(3): e20409, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527929",
-            "keyword": [
-                "metals",
-                "Lime",
-                "pH",
-                "Electrical conductivity",
-                "superfund sites",
-                "biosolids"
-            ],
             "contactPoint": {
                 "fn": "Mark Johnson",
                 "hasEmail": "mailto:johnson.markg@epa.gov"
             },
+            "description": "Greenhouse screening of plants using a variety of combinations of amendments to provide information for a full-scale on-site revegetation study. \n\nThis dataset is associated with the following publication:\nJohnson, M., D. Olszyk, T. Shiroyama, M. Bollman, M. Nash, V. Manning, K. Trippe, D. Watts, and J. Novak. Designing Amendments to Improve Plant Performance for Mine Tailings Revegetation.   Agrosystems, Geosciences & Environment. John Wiley & Sons, Inc., Hoboken, NJ, USA, 6(3): e20409, (2023).",
             "distribution": [
                 {
-                    "title": "Formosa Tailings, Biosolids, Biochar Chemistry Data Final 082522.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527929/Formosa%20Tailings%2C%20Biosolids%2C%20Biochar%20Chemistry%20Data%20Final%20082522.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Formosa Tailings, Biosolids, Biochar Chemistry Data Final 082522.xlsx"
                 },
                 {
-                    "title": "Formosa III Greenhouse Study Soil Mixture Moisture Data Sheet For Appendix C.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527929/Formosa%20III%20Greenhouse%20Study%20Soil%20Mixture%20Moisture%20Data%20Sheet%20For%20Appendix%20C.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Formosa III Greenhouse Study Soil Mixture Moisture Data Sheet For Appendix C.xlsx"
                 },
                 {
-                    "title": "Formosa Greenhouse Study 1 For SH DF 083022.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527929/Formosa%20Greenhouse%20Study%201%20For%20SH%20DF%20083022.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Formosa Greenhouse Study 1 For SH DF 083022.xlsx"
                 },
                 {
-                    "title": "Formosa Greenhouse 2 Soil Chemistry Data Revised 042920.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527929/Formosa%20Greenhouse%202%20Soil%20Chemistry%20Data%20Revised%20042920.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Formosa Greenhouse 2 Soil Chemistry Data Revised 042920.xlsx"
                 },
                 {
-                    "title": "Formosa Greenhouse 2 Plant Data Revised 072522.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527929/Formosa%20Greenhouse%202%20Plant%20Data%20Revised%20072522.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Formosa Greenhouse 2 Plant Data Revised 072522.xls"
                 },
                 {
-                    "title": "2017-2018 Greenhouse Climate Data Final 080822.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527929/2017-2018%20Greenhouse%20Climate%20Data%20Final%20080822.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2017-2018 Greenhouse Climate Data Final 080822.xlsx"
                 },
                 {
-                    "title": "Liming study of Formosa Soil_results For Appendix A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527929/Liming%20study%20of%20Formosa%20Soil_results%20For%20Appendix%20A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Liming study of Formosa Soil_results For Appendix A.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527929",
+            "keyword": [
+                "metals",
+                "Lime",
+                "pH",
+                "Electrical conductivity",
+                "superfund sites",
+                "biosolids"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-30",
-            "references": [
-                "https://doi.org/10.1002/agg2.20409"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187760,20 +187754,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/agg2.20409"
+            ],
+            "rights": null,
+            "title": "Formosa Mine Studies"
         },
         {
-            "title": "Data on Mineral-Organic Interactions in PFAS Retention by AFFF Impacted Soil",
-            "description": "Data were collected to develop a comprehensive, generalized approach to predict the retention of per- and polyfluoroalkyl substances (PFAS) from aqueous film forming foam (AFFF) by a soil matrix as a function of PFAS molecular and soil physiochemical properties was developed. An AFFF with 34 major PFAS (12 anions and 22 zwitterions) was added to uncontaminated soil in one-dimensional saturated column experiments and PFAS mass retained was measured. PFAS mass retention was described using an exhaustive statistical approach to generate a poly-parameter quantitative structure-property relationship (ppQSPR). This dataset is not publicly accessible because: The senior author generated the data and has the data.  At the time he was a graduate student at Oregon State University. It can be accessed through the following means: By contacting the senior author at: Thomas.Wanzek@Geosyntec.com. Format: Likely in excel spreadsheets. \n\nThis dataset is associated with the following publication:\nWanzek, T., J. Stults, M. Johnson, J. Field, and M. Kleber. Role of Mineral\u2212Organic Interactions in PFAS Retention by AFFF-Impacted Soil.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(13): 5231-5242, (2023).",
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
+                "fn": "Mark Johnson",
+                "hasEmail": "mailto:johnson.markg@epa.gov"
+            },
+            "description": "Data were collected to develop a comprehensive, generalized approach to predict the retention of per- and polyfluoroalkyl substances (PFAS) from aqueous film forming foam (AFFF) by a soil matrix as a function of PFAS molecular and soil physiochemical properties was developed. An AFFF with 34 major PFAS (12 anions and 22 zwitterions) was added to uncontaminated soil in one-dimensional saturated column experiments and PFAS mass retained was measured. PFAS mass retention was described using an exhaustive statistical approach to generate a poly-parameter quantitative structure-property relationship (ppQSPR). This dataset is not publicly accessible because: The senior author generated the data and has the data.  At the time he was a graduate student at Oregon State University. It can be accessed through the following means: By contacting the senior author at: Thomas.Wanzek@Geosyntec.com. Format: Likely in excel spreadsheets. \n\nThis dataset is associated with the following publication:\nWanzek, T., J. Stults, M. Johnson, J. Field, and M. Kleber. Role of Mineral\u2212Organic Interactions in PFAS Retention by AFFF-Impacted Soil.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 57(13): 5231-5242, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529832",
             "keyword": [
                 "PFAS",
@@ -187784,14 +187782,10 @@
                 "ppQSPR",
                 "AFFF"
             ],
-            "contactPoint": {
-                "fn": "Mark Johnson",
-                "hasEmail": "mailto:johnson.markg@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-02-10",
-            "references": [
-                "https://doi.org/10.1021/acs.est.2c08806"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187801,40 +187795,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.2c08806"
+            ],
+            "rights": null,
+            "title": "Data on Mineral-Organic Interactions in PFAS Retention by AFFF Impacted Soil"
         },
         {
-            "title": "Equilibrium and kinetic sorption of heavy metals by poultry litter biochar: pH-dependency and modeling",
-            "description": "[4:05 PM] Reed, Coral\nBiochars with high phosphate (P) contents are promising amendments to remediate metal-contaminated soils due to their ability to form stable metal-P precipitates. However, their performance is usually assessed at a single pH. This study investigated the sorption of Pb, Cu, Zn, Cd, and Ni by poultry litter (PL) biochar across a pH range using sorption edge, isotherm, and kinetics experiments. Metal sorption was strongly pH-dependent with increased sorption at higher pH. The affinity of the PL biochar for the metals decreased in the order of Pb>>Cu>Zn>Cd>Ni. In all cases, \u226421% of the sorbed metals were exchangeable, indicating that stable metal-biochar associations were formed. Sorption kinetics experiments demonstrated that reaction rates were slower at pH 4.5 than 6.5 for Pb, Cu, and Cd whereas those for Zn and Ni were unaffected by pH. The results suggested that metal-P precipitation was favored for Cu, Cd, and Zn at pH\u22655.5, or Pb at any pH. This indicates that PL-derived biochars can be effective amendments for contaminated soils given that the soils are not too acidic. Experimental data were described using a pH-dependent Freundlich-type isotherm and its kinetic analog. Sorption edges and isotherms were reasonably described for Pb, Zn, Cd, and Ni (r2\u22650.83). Kinetics data were best described using model parameters obtained from sorption edge experiments due to similarities between the input metal concentrations. This modeling approach has superior descriptive capabilities than traditional empirical approaches while maintaining relative simplicity. Moreover, pH-dependent equilibrium and kinetic sorption can be described using a single set of parameters. \n\nThis dataset is associated with the following publication:\nPadilla, J.T., D. Watts, A.A. Szogi, and M. Johnson. Evaluation of a pH- and time-dependent model for the sorption of heavy metal cations by poultry litter-derived biochar.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 347: 140688, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529912",
-            "keyword": [
-                "phosphorous",
-                "biochar",
-                "Metal sorption",
-                "remediation"
-            ],
             "contactPoint": {
                 "fn": "Mark Johnson",
                 "hasEmail": "mailto:johnson.markg@epa.gov"
             },
+            "description": "[4:05 PM] Reed, Coral\nBiochars with high phosphate (P) contents are promising amendments to remediate metal-contaminated soils due to their ability to form stable metal-P precipitates. However, their performance is usually assessed at a single pH. This study investigated the sorption of Pb, Cu, Zn, Cd, and Ni by poultry litter (PL) biochar across a pH range using sorption edge, isotherm, and kinetics experiments. Metal sorption was strongly pH-dependent with increased sorption at higher pH. The affinity of the PL biochar for the metals decreased in the order of Pb>>Cu>Zn>Cd>Ni. In all cases, \u226421% of the sorbed metals were exchangeable, indicating that stable metal-biochar associations were formed. Sorption kinetics experiments demonstrated that reaction rates were slower at pH 4.5 than 6.5 for Pb, Cu, and Cd whereas those for Zn and Ni were unaffected by pH. The results suggested that metal-P precipitation was favored for Cu, Cd, and Zn at pH\u22655.5, or Pb at any pH. This indicates that PL-derived biochars can be effective amendments for contaminated soils given that the soils are not too acidic. Experimental data were described using a pH-dependent Freundlich-type isotherm and its kinetic analog. Sorption edges and isotherms were reasonably described for Pb, Zn, Cd, and Ni (r2\u22650.83). Kinetics data were best described using model parameters obtained from sorption edge experiments due to similarities between the input metal concentrations. This modeling approach has superior descriptive capabilities than traditional empirical approaches while maintaining relative simplicity. Moreover, pH-dependent equilibrium and kinetic sorption can be described using a single set of parameters. \n\nThis dataset is associated with the following publication:\nPadilla, J.T., D. Watts, A.A. Szogi, and M. Johnson. Evaluation of a pH- and time-dependent model for the sorption of heavy metal cations by poultry litter-derived biochar.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 347: 140688, (2024).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.5061/dryad.4f4qrfjk8",
-                    "accessURL": "https://doi.org/10.5061/dryad.4f4qrfjk8"
+                    "accessURL": "https://doi.org/10.5061/dryad.4f4qrfjk8",
+                    "title": "https://doi.org/10.5061/dryad.4f4qrfjk8"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529912",
+            "keyword": [
+                "phosphorous",
+                "biochar",
+                "Metal sorption",
+                "remediation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-11-15",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2023.140688"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187844,41 +187838,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2023.140688"
+            ],
+            "rights": null,
+            "title": "Equilibrium and kinetic sorption of heavy metals by poultry litter biochar: pH-dependency and modeling"
         },
         {
-            "title": "Data set for Particulate Pb emission factors from wildland fires in the United States",
-            "description": "Dataset used to generate the figures and tables in manuscript describing the particulate Pb emission factors from wildland fires in the United States. \n\nThis dataset is associated with the following publication:\nHolder, A., V. Rao, K. Kovalcik, and P. Virtaranta. Particulate Pb emission factors from wildland fires in the United States.   Atmospheric Environment: X. Elsevier B.V., Amsterdam,  NETHERLANDS,  0, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528599",
-            "keyword": [
-                "Fine Particulate Matter",
-                "emissions",
-                "wildland fire smoke",
-                "Toxic metals"
-            ],
             "contactPoint": {
                 "fn": "Amara Holder",
                 "hasEmail": "mailto:holder.amara@epa.gov"
             },
+            "description": "Dataset used to generate the figures and tables in manuscript describing the particulate Pb emission factors from wildland fires in the United States. \n\nThis dataset is associated with the following publication:\nHolder, A., V. Rao, K. Kovalcik, and P. Virtaranta. Particulate Pb emission factors from wildland fires in the United States.   Atmospheric Environment: X. Elsevier B.V., Amsterdam,  NETHERLANDS,  0, (2023).",
             "distribution": [
                 {
-                    "title": "Data set for Particulate Pb EFs Final.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528599/Data%20set%20for%20Particulate%20Pb%20EFs%20Final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data set for Particulate Pb EFs Final.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528599",
+            "keyword": [
+                "Fine Particulate Matter",
+                "emissions",
+                "wildland fire smoke",
+                "Toxic metals"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-12",
-            "references": [
-                "https://www.sciencedirect.com/science/article/pii/S2590162123000291?via%3Dihub"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187888,41 +187882,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.sciencedirect.com/science/article/pii/S2590162123000291?via%3Dihub"
+            ],
+            "rights": null,
+            "title": "Data set for Particulate Pb emission factors from wildland fires in the United States"
         },
         {
-            "title": "Expanding Non-invasive Approaches for Fish-Health Monitoring",
-            "description": "Summary of inter species differences captured using non-invasive sampling of epidermal mucus and mass spectrometry. \n\nThis dataset is associated with the following publication:\nEkman, D., M. Evich, J. Mosley, J. Doering, K. Fay, G. Ankley, and T. Collette. Expanding non-invasive approaches for fish-health monitoring: A survey of the epidermal mucous metabolomes of phylogenetically diverse freshwater fish species.   JOURNAL OF FISH BIOLOGY. Blackwell Publishing, Malden, MA, USA, 103(5): 1178-1189, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1528415",
-            "keyword": [
-                "epidermal mucus",
-                "metabolomics",
-                "non-lethal monitoring",
-                "fish"
-            ],
             "contactPoint": {
                 "fn": "Drew Ekman",
                 "hasEmail": "mailto:ekman.drew@epa.gov"
             },
+            "description": "Summary of inter species differences captured using non-invasive sampling of epidermal mucus and mass spectrometry. \n\nThis dataset is associated with the following publication:\nEkman, D., M. Evich, J. Mosley, J. Doering, K. Fay, G. Ankley, and T. Collette. Expanding non-invasive approaches for fish-health monitoring: A survey of the epidermal mucous metabolomes of phylogenetically diverse freshwater fish species.   JOURNAL OF FISH BIOLOGY. Blackwell Publishing, Malden, MA, USA, 103(5): 1178-1189, (2023).",
             "distribution": [
                 {
-                    "title": "Ekman et al._SciHub Entry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528415/Ekman%20et%20al._SciHub%20Entry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Ekman et al._SciHub Entry.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1528415",
+            "keyword": [
+                "epidermal mucus",
+                "metabolomics",
+                "non-lethal monitoring",
+                "fish"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-31",
-            "references": [
-                "https://doi.org/10.1111/jfb.15512"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187932,19 +187926,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/jfb.15512"
+            ],
+            "rights": null,
+            "title": "Expanding Non-invasive Approaches for Fish-Health Monitoring"
         },
         {
-            "title": "qPCR mastersheet-mod-no-CoV2",
-            "description": "This data set contains information on the concentration of selected gastrointestinal viral and bacterial pathogens extracted from raw wastewater. \n\nThis dataset is associated with the following publication:\nWu, H., M.A. Juel, S. Eytcheson, T.G. Aw, M. Munir, and M. Molina. Temporal and spatial relationships of CrAssphage and enteric viral and bacterial pathogens in wastewater in North Carolina.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 239: 120008, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Marirosa Molina",
+                "hasEmail": "mailto:molina.marirosa@epa.gov"
+            },
+            "description": "This data set contains information on the concentration of selected gastrointestinal viral and bacterial pathogens extracted from raw wastewater. \n\nThis dataset is associated with the following publication:\nWu, H., M.A. Juel, S. Eytcheson, T.G. Aw, M. Munir, and M. Molina. Temporal and spatial relationships of CrAssphage and enteric viral and bacterial pathogens in wastewater in North Carolina.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 239: 120008, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529823/qPCR_mastersheet_mod_no-CoV2.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "qPCR_mastersheet_mod_no-CoV2.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529823",
             "keyword": [
@@ -187964,20 +187968,10 @@
                 "Salmonella",
                 "Stx2"
             ],
-            "contactPoint": {
-                "fn": "Marirosa Molina",
-                "hasEmail": "mailto:molina.marirosa@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "qPCR_mastersheet_mod_no-CoV2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529823/qPCR_mastersheet_mod_no-CoV2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-12-06",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2023.120008"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -187987,19 +187981,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2023.120008"
+            ],
+            "rights": null,
+            "title": "qPCR mastersheet-mod-no-CoV2"
         },
         {
-            "title": "Niagara River Trib Sample Data FINAL.xlsx",
-            "description": "Tables with data on the macroinvertebrate communities at multiple sites. Data list how many individuals of each of several taxa were retrieved from each site/ station. \n\nThis dataset is associated with the following publication:\nYeardley, R., B. Duffy, K. Kimbrough, J. Lazorchak, M. Mills, and E. Johnson. A Comparison of Two Macroinvertebrate Multi-Plate Sampling Methods to Inform Great Lakes Monitoring and Remediation Efforts.   Journal of Environmental Protection. Scientific Research Publishing, Inc., Irvine, CA, USA, 14(12): 933-953, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Roger Yeardley",
+                "hasEmail": "mailto:yeardley.roger@epa.gov"
+            },
+            "description": "Tables with data on the macroinvertebrate communities at multiple sites. Data list how many individuals of each of several taxa were retrieved from each site/ station. \n\nThis dataset is associated with the following publication:\nYeardley, R., B. Duffy, K. Kimbrough, J. Lazorchak, M. Mills, and E. Johnson. A Comparison of Two Macroinvertebrate Multi-Plate Sampling Methods to Inform Great Lakes Monitoring and Remediation Efforts.   Journal of Environmental Protection. Scientific Research Publishing, Inc., Irvine, CA, USA, 14(12): 933-953, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527705/Niagara%20River%20Trib%20Sample%20Data%20FINAL.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Niagara River Trib Sample Data FINAL.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1527705",
             "keyword": [
@@ -188012,20 +188016,10 @@
                 "samplers",
                 "monitoring"
             ],
-            "contactPoint": {
-                "fn": "Roger Yeardley",
-                "hasEmail": "mailto:yeardley.roger@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Niagara River Trib Sample Data FINAL.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527705/Niagara%20River%20Trib%20Sample%20Data%20FINAL.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-13",
-            "references": [
-                "https://doi.org/10.4236/jep.2023.1412052"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188035,44 +188029,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.4236/jep.2023.1412052"
+            ],
+            "rights": null,
+            "title": "Niagara River Trib Sample Data FINAL.xlsx"
         },
         {
-            "title": "Exploring the Effects of Experimental Parameters and Data Modeling Approaches on In Vitro Transcriptomic Point-of-Departure Estimates",
-            "description": "Dataset for 'Exploring the Effects of Experimental Parameters and Data Modeling Approaches on In Vitro Transcriptomic Point-of-Departure Estimates' published in Toxicology December 2023, DOI https://doi.org/10.1016/j.tox.2023.153694. \n\nThis dataset is associated with the following publication:\nHarrill, J., L. Everett, D. Haggard, J. Bundy, C. Willis, I. Shah, K. Friedman, D. Basili, A. Middleton, and R. Judson. Exploring the Effects of Experimental Parameters and Data Modeling Approaches on In Vitro Transcriptomic Point-of-Departure Estimates.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 501: 153694, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529903",
-            "keyword": [
-                "New Approach Methods (NAMs)",
-                "point of departure",
-                "in vitro",
-                "transcriptomics"
-            ],
             "contactPoint": {
                 "fn": "Joshua Harrill",
                 "hasEmail": "mailto:harrill.joshua@epa.gov"
             },
+            "description": "Dataset for 'Exploring the Effects of Experimental Parameters and Data Modeling Approaches on In Vitro Transcriptomic Point-of-Departure Estimates' published in Toxicology December 2023, DOI https://doi.org/10.1016/j.tox.2023.153694. \n\nThis dataset is associated with the following publication:\nHarrill, J., L. Everett, D. Haggard, J. Bundy, C. Willis, I. Shah, K. Friedman, D. Basili, A. Middleton, and R. Judson. Exploring the Effects of Experimental Parameters and Data Modeling Approaches on In Vitro Transcriptomic Point-of-Departure Estimates.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 501: 153694, (2024).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249377",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249377"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249377",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE249377"
                 },
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=64be8d55e4b08a6b5a432a34&page=0",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=64be8d55e4b08a6b5a432a34&page=0"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=64be8d55e4b08a6b5a432a34&page=0",
+                    "title": "https://clowder.edap-cluster.com/datasets/61147fefe4b0856fdc65639b#folderId=64be8d55e4b08a6b5a432a34&page=0"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529903",
+            "keyword": [
+                "New Approach Methods (NAMs)",
+                "point of departure",
+                "in vitro",
+                "transcriptomics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-07-26",
-            "references": [
-                "https://doi.org/10.1016/j.tox.2023.153694"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188082,41 +188076,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tox.2023.153694"
+            ],
+            "rights": null,
+            "title": "Exploring the Effects of Experimental Parameters and Data Modeling Approaches on In Vitro Transcriptomic Point-of-Departure Estimates"
         },
         {
-            "title": "2018 CSMI LAKE ONTARIO LOWER FOOD AQUATIC WEB ASSESSMENT - Total Phosphorous Data",
-            "description": "Lake Ontario open lake and nearshore phosphorus data in support of developing a model and manuscript. \n\nThis dataset is associated with the following publication:\nPauer, J., W. Melendez, T. Hollenhorst, D. Woodruff, and T. Brown. A modeling study to determine the contribution of interbasin versus intrabasin phosphorus loads on the southwestern nearshore of Lake Ontario.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 48(2): 343-358, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1520668",
-            "keyword": [
-                "Lake Ontario",
-                "total phosphorus",
-                "nearshore",
-                "mathematical model"
-            ],
             "contactPoint": {
                 "fn": "James Pauer",
                 "hasEmail": "mailto:pauer.james@epa.gov"
             },
+            "description": "Lake Ontario open lake and nearshore phosphorus data in support of developing a model and manuscript. \n\nThis dataset is associated with the following publication:\nPauer, J., W. Melendez, T. Hollenhorst, D. Woodruff, and T. Brown. A modeling study to determine the contribution of interbasin versus intrabasin phosphorus loads on the southwestern nearshore of Lake Ontario.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 48(2): 343-358, (2022).",
             "distribution": [
                 {
-                    "title": "CSMI_WQ2018GLTEDdata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1520668/CSMI_WQ2018GLTEDdata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CSMI_WQ2018GLTEDdata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1520668",
+            "keyword": [
+                "Lake Ontario",
+                "total phosphorus",
+                "nearshore",
+                "mathematical model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-01-12",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2021.09.014"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188126,42 +188120,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2021.09.014"
+            ],
+            "rights": null,
+            "title": "2018 CSMI LAKE ONTARIO LOWER FOOD AQUATIC WEB ASSESSMENT - Total Phosphorous Data"
         },
         {
-            "title": "Case study in 21st century ecotoxicology:  Using in vitro aromatase inhibition data to predict reproductive outcomes in fish, in vivo.",
-            "description": "Data set includes empirical results from 60 h, 10 d, and 21 d exposures of female fathead minnows to the fungicide imazalil as well as simulations from predictive models anchored to an established adverse outcome pathway (https://aopwiki.org/aops/25). Contents are organized into multiple tabs:\n(1) Simulated effects on plasma 17b-estradiol and vitellogenin used to inform experimental design. (2) Model simulations based on nominal concentrations used in the 60 h, 10 d, and 21 d exposures. (3) Biological effects data from the 60 h experiment. (4) Analytical exposure verification from the 60 h experiment. (5) Biological effects data from the 10 d exposure. (6) Biological effects data from 21 d exposure. (7) Analytical exposure verification from the 10 d and 21 d exposures. (8) Reproduction data from the 10 d and 21 d exposures. (9) Simulated reproduction results based on nominal exposure concentrations used in the 10 d and 21 d exposures. (10) Histopathology evaluations for selected females from the 10 d and 21 d exposures. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., B. Blackwell, C. Blanksma, J. Cavallin, W. Cheng, R. Conolly, K. Conrow, D. Feifarek, L. Heinis, K. Jensen, M. Kahl, R. Milsk, S. Poole, E. Randolph, T. Saari, K. Watanabe, and G. Ankley. Case Study in 21st-Century Ecotoxicology: Using In Vitro Aromatase Inhibition Data to Predict Reproductive Outcomes in Fish In Vivo.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(1): 100-116, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1526378",
-            "keyword": [
-                "New Approach Methods (Alternatives to Animal Testi",
-                "endocrine disruption",
-                "Adverse Outcome Pathways (AOPs)",
-                "reproduction",
-                "aquatic"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Data set includes empirical results from 60 h, 10 d, and 21 d exposures of female fathead minnows to the fungicide imazalil as well as simulations from predictive models anchored to an established adverse outcome pathway (https://aopwiki.org/aops/25). Contents are organized into multiple tabs:\n(1) Simulated effects on plasma 17b-estradiol and vitellogenin used to inform experimental design. (2) Model simulations based on nominal concentrations used in the 60 h, 10 d, and 21 d exposures. (3) Biological effects data from the 60 h experiment. (4) Analytical exposure verification from the 60 h experiment. (5) Biological effects data from the 10 d exposure. (6) Biological effects data from 21 d exposure. (7) Analytical exposure verification from the 10 d and 21 d exposures. (8) Reproduction data from the 10 d and 21 d exposures. (9) Simulated reproduction results based on nominal exposure concentrations used in the 10 d and 21 d exposures. (10) Histopathology evaluations for selected females from the 10 d and 21 d exposures. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., B. Blackwell, C. Blanksma, J. Cavallin, W. Cheng, R. Conolly, K. Conrow, D. Feifarek, L. Heinis, K. Jensen, M. Kahl, R. Milsk, S. Poole, E. Randolph, T. Saari, K. Watanabe, and G. Ankley. Case Study in 21st-Century Ecotoxicology: Using In Vitro Aromatase Inhibition Data to Predict Reproductive Outcomes in Fish In Vivo.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(1): 100-116, (2023).",
             "distribution": [
                 {
-                    "title": "Aromatase inhib QAOP MS Part 2 Science Hub_v4_2022-04-24.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1526378/Aromatase%20inhib%20QAOP%20MS%20Part%202%20Science%20Hub_v4_2022-04-24.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Aromatase inhib QAOP MS Part 2 Science Hub_v4_2022-04-24.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1526378",
+            "keyword": [
+                "New Approach Methods (Alternatives to Animal Testi",
+                "endocrine disruption",
+                "Adverse Outcome Pathways (AOPs)",
+                "reproduction",
+                "aquatic"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-04-23",
-            "references": [
-                "https://doi.org/10.1002/etc.5504"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188171,42 +188165,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5504"
+            ],
+            "rights": null,
+            "title": "Case study in 21st century ecotoxicology:  Using in vitro aromatase inhibition data to predict reproductive outcomes in fish, in vivo."
         },
         {
-            "title": "Evaluation of Complex Mixture Toxicity: An Effects-Driven Analysis in the Milwaukee Estuary (WI, USA) ",
-            "description": "Anthropogenic activities introduce complex mixtures into aquatic environments, necessitating the evaluation of mixture toxicity during ecological risk assessments. There are many new approach methodologies (NAMs) that can be used to complement traditional approaches for conducting mixture assessments. This study aimed to demonstrate how traditional approaches and NAMs can be integrated and employed for mixture evaluation in a target watershed. Assessments were carried out over two years (2017 \u2013 2018) across 8 \u2013 11 study sites in the Milwaukee Estuary (WI, USA). Whole mixtures were evaluated on a site-specific basis by deploying caged fathead minnows (Pimephales promelas) alongside composite samplers for 96-h and characterizing chemical composition, in vitro bioactivity, and in vivo effects in collected water and tissue samples. Chemicals were grouped based on structure/mode of action, bioactivity, and pharmacological actions. Significant chemical/mixtures were identified by assessing contributions to cumulative toxicity units (maximum cumulative ratio analyses) and predictive relationships with measured effects (random Forest regression). Whole mixture assessments identified specific target sites for further evaluation in the Milwaukee Estuary, including four sites impacted by industrial chemical/fuel/polycyclic aromatic hydrocarbon mixtures, four sites impacted by pharmaceutical mixtures, two sites requiring further experimental evaluation, and one low impact site. Constituent-based and predictive analyses identified twelve mixtures and twelve chemicals which significantly contributed to and/or predicted cumulative effects, thus representing priority targets for further ecotoxicological evaluation, monitoring, or regulatory assessment. Overall, this study represents an important complement to single-chemical prioritizations, providing a more comprehensive evaluation of cumulative effects of chemicals detected in a target watershed. Furthermore, it demonstrates diverse tools and techniques that can be employed and adapted for future mixture risk assessments in aquatic environments. \n\nThis dataset is associated with the following publication:\nMaloney, E., D. Villeneuve, K. Jensen, B. Blackwell, M. Kahl, S. Poole, K. Vitense, D. Feifarek, G. Patlewicz, K. Dean, C. Tilton, E. Randolph, J. Cavallin, C. Lalone, D. Blatz, C. Schaupp, and G. Ankley. Evaluation of Complex Mixture Toxicity in the Milwaukee Estuary (WI, USA) Using Whole-Mixture and Component-Based Evaluation Methods.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(6): 1229-1256, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527630",
-            "keyword": [
-                "screening",
-                "chemical mixtures",
-                "restoration",
-                "Great Lakes Restoration Initiative",
-                "Ambient Water"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Anthropogenic activities introduce complex mixtures into aquatic environments, necessitating the evaluation of mixture toxicity during ecological risk assessments. There are many new approach methodologies (NAMs) that can be used to complement traditional approaches for conducting mixture assessments. This study aimed to demonstrate how traditional approaches and NAMs can be integrated and employed for mixture evaluation in a target watershed. Assessments were carried out over two years (2017 \u2013 2018) across 8 \u2013 11 study sites in the Milwaukee Estuary (WI, USA). Whole mixtures were evaluated on a site-specific basis by deploying caged fathead minnows (Pimephales promelas) alongside composite samplers for 96-h and characterizing chemical composition, in vitro bioactivity, and in vivo effects in collected water and tissue samples. Chemicals were grouped based on structure/mode of action, bioactivity, and pharmacological actions. Significant chemical/mixtures were identified by assessing contributions to cumulative toxicity units (maximum cumulative ratio analyses) and predictive relationships with measured effects (random Forest regression). Whole mixture assessments identified specific target sites for further evaluation in the Milwaukee Estuary, including four sites impacted by industrial chemical/fuel/polycyclic aromatic hydrocarbon mixtures, four sites impacted by pharmaceutical mixtures, two sites requiring further experimental evaluation, and one low impact site. Constituent-based and predictive analyses identified twelve mixtures and twelve chemicals which significantly contributed to and/or predicted cumulative effects, thus representing priority targets for further ecotoxicological evaluation, monitoring, or regulatory assessment. Overall, this study represents an important complement to single-chemical prioritizations, providing a more comprehensive evaluation of cumulative effects of chemicals detected in a target watershed. Furthermore, it demonstrates diverse tools and techniques that can be employed and adapted for future mixture risk assessments in aquatic environments. \n\nThis dataset is associated with the following publication:\nMaloney, E., D. Villeneuve, K. Jensen, B. Blackwell, M. Kahl, S. Poole, K. Vitense, D. Feifarek, G. Patlewicz, K. Dean, C. Tilton, E. Randolph, J. Cavallin, C. Lalone, D. Blatz, C. Schaupp, and G. Ankley. Evaluation of Complex Mixture Toxicity in the Milwaukee Estuary (WI, USA) Using Whole-Mixture and Component-Based Evaluation Methods.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(6): 1229-1256, (2023).",
             "distribution": [
                 {
-                    "title": "Milwaukee_Mixtures_Sci_Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527630/Milwaukee_Mixtures_Sci_Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Milwaukee_Mixtures_Sci_Hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527630",
+            "keyword": [
+                "screening",
+                "chemical mixtures",
+                "restoration",
+                "Great Lakes Restoration Initiative",
+                "Ambient Water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-06-27",
-            "references": [
-                "https://doi.org/10.1002/etc.5571"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188216,46 +188210,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5571"
+            ],
+            "rights": null,
+            "title": "Evaluation of Complex Mixture Toxicity: An Effects-Driven Analysis in the Milwaukee Estuary (WI, USA) "
         },
         {
-            "title": "Pilot testing and optimization of a larval fathead minnow high throughput transcriptomics assay",
-            "description": "The present study describes pilot testing of a high throughput compatible transcriptomics assay with larval fathead minnows. One day post hatch fathead minnows were exposed to eleven different concentrations of three metals, three selective serotonin reuptake inhibitors, and four neonicotinoid-like compounds for 24 h and concentration response modeling was applied to whole body gene expression data. Transcriptomics-based points of departure (tPODs) were consistently lower than effect concentrations reported in apical endpoint studies in fish. However, larval fathead minnow-based tPODs were not always lower than concentrations reported to elicit apical toxicity in other aquatic organisms like crustaceans or insects. Random in silico subsampling of data from the pilot assays was used to evaluate various assay design and acceptance considerations such as transcriptome coverage, number of replicate individuals to sequence per treatment, and minimum number of differentially expressed genes to produce a reliable tPOD estimate. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., M. Le, M. Hazemi, A. Biales, D. Bencic, K. Bush, R. Flick, J. Martinson, M. Morshead, K. Santana Rodriguez, K. Vitense, and K. Flynn. Pilot testing and optimization of a larval fathead minnow high throughput transcriptomics assay.   Current Research in Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 4: 100099, (2022).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527818",
-            "keyword": [
-                "screening and prioritization",
-                "aquatic ecosystems",
-                "New Approach Methods (Alternatives to Animal Testi",
-                "computational toxicology",
-                "transcriptomics"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1527818/documents/ORD-049387%20Data%20dictionary%20and%20mapping_v5.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The present study describes pilot testing of a high throughput compatible transcriptomics assay with larval fathead minnows. One day post hatch fathead minnows were exposed to eleven different concentrations of three metals, three selective serotonin reuptake inhibitors, and four neonicotinoid-like compounds for 24 h and concentration response modeling was applied to whole body gene expression data. Transcriptomics-based points of departure (tPODs) were consistently lower than effect concentrations reported in apical endpoint studies in fish. However, larval fathead minnow-based tPODs were not always lower than concentrations reported to elicit apical toxicity in other aquatic organisms like crustaceans or insects. Random in silico subsampling of data from the pilot assays was used to evaluate various assay design and acceptance considerations such as transcriptome coverage, number of replicate individuals to sequence per treatment, and minimum number of differentially expressed genes to produce a reliable tPOD estimate. \n\nThis dataset is associated with the following publication:\nVilleneuve, D., M. Le, M. Hazemi, A. Biales, D. Bencic, K. Bush, R. Flick, J. Martinson, M. Morshead, K. Santana Rodriguez, K. Vitense, and K. Flynn. Pilot testing and optimization of a larval fathead minnow high throughput transcriptomics assay.   Current Research in Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 4: 100099, (2022).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207231",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207231"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207231",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207231"
                 },
                 {
-                    "title": "https://clowder.edap-cluster.com/datasets/62e9145ae4b055edffc06b34",
-                    "accessURL": "https://clowder.edap-cluster.com/datasets/62e9145ae4b055edffc06b34"
+                    "accessURL": "https://clowder.edap-cluster.com/datasets/62e9145ae4b055edffc06b34",
+                    "title": "https://clowder.edap-cluster.com/datasets/62e9145ae4b055edffc06b34"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527818",
+            "keyword": [
+                "screening and prioritization",
+                "aquatic ecosystems",
+                "New Approach Methods (Alternatives to Animal Testi",
+                "computational toxicology",
+                "transcriptomics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-08-09",
-            "references": [
-                "https://doi.org/10.1016/j.crtox.2022.100099",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9816907"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188266,42 +188261,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1527818/documents/ORD-049387%20Data%20dictionary%20and%20mapping_v5.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.crtox.2022.100099",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9816907"
+            ],
+            "rights": null,
+            "title": "Pilot testing and optimization of a larval fathead minnow high throughput transcriptomics assay"
         },
         {
-            "title": "Data supporting amphibian thyroid model parameterization",
-            "description": "This dataset was generated to support parameterization of a larval amphibian thyroid axis computational model. Specifically, plasma iodine levels were determined not only to inform a concentration value for model parameter specification in the model, but also to support the notion that aquatic and terrestrial species should be considered substantially different with regard to circulating iodide levels. Other computational model physical parameters were informed by evaluating Xenopus laevis thyroid gland histological images for morphological features including thyroid follicular cell numbers and areas. \n\nThis dataset is associated with the following publication:\nHaselman, J., J. Nichols, K. Mattingly, M. Hornung, and S. Degitz. A biologically based computational model for the hypothalamic-pituitary-thyroid (HPT) axis in Xenopus laevis larvae.   MATHEMATICAL BIOSCIENCES. Elsevier Science Ltd, New York, NY, USA, 362: 109021, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527937",
-            "keyword": [
-                "computational toxicology",
-                "endocrine",
-                "modeling",
-                "thyroid"
-            ],
             "contactPoint": {
                 "fn": "Jonathan Haselman",
                 "hasEmail": "mailto:haselman.jon@epa.gov"
             },
+            "description": "This dataset was generated to support parameterization of a larval amphibian thyroid axis computational model. Specifically, plasma iodine levels were determined not only to inform a concentration value for model parameter specification in the model, but also to support the notion that aquatic and terrestrial species should be considered substantially different with regard to circulating iodide levels. Other computational model physical parameters were informed by evaluating Xenopus laevis thyroid gland histological images for morphological features including thyroid follicular cell numbers and areas. \n\nThis dataset is associated with the following publication:\nHaselman, J., J. Nichols, K. Mattingly, M. Hornung, and S. Degitz. A biologically based computational model for the hypothalamic-pituitary-thyroid (HPT) axis in Xenopus laevis larvae.   MATHEMATICAL BIOSCIENCES. Elsevier Science Ltd, New York, NY, USA, 362: 109021, (2023).",
             "distribution": [
                 {
-                    "title": "Haselman_et_al_2022_SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527937/Haselman_et_al_2022_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Haselman_et_al_2022_SciHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527937",
+            "keyword": [
+                "computational toxicology",
+                "endocrine",
+                "modeling",
+                "thyroid"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-09-09",
-            "references": [
-                "https://doi.org/10.1016/j.mbs.2023.109021"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188311,19 +188305,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.mbs.2023.109021"
+            ],
+            "rights": null,
+            "title": "Data supporting amphibian thyroid model parameterization"
         },
         {
-            "title": "combined canonical pathways for nano Cu and CuCl2 from IPA. data for table 2, 3,4 ,5",
-            "description": "canonical pathways for each concentration of nano Cu and CuCl2 after upload the DEG lists of each concentration to Ingenuity Pathway Analysis",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Sheau-Fung Thai",
+                "hasEmail": "mailto:thai.sheau-fung@epa.gov"
+            },
+            "description": "canonical pathways for each concentration of nano Cu and CuCl2 after upload the DEG lists of each concentration to Ingenuity Pathway Analysis",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518401/combined%20canonical%20pathway%20for%20nano%20Cu.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "combined canonical pathway for nano Cu.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1518401",
             "keyword": [
@@ -188334,19 +188338,11 @@
                 "signaling pathways",
                 "microRNA target filter analysis"
             ],
-            "contactPoint": {
-                "fn": "Sheau-Fung Thai",
-                "hasEmail": "mailto:thai.sheau-fung@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "combined canonical pathway for nano Cu.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1518401/combined%20canonical%20pathway%20for%20nano%20Cu.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2020-03-05",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -188355,46 +188351,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "combined canonical pathways for nano Cu and CuCl2 from IPA. data for table 2, 3,4 ,5"
         },
         {
-            "title": "Review of per- and polyfluoroalkyl substances (PFAS) bioaccumulation in earthworms",
-            "description": "Supplementary materials for \"Lawrence P. Burkhard, Lauren K. Votava, Review of per- and polyfluoroalkyl substances (PFAS) bioaccumulation in earthworms, Environmental Advances, Volume 11, 2023, 100335, ISSN 2666-7657, https://doi.org/10.1016/j.envadv.2022.100335.\". \n\nThis dataset is associated with the following publication:\nBurkhard, L., and L. Votava. Review of per- and polyfluoroalkyl substances (PFAS) bioaccumulation in earthworms.   Environmental Advances. Elsevier B.V., Amsterdam,  NETHERLANDS, 11: 100335, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529948",
-            "keyword": [
-                "PFAS",
-                "oligochaetes",
-                "bioaccumulation",
-                "earthworms"
-            ],
             "contactPoint": {
                 "fn": "Michael Hornung",
                 "hasEmail": "mailto:hornung.michael@epa.gov"
             },
+            "description": "Supplementary materials for \"Lawrence P. Burkhard, Lauren K. Votava, Review of per- and polyfluoroalkyl substances (PFAS) bioaccumulation in earthworms, Environmental Advances, Volume 11, 2023, 100335, ISSN 2666-7657, https://doi.org/10.1016/j.envadv.2022.100335.\". \n\nThis dataset is associated with the following publication:\nBurkhard, L., and L. Votava. Review of per- and polyfluoroalkyl substances (PFAS) bioaccumulation in earthworms.   Environmental Advances. Elsevier B.V., Amsterdam,  NETHERLANDS, 11: 100335, (2023).",
             "distribution": [
                 {
-                    "title": "Supplementary materials 2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529948/Supplementary%20materials%202.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary materials 2.docx"
                 },
                 {
-                    "title": "Supplementary materials 1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529948/Supplementary%20materials%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplementary materials 1.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529948",
+            "keyword": [
+                "PFAS",
+                "oligochaetes",
+                "bioaccumulation",
+                "earthworms"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-12-14",
-            "references": [
-                "https://doi.org/10.1016/j.envadv.2022.100335"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188404,20 +188398,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envadv.2022.100335"
+            ],
+            "rights": null,
+            "title": "Review of per- and polyfluoroalkyl substances (PFAS) bioaccumulation in earthworms"
         },
         {
-            "title": "The combined effects of temperature and fragment area on the demographic rates of an Afrotropical bird community over 34 years",
-            "description": "Method to access data for \"Montague H.C. Neate-Clegg, Matthew A. Etterson, Morgan W. Tingley, William D. Newmark,\nThe combined effects of temperature and fragment area on the demographic rates of an Afrotropical bird community over 34\u00a0years, Biological Conservation, Volume 282, 2023, 110051, ISSN 0006-3207, https://doi.org/10.1016/j.biocon.2023.110051.\". This dataset is not publicly accessible because: N/A. It can be accessed through the following means: To request data, email monteneateclegg@gmail.com at UCLA. Format: N/A. \n\nThis dataset is associated with the following publication:\nNeate-Clegg, M., M. Etterson, M. Tingley, and W. Newmark. The combined effects of temperature and fragment area on the demographic rates of an Afrotropical bird community over 34 years.   BIOLOGICAL CONSERVATION. Elsevier Science Ltd, New York, NY, USA, 282: 110051, (2023).",
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
+                "fn": "Matthew Etterson",
+                "hasEmail": "mailto:etterson.matthew@epa.gov"
+            },
+            "description": "Method to access data for \"Montague H.C. Neate-Clegg, Matthew A. Etterson, Morgan W. Tingley, William D. Newmark,\nThe combined effects of temperature and fragment area on the demographic rates of an Afrotropical bird community over 34\u00a0years, Biological Conservation, Volume 282, 2023, 110051, ISSN 0006-3207, https://doi.org/10.1016/j.biocon.2023.110051.\". This dataset is not publicly accessible because: N/A. It can be accessed through the following means: To request data, email monteneateclegg@gmail.com at UCLA. Format: N/A. \n\nThis dataset is associated with the following publication:\nNeate-Clegg, M., M. Etterson, M. Tingley, and W. Newmark. The combined effects of temperature and fragment area on the demographic rates of an Afrotropical bird community over 34 years.   BIOLOGICAL CONSERVATION. Elsevier Science Ltd, New York, NY, USA, 282: 110051, (2023).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1529950",
             "keyword": [
                 "Apparent survival",
@@ -188427,14 +188425,10 @@
                 "recruitment",
                 "Tropical mountain"
             ],
-            "contactPoint": {
-                "fn": "Matthew Etterson",
-                "hasEmail": "mailto:etterson.matthew@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-04-01",
-            "references": [
-                "https://doi.org/10.1016/j.biocon.2023.110051"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188444,48 +188438,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.biocon.2023.110051"
+            ],
+            "rights": null,
+            "title": "The combined effects of temperature and fragment area on the demographic rates of an Afrotropical bird community over 34 years"
         },
         {
-            "title": "Models Used to Predict Chemical Bioaccumulation in Fish from in Vitro Biotransformation Rates Require Accurate Estimates of Blood\u2013Water Partitioning and Chemical Volume of Distribution",
-            "description": "Supporting information in \"Saunders, L.J. and Nichols, J.W. (2023), Models Used to Predict Chemical Bioaccumulation in Fish from in Vitro Biotransformation Rates Require Accurate Estimates of Blood\u2013Water Partitioning and Chemical Volume of Distribution. Environ Toxicol Chem, 42: 33-45. https://doi.org/10.1002/etc.5503\". \n\nThis dataset is associated with the following publication:\nSaunders, L., and J. Nichols. Models Used to Predict Chemical Bioaccumulation in Fish from in Vitro Biotransformation Rates Require Accurate Estimates of Blood\u2013Water Partitioning and Chemical Volume of Distribution.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(1): 33-45, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529949",
-            "keyword": [
-                "bioaccumulation",
-                "biotransformation",
-                "in vitro-in vivo extrapolation",
-                "nonspecific binding",
-                "partitioning",
-                "volume of distribution"
-            ],
             "contactPoint": {
                 "fn": "Michael Hornung",
                 "hasEmail": "mailto:hornung.michael@epa.gov"
             },
+            "description": "Supporting information in \"Saunders, L.J. and Nichols, J.W. (2023), Models Used to Predict Chemical Bioaccumulation in Fish from in Vitro Biotransformation Rates Require Accurate Estimates of Blood\u2013Water Partitioning and Chemical Volume of Distribution. Environ Toxicol Chem, 42: 33-45. https://doi.org/10.1002/etc.5503\". \n\nThis dataset is associated with the following publication:\nSaunders, L., and J. Nichols. Models Used to Predict Chemical Bioaccumulation in Fish from in Vitro Biotransformation Rates Require Accurate Estimates of Blood\u2013Water Partitioning and Chemical Volume of Distribution.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 42(1): 33-45, (2023).",
             "distribution": [
                 {
-                    "title": "Supporting Information.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529949/Supporting%20Information.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supporting Information.pdf"
                 },
                 {
-                    "title": "Metadata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529949/Metadata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Metadata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529949",
+            "keyword": [
+                "bioaccumulation",
+                "biotransformation",
+                "in vitro-in vivo extrapolation",
+                "nonspecific binding",
+                "partitioning",
+                "volume of distribution"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2022-10-15",
-            "references": [
-                "https://doi.org/10.1002/etc.5503"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188495,42 +188489,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.5503"
+            ],
+            "rights": null,
+            "title": "Models Used to Predict Chemical Bioaccumulation in Fish from in Vitro Biotransformation Rates Require Accurate Estimates of Blood\u2013Water Partitioning and Chemical Volume of Distribution"
         },
         {
-            "title": "Using Pop-GUIDE to Assess the Applicability of MCnest for Relative Risk of Pesticides to Hummingbirds",
-            "description": "- Text description of regulatory methods for estimating nectar and pollen concentrations from soil applications and seed treatments; \n- Table S1: Parameter set for imidacloprid used for simulations to assess the relative risk of neonicotinoid pesticides to hummingbirds.\n- Table S2: Full sensitivity results for ruby-throated hummingbird exposure to imidacloprid simulation\n- Table S3: Data used for estimating the Mineau scaling factor for imidacloprid. \n\nThis dataset is associated with the following publication:\nEtterson, M., E. Paulukonis, and S. Purucker. Using Pop-GUIDE to Assess the Applicability of MCnest for Relative Risk of Pesticides to Hummingbirds.   Ecologies. MDPI, Basel,  SWITZERLAND, 4(1): 171-194, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529953",
-            "keyword": [
-                "MCnest",
-                "Hummingbird",
-                "Pop GUIDE",
-                "Trochilidae",
-                "Avian Pollinator"
-            ],
             "contactPoint": {
                 "fn": "Matthew Etterson",
                 "hasEmail": "mailto:etterson.matthew@epa.gov"
             },
+            "description": "- Text description of regulatory methods for estimating nectar and pollen concentrations from soil applications and seed treatments; \n- Table S1: Parameter set for imidacloprid used for simulations to assess the relative risk of neonicotinoid pesticides to hummingbirds.\n- Table S2: Full sensitivity results for ruby-throated hummingbird exposure to imidacloprid simulation\n- Table S3: Data used for estimating the Mineau scaling factor for imidacloprid. \n\nThis dataset is associated with the following publication:\nEtterson, M., E. Paulukonis, and S. Purucker. Using Pop-GUIDE to Assess the Applicability of MCnest for Relative Risk of Pesticides to Hummingbirds.   Ecologies. MDPI, Basel,  SWITZERLAND, 4(1): 171-194, (2023).",
             "distribution": [
                 {
-                    "title": "Supplementary Materials.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529953/Supplementary%20Materials.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supplementary Materials.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529953",
+            "keyword": [
+                "MCnest",
+                "Hummingbird",
+                "Pop GUIDE",
+                "Trochilidae",
+                "Avian Pollinator"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-02-22",
-            "references": [
-                "https://doi.org/10.3390/ecologies4010013"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188540,52 +188534,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ecologies4010013"
+            ],
+            "rights": null,
+            "title": "Using Pop-GUIDE to Assess the Applicability of MCnest for Relative Risk of Pesticides to Hummingbirds"
         },
         {
-            "title": "Weight of evidence for cross-species conservation of androgen receptor-based biological activity",
-            "description": "Figures, tables, data for \"Sara M F Vliet, Kristan J Markey, Scott G Lynn, Anna Adetona, Dawn Fallacara, Patricia Ceger, Neepa Choksi, Agnes L Karmaus, AtLee Watson, Andrew Ewans, Amber B Daniel, Jonathan Hamm, Kelsey Vitense, Kaitlyn A Wolf, Amy Thomas, Carlie A LaLone, Weight of evidence for cross-species conservation of androgen receptor-based biological activity, Toxicological Sciences, Volume 193, Issue 2, June 2023, Pages 131\u2013145, https://doi.org/10.1093/toxsci/kfad038\". \n\nThis dataset is associated with the following publication:\nVliet, S., K. Markey, S. Lynn, A. Adetona, D. Fallacara, P. Ceger, N. Choski, A. Karmaus, A. Watson, A. Ewans, A. Daniel, J. Hamm, K. Vitense, K. Wolf, A. Thomas, and C. Lalone. Weight of evidence for cross-species conservation of androgen receptor-based biological activity.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  193(2): 131-145, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529954",
-            "keyword": [
-                "Computational Analysis",
-                "Cross species extrapolation",
-                "endocrine disrupting chemicals",
-                "Systematic Literature Review",
-                "weight of evidence",
-                "Androgen receptor"
-            ],
             "contactPoint": {
                 "fn": "Carlie LaLone",
                 "hasEmail": "mailto:lalone.carlie@epa.gov"
             },
+            "description": "Figures, tables, data for \"Sara M F Vliet, Kristan J Markey, Scott G Lynn, Anna Adetona, Dawn Fallacara, Patricia Ceger, Neepa Choksi, Agnes L Karmaus, AtLee Watson, Andrew Ewans, Amber B Daniel, Jonathan Hamm, Kelsey Vitense, Kaitlyn A Wolf, Amy Thomas, Carlie A LaLone, Weight of evidence for cross-species conservation of androgen receptor-based biological activity, Toxicological Sciences, Volume 193, Issue 2, June 2023, Pages 131\u2013145, https://doi.org/10.1093/toxsci/kfad038\". \n\nThis dataset is associated with the following publication:\nVliet, S., K. Markey, S. Lynn, A. Adetona, D. Fallacara, P. Ceger, N. Choski, A. Karmaus, A. Watson, A. Ewans, A. Daniel, J. Hamm, K. Vitense, K. Wolf, A. Thomas, and C. Lalone. Weight of evidence for cross-species conservation of androgen receptor-based biological activity.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  193(2): 131-145, (2023).",
             "distribution": [
                 {
-                    "title": "Supplemental Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529954/Supplemental%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Supplemental Data.xlsx"
                 },
                 {
-                    "title": "Supplemental Table.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529954/Supplemental%20Table.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplemental Table.docx"
                 },
                 {
-                    "title": "https://doi.org/10.23645/epacomptox.22272439.v1",
-                    "accessURL": "https://doi.org/10.23645/epacomptox.22272439.v1"
+                    "accessURL": "https://doi.org/10.23645/epacomptox.22272439.v1",
+                    "title": "https://doi.org/10.23645/epacomptox.22272439.v1"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529954",
+            "keyword": [
+                "Computational Analysis",
+                "Cross species extrapolation",
+                "endocrine disrupting chemicals",
+                "Systematic Literature Review",
+                "weight of evidence",
+                "Androgen receptor"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-04-18",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfad038"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188595,42 +188589,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfad038"
+            ],
+            "rights": null,
+            "title": "Weight of evidence for cross-species conservation of androgen receptor-based biological activity"
         },
         {
-            "title": "Climate Change, Extreme Events, and Their Potential Effects on Aboveground Storage Tanks (AST) Data Set",
-            "description": "Dataset for journal article \"Climate Change, Extreme Events, and Their Potential Effects on Aboveground Storage Tanks\" published in EM Magazine in September 2023.  The dataset describes calculations for predicted emissions based on AP-42, Chapter 7, and the TankESP software from Trinity Consultants.  The calculations are detailed for aboveground storage tanks at various temperatures, wind speeds, and maintenance conditions for an example tank storing gasoline in Greensboro, NC.  The dataset also describes the composition of the gasoline used in the example calculations.  A glossary of abbreviations is also provided.  The same dataset was used to produce a two-page summary report, Community Vulnerabilities at Aboveground Storage Tanks Due to Climate Change and Extreme Events. \n\nThis dataset is associated with the following publication:\nSmith, R.L., J. Terriquez, E. Thoma, M.A. Gonzalez, D. Johnson, H. Buenning, F. Kremer, J.D. Carpenter, and N.N. Clark. Climate Change, Extreme Events, and Their Potential Effects on Aboveground Storage Tanks.   EM:  AIR AND WASTE MANAGEMENT ASSOCIATION'S MAGAZINE FOR ENVIRONMENTAL MANAGERS. Air & Waste Management Association, Pittsburgh, PA, USA,  1-6, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529958",
-            "keyword": [
-                "emissions",
-                "Extreme Events",
-                "Aboveground Storage Tanks",
-                "climate change",
-                "gasoline"
-            ],
             "contactPoint": {
                 "fn": "Raymond Smith",
                 "hasEmail": "mailto:smith.raymond@epa.gov"
             },
+            "description": "Dataset for journal article \"Climate Change, Extreme Events, and Their Potential Effects on Aboveground Storage Tanks\" published in EM Magazine in September 2023.  The dataset describes calculations for predicted emissions based on AP-42, Chapter 7, and the TankESP software from Trinity Consultants.  The calculations are detailed for aboveground storage tanks at various temperatures, wind speeds, and maintenance conditions for an example tank storing gasoline in Greensboro, NC.  The dataset also describes the composition of the gasoline used in the example calculations.  A glossary of abbreviations is also provided.  The same dataset was used to produce a two-page summary report, Community Vulnerabilities at Aboveground Storage Tanks Due to Climate Change and Extreme Events. \n\nThis dataset is associated with the following publication:\nSmith, R.L., J. Terriquez, E. Thoma, M.A. Gonzalez, D. Johnson, H. Buenning, F. Kremer, J.D. Carpenter, and N.N. Clark. Climate Change, Extreme Events, and Their Potential Effects on Aboveground Storage Tanks.   EM:  AIR AND WASTE MANAGEMENT ASSOCIATION'S MAGAZINE FOR ENVIRONMENTAL MANAGERS. Air & Waste Management Association, Pittsburgh, PA, USA,  1-6, (2023).",
             "distribution": [
                 {
-                    "title": "ClimateChangeExtremeEventsAndTheirPotentialEffectsOnAbovegroundStorageTanks_AST_DataSet.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529958/ClimateChangeExtremeEventsAndTheirPotentialEffectsOnAbovegroundStorageTanks_AST_DataSet.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ClimateChangeExtremeEventsAndTheirPotentialEffectsOnAbovegroundStorageTanks_AST_DataSet.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529958",
+            "keyword": [
+                "emissions",
+                "Extreme Events",
+                "Aboveground Storage Tanks",
+                "climate change",
+                "gasoline"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-20",
-            "references": [
-                "https://www.awma.org/content.asp?admin=Y&contentid=836"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188640,39 +188634,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.awma.org/content.asp?admin=Y&contentid=836"
+            ],
+            "rights": null,
+            "title": "Climate Change, Extreme Events, and Their Potential Effects on Aboveground Storage Tanks (AST) Data Set"
         },
         {
-            "title": "GLRI-Contaminants of emerging concern and biological effects database",
-            "description": "This subproduct is a database of multiagency data, funded as part of the Great Lakes Restoration Initiative (GLRI), to monitor and assess potential exposure and effects of chemicals of emerging concern (CECs) on aquatic and other wildlife in the Great Lakes. This database includes environmental contaminant occurrence data and biological indicator data from Army Corps of Engineers, NOAA, US EPA, US FWS, and USGS.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527944",
-            "keyword": [
-                "Great Lakes",
-                "database",
-                "biological indicators",
-                "environmental contaminants"
-            ],
             "contactPoint": {
                 "fn": "Brett Blackwell",
                 "hasEmail": "mailto:blackwell.brett@epa.gov"
             },
+            "description": "This subproduct is a database of multiagency data, funded as part of the Great Lakes Restoration Initiative (GLRI), to monitor and assess potential exposure and effects of chemicals of emerging concern (CECs) on aquatic and other wildlife in the Great Lakes. This database includes environmental contaminant occurrence data and biological indicator data from Army Corps of Engineers, NOAA, US EPA, US FWS, and USGS.",
             "distribution": [
                 {
-                    "title": "https://clowder.edap-cluster.com/spaces/6180851fe4b07e4aef62b089",
-                    "accessURL": "https://clowder.edap-cluster.com/spaces/6180851fe4b07e4aef62b089"
+                    "accessURL": "https://clowder.edap-cluster.com/spaces/6180851fe4b07e4aef62b089",
+                    "title": "https://clowder.edap-cluster.com/spaces/6180851fe4b07e4aef62b089"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527944",
+            "keyword": [
+                "Great Lakes",
+                "database",
+                "biological indicators",
+                "environmental contaminants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-02-01",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -188681,19 +188677,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "GLRI-Contaminants of emerging concern and biological effects database"
         },
         {
-            "title": "Vapor Intrusion Potential of Select Per- and Polyfluoroalkyl Substances",
-            "description": "Certain per- and polyfluoroalkyl substances (PFAS) have sufficient vapor pressures to be designated as vapor-forming chemicals and; thus, be a concern for vapor intrusion into the indoor air of residences and buildings overlying a contaminated soil or groundwater source. Multiple PFAS species, both neutral (e.g., fluorotelomer alcohols) and ionic (e.g., perfluoroalkyl carboxylic acids), were found in the groundwater, soil, soil gas, and subslab soil gas. With the presence of PFAS in these matrices, a vapor intrusion pathway has been established. This initial research effort provides regulators with scientific evidence that will help them decide whether VI should be evaluated at the hundreds of sites where PFAS are reasonably expected to have been released to the subsurface. \n\nThis dataset is associated with the following publications:\nSchumacher, B., J. Zimmerman, A. Williams, C. Lutes, C. Holton, E. Escobar, H. Hayes, and R. Warrier. Distribution of select per- and polyfluoroalkyl substances at a chemical manufacturing plant.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 464: 133025, (2024).\nSchumacher, B., J. Zimmerman, K. Bronstein, R. Warrier, C. Lutes, E. Escobar, and A. Williams. Subsurface Per- and Polyfluoroalkyl Substances (PFAS) Distribution at Two Contaminated Sites. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Brian Schumacher",
+                "hasEmail": "mailto:schumacher.brian@epa.gov"
+            },
+            "description": "Certain per- and polyfluoroalkyl substances (PFAS) have sufficient vapor pressures to be designated as vapor-forming chemicals and; thus, be a concern for vapor intrusion into the indoor air of residences and buildings overlying a contaminated soil or groundwater source. Multiple PFAS species, both neutral (e.g., fluorotelomer alcohols) and ionic (e.g., perfluoroalkyl carboxylic acids), were found in the groundwater, soil, soil gas, and subslab soil gas. With the presence of PFAS in these matrices, a vapor intrusion pathway has been established. This initial research effort provides regulators with scientific evidence that will help them decide whether VI should be evaluated at the hundreds of sites where PFAS are reasonably expected to have been released to the subsurface. \n\nThis dataset is associated with the following publications:\nSchumacher, B., J. Zimmerman, A. Williams, C. Lutes, C. Holton, E. Escobar, H. Hayes, and R. Warrier. Distribution of select per- and polyfluoroalkyl substances at a chemical manufacturing plant.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 464: 133025, (2024).\nSchumacher, B., J. Zimmerman, K. Bronstein, R. Warrier, C. Lutes, E. Escobar, and A. Williams. Subsurface Per- and Polyfluoroalkyl Substances (PFAS) Distribution at Two Contaminated Sites. U.S. Environmental Protection Agency, Washington, DC, USA, 2023.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528416/PFAS_ORD_Chemours%202-2-2022%20CL%20reformat%20and%20blanks%20filled%20in%20May%202022.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PFAS_ORD_Chemours 2-2-2022 CL reformat and blanks filled in May 2022.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1528416",
             "keyword": [
@@ -188707,21 +188711,10 @@
                 "vapor intrusion",
                 "FTOH"
             ],
-            "contactPoint": {
-                "fn": "Brian Schumacher",
-                "hasEmail": "mailto:schumacher.brian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "PFAS_ORD_Chemours 2-2-2022 CL reformat and blanks filled in May 2022.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1528416/PFAS_ORD_Chemours%202-2-2022%20CL%20reformat%20and%20blanks%20filled%20in%20May%202022.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2022-07-14",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2023.133025",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10734402"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188731,19 +188724,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2023.133025",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10734402"
+            ],
+            "rights": null,
+            "title": "Vapor Intrusion Potential of Select Per- and Polyfluoroalkyl Substances"
         },
         {
-            "title": "Dermal and oral exposure risks to heavy metals from 3D Printing metal-fill thermoplastics-Data Set",
-            "description": "Data that was used to generate the figures in Wade, A.M., D.M. Peloquin, J.M. Matheson, and T.P. Luxton (2023) Dermal and oral exposure risks to heavy metals from 3D printing metal-fill thermoplastics. Science of The Total Environment. 903: p. 166538. \n\nThis dataset is associated with the following publication:\nWade, A.M., D.M. Peloquin, J.M. Matheson, and T.P. Luxton. Dermal and oral exposure risks to heavy metals from 3D printing metal-fill thermoplastics.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 903: 166538, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Todd Luxton",
+                "hasEmail": "mailto:luxton.todd@epa.gov"
+            },
+            "description": "Data that was used to generate the figures in Wade, A.M., D.M. Peloquin, J.M. Matheson, and T.P. Luxton (2023) Dermal and oral exposure risks to heavy metals from 3D printing metal-fill thermoplastics. Science of The Total Environment. 903: p. 166538. \n\nThis dataset is associated with the following publication:\nWade, A.M., D.M. Peloquin, J.M. Matheson, and T.P. Luxton. Dermal and oral exposure risks to heavy metals from 3D printing metal-fill thermoplastics.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 903: 166538, (2023).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529110/05_30_23_Metals_draft.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "05_30_23_Metals_draft.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529110",
             "keyword": [
@@ -188756,22 +188760,10 @@
                 "Hazardous Additives",
                 "Additive Manufacturing"
             ],
-            "contactPoint": {
-                "fn": "Todd Luxton",
-                "hasEmail": "mailto:luxton.todd@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "05_30_23_Metals_draft.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529110/05_30_23_Metals_draft.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-20",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2023.166538",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10653099",
-                "https://pasteur.epa.gov/uploads/10.23719/1529110/documents/Data%20for%20STOTEN2023_3Dprinting.xlsx"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188781,55 +188773,56 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2023.166538",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10653099",
+                "https://pasteur.epa.gov/uploads/10.23719/1529110/documents/Data%20for%20STOTEN2023_3Dprinting.xlsx"
+            ],
+            "rights": null,
+            "title": "Dermal and oral exposure risks to heavy metals from 3D Printing metal-fill thermoplastics-Data Set"
         },
         {
-            "title": "IPCC AR4, AR5, and AR6 20-, 100-, and 500-year GWPs",
-            "description": "The International Panel for Climate Change (IPCC) produces regular Assessment Reports that provide global warming potentials (GWPs) for greenhouse gases (GHG) in the context of multiple time horizons including 20, 100, and 500 years. The GWPs (in kg CO2-equivalent per kg GHG) can be multiplied by kg GHGs emitted for use in estimating CO2-equivalent (CO2e) impacts of GHGs emitted. In the context of life cycle assessment (LCA) , the GWPs can be used as characterization factors in of the life cycle impact assessment. This dataset provides 20- (GWP-20), 100- (GWP-100) and 500-year (GWP-500) GWPs from the 4th (AR4), 6th (AR6) IPCC assessment reports, and 20- (GWP-20) and 100-year (GWP-100) GWPs from the 5th (AR5) report (AR5 provided no 500 yr GWPs). Datasets are provided in simple tables in Excel, in the openLCA JSON-LD format compliant with the U.S. Federal LCA Commons standards, and in Apache parquet format for the most efficient import into applications or scripts using languages like Python and R. The names for GHGs are from the Federal LCA Elementary Flow List (FEDEFL) v1.2, which are names preferred for this GHGs in the USEPA's Substance Registry Service. These datasets were created using the LCIA Formatter v1.1.1 (https://github.com/USEPA/LCIAformatter).  The GWP values are provided in these formats for convenient use; the values have not been altered from the values reported in the Assessment Reports. \nPython code used to produce the data is available in a github gist under the supporting data links along with dataset metadata from the LCIA formatter.\n",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529821",
-            "keyword": [
-                "Global Warming Potential",
-                "Greenhouse gas",
-                "International Panel for Climate Change",
-                "AR4",
-                "AR5",
-                "AR6",
-                "FEDEFL",
-                "openLCA"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "description": "The International Panel for Climate Change (IPCC) produces regular Assessment Reports that provide global warming potentials (GWPs) for greenhouse gases (GHG) in the context of multiple time horizons including 20, 100, and 500 years. The GWPs (in kg CO2-equivalent per kg GHG) can be multiplied by kg GHGs emitted for use in estimating CO2-equivalent (CO2e) impacts of GHGs emitted. In the context of life cycle assessment (LCA) , the GWPs can be used as characterization factors in of the life cycle impact assessment. This dataset provides 20- (GWP-20), 100- (GWP-100) and 500-year (GWP-500) GWPs from the 4th (AR4), 6th (AR6) IPCC assessment reports, and 20- (GWP-20) and 100-year (GWP-100) GWPs from the 5th (AR5) report (AR5 provided no 500 yr GWPs). Datasets are provided in simple tables in Excel, in the openLCA JSON-LD format compliant with the U.S. Federal LCA Commons standards, and in Apache parquet format for the most efficient import into applications or scripts using languages like Python and R. The names for GHGs are from the Federal LCA Elementary Flow List (FEDEFL) v1.2, which are names preferred for this GHGs in the USEPA's Substance Registry Service. These datasets were created using the LCIA Formatter v1.1.1 (https://github.com/USEPA/LCIAformatter).  The GWP values are provided in these formats for convenient use; the values have not been altered from the values reported in the Assessment Reports. \nPython code used to produce the data is available in a github gist under the supporting data links along with dataset metadata from the LCIA formatter.\n",
             "distribution": [
                 {
-                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/lciafmt/ipcc/IPCC_v1.1.1_27ba917.parquet",
-                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/lciafmt/ipcc/IPCC_v1.1.1_27ba917.parquet"
+                    "accessURL": "https://dmap-data-commons-ord.s3.amazonaws.com/lciafmt/ipcc/IPCC_v1.1.1_27ba917.parquet",
+                    "title": "https://dmap-data-commons-ord.s3.amazonaws.com/lciafmt/ipcc/IPCC_v1.1.1_27ba917.parquet"
                 },
                 {
-                    "title": "IPCC_FEDEFL_JSON-LD_no_flows.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529821/IPCC_FEDEFL_JSON-LD_no_flows.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "IPCC_FEDEFL_JSON-LD_no_flows.zip"
                 },
                 {
-                    "title": "IPCC_AR4-AR6_GWPs.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529821/IPCC_AR4-AR6_GWPs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "IPCC_AR4-AR6_GWPs.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529821",
+            "keyword": [
+                "Global Warming Potential",
+                "Greenhouse gas",
+                "International Panel for Climate Change",
+                "AR4",
+                "AR5",
+                "AR6",
+                "FEDEFL",
+                "openLCA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-11-01",
-            "references": [
-                "https://dmap-data-commons-ord.s3.amazonaws.com/lciafmt/ipcc/IPCC_v1.1.1_27ba917_metadata.json",
-                "https://gist.github.com/WesIngwersen/90fcb8be085c8554231913188577876e"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188839,19 +188832,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://dmap-data-commons-ord.s3.amazonaws.com/lciafmt/ipcc/IPCC_v1.1.1_27ba917_metadata.json",
+                "https://gist.github.com/WesIngwersen/90fcb8be085c8554231913188577876e"
+            ],
+            "rights": null,
+            "title": "IPCC AR4, AR5, and AR6 20-, 100-, and 500-year GWPs"
         },
         {
-            "title": "A compartment model to predict in vitro finite dose absorption of chemicals by human skin",
-            "description": "Supplementary data for \"H.A. Fisher, M.V. Evans, A.L. Bunge, E.A. Cohen Hubal, D.A. Vallero, A compartment model to predict in vitro finite dose absorption of chemicals by human skin, Chemosphere, Volume 349, 2024, 140689, ISSN 0045-6535, https://doi.org/10.1016/j.chemosphere.2023.140689.\". \n\nThis dataset is associated with the following publication:\nFisher, H., M. Evans, A. Bunge, E. Cohen-Hubal, and D. Vallero. A compartment model to predict in vitro finite dose absorption of chemicals by human skin.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 349: 140689, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Marina Evans",
+                "hasEmail": "mailto:evans.marina@epa.gov"
+            },
+            "description": "Supplementary data for \"H.A. Fisher, M.V. Evans, A.L. Bunge, E.A. Cohen Hubal, D.A. Vallero, A compartment model to predict in vitro finite dose absorption of chemicals by human skin, Chemosphere, Volume 349, 2024, 140689, ISSN 0045-6535, https://doi.org/10.1016/j.chemosphere.2023.140689.\". \n\nThis dataset is associated with the following publication:\nFisher, H., M. Evans, A. Bunge, E. Cohen-Hubal, and D. Vallero. A compartment model to predict in vitro finite dose absorption of chemicals by human skin.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 349: 140689, (2024).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529955/SI_submission.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "SI_submission.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529955",
             "keyword": [
@@ -188862,20 +188866,10 @@
                 "human dermal permeability",
                 "in vitro model"
             ],
-            "contactPoint": {
-                "fn": "Marina Evans",
-                "hasEmail": "mailto:evans.marina@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SI_submission.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529955/SI_submission.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-11-09",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2023.140689"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188885,19 +188879,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2023.140689"
+            ],
+            "rights": null,
+            "title": "A compartment model to predict in vitro finite dose absorption of chemicals by human skin"
         },
         {
-            "title": "Global change scenarios in coastal deltas",
-            "description": "For this study we explored future scenarios for 49 deltas, including\nthe most populated and largest coastal deltas in the world, as well as a\nrange of smaller and less populated deltas representing different climates,\nbiomes, and socio-economic development states (Fig. 2). The set\nof deltas corresponds to only a fraction of the total number of deltas\nglobally (cf. 235 large deltas of Reader et al., 2022; and the thousands of\ndeltas of Nienhuis et al., 2020), but were chosen to represent a wide\nrange of geographies and align with previous work on delta risk (Dunn\net al., 2019; Tessler et al., 2015) and the availability of limited data on\nland subsidence (Nicholls et al., 2021). For our analysis we chose a set of\n13 variables that represent various socio-economic and geophysical\npressures on deltas and are indicators of the different components of\ndelta risk as defined by Tessler et al. (2015) (Table 1). \n\nThis dataset is associated with the following publication:\nScown, M., F. Dunn, S. Dekker, D. van Vuuren, S. Karabil, E. Sutanudjaja, M. Santos, P. Minderhoud, A. Garmestani, and H. Middelkoop. Global change scenarios in coastal deltas and their sustainable development implications.   Global Environmental Change. Elsevier B.V., Amsterdam,  NETHERLANDS,  14, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Ahjond Garmestani",
+                "hasEmail": "mailto:garmestani.ahjond@epa.gov"
+            },
+            "description": "For this study we explored future scenarios for 49 deltas, including\nthe most populated and largest coastal deltas in the world, as well as a\nrange of smaller and less populated deltas representing different climates,\nbiomes, and socio-economic development states (Fig. 2). The set\nof deltas corresponds to only a fraction of the total number of deltas\nglobally (cf. 235 large deltas of Reader et al., 2022; and the thousands of\ndeltas of Nienhuis et al., 2020), but were chosen to represent a wide\nrange of geographies and align with previous work on delta risk (Dunn\net al., 2019; Tessler et al., 2015) and the availability of limited data on\nland subsidence (Nicholls et al., 2021). For our analysis we chose a set of\n13 variables that represent various socio-economic and geophysical\npressures on deltas and are indicators of the different components of\ndelta risk as defined by Tessler et al. (2015) (Table 1). \n\nThis dataset is associated with the following publication:\nScown, M., F. Dunn, S. Dekker, D. van Vuuren, S. Karabil, E. Sutanudjaja, M. Santos, P. Minderhoud, A. Garmestani, and H. Middelkoop. Global change scenarios in coastal deltas and their sustainable development implications.   Global Environmental Change. Elsevier B.V., Amsterdam,  NETHERLANDS,  14, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1016/j.gloenvcha.2023.102736",
+                    "title": "https://doi.org/10.1016/j.gloenvcha.2023.102736"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529592",
             "keyword": [
@@ -188907,20 +188910,10 @@
                 "Deltas",
                 "floodplains"
             ],
-            "contactPoint": {
-                "fn": "Ahjond Garmestani",
-                "hasEmail": "mailto:garmestani.ahjond@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1016/j.gloenvcha.2023.102736",
-                    "accessURL": "https://doi.org/10.1016/j.gloenvcha.2023.102736"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-15",
-            "references": [
-                "https://doi.org/10.1016/j.gloenvcha.2023.102736",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10483986"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188930,53 +188923,54 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.gloenvcha.2023.102736",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10483986"
+            ],
+            "rights": null,
+            "title": "Global change scenarios in coastal deltas"
         },
         {
-            "title": "A multi-tiered hierarchical Bayesian approach to derive toxic equivalency factors for dioxin-like compounds",
-            "description": "Supplementary data for \"Ring C, Blanchette A, Klaren WD, Fitch S, Haws L, Wheeler MW, DeVito M, Walker N, Wikoff D. A multi-tiered hierarchical Bayesian approach to derive toxic equivalency factors for dioxin-like compounds. Regul Toxicol Pharmacol. 2023 Sep;143:105464. doi: 10.1016/j.yrtph.2023.105464. Epub 2023 Jul 27. PMID: 37516304.\". Portions of this dataset are inaccessible because: Available on request from Daniele Wikoff. They can be accessed through the following means: Available on request from dwikoff@toxstrategies.com. Format: N/A. \n\nThis dataset is associated with the following publication:\nRing, C., A. Blanchette, W. Klaren, S. Fitch, L. Haws, M. Wheeler, M. Devito, N. Walker, and D. Wikoff. A multi-tiered hierarchical Bayesian approach to derive toxic equivalency factors for dioxin-like compounds.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 143: 105464, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529962",
-            "keyword": [
-                "relative estimated potency",
-                "toxic equivalency factors",
-                "dioxin-like compounds",
-                "Environmental Justice",
-                "Children's Environmental Health",
-                "bayesian approach"
-            ],
             "contactPoint": {
                 "fn": "Michael Devito",
                 "hasEmail": "mailto:devito.michael@epa.gov"
             },
+            "description": "Supplementary data for \"Ring C, Blanchette A, Klaren WD, Fitch S, Haws L, Wheeler MW, DeVito M, Walker N, Wikoff D. A multi-tiered hierarchical Bayesian approach to derive toxic equivalency factors for dioxin-like compounds. Regul Toxicol Pharmacol. 2023 Sep;143:105464. doi: 10.1016/j.yrtph.2023.105464. Epub 2023 Jul 27. PMID: 37516304.\". Portions of this dataset are inaccessible because: Available on request from Daniele Wikoff. They can be accessed through the following means: Available on request from dwikoff@toxstrategies.com. Format: N/A. \n\nThis dataset is associated with the following publication:\nRing, C., A. Blanchette, W. Klaren, S. Fitch, L. Haws, M. Wheeler, M. Devito, N. Walker, and D. Wikoff. A multi-tiered hierarchical Bayesian approach to derive toxic equivalency factors for dioxin-like compounds.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 143: 105464, (2023).",
             "distribution": [
                 {
-                    "title": "1-s2.0-S0273230023001320-mmc1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529962/1-s2.0-S0273230023001320-mmc1.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "1-s2.0-S0273230023001320-mmc1.docx"
                 },
                 {
-                    "title": "1-s2.0-S0273230023001320-mmc3.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529962/1-s2.0-S0273230023001320-mmc3.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "1-s2.0-S0273230023001320-mmc3.docx"
                 },
                 {
-                    "title": "1-s2.0-S0273230023001320-mmc2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529962/1-s2.0-S0273230023001320-mmc2.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "1-s2.0-S0273230023001320-mmc2.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529962",
+            "keyword": [
+                "relative estimated potency",
+                "toxic equivalency factors",
+                "dioxin-like compounds",
+                "Environmental Justice",
+                "Children's Environmental Health",
+                "bayesian approach"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-25",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2023.105464"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -188986,19 +188980,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2023.105464"
+            ],
+            "rights": null,
+            "title": "A multi-tiered hierarchical Bayesian approach to derive toxic equivalency factors for dioxin-like compounds"
         },
         {
-            "title": "2012-2020 Greenhouse Gas National- and State-Level Emission Totals by Industry",
-            "description": "These data represent annual greenhouse gas (GHG) emission totals by industry sectors and households for the total U.S. and by state, for years 2012 to 2020. Industry sectors are defined by North American Industry Classification System (NAICS) 2012 codes, with additional codes added for households and government.\nEmissions of 16 different GHGs, which are the same GHGs as reported in the U.S. GHG Inventory, are included. \nValues are given in total kilograms emitted for the given year, sector and location.\n\nData are provided in two alternative formats, as Excel files and as Apache parquet files.\nThe Excel files include:\n1) GHGs by 114 aggregate level sectors by state and year,\n2) GHGs by 114 aggregate level sectors by year for the U.S., and\n3) GHGs by 540 detailed sectors by year for the U.S. \nThe Excel files use a simplified version (not all fields included) of the Flow-by-Sector format (see link to format specification below). \nThe parquet files align with the Excel files except are also separated by year, and provide the complete flow by sector format, where files with \"state_m1\" correspond to the aggregate level state datasets, files with \"national_m1\" correspond to the aggregate level national dataset, and files with \"national_m2\" correspond to the aggregate level state datasets, \nStandard metadata files in JSON format, and log and validation files in text format (with .log extension) are provided for each parquet file. \n\nThe data are a product of updated sector attribution models that improve upon the National Greenhouse Gas Industry Attribution Model.  \n The models used to generate the national aggregate and the state datasets are sector attribution models coded in the FLOWSA v2.0.0 tool (https://github.com/USEPA/flowsa/tree/v2.0.0). The national detailed datasets are developed with FLOWSA v2.0.1 (https://github.com/USEPA/flowsa/tree/v2.0.1).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Wesley Ingwersen",
+                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
+            },
+            "description": "These data represent annual greenhouse gas (GHG) emission totals by industry sectors and households for the total U.S. and by state, for years 2012 to 2020. Industry sectors are defined by North American Industry Classification System (NAICS) 2012 codes, with additional codes added for households and government.\nEmissions of 16 different GHGs, which are the same GHGs as reported in the U.S. GHG Inventory, are included. \nValues are given in total kilograms emitted for the given year, sector and location.\n\nData are provided in two alternative formats, as Excel files and as Apache parquet files.\nThe Excel files include:\n1) GHGs by 114 aggregate level sectors by state and year,\n2) GHGs by 114 aggregate level sectors by year for the U.S., and\n3) GHGs by 540 detailed sectors by year for the U.S. \nThe Excel files use a simplified version (not all fields included) of the Flow-by-Sector format (see link to format specification below). \nThe parquet files align with the Excel files except are also separated by year, and provide the complete flow by sector format, where files with \"state_m1\" correspond to the aggregate level state datasets, files with \"national_m1\" correspond to the aggregate level national dataset, and files with \"national_m2\" correspond to the aggregate level state datasets, \nStandard metadata files in JSON format, and log and validation files in text format (with .log extension) are provided for each parquet file. \n\nThe data are a product of updated sector attribution models that improve upon the National Greenhouse Gas Industry Attribution Model.  \n The models used to generate the national aggregate and the state datasets are sector attribution models coded in the FLOWSA v2.0.0 tool (https://github.com/USEPA/flowsa/tree/v2.0.0). The national detailed datasets are developed with FLOWSA v2.0.1 (https://github.com/USEPA/flowsa/tree/v2.0.1).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529805/GHGs_by_Sector_and_State_2012-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GHGs_by_Sector_and_State_2012-2020.xlsx"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529805/GHGs_by_Detailed_Sector_US_2012-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GHGs_by_Detailed_Sector_US_2012-2020.xlsx"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529805/GHGs_by_Aggregate_Sector_US_2012-2020.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GHGs_by_Aggregate_Sector_US_2012-2020.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529805",
             "keyword": [
@@ -189016,28 +189030,20 @@
                 "greenhouse gas emissions",
                 "national totals by industry"
             ],
-            "contactPoint": {
-                "fn": "Wesley Ingwersen",
-                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "GHGs_by_Sector_and_State_2012-2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529805/GHGs_by_Sector_and_State_2012-2020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "GHGs_by_Detailed_Sector_US_2012-2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529805/GHGs_by_Detailed_Sector_US_2012-2020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "GHGs_by_Aggregate_Sector_US_2012-2020.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529805/GHGs_by_Aggregate_Sector_US_2012-2020.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-11",
+            "programCode": [
+                "020:000"
+            ],
+            "publisher": {
+                "name": "U.S. EPA Office of Research and Development (ORD)",
+                "subOrganizationOf": {
+                    "name": "U.S. Environmental Protection Agency",
+                    "subOrganizationOf": {
+                        "name": "U.S. Government"
+                    }
+                }
+            },
             "references": [
                 "https://github.com/USEPA/flowsa/blob/v2.0.1/format%20specs/FlowBySector.md",
                 "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/GHG_national_2012_m1_v2.0.0_a8c5929.log",
@@ -189149,55 +189155,42 @@
                 "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/GHG_state_2020_m1_v2.0.0_a8c5929_metadata.json",
                 "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/GHG_state_2020_m1_v2.0.0_a8c5929_validation.log"
             ],
-            "publisher": {
-                "name": "U.S. EPA Office of Research and Development (ORD)",
-                "subOrganizationOf": {
-                    "name": "U.S. Environmental Protection Agency",
-                    "subOrganizationOf": {
-                        "name": "U.S. Government"
-                    }
-                }
-            }
+            "rights": null,
+            "title": "2012-2020 Greenhouse Gas National- and State-Level Emission Totals by Industry"
         },
         {
-            "title": "3D Printers Emissions of Environmentally Persistent Free Radicals (EPFRs)",
-            "description": "Polymers used in 3D printing are known to emit hazardous materials when heated. While the emissions from pristine polymers and some filaments have been studied, many filaments contain additives that may influence their hazardous emissions. This research used a variety of commercially-available 3D printer filaments to assess the possibly formation of environmentally persistent free radicals (EPFRs), a class of surface-bound free radicals that have much longer lifetimes compared to their gas-phase counterparts. Electron paramagnetic resonance (EPR) spectroscopy was used to successfully identify EPFRs in particulate matter collected during regular 3D printer use. These findings should influence future studies on 3D printer emissions to include consideration of EPFR formation. These methodologies may be used by EPA's Chemical Safety and Pollution Prevention (OCSPP), Consumer Protection and Safety Commission (CPSC), and National Institute of Occupational of Safety and Health (NIOSH). \n\nThis dataset is associated with the following publication:\nHasan, F., P.M. Potter, S.R. Al-Abed, J. Matheson, and S.M. Lomnicki. Investigating environmentally persistent free radicals (EPFRs) emissions of 3D printing process.   Chemical Engineering Journal. Elsevier BV, AMSTERDAM,  NETHERLANDS, 480: 148158, (2024).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529613",
-            "keyword": [
-                "indoor air quality",
-                "3D Prining",
-                "Emerging Contaminant",
-                "electron paramagnetic resonance spectroscopy"
-            ],
             "contactPoint": {
                 "fn": "Souhail Al-Abed",
                 "hasEmail": "mailto:al-abed.souhail@epa.gov"
             },
+            "description": "Polymers used in 3D printing are known to emit hazardous materials when heated. While the emissions from pristine polymers and some filaments have been studied, many filaments contain additives that may influence their hazardous emissions. This research used a variety of commercially-available 3D printer filaments to assess the possibly formation of environmentally persistent free radicals (EPFRs), a class of surface-bound free radicals that have much longer lifetimes compared to their gas-phase counterparts. Electron paramagnetic resonance (EPR) spectroscopy was used to successfully identify EPFRs in particulate matter collected during regular 3D printer use. These findings should influence future studies on 3D printer emissions to include consideration of EPFR formation. These methodologies may be used by EPA's Chemical Safety and Pollution Prevention (OCSPP), Consumer Protection and Safety Commission (CPSC), and National Institute of Occupational of Safety and Health (NIOSH). \n\nThis dataset is associated with the following publication:\nHasan, F., P.M. Potter, S.R. Al-Abed, J. Matheson, and S.M. Lomnicki. Investigating environmentally persistent free radicals (EPFRs) emissions of 3D printing process.   Chemical Engineering Journal. Elsevier BV, AMSTERDAM,  NETHERLANDS, 480: 148158, (2024).",
             "distribution": [
                 {
-                    "title": "ABS-Blue_Raw Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529613/ABS-Blue_Raw%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ABS-Blue_Raw Data.xlsx"
                 },
                 {
-                    "title": "ABS-Black_Raw Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529613/ABS-Black_Raw%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ABS-Black_Raw Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529613",
+            "keyword": [
+                "indoor air quality",
+                "3D Prining",
+                "Emerging Contaminant",
+                "electron paramagnetic resonance spectroscopy"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-08-29",
-            "references": [
-                "https://doi.org/10.1016/j.cej.2023.148158",
-                "https://pasteur.epa.gov/uploads/10.23719/1529613/documents/Supporting%20Information_EPFR%20Manuscript.docx"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189207,19 +189200,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.cej.2023.148158",
+                "https://pasteur.epa.gov/uploads/10.23719/1529613/documents/Supporting%20Information_EPFR%20Manuscript.docx"
+            ],
+            "rights": null,
+            "title": "3D Printers Emissions of Environmentally Persistent Free Radicals (EPFRs)"
         },
         {
-            "title": "Hamilton et al. 2023 A voucher flora of diatoms from fens in the Tanana River floodplain, Alaska",
-            "description": "Supporting information for Hamilton et al. 2023, File S1: taxonomic authority references; Table S1: species information. \n\nThis dataset is associated with the following publication:\nHamilton, V., S. Lee, A. Rober, P. Furey, K. Manoylov, and K. Wyatt. A voucher flora of diatoms from fens in the Tanana River floodplain, Alaska..   WATER. MDPI, Basel,  SWITZERLAND, 15: 2803, (2023).",
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
+            "description": "Supporting information for Hamilton et al. 2023, File S1: taxonomic authority references; Table S1: species information. \n\nThis dataset is associated with the following publication:\nHamilton, V., S. Lee, A. Rober, P. Furey, K. Manoylov, and K. Wyatt. A voucher flora of diatoms from fens in the Tanana River floodplain, Alaska..   WATER. MDPI, Basel,  SWITZERLAND, 15: 2803, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.mdpi.com/article/10.3390/w15152803/s1",
+                    "title": "https://www.mdpi.com/article/10.3390/w15152803/s1"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529965",
             "keyword": [
@@ -189229,20 +189232,10 @@
                 "wetlands",
                 "climate change"
             ],
-            "contactPoint": {
-                "fn": "Sylvia Lee",
-                "hasEmail": "mailto:lee.sylvia@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.mdpi.com/article/10.3390/w15152803/s1",
-                    "accessURL": "https://www.mdpi.com/article/10.3390/w15152803/s1"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-08-02",
-            "references": [
-                "https://doi.org/10.3390/w15152803",
-                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10750759"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189252,115 +189245,118 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/w15152803",
+                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10750759"
+            ],
+            "rights": null,
+            "title": "Hamilton et al. 2023 A voucher flora of diatoms from fens in the Tanana River floodplain, Alaska"
         },
         {
-            "title": "Scenario Planning Management Actions to Restore Cold Water Stream Habitat Data",
-            "description": "This data repository holds modeling inputs and output from a project that compared various restoration and management actions influence on stream temperature. Three study systems were used in this effort that include the Middle Fork John Day River, South Fork Nooksack River, and Wind River basins of Oregon and Washington states in the USA. The spatial stream network (SSN) models used in this project were previously developed and published in the Journal of American Water Resources Research (doi: 10.1111/1752-1688.13158). These models were used to make predictions in each study basin that reflected restoration and management goals within each system. The predictions for temperature changes were then compared individually as well as in a combined management activity scenario. This repository holds the input data for the SSN models as well as the prediction output from each modeling scenario for each basin. ",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529829",
-            "keyword": [
-                "stream temperature",
-                "cold-water habitat",
-                "spatial stream network model",
-                "fish use thermal criteria",
-                "scenario planning",
-                "model averaging",
-                "Environmental Restoration",
-                "freshwater management",
-                "Pacific Northwest"
-            ],
             "contactPoint": {
                 "fn": "Naomi Detenbeck",
                 "hasEmail": "mailto:detenbeck.naomi@epa.gov"
             },
+            "description": "This data repository holds modeling inputs and output from a project that compared various restoration and management actions influence on stream temperature. Three study systems were used in this effort that include the Middle Fork John Day River, South Fork Nooksack River, and Wind River basins of Oregon and Washington states in the USA. The spatial stream network (SSN) models used in this project were previously developed and published in the Journal of American Water Resources Research (doi: 10.1111/1752-1688.13158). These models were used to make predictions in each study basin that reflected restoration and management goals within each system. The predictions for temperature changes were then compared individually as well as in a combined management activity scenario. This repository holds the input data for the SSN models as well as the prediction output from each modeling scenario for each basin. ",
             "distribution": [
                 {
-                    "title": "00ScienceHubREADME.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/00ScienceHubREADME.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "00ScienceHubREADME.docx"
                 },
                 {
-                    "title": "WR_900Sep_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/WR_900Sep_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "WR_900Sep_scenarios.zip"
                 },
                 {
-                    "title": "WR_800Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/WR_800Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "WR_800Aug_scenarios.zip"
                 },
                 {
-                    "title": "WR_500May_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/WR_500May_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "WR_500May_scenarios.zip"
                 },
                 {
-                    "title": "SFNR_900Sep_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/SFNR_900Sep_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "SFNR_900Sep_scenarios.zip"
                 },
                 {
-                    "title": "SFNR_800Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/SFNR_800Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "SFNR_800Aug_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_900Sep_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_900Sep_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_900Sep_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_806Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_806Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_806Aug_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_805Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_805Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_805Aug_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_804Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_804Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_804Aug_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_803Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_803Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_803Aug_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_802Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_802Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_802Aug_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_801Aug_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_801Aug_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_801Aug_scenarios.zip"
                 },
                 {
-                    "title": "MFJD_500May_scenarios.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/MFJD_500May_scenarios.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "MFJD_500May_scenarios.zip"
                 },
                 {
-                    "title": "00StudyBasin_README_and_metadata_directories.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529829/00StudyBasin_README_and_metadata_directories.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "00StudyBasin_README_and_metadata_directories.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529829",
+            "keyword": [
+                "stream temperature",
+                "cold-water habitat",
+                "spatial stream network model",
+                "fish use thermal criteria",
+                "scenario planning",
+                "model averaging",
+                "Environmental Restoration",
+                "freshwater management",
+                "Pacific Northwest"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2021-05-21",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -189369,40 +189365,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Scenario Planning Management Actions to Restore Cold Water Stream Habitat Data"
         },
         {
-            "title": "Data for Upwind Barriers Mitigating the AQ Impact of Highway Em",
-            "description": "Wind tunnel study of dispersion from roadway with a solid barrier upwind of the road. \n\nThis dataset is associated with the following publication:\nFrancisco, D., D. Heist, A. Venkatram, L. Brouwer, and S. Perry. Incorporating the Impact of Roadside Barrier Effects on Dispersion into AERMOD.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 74(1): Pages 39-51, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1527771",
-            "keyword": [
-                "near-road",
-                "wind tunnel",
-                "Dispersion"
-            ],
             "contactPoint": {
                 "fn": "David Heist",
                 "hasEmail": "mailto:heist.david@epa.gov"
             },
+            "description": "Wind tunnel study of dispersion from roadway with a solid barrier upwind of the road. \n\nThis dataset is associated with the following publication:\nFrancisco, D., D. Heist, A. Venkatram, L. Brouwer, and S. Perry. Incorporating the Impact of Roadside Barrier Effects on Dispersion into AERMOD.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 74(1): Pages 39-51, (2023).",
             "distribution": [
                 {
-                    "title": "Dataset D-prrq.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1527771/Dataset%20D-prrq.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "Dataset D-prrq.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1527771",
+            "keyword": [
+                "near-road",
+                "wind tunnel",
+                "Dispersion"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-10-19",
-            "references": [
-                "https://doi.org/10.1080/10962247.2023.2277754"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189412,39 +189406,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10962247.2023.2277754"
+            ],
+            "rights": null,
+            "title": "Data for Upwind Barriers Mitigating the AQ Impact of Highway Em"
         },
         {
-            "title": "Composition of active bacterial communities and presence of opportunistic pathogens in Finland (S02)",
-            "description": "The bacteria sequence data generated in this study is available in the Short Read Archive (SRA) of NCBI (https://www.ncbi.nlm.nih.gov/) under BioProject PRJNA509718.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529855",
-            "keyword": [
-                "Drinking water distribution system",
-                "pathogens",
-                "disinfection",
-                "16S rRNA Amplicon Sequencing"
-            ],
             "contactPoint": {
                 "fn": "Vicente Gomez-Alvarez",
                 "hasEmail": "mailto:gomez-alvarez.vicente@epa.gov"
             },
+            "description": "The bacteria sequence data generated in this study is available in the Short Read Archive (SRA) of NCBI (https://www.ncbi.nlm.nih.gov/) under BioProject PRJNA509718.",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA509718",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA509718"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA509718",
+                    "title": "https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA509718"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529855",
+            "keyword": [
+                "Drinking water distribution system",
+                "pathogens",
+                "disinfection",
+                "16S rRNA Amplicon Sequencing"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2018-12-13",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -189453,19 +189449,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Composition of active bacterial communities and presence of opportunistic pathogens in Finland (S02)"
         },
         {
-            "title": "Ecological Suitability ",
-            "description": "Data represent an example calculation of ecological suitability for Pensacola and Perdido Bays.  Data used are publicly available and are presented as tables, figures and appendices in the published paper. https://doi.org/10.1016/j.ecolind.2023.110896. \n\nThis dataset is associated with the following publication:\nSmith, L., E. Reschke, J. Bousquin, L. Cheskiewicz, N. Ilias, J. Summers, and J. Harvey. Methods for a composite ecological suitability measure to inform cumulative restoration assessments in Gulf of Mexico estuaries.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 154: 1-15, (2023).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Lisa Smith",
+                "hasEmail": "mailto:smith.lisam@epa.gov"
+            },
+            "description": "Data represent an example calculation of ecological suitability for Pensacola and Perdido Bays.  Data used are publicly available and are presented as tables, figures and appendices in the published paper. https://doi.org/10.1016/j.ecolind.2023.110896. \n\nThis dataset is associated with the following publication:\nSmith, L., E. Reschke, J. Bousquin, L. Cheskiewicz, N. Ilias, J. Summers, and J. Harvey. Methods for a composite ecological suitability measure to inform cumulative restoration assessments in Gulf of Mexico estuaries.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 154: 1-15, (2023).",
+            "distribution": [
+                {
+                    "accessURL": "https://doi.org/10.1016/j.ecolind.2023.110896.",
+                    "title": "https://doi.org/10.1016/j.ecolind.2023.110896."
+                }
             ],
             "identifier": "https://doi.org/10.23719/1529974",
             "keyword": [
@@ -189477,19 +189480,10 @@
                 "restoration",
                 "Gulf of Mexico estuaries"
             ],
-            "contactPoint": {
-                "fn": "Lisa Smith",
-                "hasEmail": "mailto:smith.lisam@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://doi.org/10.1016/j.ecolind.2023.110896.",
-                    "accessURL": "https://doi.org/10.1016/j.ecolind.2023.110896."
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license-non-epa-generated.html",
             "modified": "2023-07-14",
-            "references": [
-                "https://doi.org/10.1016/j.ecolind.2023.110896"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189499,51 +189493,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolind.2023.110896"
+            ],
+            "rights": null,
+            "title": "Ecological Suitability "
         },
         {
-            "title": "U.S. Food Waste Flows Between Sectors, 2018 v1.3.2",
-            "description": "These Flow-By-Sector (FBS) datasets capture food waste flows between waste-generating sectors and waste management pathways. The sectors are generally North American Industry Classification System (NAICS) 2012 codes. The first dataset, method 1 (m1), attributes food waste generation and disposition data from the USEPA Wasted Food Report to sectors. The second method, method 2 (m2), attributes wasted food data from the National Commercial Non-Hazardous Waste (CNHW) FBS dataset to sectors.\n\nThese food waste datasets were generated with FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2). M1 is generated with https://github.com/USEPA/flowsa/blob/v1.3.2/flowsa/methods/flowbysectormethods/Food_Waste_national_2018_m1.yaml and m2 is generated with https://github.com/USEPA/flowsa/blob/v1.3.2/flowsa/methods/flowbysectormethods/Food_Waste_national_2018_m2.yaml. The metadata text files included as a supporting document records the FLOWSA tool version and input dataset bibliographic details. The CNHW data were generated in FLOWSA v1.3.0, with the method file https://github.com/USEPA/flowsa/blob/v1.3.0/flowsa/methods/flowbysectormethods/CNHW_national_2018.yaml.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529936",
-            "keyword": [
-                "sector attribution model",
-                "NAICS",
-                "FLOWSA",
-                "Waste Management",
-                "Wasted Food Report"
-            ],
             "contactPoint": {
                 "fn": "Catherine Birney",
                 "hasEmail": "mailto:birney.catherine@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md",
+            "description": "These Flow-By-Sector (FBS) datasets capture food waste flows between waste-generating sectors and waste management pathways. The sectors are generally North American Industry Classification System (NAICS) 2012 codes. The first dataset, method 1 (m1), attributes food waste generation and disposition data from the USEPA Wasted Food Report to sectors. The second method, method 2 (m2), attributes wasted food data from the National Commercial Non-Hazardous Waste (CNHW) FBS dataset to sectors.\n\nThese food waste datasets were generated with FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2). M1 is generated with https://github.com/USEPA/flowsa/blob/v1.3.2/flowsa/methods/flowbysectormethods/Food_Waste_national_2018_m1.yaml and m2 is generated with https://github.com/USEPA/flowsa/blob/v1.3.2/flowsa/methods/flowbysectormethods/Food_Waste_national_2018_m2.yaml. The metadata text files included as a supporting document records the FLOWSA tool version and input dataset bibliographic details. The CNHW data were generated in FLOWSA v1.3.0, with the method file https://github.com/USEPA/flowsa/blob/v1.3.0/flowsa/methods/flowbysectormethods/CNHW_national_2018.yaml.",
             "distribution": [
                 {
-                    "title": "Food_Waste_national_2018_m2_v1.3.2_9b1bb41.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529936/Food_Waste_national_2018_m2_v1.3.2_9b1bb41.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Food_Waste_national_2018_m2_v1.3.2_9b1bb41.csv"
                 },
                 {
-                    "title": "Food_Waste_national_2018_m1_v1.3.2_9b1bb41.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529936/Food_Waste_national_2018_m1_v1.3.2_9b1bb41.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Food_Waste_national_2018_m1_v1.3.2_9b1bb41.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529936",
+            "keyword": [
+                "sector attribution model",
+                "NAICS",
+                "FLOWSA",
+                "Waste Management",
+                "Wasted Food Report"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-14",
-            "references": [
-                "https://figshare.com/articles/figure/_/24681378/0",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m1_v1.3.2_9b1bb41.parquet",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m1_v1.3.2_9b1bb41_metadata.json",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m2_v1.3.2_9b1bb41.parquet",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m2_v1.3.2_9b1bb41_metadata.json"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189554,42 +189545,44 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md"
+            "references": [
+                "https://figshare.com/articles/figure/_/24681378/0",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m1_v1.3.2_9b1bb41.parquet",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m1_v1.3.2_9b1bb41_metadata.json",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m2_v1.3.2_9b1bb41.parquet",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Food_Waste_national_2018_m2_v1.3.2_9b1bb41_metadata.json"
+            ],
+            "rights": null,
+            "title": "U.S. Food Waste Flows Between Sectors, 2018 v1.3.2"
         },
         {
-            "title": "U.S. Concrete Waste Flows Between Sectors, 2018 v1.3.2",
-            "description": "This dataset contains 2018 national concrete waste flows from waste-generating sectors to waste management pathways. The sectors are based on North American Industry Classification System (NAICS) 2012 codes. \n\nThese dataset was generated in FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) with https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/CDD_concrete_national_2018.yaml. The metadata text files included as a supporting document records the FLOWSA tool version and input dataset bibliographic details.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529937",
-            "keyword": [
-                "sector attribution model",
-                "NAICS",
-                "Waste Management"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md",
+            "description": "This dataset contains 2018 national concrete waste flows from waste-generating sectors to waste management pathways. The sectors are based on North American Industry Classification System (NAICS) 2012 codes. \n\nThese dataset was generated in FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) with https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/CDD_concrete_national_2018.yaml. The metadata text files included as a supporting document records the FLOWSA tool version and input dataset bibliographic details.",
             "distribution": [
                 {
-                    "title": "CDD_concrete_national_2018_v1.3.2_9b1bb41.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529937/CDD_concrete_national_2018_v1.3.2_9b1bb41.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "CDD_concrete_national_2018_v1.3.2_9b1bb41.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529937",
+            "keyword": [
+                "sector attribution model",
+                "NAICS",
+                "Waste Management"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-14",
-            "references": [
-                "https://figshare.com/articles/figure/_/24681357/0",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CDD_concrete_national_2018_v1.3.2_9b1bb41.parquet",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CDD_concrete_national_2018_v1.3.2_9b1bb41_metadata.json"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189600,42 +189593,42 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md"
+            "references": [
+                "https://figshare.com/articles/figure/_/24681357/0",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CDD_concrete_national_2018_v1.3.2_9b1bb41.parquet",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/CDD_concrete_national_2018_v1.3.2_9b1bb41_metadata.json"
+            ],
+            "rights": null,
+            "title": "U.S. Concrete Waste Flows Between Sectors, 2018 v1.3.2"
         },
         {
-            "title": "U.S. Total Waste Management by Sector and Material, 2018 v1.3.2",
-            "description": "This Flow-By-Sector (FBS) dataset quantifies waste management for U.S. generated waste by waste management pathway and 13 waste materials. The waste management pathways are assigned sector codes based on North American Industry Classification System (NAICS) 2012 codes. \n\nThis FBS was generated in FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) using the method file https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/Waste_national_2018.yaml.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529938",
-            "keyword": [
-                "sector attribution model",
-                "NAICS",
-                "Waste Management"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md",
+            "description": "This Flow-By-Sector (FBS) dataset quantifies waste management for U.S. generated waste by waste management pathway and 13 waste materials. The waste management pathways are assigned sector codes based on North American Industry Classification System (NAICS) 2012 codes. \n\nThis FBS was generated in FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) using the method file https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/Waste_national_2018.yaml.",
             "distribution": [
                 {
-                    "title": "Waste_national_2018_v1.3.2_9b1bb41.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529938/Waste_national_2018_v1.3.2_9b1bb41.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Waste_national_2018_v1.3.2_9b1bb41.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529938",
+            "keyword": [
+                "sector attribution model",
+                "NAICS",
+                "Waste Management"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-14",
-            "references": [
-                "https://figshare.com/articles/figure/_/24681297/0",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Waste_national_2018_v1.3.2_9b1bb41.parquet",
-                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Waste_national_2018_v1.3.2_9b1bb41_metadata.json"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -189646,39 +189639,43 @@
                     }
                 }
             },
-            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md"
+            "references": [
+                "https://figshare.com/articles/figure/_/24681297/0",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Waste_national_2018_v1.3.2_9b1bb41.parquet",
+                "https://dmap-data-commons-ord.s3.amazonaws.com/flowsa/FlowBySector/Waste_national_2018_v1.3.2_9b1bb41_metadata.json"
+            ],
+            "rights": null,
+            "title": "U.S. Total Waste Management by Sector and Material, 2018 v1.3.2"
         },
         {
-            "title": "U.S. Scaled WARM Waste Management by Sector and Material, 2018 v1.3.2",
-            "description": "Scaled WARM is a direct impacts model of GHG emissions, Employment, Wages, and Taxes attributed to material-specific waste management pathways. The waste management pathways are based on North American Industry Classification System (NAICS) 2012 codes. \n\nThis dataset is generated by fusing material-specific factors from the USEPA Waste Reduction Model (WARM) with waste generation data from USEPA Facts and Figures, Wasted Food Report, and CDDPath. Scaled WARM is generated with FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) and the method file https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/Mixed_WARM_national_2018.yaml.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1529939",
-            "keyword": [
-                "sector attribution model",
-                "NAICS",
-                "Waste Management"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://github.com/USEPA/flowsa/blob/v1.3.2/format%20specs/FlowBySector.md",
+            "description": "Scaled WARM is a direct impacts model of GHG emissions, Employment, Wages, and Taxes attributed to material-specific waste management pathways. The waste management pathways are based on North American Industry Classification System (NAICS) 2012 codes. \n\nThis dataset is generated by fusing material-specific factors from the USEPA Waste Reduction Model (WARM) with waste generation data from USEPA Facts and Figures, Wasted Food Report, and CDDPath. Scaled WARM is generated with FLOWSA v1.3.2 (https://github.com/USEPA/flowsa/tree/v1.3.2) and the method file https://github.com/USEPA/HIO/blob/v0.1.0/flowsa/flowbysectormethods/Mixed_WARM_national_2018.yaml.",
             "distribution": [
                 {
-                    "title": "Mixed_WARM_national_2018_v1.3.2_9b1bb41.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1529939/Mixed_WARM_national_2018_v1.3.2_9b1bb41.csv",
-                    "mediaType": "text/csv"
+                    "mediaType": "text/csv",
+                    "title": "Mixed_WARM_national_2018_v1.3.2_9b1bb41.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1529939",
+            "keyword": [
+                "sector attribution model",
+                "NAICS",
+                "Waste Management"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2023-12-14",
-            "references": null,
```

