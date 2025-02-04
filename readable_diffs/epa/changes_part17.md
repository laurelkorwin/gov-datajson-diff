# Change History for epa.json (Part 17)

### Changes from 31606f9 to dd2190f (Part 7/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "This data set is associated with the results found in the journal article: Valencia et al, 2018. Development and evaluation of the R-LINE model algorithms to account for chemical transformation in the near-road environment. Transportation Research Part D, https://doi.org/10.1016/j.trd.2018.01.028. \nTo address the need to estimate near-road NO2 concentrations, we implemented three different approaches in order of increasing degrees of complexity and barrier to implementation from simplest to more complex. The first is an empirical approach based upon fitting a 4th order polynomial to existing near-road observations across the continental U.S., the second involves a simplified Two-reaction chemical scheme, and the third involves a more detailed set of chemical reactions based upon the Generic Reaction Set (GRS) mechanism. All models were able to estimate more than 75% of  concentrations within a factor of two of the near-road monitoring data and produced comparable performance statistics. These results indicate that the performance of the new R-LINE chemistry algorithms for predicting NO2 is comparable to other models (i.e. ADMS-Roads with GRS), both showing less than\u00b115% fractional bias and less than 45% normalized mean square error. \n\nThis dataset is associated with the following publication:\nValencia, A., A. Venkatram, D. Heist, D. Carruthers , and S. Arunachalam. Development and evaluation of the R-LINE model algorithms to account for chemical transformation in the near-road environment.   Transportation Research Part D: Transport and Environment. Elsevier BV, AMSTERDAM,  NETHERLANDS, 59: 464-477, (2018).",
             "distribution": [
                 {
-                    "title": "HeistDavid_A-z099_Datafiles_RLINE_NO2.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1433507/HeistDavid_A-z099_Datafiles_RLINE_NO2.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "HeistDavid_A-z099_Datafiles_RLINE_NO2.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1433507",
+            "keyword": [
+                "air pollution",
+                "dispersion modeling",
+                "Mobile sources",
+                "exposure",
+                "near road"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-15",
-            "references": [
-                "https://doi.org/10.1016/j.trd.2018.01.028"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67158,20 +67154,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1433507/documents/HeistDavid_A-z099_DataDictionary_RLINE_NO2.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1016/j.trd.2018.01.028"
+            ],
+            "rights": null,
+            "title": "RLINE model algrotihms to account for NO2 near-road chemistry data set - RLINE_N02"
         },
         {
-            "title": "Characterization of Emissions from Liquid Fuel and Propane Open Burns",
-            "description": "emission factor data. \n\nThis dataset is associated with the following publication:\nAurell, J., D. Hubble, B. Gullett, A. Holder, E. Washburn, and D. Tabor. Characterization of Emissions from Liquid Fuel and Propane Open Burns.   Fire Technology. Springer International Publishing AG, Cham (ZG),  SWITZERLAND, 53(6): 2023-2038, (2017).",
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
+            "description": "emission factor data. \n\nThis dataset is associated with the following publication:\nAurell, J., D. Hubble, B. Gullett, A. Holder, E. Washburn, and D. Tabor. Characterization of Emissions from Liquid Fuel and Propane Open Burns.   Fire Technology. Springer International Publishing AG, Cham (ZG),  SWITZERLAND, 53(6): 2023-2038, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407527/Data%20Table%20Science%20Hub%20Dahlgren%2001-26-2017%20JA.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Table Science Hub Dahlgren 01-26-2017 JA.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407527",
             "keyword": [
@@ -67183,20 +67187,10 @@
                 "pool fire",
                 "fast cook off"
             ],
-            "contactPoint": {
-                "fn": "Brian Gullett",
-                "hasEmail": "mailto:gullett.brian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data Table Science Hub Dahlgren 01-26-2017 JA.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407527/Data%20Table%20Science%20Hub%20Dahlgren%2001-26-2017%20JA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-26",
-            "references": [
-                "https://doi.org/10.1007/s10694-017-0670-2"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67206,48 +67200,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10694-017-0670-2"
+            ],
+            "rights": null,
+            "title": "Characterization of Emissions from Liquid Fuel and Propane Open Burns"
         },
         {
-            "title": "Biofiltration of chloroform in a trickle bed air biofilter under acidic conditions",
-            "description": "In this paper, the application of biofiltration is investigated for controlled removal of gas phase chloroform through cometabolic degradation with ethanol. A trickle bed air biofilter (TBAB) operated under acidic pH 4 is subjected to aerobic biodegradation of chloroform and ethanol. The TBAB is composed of pelleted diatomaceous earth filter media inoculated with filamentous fungi species, which served as the principle biodegrading microorganism. \n\nThis dataset is associated with the following publication:\nPalanisamy , K., B.  Mezgebe , G. Sorial, and E. Sahle-Demessie. Biofiltration of Chloroform in a Trickle Bed Air Biofilter Under Acidic Conditions.   WATER, AIR, & SOIL POLLUTION. Springer, New York, NY, USA, 227: 478, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1435556",
-            "keyword": [
-                "biofiltration",
-                "Chloroform",
-                "filamentous fungi",
-                "cometabolism",
-                "ethanol",
-                "trickle bed air biofilter"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1435556/documents/Data%20Dictionary_BiotrickleFiltration.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "In this paper, the application of biofiltration is investigated for controlled removal of gas phase chloroform through cometabolic degradation with ethanol. A trickle bed air biofilter (TBAB) operated under acidic pH 4 is subjected to aerobic biodegradation of chloroform and ethanol. The TBAB is composed of pelleted diatomaceous earth filter media inoculated with filamentous fungi species, which served as the principle biodegrading microorganism. \n\nThis dataset is associated with the following publication:\nPalanisamy , K., B.  Mezgebe , G. Sorial, and E. Sahle-Demessie. Biofiltration of Chloroform in a Trickle Bed Air Biofilter Under Acidic Conditions.   WATER, AIR, & SOIL POLLUTION. Springer, New York, NY, USA, 227: 478, (2016).",
             "distribution": [
                 {
-                    "title": "G-STD-0016294-JA-5-0_Kertee'sPPR.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435556/G-STD-0016294-JA-5-0_Kertee%27sPPR.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "G-STD-0016294-JA-5-0_Kertee'sPPR.docx"
                 },
                 {
-                    "title": "G-STD-0016294-JA-5-0_Kertee'sPPR_Figures.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435556/G-STD-0016294-JA-5-0_Kertee%27sPPR_Figures.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "G-STD-0016294-JA-5-0_Kertee'sPPR_Figures.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435556",
+            "keyword": [
+                "biofiltration",
+                "Chloroform",
+                "filamentous fungi",
+                "cometabolism",
+                "ethanol",
+                "trickle bed air biofilter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-01",
-            "references": [
-                "https://doi.org/10.1007/s11270-016-3194-3"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67258,51 +67254,51 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1435556/documents/Data%20Dictionary_BiotrickleFiltration.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1007/s11270-016-3194-3"
+            ],
+            "rights": null,
+            "title": "Biofiltration of chloroform in a trickle bed air biofilter under acidic conditions"
         },
         {
-            "title": "Effect of natural organic matter effec on fate and transport of engineered nanoparticles ",
-            "description": "This study characterized Ohio river natural organic matter during winter and summer seasons, and demonstrated the effects of these natural organic samples on stability and transport of cerium oxide nanoparticles in saturated porous media. OR-NOM samples that were characterized by thermal analysis, Fourier transfer solid state neutron magnetic resonance spectrometer and elemental analysis showed to have structural and compositional differences from standard humic acid. This study explored the effects of OR-NOM in enhancing the transport and breakthrough of ceria nanoparticle in moderate (1-10 mM) ionic strength solutions. The enhancement in stability and transport appear to be dominated by the altered electrokinetic properties of the nanopraticles. \n\nThis dataset is associated with the following publication:\nLi, Z., E. Sahle-Demessie, A. Aly Hassan, J. Pressman, C. Han, and G. Sorial. Effects of source and seasonal variations of natural organic matters on the fate and transport of CeO2 nanoparticles in the environment.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 609: 1616-1626, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1407605",
-            "keyword": [
-                "engineered nanomaterials",
-                "natural organic matter",
-                "fourier transfer spectroscopy",
-                "Nanoparticles",
-                "CeO2",
-                "ssNMR-FTIR",
-                "packed-column transport",
-                "Ohio River"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407605/documents/Seasonal%20Variation%20of%20NOM_Data%20Dictionary.pdf",
+            "describedByType": "application/pdf",
+            "description": "This study characterized Ohio river natural organic matter during winter and summer seasons, and demonstrated the effects of these natural organic samples on stability and transport of cerium oxide nanoparticles in saturated porous media. OR-NOM samples that were characterized by thermal analysis, Fourier transfer solid state neutron magnetic resonance spectrometer and elemental analysis showed to have structural and compositional differences from standard humic acid. This study explored the effects of OR-NOM in enhancing the transport and breakthrough of ceria nanoparticle in moderate (1-10 mM) ionic strength solutions. The enhancement in stability and transport appear to be dominated by the altered electrokinetic properties of the nanopraticles. \n\nThis dataset is associated with the following publication:\nLi, Z., E. Sahle-Demessie, A. Aly Hassan, J. Pressman, C. Han, and G. Sorial. Effects of source and seasonal variations of natural organic matters on the fate and transport of CeO2 nanoparticles in the environment.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 609: 1616-1626, (2017).",
             "distribution": [
                 {
-                    "title": "Effects of source and seasonal variations of natural organic matters on the fate and transport of CeO2 nanoparticles i.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407605/Effects%20of%20source%20and%20seasonal%20variations%20of%20natural%20organic%20matters%20on%20the%20fate%20and%20transport%20of%20CeO2%20nanoparticles%20i.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Effects of source and seasonal variations of natural organic matters on the fate and transport of CeO2 nanoparticles i.pdf"
                 },
                 {
-                    "title": "Supplementary Data_NOM_CeO2_PPR.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407605/Supplementary%20Data_NOM_CeO2_PPR.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary Data_NOM_CeO2_PPR.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407605",
+            "keyword": [
+                "engineered nanomaterials",
+                "natural organic matter",
+                "fourier transfer spectroscopy",
+                "Nanoparticles",
+                "CeO2",
+                "ssNMR-FTIR",
+                "packed-column transport",
+                "Ohio River"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-02-01",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2017.07.154"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67313,20 +67309,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407605/documents/Seasonal%20Variation%20of%20NOM_Data%20Dictionary.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2017.07.154"
+            ],
+            "rights": null,
+            "title": "Effect of natural organic matter effec on fate and transport of engineered nanoparticles "
         },
         {
-            "title": "SA-PM versus SA-O3 complete data set_May 2014-August 2015",
-            "description": "Raw data of cardiac and ventilatory responses to SA-PM and SA-O3. \n\nThis dataset is associated with the following publication:\nHazari, M., K. Stratford, T. Krantz, C. King, J. Krug, A. Farraj, and I. Gilmour. Comparative cardiopulmonary effects of particulate matter- and ozone-enhanced smog atmospheres in mice.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(5): 3071-3080, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Mehdi Hazari",
+                "hasEmail": "mailto:hazari.mehdi@epa.gov"
+            },
+            "description": "Raw data of cardiac and ventilatory responses to SA-PM and SA-O3. \n\nThis dataset is associated with the following publication:\nHazari, M., K. Stratford, T. Krantz, C. King, J. Krug, A. Farraj, and I. Gilmour. Comparative cardiopulmonary effects of particulate matter- and ozone-enhanced smog atmospheres in mice.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(5): 3071-3080, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375203/SA-PM%20vs%20SA-O3_all%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SA-PM vs SA-O3_all data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1375203",
             "keyword": [
@@ -67339,20 +67343,10 @@
                 "Ozone",
                 "heart rate"
             ],
-            "contactPoint": {
-                "fn": "Mehdi Hazari",
-                "hasEmail": "mailto:hazari.mehdi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SA-PM vs SA-O3_all data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375203/SA-PM%20vs%20SA-O3_all%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-13",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b04880"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67362,42 +67356,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b04880"
+            ],
+            "rights": null,
+            "title": "SA-PM versus SA-O3 complete data set_May 2014-August 2015"
         },
         {
-            "title": "Figure Data and Table Data for Differential exposure and acute health impacts of inhaled solid-fuel emissions from rudimentary and advanced cookstoves in female CD-1 mice. ",
-            "description": "To link health benefits derived from advanced CS usage to increasing combustion efficiencies of the cookstove, a wide variety of general health and respiratory system parameters that are often altered acutely following exposure to air pollutants were assessed.  The figures and tables reflect the health outcomes. \n\nThis dataset is associated with the following publication:\nGibbs-Flournoy, E., I. Gilmour, M. Higuchi, J. Jetter, I. George, L. Copeland, R. Harrison, V. Moser, and J. Dye. Differential exposure and acute health impacts of inhaled solid-fuel emissions from rudimentary and advanced cookstoves in female CD-1 mice..   ENVIRONMENTAL RESEARCH. Academic Press Incorporated, Orlando, FL, USA, 161: 35-48, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1377833",
-            "keyword": [
-                "cookstoves",
-                "incomplete combustion",
-                "lung injury",
-                "oxidative stress",
-                "phagocytosis"
-            ],
             "contactPoint": {
                 "fn": "Janice Dye",
                 "hasEmail": "mailto:dye.janice@epa.gov"
             },
+            "description": "To link health benefits derived from advanced CS usage to increasing combustion efficiencies of the cookstove, a wide variety of general health and respiratory system parameters that are often altered acutely following exposure to air pollutants were assessed.  The figures and tables reflect the health outcomes. \n\nThis dataset is associated with the following publication:\nGibbs-Flournoy, E., I. Gilmour, M. Higuchi, J. Jetter, I. George, L. Copeland, R. Harrison, V. Moser, and J. Dye. Differential exposure and acute health impacts of inhaled solid-fuel emissions from rudimentary and advanced cookstoves in female CD-1 mice..   ENVIRONMENTAL RESEARCH. Academic Press Incorporated, Orlando, FL, USA, 161: 35-48, (2018).",
             "distribution": [
                 {
-                    "title": "ScienceHub-Gibbs-Cookstoves_Figs&TablesFINAL.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1377833/ScienceHub-Gibbs-Cookstoves_Figs%26TablesFINAL.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHub-Gibbs-Cookstoves_Figs&TablesFINAL.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1377833",
+            "keyword": [
+                "cookstoves",
+                "incomplete combustion",
+                "lung injury",
+                "oxidative stress",
+                "phagocytosis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-30",
-            "references": [
-                "https://doi.org/10.1016/j.envres.2017.10.043"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67407,19 +67401,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envres.2017.10.043"
+            ],
+            "rights": null,
+            "title": "Figure Data and Table Data for Differential exposure and acute health impacts of inhaled solid-fuel emissions from rudimentary and advanced cookstoves in female CD-1 mice. "
         },
         {
-            "title": "See appendices K-N in report at http://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693",
-            "description": "See report at: http://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693. \n\nThis dataset is associated with the following publication:\nJulius , S., J. Blue, and N. Hiremath. Urban Resilience to Climate Change: Washington, DC and Worcester, MA Case Studies. U.S. Environmental Protection Agency, Washington, DC, USA, 2017.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Susan Julius",
+                "hasEmail": "mailto:julius.susan@epa.gov"
+            },
+            "describedBy": "https://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693",
+            "description": "See report at: http://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693. \n\nThis dataset is associated with the following publication:\nJulius , S., J. Blue, and N. Hiremath. Urban Resilience to Climate Change: Washington, DC and Worcester, MA Case Studies. U.S. Environmental Protection Agency, Washington, DC, USA, 2017.",
+            "distribution": [
+                {
+                    "accessURL": "https://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693",
+                    "title": "https://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407611",
             "keyword": [
@@ -67434,18 +67438,11 @@
                 "Vulnerability",
                 "indicators"
             ],
-            "contactPoint": {
-                "fn": "Susan Julius",
-                "hasEmail": "mailto:julius.susan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693",
-                    "accessURL": "https://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-13",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -67455,148 +67452,145 @@
                     }
                 }
             },
-            "describedBy": "https://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693"
+            "references": null,
+            "rights": null,
+            "title": "See appendices K-N in report at http://ofmpub.epa.gov/eims/eimscomm.getfile?p_download_id=530693"
         },
         {
-            "title": "AOP-Wiki Event Component Annotation",
-            "description": "This dataset contains ontology terms associated with key events from the AOP-Wiki.  This information was used to seed the AOP-Wiki with a carefully selected set of ontology terms prior to opening up the option for authors to tag their own AOPs. This is intended to provide existing examples for authors and improve consistency when assigning terms to the key events. \n\nThis dataset is associated with the following publication:\nIves, C., I. Campia, R. Wang, C. Wittwehr, and S. Edwards. Creating a Structured Adverse Outcome Pathway Knowledgebase via Ontology-Based Annotations.   Applied In Vitro Toxicology. Mary Ann Liebert, Inc., Larchmont, NY, USA, 3(4): 298-311, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1407549",
-            "keyword": [
-                "adverse outcome pathway",
-                "key event",
-                "ontology",
-                "knowledgebase"
-            ],
             "contactPoint": {
                 "fn": "Stephen Edwards",
                 "hasEmail": "mailto:edwards.stephen@epa.gov"
             },
+            "description": "This dataset contains ontology terms associated with key events from the AOP-Wiki.  This information was used to seed the AOP-Wiki with a carefully selected set of ontology terms prior to opening up the option for authors to tag their own AOPs. This is intended to provide existing examples for authors and improve consistency when assigning terms to the key events. \n\nThis dataset is associated with the following publication:\nIves, C., I. Campia, R. Wang, C. Wittwehr, and S. Edwards. Creating a Structured Adverse Outcome Pathway Knowledgebase via Ontology-Based Annotations.   Applied In Vitro Toxicology. Mary Ann Liebert, Inc., Larchmont, NY, USA, 3(4): 298-311, (2017).",
             "distribution": [
                 {
-                    "title": "https://aopwiki.org",
-                    "accessURL": "https://aopwiki.org"
+                    "accessURL": "https://aopwiki.org",
+                    "title": "https://aopwiki.org"
                 },
                 {
-                    "title": "CIvesSupplementaryTables_revised_08-04-17.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407549/CIvesSupplementaryTables_revised_08-04-17.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CIvesSupplementaryTables_revised_08-04-17.xlsx"
                 }
             ],
-            "modified": "2017-05-16",
-            "references": [
-                "https://doi.org/10.1089/aivt.2017.0017"
+            "identifier": "https://doi.org/10.23719/1407549",
+            "keyword": [
+                "adverse outcome pathway",
+                "key event",
+                "ontology",
+                "knowledgebase"
             ],
-            "publisher": {
-                "name": "U.S. EPA Office of Research and Development (ORD)",
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
+            "modified": "2017-05-16",
+            "programCode": [
+                "020:095"
+            ],
+            "publisher": {
+                "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
                     "name": "U.S. Environmental Protection Agency",
                     "subOrganizationOf": {
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1089/aivt.2017.0017"
+            ],
+            "rights": null,
+            "title": "AOP-Wiki Event Component Annotation"
         },
         {
-            "title": " Safe Drinking Water Information System (SDWIS) Federal Reports Advanced Search Tool",
-            "description": "A database where EPA has compiled data on public drinking water systems and whether they have certain drinking water violations.  This data is collected by the states and given to the EPA. \n\nThis dataset is associated with the following publication:\nPennino, M., J. Compton, and S. Leibowitz. Trends in Drinking Water Nitrate Violations Across the United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  13450-13460, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407575",
-            "keyword": [
-                "violation",
-                "contaminants in water systems",
-                "Clean Water Act",
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
+            "description": "A database where EPA has compiled data on public drinking water systems and whether they have certain drinking water violations.  This data is collected by the states and given to the EPA. \n\nThis dataset is associated with the following publication:\nPennino, M., J. Compton, and S. Leibowitz. Trends in Drinking Water Nitrate Violations Across the United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  13450-13460, (2017).",
             "distribution": [
                 {
-                    "title": "https://ofmpub.epa.gov/apex/sfdw/f?p=108:9:::NO::P9_REPORT:VIO",
-                    "accessURL": "https://ofmpub.epa.gov/apex/sfdw/f?p=108:9:::NO::P9_REPORT:VIO"
+                    "accessURL": "https://ofmpub.epa.gov/apex/sfdw/f?p=108:9:::NO::P9_REPORT:VIO",
+                    "title": "https://ofmpub.epa.gov/apex/sfdw/f?p=108:9:::NO::P9_REPORT:VIO"
                 },
                 {
-                    "title": "Mean_Annual_NO3_Pop_Served_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/Mean_Annual_NO3_Pop_Served_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mean_Annual_NO3_Pop_Served_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "Mean_Annual_NO3_Violations_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/Mean_Annual_NO3_Violations_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mean_Annual_NO3_Violations_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_NO3_Violation_Duration_State_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_NO3_Violation_Duration_State_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_NO3_Violation_Duration_State_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_NO3_Violations_Over_Time_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_NO3_Violations_Over_Time_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_NO3_Violations_Over_Time_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_GW_NO3_Violations_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_GW_NO3_Violations_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_GW_NO3_Violations_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_NO3_Pop_Served_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_NO3_Pop_Served_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_NO3_Pop_Served_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_NO3_Violations_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_NO3_Violations_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_NO3_Violations_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_Percent_GW_NO3_Violations_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_Percent_GW_NO3_Violations_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_Percent_GW_NO3_Violations_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_Percent_GWSW_Violations_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_Percent_GWSW_Violations_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_Percent_GWSW_Violations_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_Percent_SW_NO3_Violations_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_Percent_SW_NO3_Violations_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_Percent_SW_NO3_Violations_County_1994-2016_FINAL.csv"
                 },
                 {
-                    "title": "SDWIS_SW_NO3_Violations_County_1994-2016_FINAL.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407575/SDWIS_SW_NO3_Violations_County_1994-2016_FINAL.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SDWIS_SW_NO3_Violations_County_1994-2016_FINAL.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407575",
+            "keyword": [
+                "violation",
+                "contaminants in water systems",
+                "Clean Water Act",
+                "drinking water",
+                "nitrate",
+                "nitrate in groundwater",
+                "maximum contaminant level",
+                "surface water",
+                "public water systems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-30",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b04269"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67606,19 +67600,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b04269"
+            ],
+            "rights": null,
+            "title": " Safe Drinking Water Information System (SDWIS) Federal Reports Advanced Search Tool"
         },
         {
-            "title": "Photochemical smog and vitamin D deficiency",
-            "description": "The dataset contains the results of a study examining the impact of vitamin D deficiency on the cardiopulmonary response of mice to photochemical smog. \n\nThis dataset is associated with the following publication:\nStratford, K., N. Coates, L. Thompson, T. Krantz, C. King, J. Krug, I. Gilmour, A. Farraj, and M. Hazari. Early-Life Persistent Vitamin D Deficiency Alters Cardiopulmonary Responses to Particulate Matter-Enhanced Atmospheric Smog in Adult Mice.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(5): 3054-3061, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Mehdi Hazari",
+                "hasEmail": "mailto:hazari.mehdi@epa.gov"
+            },
+            "description": "The dataset contains the results of a study examining the impact of vitamin D deficiency on the cardiopulmonary response of mice to photochemical smog. \n\nThis dataset is associated with the following publication:\nStratford, K., N. Coates, L. Thompson, T. Krantz, C. King, J. Krug, I. Gilmour, A. Farraj, and M. Hazari. Early-Life Persistent Vitamin D Deficiency Alters Cardiopulmonary Responses to Particulate Matter-Enhanced Atmospheric Smog in Adult Mice.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(5): 3054-3061, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375240/Vitamin%20D%20and%20smog%20ECG.HRV.WBP%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Vitamin D and smog ECG.HRV.WBP data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1375240",
             "keyword": [
@@ -67631,20 +67635,10 @@
                 "PM",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Mehdi Hazari",
-                "hasEmail": "mailto:hazari.mehdi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Vitamin D and smog ECG.HRV.WBP data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375240/Vitamin%20D%20and%20smog%20ECG.HRV.WBP%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-08-09",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b04882"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67654,19 +67648,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b04882"
+            ],
+            "rights": null,
+            "title": "Photochemical smog and vitamin D deficiency"
         },
         {
-            "title": "Light-absorbing organic carbon from prescribed and laboratory biomass burning and gasoline vehicle emissions",
-            "description": "This dataset is a compilation of optical properties of the organic fraction of particulate matter emitted from prescribed burning and from gasoline vehicles. \n\nThis dataset is associated with the following publication:\nXie, M., M. Hays, and A. Holder. Light absorbing organic carbon from prescribed and laboratory biomass burning and gasoline vehicle emissions.   Scientific Reports. Nature Publishing Group, London,  UK,  online, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Amara Holder",
+                "hasEmail": "mailto:holder.amara@epa.gov"
+            },
+            "description": "This dataset is a compilation of optical properties of the organic fraction of particulate matter emitted from prescribed burning and from gasoline vehicles. \n\nThis dataset is associated with the following publication:\nXie, M., M. Hays, and A. Holder. Light absorbing organic carbon from prescribed and laboratory biomass burning and gasoline vehicle emissions.   Scientific Reports. Nature Publishing Group, London,  UK,  online, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375575/Scientific%20Reports2017%20Data%20Tables%20and%20Dictionary.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Scientific Reports2017 Data Tables and Dictionary.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1375575",
             "keyword": [
@@ -67679,20 +67683,10 @@
                 "Aerosol Optical Properties",
                 "Secondary Organic Aerosol"
             ],
-            "contactPoint": {
-                "fn": "Amara Holder",
-                "hasEmail": "mailto:holder.amara@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Scientific Reports2017 Data Tables and Dictionary.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375575/Scientific%20Reports2017%20Data%20Tables%20and%20Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-01",
-            "references": [
-                "https://doi.org/10.1038/s41598-017-06981-8"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67702,19 +67696,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-017-06981-8"
+            ],
+            "rights": null,
+            "title": "Light-absorbing organic carbon from prescribed and laboratory biomass burning and gasoline vehicle emissions"
         },
         {
-            "title": "Data set for Light Absorption of Secondary Organic Aerosol: Composition and Contribution of Nitro-aromatic Compounds",
-            "description": "This is the data used to generate the figures published in the journal article titled, \"Light Absorption of Secondary Organic Aerosol: Composition and Contribution of Nitro-aromatic Compounds\". \n\nThis dataset is associated with the following publication:\nXie, M., X. Chen, M. Hays, M. Lewandowski, J. Offenberg, T. Kleindienst, and A. Holder. Light absorption of secondary organic aerosol: Composition and contribution of nitro-aromatic compounds.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 51(20): 11607-11616, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Amara Holder",
+                "hasEmail": "mailto:holder.amara@epa.gov"
+            },
+            "description": "This is the data used to generate the figures published in the journal article titled, \"Light Absorption of Secondary Organic Aerosol: Composition and Contribution of Nitro-aromatic Compounds\". \n\nThis dataset is associated with the following publication:\nXie, M., X. Chen, M. Hays, M. Lewandowski, J. Offenberg, T. Kleindienst, and A. Holder. Light absorption of secondary organic aerosol: Composition and contribution of nitro-aromatic compounds.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 51(20): 11607-11616, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407634/Environmental%20Science%20and%20Technology%202017%20Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Environmental Science and Technology 2017 Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407634",
             "keyword": [
@@ -67726,20 +67730,10 @@
                 "Aerosol Optical Properties",
                 "Secondary Organic Aerosol"
             ],
-            "contactPoint": {
-                "fn": "Amara Holder",
-                "hasEmail": "mailto:holder.amara@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Environmental Science and Technology 2017 Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407634/Environmental%20Science%20and%20Technology%202017%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-28",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b03263"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67749,41 +67743,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b03263"
+            ],
+            "rights": null,
+            "title": "Data set for Light Absorption of Secondary Organic Aerosol: Composition and Contribution of Nitro-aromatic Compounds"
         },
         {
-            "title": "Data used in manuscript \"Modeling crop residue burning experiments and assessing the fire impacts on air quality\"",
-            "description": "The data sets includes the data used to generate the figures presented in the manuscript.  Each worksheet in the attached file provides data for a specific figure (as labeled). \n\nThis dataset is associated with the following publication:\nZhou, L., K. Baker, S. Napelenok, G. Pouliot, R. Elleman, S. O'Neill, S. Urbanski, and D. Wong. Modeling crop residue burning experiments to evaluate smoke emissions and plume transport.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 627: 523-533, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1434485",
-            "keyword": [
-                "air quality",
-                "biomass burning",
-                "emissions",
-                "smoke plume"
-            ],
             "contactPoint": {
                 "fn": "Sergey Napelenok",
                 "hasEmail": "mailto:napelenok.sergey@epa.gov"
             },
+            "description": "The data sets includes the data used to generate the figures presented in the manuscript.  Each worksheet in the attached file provides data for a specific figure (as labeled). \n\nThis dataset is associated with the following publication:\nZhou, L., K. Baker, S. Napelenok, G. Pouliot, R. Elleman, S. O'Neill, S. Urbanski, and D. Wong. Modeling crop residue burning experiments to evaluate smoke emissions and plume transport.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 627: 523-533, (2018).",
             "distribution": [
                 {
-                    "title": "Zhou2017_agburn_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434485/Zhou2017_agburn_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Zhou2017_agburn_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434485",
+            "keyword": [
+                "air quality",
+                "biomass burning",
+                "emissions",
+                "smoke plume"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-31",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2018.01.237"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67793,19 +67787,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2018.01.237"
+            ],
+            "rights": null,
+            "title": "Data used in manuscript \"Modeling crop residue burning experiments and assessing the fire impacts on air quality\""
         },
         {
-            "title": "Estimation of spatial and temporal variation in light attenuation due to epigrowth on Zostera marina in Yaquina Bay",
-            "description": "Data on epiphyte load, Zostera marina biomass, nutrients, and mesograzers on epiphytes for a 4 year period at six stations within Yaquina Bay, OR. Data were used to generate the figures contained in the paper \"An evaluation of factors controlling the abundance of epiphytes on Zostera marina along an estuarine gradient in Yaquina Bay, Oregon, USA\". \n\nThis dataset is associated with the following publication:\nNelson, W. An evaluation of factors controlling the abundance of epiphytes on Zostera marina along an estuarine gradient in Yaquina Bay, Oregon, USA..   AQUATIC BOTANY. Elsevier Science Ltd, New York, NY, USA, 148: 53-63, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Walter Nelson",
+                "hasEmail": "mailto:nelson.walt@epa.gov"
+            },
+            "description": "Data on epiphyte load, Zostera marina biomass, nutrients, and mesograzers on epiphytes for a 4 year period at six stations within Yaquina Bay, OR. Data were used to generate the figures contained in the paper \"An evaluation of factors controlling the abundance of epiphytes on Zostera marina along an estuarine gradient in Yaquina Bay, Oregon, USA\". \n\nThis dataset is associated with the following publication:\nNelson, W. An evaluation of factors controlling the abundance of epiphytes on Zostera marina along an estuarine gradient in Yaquina Bay, Oregon, USA..   AQUATIC BOTANY. Elsevier Science Ltd, New York, NY, USA, 148: 53-63, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375802/Nelson%20factors%20controlling%20Epiphyte%20Load%20SciHub%20figure%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Nelson factors controlling Epiphyte Load SciHub figure data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1375802",
             "keyword": [
@@ -67816,20 +67820,10 @@
                 "phosphorus",
                 "Mesograzers"
             ],
-            "contactPoint": {
-                "fn": "Walter Nelson",
-                "hasEmail": "mailto:nelson.walt@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Nelson factors controlling Epiphyte Load SciHub figure data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375802/Nelson%20factors%20controlling%20Epiphyte%20Load%20SciHub%20figure%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-08",
-            "references": [
-                "https://doi.org/10.1016/j.aquabot.2018.04.010"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67839,19 +67833,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.aquabot.2018.04.010"
+            ],
+            "rights": null,
+            "title": "Estimation of spatial and temporal variation in light attenuation due to epigrowth on Zostera marina in Yaquina Bay"
         },
         {
-            "title": "TDS-TSS-Flow Data Used_IMWA_Eval Relationships between TDS and TSS in a mining-influenced watershed",
-            "description": "TDS, TSS, and Flow data used for developing and testing relationships in the Clear Creek Watershed, Colorado.  Data for development of relationships was collected by Barbara Butler while at the Colorado School of Mines.  Data for testing relationships was obtained from Tim Steele of TDS Consulting in Colorado as provided by the Upper Clear Creek Watershed Association. \n\nThis dataset is associated with the following publication:\nButler, B., and R. Ford. Evaluating Relationships Between Total Dissolved Solids (TDS) and Total Suspended Solids (TSS) in a Mining-Influenced Watershed.  Bob Kleinmann  Mine Water and the Environment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 37(1): 18-30, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Barbara Butler",
+                "hasEmail": "mailto:butler.barbara@epa.gov"
+            },
+            "description": "TDS, TSS, and Flow data used for developing and testing relationships in the Clear Creek Watershed, Colorado.  Data for development of relationships was collected by Barbara Butler while at the Colorado School of Mines.  Data for testing relationships was obtained from Tim Steele of TDS Consulting in Colorado as provided by the Upper Clear Creek Watershed Association. \n\nThis dataset is associated with the following publication:\nButler, B., and R. Ford. Evaluating Relationships Between Total Dissolved Solids (TDS) and Total Suspended Solids (TSS) in a Mining-Influenced Watershed.  Bob Kleinmann  Mine Water and the Environment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 37(1): 18-30, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407561/TDS-TSS-Flow%20Data%20Used_IMWA_Eval%20Relationships%20between%20TDS%20and%20TSS%20in%20a%20mining-influenced%20watershed.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TDS-TSS-Flow Data Used_IMWA_Eval Relationships between TDS and TSS in a mining-influenced watershed.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407561",
             "keyword": [
@@ -67864,20 +67868,10 @@
                 "mining-influenced water",
                 "water quality monitoring"
             ],
-            "contactPoint": {
-                "fn": "Barbara Butler",
-                "hasEmail": "mailto:butler.barbara@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "TDS-TSS-Flow Data Used_IMWA_Eval Relationships between TDS and TSS in a mining-influenced watershed.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407561/TDS-TSS-Flow%20Data%20Used_IMWA_Eval%20Relationships%20between%20TDS%20and%20TSS%20in%20a%20mining-influenced%20watershed.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-07",
-            "references": [
-                "https://doi.org/10.1007/s10230-017-0484-y"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67887,19 +67881,36 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10230-017-0484-y"
+            ],
+            "rights": null,
+            "title": "TDS-TSS-Flow Data Used_IMWA_Eval Relationships between TDS and TSS in a mining-influenced watershed"
         },
         {
-            "title": "Florida Estuary Optics 2009-2012",
-            "description": "Small boat surveys were conducted in four Florida estuaries along the northern Gulf of Mexico from September 2009 through January 2012.  The systems selected represent a range of optical characteristics (e.g., high vs. low particulate loads) and were of sufficient size to be adequately resolved with remote sensing imagery. The systems sampled were Pensacola Bay, Choctawhatchee Bay, St. Andrews Bay, and St. Joseph Bay.  Field data collection included discrete water samples, profiling water quality data, and above/below water in-situ hyperspectral optical measures.. \n\nThis dataset is associated with the following publication:\nSari Austuti, I., D. Mishra, S. Mishra, and B. Schaeffer. Spatio-temporal dynamics of inherent optical properties in oligotrophic northern Gulf of Mexico estuaries.   Continental Shelf Research. Elsevier BV, AMSTERDAM,  NETHERLANDS, 166: 92-107, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Blake Schaeffer",
+                "hasEmail": "mailto:schaeffer.blake@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1424031/documents/FL_estuaries_data_dictionary.pdf",
+            "describedByType": "application/pdf",
+            "description": "Small boat surveys were conducted in four Florida estuaries along the northern Gulf of Mexico from September 2009 through January 2012.  The systems selected represent a range of optical characteristics (e.g., high vs. low particulate loads) and were of sufficient size to be adequately resolved with remote sensing imagery. The systems sampled were Pensacola Bay, Choctawhatchee Bay, St. Andrews Bay, and St. Joseph Bay.  Field data collection included discrete water samples, profiling water quality data, and above/below water in-situ hyperspectral optical measures.. \n\nThis dataset is associated with the following publication:\nSari Austuti, I., D. Mishra, S. Mishra, and B. Schaeffer. Spatio-temporal dynamics of inherent optical properties in oligotrophic northern Gulf of Mexico estuaries.   Continental Shelf Research. Elsevier BV, AMSTERDAM,  NETHERLANDS, 166: 92-107, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1424031/FL_Optics_data.zip",
+                    "mediaType": "application/zip",
+                    "title": "FL_Optics_data.zip"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1424031/FL_Estuaries_updated.zip",
+                    "mediaType": "application/zip",
+                    "title": "FL_Estuaries_updated.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1424031",
             "keyword": [
@@ -67913,25 +67924,10 @@
                 "Pensacola Bay",
                 "and St. Joseph Bay"
             ],
-            "contactPoint": {
-                "fn": "Blake Schaeffer",
-                "hasEmail": "mailto:schaeffer.blake@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "FL_Optics_data.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1424031/FL_Optics_data.zip",
-                    "mediaType": "application/zip"
-                },
-                {
-                    "title": "FL_Estuaries_updated.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1424031/FL_Estuaries_updated.zip",
-                    "mediaType": "application/zip"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-01-01",
-            "references": [
-                "https://doi.org/10.1016/j.csr.2018.06.016"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67942,20 +67938,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1424031/documents/FL_estuaries_data_dictionary.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1016/j.csr.2018.06.016"
+            ],
+            "rights": null,
+            "title": "Florida Estuary Optics 2009-2012"
         },
         {
-            "title": "Dataset for paper: Evaluating the performance of household liquefied petroleum gas cookstoves",
-            "description": "This dataset provides supporting information for figures in the journal article entitled: Evaluating the performance of household liquefied petroleum gas cookstoves. \n\nThis dataset is associated with the following publication:\nShen, G., J. Jetter, K. Smith, C. Williams, J. Faircloth, and M. Hays. Evaluating the Performance of Household Liquefied Petroleum Gas Cookstoves.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(2): 904-915, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "James Jetter",
+                "hasEmail": "mailto:jetter.jim@epa.gov"
+            },
+            "description": "This dataset provides supporting information for figures in the journal article entitled: Evaluating the performance of household liquefied petroleum gas cookstoves. \n\nThis dataset is associated with the following publication:\nShen, G., J. Jetter, K. Smith, C. Williams, J. Faircloth, and M. Hays. Evaluating the Performance of Household Liquefied Petroleum Gas Cookstoves.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(2): 904-915, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407647/Data%20in%20LPG%20paper-%2020180505.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data in LPG paper- 20180505.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407647",
             "keyword": [
@@ -67966,20 +67970,10 @@
                 "emission",
                 "efficiency"
             ],
-            "contactPoint": {
-                "fn": "James Jetter",
-                "hasEmail": "mailto:jetter.jim@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data in LPG paper- 20180505.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407647/Data%20in%20LPG%20paper-%2020180505.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-21",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b05155"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -67989,19 +67983,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b05155"
+            ],
+            "rights": null,
+            "title": "Dataset for paper: Evaluating the performance of household liquefied petroleum gas cookstoves"
         },
         {
-            "title": "Blood Pb prediction with SHEDS-MM witth IEUBK",
-            "description": "The data is related to all figures and tables presented in the journal article. All data is written using the SAS software data format. \n\nThis dataset is associated with the following publication:\nZartarian, V., J. Xue, R. Tornero-Velez, and J. Brown. Children\u2019s Lead Exposure: A Multimedia Modeling Analysis to Guide Public Health Decision-Making.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(9): 1-10, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Valerie Zartarian Morrison",
+                "hasEmail": "mailto:zartarian.valerie@epa.gov"
+            },
+            "description": "The data is related to all figures and tables presented in the journal article. All data is written using the SAS software data format. \n\nThis dataset is associated with the following publication:\nZartarian, V., J. Xue, R. Tornero-Velez, and J. Brown. Children\u2019s Lead Exposure: A Multimedia Modeling Analysis to Guide Public Health Decision-Making.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(9): 1-10, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407554/XueJianping_2.63.6_Data_5-22-2017.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "XueJianping_2.63.6_Data_5-22-2017.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407554",
             "keyword": [
@@ -68015,21 +68019,10 @@
                 "model evaluation",
                 "lead copper rule"
             ],
-            "contactPoint": {
-                "fn": "Valerie Zartarian Morrison",
-                "hasEmail": "mailto:zartarian.valerie@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "XueJianping_2.63.6_Data_5-22-2017.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407554/XueJianping_2.63.6_Data_5-22-2017.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-01",
-            "references": [
-                "https://doi.org/10.1289/ehp1605",
-                "https://www.epa.gov/dwstandardsregulations/lead-modeling-peer-review"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68039,41 +68032,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp1605",
+                "https://www.epa.gov/dwstandardsregulations/lead-modeling-peer-review"
+            ],
+            "rights": null,
+            "title": "Blood Pb prediction with SHEDS-MM witth IEUBK"
         },
         {
-            "title": "Gridded Hourly O3 Data for BASE case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378452",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378452/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_O3_Base.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378452/ImEtAl_Gridded_Data_O3_Base.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_O3_Base.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378452",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68084,42 +68080,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378452/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly O3 Data for BASE case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly O3 Data for NAM case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378453",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378453/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_O3_NAM.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378453/ImEtAl_Gridded_Data_O3_NAM.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_O3_NAM.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378453",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68130,42 +68126,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378453/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly O3 Data for NAM case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly O3 Data for GLO case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378454",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378454/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_O3_GLO.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378454/ImEtAl_Gridded_Data_O3_GLO.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_O3_GLO.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378454",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68176,42 +68172,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378454/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly O3 Data for GLO case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly O3 Data for EAS case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378455",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378455/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_O3_EAS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378455/ImEtAl_Gridded_Data_O3_EAS.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_O3_EAS.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378455",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68222,42 +68218,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378455/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly O3 Data for EAS case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly CO Data for BASE case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378456",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378456/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_CO_Base.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378456/ImEtAl_Gridded_Data_CO_Base.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_CO_Base.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378456",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68268,42 +68264,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378456/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly CO Data for BASE case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly CO Data for NAM case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378457",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378457/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_CO_NAM.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378457/ImEtAl_Gridded_Data_CO_NAM.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_CO_NAM.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378457",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68314,42 +68310,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378457/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly CO Data for NAM case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly CO Data for EAS case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378458",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378458/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_CO_EAS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378458/ImEtAl_Gridded_Data_CO_EAS.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_CO_EAS.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378458",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68360,42 +68356,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378458/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly CO Data for EAS case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly CO Data for GLO case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378459",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378459/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_CO_GLO.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378459/ImEtAl_Gridded_Data_CO_GLO.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_CO_GLO.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378459",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68406,42 +68402,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378459/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly CO Data for GLO case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly PM2.5 Data for BASE case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378460",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378460/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_PM2_5_Base.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378460/ImEtAl_Gridded_Data_PM2_5_Base.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_PM2_5_Base.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378460",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68452,42 +68448,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378460/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly PM2.5 Data for BASE case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly PM2.5 Data for EAS case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378461",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378461/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_PM2_5_EAS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378461/ImEtAl_Gridded_Data_PM2_5_EAS.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_PM2_5_EAS.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378461",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68498,42 +68494,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378461/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly PM2.5 Data for EAS case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly PM2.5 Data for NAM case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378462",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378462/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_PM2_5_NAM.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378462/ImEtAl_Gridded_Data_PM2_5_NAM.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_PM2_5_NAM.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378462",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68544,42 +68540,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378462/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly PM2.5 Data for NAM case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly PM2.5 Data for GLO case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378463",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378463/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_PM2_5_GLO.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378463/ImEtAl_Gridded_Data_PM2_5_GLO.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_PM2_5_GLO.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378463",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68590,42 +68586,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378463/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly PM2.5 Data for GLO case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly SO2 Data for BASE case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378464",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378464/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_SO2_Base.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378464/ImEtAl_Gridded_Data_SO2_Base.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_SO2_Base.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378464",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68636,42 +68632,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378464/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly SO2 Data for BASE case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly SO2 Data for NAM case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378465",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378465/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_SO2_NAM.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378465/ImEtAl_Gridded_Data_SO2_NAM.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_SO2_NAM.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378465",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68682,42 +68678,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378465/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly SO2 Data for NAM case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly SO2 Data for EAS case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378466",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378466/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_SO2_EAS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378466/ImEtAl_Gridded_Data_SO2_EAS.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_SO2_EAS.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378466",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68728,42 +68724,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378466/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly SO2 Data for EAS case contributed by USEPA"
         },
         {
-            "title": "Gridded Hourly SO2 Data for GLO case contributed by USEPA",
-            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1378467",
-            "keyword": [
-                "ensemble modeling",
-                "air quality health impacts",
-                "economic valuation of health impacts",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378467/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains data contributed by EPA/ORD/NERL/CED researchers to the manuscript \" Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Brandt, C. Geels, K. Hansen, J. Christensen, M. Andersen, E. Solazzo, I. Kioutsioukis, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, C. Liang, U. Nopmongcol, G. Pirovano, L. Pozzoli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, J. West, G. Yarwood, C. Hogrefe, and S. Galmarini. Assessment and economic valuation of air pollution impacts on human health over Europe and the United States as calculated by a multi-model ensemble in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 5967-5989, (2018).",
             "distribution": [
                 {
-                    "title": "ImEtAl_Gridded_Data_SO2_GLO.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378467/ImEtAl_Gridded_Data_SO2_GLO.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ImEtAl_Gridded_Data_SO2_GLO.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378467",
+            "keyword": [
+                "ensemble modeling",
+                "air quality health impacts",
+                "economic valuation of health impacts",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-5967-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68774,42 +68770,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378467/documents/HogrefeChristian_A-02v7_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-5967-2018"
+            ],
+            "rights": null,
+            "title": "Gridded Hourly SO2 Data for GLO case contributed by USEPA"
         },
         {
-            "title": "A Workflow for Identifying Metabolically Active Chemicals to Complement in vitro Toxicity Screening",
-            "description": "This data includes metabolite predictions for in vitro inactive chemicals, predictions of those metabolite's estrogen receptor binding activity, in vitro and in silico information regarding parent compound binding activities, linking of metabolite structures and routes to parent compounds, and estimates of binding activity obtained from literature when possible. \n\nThis dataset is associated with the following publication:\nLeonard, J., C. Stevens, K. Mansouri, D. Chang, H. Pudukodu, S. Smith, and C. Tan. A Workflow for Identifying Metabolically Active Chemicals to Complement in vitro Toxicity Screening.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 6: 71-83, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1407568",
-            "keyword": [
-                "Metabolism",
-                "quantitative structure activity relationship (QSAR)",
-                "in vitro assays",
-                "bioactivity"
-            ],
             "contactPoint": {
                 "fn": "Yu-Mei Tan",
                 "hasEmail": "mailto:tan.cecilia@epa.gov"
             },
+            "description": "This data includes metabolite predictions for in vitro inactive chemicals, predictions of those metabolite's estrogen receptor binding activity, in vitro and in silico information regarding parent compound binding activities, linking of metabolite structures and routes to parent compounds, and estimates of binding activity obtained from literature when possible. \n\nThis dataset is associated with the following publication:\nLeonard, J., C. Stevens, K. Mansouri, D. Chang, H. Pudukodu, S. Smith, and C. Tan. A Workflow for Identifying Metabolically Active Chemicals to Complement in vitro Toxicity Screening.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 6: 71-83, (2018).",
             "distribution": [
                 {
-                    "title": "ScienceHub_Files.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407568/ScienceHub_Files.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "ScienceHub_Files.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407568",
+            "keyword": [
+                "Metabolism",
+                "quantitative structure activity relationship (QSAR)",
+                "in vitro assays",
+                "bioactivity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-25",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2017.10.003"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68819,19 +68813,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2017.10.003"
+            ],
+            "rights": null,
+            "title": "A Workflow for Identifying Metabolically Active Chemicals to Complement in vitro Toxicity Screening"
         },
         {
-            "title": "Predict_Organ_Toxicity_ChemResTox_Data",
-            "description": "We use a supervised machine learning strategy to systematically investigate the relative importance of study type, machine learning algorithm, and type of descriptor on predicting in vivo repeat-dose toxicity at the organ-level.   A total of 985 compounds were represented using chemical structural descriptors, ToxPrint chemotype descriptors, and bioactivity descriptors from ToxCast in vitro high-throughput screening assays.  Using ToxRefDB, a total of 35 target organ outcomes were identified that contained at least 100 chemicals (50 positive and 50 negative). Supervised machine learning was performed using Na&iuml;ve Bayes, k-nearest neighbor, random forest, classification and regression trees, and support vector classification approaches. Model performnce was assessed based on F1 scores using five-fold cross-validation with balanced bootstrap replicates.  Fixed effects modeling showed the variance in F1 scores was explained mostly by target organ outcome, followed by descriptor type, machine learning algorithm, and interactions between these three factors.  A combination of bioactivity and chemical structure or chemotype descriptors were the most predictive. Model performance improved with more chemicals (up to a maximum of 24%) and these gains were correlated (&rho;= 0.92) with the number of chemicals. \n\nThis dataset is associated with the following publication:\nLiu, J., G. Patlewicz, A. Williams, R. Thomas, and I. Shah. (Chemical Research in Toxicology) Predicting organ toxicity using in vitro bioactivity data and chemical structure.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 30: 2046\u22122059, (2017).",
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
+            "description": "We use a supervised machine learning strategy to systematically investigate the relative importance of study type, machine learning algorithm, and type of descriptor on predicting in vivo repeat-dose toxicity at the organ-level.   A total of 985 compounds were represented using chemical structural descriptors, ToxPrint chemotype descriptors, and bioactivity descriptors from ToxCast in vitro high-throughput screening assays.  Using ToxRefDB, a total of 35 target organ outcomes were identified that contained at least 100 chemicals (50 positive and 50 negative). Supervised machine learning was performed using Na&iuml;ve Bayes, k-nearest neighbor, random forest, classification and regression trees, and support vector classification approaches. Model performnce was assessed based on F1 scores using five-fold cross-validation with balanced bootstrap replicates.  Fixed effects modeling showed the variance in F1 scores was explained mostly by target organ outcome, followed by descriptor type, machine learning algorithm, and interactions between these three factors.  A combination of bioactivity and chemical structure or chemotype descriptors were the most predictive. Model performance improved with more chemicals (up to a maximum of 24%) and these gains were correlated (&rho;= 0.92) with the number of chemicals. \n\nThis dataset is associated with the following publication:\nLiu, J., G. Patlewicz, A. Williams, R. Thomas, and I. Shah. (Chemical Research in Toxicology) Predicting organ toxicity using in vitro bioactivity data and chemical structure.   CHEMICAL RESEARCH IN TOXICOLOGY. American Chemical Society, Washington, DC, USA, 30: 2046\u22122059, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/ShahImran/Predicting_Organ_Toxicity/",
+                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/ShahImran/Predicting_Organ_Toxicity/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407008",
             "keyword": [
@@ -68844,19 +68847,10 @@
                 "High throughput screening",
                 "high throughput toxicology"
             ],
-            "contactPoint": {
-                "fn": "Keith Houck",
-                "hasEmail": "mailto:houck.keith@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/ShahImran/Predicting_Organ_Toxicity/",
-                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/ShahImran/Predicting_Organ_Toxicity/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-28",
-            "references": [
-                "https://doi.org/10.1021/acs.chemrestox.7b00084"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68866,108 +68860,108 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.chemrestox.7b00084"
+            ],
+            "rights": null,
+            "title": "Predict_Organ_Toxicity_ChemResTox_Data"
         },
         {
-            "title": "Chlorine and DBP formation experimental data and kinetic modeling analysis to derive chlorine decay and DBP formation kinetic constants under different pipe flow conditions",
-            "description": "Experimental and modeling datasets and results. \n\nThis dataset is associated with the following publication:\nYang, J., Y. Zhao, Y. Shao, T. Speth, and T. Zhang. The Dependence of Chlorine Decay and DBP Formation Kinetics On Pipe Flow Properties in Drinking Water Distribution.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 141: 32-45, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1407631",
-            "keyword": [
-                "chlorine decay",
-                "THM formation",
-                "Pipe flow hydrodynamics",
-                "Drinking water distribution system",
-                "DBP formation",
-                "modeling"
-            ],
             "contactPoint": {
                 "fn": "Yingping Yang",
                 "hasEmail": "mailto:yang.jeff@epa.gov"
             },
+            "description": "Experimental and modeling datasets and results. \n\nThis dataset is associated with the following publication:\nYang, J., Y. Zhao, Y. Shao, T. Speth, and T. Zhang. The Dependence of Chlorine Decay and DBP Formation Kinetics On Pipe Flow Properties in Drinking Water Distribution.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 141: 32-45, (2018).",
             "distribution": [
                 {
-                    "title": "regression constant.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/regression%20constant.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "regression constant.xlsx"
                 },
                 {
-                    "title": "Loop4&5Results082207.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results082207.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results082207.xls"
                 },
                 {
-                    "title": "Loop4&5Results101707.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results101707.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results101707.xls"
                 },
                 {
-                    "title": "Loop4&5Results102307.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results102307.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results102307.xls"
                 },
                 {
-                    "title": "Loop4&5Results103007.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results103007.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results103007.xls"
                 },
                 {
-                    "title": "Loop4&5Results111407.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results111407.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results111407.xls"
                 },
                 {
-                    "title": "Loop4&5Results121107.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results121107.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results121107.xls"
                 },
                 {
-                    "title": "Loop4&5Results041107.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results041107.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results041107.xls"
                 },
                 {
-                    "title": "Loop4&5Results041807.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results041807.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results041807.xls"
                 },
                 {
-                    "title": "Loop4&5Results061907.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results061907.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results061907.xls"
                 },
                 {
-                    "title": "Loop4&5Results062607.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results062607.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results062607.xls"
                 },
                 {
-                    "title": "Loop4&5Results071007.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results071007.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results071007.xls"
                 },
                 {
-                    "title": "Loop4&5Results091107.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results091107.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results091107.xls"
                 },
                 {
-                    "title": "Loop4&5Results091807.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407631/Loop4%265Results091807.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Loop4&5Results091807.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407631",
+            "keyword": [
+                "chlorine decay",
+                "THM formation",
+                "Pipe flow hydrodynamics",
+                "Drinking water distribution system",
+                "DBP formation",
+                "modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-13",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2018.04.048"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -68977,42 +68971,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2018.04.048"
+            ],
+            "rights": null,
+            "title": "Chlorine and DBP formation experimental data and kinetic modeling analysis to derive chlorine decay and DBP formation kinetic constants under different pipe flow conditions"
         },
         {
-            "title": "Use of Targeted and Untargeted Effects-based Monitoring Tools to Assess Impacts of Wastewater Effluents on Fish in the South Platte River, CO",
-            "description": "Results of partial least squares (PLS) analysis of metabolite changes and contaminant concentrations to determine contaminants most likely to responsible for biological effects and to screen against those contaminants not responsible. \n\nThis dataset is associated with the following publication:\nEkman, D., K. Keteles, J. Beihoffer, J. Cavallin, K. Dahlin, J. Davis, A. Jastrow, J. Lazorchak, M. Mills, M. Murphy, D. Nguyen, A. Vajda, D. Villeneuve, D. Winkelman, and T. Collette. Evaluation of targeted and untargeted effects-based monitoring tools to assess impacts of contaminants of emerging concern on fish in the South Platte River, CO.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 239: 706-713, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1378558",
-            "keyword": [
-                "NMR",
-                "vitellogenin",
-                "fathead minnow",
-                "environmental estrogens",
-                "metabolomics"
-            ],
             "contactPoint": {
                 "fn": "Drew Ekman",
                 "hasEmail": "mailto:ekman.drew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378558/documents/Data%20Dictionary%20for%20Ekman%20et%20al._S.%20Platte_Input%20File.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Results of partial least squares (PLS) analysis of metabolite changes and contaminant concentrations to determine contaminants most likely to responsible for biological effects and to screen against those contaminants not responsible. \n\nThis dataset is associated with the following publication:\nEkman, D., K. Keteles, J. Beihoffer, J. Cavallin, K. Dahlin, J. Davis, A. Jastrow, J. Lazorchak, M. Mills, M. Murphy, D. Nguyen, A. Vajda, D. Villeneuve, D. Winkelman, and T. Collette. Evaluation of targeted and untargeted effects-based monitoring tools to assess impacts of contaminants of emerging concern on fish in the South Platte River, CO.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 239: 706-713, (2018).",
             "distribution": [
                 {
-                    "title": "Ekman et al._2018_Env. Pollut.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378558/Ekman%20et%20al._2018_Env.%20Pollut.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Ekman et al._2018_Env. Pollut.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378558",
+            "keyword": [
+                "NMR",
+                "vitellogenin",
+                "fathead minnow",
+                "environmental estrogens",
+                "metabolomics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2018.04.054"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69023,72 +69019,70 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1378558/documents/Data%20Dictionary%20for%20Ekman%20et%20al._S.%20Platte_Input%20File.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2018.04.054"
+            ],
+            "rights": null,
+            "title": "Use of Targeted and Untargeted Effects-based Monitoring Tools to Assess Impacts of Wastewater Effluents on Fish in the South Platte River, CO"
         },
         {
-            "title": "State and regional sensitivity spreadsheets for bar and pie charts",
-            "description": "These files represent the state and regional summaries of sensitivities to formaldehyde, acetaldehyde and ozone to various sources and compounds. \n\nThis dataset is associated with the following publication:\nLuecken, D., S. Napelenok, M. Strum, R. Scheffe, and S. Phillips. Sensitivity of Ambient Atmospheric Formaldehyde and Ozone to Precursor Species and Source Types Across the United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(8): 4668\u20134675, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1407657",
-            "keyword": [
-                "Formaldehyde",
-                "NATA",
-                "HAPs",
-                "Sensitivity"
-            ],
             "contactPoint": {
                 "fn": "Deborah Luecken",
                 "hasEmail": "mailto:luecken.deborah@epa.gov"
             },
+            "description": "These files represent the state and regional summaries of sensitivities to formaldehyde, acetaldehyde and ozone to various sources and compounds. \n\nThis dataset is associated with the following publication:\nLuecken, D., S. Napelenok, M. Strum, R. Scheffe, and S. Phillips. Sensitivity of Ambient Atmospheric Formaldehyde and Ozone to Precursor Species and Source Types Across the United States.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(8): 4668\u20134675, (2018).",
             "distribution": [
                 {
-                    "title": "FORM_sens_Jan_2017.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407657/FORM_sens_Jan_2017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FORM_sens_Jan_2017.xlsx"
                 },
                 {
-                    "title": "Form_sens_July_2017.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407657/Form_sens_July_2017.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Form_sens_July_2017.xls"
                 },
                 {
-                    "title": "Ozone_sens_Jan_2017.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407657/Ozone_sens_Jan_2017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Ozone_sens_Jan_2017.xlsx"
                 },
                 {
-                    "title": "Ozone_sens_July_2017.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407657/Ozone_sens_July_2017.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ozone_sens_July_2017.xls"
                 },
                 {
-                    "title": "ALD2_sens_Jan_2017.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407657/ALD2_sens_Jan_2017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ALD2_sens_Jan_2017.xlsx"
                 },
                 {
-                    "title": "ALD_sens_July_2017.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407657/ALD_sens_July_2017.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ALD_sens_July_2017.xls"
                 },
                 {
-                    "title": "emissions.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407657/emissions.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "emissions.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407657",
+            "keyword": [
+                "Formaldehyde",
+                "NATA",
+                "HAPs",
+                "Sensitivity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-07",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b05509"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69098,20 +69092,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b05509"
+            ],
+            "rights": null,
+            "title": "State and regional sensitivity spreadsheets for bar and pie charts"
         },
         {
-            "title": "Aircraft emission impacts on air quality",
-            "description": "Data sets include information on emissions of air pollutants, description of 3-D meteorological state of the atmosphere, and output from the CMAQ model over the northern hemisphere and contiguous U.S. This dataset is not publicly accessible because: This research was conducted a part of the primary author's Ph.D. dissertation at the University of North Carolina at Chapel Hill. All data sets were created on the UNC computers and are housed there. Since the data sets are not directly available to the EPA investigator, they are not included in ScienceHub. It can be accessed through the following means: Data sets can be accessed by contacting Dr. Sarav Arunachalam at UNC - sarav@email.unc.edu. Format: Model input (3D meteorological fields and 3D emission files) and output are in netcdf format. Observational data sets used are publicly available and typically available as ascii files. \n\nThis dataset is associated with the following publication:\nVennam, L., W. Vizuete, K. Talgo, M. Omary, F. Binkowski, J. Xing, R. Mathur, and S. Arunachalam. Modeled Full-Flight Aircraft Emissions Impacts on Air Quality and Their Sensitivity to Grid Resolution.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 122(24): 13,472\u201313,494, (2017).",
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
+                "fn": "Rohit Mathur",
+                "hasEmail": "mailto:mathur.rohit@epa.gov"
+            },
+            "description": "Data sets include information on emissions of air pollutants, description of 3-D meteorological state of the atmosphere, and output from the CMAQ model over the northern hemisphere and contiguous U.S. This dataset is not publicly accessible because: This research was conducted a part of the primary author's Ph.D. dissertation at the University of North Carolina at Chapel Hill. All data sets were created on the UNC computers and are housed there. Since the data sets are not directly available to the EPA investigator, they are not included in ScienceHub. It can be accessed through the following means: Data sets can be accessed by contacting Dr. Sarav Arunachalam at UNC - sarav@email.unc.edu. Format: Model input (3D meteorological fields and 3D emission files) and output are in netcdf format. Observational data sets used are publicly available and typically available as ascii files. \n\nThis dataset is associated with the following publication:\nVennam, L., W. Vizuete, K. Talgo, M. Omary, F. Binkowski, J. Xing, R. Mathur, and S. Arunachalam. Modeled Full-Flight Aircraft Emissions Impacts on Air Quality and Their Sensitivity to Grid Resolution.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 122(24): 13,472\u201313,494, (2017).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1407531",
             "keyword": [
                 "Aircraft emissions",
@@ -69119,14 +69117,10 @@
                 "air pollution",
                 "modeling"
             ],
-            "contactPoint": {
-                "fn": "Rohit Mathur",
-                "hasEmail": "mailto:mathur.rohit@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-28",
-            "references": [
-                "https://doi.org/10.1002/2017jd026598"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69136,20 +69130,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2017jd026598"
+            ],
+            "rights": null,
+            "title": "Aircraft emission impacts on air quality"
         },
         {
-            "title": "WRF and CMAQ Model Output",
-            "description": "WRF and CMAQ model output for July 2011. This dataset is not publicly accessible because: The files are too large. It can be accessed through the following means: The data can be accessed through NCC's tape archival storage system (ASM). Format: WRF and CMAQ model output for July 2011. \n\nThis dataset is associated with the following publication:\nForoutan, H., and J. Pleim. Improving the simulation of convective dust storms in regional-to-global models.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 9(5): 2046\u20132060, (2017).",
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
+                "fn": "Hosein Foroutan",
+                "hasEmail": "mailto:foroutan.hosein@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407597/documents/ForoutanHosein_A-15dz_Data_Dictionary_20170808.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "WRF and CMAQ model output for July 2011. This dataset is not publicly accessible because: The files are too large. It can be accessed through the following means: The data can be accessed through NCC's tape archival storage system (ASM). Format: WRF and CMAQ model output for July 2011. \n\nThis dataset is associated with the following publication:\nForoutan, H., and J. Pleim. Improving the simulation of convective dust storms in regional-to-global models.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 9(5): 2046\u20132060, (2017).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1407597",
             "keyword": [
                 "Dust",
@@ -69158,14 +69158,10 @@
                 "lightning assimilation",
                 "CMAQ"
             ],
-            "contactPoint": {
-                "fn": "Hosein Foroutan",
-                "hasEmail": "mailto:foroutan.hosein@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-03-01",
-            "references": [
-                "https://doi.org/10.1002/2017ms000953"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69176,98 +69172,96 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407597/documents/ForoutanHosein_A-15dz_Data_Dictionary_20170808.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1002/2017ms000953"
+            ],
+            "rights": null,
+            "title": "WRF and CMAQ Model Output"
         },
         {
-            "title": "LCA of fuels and stoves in India, China, Ghana, and Kenya",
-            "description": "This provides 4 results workbooks and 7 workbooks documenting the inventory. \n\nThis dataset is associated with the following publications:\nMorelli, B., S. Cashman, and M. Rodgers. Life Cycle Assessment of Cookstoves and Fuels in India, China, Kenya, and Ghana. U.S. Environmental Protection Agency, Washington, DC, USA, 2017.\nCashman, S. Life-Cycle Assessment of Cookstove Fuels in India and China. U.S. Environmental Protection Agency, Washington, DC, USA, 2016.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1407614",
-            "keyword": [
-                "Life cycle assessment (LCA)",
-                "openLCA",
-                "cookstoves",
-                "indoor air quality",
-                "energy ladder"
-            ],
             "contactPoint": {
                 "fn": "Susan Thorneloe-Howard",
                 "hasEmail": "mailto:thorneloe.susan@epa.gov"
             },
+            "description": "This provides 4 results workbooks and 7 workbooks documenting the inventory. \n\nThis dataset is associated with the following publications:\nMorelli, B., S. Cashman, and M. Rodgers. Life Cycle Assessment of Cookstoves and Fuels in India, China, Kenya, and Ghana. U.S. Environmental Protection Agency, Washington, DC, USA, 2017.\nCashman, S. Life-Cycle Assessment of Cookstove Fuels in India and China. U.S. Environmental Protection Agency, Washington, DC, USA, 2016.",
             "distribution": [
                 {
-                    "title": "archive.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/archive.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "archive.zip"
                 },
                 {
-                    "title": "EPA Phase II Cookstove LCA Results - KE.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/EPA%20Phase%20II%20Cookstove%20LCA%20Results%20-%20KE.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA Phase II Cookstove LCA Results - KE.xlsx"
                 },
                 {
-                    "title": "EPA Phase II Cookstove LCA Results - IN.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/EPA%20Phase%20II%20Cookstove%20LCA%20Results%20-%20IN.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA Phase II Cookstove LCA Results - IN.xlsx"
                 },
                 {
-                    "title": "EPA Phase II Cookstove LCA Results - CN.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/EPA%20Phase%20II%20Cookstove%20LCA%20Results%20-%20CN.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA Phase II Cookstove LCA Results - CN.xlsx"
                 },
                 {
-                    "title": "EPA Phase II Cookstove LCA Results - GH.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/EPA%20Phase%20II%20Cookstove%20LCA%20Results%20-%20GH.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA Phase II Cookstove LCA Results - GH.xlsx"
                 },
                 {
-                    "title": "SI6. Charcoal Kiln Supplementary Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/SI6.%20Charcoal%20Kiln%20Supplementary%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI6. Charcoal Kiln Supplementary Information.xlsx"
                 },
                 {
-                    "title": "SI3. Fuel Mix Scenario Supplementary Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/SI3.%20Fuel%20Mix%20Scenario%20Supplementary%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI3. Fuel Mix Scenario Supplementary Information.xlsx"
                 },
                 {
-                    "title": "SI4. Cookstove Electricity Scenario Supplementary Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/SI4.%20Cookstove%20Electricity%20Scenario%20Supplementary%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI4. Cookstove Electricity Scenario Supplementary Information.xlsx"
                 },
                 {
-                    "title": "SI2. Stove LCI Supplementary Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/SI2.%20Stove%20LCI%20Supplementary%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI2. Stove LCI Supplementary Information.xlsx"
                 },
                 {
-                    "title": "SI7. Biogas Modeling Supplementary Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/SI7.%20Biogas%20Modeling%20Supplementary%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI7. Biogas Modeling Supplementary Information.xlsx"
                 },
                 {
-                    "title": "SI1. Stove Use and Emissions Supplementary Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/SI1.%20Stove%20Use%20and%20Emissions%20Supplementary%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI1. Stove Use and Emissions Supplementary Information.xlsx"
                 },
                 {
-                    "title": "SI5. Crop Residue Supplementary Information.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407614/SI5.%20Crop%20Residue%20Supplementary%20Information.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI5. Crop Residue Supplementary Information.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407614",
+            "keyword": [
+                "Life cycle assessment (LCA)",
+                "openLCA",
+                "cookstoves",
+                "indoor air quality",
+                "energy ladder"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-14",
-            "references": [
-                "https://nepis.epa.gov/Exe/ZyPDF.cgi/P100T7UD.PDF?Dockey=P100T7UD.PDF"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69277,19 +69271,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://nepis.epa.gov/Exe/ZyPDF.cgi/P100T7UD.PDF?Dockey=P100T7UD.PDF"
+            ],
+            "rights": null,
+            "title": "LCA of fuels and stoves in India, China, Ghana, and Kenya"
         },
         {
-            "title": "StreamCat",
-            "description": "The StreamCat Dataset provides summaries of natural and anthropogenic landscape features for ~2.65 million streams, and their associated catchments, within the conterminous USA. \n\nThis dataset is associated with the following publications:\nHill, R.A., M. Weber , S. Leibowitz , T. Olsen , and D.J. Thornbrugh. The Stream-Catchment (StreamCat) Dataset: A database of watershed metrics for the conterminous USA.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA,  9, (2015).\nHill, R., E. Fox, S. Leibowitz, T. Olsen, D. Thornbrugh, and M. Weber. Predictive Mapping of the Biotic Condition of Conterminous-USA Rivers and Streams.   ECOLOGICAL APPLICATIONS. Ecological Society of America, Ithaca, NY, USA, 27(8): 2397-2415, (2017).\nFox, E., R. Hill, S. Leibowitz, T. Olsen, D. Thornbrugh, and M. Weber. Assessing the accuracy and stability of variable selection methods for random forest modeling in ecology.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 189(316): 1-20, (2017).\nThornbrugh, D., S. Leibowitz, R. Hill, M. Weber, Z. Johnson, T. Olsen, J. Flotemersch, J. Stoddard, and D. Peck. Mapping watershed integrity for the conterminous United States...   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 85: 1133-1148, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Scott Leibowitz",
+                "hasEmail": "mailto:leibowitz.scott@epa.gov"
+            },
+            "describedBy": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/Documentation/DataDictionary.html",
+            "description": "The StreamCat Dataset provides summaries of natural and anthropogenic landscape features for ~2.65 million streams, and their associated catchments, within the conterminous USA. \n\nThis dataset is associated with the following publications:\nHill, R.A., M. Weber , S. Leibowitz , T. Olsen , and D.J. Thornbrugh. The Stream-Catchment (StreamCat) Dataset: A database of watershed metrics for the conterminous USA.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA,  9, (2015).\nHill, R., E. Fox, S. Leibowitz, T. Olsen, D. Thornbrugh, and M. Weber. Predictive Mapping of the Biotic Condition of Conterminous-USA Rivers and Streams.   ECOLOGICAL APPLICATIONS. Ecological Society of America, Ithaca, NY, USA, 27(8): 2397-2415, (2017).\nFox, E., R. Hill, S. Leibowitz, T. Olsen, D. Thornbrugh, and M. Weber. Assessing the accuracy and stability of variable selection methods for random forest modeling in ecology.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 189(316): 1-20, (2017).\nThornbrugh, D., S. Leibowitz, R. Hill, M. Weber, Z. Johnson, T. Olsen, J. Flotemersch, J. Stoddard, and D. Peck. Mapping watershed integrity for the conterminous United States...   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 85: 1133-1148, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407613",
             "keyword": [
@@ -69303,22 +69307,10 @@
                 "aquatic condition",
                 "National Aquatic Resource Surveys"
             ],
-            "contactPoint": {
-                "fn": "Scott Leibowitz",
-                "hasEmail": "mailto:leibowitz.scott@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-11",
-            "references": [
-                "https://doi.org/10.1111/1752-1688.12372",
-                "https://doi.org/10.1002/eap.1617",
-                "https://doi.org/10.1007/s10661-017-6025-0",
-                "https://doi.org/10.1016/j.ecolind.2017.10.070"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69329,38 +69321,40 @@
                     }
                 }
             },
-            "describedBy": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/Documentation/DataDictionary.html"
+            "references": [
+                "https://doi.org/10.1111/1752-1688.12372",
+                "https://doi.org/10.1002/eap.1617",
+                "https://doi.org/10.1007/s10661-017-6025-0",
+                "https://doi.org/10.1016/j.ecolind.2017.10.070"
+            ],
+            "rights": null,
+            "title": "StreamCat"
         },
         {
-            "title": "LaneCharles_A-dv4f_Data_20180430.xls",
-            "description": "Data associated with the paper, \"Comparing pixel- and object-based approaches in effectively classifying wetland-dominated landscapes\". \n\nThis dataset is associated with the following publication:\nBerhane, T., C. Lane, Q. Wu, O. Anenkhonov, V. Chepinoga, B. Autrey, and H. Liu. Comparing Pixel- and Object-Based Approaches in Effectively Classifying Wetland-Dominated Landscapes.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 10(1): 46, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1500025",
-            "keyword": [
-                "wetlands"
-            ],
             "contactPoint": {
                 "fn": "Charles Lane",
                 "hasEmail": "mailto:lane.charles@epa.gov"
             },
+            "description": "Data associated with the paper, \"Comparing pixel- and object-based approaches in effectively classifying wetland-dominated landscapes\". \n\nThis dataset is associated with the following publication:\nBerhane, T., C. Lane, Q. Wu, O. Anenkhonov, V. Chepinoga, B. Autrey, and H. Liu. Comparing Pixel- and Object-Based Approaches in Effectively Classifying Wetland-Dominated Landscapes.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 10(1): 46, (2018).",
             "distribution": [
                 {
-                    "title": "LaneCharles_A-dv4f_Data_20180430.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500025/LaneCharles_A-dv4f_Data_20180430.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LaneCharles_A-dv4f_Data_20180430.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500025",
+            "keyword": [
+                "wetlands"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-08",
-            "references": [
-                "https://doi.org/10.3390/rs10010046"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69370,38 +69364,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/rs10010046"
+            ],
+            "rights": null,
+            "title": "LaneCharles_A-dv4f_Data_20180430.xls"
         },
         {
-            "title": "LaneCharles_A-zpd2_Data_30042018.xlsx",
-            "description": "Data associated with the paper, \"Decision-Tree, Rule-Based, and Random Forest Classification of High-Resolution Multispectral Imagery for Wetland Mapping and Inventory\". \n\nThis dataset is associated with the following publication:\nBerhane, T., C. Lane, Q. Wu, B. Autrey, O. Anenkhonov, V. Chepinoga, and H. Liu. Decision-Tree, Rule-Based, and Random Forest Classification of High-Resolution Multispectral Imagery for Wetland Mapping and Inventory.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 10(4): 580, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500026",
-            "keyword": [
-                "wetland"
-            ],
             "contactPoint": {
                 "fn": "Charles Lane",
                 "hasEmail": "mailto:lane.charles@epa.gov"
             },
+            "description": "Data associated with the paper, \"Decision-Tree, Rule-Based, and Random Forest Classification of High-Resolution Multispectral Imagery for Wetland Mapping and Inventory\". \n\nThis dataset is associated with the following publication:\nBerhane, T., C. Lane, Q. Wu, B. Autrey, O. Anenkhonov, V. Chepinoga, and H. Liu. Decision-Tree, Rule-Based, and Random Forest Classification of High-Resolution Multispectral Imagery for Wetland Mapping and Inventory.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 10(4): 580, (2018).",
             "distribution": [
                 {
-                    "title": "LaneCharles_A-zpd2_Data_30042018.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500026/LaneCharles_A-zpd2_Data_30042018.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LaneCharles_A-zpd2_Data_30042018.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500026",
+            "keyword": [
+                "wetland"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-08",
-            "references": [
-                "https://doi.org/10.3390/rs10040580"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69411,19 +69405,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/rs10040580"
+            ],
+            "rights": null,
+            "title": "LaneCharles_A-zpd2_Data_30042018.xlsx"
         },
         {
-            "title": "Las Vegas Near Road Data - PM2.5 and Black Carbon",
-            "description": "Las Vegas Near Road Data PM2.5 and Black Carbon Data. \n\nThis dataset is associated with the following publication:\nKimbrough, S., T. Hanley, G. Hagler, R. Baldauf, M. Snyder, and H. Brantley. Influential factors affecting black carbon trends at four sites of differing distance from a major highway in Las Vegas.   Air Quality, Atmosphere & Health. Springer Netherlands,   NETHERLANDS, 11(2): 181-196, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Evelyn Kimbrough",
+                "hasEmail": "mailto:kimbrough.sue@epa.gov"
+            },
+            "description": "Las Vegas Near Road Data PM2.5 and Black Carbon Data. \n\nThis dataset is associated with the following publication:\nKimbrough, S., T. Hanley, G. Hagler, R. Baldauf, M. Snyder, and H. Brantley. Influential factors affecting black carbon trends at four sites of differing distance from a major highway in Las Vegas.   Air Quality, Atmosphere & Health. Springer Netherlands,   NETHERLANDS, 11(2): 181-196, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1373706/PM%20and%20BC%20data.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "PM and BC data.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1373706",
             "keyword": [
@@ -69434,20 +69438,10 @@
                 "air quality",
                 "air pollution"
             ],
-            "contactPoint": {
-                "fn": "Evelyn Kimbrough",
-                "hasEmail": "mailto:kimbrough.sue@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "PM and BC data.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1373706/PM%20and%20BC%20data.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-25",
-            "references": [
-                "https://doi.org/10.1007/s11869-017-0519-3"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69457,46 +69451,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11869-017-0519-3"
+            ],
+            "rights": null,
+            "title": "Las Vegas Near Road Data - PM2.5 and Black Carbon"
         },
         {
-            "title": "Space-time paired simulation-observation records",
-            "description": "Files uploaded to ScienceHub pair the model results in space and time to observations of NCAR NOy, NO, NO2 and O3, UC Berkeley NO2, peroxy nitrates, alkyl nitrates, and nitric acid, made aboard the NASA P3B aircraft during the DISCOVER-AQ, Maryland, 2011. Data are paired as follows: Model predictions are paired with aircraft measurements in space where aircraft latitude, longitude, altitude were matched to nearest grid cell center and model layer center height.  Fifteen second averages of measurements were matched to modeled estimates in time to the nearest hour.\r\n\r\nObservational data is also archived at the NASA LaRC Atmospheric Sciences Data Center (https://www-air.larc.nasa.gov/data.htm). \n\nThis dataset is associated with the following publication:\nSimon, H., K. Baker, L. Valin, J. Crawford, S. Puesede, J. Kelly, K. Foley, R. Cohen, B. Timin, A. Weinheimer, N. Possiel, C. Owen, C. Misenis, G. Diskin, A. Fried, and B. Henderson. Characterizing CO and NOy Sources and Relative Ambient Ratios in the Baltimore Area Using Ambient Measurements and Source Attribution Modeling.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 123(6): 3304-3320, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1407577",
-            "keyword": [
-                "Ozone",
-                "air quality",
-                "NOx emissions",
-                "CO emissions",
-                "Air Quality Model"
-            ],
             "contactPoint": {
                 "fn": "Lukas Valin",
                 "hasEmail": "mailto:valin.lukas@epa.gov"
             },
+            "description": "Files uploaded to ScienceHub pair the model results in space and time to observations of NCAR NOy, NO, NO2 and O3, UC Berkeley NO2, peroxy nitrates, alkyl nitrates, and nitric acid, made aboard the NASA P3B aircraft during the DISCOVER-AQ, Maryland, 2011. Data are paired as follows: Model predictions are paired with aircraft measurements in space where aircraft latitude, longitude, altitude were matched to nearest grid cell center and model layer center height.  Fifteen second averages of measurements were matched to modeled estimates in time to the nearest hour.\r\n\r\nObservational data is also archived at the NASA LaRC Atmospheric Sciences Data Center (https://www-air.larc.nasa.gov/data.htm). \n\nThis dataset is associated with the following publication:\nSimon, H., K. Baker, L. Valin, J. Crawford, S. Puesede, J. Kelly, K. Foley, R. Cohen, B. Timin, A. Weinheimer, N. Possiel, C. Owen, C. Misenis, G. Diskin, A. Fried, and B. Henderson. Characterizing CO and NOy Sources and Relative Ambient Ratios in the Baltimore Area Using Ambient Measurements and Source Attribution Modeling.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 123(6): 3304-3320, (2018).",
             "distribution": [
                 {
-                    "title": "paired-DISCOVER-AQ_CMAQ-ISAM_datafiles.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407577/paired-DISCOVER-AQ_CMAQ-ISAM_datafiles.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "paired-DISCOVER-AQ_CMAQ-ISAM_datafiles.zip"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/missions/discover-aq/dataaccess.htm",
-                    "accessURL": "https://www-air.larc.nasa.gov/missions/discover-aq/dataaccess.htm"
+                    "accessURL": "https://www-air.larc.nasa.gov/missions/discover-aq/dataaccess.htm",
+                    "title": "https://www-air.larc.nasa.gov/missions/discover-aq/dataaccess.htm"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407577",
+            "keyword": [
+                "Ozone",
+                "air quality",
+                "NOx emissions",
+                "CO emissions",
+                "Air Quality Model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-06",
-            "references": [
-                "https://doi.org/10.1002/2017jd027688"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69506,40 +69500,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2017jd027688"
+            ],
+            "rights": null,
+            "title": "Space-time paired simulation-observation records"
         },
         {
-            "title": "Census and Facility Emissions Dataset",
-            "description": "Data Sources, including links; \nData Dictionary; \n2009-2013 American Community Survey, Block group-level Population Data; \n2010 Decennial Census, Block group-level Population Data; \n2008 National Emissions Inventory, Facility-level Data; \n2011 National Emissions Inventory, Facility-level Data; \n2014 National Emissions Inventory, Facility-level Data; \n2010 Rural-Urban Commuting Area Codes, Tract-level Data;\n2011 PM 2.5 Daily Average Fused Air Quality Surface Using Downscaling (FAQSD) Output, mean Tract-level Data, CONUS. \n\nThis dataset is associated with the following publication:\nMikati, I., A. Benson, T. Luben, J. Sacks, and J. Richmond-Bryant. Disparities in Distribution of Particulate Matter Emission Sources by Race and Poverty Status.   American Journal of Public Health. American Public Health Association, Washington, DC, USA, 108(4): 480-485, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "https://doi.org/10.23719/1407543",
-            "keyword": [
-                "particulate matter",
-                "national emissions inventory",
-                "american community survey"
-            ],
             "contactPoint": {
                 "fn": "Ihab Mikati",
                 "hasEmail": "mailto:mikati.ihab@epa.gov"
             },
+            "description": "Data Sources, including links; \nData Dictionary; \n2009-2013 American Community Survey, Block group-level Population Data; \n2010 Decennial Census, Block group-level Population Data; \n2008 National Emissions Inventory, Facility-level Data; \n2011 National Emissions Inventory, Facility-level Data; \n2014 National Emissions Inventory, Facility-level Data; \n2010 Rural-Urban Commuting Area Codes, Tract-level Data;\n2011 PM 2.5 Daily Average Fused Air Quality Surface Using Downscaling (FAQSD) Output, mean Tract-level Data, CONUS. \n\nThis dataset is associated with the following publication:\nMikati, I., A. Benson, T. Luben, J. Sacks, and J. Richmond-Bryant. Disparities in Distribution of Particulate Matter Emission Sources by Race and Poverty Status.   American Journal of Public Health. American Public Health Association, Washington, DC, USA, 108(4): 480-485, (2018).",
             "distribution": [
                 {
-                    "title": "Mikati_A-hdrp_census-facility-emissions-dataset-20170509.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407543/Mikati_A-hdrp_census-facility-emissions-dataset-20170509.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mikati_A-hdrp_census-facility-emissions-dataset-20170509.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407543",
+            "keyword": [
+                "particulate matter",
+                "national emissions inventory",
+                "american community survey"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-09",
-            "references": [
-                "https://doi.org/10.2105/ajph.2017.304297"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69549,43 +69543,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2105/ajph.2017.304297"
+            ],
+            "rights": null,
+            "title": "Census and Facility Emissions Dataset"
         },
         {
-            "title": "LVdata 05182016 on-road estimates",
-            "description": "Meteorological and concentration data at the Las Vegas I-15 monitoring site. \n\nThis dataset is associated with the following publications:\nRichmond-Bryant, J., M. Snyder, C. Owen, and S. Kimbrough. Factors associated with NO2 and NOx concentration gradients near a highway.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA,  214-226, (2017).\nRichmond-Bryant , J., C. Owen , S. Graham , M. Snyder, S. McDow , M. Oakes, and S. Kimbrough. Estimation of on-road NO2 concentrations, NO2/NOx ratios, and related roadway gradients from near-road monitoring data.   Air Quality, Atmosphere & Health. Springer Netherlands,   NETHERLANDS,  611-625, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1407612",
-            "keyword": [
-                "near road",
-                "oxides of nitrogen",
-                "nitrogen dioxide",
-                "NO2",
-                "NOx"
-            ],
             "contactPoint": {
                 "fn": "Evelyn Kimbrough",
                 "hasEmail": "mailto:kimbrough.sue@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407612/documents/dictionary%2005212018%20v2.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Meteorological and concentration data at the Las Vegas I-15 monitoring site. \n\nThis dataset is associated with the following publications:\nRichmond-Bryant, J., M. Snyder, C. Owen, and S. Kimbrough. Factors associated with NO2 and NOx concentration gradients near a highway.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA,  214-226, (2017).\nRichmond-Bryant , J., C. Owen , S. Graham , M. Snyder, S. McDow , M. Oakes, and S. Kimbrough. Estimation of on-road NO2 concentrations, NO2/NOx ratios, and related roadway gradients from near-road monitoring data.   Air Quality, Atmosphere & Health. Springer Netherlands,   NETHERLANDS,  611-625, (2017).",
             "distribution": [
                 {
-                    "title": "LVdata 05182016 on-road estimates REVISED Q3 only.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407612/LVdata%2005182016%20on-road%20estimates%20REVISED%20Q3%20only.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "LVdata 05182016 on-road estimates REVISED Q3 only.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407612",
+            "keyword": [
+                "near road",
+                "oxides of nitrogen",
+                "nitrogen dioxide",
+                "NO2",
+                "NOx"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-18",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.11.026",
-                "https://doi.org/10.1007/s11869-016-0455-7"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69596,20 +69591,29 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1407612/documents/dictionary%2005212018%20v2.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2017.11.026",
+                "https://doi.org/10.1007/s11869-016-0455-7"
+            ],
+            "rights": null,
+            "title": "LVdata 05182016 on-road estimates"
         },
         {
-            "title": "Acrolein Inhalation Alters Myocardial Synchrony and Performance at and Below Exposure Concentration that Cause Ventilatory Responses in Mice",
-            "description": "we examined the cardiovascular effects acrolein inhalation, particularly on myocardial synchrony and performance via ultrasound echocardiography. Male C57Bl/6J mice (n=6/group) were exposed to filtered air (FA), 0.3 ppm acrolein, or 3.0 ppm acrolein for 3 hours in whole body plethysmography chambers. Cardiac strain data, heart function, and transmitral blood flow were investigated with echocardiography (40 MHz) 1 day prior to exposure, 1 hour after exposure, and 1 day after exposure. During the first 30 minutes of exposure, breathing frequency decreased. tidal volume increased, and expiratory/inspiratory time ratio increased in response to 3.0 ppm acrolein. Elapsed time between peak strain in adjacent wall segments (i.e. myocardial strain delay), a measure of myocardial dyssynchrony, increased significantly in mice exposed to 3.0 ppm acrolein at 1 and 24 hours post-exposure. Mice exposed to 0.3 ppm acrolein did not demonstrate changes in myocardial synchrony but did show decreases in myocardial performance, i.e. increased Tei index, at both 1 and 24 hours post-exposure. \n\nThis dataset is associated with the following publication:\nThompson, L., A. Ledbetter , N. Coates , W. Cascio , M. Hazari , and A. Farraj. Acrolein inhalation alters myocardial synchrony and performance at and below exposure concentrations that cause ventilatory responses.   Cardiovascular Toxicology. Humana Press Incorporated, Totowa, NJ, USA, 17(2): 97-108, (2017).",
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
+            "description": "we examined the cardiovascular effects acrolein inhalation, particularly on myocardial synchrony and performance via ultrasound echocardiography. Male C57Bl/6J mice (n=6/group) were exposed to filtered air (FA), 0.3 ppm acrolein, or 3.0 ppm acrolein for 3 hours in whole body plethysmography chambers. Cardiac strain data, heart function, and transmitral blood flow were investigated with echocardiography (40 MHz) 1 day prior to exposure, 1 hour after exposure, and 1 day after exposure. During the first 30 minutes of exposure, breathing frequency decreased. tidal volume increased, and expiratory/inspiratory time ratio increased in response to 3.0 ppm acrolein. Elapsed time between peak strain in adjacent wall segments (i.e. myocardial strain delay), a measure of myocardial dyssynchrony, increased significantly in mice exposed to 3.0 ppm acrolein at 1 and 24 hours post-exposure. Mice exposed to 0.3 ppm acrolein did not demonstrate changes in myocardial synchrony but did show decreases in myocardial performance, i.e. increased Tei index, at both 1 and 24 hours post-exposure. \n\nThis dataset is associated with the following publication:\nThompson, L., A. Ledbetter , N. Coates , W. Cascio , M. Hazari , and A. Farraj. Acrolein inhalation alters myocardial synchrony and performance at and below exposure concentrations that cause ventilatory responses.   Cardiovascular Toxicology. Humana Press Incorporated, Totowa, NJ, USA, 17(2): 97-108, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1427298/LT1%20Thompson%20et%20al%20Acrolein%20Study_Science%20Hub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LT1 Thompson et al Acrolein Study_Science Hub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1427298",
             "keyword": [
@@ -69622,20 +69626,10 @@
                 "myocardial dyssynchrony",
                 "echocardiography"
             ],
-            "contactPoint": {
-                "fn": "Leslie Thompson",
-                "hasEmail": "mailto:thompson.leslie@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "LT1 Thompson et al Acrolein Study_Science Hub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1427298/LT1%20Thompson%20et%20al%20Acrolein%20Study_Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-20",
-            "references": [
-                "https://doi.org/10.1007/s12012-016-9360-4"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69645,39 +69639,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12012-016-9360-4"
+            ],
+            "rights": null,
+            "title": "Acrolein Inhalation Alters Myocardial Synchrony and Performance at and Below Exposure Concentration that Cause Ventilatory Responses in Mice"
         },
         {
-            "title": "Hong and Purucker sensitivity analysis code and data",
-            "description": "Code and data associated with Hong T, Purucker ST, 2018. Spatiotemporal sensitivity analysis of vertical transport of pesticides in soil, Environmental Modelling and Software, 105: 24-38, https://doi.org/10.1016/j.envsoft.2018.03.018. \n\nThis dataset is associated with the following publication:\nHong, T., and T. Purucker. Spatiotemporal sensitivity analysis of vertical transport of pesticides in soil.   ENVIRONMENTAL MODELLING & SOFTWARE. Elsevier Science, New York, NY,   105: 24-38, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1435024",
-            "keyword": [
-                "Pesticide Root Zone Model (PRZM)",
-                "Sobol' sensitivity analysis",
-                "global sensitivity analysis"
-            ],
             "contactPoint": {
                 "fn": "Steven Purucker",
                 "hasEmail": "mailto:purucker.tom@epa.gov"
             },
+            "description": "Code and data associated with Hong T, Purucker ST, 2018. Spatiotemporal sensitivity analysis of vertical transport of pesticides in soil, Environmental Modelling and Software, 105: 24-38, https://doi.org/10.1016/j.envsoft.2018.03.018. \n\nThis dataset is associated with the following publication:\nHong, T., and T. Purucker. Spatiotemporal sensitivity analysis of vertical transport of pesticides in soil.   ENVIRONMENTAL MODELLING & SOFTWARE. Elsevier Science, New York, NY,   105: 24-38, (2018).",
             "distribution": [
                 {
-                    "title": "https://github.com/puruckertom/hongpurucker_przm_sobol",
-                    "accessURL": "https://github.com/puruckertom/hongpurucker_przm_sobol"
+                    "accessURL": "https://github.com/puruckertom/hongpurucker_przm_sobol",
+                    "title": "https://github.com/puruckertom/hongpurucker_przm_sobol"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435024",
+            "keyword": [
+                "Pesticide Root Zone Model (PRZM)",
+                "Sobol' sensitivity analysis",
+                "global sensitivity analysis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-14",
-            "references": [
-                "https://doi.org/10.1016/j.envsoft.2018.03.018"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69687,19 +69681,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envsoft.2018.03.018"
+            ],
+            "rights": null,
+            "title": "Hong and Purucker sensitivity analysis code and data"
         },
         {
-            "title": "Supporting data for \"Conway, G., Robertson, D., Chadwell, C., McDonald, J. et al. 2018 Evaluation of Emerging Technologies on a 1.6 L Turbocharged GDI Engine. SAE 2018-01-1423\" V1",
-            "description": "Low-pressure loop exhaust gas recirculation (LP- EGR) combined with higher compression ratio, is a technology package that has been a focus of research to increase engine thermal efficiency of downsized, turbocharged gasoline direct injection (GDI) engines. Research shows that the addition of LP-EGR reduces the propensity to knock that is experienced at higher compression ratios. To investigate the interaction and compatibility between increased compression ratio and LP-EGR, a 1.6 L Turbocharged GDI engine was modified to run with LP-EGR at a higher compression ratio (12:1 versus 10.5:1) via a piston change. This work includes the results of baseline testing on an engine run with a prototype controller and initially tuned to mimic an original equipment manufacturer (OEM) baseline control strategy running on premium fuel (92.8 anti-knock index). This paper then presents test results after first adding LP-EGR to the baseline engine, and then also increasing the compression ratio (CR) using 12:1 pistons. As a last step, the 10.5 CR engine with LP-EGR was run on regular fuel (87.7 anti-knock index) to verify that this configuration could be calibrated to maintain performance like the baseline engine running on premium fuel. To understand the effect of each technology and operating strategy combination on vehicle fuel economy, the various engine maps were compared in EPA\u2019s Advanced Light-Duty Powertrain and Hybrid Analysis (ALPHA) tool over U.S. regulatory drive cycles. This work was done as part of the EPA's continuing assessment of advanced light-duty automotive technologies to support a Midterm Evaluation of Light-duty Vehicle GHG Standards. \n\nThis dataset is associated with the following publication:\nMcDonald, J., M. Stuhldreher, D. Barba, J. Kargul, G. Conway, D. Robertson, and C. Chadwell. Evaluation of Emerging Technologies on a 1.6 L Turbocharged GDI Engine.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  15, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Joseph McDonald",
+                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
+            },
+            "description": "Low-pressure loop exhaust gas recirculation (LP- EGR) combined with higher compression ratio, is a technology package that has been a focus of research to increase engine thermal efficiency of downsized, turbocharged gasoline direct injection (GDI) engines. Research shows that the addition of LP-EGR reduces the propensity to knock that is experienced at higher compression ratios. To investigate the interaction and compatibility between increased compression ratio and LP-EGR, a 1.6 L Turbocharged GDI engine was modified to run with LP-EGR at a higher compression ratio (12:1 versus 10.5:1) via a piston change. This work includes the results of baseline testing on an engine run with a prototype controller and initially tuned to mimic an original equipment manufacturer (OEM) baseline control strategy running on premium fuel (92.8 anti-knock index). This paper then presents test results after first adding LP-EGR to the baseline engine, and then also increasing the compression ratio (CR) using 12:1 pistons. As a last step, the 10.5 CR engine with LP-EGR was run on regular fuel (87.7 anti-knock index) to verify that this configuration could be calibrated to maintain performance like the baseline engine running on premium fuel. To understand the effect of each technology and operating strategy combination on vehicle fuel economy, the various engine maps were compared in EPA\u2019s Advanced Light-Duty Powertrain and Hybrid Analysis (ALPHA) tool over U.S. regulatory drive cycles. This work was done as part of the EPA's continuing assessment of advanced light-duty automotive technologies to support a Midterm Evaluation of Light-duty Vehicle GHG Standards. \n\nThis dataset is associated with the following publication:\nMcDonald, J., M. Stuhldreher, D. Barba, J. Kargul, G. Conway, D. Robertson, and C. Chadwell. Evaluation of Emerging Technologies on a 1.6 L Turbocharged GDI Engine.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  15, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435450/SAE%202018-01-1423%20Evaluation%20of%20Emerging%20Tech.%20on%20a%201.6%20L%20TGDI%20Engine.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "SAE 2018-01-1423 Evaluation of Emerging Tech. on a 1.6 L TGDI Engine.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1435450",
             "keyword": [
@@ -69711,20 +69715,10 @@
                 "Hybrid Electric Vehicles",
                 "Electric Vehicles"
             ],
-            "contactPoint": {
-                "fn": "Joseph McDonald",
-                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SAE 2018-01-1423 Evaluation of Emerging Tech. on a 1.6 L TGDI Engine.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435450/SAE%202018-01-1423%20Evaluation%20of%20Emerging%20Tech.%20on%20a%201.6%20L%20TGDI%20Engine.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": [
-                "https://doi.org/10.4271/2018-01-1423"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69734,54 +69728,54 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.4271/2018-01-1423"
+            ],
+            "rights": null,
+            "title": "Supporting data for \"Conway, G., Robertson, D., Chadwell, C., McDonald, J. et al. 2018 Evaluation of Emerging Technologies on a 1.6 L Turbocharged GDI Engine. SAE 2018-01-1423\" V1"
         },
         {
-            "title": "Gap to gap region data: soil, water level, modflow output hyporheic flow pathlines (2013-2015)",
-            "description": ". In this study Light Detection and Ranging (LiDAR) data were used along with the head data from observation wells and stage data from rivers to setup and calibrate a groundwater model for 458 km2 of area within Gap to Gap reach of the Yakima River, WA. \n\nThis dataset is associated with the following publication:\nSingh, H., B. Faulkner, A. Keeley, J. Freudenthal, and K. Forshay. Floodplain restoration increases hyporheic flow in the Yakima River Watershed, Washington.   ECOLOGICAL ENGINEERING. Elsevier Science Ltd, New York, NY, USA, 116: 110-120, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1394800",
-            "keyword": [
-                "elevation",
-                "stage",
-                "hyporheic pathlines",
-                "hyporheic flow",
-                "MODFLOW",
-                "Floodplain",
-                "Levee setback"
-            ],
             "contactPoint": {
                 "fn": "Barton Faulkner",
                 "hasEmail": "mailto:faulkner.bart@epa.gov"
             },
+            "description": ". In this study Light Detection and Ranging (LiDAR) data were used along with the head data from observation wells and stage data from rivers to setup and calibrate a groundwater model for 458 km2 of area within Gap to Gap reach of the Yakima River, WA. \n\nThis dataset is associated with the following publication:\nSingh, H., B. Faulkner, A. Keeley, J. Freudenthal, and K. Forshay. Floodplain restoration increases hyporheic flow in the Yakima River Watershed, Washington.   ECOLOGICAL ENGINEERING. Elsevier Science Ltd, New York, NY, USA, 116: 110-120, (2018).",
             "distribution": [
                 {
-                    "title": "FaulknerBarton_A-rxx2_SDMP_20170825.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1394800/FaulknerBarton_A-rxx2_SDMP_20170825.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FaulknerBarton_A-rxx2_SDMP_20170825.xlsx"
                 },
                 {
-                    "title": "HSsdmp_template_short.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1394800/HSsdmp_template_short.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "HSsdmp_template_short.docx"
                 },
                 {
-                    "title": "QA.Summary.HarshSingh20170825.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1394800/QA.Summary.HarshSingh20170825.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "QA.Summary.HarshSingh20170825.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1394800",
+            "keyword": [
+                "elevation",
+                "stage",
+                "hyporheic pathlines",
+                "hyporheic flow",
+                "MODFLOW",
+                "Floodplain",
+                "Levee setback"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-17",
-            "references": [
-                "https://doi.org/10.1016/j.ecoleng.2018.02.001"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69791,84 +69785,85 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecoleng.2018.02.001"
+            ],
+            "rights": null,
+            "title": "Gap to gap region data: soil, water level, modflow output hyporheic flow pathlines (2013-2015)"
         },
         {
-            "title": "Dendrochronological data for western Oregon",
-            "description": "Master chronologies of radial stem growth of Douglas-fir for western Oregon. \n\nThis dataset is associated with the following publications:\nLee, E., P. Beedlow, R. Waschmann, D.T. Tingey, S. Cline, M. Bollman, C. Wickham, and C. Carlile. Regional patterns of increasing Swiss needle cast impacts on Douglas-fir growth with warming temperatures..   Ecology and Evolution. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 7(24): 11167-11196, (2017).\nLee, E., C. Wickham, P. Beedlow, R. Waschmann, and D.T. Tingey. A likelihood-based time series modeling approach for application in dendrochronology to examine the growth-climate relations and forest disturbance history.   Dendrochronologia. Elsevier, Shannon,  IRELAND, 45: 132-144, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1419254",
-            "keyword": [
-                "climate change",
-                "dendrochronology",
-                "Douglas-fir",
-                "Pacific Decadal Oscillation",
-                "Pacific Northwest",
-                "Swiss needle cast"
-            ],
             "contactPoint": {
                 "fn": "E. Lee",
                 "hasEmail": "mailto:lee.ehenry@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1419254/documents/Data%20dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Master chronologies of radial stem growth of Douglas-fir for western Oregon. \n\nThis dataset is associated with the following publications:\nLee, E., P. Beedlow, R. Waschmann, D.T. Tingey, S. Cline, M. Bollman, C. Wickham, and C. Carlile. Regional patterns of increasing Swiss needle cast impacts on Douglas-fir growth with warming temperatures..   Ecology and Evolution. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 7(24): 11167-11196, (2017).\nLee, E., C. Wickham, P. Beedlow, R. Waschmann, and D.T. Tingey. A likelihood-based time series modeling approach for application in dendrochronology to examine the growth-climate relations and forest disturbance history.   Dendrochronologia. Elsevier, Shannon,  IRELAND, 45: 132-144, (2017).",
             "distribution": [
                 {
-                    "title": "falls_creek_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/falls_creek_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "falls_creek_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "horse_creek_trail_upper_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/horse_creek_trail_upper_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "horse_creek_trail_upper_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "cascade_head_14_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/cascade_head_14_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "cascade_head_14_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "horse_creek_trail_lower_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/horse_creek_trail_lower_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "horse_creek_trail_lower_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "jackson_place_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/jackson_place_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "jackson_place_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "moose_mtn_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/moose_mtn_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "moose_mtn_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "toad_creek_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/toad_creek_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "toad_creek_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "woods_creek_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/woods_creek_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "woods_creek_douglas-fir_ringwidth.xls"
                 },
                 {
-                    "title": "soapgrass_mtn_douglas-fir_ringwidth.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1419254/soapgrass_mtn_douglas-fir_ringwidth.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "soapgrass_mtn_douglas-fir_ringwidth.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1419254",
+            "keyword": [
+                "climate change",
+                "dendrochronology",
+                "Douglas-fir",
+                "Pacific Decadal Oscillation",
+                "Pacific Northwest",
+                "Swiss needle cast"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-15",
-            "references": [
-                "https://doi.org/10.1002/ece3.3573",
-                "https://doi.org/10.1016/j.dendro.2017.08.003"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69879,20 +69874,29 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1419254/documents/Data%20dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1002/ece3.3573",
+                "https://doi.org/10.1016/j.dendro.2017.08.003"
+            ],
+            "rights": null,
+            "title": "Dendrochronological data for western Oregon"
         },
         {
-            "title": "Supporting data for \"Lee, S.D., Cherry, J., Safoutin, M., McDonald, J. et al. 2018. Modeling and Validation of 48 V Mild Hybrid Lithium-Ion Battery Pack. SAE 2018-01-0433\" V1",
-            "description": "The purpose of this work was to develop and validate a 48 V lithium-ion battery model for integration into EPA\u2019s ALPHA vehicle simulation model and that can also be used within Gamma Technologies, LLC (Westmont, IL) GT-DRIVE\u2122 vehicle simulations.  These vehicle models allow simulation of energy flows and CO2 emissions for mild hybrid electric vehicles over EPA regulatory drive cycles and during real-world driving.  The battery model is a standard equivalent circuit model with two-time constant resistance-capacitance (RC) blocks. Resistances and capacitances were calculated using test data from an 8 Ah, 0.4 kWh, 48 V (nominal) lithium-ion battery obtained from a Tier 1 automotive supplier, A123 Systems, and developed specifically for 48 V MHEV applications. The A123 Systems battery has 14 pouch-type lithium ion cells arranged in a 14 series and 1 parallel (14S1P) configuration. The RC battery model was validated using battery test data generated by a hardware-in-the-loop (HIL) system that simulated the impact of mild hybrid electric vehicle (MHEV) operation on the A123 systems 48 V battery pack over U.S. regulatory drive cycles. The HIL system matched charge and discharge data originally generated by Argonne National Laboratory (ANL) during chassis dynamometer testing of a 2013 Chevy Malibu Eco 115 V MHEV. All validation testing was performed at the Battery Test Facility (BTF) at the U.S. EPA National Vehicle and Fuel Emissions Laboratory (NVFEL) in Ann Arbor, Michigan. The simulated battery voltages, currents, and state of charge (SOC) of the HIL tests were in good agreement with vehicle test data over a number of different drive cycles and excellent agreement was achieved between RC model simulations of the 48 V battery and HIL battery test data. \n\nThis dataset is associated with the following publication:\nLee, S., J. Cherry, M. Safoutin, J. McDonald, and M. Olechiw. Modeling and Validation of 48V Mild Hybrid Lithium-ion Battery Pack.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  11, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Joseph McDonald",
+                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
+            },
+            "description": "The purpose of this work was to develop and validate a 48 V lithium-ion battery model for integration into EPA\u2019s ALPHA vehicle simulation model and that can also be used within Gamma Technologies, LLC (Westmont, IL) GT-DRIVE\u2122 vehicle simulations.  These vehicle models allow simulation of energy flows and CO2 emissions for mild hybrid electric vehicles over EPA regulatory drive cycles and during real-world driving.  The battery model is a standard equivalent circuit model with two-time constant resistance-capacitance (RC) blocks. Resistances and capacitances were calculated using test data from an 8 Ah, 0.4 kWh, 48 V (nominal) lithium-ion battery obtained from a Tier 1 automotive supplier, A123 Systems, and developed specifically for 48 V MHEV applications. The A123 Systems battery has 14 pouch-type lithium ion cells arranged in a 14 series and 1 parallel (14S1P) configuration. The RC battery model was validated using battery test data generated by a hardware-in-the-loop (HIL) system that simulated the impact of mild hybrid electric vehicle (MHEV) operation on the A123 systems 48 V battery pack over U.S. regulatory drive cycles. The HIL system matched charge and discharge data originally generated by Argonne National Laboratory (ANL) during chassis dynamometer testing of a 2013 Chevy Malibu Eco 115 V MHEV. All validation testing was performed at the Battery Test Facility (BTF) at the U.S. EPA National Vehicle and Fuel Emissions Laboratory (NVFEL) in Ann Arbor, Michigan. The simulated battery voltages, currents, and state of charge (SOC) of the HIL tests were in good agreement with vehicle test data over a number of different drive cycles and excellent agreement was achieved between RC model simulations of the 48 V battery and HIL battery test data. \n\nThis dataset is associated with the following publication:\nLee, S., J. Cherry, M. Safoutin, J. McDonald, and M. Olechiw. Modeling and Validation of 48V Mild Hybrid Lithium-ion Battery Pack.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  11, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435437/SAE%202018-01-0433%2048V%20Li-Ion%20Battery%20Model.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "SAE 2018-01-0433 48V Li-Ion Battery Model.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1435437",
             "keyword": [
@@ -69904,20 +69908,10 @@
                 "Hybrid Electric Vehicles",
                 "Electric Vehicles"
             ],
-            "contactPoint": {
-                "fn": "Joseph McDonald",
-                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SAE 2018-01-0433 48V Li-Ion Battery Model.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435437/SAE%202018-01-0433%2048V%20Li-Ion%20Battery%20Model.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": [
-                "https://doi.org/10.4271/2018-01-0433"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69927,19 +69921,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.4271/2018-01-0433"
+            ],
+            "rights": null,
+            "title": "Supporting data for \"Lee, S.D., Cherry, J., Safoutin, M., McDonald, J. et al. 2018. Modeling and Validation of 48 V Mild Hybrid Lithium-Ion Battery Pack. SAE 2018-01-0433\" V1"
         },
         {
-            "title": "Supporting data for \"Lee, S., Cherry, J., Safoutin, M., Neam, A., McDonald, J., Newman, K.  2018. Modeling and Controls Development of 48 V Mild Hybrid Electric Vehicles. SAE 2018-01-0413\" V1",
-            "description": "The purpose of this work was to develop a 48 V mild hybrid electric vehicle (MHEV) model for drive cycle simulation using the EPA Advanced Light-Duty Powertrain and Hybrid Analysis tool (ALPHA).  The work included controls development, component and vehicle modeling , and model validation for simulations of a vehicle with a 48 V Belt Integrated Starter Generator (BISG) MHEV system.  An initial model design was also developed for a 48 V inline on-axis P2-configuration MHEV and will be validated as part of future work. Both MHEV configurations were developed into sub-models using a MATLAB/Simulink/Stateflow tool.  The sub-models have subsequently been integrated into EPA\u2019s ALPHA vehicle model.  Initial sub-model development and validation was conducted using the commercially-available Gamma Technology GT-DRIVE vehicle simulation model. The mild hybrid electric vehicle model was validated using vehicle data obtained from Argonne National Laboratory (ANL) chassis dynamometer tests of a 2013 Chevrolet Malibu Eco 115 V 15 kW BISG mild hybrid electric vehicle. The simulated fuel economy, engine torque/speed, motor torque/speed, engine on-off controls, battery voltage, current, and State of Charge (SOC) were all in good agreement with the vehicle test data on a number of drive schedules. The developed 48 V mild hybrid electric vehicle model can be used to estimate the GHG emissions and fuel economy of 48 V mild hybrid electric vehicles over the EPA regulatory drive cycles and to estimate off-cycle GHG emissions, real-world GHG emissions, and vehicle energy flows. The 48 V mild hybrid electric vehicle model will be further validated with additional 48 V mild hybrid electric vehicle test data in the future as more vehicle models become available. EPA has included 48 V BISG mild hybrid electric vehicle technology in its assessment of CO2-reducing technologies available for compliance with U.S. GHG standards. \n\nThis dataset is associated with the following publication:\nLee, S., M. Safoutin, A. Neam, J. Cherry, and J. McDonald. Modeling and Controls Development of 48V Mild Hybrid Electric Vehicles.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  15, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Joseph McDonald",
+                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
+            },
+            "description": "The purpose of this work was to develop a 48 V mild hybrid electric vehicle (MHEV) model for drive cycle simulation using the EPA Advanced Light-Duty Powertrain and Hybrid Analysis tool (ALPHA).  The work included controls development, component and vehicle modeling , and model validation for simulations of a vehicle with a 48 V Belt Integrated Starter Generator (BISG) MHEV system.  An initial model design was also developed for a 48 V inline on-axis P2-configuration MHEV and will be validated as part of future work. Both MHEV configurations were developed into sub-models using a MATLAB/Simulink/Stateflow tool.  The sub-models have subsequently been integrated into EPA\u2019s ALPHA vehicle model.  Initial sub-model development and validation was conducted using the commercially-available Gamma Technology GT-DRIVE vehicle simulation model. The mild hybrid electric vehicle model was validated using vehicle data obtained from Argonne National Laboratory (ANL) chassis dynamometer tests of a 2013 Chevrolet Malibu Eco 115 V 15 kW BISG mild hybrid electric vehicle. The simulated fuel economy, engine torque/speed, motor torque/speed, engine on-off controls, battery voltage, current, and State of Charge (SOC) were all in good agreement with the vehicle test data on a number of drive schedules. The developed 48 V mild hybrid electric vehicle model can be used to estimate the GHG emissions and fuel economy of 48 V mild hybrid electric vehicles over the EPA regulatory drive cycles and to estimate off-cycle GHG emissions, real-world GHG emissions, and vehicle energy flows. The 48 V mild hybrid electric vehicle model will be further validated with additional 48 V mild hybrid electric vehicle test data in the future as more vehicle models become available. EPA has included 48 V BISG mild hybrid electric vehicle technology in its assessment of CO2-reducing technologies available for compliance with U.S. GHG standards. \n\nThis dataset is associated with the following publication:\nLee, S., M. Safoutin, A. Neam, J. Cherry, and J. McDonald. Modeling and Controls Development of 48V Mild Hybrid Electric Vehicles.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  15, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435438/SAE%202018-01-0413%2048V%20MHEV%20Model.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "SAE 2018-01-0413 48V MHEV Model.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1435438",
             "keyword": [
@@ -69951,20 +69955,10 @@
                 "Hybrid Electric Vehicles",
                 "Electric Vehicles"
             ],
-            "contactPoint": {
-                "fn": "Joseph McDonald",
-                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SAE 2018-01-0413 48V MHEV Model.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435438/SAE%202018-01-0413%2048V%20MHEV%20Model.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": [
-                "https://doi.org/10.4271/2018-01-0413"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -69974,19 +69968,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.4271/2018-01-0413"
+            ],
+            "rights": null,
+            "title": "Supporting data for \"Lee, S., Cherry, J., Safoutin, M., Neam, A., McDonald, J., Newman, K.  2018. Modeling and Controls Development of 48 V Mild Hybrid Electric Vehicles. SAE 2018-01-0413\" V1"
         },
         {
-            "title": "Supporting data for \"Robertson, D., Conway, G., Chadwell, C., McDonald, J. et al. 2018. Predictive GT-Power Simulation for VNT Matching on a 1.6 L Turbocharged GDI Engine. SAE 2018-01-0161\" V1",
-            "description": "Low-pressure loop exhaust gas recirculation (LP- EGR) combined with higher compression ratio, is a technology package that has been a focus of research to increase engine thermal efficiency of downsized, turbocharged gasoline direct injection (GDI) engines. Research shows that the addition of LP-EGR reduces the propensity to knock that is experienced at higher compression ratios [1]. To investigate the interaction and compatibility between increased compression ratio and LP-EGR, a 1.6 L Turbocharged GDI engine was modified to run with LP-EGR at a higher compression ratio (12:1 versus 10.5:1) via a piston change. This paper presents the results of the baseline testing on an engine run with a prototype controller and initially tuned to mimic an original equipment manufacturer (OEM) baseline control strategy running on premium fuel (92.8 anti-knock index). This paper then presents test results after first adding LP-EGR to the baseline engine, and then also increasing the compression ratio (CR) using 12:1 pistons. As a last step, the 10.5 CR engine with LP-EGR was run on regular fuel (87.7 anti-knock index) to verify that this configuration could be calibrated to maintain performance like the baseline engine running on premium fuel. To understand the effect of each technology and operating strategy combination on vehicle fuel economy, the various engine maps were compared in EPA\u2019s Advanced Light-Duty Powertrain and Hybrid Analysis (ALPHA) tool over U.S. regulatory drive cycles. This work was done as part of the EPA's continuing assessment of advanced light-duty automotive technologies to support a Midterm Evaluation of Light-duty Vehicle GHG Standards. \n\nThis dataset is associated with the following publication:\nMcDonald, J., J. Kargul, D. Barba, G. Conway, D. Robertson, and C. Chadwell. Predictive GT-Power Simulation for VNT Matching on a 1.6 L GDI Turbocharged Engine.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  16, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Joseph McDonald",
+                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
+            },
+            "description": "Low-pressure loop exhaust gas recirculation (LP- EGR) combined with higher compression ratio, is a technology package that has been a focus of research to increase engine thermal efficiency of downsized, turbocharged gasoline direct injection (GDI) engines. Research shows that the addition of LP-EGR reduces the propensity to knock that is experienced at higher compression ratios [1]. To investigate the interaction and compatibility between increased compression ratio and LP-EGR, a 1.6 L Turbocharged GDI engine was modified to run with LP-EGR at a higher compression ratio (12:1 versus 10.5:1) via a piston change. This paper presents the results of the baseline testing on an engine run with a prototype controller and initially tuned to mimic an original equipment manufacturer (OEM) baseline control strategy running on premium fuel (92.8 anti-knock index). This paper then presents test results after first adding LP-EGR to the baseline engine, and then also increasing the compression ratio (CR) using 12:1 pistons. As a last step, the 10.5 CR engine with LP-EGR was run on regular fuel (87.7 anti-knock index) to verify that this configuration could be calibrated to maintain performance like the baseline engine running on premium fuel. To understand the effect of each technology and operating strategy combination on vehicle fuel economy, the various engine maps were compared in EPA\u2019s Advanced Light-Duty Powertrain and Hybrid Analysis (ALPHA) tool over U.S. regulatory drive cycles. This work was done as part of the EPA's continuing assessment of advanced light-duty automotive technologies to support a Midterm Evaluation of Light-duty Vehicle GHG Standards. \n\nThis dataset is associated with the following publication:\nMcDonald, J., J. Kargul, D. Barba, G. Conway, D. Robertson, and C. Chadwell. Predictive GT-Power Simulation for VNT Matching on a 1.6 L GDI Turbocharged Engine.   SAE Technical Paper Series. SAE International, Warrendale, PA, USA,  16, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435449/SAE%202018-01-0161%20%201.6%20L%20TGDI%20VNT%20Engine%20Model.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "SAE 2018-01-0161  1.6 L TGDI VNT Engine Model.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1435449",
             "keyword": [
@@ -69998,20 +70002,10 @@
                 "Hybrid Electric Vehicles",
                 "Electric Vehicles"
             ],
-            "contactPoint": {
-                "fn": "Joseph McDonald",
-                "hasEmail": "mailto:mcdonald.joseph@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SAE 2018-01-0161  1.6 L TGDI VNT Engine Model.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435449/SAE%202018-01-0161%20%201.6%20L%20TGDI%20VNT%20Engine%20Model.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": [
-                "https://doi.org/10.4271/2018-01-0161"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70021,45 +70015,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.4271/2018-01-0161"
+            ],
+            "rights": null,
+            "title": "Supporting data for \"Robertson, D., Conway, G., Chadwell, C., McDonald, J. et al. 2018. Predictive GT-Power Simulation for VNT Matching on a 1.6 L Turbocharged GDI Engine. SAE 2018-01-0161\" V1"
         },
         {
-            "title": "Supporting datasets for paper \"Estimating Future Temperature Maxima in Lakes across the United States using a Surrogate Modeling Approach\"",
-            "description": "Model input and simulation output files. \n\nThis dataset is associated with the following publication:\nButcher, J., T. Zi, M. Schmidt, T. Johnson, D. Nover, and C. Clark. Critical Lake Temperature Response to Climate Change across the United States.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 12(11): 1-16, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1376237",
-            "keyword": [
-                "climate",
-                "change",
-                "lake",
-                "thermal"
-            ],
             "contactPoint": {
                 "fn": "Thomas Johnson",
                 "hasEmail": "mailto:johnson.thomas@epa.gov"
             },
+            "description": "Model input and simulation output files. \n\nThis dataset is associated with the following publication:\nButcher, J., T. Zi, M. Schmidt, T. Johnson, D. Nover, and C. Clark. Critical Lake Temperature Response to Climate Change across the United States.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 12(11): 1-16, (2017).",
             "distribution": [
                 {
-                    "title": "Lakes_Data Files.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1376237/Lakes_Data%20Files.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Lakes_Data Files.docx"
                 },
                 {
-                    "title": "https://osf.io/4r44z/",
-                    "accessURL": "https://osf.io/4r44z/"
+                    "accessURL": "https://osf.io/4r44z/",
+                    "title": "https://osf.io/4r44z/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1376237",
+            "keyword": [
+                "climate",
+                "change",
+                "lake",
+                "thermal"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-24",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0183499"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70069,53 +70063,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0183499"
+            ],
+            "rights": null,
+            "title": "Supporting datasets for paper \"Estimating Future Temperature Maxima in Lakes across the United States using a Surrogate Modeling Approach\""
         },
         {
-            "title": "MBRs LCI and LCIA data",
-            "description": "This study calculated the cumulative energy and greenhouse gas (GHG) life cycle and cost profiles of transitional aerobic membrane bioreactors (AeMBR) and anaerobic MBRs (AnMBR). Membrane bioreactors (MBR) represent a promising technology for decentralized wastewater treatment and can produce recycled water to displace potable water. Energy recovery is also possible with methane generated from AnMBRs. In this study, scenarios for these technologies were investigated for different scale systems serving various population densities under various climate conditions with multiple methane recovery options. Details of the GHG life cycle and cost profiles for the AeMBR and AnMBR can be found in AeMBR_LCI_Cost_9-9-15.xls and AnMBR_LCI_Cost_9-9-15.xls respectively. Results of the previously described comparisons can be found can be found in MBR_LCIAResults_9-9-15.xlsx. \n\nThis dataset is associated with the following publication:\nCashman, S., C. Ma, J. Mosley, J. Garland, B. Crone, and X. Xue. Energy and greenhouse gas life cycle assessment and cost analysis of aerobic and anaerobic membrane bioreactor systems: Influence of scale, population density, climate, and methane recovery.   Bioresource Technology. Elsevier Online, New York, NY, USA, 254: 56-66, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1413477",
-            "keyword": [
-                "life cycle assessment",
-                "Membrane Bioreactor",
-                "Energy Demand",
-                "Greenhouse gas",
-                "Life Cycle Cost",
-                "e Cycle Assessment"
-            ],
             "contactPoint": {
                 "fn": "Jay Garland",
                 "hasEmail": "mailto:garland.jay@epa.gov"
             },
+            "description": "This study calculated the cumulative energy and greenhouse gas (GHG) life cycle and cost profiles of transitional aerobic membrane bioreactors (AeMBR) and anaerobic MBRs (AnMBR). Membrane bioreactors (MBR) represent a promising technology for decentralized wastewater treatment and can produce recycled water to displace potable water. Energy recovery is also possible with methane generated from AnMBRs. In this study, scenarios for these technologies were investigated for different scale systems serving various population densities under various climate conditions with multiple methane recovery options. Details of the GHG life cycle and cost profiles for the AeMBR and AnMBR can be found in AeMBR_LCI_Cost_9-9-15.xls and AnMBR_LCI_Cost_9-9-15.xls respectively. Results of the previously described comparisons can be found can be found in MBR_LCIAResults_9-9-15.xlsx. \n\nThis dataset is associated with the following publication:\nCashman, S., C. Ma, J. Mosley, J. Garland, B. Crone, and X. Xue. Energy and greenhouse gas life cycle assessment and cost analysis of aerobic and anaerobic membrane bioreactor systems: Influence of scale, population density, climate, and methane recovery.   Bioresource Technology. Elsevier Online, New York, NY, USA, 254: 56-66, (2018).",
             "distribution": [
                 {
-                    "title": "AeMBR_LCI_Cost_9-9-15.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413477/AeMBR_LCI_Cost_9-9-15.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AeMBR_LCI_Cost_9-9-15.xls"
                 },
                 {
-                    "title": "AnMBR_LCI_Cost_9-9-15.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413477/AnMBR_LCI_Cost_9-9-15.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AnMBR_LCI_Cost_9-9-15.xls"
                 },
                 {
-                    "title": "MBR_LCIAResults_9-9-15.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413477/MBR_LCIAResults_9-9-15.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MBR_LCIAResults_9-9-15.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1413477",
+            "keyword": [
+                "life cycle assessment",
+                "Membrane Bioreactor",
+                "Energy Demand",
+                "Greenhouse gas",
+                "Life Cycle Cost",
+                "e Cycle Assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-23",
-            "references": [
-                "https://doi.org/10.1016/j.biortech.2018.01.060"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70125,19 +70119,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.biortech.2018.01.060"
+            ],
+            "rights": null,
+            "title": "MBRs LCI and LCIA data"
         },
         {
-            "title": "Data for MAMA Study and modeled predictions for PBDEs",
-            "description": "Data set contains concentrations of persistent organic chemicals measured breast milk and blood for a small cohort of North Carolina women. \n\nThis dataset is associated with the following publication:\nMarchitti, S., S. Fenton, P. Mendola, J. Kenneke , and E. Hines. Polybrominated Diphenyl Ethers in Human Milk and Serum from the U.S. EPA MAMA Study: Modeled Predictions of Infant Exposure and Considerations for Risk Assessment.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(4): 706\u2013713, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "John Kenneke",
+                "hasEmail": "mailto:kenneke.john@epa.gov"
+            },
+            "description": "Data set contains concentrations of persistent organic chemicals measured breast milk and blood for a small cohort of North Carolina women. \n\nThis dataset is associated with the following publication:\nMarchitti, S., S. Fenton, P. Mendola, J. Kenneke , and E. Hines. Polybrominated Diphenyl Ethers in Human Milk and Serum from the U.S. EPA MAMA Study: Modeled Predictions of Infant Exposure and Considerations for Risk Assessment.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(4): 706\u2013713, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407656/MAMA%20Study%20Data.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "MAMA Study Data.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407656",
             "keyword": [
@@ -70151,20 +70155,10 @@
                 "transporter",
                 "Metabolism"
             ],
-            "contactPoint": {
-                "fn": "John Kenneke",
-                "hasEmail": "mailto:kenneke.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MAMA Study Data.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407656/MAMA%20Study%20Data.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-01-25",
-            "references": [
-                "https://doi.org/10.1289/ehp332"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70174,19 +70168,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp332"
+            ],
+            "rights": null,
+            "title": "Data for MAMA Study and modeled predictions for PBDEs"
         },
         {
-            "title": "Data set fro Inhibition of Human ABC efflux transporters p-gp and BCRP by BDE-47 hydroxylated metabolite 6-OH-BDE-47",
-            "description": "In vitro data from cell-based assays on the inhibition of BDE and its hydroxylated metabolite on ABC transporters. \n\nThis dataset is associated with the following publication:\nMarchitti, S., C. Mazur, C. Dillingham, S. Rawat, A. Sharma, J. Zastre, and J. Kenneke. Inhibition of the Human ABC Efflux Transporters P-gp and BCRP by the BDE-47 Hydroxylated Metabolite 6-OH-BDE-47: Considerations for Human Exposure.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    155(1): 270-282, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "John Kenneke",
+                "hasEmail": "mailto:kenneke.john@epa.gov"
+            },
+            "description": "In vitro data from cell-based assays on the inhibition of BDE and its hydroxylated metabolite on ABC transporters. \n\nThis dataset is associated with the following publication:\nMarchitti, S., C. Mazur, C. Dillingham, S. Rawat, A. Sharma, J. Zastre, and J. Kenneke. Inhibition of the Human ABC Efflux Transporters P-gp and BCRP by the BDE-47 Hydroxylated Metabolite 6-OH-BDE-47: Considerations for Human Exposure.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    155(1): 270-282, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407655/Data%20for%20Figures%20Marchitti%20SOT%202017.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Data for Figures Marchitti SOT 2017.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407655",
             "keyword": [
@@ -70200,20 +70204,10 @@
                 "PBDE",
                 "Metabolism"
             ],
-            "contactPoint": {
-                "fn": "John Kenneke",
-                "hasEmail": "mailto:kenneke.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data for Figures Marchitti SOT 2017.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407655/Data%20for%20Figures%20Marchitti%20SOT%202017.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-13",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfw209"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70223,42 +70217,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfw209"
+            ],
+            "rights": null,
+            "title": "Data set fro Inhibition of Human ABC efflux transporters p-gp and BCRP by BDE-47 hydroxylated metabolite 6-OH-BDE-47"
         },
         {
-            "title": "McEachran target NTA Sciencehub entry 170926",
-            "description": "This dataset contains:\nNTA Features - Aligned, processed, and matched HRMS features from non-target analysis for both positive and negative ESI modes for both sites and all three sampling months \nTargeted FWRS data - Monthly concentrations and chemical identifiers of all targeted CECs at the Forest Water Reuse System (FWRS)\nConventional WWTP Data - Monthly concentrations and chemical identifiers of all targeted CECs at the Conventional WWTP. \n\nThis dataset is associated with the following publication:\nMcEachran, A., M. Hedgespeth, S. Newton, R. McMahen, M. Strynar, D. Shea, and E. Guthrie Nichols. Comparison of emerging contaminants in receiving waters downstream of a conventional wastewater treatment plant and a forest-water reuse system.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 25(13): 12451-12463, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1407653",
-            "keyword": [
-                "wastewater",
-                "contaminants of emerging concern (CEC)",
-                "forest-water reuse",
-                "non-targeted analysis",
-                "surface water"
-            ],
             "contactPoint": {
                 "fn": "Seth Newton",
                 "hasEmail": "mailto:newton.seth@epa.gov"
             },
+            "description": "This dataset contains:\nNTA Features - Aligned, processed, and matched HRMS features from non-target analysis for both positive and negative ESI modes for both sites and all three sampling months \nTargeted FWRS data - Monthly concentrations and chemical identifiers of all targeted CECs at the Forest Water Reuse System (FWRS)\nConventional WWTP Data - Monthly concentrations and chemical identifiers of all targeted CECs at the Conventional WWTP. \n\nThis dataset is associated with the following publication:\nMcEachran, A., M. Hedgespeth, S. Newton, R. McMahen, M. Strynar, D. Shea, and E. Guthrie Nichols. Comparison of emerging contaminants in receiving waters downstream of a conventional wastewater treatment plant and a forest-water reuse system.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 25(13): 12451-12463, (2018).",
             "distribution": [
                 {
-                    "title": "McEachran target NTA Sciencehub entry 170926.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407653/McEachran%20target%20NTA%20Sciencehub%20entry%20170926.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "McEachran target NTA Sciencehub entry 170926.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407653",
+            "keyword": [
+                "wastewater",
+                "contaminants of emerging concern (CEC)",
+                "forest-water reuse",
+                "non-targeted analysis",
+                "surface water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-26",
-            "references": [
-                "https://doi.org/10.1007/s11356-018-1505-5"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70268,47 +70262,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11356-018-1505-5"
+            ],
+            "rights": null,
+            "title": "McEachran target NTA Sciencehub entry 170926"
         },
         {
-            "title": "Comparative study on the performance of Anaerobic and Aerobic Biotrickling Filter for the Removal of Chloroform",
-            "description": "Method for the removal and degradation of harmful disinfection byproducts from drinking water. \n\nThis dataset is associated with the following publication:\nMezgebe, B., K. Palanisamy,, G. Sorial, E. Sahle-Demessie, A. Aly Hassan, and J. Lu. Comparative Study on the Performance of Anaerobic and Aerobic Biotrickling Filter for Removal of Chloroform.   ENVIRONMENTAL ENGINEERING SCIENCE. Mary Ann Liebert, Inc., Larchmont, NY, USA, 35(5): 462-471, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1435446",
-            "keyword": [
-                "Aerobic",
-                "anaerobic",
-                "Biotrickling Filter",
-                "Microbial diversity",
-                "trihalomethanes"
-            ],
             "contactPoint": {
                 "fn": "Endalkac Sahle-Demessie",
                 "hasEmail": "mailto:sahle-demessie.endalkachew@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1435446/documents/Data%20Dictionary_BiotrickleFiltration.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Method for the removal and degradation of harmful disinfection byproducts from drinking water. \n\nThis dataset is associated with the following publication:\nMezgebe, B., K. Palanisamy,, G. Sorial, E. Sahle-Demessie, A. Aly Hassan, and J. Lu. Comparative Study on the Performance of Anaerobic and Aerobic Biotrickling Filter for Removal of Chloroform.   ENVIRONMENTAL ENGINEERING SCIENCE. Mary Ann Liebert, Inc., Larchmont, NY, USA, 35(5): 462-471, (2017).",
             "distribution": [
                 {
-                    "title": "G-STD-0016294-JA-7-0_figs.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435446/G-STD-0016294-JA-7-0_figs.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "G-STD-0016294-JA-7-0_figs.docx"
                 },
                 {
-                    "title": "G-STD-0016294-JA-7-0.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435446/G-STD-0016294-JA-7-0.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "G-STD-0016294-JA-7-0.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435446",
+            "keyword": [
+                "Aerobic",
+                "anaerobic",
+                "Biotrickling Filter",
+                "Microbial diversity",
+                "trihalomethanes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-01",
-            "references": [
-                "https://doi.org/10.1089/ees.2017.0275"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70319,20 +70315,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1435446/documents/Data%20Dictionary_BiotrickleFiltration.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1089/ees.2017.0275"
+            ],
+            "rights": null,
+            "title": "Comparative study on the performance of Anaerobic and Aerobic Biotrickling Filter for the Removal of Chloroform"
         },
         {
-            "title": "Las Vegas Data",
-            "description": "Las Vegas Near Road Data. \n\nThis dataset is associated with the following publication:\nKimbrough , S., C. Owen, M. Snyder, and J. Richmond-Bryant. NO to NO2 conversion rate analysis and implications for dispersion model chemistry\r\nmethods using Las Vegas, Nevada near-road field measurements.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 165: 23-24, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Evelyn Kimbrough",
+                "hasEmail": "mailto:kimbrough.sue@epa.gov"
+            },
+            "description": "Las Vegas Near Road Data. \n\nThis dataset is associated with the following publication:\nKimbrough , S., C. Owen, M. Snyder, and J. Richmond-Bryant. NO to NO2 conversion rate analysis and implications for dispersion model chemistry\r\nmethods using Las Vegas, Nevada near-road field measurements.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 165: 23-24, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1373703/LVdata.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "LVdata.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1373703",
             "keyword": [
@@ -70343,20 +70347,10 @@
                 "air quality",
                 "air pollution"
             ],
-            "contactPoint": {
-                "fn": "Evelyn Kimbrough",
-                "hasEmail": "mailto:kimbrough.sue@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "LVdata.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1373703/LVdata.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-23",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.06.027"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70366,48 +70360,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2017.06.027"
+            ],
+            "rights": null,
+            "title": "Las Vegas Data"
         },
         {
-            "title": "Climate differentiates forest structure across a residential macrosystem",
-            "description": "The extent of urban ecological homogenization depends on how humans build, inhabit, and manage cities.  Morphological and socio-economic facets of neighborhoods can drive the homogenization of forest cover, thus affecting urban ecological and hydrological processes, and ecosystem services.  Recent evidence, however, suggests that the same biophysical drivers differentiating composition and structure of natural forests can further counteract the homogenization of urban forests.  We hypothesize that climate can differentiate forest structure across residential macrosystems, regional-to-continental discontinuous systems of urban land.  To test this hypothesis, forest structure (tree and shrub cover and volume) was measured using LiDAR data and multispectral imagery across a residential macrosystem composed of 9 cities, 1503 neighborhoods, and 1.4 million residential parcels.  Cities were selected along a potential evapotranspiration (PET) gradient in the conterminous United States, ranging from the colder continental climate of Fargo, North Dakota (PET = 66.21 mm) to the hotter subtropical climate of Tallahassee, Florida (PET = 160.49 mm).  The relative effects of climate, urban morphology, and socio-economic variables on residential forest structure were assessed by using generalized linear models.  Climate differentiated forest structure of the residential macrosystem as hypothesized.  Average forest cover doubled along the PET gradient (0.39 - 0.78 m2 m-2), whereas average forest volume had a threefold increase (2.50 \u2013 8.12 m3 m-2).  Forest volume across neighborhoods increased exponentially with forest cover.  Urban morphology had a greater effect in homogenizing forest structure on residential parcels compared to socio-economics.  Climate and urban morphology variables best predicted residential forest structure, whereas socio-economic variables had the lowest predictive power.  Results indicate that climate can differentiate forest structure across residential macrosystems and may counteract the homogenizing effects of urban morphology and socio-economic drivers at city-wide scales.  This resonates with recent empirical work suggesting the existence of complex multi-scalar mechanisms that regulate ecological homogenization and ecosystem convergence among cities.  The study initiates high-resolution assessments of forest structure across entire urban macrosystems and breaks new ground for research on the ecological and hydrological significance of urban vegetation at subcontinental scale. \n\nThis dataset is associated with the following publication:\nOssola, A., and M. Hopton. Climate differentiates forest structure across a residential macrosystem.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 639: 1164-1174, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1393851",
-            "keyword": [
-                "Green Infrastructure",
-                "socio-ecological systems",
-                "urban ecology",
-                "urban trees",
-                "urban ecosystem convergence theory",
-                "ecosystem services"
-            ],
             "contactPoint": {
                 "fn": "Matthew Hopton",
                 "hasEmail": "mailto:hopton.matthew@epa.gov"
             },
+            "description": "The extent of urban ecological homogenization depends on how humans build, inhabit, and manage cities.  Morphological and socio-economic facets of neighborhoods can drive the homogenization of forest cover, thus affecting urban ecological and hydrological processes, and ecosystem services.  Recent evidence, however, suggests that the same biophysical drivers differentiating composition and structure of natural forests can further counteract the homogenization of urban forests.  We hypothesize that climate can differentiate forest structure across residential macrosystems, regional-to-continental discontinuous systems of urban land.  To test this hypothesis, forest structure (tree and shrub cover and volume) was measured using LiDAR data and multispectral imagery across a residential macrosystem composed of 9 cities, 1503 neighborhoods, and 1.4 million residential parcels.  Cities were selected along a potential evapotranspiration (PET) gradient in the conterminous United States, ranging from the colder continental climate of Fargo, North Dakota (PET = 66.21 mm) to the hotter subtropical climate of Tallahassee, Florida (PET = 160.49 mm).  The relative effects of climate, urban morphology, and socio-economic variables on residential forest structure were assessed by using generalized linear models.  Climate differentiated forest structure of the residential macrosystem as hypothesized.  Average forest cover doubled along the PET gradient (0.39 - 0.78 m2 m-2), whereas average forest volume had a threefold increase (2.50 \u2013 8.12 m3 m-2).  Forest volume across neighborhoods increased exponentially with forest cover.  Urban morphology had a greater effect in homogenizing forest structure on residential parcels compared to socio-economics.  Climate and urban morphology variables best predicted residential forest structure, whereas socio-economic variables had the lowest predictive power.  Results indicate that climate can differentiate forest structure across residential macrosystems and may counteract the homogenizing effects of urban morphology and socio-economic drivers at city-wide scales.  This resonates with recent empirical work suggesting the existence of complex multi-scalar mechanisms that regulate ecological homogenization and ecosystem convergence among cities.  The study initiates high-resolution assessments of forest structure across entire urban macrosystems and breaks new ground for research on the ecological and hydrological significance of urban vegetation at subcontinental scale. \n\nThis dataset is associated with the following publication:\nOssola, A., and M. Hopton. Climate differentiates forest structure across a residential macrosystem.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 639: 1164-1174, (2018).",
             "distribution": [
                 {
-                    "title": "Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1393851/Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data.xlsx"
                 },
                 {
-                    "title": "Ranalyses.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1393851/Ranalyses.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Ranalyses.txt"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1393851",
+            "keyword": [
+                "Green Infrastructure",
+                "socio-ecological systems",
+                "urban ecology",
+                "urban trees",
+                "urban ecosystem convergence theory",
+                "ecosystem services"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-17",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2018.05.237"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70417,84 +70411,94 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2018.05.237"
+            ],
+            "rights": null,
+            "title": "Climate differentiates forest structure across a residential macrosystem"
         },
         {
-            "title": "Supporting Simulation Output - Earth Interactions article \"The Effects of Downscaling Method on the Variability of Simulated Watershed Response to Climate Change in Five U.S. Basins\"",
-            "description": "Monthly summaries of simulated watershed responses to mid-century climate change scenarios in 5 U.S. basins. \n\nThis dataset is associated with the following publication:\nNover, D., J. Witt , J. Butcher, T. Johnson , and C. Weaver. The Effects of Downscaling Method on the Variability of Simulated Watershed Response to Climate Change in Five U.S. Basins.   Earth Interactions. American Meteorological Society, Boston, MA, USA, 20, 1-27, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1390087",
-            "keyword": [
-                "climate change streamflow water quality downscaling",
-                "climate",
-                "change",
-                "downscaling",
-                "method"
-            ],
             "contactPoint": {
                 "fn": "Thomas Johnson",
                 "hasEmail": "mailto:johnson.thomas@epa.gov"
             },
+            "description": "Monthly summaries of simulated watershed responses to mid-century climate change scenarios in 5 U.S. basins. \n\nThis dataset is associated with the following publication:\nNover, D., J. Witt , J. Butcher, T. Johnson , and C. Weaver. The Effects of Downscaling Method on the Variability of Simulated Watershed Response to Climate Change in Five U.S. Basins.   Earth Interactions. American Meteorological Society, Boston, MA, USA, 20, 1-27, (2016).",
             "distribution": [
                 {
-                    "title": "ACF River.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390087/ACF%20River.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ACF River.xlsx"
                 },
                 {
-                    "title": "Minnesota River.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390087/Minnesota%20River.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Minnesota River.xlsx"
                 },
                 {
-                    "title": "Salt River.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390087/Salt%20River.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Salt River.xlsx"
                 },
                 {
-                    "title": "Susquehanna River.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390087/Susquehanna%20River.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Susquehanna River.xlsx"
                 },
                 {
-                    "title": "Willamette River.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390087/Willamette%20River.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Willamette River.xlsx"
                 }
             ],
-            "modified": "2016-01-04",
-            "references": [
-                "https://doi.org/10.1175/ei-d-15-0024.1"
+            "identifier": "https://doi.org/10.23719/1390087",
+            "keyword": [
+                "climate change streamflow water quality downscaling",
+                "climate",
+                "change",
+                "downscaling",
+                "method"
             ],
-            "publisher": {
-                "name": "U.S. EPA Office of Research and Development (ORD)",
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
+            "modified": "2016-01-04",
+            "programCode": [
+                "020:000"
+            ],
+            "publisher": {
+                "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
                     "name": "U.S. Environmental Protection Agency",
                     "subOrganizationOf": {
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1175/ei-d-15-0024.1"
+            ],
+            "rights": null,
+            "title": "Supporting Simulation Output - Earth Interactions article \"The Effects of Downscaling Method on the Variability of Simulated Watershed Response to Climate Change in Five U.S. Basins\""
         },
         {
-            "title": "A small, lightweight multipollutant sensor system for ground-mobile and aerial emission sampling from open area sources",
-            "description": "Emission data from UAV flights. \n\nThis dataset is associated with the following publication:\nZhou, X., J. Aurell, B. Mitchell, D. Tabor, and B. Gullett. A small, lightweight multipollutant sensor system for ground-mobile and aerial emission sampling from open area sources.   JOURNAL OF AIR AND WASTE MANAGEMENT. Air & Waste Management Association, Pittsburgh, PA, USA, 154: 31-41, (2017).",
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
+            "description": "Emission data from UAV flights. \n\nThis dataset is associated with the following publication:\nZhou, X., J. Aurell, B. Mitchell, D. Tabor, and B. Gullett. A small, lightweight multipollutant sensor system for ground-mobile and aerial emission sampling from open area sources.   JOURNAL OF AIR AND WASTE MANAGEMENT. Air & Waste Management Association, Pittsburgh, PA, USA, 154: 31-41, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390075/Data%20Table%20for%20Science%20Hub%20Zhou%20paper%20Gullett.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Table for Science Hub Zhou paper Gullett.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1390075",
             "keyword": [
@@ -70505,20 +70509,10 @@
                 "unmanned aerial vehicles",
                 "aerostats"
             ],
-            "contactPoint": {
-                "fn": "Brian Gullett",
-                "hasEmail": "mailto:gullett.brian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data Table for Science Hub Zhou paper Gullett.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390075/Data%20Table%20for%20Science%20Hub%20Zhou%20paper%20Gullett.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-08",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.01.029"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70528,42 +70522,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2017.01.029"
+            ],
+            "rights": null,
+            "title": "A small, lightweight multipollutant sensor system for ground-mobile and aerial emission sampling from open area sources"
         },
         {
-            "title": "Aerial sampling of emissions from biomass pile burns in Oregon",
-            "description": "Emissions from burning slash biomass piles in western Oregon. \n\nThis dataset is associated with the following publication:\nAurell, J., B. Gullett, D. Tabor, and N. Yonker. Emissions from  prescribed burning of timber slash piles in Oregon..   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 150: 395-406, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1390074",
-            "keyword": [
-                "emission factors",
-                "timber slash",
-                "pile cover",
-                "moisture",
-                "polyethylene"
-            ],
             "contactPoint": {
                 "fn": "Brian Gullett",
                 "hasEmail": "mailto:gullett.brian@epa.gov"
             },
+            "description": "Emissions from burning slash biomass piles in western Oregon. \n\nThis dataset is associated with the following publication:\nAurell, J., B. Gullett, D. Tabor, and N. Yonker. Emissions from  prescribed burning of timber slash piles in Oregon..   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 150: 395-406, (2017).",
             "distribution": [
                 {
-                    "title": "Data Table Science Hub Oregon 07-25-2016 JA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390074/Data%20Table%20Science%20Hub%20Oregon%2007-25-2016%20JA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data Table Science Hub Oregon 07-25-2016 JA.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390074",
+            "keyword": [
+                "emission factors",
+                "timber slash",
+                "pile cover",
+                "moisture",
+                "polyethylene"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-25",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2016.11.034"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70573,19 +70567,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2016.11.034"
+            ],
+            "rights": null,
+            "title": "Aerial sampling of emissions from biomass pile burns in Oregon"
         },
         {
-            "title": "LakeCat",
-            "description": "The LakeCat Dataset provides summaries of watershed features for 378,088 lakes within the conterminous USA and provides several hundred watershed-level metrics that summarize both natural (e.g., soils, geology, climate, and land cover) and anthropogenic (e.g., urbanization,\nagriculture, and mines) features. \n\nThis dataset is associated with the following publication:\nHill, R., M. Weber, R. Debbout, S. Leibowitz, and T. Olsen. The Lake-Catchment (LakeCat) Dataset: Characterizing landscape features for lake basins within the conterminous USA.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  37: 208-221, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Scott Leibowitz",
+                "hasEmail": "mailto:leibowitz.scott@epa.gov"
+            },
+            "describedBy": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/LakeCat/Documentation/DataDictionary.html",
+            "description": "The LakeCat Dataset provides summaries of watershed features for 378,088 lakes within the conterminous USA and provides several hundred watershed-level metrics that summarize both natural (e.g., soils, geology, climate, and land cover) and anthropogenic (e.g., urbanization,\nagriculture, and mines) features. \n\nThis dataset is associated with the following publication:\nHill, R., M. Weber, R. Debbout, S. Leibowitz, and T. Olsen. The Lake-Catchment (LakeCat) Dataset: Characterizing landscape features for lake basins within the conterminous USA.   Freshwater Science. The Society for Freshwater Science, Springfield, IL,  37: 208-221, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500884",
             "keyword": [
@@ -70600,19 +70604,10 @@
                 "aquatic condition",
                 "National Aquatic Resource Surveys"
             ],
-            "contactPoint": {
-                "fn": "Scott Leibowitz",
-                "hasEmail": "mailto:leibowitz.scott@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-11",
-            "references": [
-                "https://doi.org/10.1086/697966"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70623,40 +70618,39 @@
                     }
                 }
             },
-            "describedBy": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/LakeCat/Documentation/DataDictionary.html"
+            "references": [
+                "https://doi.org/10.1086/697966"
+            ],
+            "rights": null,
+            "title": "LakeCat"
         },
         {
-            "title": "in vitro and microsome experiment data",
-            "description": "exposure_experiment.csv: \r\ntime: length of time that amphibian was exposed to that pesticide in hours.  \r\nparent: is the active ingredient that the amphibian was exposed to.  \r\nanalyte: either the main parent compound or the metabolite that was quantified.  \r\nmatrix: the sample that was analyzed either the amphibian or soil.  \r\nconc: is the concentration for that specific analyte in that matrix for that specific species in microg/g\r\nreplicate: is the individual amphibian or soil exposed to that pesticide.\r\n\r\nmicrosome_experiment3.csv:  \r\ntime: is the length of time that the microsomes were exposed before being quenched in minutes.  \r\nparent: is the active ingredient that the amphibian was exposed to.  \r\nanalyte: either the main parent compound or the metabolite that was quantified.  \r\nmatrix: the sample that was analyzed microsomes.  \r\nconc: is the concentration for that specific analyte in that matrix for that specific species.  in micromolar (uM)\r\nreplicate: is the individual microsome exposed to that pesticide. \r\nmicroMexp: is the concentration in micromolar (uM) that the microsomes were exposed to for that pesticide. \n\nThis dataset is associated with the following publication:\nGlinski, D., M. Henderson, R. Van Meter, and T. Purucker. Using in vitro derived enzymatic reaction rates of metabolism to inform pesticide body burdens in amphibians.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 288: 9-16, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1407588",
-            "keyword": [
-                "microsomes",
-                "Metabolism",
-                "pesticides",
-                "amphibians"
-            ],
             "contactPoint": {
                 "fn": "Steven Purucker",
                 "hasEmail": "mailto:purucker.tom@epa.gov"
             },
+            "description": "exposure_experiment.csv: \r\ntime: length of time that amphibian was exposed to that pesticide in hours.  \r\nparent: is the active ingredient that the amphibian was exposed to.  \r\nanalyte: either the main parent compound or the metabolite that was quantified.  \r\nmatrix: the sample that was analyzed either the amphibian or soil.  \r\nconc: is the concentration for that specific analyte in that matrix for that specific species in microg/g\r\nreplicate: is the individual amphibian or soil exposed to that pesticide.\r\n\r\nmicrosome_experiment3.csv:  \r\ntime: is the length of time that the microsomes were exposed before being quenched in minutes.  \r\nparent: is the active ingredient that the amphibian was exposed to.  \r\nanalyte: either the main parent compound or the metabolite that was quantified.  \r\nmatrix: the sample that was analyzed microsomes.  \r\nconc: is the concentration for that specific analyte in that matrix for that specific species.  in micromolar (uM)\r\nreplicate: is the individual microsome exposed to that pesticide. \r\nmicroMexp: is the concentration in micromolar (uM) that the microsomes were exposed to for that pesticide. \n\nThis dataset is associated with the following publication:\nGlinski, D., M. Henderson, R. Van Meter, and T. Purucker. Using in vitro derived enzymatic reaction rates of metabolism to inform pesticide body burdens in amphibians.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 288: 9-16, (2018).",
             "distribution": [
                 {
-                    "title": "https://zenodo.org/record/837834#.WYD9BfnythE",
-                    "accessURL": "https://zenodo.org/record/837834#.WYD9BfnythE"
+                    "accessURL": "https://zenodo.org/record/837834#.WYD9BfnythE",
+                    "title": "https://zenodo.org/record/837834#.WYD9BfnythE"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407588",
+            "keyword": [
+                "microsomes",
+                "Metabolism",
+                "pesticides",
+                "amphibians"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-12",
-            "references": [
-                "https://doi.org/10.1016/j.toxlet.2018.02.016"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70666,47 +70660,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.toxlet.2018.02.016"
+            ],
+            "rights": null,
+            "title": "in vitro and microsome experiment data"
         },
         {
-            "title": "Adverse Outcome Pathway Networks I: Development and Applications",
-            "description": "In September, 2015, a water sample was collected downstream of a major metropolitan waste water treatment plant that discharges to the South Platte River, Colorado, USA. The grab sample, 1L, was collected just below the water surface, directly into a pre-cleaned, organic-free, amber glass bottle. The water sample was extracted by solid phase extraction using an Oasis-HLB glass catridge. Cartidges were conditioned sequentially using 5mL each of ethyl acetate, 50:50 methanol (MeOH):dichloromethane (DCM), MeOH, and water. The extract in DMSO was tested in the Attagene cis- and trans-FactorialTM assays (http://www.attagene.com/technology.php; Martin and others 2010; Romanov and others 2008). Data were analyzed using an established analysis pipeline for analyzing ToxCast\u2122 high throughput screening data (Filer and others 2017). \"Active hits\" in the Attagene assay are included in the data table. \n\nThis dataset is associated with the following publication:\nKnapen, D., M. Angrish, M. Fortin, I. Katsiadaki, M. Leonard, L. Mariotta-Casaluci, S. Munn, J. O'Brien, N. Pollesch, L.C. Smith, X. Zhang, and D. Villeneuve. Adverse outcome pathway networks I: Development and applications.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 37(6): 1723-1733, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1423303",
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
+            "description": "In September, 2015, a water sample was collected downstream of a major metropolitan waste water treatment plant that discharges to the South Platte River, Colorado, USA. The grab sample, 1L, was collected just below the water surface, directly into a pre-cleaned, organic-free, amber glass bottle. The water sample was extracted by solid phase extraction using an Oasis-HLB glass catridge. Cartidges were conditioned sequentially using 5mL each of ethyl acetate, 50:50 methanol (MeOH):dichloromethane (DCM), MeOH, and water. The extract in DMSO was tested in the Attagene cis- and trans-FactorialTM assays (http://www.attagene.com/technology.php; Martin and others 2010; Romanov and others 2008). Data were analyzed using an established analysis pipeline for analyzing ToxCast\u2122 high throughput screening data (Filer and others 2017). \"Active hits\" in the Attagene assay are included in the data table. \n\nThis dataset is associated with the following publication:\nKnapen, D., M. Angrish, M. Fortin, I. Katsiadaki, M. Leonard, L. Mariotta-Casaluci, S. Munn, J. O'Brien, N. Pollesch, L.C. Smith, X. Zhang, and D. Villeneuve. Adverse outcome pathway networks I: Development and applications.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 37(6): 1723-1733, (2018).",
             "distribution": [
                 {
-                    "title": "WG1-paper-1-supplementary-2018-02-08.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1423303/WG1-paper-1-supplementary-2018-02-08.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "WG1-paper-1-supplementary-2018-02-08.docx"
                 },
                 {
-                    "title": "Attagene SP 2014-15_ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1423303/Attagene%20SP%202014-15_ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Attagene SP 2014-15_ScienceHub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1423303",
+            "keyword": [
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "endocrine disruption",
+                "screening and prioritization",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-01",
-            "references": [
-                "https://doi.org/10.1002/etc.4125"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70716,51 +70710,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4125"
+            ],
+            "rights": null,
+            "title": "Adverse Outcome Pathway Networks I: Development and Applications"
         },
         {
-            "title": "Adverse Outcome Pathway Networks II: Network Analytics",
-            "description": "The data set provides a set of txt files and cytoscape files that were used to construct the example AOP networks included in the paper. Additionally, a supplementary table file provides all the network statistics discussed in the manuscript (e.g., node degree calculations, betweenness centrality, eccentricity, etc.). \n\nThis dataset is associated with the following publication:\nVilleneuve, D., M. Angrish, M. Fortin, I. Katsiadaki, M. Leonard, L. Margiotta-Casaluci, S. Munn, J. O'Brien, N. Pollesch, C. Smith, X. Zhang, and D. Knapen. Adverse outcome pathway networks II: Network analytics.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 37(6): 1734-1748, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1430043",
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
+            "description": "The data set provides a set of txt files and cytoscape files that were used to construct the example AOP networks included in the paper. Additionally, a supplementary table file provides all the network statistics discussed in the manuscript (e.g., node degree calculations, betweenness centrality, eccentricity, etc.). \n\nThis dataset is associated with the following publication:\nVilleneuve, D., M. Angrish, M. Fortin, I. Katsiadaki, M. Leonard, L. Margiotta-Casaluci, S. Munn, J. O'Brien, N. Pollesch, C. Smith, X. Zhang, and D. Knapen. Adverse outcome pathway networks II: Network analytics.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 37(6): 1734-1748, (2018).",
             "distribution": [
                 {
-                    "title": "https://setac.onlinelibrary.wiley.com/doi/abs/10.1002/etc.4124",
-                    "accessURL": "https://setac.onlinelibrary.wiley.com/doi/abs/10.1002/etc.4124"
+                    "accessURL": "https://setac.onlinelibrary.wiley.com/doi/abs/10.1002/etc.4124",
+                    "title": "https://setac.onlinelibrary.wiley.com/doi/abs/10.1002/etc.4124"
                 },
                 {
-                    "title": "Networkfiles.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430043/Networkfiles.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Networkfiles.zip"
                 },
                 {
-                    "title": "Part-II-supplementary-tables_for submissioin.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1430043/Part-II-supplementary-tables_for%20submissioin.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Part-II-supplementary-tables_for submissioin.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1430043",
+            "keyword": [
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "endocrine disruption",
+                "screening and prioritization",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-28",
-            "references": [
-                "https://doi.org/10.1002/etc.4124"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70770,49 +70764,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.4124"
+            ],
+            "rights": null,
+            "title": "Adverse Outcome Pathway Networks II: Network Analytics"
         },
         {
-            "title": "Self-Cleaning Carbon Nanotube Membranes for Water Purification-confocal microscope pitures and slide preparation procedures",
-            "description": "The pictures in the power point file were taken using a confocal microscope with green and red filters which represent viable and dead bacteria cells, respectively. Additionally, we provided the detailed procedures of bacteria propagation and viability staining in a MS word file. The data may provide background/supporting information for other researchers who are planning to perform for microscopic bacteria viability assays. \n\nThis dataset is associated with the following publication:\nAlvarez, N., R. Noga, S. Chae, G. Sorial, H. Ryu, and V. Shanov. Heatable carbon nanotube composite membranes for sustainable recovery from biofouling.   Biofouling. Taylor & Francis Group, London,  UK, 33(10): 847-854, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1378446",
-            "keyword": [
-                "carbon nanotubes",
-                "drawable and spinnable CNT",
-                "membranes",
-                "ohmic heating",
-                "biofouling",
-                "water and wastewater treatment",
-                "Escherichia coli."
-            ],
             "contactPoint": {
                 "fn": "Hodon Ryu",
                 "hasEmail": "mailto:ryu.hodon@epa.gov"
             },
+            "description": "The pictures in the power point file were taken using a confocal microscope with green and red filters which represent viable and dead bacteria cells, respectively. Additionally, we provided the detailed procedures of bacteria propagation and viability staining in a MS word file. The data may provide background/supporting information for other researchers who are planning to perform for microscopic bacteria viability assays. \n\nThis dataset is associated with the following publication:\nAlvarez, N., R. Noga, S. Chae, G. Sorial, H. Ryu, and V. Shanov. Heatable carbon nanotube composite membranes for sustainable recovery from biofouling.   Biofouling. Taylor & Francis Group, London,  UK, 33(10): 847-854, (2017).",
             "distribution": [
                 {
-                    "title": "Results (Sep 23, 2016) (revised).pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378446/Results%20%28Sep%2023%2C%202016%29%20%28revised%29.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Results (Sep 23, 2016) (revised).pdf"
                 },
                 {
-                    "title": "Bacteria propagation and staining.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378446/Bacteria%20propagation%20and%20staining.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Bacteria propagation and staining.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1378446",
+            "keyword": [
+                "carbon nanotubes",
+                "drawable and spinnable CNT",
+                "membranes",
+                "ohmic heating",
+                "biofouling",
+                "water and wastewater treatment",
+                "Escherichia coli."
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-05",
-            "references": [
-                "https://doi.org/10.1080/08927014.2017.1376322"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70822,46 +70816,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08927014.2017.1376322"
+            ],
+            "rights": null,
+            "title": "Self-Cleaning Carbon Nanotube Membranes for Water Purification-confocal microscope pitures and slide preparation procedures"
         },
         {
-            "title": "Taxonomic summary tables for illumina sequences from MEC study on influence of electrical conductivity by microbial activity in biofilm anode",
-            "description": "This study assessed the conductivity of a Geobacter-enriched biofilm anode along with biofilm activity in a microbial electrochemical cell (MxC) equipped with two gold anodes (25 mM acetate medium), as different proton gradients were built throughout the biofilm. There was no pH gradient across the biofilm anode at 100 mM phosphate buffer (current density 2.38 A/m2) and biofilm conductivity (Kbio) was as high as 0.87 mS/cm. In comparison, an inner biofilm became acidic at 2.5 mM phosphate buffer in which approximately 80 \u03bcm of the inner biofilm anode was metabolically inactive. At this low phosphate buffer, Kbio significantly decreased by 0.27 mS/cm, together with declined current density of 0.64 A/m2. This work demonstrates that biofilm conductivity depends on metabolic activity of Geobacter in the conductive biofilm anode. The decreased Kbio at acidic environment implies the presence of multiple conduction-EET pathways in the biofilm anode. \n\nThis dataset is associated with the following publication:\nDhar, B., J. Sim, H. Ryu, H. Ren, J. Santodomingo, J. Chae, and H. Lee. Microbial Activity Influences Electrical Conductivity of Biofilm Anode.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 127: 230-238, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1379483",
-            "keyword": [
-                "Microbial electrochemical cell",
-                "Electrical conductivity",
-                "Biofilm anode",
-                "Geobacter"
-            ],
             "contactPoint": {
                 "fn": "Hodon Ryu",
                 "hasEmail": "mailto:ryu.hodon@epa.gov"
             },
+            "description": "This study assessed the conductivity of a Geobacter-enriched biofilm anode along with biofilm activity in a microbial electrochemical cell (MxC) equipped with two gold anodes (25 mM acetate medium), as different proton gradients were built throughout the biofilm. There was no pH gradient across the biofilm anode at 100 mM phosphate buffer (current density 2.38 A/m2) and biofilm conductivity (Kbio) was as high as 0.87 mS/cm. In comparison, an inner biofilm became acidic at 2.5 mM phosphate buffer in which approximately 80 \u03bcm of the inner biofilm anode was metabolically inactive. At this low phosphate buffer, Kbio significantly decreased by 0.27 mS/cm, together with declined current density of 0.64 A/m2. This work demonstrates that biofilm conductivity depends on metabolic activity of Geobacter in the conductive biofilm anode. The decreased Kbio at acidic environment implies the presence of multiple conduction-EET pathways in the biofilm anode. \n\nThis dataset is associated with the following publication:\nDhar, B., J. Sim, H. Ryu, H. Ren, J. Santodomingo, J. Chae, and H. Lee. Microbial Activity Influences Electrical Conductivity of Biofilm Anode.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 127: 230-238, (2017).",
             "distribution": [
                 {
-                    "title": "MEC-microbial activity_pH-MMXC_Illumina results_tables.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1379483/MEC-microbial%20activity_pH-MMXC_Illumina%20results_tables.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "MEC-microbial activity_pH-MMXC_Illumina results_tables.docx"
                 },
                 {
-                    "title": "MEC-microbial activity_pH-MMXC_taxonomy summary.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1379483/MEC-microbial%20activity_pH-MMXC_taxonomy%20summary.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "MEC-microbial activity_pH-MMXC_taxonomy summary.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1379483",
+            "keyword": [
+                "Microbial electrochemical cell",
+                "Electrical conductivity",
+                "Biofilm anode",
+                "Geobacter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-06",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2017.10.028"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70871,40 +70865,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2017.10.028"
+            ],
+            "rights": null,
+            "title": "Taxonomic summary tables for illumina sequences from MEC study on influence of electrical conductivity by microbial activity in biofilm anode"
         },
         {
-            "title": "Integrated cell culture RT quantitative PCR and UV disinfection dataset",
-            "description": "This dataset includes the standard curves for ICCRTqPCR to convert the assay quantities to the concentrations of infectious viruses and all the calculations on inactivation rate constants. Also, all the figures used in the manuscripts are presented. \n\nThis dataset is associated with the following publication:\nRyu, H., K. Schrantz, N. Brinkman, and L. Boczek. Applicability of integrated cell culture reverse transcriptase quantitative PCR (ICC-RTqPCR) for the simultaneous detection of the four human enteric enterovirus species in disinfection studies.   JOURNAL OF VIROLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 258: 35-40, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1422043",
-            "keyword": [
-                "multiplex integrated cell culture quantitative PCR",
-                "enteroviruses",
-                "UV disinfection"
-            ],
             "contactPoint": {
                 "fn": "Hodon Ryu",
                 "hasEmail": "mailto:ryu.hodon@epa.gov"
             },
+            "description": "This dataset includes the standard curves for ICCRTqPCR to convert the assay quantities to the concentrations of infectious viruses and all the calculations on inactivation rate constants. Also, all the figures used in the manuscripts are presented. \n\nThis dataset is associated with the following publication:\nRyu, H., K. Schrantz, N. Brinkman, and L. Boczek. Applicability of integrated cell culture reverse transcriptase quantitative PCR (ICC-RTqPCR) for the simultaneous detection of the four human enteric enterovirus species in disinfection studies.   JOURNAL OF VIROLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 258: 35-40, (2018).",
             "distribution": [
                 {
-                    "title": "ICCRTqPCR_Enterovirus_UV.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1422043/ICCRTqPCR_Enterovirus_UV.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ICCRTqPCR_Enterovirus_UV.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1422043",
+            "keyword": [
+                "multiplex integrated cell culture quantitative PCR",
+                "enteroviruses",
+                "UV disinfection"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-06",
-            "references": [
-                "https://doi.org/10.1016/j.jviromet.2018.05.008"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70914,47 +70908,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jviromet.2018.05.008"
+            ],
+            "rights": null,
+            "title": "Integrated cell culture RT quantitative PCR and UV disinfection dataset"
         },
         {
-            "title": "HTMLS of Spatial Stream Network Modeling to Predict Total Phosphorus Concentration in the East Fork of the Little Miami River, Ohio",
-            "description": "These files contain data for relating stream total phosphorus concentration, a nutrient, to land cover and land use variables in the East Fork of the Little Miami River watershed near Cincinnati, Ohio.  Water quality grab samples were collected from June 26, 2012 to September 11, 2012, and total phosphorus concentrations were measured on those samples.  The files in the jawr12543-sup-002-R_code_and outputs folder are htmls, which can be opened with any browser to view the data and work flow of the data analysis.  The files in the jawr12543-sup-003-SSN_file_objects contains the dataset as an R object, which can be opened in the open-source R software. \n\nThis dataset is associated with the following publication:\nScown, M., M. McManus, J. Carson, and C. Nietch. Improving predictive models of in-stream phosphorus based on nationally-available spatial data coverages in a Southwestern Ohio watershed.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA, 53(4): 944-960, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1415037",
-            "keyword": [
-                "spatial data",
-                "stream networks",
-                "spatial statistical network model",
-                "phosphorus",
-                "spatial autocorrelation"
-            ],
             "contactPoint": {
                 "fn": "Michael McManus",
                 "hasEmail": "mailto:mcmanus.michael@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1415037/documents/DataDictionary_SpatialStreamNetworkModeling_EastForkLittleMiamiRiver.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "These files contain data for relating stream total phosphorus concentration, a nutrient, to land cover and land use variables in the East Fork of the Little Miami River watershed near Cincinnati, Ohio.  Water quality grab samples were collected from June 26, 2012 to September 11, 2012, and total phosphorus concentrations were measured on those samples.  The files in the jawr12543-sup-002-R_code_and outputs folder are htmls, which can be opened with any browser to view the data and work flow of the data analysis.  The files in the jawr12543-sup-003-SSN_file_objects contains the dataset as an R object, which can be opened in the open-source R software. \n\nThis dataset is associated with the following publication:\nScown, M., M. McManus, J. Carson, and C. Nietch. Improving predictive models of in-stream phosphorus based on nationally-available spatial data coverages in a Southwestern Ohio watershed.   JOURNAL OF THE AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA, 53(4): 944-960, (2017).",
             "distribution": [
                 {
-                    "title": "jawr12543-sup-0002-R_code_and_outputs.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1415037/jawr12543-sup-0002-R_code_and_outputs.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "jawr12543-sup-0002-R_code_and_outputs.zip"
                 },
                 {
-                    "title": "jawr12543-sup-0003-SSN_file_objects.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1415037/jawr12543-sup-0003-SSN_file_objects.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "jawr12543-sup-0003-SSN_file_objects.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1415037",
+            "keyword": [
+                "spatial data",
+                "stream networks",
+                "spatial statistical network model",
+                "phosphorus",
+                "spatial autocorrelation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-01-26",
-            "references": [
-                "https://doi.org/10.1111/1752-1688.12543"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -70965,43 +70961,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1415037/documents/DataDictionary_SpatialStreamNetworkModeling_EastForkLittleMiamiRiver.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1111/1752-1688.12543"
+            ],
+            "rights": null,
+            "title": "HTMLS of Spatial Stream Network Modeling to Predict Total Phosphorus Concentration in the East Fork of the Little Miami River, Ohio"
         },
         {
-            "title": "Supplementary Material for \"The Effects of Source Water Quality on Drinking Water Treatment Costs: A Review and Synthesis of Empirical Literature\"",
-            "description": "Characteristics of 24 studies that model drinking water treatment costs to source water quality. \n\nThis dataset is associated with the following publication:\nPrice, J., and M. Heberling. The Effects of Source Water Quality on Drinking Water Treatment Costs: A Review and Synthesis of Empirical Literature - Ecological Economics.   ECOLOGICAL ECONOMICS. Elsevier Science Ltd, New York, NY, USA, 151: 195-209, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407619",
-            "keyword": [
-                "literature review",
-                "source water protection",
-                "drinking water",
-                "treatment costs",
-                "economics"
-            ],
             "contactPoint": {
                 "fn": "Matthew Heberling",
                 "hasEmail": "mailto:heberling.matt@epa.gov"
             },
+            "description": "Characteristics of 24 studies that model drinking water treatment costs to source water quality. \n\nThis dataset is associated with the following publication:\nPrice, J., and M. Heberling. The Effects of Source Water Quality on Drinking Water Treatment Costs: A Review and Synthesis of Empirical Literature - Ecological Economics.   ECOLOGICAL ECONOMICS. Elsevier Science Ltd, New York, NY, USA, 151: 195-209, (2018).",
             "distribution": [
                 {
-                    "title": "TreatmentCosts&WQReview_SupplementaryMaterial.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407619/TreatmentCosts%26WQReview_SupplementaryMaterial.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TreatmentCosts&WQReview_SupplementaryMaterial.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407619",
+            "keyword": [
+                "literature review",
+                "source water protection",
+                "drinking water",
+                "treatment costs",
+                "economics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-23",
-            "references": [
-                "https://doi.org/10.1016/j.ecolecon.2018.04.014"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71011,42 +71005,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolecon.2018.04.014"
+            ],
+            "rights": null,
+            "title": "Supplementary Material for \"The Effects of Source Water Quality on Drinking Water Treatment Costs: A Review and Synthesis of Empirical Literature\""
         },
         {
-            "title": "Data for a PPAR-alpha dependence of developmental effects of PFNA in mouse.",
-            "description": "Perfluorononanoic acid (PFNA) is one of the perfluoroalkyl acids found in the environment and in tissues of humans and wildlife. Prenatal exposure to PFNA negatively impacts survival and development of mice and activates the mouse and human peroxisome proliferator-activated receptor-alpha (PPAR\u03b1). In the current study, we used PPAR\u03b1 knockout (KO) and 129S1/SvlmJ wild-type (WT) mice to investigate the role of PPAR\u03b1 in mediating PFNA-induced in vivo effects. Pregnant KO and WT mice were dosed orally with water (vehicle control: 10 ml/kg), 0.83, 1.1, 1.5, or 2mg/kg PFNA on gestational days (GDs) 1\u221218 (day of sperm plug = GD 0). Maternal weight gain, implantation, litter size, and pup weight at birth were unaffected in either strain. PFNA exposure reduced the number of live pups at birth and survival of offspring to weaning in the 1.1 and 2 mg/kg groups in WT. Eye opening was delayed (mean delay 2.1 days) and pup weight at weaning was reduced inWT pups at 2mg/kg. These developmental endpoints were not affected in the KO. Relative liver weight was increased in a dose-dependent manner in dams and pups of theWT strain at all dose levels but only slightly increased in the highest dose group in the KO strain. In summary, PFNA altered liver weight of dams and pups, pup survival, body weight, and development in the WT, while only inducing a slight increase in relative liver weight of dams and pups at 2mg/kg in KO mice. These results suggest that PPAR\u03b1 is an essential mediator of PFNA-induced developmental toxicity in the mouse. \n\nThis dataset is associated with the following publication:\nAbbott, B., C. Wolf, J. Schmid, C. Lau, and R. Zehr. Developmental Effects of Perfluorononanoic Acid in the Mouse Are Dependent on Peroxisome Proliferator-Activated Receptor-alpha..   PPAR research. Hindawi Publishing Corporation, New York, NY, USA,  1-11, (2010).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1435034",
-            "keyword": [
-                "Developmental Toxicity",
-                "PPAR-alpha",
-                "PFNA",
-                "PFAA",
-                "perfluoroalkyl acids"
-            ],
             "contactPoint": {
                 "fn": "Barbara Abbott",
                 "hasEmail": "mailto:abbott.barbara@epa.gov"
             },
+            "description": "Perfluorononanoic acid (PFNA) is one of the perfluoroalkyl acids found in the environment and in tissues of humans and wildlife. Prenatal exposure to PFNA negatively impacts survival and development of mice and activates the mouse and human peroxisome proliferator-activated receptor-alpha (PPAR\u03b1). In the current study, we used PPAR\u03b1 knockout (KO) and 129S1/SvlmJ wild-type (WT) mice to investigate the role of PPAR\u03b1 in mediating PFNA-induced in vivo effects. Pregnant KO and WT mice were dosed orally with water (vehicle control: 10 ml/kg), 0.83, 1.1, 1.5, or 2mg/kg PFNA on gestational days (GDs) 1\u221218 (day of sperm plug = GD 0). Maternal weight gain, implantation, litter size, and pup weight at birth were unaffected in either strain. PFNA exposure reduced the number of live pups at birth and survival of offspring to weaning in the 1.1 and 2 mg/kg groups in WT. Eye opening was delayed (mean delay 2.1 days) and pup weight at weaning was reduced inWT pups at 2mg/kg. These developmental endpoints were not affected in the KO. Relative liver weight was increased in a dose-dependent manner in dams and pups of theWT strain at all dose levels but only slightly increased in the highest dose group in the KO strain. In summary, PFNA altered liver weight of dams and pups, pup survival, body weight, and development in the WT, while only inducing a slight increase in relative liver weight of dams and pups at 2mg/kg in KO mice. These results suggest that PPAR\u03b1 is an essential mediator of PFNA-induced developmental toxicity in the mouse. \n\nThis dataset is associated with the following publication:\nAbbott, B., C. Wolf, J. Schmid, C. Lau, and R. Zehr. Developmental Effects of Perfluorononanoic Acid in the Mouse Are Dependent on Peroxisome Proliferator-Activated Receptor-alpha..   PPAR research. Hindawi Publishing Corporation, New York, NY, USA,  1-11, (2010).",
             "distribution": [
                 {
-                    "title": "Wolf et al 2010 SciHub Data Set.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435034/Wolf%20et%20al%202010%20SciHub%20Data%20Set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Wolf et al 2010 SciHub Data Set.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435034",
+            "keyword": [
+                "Developmental Toxicity",
+                "PPAR-alpha",
+                "PFNA",
+                "PFAA",
+                "perfluoroalkyl acids"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2010-03-17",
-            "references": [
-                "https://doi.org/10.1155/2010/282896"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71056,49 +71050,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1155/2010/282896"
+            ],
+            "rights": null,
+            "title": "Data for a PPAR-alpha dependence of developmental effects of PFNA in mouse."
         },
         {
-            "title": "Environmental Monitoring and Assessment Program (1990-1998), National Coastal Assessment (2000-2006), National Aquatic Resource Surveys (2000-2015)",
-            "description": "These data are from EPA's national coastal monitoring programs and include data from the water column, sediments, and biota, 1990-2015. \n\nThis dataset is associated with the following publication:\nHale, S., H. Buffum, J. Kiddon, and M. Hughes. Subtidal Benthic Invertebrates Shifting Northward Along the U.S. Atlantic Coast.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 40(6): 1744-1756, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500437",
-            "keyword": [
-                "benthic invertebrates",
-                "species\u2019 range shifts",
-                "U.S. Atlantic coast",
-                "Carolinian Biogeographic Province",
-                "Virginian Biogeographic Province"
-            ],
             "contactPoint": {
                 "fn": "Stephen Hale",
                 "hasEmail": "mailto:hale.stephen@epa.gov"
             },
+            "description": "These data are from EPA's national coastal monitoring programs and include data from the water column, sediments, and biota, 1990-2015. \n\nThis dataset is associated with the following publication:\nHale, S., H. Buffum, J. Kiddon, and M. Hughes. Subtidal Benthic Invertebrates Shifting Northward Along the U.S. Atlantic Coast.   Estuaries and Coasts. Estuarine Research Federation, Port Republic, MD, USA, 40(6): 1744-1756, (2017).",
             "distribution": [
                 {
-                    "title": "https://archive.epa.gov/emap/archive-emap/web/html/index-21.html",
-                    "accessURL": "https://archive.epa.gov/emap/archive-emap/web/html/index-21.html"
+                    "accessURL": "https://archive.epa.gov/emap/archive-emap/web/html/index-21.html",
+                    "title": "https://archive.epa.gov/emap/archive-emap/web/html/index-21.html"
                 },
                 {
-                    "title": "https://archive.epa.gov/emap/archive-emap/web/html/index-124.html",
-                    "accessURL": "https://archive.epa.gov/emap/archive-emap/web/html/index-124.html"
+                    "accessURL": "https://archive.epa.gov/emap/archive-emap/web/html/index-124.html",
+                    "title": "https://archive.epa.gov/emap/archive-emap/web/html/index-124.html"
                 },
                 {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500437",
+            "keyword": [
+                "benthic invertebrates",
+                "species\u2019 range shifts",
+                "U.S. Atlantic coast",
+                "Carolinian Biogeographic Province",
+                "Virginian Biogeographic Province"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-31",
-            "references": [
-                "https://doi.org/10.1007/s12237-017-0236-z"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71108,19 +71102,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12237-017-0236-z"
+            ],
+            "rights": null,
+            "title": "Environmental Monitoring and Assessment Program (1990-1998), National Coastal Assessment (2000-2006), National Aquatic Resource Surveys (2000-2015)"
         },
         {
-            "title": "Traffic Density Parameters",
-            "description": "The complete data sets and programs used for data analysis were combined into one zip file. \n\nThis dataset is associated with the following publication:\nLiu , S., J. Burke , F. Chen , and J. Xue. Evaluation of Traffic Density Parameters as an Indicator of Vehicle Emission-Related Near-Road Air Pollution: A Case Study with NEXUS Measurement Data on Black Carbon.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 14(12): 1581, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Shi Liu",
+                "hasEmail": "mailto:liu.shi@epa.gov"
+            },
+            "description": "The complete data sets and programs used for data analysis were combined into one zip file. \n\nThis dataset is associated with the following publication:\nLiu , S., J. Burke , F. Chen , and J. Xue. Evaluation of Traffic Density Parameters as an Indicator of Vehicle Emission-Related Near-Road Air Pollution: A Case Study with NEXUS Measurement Data on Black Carbon.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 14(12): 1581, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434295/Mj_nexus.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Mj_nexus.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1434295",
             "keyword": [
@@ -71132,20 +71136,10 @@
                 "Black Carbon",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Shi Liu",
-                "hasEmail": "mailto:liu.shi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Mj_nexus.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434295/Mj_nexus.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-29",
-            "references": [
-                "https://doi.org/10.3390/ijerph14121581"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71155,19 +71149,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/ijerph14121581"
+            ],
+            "rights": null,
+            "title": "Traffic Density Parameters"
         },
         {
-            "title": "On-road Emissions and Chemical Transformation of Nitrogen Oxides",
-            "description": "On-road chase and PEMS measurement data while following traffic.  Time-averaged to assess the emission rate of the followed vehicle, including the presence of a PEMS to measure direct tailpipe exhaust. \n\nThis dataset is associated with the following publication:\nSnow, R., J. Faircloth, R. Baldauf, B. Yand, M. Zhang, P. Deshmukh, and X. Zhang. On-road Emissions and Chemical Transformation of Nitrogen Oxides.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA,  22, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Richard Baldauf",
+                "hasEmail": "mailto:baldauf.richard@epa.gov"
+            },
+            "description": "On-road chase and PEMS measurement data while following traffic.  Time-averaged to assess the emission rate of the followed vehicle, including the presence of a PEMS to measure direct tailpipe exhaust. \n\nThis dataset is associated with the following publication:\nSnow, R., J. Faircloth, R. Baldauf, B. Yand, M. Zhang, P. Deshmukh, and X. Zhang. On-road Emissions and Chemical Transformation of Nitrogen Oxides.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA,  22, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407590/Figure2b_Right_Daytime%20East%20Dominated%20Wind%20Net%20NO2%20over%205%20ppb.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure2b_Right_Daytime East Dominated Wind Net NO2 over 5 ppb.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407590",
             "keyword": [
@@ -71178,20 +71182,10 @@
                 "emissions",
                 "on-road"
             ],
-            "contactPoint": {
-                "fn": "Richard Baldauf",
-                "hasEmail": "mailto:baldauf.richard@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Figure2b_Right_Daytime East Dominated Wind Net NO2 over 5 ppb.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407590/Figure2b_Right_Daytime%20East%20Dominated%20Wind%20Net%20NO2%20over%205%20ppb.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-07",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b05648"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71201,45 +71195,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b05648"
+            ],
+            "rights": null,
+            "title": "On-road Emissions and Chemical Transformation of Nitrogen Oxides"
         },
         {
-            "title": "Using methods development efforts ongoing within NRMRL, NERL, and Regional labs, the concentrations of polyfluorinated chemicals",
-            "description": "Concentrations of polyfluorinated chemicals in drinking water from homes. \n\nThis dataset is associated with the following publication:\nDasu, K., S. Nakayama, M. Yoshikane, M. Mills, J.M. Wright, and S. Ehrlich. An Ultra-Sensitive Method for the Analysis of Perfluorinated Alkyl Acids in Drinking Water using a Column Switching High-Performance Liquid Chromatography Tandem Mass Spectrometry.  M.C. Breadmore, J.G. Dorsey, P. Dugo, S. Fanali  JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1494: 46-54, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407671",
-            "keyword": [
-                "Column-switching HPLC",
-                "drinking water",
-                "Perfluorinated alkyl acids",
-                "Solid phase extraction"
-            ],
             "contactPoint": {
                 "fn": "Marc Mills",
                 "hasEmail": "mailto:mills.marc@epa.gov"
             },
+            "describedBy": "https://doi.org/10.1016/j.chroma.2017.03.006",
+            "description": "Concentrations of polyfluorinated chemicals in drinking water from homes. \n\nThis dataset is associated with the following publication:\nDasu, K., S. Nakayama, M. Yoshikane, M. Mills, J.M. Wright, and S. Ehrlich. An Ultra-Sensitive Method for the Analysis of Perfluorinated Alkyl Acids in Drinking Water using a Column Switching High-Performance Liquid Chromatography Tandem Mass Spectrometry.  M.C. Breadmore, J.G. Dorsey, P. Dugo, S. Fanali  JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1494: 46-54, (2017).",
             "distribution": [
                 {
-                    "title": "Mills Dasu et al Science hub data.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407671/Mills%20Dasu%20et%20al%20Science%20hub%20data.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Mills Dasu et al Science hub data.docx"
                 },
                 {
-                    "title": "https://doi.org/10.1016/j.chroma.2017.03.006",
-                    "accessURL": "https://doi.org/10.1016/j.chroma.2017.03.006"
+                    "accessURL": "https://doi.org/10.1016/j.chroma.2017.03.006",
+                    "title": "https://doi.org/10.1016/j.chroma.2017.03.006"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407671",
+            "keyword": [
+                "Column-switching HPLC",
+                "drinking water",
+                "Perfluorinated alkyl acids",
+                "Solid phase extraction"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-26",
-            "references": [
-                "https://doi.org/10.1016/j.chroma.2017.03.006"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71250,42 +71245,41 @@
                     }
                 }
             },
-            "describedBy": "https://doi.org/10.1016/j.chroma.2017.03.006"
+            "references": [
+                "https://doi.org/10.1016/j.chroma.2017.03.006"
+            ],
+            "rights": null,
+            "title": "Using methods development efforts ongoing within NRMRL, NERL, and Regional labs, the concentrations of polyfluorinated chemicals"
         },
         {
-            "title": "Wanjugi et al 2016_Data Set",
-            "description": "Decomposition data of bacterial and viral fecal indicators in common human pollution types. \n\nThis dataset is associated with the following publication:\nWanjugi, P., M. Sivaganesan, A. Korajkic, C. Kelty, B. McMinn, R. Ulrich, V. Harwood, and O. Shanks. Differential Decomposition of Bacterial and Viral Fecal Indicators in Common Human Pollution Types.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 105: 591-601, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407668",
-            "keyword": [
-                "human fecal pollution",
-                "water quality",
-                "qPCR",
-                "Microbial Source Tracking",
-                "coliphage"
-            ],
             "contactPoint": {
                 "fn": "Orin Shanks",
                 "hasEmail": "mailto:shanks.orin@epa.gov"
             },
+            "description": "Decomposition data of bacterial and viral fecal indicators in common human pollution types. \n\nThis dataset is associated with the following publication:\nWanjugi, P., M. Sivaganesan, A. Korajkic, C. Kelty, B. McMinn, R. Ulrich, V. Harwood, and O. Shanks. Differential Decomposition of Bacterial and Viral Fecal Indicators in Common Human Pollution Types.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 105: 591-601, (2016).",
             "distribution": [
                 {
-                    "title": "Wanjugi etal 2016_Data Set.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407668/Wanjugi%20etal%202016_Data%20Set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Wanjugi etal 2016_Data Set.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407668",
+            "keyword": [
+                "human fecal pollution",
+                "water quality",
+                "qPCR",
+                "Microbial Source Tracking",
+                "coliphage"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-05",
-            "references": [
-                "http://www.sciencedirect.com/science/article/pii/S0043135416307187"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71295,42 +71289,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.sciencedirect.com/science/article/pii/S0043135416307187"
+            ],
+            "rights": null,
+            "title": "Wanjugi et al 2016_Data Set"
         },
         {
-            "title": "Fort Riley Tensiometer Data",
-            "description": "Tensiometers were installed a various depths and distances to monitor soil moisture tension. The installation was used to monitor subsurface water flow patterns from the storage gallery under the permeable pavement site. \n\nThis dataset is associated with the following publication:\nRazzaghmanesh, M., and M. Borst. Monitoring the performance of urban green infrastructure using a tensiometer approach.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 651: 2535-2545, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500904",
-            "keyword": [
-                "Tensiometer",
-                "Exfiltration",
-                "sidewalls",
-                "permeable pavement",
-                "stormwater control"
-            ],
             "contactPoint": {
                 "fn": "Michael Borst",
                 "hasEmail": "mailto:borst.mike@epa.gov"
             },
+            "description": "Tensiometers were installed a various depths and distances to monitor soil moisture tension. The installation was used to monitor subsurface water flow patterns from the storage gallery under the permeable pavement site. \n\nThis dataset is associated with the following publication:\nRazzaghmanesh, M., and M. Borst. Monitoring the performance of urban green infrastructure using a tensiometer approach.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 651: 2535-2545, (2019).",
             "distribution": [
                 {
-                    "title": "Fort Riley Tensiometer Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500904/Fort%20Riley%20Tensiometer%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fort Riley Tensiometer Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500904",
+            "keyword": [
+                "Tensiometer",
+                "Exfiltration",
+                "sidewalls",
+                "permeable pavement",
+                "stormwater control"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-30",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2018.10.120"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71340,19 +71334,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2018.10.120"
+            ],
+            "rights": null,
+            "title": "Fort Riley Tensiometer Data"
         },
         {
-            "title": "Cylindrospermopsin 90-day oral route toxicology study",
-            "description": "General toxicology, clinical chemistry, complete blood counts, histopathology, gene expression. \n\nThis dataset is associated with the following publication:\nChernoff, N., D. Hill, I. Chorus, D. Diggs, H. Huang, D. King, J. Lang, T. Le, J. Schmid, G. Travlos, E. Whitley, R. Wilson, and C. Wood. Cylindrospermopsin toxicity in mice following a 90-d oral exposure.   ENVIRONMENTAL TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA,  549-566, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Neil Chernoff",
+                "hasEmail": "mailto:chernoff.neil@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1375219/documents/Data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "General toxicology, clinical chemistry, complete blood counts, histopathology, gene expression. \n\nThis dataset is associated with the following publication:\nChernoff, N., D. Hill, I. Chorus, D. Diggs, H. Huang, D. King, J. Lang, T. Le, J. Schmid, G. Travlos, E. Whitley, R. Wilson, and C. Wood. Cylindrospermopsin toxicity in mice following a 90-d oral exposure.   ENVIRONMENTAL TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA,  549-566, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375219/Combined%20data%20sets%20.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Combined data sets .docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1375219",
             "keyword": [
@@ -71364,20 +71370,10 @@
                 "liver toxicity",
                 "kidney toxicity"
             ],
-            "contactPoint": {
-                "fn": "Neil Chernoff",
-                "hasEmail": "mailto:chernoff.neil@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Combined data sets .docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375219/Combined%20data%20sets%20.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-30",
-            "references": [
-                "https://doi.org/10.1080/15287394.2018.1460787"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71388,43 +71384,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1375219/documents/Data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1080/15287394.2018.1460787"
+            ],
+            "rights": null,
+            "title": "Cylindrospermopsin 90-day oral route toxicology study"
         },
         {
-            "title": "HESI_Biocrates_TMT_2017",
-            "description": "Biocrates metabolomics data for cerebrospinal fluid, serum, plasma, and urine from rats dosed with trimethyl tin at 2, 6, 10, or 14 days after treatmetn. \n\nThis dataset is associated with the following publication:\nImam, S., Z. He, E. Cuevas, H. Rosas-Hernandez, S. Lantz, S. Sarkar, J. Raymick, B. Robinson, J. Hanig, D. Herr, D. MacMillan, A. Smith, S. Liachenko, S. Ferguson, J. O'Callaghan, D. Miller, C. Somps, I. Pardo, W. Slikker, J. Pierson, R. Roberts, B. Gong, W. Tong, M. Aschner, M.J. Kallman, D. Calligaro, and M. Paule. Changes in the metabolome and microRNA levels in biological fluids might represent biomarkers of neurotoxicity: A trimethyltin study.   Experimental Biology and Medicine. SAGE Publications, THOUSAND OAKS, CA, USA, 243(3): 228-236, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1376677",
-            "keyword": [
-                "Biocrates",
-                "neurotoxicity",
-                "biomarker",
-                "metabolomics",
-                "trimethyltin"
-            ],
             "contactPoint": {
                 "fn": "David Herr",
                 "hasEmail": "mailto:herr.david@epa.gov"
             },
+            "description": "Biocrates metabolomics data for cerebrospinal fluid, serum, plasma, and urine from rats dosed with trimethyl tin at 2, 6, 10, or 14 days after treatmetn. \n\nThis dataset is associated with the following publication:\nImam, S., Z. He, E. Cuevas, H. Rosas-Hernandez, S. Lantz, S. Sarkar, J. Raymick, B. Robinson, J. Hanig, D. Herr, D. MacMillan, A. Smith, S. Liachenko, S. Ferguson, J. O'Callaghan, D. Miller, C. Somps, I. Pardo, W. Slikker, J. Pierson, R. Roberts, B. Gong, W. Tong, M. Aschner, M.J. Kallman, D. Calligaro, and M. Paule. Changes in the metabolome and microRNA levels in biological fluids might represent biomarkers of neurotoxicity: A trimethyltin study.   Experimental Biology and Medicine. SAGE Publications, THOUSAND OAKS, CA, USA, 243(3): 228-236, (2018).",
             "distribution": [
                 {
-                    "title": "HESI_Biocrates_2017.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1376677/HESI_Biocrates_2017.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "HESI_Biocrates_2017.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1376677",
+            "keyword": [
+                "Biocrates",
+                "neurotoxicity",
+                "biomarker",
+                "metabolomics",
+                "trimethyltin"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-22",
-            "references": [
-                "https://doi.org/10.1177/1535370217739859"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71434,19 +71428,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1177/1535370217739859"
+            ],
+            "rights": null,
+            "title": "HESI_Biocrates_TMT_2017"
         },
         {
-            "title": "The Application of a Highly Purified Rat Leydig Cell Assay as a Complement to the H295R Steroidogenesis Assay to Evaluate Toxicant Induced Alterations in Testosterone Production",
-            "description": "The greater dynamic range of testosterone production in a highly purified rat Leydig cell assay permitted the detection of chemical induced inhibition that was not detected by the high throughput screening format of the H295R steroidogenesis assay.  This dataset is associated with ORD-022468 entered in STICS. \n\nThis dataset is associated with the following publication:\nBotteri Principato, N., J. Suarez, S. Laws, and G. Klinefelter. The Use of Purified Rat Leydig Cells Complements the H295R Screen to Detect Chemical Induced Alterations in Testosterone Production.   BIOLOGY OF REPRODUCTION. Society for the Study of Reproduction,    98(2): 239-249, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Gary Klinefelter",
+                "hasEmail": "mailto:klinefelter.gary@epa.gov"
+            },
+            "description": "The greater dynamic range of testosterone production in a highly purified rat Leydig cell assay permitted the detection of chemical induced inhibition that was not detected by the high throughput screening format of the H295R steroidogenesis assay.  This dataset is associated with ORD-022468 entered in STICS. \n\nThis dataset is associated with the following publication:\nBotteri Principato, N., J. Suarez, S. Laws, and G. Klinefelter. The Use of Purified Rat Leydig Cells Complements the H295R Screen to Detect Chemical Induced Alterations in Testosterone Production.   BIOLOGY OF REPRODUCTION. Society for the Study of Reproduction,    98(2): 239-249, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378085/manuscript%20figures%206-2-17.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "manuscript figures 6-2-17.pdf"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1378085",
             "keyword": [
@@ -71460,20 +71464,10 @@
                 "Leydig cell assay",
                 "2nd Tier screen"
             ],
-            "contactPoint": {
-                "fn": "Gary Klinefelter",
-                "hasEmail": "mailto:klinefelter.gary@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "manuscript figures 6-2-17.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1378085/manuscript%20figures%206-2-17.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-16",
-            "references": [
-                "https://doi.org/10.1093/biolre/iox177"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71483,41 +71477,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/biolre/iox177"
+            ],
+            "rights": null,
+            "title": "The Application of a Highly Purified Rat Leydig Cell Assay as a Complement to the H295R Steroidogenesis Assay to Evaluate Toxicant Induced Alterations in Testosterone Production"
         },
         {
-            "title": "Data Table for Figures",
-            "description": "This excel file contains 7 tabs, each tabs contains the data for one specific figure in the paper. Description of the data and column names is also provided in each tab. \n\nThis dataset is associated with the following publication:\nWang, J., D. Hallinger, A. Murr, A. Buckalew, S. Simmons, S. Laws, and T. Stoker. High-Throughput Screening and Quantitative Chemical Ranking for Sodium Iodide Symporter Inhibitors in ToxCast Phase 1 Chemical Library.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(9): 5417-5426, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1389586",
-            "keyword": [
-                "Sodium Iodide Symporter",
-                "thyroid",
-                "endocrine disruptor",
-                "high-throughput in vitro screening assay"
-            ],
             "contactPoint": {
                 "fn": "Tammy Stoker",
                 "hasEmail": "mailto:stoker.tammy@epa.gov"
             },
+            "description": "This excel file contains 7 tabs, each tabs contains the data for one specific figure in the paper. Description of the data and column names is also provided in each tab. \n\nThis dataset is associated with the following publication:\nWang, J., D. Hallinger, A. Murr, A. Buckalew, S. Simmons, S. Laws, and T. Stoker. High-Throughput Screening and Quantitative Chemical Ranking for Sodium Iodide Symporter Inhibitors in ToxCast Phase 1 Chemical Library.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(9): 5417-5426, (2018).",
             "distribution": [
                 {
-                    "title": "NIS ph1 dataset for science-hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1389586/NIS%20ph1%20dataset%20for%20science-hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "NIS ph1 dataset for science-hub.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1389586",
+            "keyword": [
+                "Sodium Iodide Symporter",
+                "thyroid",
+                "endocrine disruptor",
+                "high-throughput in vitro screening assay"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-25",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b06145"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71527,19 +71521,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b06145"
+            ],
+            "rights": null,
+            "title": "Data Table for Figures"
         },
         {
-            "title": "Sediment Porewater Data Set",
-            "description": "The data set contains a summary of all measurements that were collected at the cottage grove\nreservoir over the time period of the study. \n\nThis dataset is associated with the following publication:\nEckley, C., T. Luxton, J. Goetz, and J. McKernan. Water-level fluctuations influence sediment porewater chemistry and methylmercury production in a flood-control reservoir..  David Carpenter, and Eddy Zeng  ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 222: 32-41, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Todd Luxton",
+                "hasEmail": "mailto:luxton.todd@epa.gov"
+            },
+            "description": "The data set contains a summary of all measurements that were collected at the cottage grove\nreservoir over the time period of the study. \n\nThis dataset is associated with the following publication:\nEckley, C., T. Luxton, J. Goetz, and J. McKernan. Water-level fluctuations influence sediment porewater chemistry and methylmercury production in a flood-control reservoir..  David Carpenter, and Eddy Zeng  ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 222: 32-41, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502433/CGR%20Data%20Summary.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CGR Data Summary.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502433",
             "keyword": [
@@ -71550,20 +71554,10 @@
                 "mercury methylation",
                 "dissolved organic carbon"
             ],
-            "contactPoint": {
-                "fn": "Todd Luxton",
-                "hasEmail": "mailto:luxton.todd@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "CGR Data Summary.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502433/CGR%20Data%20Summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-20",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2017.01.010"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71573,66 +71567,65 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2017.01.010"
+            ],
+            "rights": null,
+            "title": "Sediment Porewater Data Set"
         },
         {
-            "title": "Predicting Potential Human Health Risk with the Tox21 10k Library",
-            "description": "This study represents the first report applying IVIVE approaches and exposure comparisons using the entirety of the Tox21 federal collaboration chemical screening data, incorporating assay response efficacy and quality of concentration-response fits, and providing quantitative anchoring to first address the likelihood of human in vivo interactions with Tox21 compounds. This likelihood was assessed using a maximum blood concentration to in vitro response ratio approach (Cmax/AC50), analogous to decision-making methods for clinical drug-drug interactions. Fraction unbound in plasma (fup) and intrinsic hepatic clearance (CLint) parameters were estimated in silico and incorporated in a 3-compartment toxicokinetic (TK) model to first predict Cmax for in vivo corroboration using therapeutic scenarios. \n\nThis dataset is associated with the following publication:\nSipes, N., J. Wambaugh, R. Pearce, S. Auerbach, B. Wetmore, J. Hsieh, A. Shapiro, D. Sboboda, M. DeVito, and S. Ferguson. (ENVIRONMENTAL SCIENCE and TECHNOLOGY) An Intuitive Approach for Predicting Human Risk with the Tox21 10k Library.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, issue}: 10786-10796, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1395143",
-            "keyword": [
-                "in vitro to in vivo extrapolation (IVIVE)",
-                "high throughput toxicokinetics",
-                "httk",
-                "IVIVE",
-                "Tox21",
-                "High throughput screening",
-                "HTS",
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "This study represents the first report applying IVIVE approaches and exposure comparisons using the entirety of the Tox21 federal collaboration chemical screening data, incorporating assay response efficacy and quality of concentration-response fits, and providing quantitative anchoring to first address the likelihood of human in vivo interactions with Tox21 compounds. This likelihood was assessed using a maximum blood concentration to in vitro response ratio approach (Cmax/AC50), analogous to decision-making methods for clinical drug-drug interactions. Fraction unbound in plasma (fup) and intrinsic hepatic clearance (CLint) parameters were estimated in silico and incorporated in a 3-compartment toxicokinetic (TK) model to first predict Cmax for in vivo corroboration using therapeutic scenarios. \n\nThis dataset is associated with the following publication:\nSipes, N., J. Wambaugh, R. Pearce, S. Auerbach, B. Wetmore, J. Hsieh, A. Shapiro, D. Sboboda, M. DeVito, and S. Ferguson. (ENVIRONMENTAL SCIENCE and TECHNOLOGY) An Intuitive Approach for Predicting Human Risk with the Tox21 10k Library.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, issue}: 10786-10796, (2017).",
             "distribution": [
                 {
-                    "title": "Supporting Information_EST_FINAL_18JUL2017.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395143/Supporting%20Information_EST_FINAL_18JUL2017.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Supporting Information_EST_FINAL_18JUL2017.pdf"
                 },
                 {
-                    "title": "Table S1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395143/Table%20S1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S1.xlsx"
                 },
                 {
-                    "title": "Table S2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395143/Table%20S2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S2.xlsx"
                 },
                 {
-                    "title": "Table S3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395143/Table%20S3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table S3.xlsx"
                 },
                 {
-                    "title": "https://ntp.niehs.nih.gov/sandbox/ivive/",
-                    "accessURL": "https://ntp.niehs.nih.gov/sandbox/ivive/"
+                    "accessURL": "https://ntp.niehs.nih.gov/sandbox/ivive/",
+                    "title": "https://ntp.niehs.nih.gov/sandbox/ivive/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1395143",
+            "keyword": [
+                "in vitro to in vivo extrapolation (IVIVE)",
+                "high throughput toxicokinetics",
+                "httk",
+                "IVIVE",
+                "Tox21",
+                "High throughput screening",
+                "HTS",
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-19",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b00650",
-                "https://ntp.niehs.nih.gov/sandbox/ivive/"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71642,19 +71635,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b00650",
+                "https://ntp.niehs.nih.gov/sandbox/ivive/"
+            ],
+            "rights": null,
+            "title": "Predicting Potential Human Health Risk with the Tox21 10k Library"
         },
         {
-            "title": "Triclosan Hershberger H295 data",
-            "description": "Triclosan data from Hershberger experiment using castrated male rats.  Data includes accessory sex tissue mean weights and thyroid gland weight following exposure to triclosan for 10 days both with and without testosterone stimulation.  Also included are the thyroxine hormone means in these males.  In addition, mean data on the in vitro adrenocortical cells for steroid hormone production (testosterone and estradiol) with a dose response of triclosan. \n\nThis dataset is associated with the following publication:\nFarmer, W., G. Louis, A. Buckalew, D. Hallinger, and T. Stoker. Evaluation of Triclosan in the Hershberger and H295R Steroidogenesis Assays.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA,  194-199, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Tammy Stoker",
+                "hasEmail": "mailto:stoker.tammy@epa.gov"
+            },
+            "description": "Triclosan data from Hershberger experiment using castrated male rats.  Data includes accessory sex tissue mean weights and thyroid gland weight following exposure to triclosan for 10 days both with and without testosterone stimulation.  Also included are the thyroxine hormone means in these males.  In addition, mean data on the in vitro adrenocortical cells for steroid hormone production (testosterone and estradiol) with a dose response of triclosan. \n\nThis dataset is associated with the following publication:\nFarmer, W., G. Louis, A. Buckalew, D. Hallinger, and T. Stoker. Evaluation of Triclosan in the Hershberger and H295R Steroidogenesis Assays.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA,  194-199, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407648/ScienceHubDataforTriclosan%20Hershberger%20Paper%20Final%201.29.18.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHubDataforTriclosan Hershberger Paper Final 1.29.18.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407648",
             "keyword": [
@@ -71666,20 +71670,10 @@
                 "estrogen",
                 "Triclosan"
             ],
-            "contactPoint": {
-                "fn": "Tammy Stoker",
-                "hasEmail": "mailto:stoker.tammy@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ScienceHubDataforTriclosan Hershberger Paper Final 1.29.18.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407648/ScienceHubDataforTriclosan%20Hershberger%20Paper%20Final%201.29.18.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-25",
-            "references": [
-                "https://doi.org/10.1016/j.toxlet.2018.03.001"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71689,19 +71683,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.toxlet.2018.03.001"
+            ],
+            "rights": null,
+            "title": "Triclosan Hershberger H295 data"
         },
         {
-            "title": "Dataset for manuscript \"Mixed \u201canti-androgenic\u201d chemicals at low individual doses produces reproductive tract malformations in the male rat\"",
-            "description": "Dataset contains summary data (mean, standard error, sample size (n)) for all measured endpoints reported and depicted in the corresponding manuscript. \n\nThis dataset is associated with the following publication:\nConley, J., C. Lambright, N. Evans, M. Cardon, J. Furr, V. Wilson, and E. Gray. Mixed \u201cantiandrogenic\u201d chemicals at low individual doses produce reproductive tract malformations in the male rat.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  164(1): 166-178, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Justin Conley",
+                "hasEmail": "mailto:conley.justin@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1408091/documents/ConleyJustin_A-73ng_Dataset_Dictionary_20171108.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Dataset contains summary data (mean, standard error, sample size (n)) for all measured endpoints reported and depicted in the corresponding manuscript. \n\nThis dataset is associated with the following publication:\nConley, J., C. Lambright, N. Evans, M. Cardon, J. Furr, V. Wilson, and E. Gray. Mixed \u201cantiandrogenic\u201d chemicals at low individual doses produce reproductive tract malformations in the male rat.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  164(1): 166-178, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408091/ConleyJustin_Dataset_A-73ng_20171108.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "ConleyJustin_Dataset_A-73ng_20171108.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1408091",
             "keyword": [
@@ -71712,20 +71718,10 @@
                 "pesticides",
                 "Phthalates"
             ],
-            "contactPoint": {
-                "fn": "Justin Conley",
-                "hasEmail": "mailto:conley.justin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ConleyJustin_Dataset_A-73ng_20171108.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408091/ConleyJustin_Dataset_A-73ng_20171108.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-09",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfy069"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71736,42 +71732,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1408091/documents/ConleyJustin_A-73ng_Dataset_Dictionary_20171108.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfy069"
+            ],
+            "rights": null,
+            "title": "Dataset for manuscript \"Mixed \u201canti-androgenic\u201d chemicals at low individual doses produces reproductive tract malformations in the male rat\""
         },
         {
-            "title": "Building downwash large eddy simulations",
-            "description": "This data set is associated with the results found in the journal article: Foroutan et al, 2018. Numerical analysis of pollutant dispersion around elongated buildings: an embedded large eddy simulation approach. Atmospheric Environment, https://doi.org/10.1016/j.atmosenv.2018.05.053. \nThe objective of the paper is to employ a scale-resolving turbulence model, namely the embedded LES (ELES), to study near-field pollutant dispersion around elongated/rotated buildings. It includes the evaluation of the ELES performance against wind tunnel measurements, as well as the analysis of the computational results for various source-building geometries while emphasizing the aspects important for dispersion modeling. \n\nThis dataset is associated with the following publication:\nForoutan, H., W. Tang, D. Heist, S. Perry, L. Brouwer, and E. Monbureau. Numerical analysis of pollutant dispersion around elongated buildings: An embedded large eddy simulation approach.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 187: 117-130, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1434501",
-            "keyword": [
-                "Pollutant dispersion",
-                "building downwash",
-                "Large Eddy Simulation",
-                "CFD"
-            ],
             "contactPoint": {
                 "fn": "Hosein Foroutan",
                 "hasEmail": "mailto:foroutan.hosein@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434501/documents/ForoutanHosein_A-f7md_DataDictionary_20180605.pdf",
+            "describedByType": "application/pdf",
+            "description": "This data set is associated with the results found in the journal article: Foroutan et al, 2018. Numerical analysis of pollutant dispersion around elongated buildings: an embedded large eddy simulation approach. Atmospheric Environment, https://doi.org/10.1016/j.atmosenv.2018.05.053. \nThe objective of the paper is to employ a scale-resolving turbulence model, namely the embedded LES (ELES), to study near-field pollutant dispersion around elongated/rotated buildings. It includes the evaluation of the ELES performance against wind tunnel measurements, as well as the analysis of the computational results for various source-building geometries while emphasizing the aspects important for dispersion modeling. \n\nThis dataset is associated with the following publication:\nForoutan, H., W. Tang, D. Heist, S. Perry, L. Brouwer, and E. Monbureau. Numerical analysis of pollutant dispersion around elongated buildings: An embedded large eddy simulation approach.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 187: 117-130, (2018).",
             "distribution": [
                 {
-                    "title": "ForoutanHosein_A-f7md_DataFiles_20180605.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434501/ForoutanHosein_A-f7md_DataFiles_20180605.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "ForoutanHosein_A-f7md_DataFiles_20180605.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434501",
+            "keyword": [
+                "Pollutant dispersion",
+                "building downwash",
+                "Large Eddy Simulation",
+                "CFD"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-05",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2018.05.053"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71782,42 +71778,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434501/documents/ForoutanHosein_A-f7md_DataDictionary_20180605.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2018.05.053"
+            ],
+            "rights": null,
+            "title": "Building downwash large eddy simulations"
         },
         {
-            "title": "FL estuaries RESTORE",
-            "description": "light attenuation data within NW Florida estuaries during 2009-2013. \n\nThis dataset is associated with the following publication:\nConmy, R., B. Schaeffer, J. Schubauer-Berigan, J. Aukamp, A. Duffy, J. Lehrter, and R. Greene. Characterizing light attenuation within Northwest Florida Estuaries: Implications for RESTORE Act water quality monitoring.  Charles Sheppard, Francois Galgani, Pat Hutchings, and Victor Quintino  MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 114(2): 995-1006, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1407617",
-            "keyword": [
-                "light attenutation",
-                "Florida estuaries",
-                "water quality",
-                "RESTORE Act"
-            ],
             "contactPoint": {
                 "fn": "Robyn Conmy",
                 "hasEmail": "mailto:conmy.robyn@epa.gov"
             },
+            "description": "light attenuation data within NW Florida estuaries during 2009-2013. \n\nThis dataset is associated with the following publication:\nConmy, R., B. Schaeffer, J. Schubauer-Berigan, J. Aukamp, A. Duffy, J. Lehrter, and R. Greene. Characterizing light attenuation within Northwest Florida Estuaries: Implications for RESTORE Act water quality monitoring.  Charles Sheppard, Francois Galgani, Pat Hutchings, and Victor Quintino  MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 114(2): 995-1006, (2017).",
             "distribution": [
                 {
-                    "title": "FL optics master sheet for conmy et al_2015.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407617/FL%20optics%20master%20sheet%20for%20conmy%20et%20al_2015.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FL optics master sheet for conmy et al_2015.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407617",
+            "keyword": [
+                "light attenutation",
+                "Florida estuaries",
+                "water quality",
+                "RESTORE Act"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-12",
-            "references": [
-                "http://www.sciencedirect.com/science/journal/0025326X/114/2"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71827,51 +71821,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.sciencedirect.com/science/journal/0025326X/114/2"
+            ],
+            "rights": null,
+            "title": "FL estuaries RESTORE"
         },
         {
-            "title": "Great Lakes Proxies Project",
-            "description": "This dataset includes five ESRI ArcMap shapefiles to provide metadata for those shapefiles. Additional, within the attribute table of  each shapefile is a data field titled \"SHP_Source\" that provides a brief description of the public data sources used to create the shapefile. These data include aquatic non-native species presence in waters of the Laurentian Great Lakes, US and Canadian population for urban areas around the Great Lakes, locations of marinas and ports in the Great Lakes, and data on maritime commerce within the Great Lakes. \n\nThis dataset is associated with the following publication:\nO'Malia, E., L. Johnson, and J. Hoffman. Pathways and places associated with nonindigenous aquatic species introductions in the Laurentian Great Lakes.   HYDROBIOLOGIA. Springer, New York, NY, USA, 817(1): 23-40, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1395247",
-            "keyword": [
-                "Great Lakes",
-                "non-indigenous aquatic species",
-                "biomonitoring",
-                "early detection"
-            ],
             "contactPoint": {
                 "fn": "Joel Hoffman",
                 "hasEmail": "mailto:hoffman.joel@epa.gov"
             },
+            "description": "This dataset includes five ESRI ArcMap shapefiles to provide metadata for those shapefiles. Additional, within the attribute table of  each shapefile is a data field titled \"SHP_Source\" that provides a brief description of the public data sources used to create the shapefile. These data include aquatic non-native species presence in waters of the Laurentian Great Lakes, US and Canadian population for urban areas around the Great Lakes, locations of marinas and ports in the Great Lakes, and data on maritime commerce within the Great Lakes. \n\nThis dataset is associated with the following publication:\nO'Malia, E., L. Johnson, and J. Hoffman. Pathways and places associated with nonindigenous aquatic species introductions in the Laurentian Great Lakes.   HYDROBIOLOGIA. Springer, New York, NY, USA, 817(1): 23-40, (2018).",
             "distribution": [
                 {
-                    "title": "HoffmanJoel_A-4qrn_Dataset_20170927.Zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395247/HoffmanJoel_A-4qrn_Dataset_20170927.Zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "HoffmanJoel_A-4qrn_Dataset_20170927.Zip"
                 },
                 {
-                    "title": "Shapefile Metadata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395247/Shapefile%20Metadata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Shapefile Metadata.xlsx"
                 },
                 {
-                    "title": "Maritime Commerce Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395247/Maritime%20Commerce%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Maritime Commerce Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1395247",
+            "keyword": [
+                "Great Lakes",
+                "non-indigenous aquatic species",
+                "biomonitoring",
+                "early detection"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-02-01",
-            "references": [
-                "https://doi.org/10.1007/s10750-018-3551-x"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71881,44 +71875,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10750-018-3551-x"
+            ],
+            "rights": null,
+            "title": "Great Lakes Proxies Project"
         },
         {
-            "title": "2017_Prediction_of_H295R_steroidogenesis_Pathway_Perturbation",
-            "description": "The objectives of this work were to: 1) develop an integrated analysis of chemical-mediated effects on steroidogenesis in the HT-H295R assay; and, 2) evaluate whether the HT-H295R assay predicts estrogen and androgen production specifically via comparison with the OECD-validated H295R assay. \n\nThis dataset is associated with the following publication:\nHaggard, D., A. Karmaus, M. Martin, R. Judson, W. Setzer, and K. Paul-Friedman. (Toxicological Sciences) High-throughput H295R steroidogenesis assay: utility as an alternative and a statistical approach to characterize effects on steroidogenesis.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  162(2): 509-534, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1407003",
-            "keyword": [
-                "EDSP21",
-                "ToxCast",
-                "steroidogenesi",
-                "ACToR"
-            ],
             "contactPoint": {
                 "fn": "Richard Judson",
                 "hasEmail": "mailto:judson.richard@epa.gov"
             },
+            "description": "The objectives of this work were to: 1) develop an integrated analysis of chemical-mediated effects on steroidogenesis in the HT-H295R assay; and, 2) evaluate whether the HT-H295R assay predicts estrogen and androgen production specifically via comparison with the OECD-validated H295R assay. \n\nThis dataset is associated with the following publication:\nHaggard, D., A. Karmaus, M. Martin, R. Judson, W. Setzer, and K. Paul-Friedman. (Toxicological Sciences) High-throughput H295R steroidogenesis assay: utility as an alternative and a statistical approach to characterize effects on steroidogenesis.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  162(2): 509-534, (2018).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Haggard/2017_Prediction_of_H295R_steroidogenesis_Pathway_Perturbation/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Haggard/2017_Prediction_of_H295R_steroidogenesis_Pathway_Perturbation/"
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Haggard/2017_Prediction_of_H295R_steroidogenesis_Pathway_Perturbation/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Haggard/2017_Prediction_of_H295R_steroidogenesis_Pathway_Perturbation/"
                 },
                 {
-                    "title": "https://github.com/USEPA/CompTox-ToxCast-EDSPsteroidogenesis",
-                    "accessURL": "https://github.com/USEPA/CompTox-ToxCast-EDSPsteroidogenesis"
+                    "accessURL": "https://github.com/USEPA/CompTox-ToxCast-EDSPsteroidogenesis",
+                    "title": "https://github.com/USEPA/CompTox-ToxCast-EDSPsteroidogenesis"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407003",
+            "keyword": [
+                "EDSP21",
+                "ToxCast",
+                "steroidogenesi",
+                "ACToR"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-08",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfx274"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71928,19 +71922,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfx274"
+            ],
+            "rights": null,
+            "title": "2017_Prediction_of_H295R_steroidogenesis_Pathway_Perturbation"
         },
         {
-            "title": "Read_Across_Prediction_of_Estrogenicity_for_Hindered_Phenols_2017_Data",
-            "description": "Read-across is an important data gap filling technique used within category and analog approaches for regulatory hazard identification and risk assessment. Although much technical guidance is available that describes how to develop category/analog approaches, practical principles to evaluate and substantiate analog validity (suitability) are still lacking. This case study uses hindered phenols as an example chemical class to determine: (1) the capability of three structure fingerprint/descriptor methods (PubChem, ToxPrints and MoSS MCSS) to identify analogs for read-across to predict Estrogen Receptor (ER) binding activity and, (2) the utility of data confidence measures, physicochemical properties, and chemical R-group properties as filters to improve ER binding predictions. The training dataset comprised 462 hindered phenols and 257 non- hindered phenols. For each chemical of interest (target), source analogs were identified from two datasets (hindered and non-hindered phenols) that had been characterized by a fingerprint/descriptor method and by two cut-offs: (1) minimum similarity distance (range: 0.1 - 0.9) and, (2) N closest analogs (range: 1 - 10). Analogs were then filtered using: (1) physicochemical properties of the phenol (termed global filtering) and, (2) physicochemical properties of the R-groups neighboring the active hydroxyl group (termed local filtering). A read-across prediction was made for each target chemical on the basis of a majority vote of the N closest analogs. The results demonstrate that: (1) concordance in ER activity increases with structural similarity, regardless of the structure fingerprint/descriptor method, (2) increased data confidence significantly improves read-across predictions, and (3) filtering analogs using global and local properties can help identify more suitable analogs. This case study illustrates that the quality of the underlying experimental data and use of endpoint relevant chemical descriptors to evaluate source analogs are critical to achieving robust read-across predictions. \n\nThis dataset is associated with the following publication:\nPradeep, P., K. Mansouri, G. Patlewicz, and R. Judson. (Computational Toxicology) A systematic evaluation of analogs and automated read-across prediction of estrogenicity: A case study using hindered phenols.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 4: 22-30, (2017).",
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
+            "description": "Read-across is an important data gap filling technique used within category and analog approaches for regulatory hazard identification and risk assessment. Although much technical guidance is available that describes how to develop category/analog approaches, practical principles to evaluate and substantiate analog validity (suitability) are still lacking. This case study uses hindered phenols as an example chemical class to determine: (1) the capability of three structure fingerprint/descriptor methods (PubChem, ToxPrints and MoSS MCSS) to identify analogs for read-across to predict Estrogen Receptor (ER) binding activity and, (2) the utility of data confidence measures, physicochemical properties, and chemical R-group properties as filters to improve ER binding predictions. The training dataset comprised 462 hindered phenols and 257 non- hindered phenols. For each chemical of interest (target), source analogs were identified from two datasets (hindered and non-hindered phenols) that had been characterized by a fingerprint/descriptor method and by two cut-offs: (1) minimum similarity distance (range: 0.1 - 0.9) and, (2) N closest analogs (range: 1 - 10). Analogs were then filtered using: (1) physicochemical properties of the phenol (termed global filtering) and, (2) physicochemical properties of the R-groups neighboring the active hydroxyl group (termed local filtering). A read-across prediction was made for each target chemical on the basis of a majority vote of the N closest analogs. The results demonstrate that: (1) concordance in ER activity increases with structural similarity, regardless of the structure fingerprint/descriptor method, (2) increased data confidence significantly improves read-across predictions, and (3) filtering analogs using global and local properties can help identify more suitable analogs. This case study illustrates that the quality of the underlying experimental data and use of endpoint relevant chemical descriptors to evaluate source analogs are critical to achieving robust read-across predictions. \n\nThis dataset is associated with the following publication:\nPradeep, P., K. Mansouri, G. Patlewicz, and R. Judson. (Computational Toxicology) A systematic evaluation of analogs and automated read-across prediction of estrogenicity: A case study using hindered phenols.   Computational Toxicology. Elsevier B.V., Amsterdam,  NETHERLANDS, 4: 22-30, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/Pradeep%20Hindered%20Phenols%202017/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/Pradeep%20Hindered%20Phenols%202017/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407005",
             "keyword": [
@@ -71950,19 +71953,10 @@
                 "ToxCast",
                 "ACToR"
             ],
-            "contactPoint": {
-                "fn": "Richard Judson",
-                "hasEmail": "mailto:judson.richard@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/Pradeep%20Hindered%20Phenols%202017/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/Pradeep%20Hindered%20Phenols%202017/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-18",
-            "references": [
-                "https://doi.org/10.1016/j.comtox.2017.09.001"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -71972,41 +71966,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.comtox.2017.09.001"
+            ],
+            "rights": null,
+            "title": "Read_Across_Prediction_of_Estrogenicity_for_Hindered_Phenols_2017_Data"
         },
         {
-            "title": "Validation of an automated counting procedure for phthalate-induced testicular multinucleated germ cells",
-            "description": "the dataset contains NHEERL collected data on fetal male rat gestational day 18 testicular testosterone production and related data. \n\nThis dataset is associated with the following publication:\nspade, d., C. Yue Bai , C. Lambright, J. Conley, K. Boekelheide , and E. Gray. Validation of an automated counting procedure for phthalate-induced testicular multinucleated germ cells.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 290: 55-61, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1408099",
-            "keyword": [
-                "Phthalates",
-                "automated high throughput methods",
-                "testis pathology",
-                "androgen signaling AOP network"
-            ],
             "contactPoint": {
                 "fn": "Leon Gray",
                 "hasEmail": "mailto:gray.earl@epa.gov"
             },
+            "description": "the dataset contains NHEERL collected data on fetal male rat gestational day 18 testicular testosterone production and related data. \n\nThis dataset is associated with the following publication:\nspade, d., C. Yue Bai , C. Lambright, J. Conley, K. Boekelheide , and E. Gray. Validation of an automated counting procedure for phthalate-induced testicular multinucleated germ cells.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 290: 55-61, (2018).",
             "distribution": [
                 {
-                    "title": "119 105 MNG BLOCKS T PROD SAS ANALYSIS used in spade manuscript and added to Science Hub 12 11 2017.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408099/119%20105%20MNG%20BLOCKS%20T%20PROD%20SAS%20ANALYSIS%20used%20in%20spade%20manuscript%20and%20added%20to%20Science%20Hub%2012%2011%202017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "119 105 MNG BLOCKS T PROD SAS ANALYSIS used in spade manuscript and added to Science Hub 12 11 2017.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1408099",
+            "keyword": [
+                "Phthalates",
+                "automated high throughput methods",
+                "testis pathology",
+                "androgen signaling AOP network"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-06",
-            "references": [
-                "https://doi.org/10.1016/j.toxlet.2018.03.018"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72016,19 +72010,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.toxlet.2018.03.018"
+            ],
+            "rights": null,
+            "title": "Validation of an automated counting procedure for phthalate-induced testicular multinucleated germ cells"
         },
         {
-            "title": "Chromatographic_Retention_Time_Prediction_Models_TALANTA_Data",
-            "description": "This paper compares the relative predictive ability and applicability to NTA workflows of three RT prediction models: (1) a logP (octanol-water partition coefficient)-based model using EPI SuiteTM logP predictions; (2) a commercially available ACD/ChromGenius model; and, (3) a newly developed Quantitative Structure Retention Relationship model called OPERA-RT. \n\nThis dataset is associated with the following publication:\nMcEachran, A., K. Mansouri, S. Newton, B. Beverly, J. Sobus, and A. Williams. (TALANTA) A comparison of three liquid chromatography (LC) retention time prediction models.   TALANTA. Elsevier Science Ltd, New York, NY, USA, 182: 371-379, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Antony Williams",
+                "hasEmail": "mailto:williams.antony@epa.gov"
+            },
+            "description": "This paper compares the relative predictive ability and applicability to NTA workflows of three RT prediction models: (1) a logP (octanol-water partition coefficient)-based model using EPI SuiteTM logP predictions; (2) a commercially available ACD/ChromGenius model; and, (3) a newly developed Quantitative Structure Retention Relationship model called OPERA-RT. \n\nThis dataset is associated with the following publication:\nMcEachran, A., K. Mansouri, S. Newton, B. Beverly, J. Sobus, and A. Williams. (TALANTA) A comparison of three liquid chromatography (LC) retention time prediction models.   TALANTA. Elsevier Science Ltd, New York, NY, USA, 182: 371-379, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/McEachran_A/RT_Prediction_2018/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/McEachran_A/RT_Prediction_2018/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407009",
             "keyword": [
@@ -72040,19 +72043,10 @@
                 "Chemistry Dashboard",
                 "dashboards"
             ],
-            "contactPoint": {
-                "fn": "Antony Williams",
-                "hasEmail": "mailto:williams.antony@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/McEachran_A/RT_Prediction_2018/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/McEachran_A/RT_Prediction_2018/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-03",
-            "references": [
-                "https://doi.org/10.1016/j.talanta.2018.01.022"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72062,37 +72056,37 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.talanta.2018.01.022"
+            ],
+            "rights": null,
+            "title": "Chromatographic_Retention_Time_Prediction_Models_TALANTA_Data"
         },
         {
-            "title": "Fitzpatrick_Jeremy_Skin_Sensitization_Data",
-            "description": "Allergic contact dermatitis (ACD) is estimated to constitute about 10-15% of all occupational diseases. Predictive testing to characterise substances for their skin sensitisation potential has historically been based on animal models such as the Local Lymph Node Assay (LLNA) and the Guinea Pig Maximisation Test (GPMT). In recent years, EU regulations, have provided a strong incentive to develop non-animal alternatives.  Significant progress has been made in developing and evaluating non-animal test methods. There have been efforts to develop and evaluate the utility of in silico models for skin sensitisation including local and global (Q)SARs as well as expert systems. In this study, we selected three different types of expert systems: VEGA (statistical), Derek Nexus (knowledge based), TIMES-SS (hybrid) and evaluated their performance using 2 large datasets of substances that had been assessed for their skin sensitisation potential in animal models. We considered a model to be successful at predicting skin sensitisation potential if it had at least the same balanced accuracy as the LLNA and the GPMT had in predicting the outcomes of one another, which ranged from 79% to 86% depending on the dataset.  We found that none of the expert systems evaluated was able to achieve such a high balanced accuracy in their global predictions, with balanced accuracies ranging from 56% to 65%.  However, for substances within the domain of TIMES-SS, balanced accuracies were found to be 79% and 82%, for the two datasets, in line with the animal data. The expert systems evaluated could be extended in light of the additional data collected as part of this study. The incorrect predictions offer new insights for how the existing alerts within these expert systems could be refined. These datasets also offer exciting opportunities for the development of new models. \n\nThis dataset is associated with the following publication:\nFitzpatrick, J., D. Roberts, and G. Patlewicz. (SAR and QSAR in ENVIRONMENTAL RESEARCH) An evaluation of selected (Q)SARs/expert systems for predicting skin sensitisation potential.   SAR AND QSAR IN ENVIRONMENTAL RESEARCH. Taylor & Francis, Inc., Philadelphia, PA, USA, 29(6): 439-468, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1427471",
-            "keyword": [
-                "DSSTox"
-            ],
             "contactPoint": {
                 "fn": "Ann Richard",
                 "hasEmail": "mailto:richard.ann@epa.gov"
             },
+            "description": "Allergic contact dermatitis (ACD) is estimated to constitute about 10-15% of all occupational diseases. Predictive testing to characterise substances for their skin sensitisation potential has historically been based on animal models such as the Local Lymph Node Assay (LLNA) and the Guinea Pig Maximisation Test (GPMT). In recent years, EU regulations, have provided a strong incentive to develop non-animal alternatives.  Significant progress has been made in developing and evaluating non-animal test methods. There have been efforts to develop and evaluate the utility of in silico models for skin sensitisation including local and global (Q)SARs as well as expert systems. In this study, we selected three different types of expert systems: VEGA (statistical), Derek Nexus (knowledge based), TIMES-SS (hybrid) and evaluated their performance using 2 large datasets of substances that had been assessed for their skin sensitisation potential in animal models. We considered a model to be successful at predicting skin sensitisation potential if it had at least the same balanced accuracy as the LLNA and the GPMT had in predicting the outcomes of one another, which ranged from 79% to 86% depending on the dataset.  We found that none of the expert systems evaluated was able to achieve such a high balanced accuracy in their global predictions, with balanced accuracies ranging from 56% to 65%.  However, for substances within the domain of TIMES-SS, balanced accuracies were found to be 79% and 82%, for the two datasets, in line with the animal data. The expert systems evaluated could be extended in light of the additional data collected as part of this study. The incorrect predictions offer new insights for how the existing alerts within these expert systems could be refined. These datasets also offer exciting opportunities for the development of new models. \n\nThis dataset is associated with the following publication:\nFitzpatrick, J., D. Roberts, and G. Patlewicz. (SAR and QSAR in ENVIRONMENTAL RESEARCH) An evaluation of selected (Q)SARs/expert systems for predicting skin sensitisation potential.   SAR AND QSAR IN ENVIRONMENTAL RESEARCH. Taylor & Francis, Inc., Philadelphia, PA, USA, 29(6): 439-468, (2018).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/PatlewiczGrace/Fitzpatrick_Evaluation_Of_QSARs_for_Predicting_Skin_Sensitisation_Potential/",
-                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/PatlewiczGrace/Fitzpatrick_Evaluation_Of_QSARs_for_Predicting_Skin_Sensitisation_Potential/"
+                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/PatlewiczGrace/Fitzpatrick_Evaluation_Of_QSARs_for_Predicting_Skin_Sensitisation_Potential/",
+                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/PatlewiczGrace/Fitzpatrick_Evaluation_Of_QSARs_for_Predicting_Skin_Sensitisation_Potential/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1427471",
+            "keyword": [
+                "DSSTox"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-02",
-            "references": [
-                "https://doi.org/10.1080/1062936x.2018.1455223"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72102,51 +72096,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/1062936x.2018.1455223"
+            ],
+            "rights": null,
+            "title": "Fitzpatrick_Jeremy_Skin_Sensitization_Data"
         },
         {
-            "title": "Illumina sequencing",
-            "description": "These data are bacterial 16S rRNA sequences and a taxonomic summary table for biofilm samples from the bio-reactors. The data may provide background/supporting information for other researchers who have a similar experimental plan with a microbial electrochemical cell reactor. \n\nThis dataset is associated with the following publication:\nSantodomingo, J., H. Lee, B. Dhar, J. An, B. Rittmann, H. Ren, and J. Chae. The Roles of Biofilm Conductivity and Donor Substrate Kinetics in a Mixed-Culture Biofilm Anod.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(23): 12799-12807, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1500924",
-            "keyword": [
-                "biofilm conductivity",
-                "Donor Substrate Kinetics",
-                "Biofilm anode",
-                "Illumina sequencing"
-            ],
             "contactPoint": {
                 "fn": "Hodon Ryu",
                 "hasEmail": "mailto:ryu.hodon@epa.gov"
             },
+            "description": "These data are bacterial 16S rRNA sequences and a taxonomic summary table for biofilm samples from the bio-reactors. The data may provide background/supporting information for other researchers who have a similar experimental plan with a microbial electrochemical cell reactor. \n\nThis dataset is associated with the following publication:\nSantodomingo, J., H. Lee, B. Dhar, J. An, B. Rittmann, H. Ren, and J. Chae. The Roles of Biofilm Conductivity and Donor Substrate Kinetics in a Mixed-Culture Biofilm Anod.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(23): 12799-12807, (2016).",
             "distribution": [
                 {
-                    "title": "biofilm conductivity kinetics_fasta.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500924/biofilm%20conductivity%20kinetics_fasta.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "biofilm conductivity kinetics_fasta.docx"
                 },
                 {
-                    "title": "biofilm conductivity kinetics_Table 1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500924/biofilm%20conductivity%20kinetics_Table%201.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "biofilm conductivity kinetics_Table 1.docx"
                 },
                 {
-                    "title": "biofilm conductivity kinetics_muthur analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500924/biofilm%20conductivity%20kinetics_muthur%20analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "biofilm conductivity kinetics_muthur analysis.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500924",
+            "keyword": [
+                "biofilm conductivity",
+                "Donor Substrate Kinetics",
+                "Biofilm anode",
+                "Illumina sequencing"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-05",
-            "references": [
-                "https://doi.org/10.1021/acs.est.6b04168"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72156,55 +72150,55 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.6b04168"
+            ],
+            "rights": null,
+            "title": "Illumina sequencing"
         },
         {
-            "title": "Clades of Candidatus Accumulibacter phosphatis enriched under cyclic anaerobic and microaerobic conditions",
-            "description": "Rates of reactor performance, and relative abundance of the different molecular groups found. \n\nThis dataset is associated with the following publication:\nCamejo, P., B. Owen, J. Martirano, J. Ma, V. Kapoor, J. Santodomingo, K. McMahon, and D. Noguera. Clades of Candidatus Accumulibacter phosphatis enriched under cyclic anaerobic and microaerobic conditions simultaneously use different electron acceptors.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 102: 125-137, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1502459",
-            "keyword": [
-                "phosphate accumulation",
-                "low dissolve oxygen",
-                "water and wastewater treatment"
-            ],
             "contactPoint": {
                 "fn": "Jorge Santo Domingo",
                 "hasEmail": "mailto:santodomingo.jorge@epa.gov"
             },
+            "description": "Rates of reactor performance, and relative abundance of the different molecular groups found. \n\nThis dataset is associated with the following publication:\nCamejo, P., B. Owen, J. Martirano, J. Ma, V. Kapoor, J. Santodomingo, K. McMahon, and D. Noguera. Clades of Candidatus Accumulibacter phosphatis enriched under cyclic anaerobic and microaerobic conditions simultaneously use different electron acceptors.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 102: 125-137, (2016).",
             "distribution": [
                 {
-                    "title": "OTU_abundance_LS-SBR.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502459/OTU_abundance_LS-SBR.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "OTU_abundance_LS-SBR.csv"
                 },
                 {
-                    "title": "OTU_abundance_PS-SBR.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502459/OTU_abundance_PS-SBR.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "OTU_abundance_PS-SBR.csv"
                 },
                 {
-                    "title": "Camejo-et.al-2016-Fig. 5-RawData Accumulibacter.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502459/Camejo-et.al-2016-Fig.%205-RawData%20Accumulibacter.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Camejo-et.al-2016-Fig. 5-RawData Accumulibacter.xlsx"
                 },
                 {
-                    "title": "qPCRSummary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502459/qPCRSummary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "qPCRSummary.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502459",
+            "keyword": [
+                "phosphate accumulation",
+                "low dissolve oxygen",
+                "water and wastewater treatment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-28",
-            "references": [
-                "http://www.sciencedirect.com/science/article/pii/S0043135416304699"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72214,40 +72208,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.sciencedirect.com/science/article/pii/S0043135416304699"
+            ],
+            "rights": null,
+            "title": "Clades of Candidatus Accumulibacter phosphatis enriched under cyclic anaerobic and microaerobic conditions"
         },
         {
-            "title": "Analysis of mitochondrail DNA sequences",
-            "description": "Data for all the tables and figures on the frequency of haplotypes found in a tropical watershed contaminated with human fecal pollution. \n\nThis dataset is associated with the following publication:\nKapoor, V., M. Elk, C. Toledo-Hernandez, and J. Santodomingo. Analysis of human mitochondrial DNA sequences from fecally polluted environmental waters as a tool to study population diversity.   AIMS Environmental Science. AIMS Press, Springfield, MO, USA, 4(3): 443-455, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1502462",
-            "keyword": [
-                "fecal poillution",
-                "Microbial Source Tracking",
-                "Mitochondria"
-            ],
             "contactPoint": {
                 "fn": "Jorge Santo Domingo",
                 "hasEmail": "mailto:santodomingo.jorge@epa.gov"
             },
+            "description": "Data for all the tables and figures on the frequency of haplotypes found in a tropical watershed contaminated with human fecal pollution. \n\nThis dataset is associated with the following publication:\nKapoor, V., M. Elk, C. Toledo-Hernandez, and J. Santodomingo. Analysis of human mitochondrial DNA sequences from fecally polluted environmental waters as a tool to study population diversity.   AIMS Environmental Science. AIMS Press, Springfield, MO, USA, 4(3): 443-455, (2017).",
             "distribution": [
                 {
-                    "title": "20samples_0.05_Haplotypes.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502462/20samples_0.05_Haplotypes.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "20samples_0.05_Haplotypes.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502462",
+            "keyword": [
+                "fecal poillution",
+                "Microbial Source Tracking",
+                "Mitochondria"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-18",
-            "references": [
-                "https://doi.org/10.3934/environsci.2017.3.443"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72257,19 +72251,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3934/environsci.2017.3.443"
+            ],
+            "rights": null,
+            "title": "Analysis of mitochondrail DNA sequences"
         },
         {
-            "title": "Copper Silver Ionization at a hospital dataset",
-            "description": "Temperature, pH, chlorine, copper and silver levels at a hospital employing copper-silver ionization to control Legionella bacteria. \n\nThis dataset is associated with the following publication:\nTriantafyllidou, S., D. Lytle, C. Muhlen, and J. Swertfeger. Copper-silver ionization at a US hospital: interaction of treated drinking water with plumbing materials, aesthetics and other considerations.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 102: 1-10, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Simoni Triantafyllidou",
+                "hasEmail": "mailto:triantafyllidou.simoni@epa.gov"
+            },
+            "description": "Temperature, pH, chlorine, copper and silver levels at a hospital employing copper-silver ionization to control Legionella bacteria. \n\nThis dataset is associated with the following publication:\nTriantafyllidou, S., D. Lytle, C. Muhlen, and J. Swertfeger. Copper-silver ionization at a US hospital: interaction of treated drinking water with plumbing materials, aesthetics and other considerations.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 102: 1-10, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502466/SciHub%20CSI%20Upload.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub CSI Upload.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502466",
             "keyword": [
@@ -72280,20 +72284,10 @@
                 "copper pipe",
                 "porcelain staining"
             ],
-            "contactPoint": {
-                "fn": "Simoni Triantafyllidou",
-                "hasEmail": "mailto:triantafyllidou.simoni@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SciHub CSI Upload.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502466/SciHub%20CSI%20Upload.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-03",
-            "references": [
-                "http://www.sciencedirect.com/science/article/pii/S0043135416304468"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72303,40 +72297,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.sciencedirect.com/science/article/pii/S0043135416304468"
+            ],
+            "rights": null,
+            "title": "Copper Silver Ionization at a hospital dataset"
         },
         {
-            "title": "Transport of carbon nanotube-magnetite nanohybrids in water-saturated porous media",
-            "description": "Our data can be used by modeler to develop mathematical models to simulate and predict the fate and transport of the next-generation multifunctional carbon-based metal oxide nanohybrids in the subsurface environments. Furthermore, the data can also be employed to assess the potential environmental impacts and risks associated with the release and transport of carbon-based metal oxide nanohybrids in the subsurface under environmentally relevant physicochemical conditions. \n\nThis dataset is associated with the following publication:\nWang, D., C. Park, A. Masud, N. Aich, and C. Su. Carboxymethylcellulose Mediates the Transport of Carbon Nanotube-Magnetite Nanohybrid Aggregates in Water-Saturated Porous Media.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 51: 12405-12415, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1414830",
-            "keyword": [
-                "Carbon\u2014metal oxide nanohybrids",
-                "fate and transport",
-                "In situ nanoremediation"
-            ],
             "contactPoint": {
                 "fn": "Chunming Su",
                 "hasEmail": "mailto:su.chunming@epa.gov"
             },
+            "description": "Our data can be used by modeler to develop mathematical models to simulate and predict the fate and transport of the next-generation multifunctional carbon-based metal oxide nanohybrids in the subsurface environments. Furthermore, the data can also be employed to assess the potential environmental impacts and risks associated with the release and transport of carbon-based metal oxide nanohybrids in the subsurface under environmentally relevant physicochemical conditions. \n\nThis dataset is associated with the following publication:\nWang, D., C. Park, A. Masud, N. Aich, and C. Su. Carboxymethylcellulose Mediates the Transport of Carbon Nanotube-Magnetite Nanohybrid Aggregates in Water-Saturated Porous Media.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 51: 12405-12415, (2017).",
             "distribution": [
                 {
-                    "title": "Data_Wang Su ES&T Paper_2017.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1414830/Data_Wang%20Su%20ES%26T%20Paper_2017.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Data_Wang Su ES&T Paper_2017.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1414830",
+            "keyword": [
+                "Carbon\u2014metal oxide nanohybrids",
+                "fate and transport",
+                "In situ nanoremediation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-26",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b04037"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72346,19 +72340,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b04037"
+            ],
+            "rights": null,
+            "title": "Transport of carbon nanotube-magnetite nanohybrids in water-saturated porous media"
         },
         {
-            "title": "Utilization of water utility lime sludge for flue gas desulfurization in coal-fired power plants: Part I. Supply-demand evaluation and life cycle assessment",
-            "description": "The dataset contains all Tables and Figures in Excel spreadsheets. \n\nThis dataset is associated with the following publication:\nSalih, H., C. Patterson, J. Li, J. Mock, and S. Dastgheib. Utilization of water utility lime sludge for flue gas desulfurization in coal-fired power plants: Part I. Supply-demand evaluation and life cycle assessment.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA, 32(6): 6627-6633, (2018).",
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
+            "description": "The dataset contains all Tables and Figures in Excel spreadsheets. \n\nThis dataset is associated with the following publication:\nSalih, H., C. Patterson, J. Li, J. Mock, and S. Dastgheib. Utilization of water utility lime sludge for flue gas desulfurization in coal-fired power plants: Part I. Supply-demand evaluation and life cycle assessment.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA, 32(6): 6627-6633, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435433/Data%20of%20Tables%20and%20Figures%20-%20Part%201%20.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data of Tables and Figures - Part 1 .xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1435433",
             "keyword": [
@@ -72369,20 +72373,10 @@
                 "environmental impact assessment",
                 "mercury re-emission"
             ],
-            "contactPoint": {
-                "fn": "Craig Patterson",
-                "hasEmail": "mailto:patterson.craig@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data of Tables and Figures - Part 1 .xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435433/Data%20of%20Tables%20and%20Figures%20-%20Part%201%20.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-02",
-            "references": [
-                "https://doi.org/10.1021/acs.energyfuels.8b00823"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72392,19 +72386,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.energyfuels.8b00823"
+            ],
+            "rights": null,
+            "title": "Utilization of water utility lime sludge for flue gas desulfurization in coal-fired power plants: Part I. Supply-demand evaluation and life cycle assessment"
         },
         {
-            "title": "Reuse of water utility lime sludge for flue gas desulfurization in coal-fired power plants: Part II. Lime sludge characterization and mercury reemission",
-            "description": "The dataset contains all Tables and Figures in Excel spreadsheets. \n\nThis dataset is associated with the following publication:\nDastgheib, S., H. Salih, J. Li, and C. Patterson. Utilization of Water Utility Lime Sludge for Flue Gas Desulfurization in Coal-Fired Power Plants: Part II. Lime Sludge Characterization and Mercury Re-emission.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA, 32(6): 6634-6640, (2018).",
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
+            "description": "The dataset contains all Tables and Figures in Excel spreadsheets. \n\nThis dataset is associated with the following publication:\nDastgheib, S., H. Salih, J. Li, and C. Patterson. Utilization of Water Utility Lime Sludge for Flue Gas Desulfurization in Coal-Fired Power Plants: Part II. Lime Sludge Characterization and Mercury Re-emission.   ENERGY AND FUELS. American Chemical Society, Washington, DC, USA, 32(6): 6634-6640, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435434/Data%20of%20Tables%20and%20Figures%20-%20Part%202.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data of Tables and Figures - Part 2.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1435434",
             "keyword": [
@@ -72415,20 +72419,10 @@
                 "environmental impact assessment",
                 "mercury re-emission"
             ],
-            "contactPoint": {
-                "fn": "Craig Patterson",
-                "hasEmail": "mailto:patterson.craig@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data of Tables and Figures - Part 2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435434/Data%20of%20Tables%20and%20Figures%20-%20Part%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-02",
-            "references": [
-                "https://doi.org/10.1021/acs.energyfuels.8b00824"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72438,38 +72432,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.energyfuels.8b00824"
+            ],
+            "rights": null,
+            "title": "Reuse of water utility lime sludge for flue gas desulfurization in coal-fired power plants: Part II. Lime sludge characterization and mercury reemission"
         },
         {
-            "title": "Three-dimensional Free Chlorine and Monochloramine Biofilm Penetration Correlating Penetration with Biofilm Activity and Viability",
-            "description": "Data for manuscript figures. \n\nThis dataset is associated with the following publication:\nLee, W.H., J. Pressman, and D. Wahman. Three-dimensional Free Chlorine and Monochloramine Biofilm Penetration: Correlating Penetration with Biofilm Activity and Viability.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(4): 1889-1898, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1402417",
-            "keyword": [
-                "microelectrode"
-            ],
             "contactPoint": {
                 "fn": "David Wahman",
                 "hasEmail": "mailto:wahman.david@epa.gov"
             },
+            "description": "Data for manuscript figures. \n\nThis dataset is associated with the following publication:\nLee, W.H., J. Pressman, and D. Wahman. Three-dimensional Free Chlorine and Monochloramine Biofilm Penetration: Correlating Penetration with Biofilm Activity and Viability.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(4): 1889-1898, (2018).",
             "distribution": [
                 {
-                    "title": "Three-dimensional Free Chlorine and Monochloramine Biofilm Penetration Correlating Penetration with Biofilm Activity and Viability.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1402417/Three-dimensional%20Free%20Chlorine%20and%20Monochloramine%20Biofilm%20Penetration%20Correlating%20Penetration%20with%20Biofilm%20Activity%20and%20Viability.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Three-dimensional Free Chlorine and Monochloramine Biofilm Penetration Correlating Penetration with Biofilm Activity and Viability.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1402417",
+            "keyword": [
+                "microelectrode"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-07",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b05215"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72479,39 +72473,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b05215"
+            ],
+            "rights": null,
+            "title": "Three-dimensional Free Chlorine and Monochloramine Biofilm Penetration Correlating Penetration with Biofilm Activity and Viability"
         },
         {
-            "title": "Adult FHM liver gene expression - treated with EE2",
-            "description": "Male adult FHM liver treated with EE2 - gene expresssion - Agilent-036574 FHM_8x60K_V2 array design. \n\nThis dataset is associated with the following publication:\nFeswick, A., M. Isaacs, A. Biales, R. Flick, D. Bencic, R. Wang, C. Vulpe, M. Brown-Augustine, A. Loguinov, F. Falciani, P. Antczak, J. Herbert, L. Brown, N. Denslow, K. Kroll, C. Lavelle, V. Dang, L. Escalon, N. Garcia-Reyero, C. Martyniuk, and K. Munkittrick. How consistent are we? Interlaboratory comparison study in fathead minnows using the model estrogen 17\u03b1\u2010ethinylestradiol to develop recommendations for environmental transcriptomics.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 36(10): 2614-2623, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407570",
-            "keyword": [
-                "microarray",
-                "fathead minnow",
-                "gene expression"
-            ],
             "contactPoint": {
                 "fn": "Adam Biales",
                 "hasEmail": "mailto:biales.adam@epa.gov"
             },
+            "description": "Male adult FHM liver treated with EE2 - gene expresssion - Agilent-036574 FHM_8x60K_V2 array design. \n\nThis dataset is associated with the following publication:\nFeswick, A., M. Isaacs, A. Biales, R. Flick, D. Bencic, R. Wang, C. Vulpe, M. Brown-Augustine, A. Loguinov, F. Falciani, P. Antczak, J. Herbert, L. Brown, N. Denslow, K. Kroll, C. Lavelle, V. Dang, L. Escalon, N. Garcia-Reyero, C. Martyniuk, and K. Munkittrick. How consistent are we? Interlaboratory comparison study in fathead minnows using the model estrogen 17\u03b1\u2010ethinylestradiol to develop recommendations for environmental transcriptomics.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 36(10): 2614-2623, (2017).",
             "distribution": [
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/gds/?term=GSE70807%5BAccession%5D",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/gds/?term=GSE70807%5BAccession%5D"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/gds/?term=GSE70807%5BAccession%5D",
+                    "title": "https://www.ncbi.nlm.nih.gov/gds/?term=GSE70807%5BAccession%5D"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407570",
+            "keyword": [
+                "microarray",
+                "fathead minnow",
+                "gene expression"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-07-07",
-            "references": [
-                "https://doi.org/10.1002/etc.3799"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72521,40 +72515,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.3799"
+            ],
+            "rights": null,
+            "title": "Adult FHM liver gene expression - treated with EE2"
         },
         {
-            "title": "Anaerobic biodegradation",
-            "description": "Data in these tables appear in the manuscript and were used to produce the published figures. \n\nThis dataset is associated with the following publication:\nWu, S., M. Yassine, M. Suidan, and A. Venosa. Anaerobic Biodegradation of soybean biodiesel and diesel blends under sulfate-reducing conditions.  Jacob de Boer, Shane Snyder  CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 161: 382-389, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1407618",
-            "keyword": [
-                "anaerobic biodegradation",
-                "biodiesel",
-                "diesel"
-            ],
             "contactPoint": {
                 "fn": "David Kozlowski",
                 "hasEmail": "mailto:kozlowski.david@epa.gov"
             },
+            "description": "Data in these tables appear in the manuscript and were used to produce the published figures. \n\nThis dataset is associated with the following publication:\nWu, S., M. Yassine, M. Suidan, and A. Venosa. Anaerobic Biodegradation of soybean biodiesel and diesel blends under sulfate-reducing conditions.  Jacob de Boer, Shane Snyder  CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 161: 382-389, (2016).",
             "distribution": [
                 {
-                    "title": "Wu et al 2016 soybean dataset.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407618/Wu%20et%20al%202016%20soybean%20dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Wu et al 2016 soybean dataset.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407618",
+            "keyword": [
+                "anaerobic biodegradation",
+                "biodiesel",
+                "diesel"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-04",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2016.06.078"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72564,41 +72558,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2016.06.078"
+            ],
+            "rights": null,
+            "title": "Anaerobic biodegradation"
         },
         {
-            "title": "ozone hourly data at four monitoring sites",
-            "description": "contains hourly ozone and meteorological data. \n\nThis dataset is associated with the following publication:\nSchliep, E., A. Gelfand, and D. Holland. Alternating Gaussian process modulated renewal processes for modeling threshold exceedances and durations.   Stochastic Environmental Research and Risk Assessment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 32(2): 401-417, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1390106",
-            "keyword": [
-                "Ozone",
-                "ozone exceedances",
-                "frequency and duration of exceedances",
-                "NAAQS"
-            ],
             "contactPoint": {
                 "fn": "David Holland",
                 "hasEmail": "mailto:holland.david@epa.gov"
             },
+            "description": "contains hourly ozone and meteorological data. \n\nThis dataset is associated with the following publication:\nSchliep, E., A. Gelfand, and D. Holland. Alternating Gaussian process modulated renewal processes for modeling threshold exceedances and durations.   Stochastic Environmental Research and Risk Assessment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 32(2): 401-417, (2018).",
             "distribution": [
                 {
-                    "title": "EPAdataCSV.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390106/EPAdataCSV.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "EPAdataCSV.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390106",
+            "keyword": [
+                "Ozone",
+                "ozone exceedances",
+                "frequency and duration of exceedances",
+                "NAAQS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-11-04",
-            "references": [
-                "https://doi.org/10.1007/s00477-017-1417-9"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72608,39 +72602,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s00477-017-1417-9"
+            ],
+            "rights": null,
+            "title": "ozone hourly data at four monitoring sites"
         },
         {
-            "title": "Sediment accretion and accumulation of P, N and organic C in depressional wetlands of three ecoregions of the United States",
-            "description": "Data used in the paper, Nitrogen Removal in Select Palustrine Isolated Wetlands of Three Ecoregions of the United States: Mid-Atlantic Coastal Plains, Erie Drift Plain, and Southern Coastal Plain: Marine and Freshwater Research http://dx.doi.org/10.1071/MF16372. \n\nThis dataset is associated with the following publication:\nLane, C., and B. Autrey. Sediment accretion and accumulation of P, N and organic C in depressional wetlands of three ecoregions of the United States.   Marine & Freshwater Research. CSIRO Publishing, Collingwood Victoria,  AUSTRALIA, 68(12): 2253-2265, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1389608",
-            "keyword": [
-                "assimilation",
-                "cesium/caesium"
-            ],
             "contactPoint": {
                 "fn": "Charles Lane",
                 "hasEmail": "mailto:lane.charles@epa.gov"
             },
+            "description": "Data used in the paper, Nitrogen Removal in Select Palustrine Isolated Wetlands of Three Ecoregions of the United States: Mid-Atlantic Coastal Plains, Erie Drift Plain, and Southern Coastal Plain: Marine and Freshwater Research http://dx.doi.org/10.1071/MF16372. \n\nThis dataset is associated with the following publication:\nLane, C., and B. Autrey. Sediment accretion and accumulation of P, N and organic C in depressional wetlands of three ecoregions of the United States.   Marine & Freshwater Research. CSIRO Publishing, Collingwood Victoria,  AUSTRALIA, 68(12): 2253-2265, (2017).",
             "distribution": [
                 {
-                    "title": "Cesium_ResearchEffort_Data_A-x96p_08302017.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1389608/Cesium_ResearchEffort_Data_A-x96p_08302017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Cesium_ResearchEffort_Data_A-x96p_08302017.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1389608",
+            "keyword": [
+                "assimilation",
+                "cesium/caesium"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-30",
-            "references": [
-                "https://doi.org/10.1071/mf16372"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72650,67 +72644,67 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1071/mf16372"
+            ],
+            "rights": null,
+            "title": "Sediment accretion and accumulation of P, N and organic C in depressional wetlands of three ecoregions of the United States"
         },
         {
-            "title": "In Vivo PK Library for IVIVE Evaluation",
-            "description": "We report on new, in vivo TK experiments in rats for 26 chemicals more commonly associated with non-therapeutic and/or unintentional exposure. These chemicals, and an additional 19 chemicals from previously published in vivo rat studies, were systematically analyzed to estimate relevant TK parameters (e.g., volume of distribution, elimination rate). Our analysis created a library of TK parameters for 38 chemicals for which rat-specific in vitro HTTK data were also available. \n\nThis dataset is associated with the following publication:\nWambaugh, J., M. Hughes, C. Ring, D. MacMillan, J. Ford, T. Fennell, S. Black, R. Snyder, N. Sipes, B. Wetmore, J. Westerhout, W. Setzer, R. Pearce, J. Simmons, and R. Thomas. Evaluating In Vitro-In Vivo Extrapolation of Toxicokinetics.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  163(1): 152-169, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1390274",
-            "keyword": [
-                "toxicokinetics",
-                "in vitro to in vivo extrapolation (IVIVE)",
-                "Analytical chemistry",
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "We report on new, in vivo TK experiments in rats for 26 chemicals more commonly associated with non-therapeutic and/or unintentional exposure. These chemicals, and an additional 19 chemicals from previously published in vivo rat studies, were systematically analyzed to estimate relevant TK parameters (e.g., volume of distribution, elimination rate). Our analysis created a library of TK parameters for 38 chemicals for which rat-specific in vitro HTTK data were also available. \n\nThis dataset is associated with the following publication:\nWambaugh, J., M. Hughes, C. Ring, D. MacMillan, J. Ford, T. Fennell, S. Black, R. Snyder, N. Sipes, B. Wetmore, J. Westerhout, W. Setzer, R. Pearce, J. Simmons, and R. Thomas. Evaluating In Vitro-In Vivo Extrapolation of Toxicokinetics.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  163(1): 152-169, (2018).",
             "distribution": [
                 {
-                    "title": "SupplementalTables1-8.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390274/SupplementalTables1-8.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "SupplementalTables1-8.docx"
                 },
                 {
-                    "title": "TableS9-InVivoData-2017-08-10.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390274/TableS9-InVivoData-2017-08-10.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS9-InVivoData-2017-08-10.xlsx"
                 },
                 {
-                    "title": "TableS10-PropertiesandEstimates-2017-08-30.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390274/TableS10-PropertiesandEstimates-2017-08-30.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS10-PropertiesandEstimates-2017-08-30.xlsx"
                 },
                 {
-                    "title": "TableS11-TKSummaryStats-2017-08-30.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390274/TableS11-TKSummaryStats-2017-08-30.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TableS11-TKSummaryStats-2017-08-30.xlsx"
                 },
                 {
-                    "title": "FiguresS1-1compartment-Fittedgeometricmean-2017-08-29.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390274/FiguresS1-1compartment-Fittedgeometricmean-2017-08-29.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "FiguresS1-1compartment-Fittedgeometricmean-2017-08-29.pdf"
                 },
                 {
-                    "title": "FiguresS2-2compartment-Fittedgeometricmean-2017-08-29.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390274/FiguresS2-2compartment-Fittedgeometricmean-2017-08-29.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "FiguresS2-2compartment-Fittedgeometricmean-2017-08-29.pdf"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390274",
+            "keyword": [
+                "toxicokinetics",
+                "in vitro to in vivo extrapolation (IVIVE)",
+                "Analytical chemistry",
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-08",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfy020"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72720,53 +72714,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfy020"
+            ],
+            "rights": null,
+            "title": "In Vivo PK Library for IVIVE Evaluation"
         },
         {
-            "title": "High-throughput in-silico prediction of ionization equilibria for pharmacokinetic modeling",
-            "description": "Estimates of ionization equilibrium constants (i.e., pKa) were analyzed for 8,132 pharmaceuticals and 24,281 other compounds to which humans might be exposed in the environment. Results revealed broad differences in the ionization of pharmaceutical chemicals and chemicals with either near-field (in the home) or far-field sources. Probability distributions corresponding to ionizable atom types (IATs) were then used to analyze the sensitivity of predicted Vdss on predicted pKa using Monte Carlo methods. 8 of the 22 compounds were predicted to be ionizable. For 5 of the 8 the predictions based upon ionization are significantly different from what would be predicted for a neutral compound. For all but one (foramsulfuron), the probability distribution of predicted Vdss generated by IAT sensitivity analysis spans both the neutral prediction and the prediction using ionization. \n\nThis dataset is associated with the following publication:\nStrope, C., K. Mansouri, H. Clewell, J. Rabinowitz, C. Stevens, and J. Wambaugh. High-Throughput in-silico prediction of ionization equilibria for pharmacokinetic modeling.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 615: 150-160, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1391808",
-            "keyword": [
-                "ionization",
-                "pKa",
-                "physiologically-based pharmacokinetic model",
-                "PBPK model",
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "Estimates of ionization equilibrium constants (i.e., pKa) were analyzed for 8,132 pharmaceuticals and 24,281 other compounds to which humans might be exposed in the environment. Results revealed broad differences in the ionization of pharmaceutical chemicals and chemicals with either near-field (in the home) or far-field sources. Probability distributions corresponding to ionizable atom types (IATs) were then used to analyze the sensitivity of predicted Vdss on predicted pKa using Monte Carlo methods. 8 of the 22 compounds were predicted to be ionizable. For 5 of the 8 the predictions based upon ionization are significantly different from what would be predicted for a neutral compound. For all but one (foramsulfuron), the probability distribution of predicted Vdss generated by IAT sensitivity analysis spans both the neutral prediction and the prediction using ionization. \n\nThis dataset is associated with the following publication:\nStrope, C., K. Mansouri, H. Clewell, J. Rabinowitz, C. Stevens, and J. Wambaugh. High-Throughput in-silico prediction of ionization equilibria for pharmacokinetic modeling.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 615: 150-160, (2018).",
             "distribution": [
                 {
-                    "title": "32k_fingerprints.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1391808/32k_fingerprints.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "32k_fingerprints.xlsx"
                 },
                 {
-                    "title": "32k_pKa_prediction-20150414.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1391808/32k_pKa_prediction-20150414.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "32k_pKa_prediction-20150414.xlsx"
                 },
                 {
-                    "title": "PBPKxIon-20170918T145752Z-001-small.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1391808/PBPKxIon-20170918T145752Z-001-small.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "PBPKxIon-20170918T145752Z-001-small.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1391808",
+            "keyword": [
+                "ionization",
+                "pKa",
+                "physiologically-based pharmacokinetic model",
+                "PBPK model",
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-18",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2017.09.033"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72776,46 +72770,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2017.09.033"
+            ],
+            "rights": null,
+            "title": "High-throughput in-silico prediction of ionization equilibria for pharmacokinetic modeling"
         },
         {
-            "title": "Raw Measurements and Predicted Concentrations for Water Samples from Cape Fear Watershed (May - July 2017)",
-            "description": "Measured and estimated concentrations of HFPO-DA and related perfluoroether compounds in the Cape Fear River as measured at multiple water treatment facilities in the watershed by QqQ LC-MS quantification. \n\nThis dataset is associated with the following publication:\nMcCord, J., S. Newton, and M. Strynar. Validation of quantitative measurements and semi-quantitative estimates of emerging perfluoroethercarboxylic acids (PFECAs) and hexfluoroprolyene oxide acids (HFPOAs).   JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1551: 52-58, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1408902",
-            "keyword": [
-                "GenX",
-                "HFPO-DA",
-                "Cape Fear River",
-                "perfluorinated ether",
-                "LC-MS"
-            ],
             "contactPoint": {
                 "fn": "James McCord",
                 "hasEmail": "mailto:mccord.james@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1408902/documents/Data%20Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Measured and estimated concentrations of HFPO-DA and related perfluoroether compounds in the Cape Fear River as measured at multiple water treatment facilities in the watershed by QqQ LC-MS quantification. \n\nThis dataset is associated with the following publication:\nMcCord, J., S. Newton, and M. Strynar. Validation of quantitative measurements and semi-quantitative estimates of emerging perfluoroethercarboxylic acids (PFECAs) and hexfluoroprolyene oxide acids (HFPOAs).   JOURNAL OF CHROMATOGRAPHY A. Elsevier Science Ltd, New York, NY, USA, 1551: 52-58, (2018).",
             "distribution": [
                 {
-                    "title": "Raw Measurements and Predicted Concentrations for LC-MSMS of PFECAs.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408902/Raw%20Measurements%20and%20Predicted%20Concentrations%20for%20LC-MSMS%20of%20PFECAs.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Raw Measurements and Predicted Concentrations for LC-MSMS of PFECAs.csv"
                 },
                 {
-                    "title": "https://deq.nc.gov/news/hot-topics/genx-investigation/genx-sampling-sites",
-                    "accessURL": "https://deq.nc.gov/news/hot-topics/genx-investigation/genx-sampling-sites"
+                    "accessURL": "https://deq.nc.gov/news/hot-topics/genx-investigation/genx-sampling-sites",
+                    "title": "https://deq.nc.gov/news/hot-topics/genx-investigation/genx-sampling-sites"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1408902",
+            "keyword": [
+                "GenX",
+                "HFPO-DA",
+                "Cape Fear River",
+                "perfluorinated ether",
+                "LC-MS"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-16",
-            "references": [
-                "https://doi.org/10.1016/j.chroma.2018.03.047"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72826,41 +72822,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1408902/documents/Data%20Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.chroma.2018.03.047"
+            ],
+            "rights": null,
+            "title": "Raw Measurements and Predicted Concentrations for Water Samples from Cape Fear Watershed (May - July 2017)"
         },
         {
-            "title": "Microcystin Congener octanol-water phase concentration measurements for pH dependent partitioning",
-            "description": "Measured concentrations in octanol-water phase partitioning of microcystin congeners. \n\nThis dataset is associated with the following publication:\nMcCord, J., J. Lang, D. Hill, M. Strynar, and N. Chernoff. pH dependent octanol\u2013water partitioning coefficients of microcystin congeners.   JOURNAL OF WATER AND HEALTH. IWA Publishing, London,  UK, 16(3): 340-345, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407664",
-            "keyword": [
-                "microcystin",
-                "cyanobacterial toxin",
-                "octanol-water partition coefficient"
-            ],
             "contactPoint": {
                 "fn": "James McCord",
                 "hasEmail": "mailto:mccord.james@epa.gov"
             },
+            "description": "Measured concentrations in octanol-water phase partitioning of microcystin congeners. \n\nThis dataset is associated with the following publication:\nMcCord, J., J. Lang, D. Hill, M. Strynar, and N. Chernoff. pH dependent octanol\u2013water partitioning coefficients of microcystin congeners.   JOURNAL OF WATER AND HEALTH. IWA Publishing, London,  UK, 16(3): 340-345, (2018).",
             "distribution": [
                 {
-                    "title": "Log Kow Raws.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407664/Log%20Kow%20Raws.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Log Kow Raws.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407664",
+            "keyword": [
+                "microcystin",
+                "cyanobacterial toxin",
+                "octanol-water partition coefficient"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-04",
-            "references": [
-                "https://doi.org/10.2166/wh.2018.257"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72870,42 +72864,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2166/wh.2018.257"
+            ],
+            "rights": null,
+            "title": "Microcystin Congener octanol-water phase concentration measurements for pH dependent partitioning"
         },
         {
-            "title": "Characterization of Aerosol Nitro Aromatic Compounds Validation of an Experimental Method",
-            "description": "The analytical capabilities associated with the use of silylation reactions have been extended to a new class of organic molecules, nitroaromatic compounds (NACs). These compounds are a possible contributor to urban particulate matter of secondary origin which would make them important analytes due to their (1) detrimental health effects, (2) potential to affect aerosol optical properties, (3) and usefulness for identifying PM2.5 from biomass burning. The technique is based on derivatization of the parent NACs using N,O-bis-(trimethylsilyl)-trifluoro acetamide, one of the most prevalent derivatization reagent for analyzing hydroxylated molecules, followed by GC-MS using electron ionization (EI) and methane chemical ionization (CI). This method is evaluated for 32 NACs including nitrophenols, methyl-/methoxy-nitrophenols, nitrobenzoic acids, and nitrobenzyl alcohols. EI spectra were characterized by a high abundance of ions corresponding to [M+.], or [M+ - 15]. CI spectra exhibited high abundance for [M+ + 1], [M+ - 15], and [M+ + 29] ions. Both EI and CI spectra exhibit ions specific to nitro group(s) for [M+. - 31], [M+. - 45], and [M+. - 60]. The strong abundance observed for [M+.] (EI), [M+ - 15] (EI/CI), or [M+ + 1] (CI) ions is consistent with the high charge stabilizing ability associated with aromatic compounds. The combination of EI and CI ionization offers strong capabilities for detection and identification of NACs. Spectra associated with NACs, containing hydrogen, carbon, oxygen, and nitrogen atoms only, as silylated derivatives show fragment/adduct ions at either (a) odd or (b) even masses that indicate either (a) odd or (b) even number of nitro groups, respectively. Mass spectra associated with silylated NACs exhibited three distinct regions where characteristic fragmentation with a specific pattern associated with: (1) -OH, and/or -COOH groups, (2) -NO2 group(s), and (3) benzene ring(s). These findings were confirmed with applications to chamber aerosol and ambient PM2.5. \n\nThis dataset is associated with the following publication:\nJaoui, M., M. Lewandowski, J. Offenberg, M. Colon, K. Docherty, and T. Kleindienst. Characterization of aerosol nitroaromatic compounds: Validation of an experimental method.   Journal of Mass Spectrometry. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 53(8): 680-692, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1416545",
-            "keyword": [
-                "Nitroaromatics",
-                "air quality",
-                "Secondary Organic Aerosol",
-                "air toxics",
-                "Ozone"
-            ],
             "contactPoint": {
                 "fn": "Michael Lewandowski",
                 "hasEmail": "mailto:lewandowski.michael@epa.gov"
             },
+            "description": "The analytical capabilities associated with the use of silylation reactions have been extended to a new class of organic molecules, nitroaromatic compounds (NACs). These compounds are a possible contributor to urban particulate matter of secondary origin which would make them important analytes due to their (1) detrimental health effects, (2) potential to affect aerosol optical properties, (3) and usefulness for identifying PM2.5 from biomass burning. The technique is based on derivatization of the parent NACs using N,O-bis-(trimethylsilyl)-trifluoro acetamide, one of the most prevalent derivatization reagent for analyzing hydroxylated molecules, followed by GC-MS using electron ionization (EI) and methane chemical ionization (CI). This method is evaluated for 32 NACs including nitrophenols, methyl-/methoxy-nitrophenols, nitrobenzoic acids, and nitrobenzyl alcohols. EI spectra were characterized by a high abundance of ions corresponding to [M+.], or [M+ - 15]. CI spectra exhibited high abundance for [M+ + 1], [M+ - 15], and [M+ + 29] ions. Both EI and CI spectra exhibit ions specific to nitro group(s) for [M+. - 31], [M+. - 45], and [M+. - 60]. The strong abundance observed for [M+.] (EI), [M+ - 15] (EI/CI), or [M+ + 1] (CI) ions is consistent with the high charge stabilizing ability associated with aromatic compounds. The combination of EI and CI ionization offers strong capabilities for detection and identification of NACs. Spectra associated with NACs, containing hydrogen, carbon, oxygen, and nitrogen atoms only, as silylated derivatives show fragment/adduct ions at either (a) odd or (b) even masses that indicate either (a) odd or (b) even number of nitro groups, respectively. Mass spectra associated with silylated NACs exhibited three distinct regions where characteristic fragmentation with a specific pattern associated with: (1) -OH, and/or -COOH groups, (2) -NO2 group(s), and (3) benzene ring(s). These findings were confirmed with applications to chamber aerosol and ambient PM2.5. \n\nThis dataset is associated with the following publication:\nJaoui, M., M. Lewandowski, J. Offenberg, M. Colon, K. Docherty, and T. Kleindienst. Characterization of aerosol nitroaromatic compounds: Validation of an experimental method.   Journal of Mass Spectrometry. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 53(8): 680-692, (2018).",
             "distribution": [
                 {
-                    "title": "Jaoui et al NACs Figure Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1416545/Jaoui%20et%20al%20NACs%20Figure%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Jaoui et al NACs Figure Data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1416545",
+            "keyword": [
+                "Nitroaromatics",
+                "air quality",
+                "Secondary Organic Aerosol",
+                "air toxics",
+                "Ozone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-01",
-            "references": [
-                "https://doi.org/10.1002/jms.4199"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72915,40 +72909,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/jms.4199"
+            ],
+            "rights": null,
+            "title": "Characterization of Aerosol Nitro Aromatic Compounds Validation of an Experimental Method"
         },
         {
-            "title": "Data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Influence of anthropogenic emissions and boundary conditions on multi-model simulations of major air pollutants over Europe and North America in the framework of AQMEII3\"",
-            "description": "This dataset contains the data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Influence of anthropogenic emissions and boundary conditions on multi-model simulations of major air pollutants over Europe and North America in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Christensen, C. Geels, K. Hansen, J. Brandt, E. Solazzo, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, P. Liu, U. Nopmongcol, L. Palacios-Pe\u00f1a, G. Pirovano, L. Pozolli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, G. Yarwood, C. Hogrefe, and S. Galmarini. Influence of anthropogenic emissions and boundary conditions on multi-model simulations of major air pollutants over Europe and North America in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 8929-8952, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1434306",
-            "keyword": [
-                "model evaluation",
-                "ensemble modeling",
-                "emission sensitivity",
-                "long-range transport"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434306/documents/HogrefeChristian_A-d25k_DataDescription_ImEtAl.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains the data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Influence of anthropogenic emissions and boundary conditions on multi-model simulations of major air pollutants over Europe and North America in the framework of AQMEII3\" led by Dr. Ulas Im of Aarhus University in Denmark. \n\nThis dataset is associated with the following publication:\nIm, U., J. Christensen, C. Geels, K. Hansen, J. Brandt, E. Solazzo, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, R. Bianconi, J. Bieser, A. Colette, G. Curci, A. Farrow, J. Flemming, A. Fraser, P. Jimenez-Guerrero, N. Kitwiroon, P. Liu, U. Nopmongcol, L. Palacios-Pe\u00f1a, G. Pirovano, L. Pozolli, M. Prank, R. Rose, R. Sokhi, P. Tuccella, A. Unal, M. Garcia Vivanco, G. Yarwood, C. Hogrefe, and S. Galmarini. Influence of anthropogenic emissions and boundary conditions on multi-model simulations of major air pollutants over Europe and North America in the framework of AQMEII3.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 8929-8952, (2018).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/exposure/A-d25k/",
-                    "accessURL": "https://gaftp.epa.gov/exposure/A-d25k/"
+                    "accessURL": "https://gaftp.epa.gov/exposure/A-d25k/",
+                    "title": "https://gaftp.epa.gov/exposure/A-d25k/"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434306",
+            "keyword": [
+                "model evaluation",
+                "ensemble modeling",
+                "emission sensitivity",
+                "long-range transport"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-8929-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -72959,42 +72955,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434306/documents/HogrefeChristian_A-d25k_DataDescription_ImEtAl.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-18-8929-2018"
+            ],
+            "rights": null,
+            "title": "Data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Influence of anthropogenic emissions and boundary conditions on multi-model simulations of major air pollutants over Europe and North America in the framework of AQMEII3\""
         },
         {
-            "title": "Data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Two-scale multi-model ensemble: Is a hybrid ensemble of opportunity telling us more?\"",
-            "description": "This dataset contains the data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Two-scale multi-model ensemble: Is a hybrid ensemble of opportunity telling us more?\" led by Dr. Stefano Galmarini of the European Commission's Joint Research Center. \n\nThis dataset is associated with the following publication:\nGalmarini, S., I. Kioutsioukis, E. Solazzo, U. Alyuz, A. Balzarini, R. Bellasio, A. Benedictow, R. Bianconi, J. Bieser, J. Brandt, J. Christensen, A. Colette, G. Curci, Y. Davila, X. Dong, J. Flemming, X. Francis, A. Fraser, J. Fu, D. Henze, C. Hogrefe, U. Im, M. Garcia Vivanco, P. Jimenez-Guerrero, J. Jonson, N. Kitwiroon, A. Manders, R. Mathur, L. Palacios-Pena, G. Pirovano, L. Pozzoli, M. Prank, M. Schultz, R. Sokhi, K. Sudo, P. Tuccella, T. Takemura, T. Sekiya, and A. Unal. Two-scale multi-model ensemble: is a hybrid ensemble of opportunity telling us more?.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 8727-8744, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1434299",
-            "keyword": [
-                "ensemble modeling",
-                "global ozone modeling",
-                "regional ozone modeling",
-                "categorical evaluation"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "description": "This dataset contains the data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Two-scale multi-model ensemble: Is a hybrid ensemble of opportunity telling us more?\" led by Dr. Stefano Galmarini of the European Commission's Joint Research Center. \n\nThis dataset is associated with the following publication:\nGalmarini, S., I. Kioutsioukis, E. Solazzo, U. Alyuz, A. Balzarini, R. Bellasio, A. Benedictow, R. Bianconi, J. Bieser, J. Brandt, J. Christensen, A. Colette, G. Curci, Y. Davila, X. Dong, J. Flemming, X. Francis, A. Fraser, J. Fu, D. Henze, C. Hogrefe, U. Im, M. Garcia Vivanco, P. Jimenez-Guerrero, J. Jonson, N. Kitwiroon, A. Manders, R. Mathur, L. Palacios-Pena, G. Pirovano, L. Pozzoli, M. Prank, M. Schultz, R. Sokhi, K. Sudo, P. Tuccella, T. Takemura, T. Sekiya, and A. Unal. Two-scale multi-model ensemble: is a hybrid ensemble of opportunity telling us more?.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 8727-8744, (2018).",
             "distribution": [
                 {
-                    "title": "HogrefeChristian_A-pnwj_DataSet.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434299/HogrefeChristian_A-pnwj_DataSet.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "HogrefeChristian_A-pnwj_DataSet.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434299",
+            "keyword": [
+                "ensemble modeling",
+                "global ozone modeling",
+                "regional ozone modeling",
+                "categorical evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-01",
-            "references": [
-                "https://doi.org/10.5194/acp-18-8727-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73004,41 +72998,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-18-8727-2018"
+            ],
+            "rights": null,
+            "title": "Data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Two-scale multi-model ensemble: Is a hybrid ensemble of opportunity telling us more?\""
         },
         {
-            "title": "Citizen Science sensor measurements to support frequently asked questions (FAQ)",
-            "description": "This file has two sheets. Data are measurements by Citizen Science Air Monitors (CSAM) and Federal Monitors, which sampled particulate matter (PM), nitrogen dioxide (NO2), relative humidity (RH), and temperature (T). Variables for each sheet are described in more detail below\nThe sheet \u201cSnorkel No-Snorkel Comparison\u201d includes data from two CSAM units, CSAM-2 and CSAM-3. CSAM-2 used a snorkel tube to sample outdoor air, and CSAM-3 did not use a snorkel tube. CSAM-2 and CSAM-3 were not in the same sampling location, but did sample contemporaneous measurements. These data were used to perform a snorkel and no-snorkel comparison. \nThe sheet \u201cCSAM-1 and Federal Monitor\u201d includes data from a CSAM unit (CSAM-1) and a Federal Monitor (which is used for regulatory measurements of air pollution). CSAM-1 and the Federal Monitor were installed in the same sampling location and recorded contemporaneous measurements. For CSAM-1, original recorded measurements are included, as well as measurements that were corrected (using regression equations) to better reflect the Federal Monitor values. \n\nThis dataset is associated with the following publication:\nBarzyk, T., H. Huang, R. Williams, A. Kaufman, and J. Essoka. Advice and Frequently Asked Questions (FAQs) for Citizen-Science Environmental Health Assessments.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 15(5): 960, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1433814",
-            "keyword": [
-                "Environmental health assessment",
-                "Decision analysis",
-                "Local stakeholders",
-                "Cumulative impacts"
-            ],
             "contactPoint": {
                 "fn": "Timothy Barzyk",
                 "hasEmail": "mailto:barzyk.timothy@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1433814/documents/BarzykTimothy_A-msc0_DataDictionary_20180419.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This file has two sheets. Data are measurements by Citizen Science Air Monitors (CSAM) and Federal Monitors, which sampled particulate matter (PM), nitrogen dioxide (NO2), relative humidity (RH), and temperature (T). Variables for each sheet are described in more detail below\nThe sheet \u201cSnorkel No-Snorkel Comparison\u201d includes data from two CSAM units, CSAM-2 and CSAM-3. CSAM-2 used a snorkel tube to sample outdoor air, and CSAM-3 did not use a snorkel tube. CSAM-2 and CSAM-3 were not in the same sampling location, but did sample contemporaneous measurements. These data were used to perform a snorkel and no-snorkel comparison. \nThe sheet \u201cCSAM-1 and Federal Monitor\u201d includes data from a CSAM unit (CSAM-1) and a Federal Monitor (which is used for regulatory measurements of air pollution). CSAM-1 and the Federal Monitor were installed in the same sampling location and recorded contemporaneous measurements. For CSAM-1, original recorded measurements are included, as well as measurements that were corrected (using regression equations) to better reflect the Federal Monitor values. \n\nThis dataset is associated with the following publication:\nBarzyk, T., H. Huang, R. Williams, A. Kaufman, and J. Essoka. Advice and Frequently Asked Questions (FAQs) for Citizen-Science Environmental Health Assessments.   International Journal of Environmental Research and Public Health. Molecular Diversity Preservation International, Basel,  SWITZERLAND, 15(5): 960, (2018).",
             "distribution": [
                 {
-                    "title": "BarzykTimothy_A-msc0_Datasets_20180419.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1433814/BarzykTimothy_A-msc0_Datasets_20180419.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "BarzykTimothy_A-msc0_Datasets_20180419.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1433814",
+            "keyword": [
+                "Environmental health assessment",
+                "Decision analysis",
+                "Local stakeholders",
+                "Cumulative impacts"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-01",
-            "references": [
-                "https://doi.org/10.3390/ijerph15050960"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73049,20 +73045,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1433814/documents/BarzykTimothy_A-msc0_DataDictionary_20180419.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.3390/ijerph15050960"
+            ],
+            "rights": null,
+            "title": "Citizen Science sensor measurements to support frequently asked questions (FAQ)"
         },
         {
-            "title": "Data file field studies aerosolized endotoxins biosolids application 2010 and 2012",
-            "description": "The dataset consists of columns of values and labels of data collected by air samplers for endotoxin monitoring during the full scale/commercial scale land application of Class B biosolids. The biosolids came from different anaerobic treatment facilities and some material was later treated with lime 24 hours prior to application. \n\nThis dataset is associated with the following publication:\nHerrmann , R., R. Grosser, D. Farrar , and B. Brobst. Field studies measuring the aerosolization of endotoxin during the land application of Class B biosolids.  Carmen Galan  AEROBIOLOGIA. Springer, New York, NY, USA, 0(0): 1-18, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Ronald Herrmann",
+                "hasEmail": "mailto:herrmann.ronald@epa.gov"
+            },
+            "description": "The dataset consists of columns of values and labels of data collected by air samplers for endotoxin monitoring during the full scale/commercial scale land application of Class B biosolids. The biosolids came from different anaerobic treatment facilities and some material was later treated with lime 24 hours prior to application. \n\nThis dataset is associated with the following publication:\nHerrmann , R., R. Grosser, D. Farrar , and B. Brobst. Field studies measuring the aerosolization of endotoxin during the land application of Class B biosolids.  Carmen Galan  AEROBIOLOGIA. Springer, New York, NY, USA, 0(0): 1-18, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500910/Data%20file%20field%20studies%20aerosolized%20endotoxins%20biosolids%20app.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data file field studies aerosolized endotoxins biosolids app.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500910",
             "keyword": [
@@ -73073,20 +73077,10 @@
                 "land application",
                 "limulus amebocyte lysate"
             ],
-            "contactPoint": {
-                "fn": "Ronald Herrmann",
-                "hasEmail": "mailto:herrmann.ronald@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data file field studies aerosolized endotoxins biosolids app.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500910/Data%20file%20field%20studies%20aerosolized%20endotoxins%20biosolids%20app.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-08-27",
-            "references": [
-                "https://doi.org/10.1007/s10453-017-9480-8"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73096,46 +73090,48 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10453-017-9480-8"
+            ],
+            "rights": null,
+            "title": "Data file field studies aerosolized endotoxins biosolids application 2010 and 2012"
         },
         {
-            "title": "Data used in the research titled, \"Quantifying the visual-sensory landscapes qualities that contribute to cultural ecosystem services using social media and LiDAR\"",
-            "description": "Sample1m are the data used to estimate the Negative Binomial models. The validation dataset compares classified photographs with viewshed estimates of visible land use/cover. \n\nThis dataset is associated with the following publication:\nVanBerkel, D., P. Tabrizian, M.A. Dorning, L. Smart, D. Newcomb, M. Mehaffey, A. Neale, and R.K. Meentemeyer. Quantifying the visual-sensory landscape qualities that contribute to cultural ecosystem services using social media and LiDAR.   Ecosystem Services. Elsevier Online, New York, NY, USA, 31: 326-335, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1433620",
-            "keyword": [
-                "Cultural Ecosystem Services",
-                "Spatial Analysis",
-                "Coastal Scenery",
-                "social media"
-            ],
             "contactPoint": {
                 "fn": "Derek Van Berkel",
                 "hasEmail": "mailto:van-berkel.derek@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1433620/documents/VariableDescription.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Sample1m are the data used to estimate the Negative Binomial models. The validation dataset compares classified photographs with viewshed estimates of visible land use/cover. \n\nThis dataset is associated with the following publication:\nVanBerkel, D., P. Tabrizian, M.A. Dorning, L. Smart, D. Newcomb, M. Mehaffey, A. Neale, and R.K. Meentemeyer. Quantifying the visual-sensory landscape qualities that contribute to cultural ecosystem services using social media and LiDAR.   Ecosystem Services. Elsevier Online, New York, NY, USA, 31: 326-335, (2018).",
             "distribution": [
                 {
-                    "title": "SampleNB.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1433620/SampleNB.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SampleNB.csv"
                 },
                 {
-                    "title": "ValidationViewshed.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1433620/ValidationViewshed.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ValidationViewshed.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1433620",
+            "keyword": [
+                "Cultural Ecosystem Services",
+                "Spatial Analysis",
+                "Coastal Scenery",
+                "social media"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-19",
-            "references": [
-                "https://doi.org/10.1016/j.ecoser.2018.03.022"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73146,20 +73142,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1433620/documents/VariableDescription.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.ecoser.2018.03.022"
+            ],
+            "rights": null,
+            "title": "Data used in the research titled, \"Quantifying the visual-sensory landscapes qualities that contribute to cultural ecosystem services using social media and LiDAR\""
         },
         {
-            "title": "amphibian_dehydration_uptake_data",
-            "description": "Bioconcentration data for Glinski DA, Henderson WM, Van Meter RJ, Purucker ST 2017. Effect of hydration status on pesticide uptake in anurans following exposure to contaminated soils. \n\nThis dataset is associated with the following publication:\nGlinski, D., M. Henderson, R. Van Meter, and T. Purucker. Effect of hydration status on pesticide uptake in anurans following exposure to contaminated soils.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 25(16): 16192-16201, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Steven Purucker",
+                "hasEmail": "mailto:purucker.tom@epa.gov"
+            },
+            "description": "Bioconcentration data for Glinski DA, Henderson WM, Van Meter RJ, Purucker ST 2017. Effect of hydration status on pesticide uptake in anurans following exposure to contaminated soils. \n\nThis dataset is associated with the following publication:\nGlinski, D., M. Henderson, R. Van Meter, and T. Purucker. Effect of hydration status on pesticide uptake in anurans following exposure to contaminated soils.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 25(16): 16192-16201, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://github.com/puruckertom/glinski_dehydration/tree/master/csv_in",
+                    "title": "https://github.com/puruckertom/glinski_dehydration/tree/master/csv_in"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407571",
             "keyword": [
@@ -73169,19 +73172,10 @@
                 "body burden",
                 "uptake"
             ],
-            "contactPoint": {
-                "fn": "Steven Purucker",
-                "hasEmail": "mailto:purucker.tom@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://github.com/puruckertom/glinski_dehydration/tree/master/csv_in",
-                    "accessURL": "https://github.com/puruckertom/glinski_dehydration/tree/master/csv_in"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-17",
-            "references": [
-                "https://doi.org/10.1007/s11356-018-1830-8"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73191,50 +73185,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11356-018-1830-8"
+            ],
+            "rights": null,
+            "title": "amphibian_dehydration_uptake_data"
         },
         {
-            "title": "Gerties Creek Proper Functioning Condition Data Forms",
-            "description": "These are Proper Functioning Condition Reach Information Forms filled out during our assessment at Georgina Island.  The forms are from the Technical Reference 1737-15 Second Edition 2015 from BLM, Forest Service and NRCS.  Dickard et al., 2015. \n\nThis dataset is associated with the following publication:\nHall, R., J. Lin, B. Schumacher, K. Charles, and D. Heggem. Ecological risk based assessment used to restore riparian physical functions to a fresh water Creek.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 221: 63-75, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1407681",
-            "keyword": [
-                "Lotic Reach Assessment",
-                "Lentic Reach Assessment",
-                "Tribal Sustainability",
-                "proper functioning condition",
-                "ecological condition assessment",
-                "Environmenal health",
-                "Ecological Health",
-                "Vulnerable Groups"
-            ],
             "contactPoint": {
                 "fn": "Daniel Heggem",
                 "hasEmail": "mailto:heggem.daniel@epa.gov"
             },
+            "description": "These are Proper Functioning Condition Reach Information Forms filled out during our assessment at Georgina Island.  The forms are from the Technical Reference 1737-15 Second Edition 2015 from BLM, Forest Service and NRCS.  Dickard et al., 2015. \n\nThis dataset is associated with the following publication:\nHall, R., J. Lin, B. Schumacher, K. Charles, and D. Heggem. Ecological risk based assessment used to restore riparian physical functions to a fresh water Creek.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 221: 63-75, (2018).",
             "distribution": [
                 {
-                    "title": "Gerties Creek Data_ScienceHub.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407681/Gerties%20Creek%20Data_ScienceHub.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Gerties Creek Data_ScienceHub.docx"
                 },
                 {
-                    "title": "Gerties Creek Data_ScienceHub2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407681/Gerties%20Creek%20Data_ScienceHub2.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Gerties Creek Data_ScienceHub2.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407681",
+            "keyword": [
+                "Lotic Reach Assessment",
+                "Lentic Reach Assessment",
+                "Tribal Sustainability",
+                "proper functioning condition",
+                "ecological condition assessment",
+                "Environmenal health",
+                "Ecological Health",
+                "Vulnerable Groups"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-24",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2018.03.117"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73244,19 +73238,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2018.03.117"
+            ],
+            "rights": null,
+            "title": "Gerties Creek Proper Functioning Condition Data Forms"
         },
         {
-            "title": "Electrolyte Selection for Electrochemical Oxidative Water Treatment Using a Boron-Doped Diamond Anode to Support Site Specific Contamination Incident Response",
-            "description": "The dataset contains the raw data for the graphs in the paper. \n\nThis dataset is associated with the following publication:\nPhillips, R., R. James, and M. Magnuson. Electrolyte Selection and Microbial Toxicity for Electrochemical Oxidative Water Treatment Using a Boron-doped Diamond Anode to Support Site Specific Contamination Incident Response.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 197: 135-141, (2017).",
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
+            "description": "The dataset contains the raw data for the graphs in the paper. \n\nThis dataset is associated with the following publication:\nPhillips, R., R. James, and M. Magnuson. Electrolyte Selection and Microbial Toxicity for Electrochemical Oxidative Water Treatment Using a Boron-doped Diamond Anode to Support Site Specific Contamination Incident Response.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 197: 135-141, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407534/MagnusonMatthew_A-7wmb_data_20170410.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MagnusonMatthew_A-7wmb_data_20170410.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407534",
             "keyword": [
@@ -73269,20 +73273,10 @@
                 "PFAS",
                 "perfluorinated"
             ],
-            "contactPoint": {
-                "fn": "Matthew Magnuson",
-                "hasEmail": "mailto:magnuson.matthew@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MagnusonMatthew_A-7wmb_data_20170410.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407534/MagnusonMatthew_A-7wmb_data_20170410.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-03",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2018.01.007"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73292,19 +73286,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2018.01.007"
+            ],
+            "rights": null,
+            "title": "Electrolyte Selection for Electrochemical Oxidative Water Treatment Using a Boron-Doped Diamond Anode to Support Site Specific Contamination Incident Response"
         },
         {
-            "title": "Cesium Emissions from Laboratory Fires",
-            "description": "The data sets contain the raw and reduced data from the instrument measurements including continuous emission monitoring and stack sampling procedure. \n\nThis dataset is associated with the following publication:\nHao, W.M., S. Baker, E. Lincoln, S. Hudson, S. Lee, and P. Lemieux. Cesium Emissions from Laboratory Fires Article.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA,  49, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
+            "contactPoint": {
+                "fn": "Sangdon Lee",
+                "hasEmail": "mailto:lee.sangdon@epa.gov"
+            },
+            "description": "The data sets contain the raw and reduced data from the instrument measurements including continuous emission monitoring and stack sampling procedure. \n\nThis dataset is associated with the following publication:\nHao, W.M., S. Baker, E. Lincoln, S. Hudson, S. Lee, and P. Lemieux. Cesium Emissions from Laboratory Fires Article.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA,  49, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1377064/Cs_CEM_data_06152017.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Cs_CEM_data_06152017.xlsx"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1377064/Missoula%20Cs%20Mass%20Calculations%20w%20ICPMS%20041717.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Missoula Cs Mass Calculations w ICPMS 041717.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1377064",
             "keyword": [
@@ -73324,25 +73333,10 @@
                 "pm2.5",
                 "radionuclides"
             ],
-            "contactPoint": {
-                "fn": "Sangdon Lee",
-                "hasEmail": "mailto:lee.sangdon@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Cs_CEM_data_06152017.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1377064/Cs_CEM_data_06152017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "Missoula Cs Mass Calculations w ICPMS 041717.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1377064/Missoula%20Cs%20Mass%20Calculations%20w%20ICPMS%20041717.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-15",
-            "references": [
-                "https://doi.org/10.1080/10962247.2018.1493001"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73352,19 +73346,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10962247.2018.1493001"
+            ],
+            "rights": null,
+            "title": "Cesium Emissions from Laboratory Fires"
         },
         {
-            "title": "National Aquatic Resources Survey datasets",
-            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data. \n\nThis dataset is associated with the following publications:\nStoddard , J., J. Van Sickle, A. Herlihy, J. Brahney, S. Paulsen , D. Peck , R. Mitchell , and A. Pollard. Continental-scale increase in stream and lake phosphorus: Are oligotrophic systems disappearing in the U.S.?.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(7): 3409-3415, (2016).\nHerlihy, A., M. Kentula, T. Magee, G. Lomnicky, A. Nahlik, and G. Serenbetz. Striving for consistency in the National Wetland Condition Assessment: developing a reference condition approach for assessing wetlands at a continental scale.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 327, (2019).\nMagee, T., K. Blocksom, and S. Fennessy. A national-scale vegetation multimetric index (VMMI) as an indicator of wetland condition across the conterminous United States..   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 322, (2019).\nHerlihy, A., J. Sifneos, G. Lomnicky, A. Nahlik, M. Kentula, T. Magee, M. Weber, and A. Trebitz. The response of wetland quality indicators to human disturbance indicators across the United States.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 296, (2019).\nHerlihy, A., S. Paulsen, M. Kentula, T. Magee, A. Nahlik, and G. Lomnicky. Assessing the relative and attributable risk of stressors to wetland condition across the conterminous United States.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 320, (2019).\nLomnicky, G., A.T. Herlihy, and P. Kaufmann. Quantifying the extent of human disturbance activities and anthropogenic stressors in wetlands across the conterminous United States: results from the National Wetland Condition Assessment.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 324, (2019).\nBowen, G., A. Putman, J.R. Brooks, D. Bowling, E. Oerter, and S. Good. Inferring the source of evaporated waters using stable H and O isotopes..   OECOLOGIA. Springer, New York, NY, USA, 187(4): 1025-1039, (2018).\nFox, E., J. Ver Hoef, and T. Olsen. Comparing Spatial Regression to Random Forests for Large Environmental Data Sets..   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 15(3): e0229509, (2020).\nNahlik, A., K. Blocksom, A. Herlihy, M. Kentula, T. Magee, and S. Paulsen. Use of national-scale data to examine human-mediated additions of heavy metals to wetland soils of the US.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 336, (2019).\nKentula, M., and S. Paulsen. The 2011 National Wetland Condition Assessment: Overview and an Invitation.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA,  325, (2019).\nMagee, T., K. Blocksom, A. Herlihy, and A. Nahlik. Characterizing nonnative plants in wetlands across the conterminous United States.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 344, (2019).\nFeio, M., R. Hughes, M. Callisto, S.J. Nichols, O.N. Odume, B.R. Quintella, M. Kuemmerlen, F.C. Aguiar, S.F.P. Almeida, P. Alonso-Egu\u00edaLis , F.O. Arimoro, F.J. Dyer , J.S. Harding , S. Jang , P. Kaufmann, S. Lee, J. Li, D.R. Macedo, A. Mendes, N. Mercado-Silva , W. Monk, K. Nakamura, G.G. Ndiritu , R. Ogden , M. Peat , T.B. Reynoldson , B. Rios-Touma , P. Segurado , and A.G. Yates. The biological assessment and rehabilitation of the world\u2019s rivers: an overview.   WATER. MDPI AG, Basel,  SWITZERLAND, 13(3): 371, (2021).",
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
+            "description": "The 4 resource surveys (coastal, rivers and streams, lakes and reservoirs, and wetlands) each have datasets covering the biological, chemical, physical habitat, hydrologic and watershed data. \n\nThis dataset is associated with the following publications:\nStoddard , J., J. Van Sickle, A. Herlihy, J. Brahney, S. Paulsen , D. Peck , R. Mitchell , and A. Pollard. Continental-scale increase in stream and lake phosphorus: Are oligotrophic systems disappearing in the U.S.?.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(7): 3409-3415, (2016).\nHerlihy, A., M. Kentula, T. Magee, G. Lomnicky, A. Nahlik, and G. Serenbetz. Striving for consistency in the National Wetland Condition Assessment: developing a reference condition approach for assessing wetlands at a continental scale.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 327, (2019).\nMagee, T., K. Blocksom, and S. Fennessy. A national-scale vegetation multimetric index (VMMI) as an indicator of wetland condition across the conterminous United States..   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 322, (2019).\nHerlihy, A., J. Sifneos, G. Lomnicky, A. Nahlik, M. Kentula, T. Magee, M. Weber, and A. Trebitz. The response of wetland quality indicators to human disturbance indicators across the United States.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 296, (2019).\nHerlihy, A., S. Paulsen, M. Kentula, T. Magee, A. Nahlik, and G. Lomnicky. Assessing the relative and attributable risk of stressors to wetland condition across the conterminous United States.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 320, (2019).\nLomnicky, G., A.T. Herlihy, and P. Kaufmann. Quantifying the extent of human disturbance activities and anthropogenic stressors in wetlands across the conterminous United States: results from the National Wetland Condition Assessment.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 324, (2019).\nBowen, G., A. Putman, J.R. Brooks, D. Bowling, E. Oerter, and S. Good. Inferring the source of evaporated waters using stable H and O isotopes..   OECOLOGIA. Springer, New York, NY, USA, 187(4): 1025-1039, (2018).\nFox, E., J. Ver Hoef, and T. Olsen. Comparing Spatial Regression to Random Forests for Large Environmental Data Sets..   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 15(3): e0229509, (2020).\nNahlik, A., K. Blocksom, A. Herlihy, M. Kentula, T. Magee, and S. Paulsen. Use of national-scale data to examine human-mediated additions of heavy metals to wetland soils of the US.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 336, (2019).\nKentula, M., and S. Paulsen. The 2011 National Wetland Condition Assessment: Overview and an Invitation.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA,  325, (2019).\nMagee, T., K. Blocksom, A. Herlihy, and A. Nahlik. Characterizing nonnative plants in wetlands across the conterminous United States.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 191: 344, (2019).\nFeio, M., R. Hughes, M. Callisto, S.J. Nichols, O.N. Odume, B.R. Quintella, M. Kuemmerlen, F.C. Aguiar, S.F.P. Almeida, P. Alonso-Egu\u00edaLis , F.O. Arimoro, F.J. Dyer , J.S. Harding , S. Jang , P. Kaufmann, S. Lee, J. Li, D.R. Macedo, A. Mendes, N. Mercado-Silva , W. Monk, K. Nakamura, G.G. Ndiritu , R. Ogden , M. Peat , T.B. Reynoldson , B. Rios-Touma , P. Segurado , and A.G. Yates. The biological assessment and rehabilitation of the world\u2019s rivers: an overview.   WATER. MDPI AG, Basel,  SWITZERLAND, 13(3): 371, (2021).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407622",
             "keyword": [
@@ -73375,17 +73378,20 @@
                 "rivers and streams",
                 "lakes and reservoirs"
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
             "modified": "2017-09-01",
+            "programCode": [
+                "020:096"
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
                 "https://doi.org/10.1021/acs.est.5b05950",
                 "https://doi.org/10.1007/s10661-019-7325-3",
@@ -73400,49 +73406,37 @@
                 "https://doi.org/10.1007/s10661-019-7317-3",
                 "https://doi.org/10.3390/w13030371"
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
+            "title": "National Aquatic Resources Survey datasets"
         },
         {
-            "title": "Domain and HWBI Scores for CWBI",
-            "description": "Geo-located county-level domain and HWBI results calculated based on HWBI framework adaptations for the development of a U.S. Children's Well-Being Index. The file contains 3143 entries. Scores are standardized between 0 and 1. \n\nThis dataset is associated with the following publication:\nBuck, K., K. Summers, L. Smith, and L. Harwell. Application of the Human Well-Being Index to Sensitive Population Divisions: A Children's Well-Being Index Development.   Child Indicators Research. Springer Netherlands,   NETHERLANDS, 11(4): 1249-1280, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1394635",
-            "keyword": [
-                "children's well-being",
-                "HWBI",
-                "sustainability",
-                "indicators"
-            ],
             "contactPoint": {
                 "fn": "Kyle Buck",
                 "hasEmail": "mailto:buck.kyle@epa.gov"
             },
+            "description": "Geo-located county-level domain and HWBI results calculated based on HWBI framework adaptations for the development of a U.S. Children's Well-Being Index. The file contains 3143 entries. Scores are standardized between 0 and 1. \n\nThis dataset is associated with the following publication:\nBuck, K., K. Summers, L. Smith, and L. Harwell. Application of the Human Well-Being Index to Sensitive Population Divisions: A Children's Well-Being Index Development.   Child Indicators Research. Springer Netherlands,   NETHERLANDS, 11(4): 1249-1280, (2018).",
             "distribution": [
                 {
-                    "title": "CWBI-ScienceHubEntry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1394635/CWBI-ScienceHubEntry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CWBI-ScienceHubEntry.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1394635",
+            "keyword": [
+                "children's well-being",
+                "HWBI",
+                "sustainability",
+                "indicators"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-25",
-            "references": [
-                "https://doi.org/10.1007/s12187-017-9469-4"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73452,93 +73446,93 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s12187-017-9469-4"
+            ],
+            "rights": null,
+            "title": "Domain and HWBI Scores for CWBI"
         },
         {
-            "title": "Boyes et al., Figure 1A",
-            "description": "Data support each of the figures in Boyes et al., Moderate Perinatal Thyroid Hormone Insufficiency Alters Visual System Function in Adult Rats (to be submitted for publication). \n\nThis dataset is associated with the following publication:\nBoyes, W., L. Degn, B. George, and M. Gilbert. Moderate Perinatal Thyroid Hormone Insufficiency Alters Visual System Function in Adult Rats.   NEUROTOXICOLOGY. Elsevier B.V., Amsterdam,  NETHERLANDS, 67: 73-83, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1410657",
-            "keyword": [
-                "electroretinograms",
-                "visual evoked potentials",
-                "propylthiouracil",
-                "endocrine disruptor",
-                "developmental hypothyroidism",
-                "visual impairment"
-            ],
             "contactPoint": {
                 "fn": "William Boyes",
                 "hasEmail": "mailto:boyes.william@epa.gov"
             },
+            "description": "Data support each of the figures in Boyes et al., Moderate Perinatal Thyroid Hormone Insufficiency Alters Visual System Function in Adult Rats (to be submitted for publication). \n\nThis dataset is associated with the following publication:\nBoyes, W., L. Degn, B. George, and M. Gilbert. Moderate Perinatal Thyroid Hormone Insufficiency Alters Visual System Function in Adult Rats.   NEUROTOXICOLOGY. Elsevier B.V., Amsterdam,  NETHERLANDS, 67: 73-83, (2018).",
             "distribution": [
                 {
-                    "title": "Figure 1A.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%201A.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1A.xlsx"
                 },
                 {
-                    "title": "Figure 1B.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%201B.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1B.xlsx"
                 },
                 {
-                    "title": "Figure 1E.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%201E.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1E.xlsx"
                 },
                 {
-                    "title": "Figure 1D.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%201D.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1D.xlsx"
                 },
                 {
-                    "title": "Figure 1F.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%201F.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1F.xlsx"
                 },
                 {
-                    "title": "Figure 1C.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%201C.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1C.xlsx"
                 },
                 {
-                    "title": "Figure 2C.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%202C.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 2C.xlsx"
                 },
                 {
-                    "title": "Figure 3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%203.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 3.xlsx"
                 },
                 {
-                    "title": "Figure 4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%204.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 4.xlsx"
                 },
                 {
-                    "title": "Figure 2A and 2B spectra.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%202A%20and%202B%20spectra.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 2A and 2B spectra.xlsx"
                 },
                 {
-                    "title": "Figure 2A and 2B waveforms.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1410657/Figure%202A%20and%202B%20waveforms.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 2A and 2B waveforms.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1410657",
+            "keyword": [
+                "electroretinograms",
+                "visual evoked potentials",
+                "propylthiouracil",
+                "endocrine disruptor",
+                "developmental hypothyroidism",
+                "visual impairment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-30",
-            "references": [
-                "https://doi.org/10.1016/j.neuro.2018.04.013"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73548,41 +73542,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.neuro.2018.04.013"
+            ],
+            "rights": null,
+            "title": "Boyes et al., Figure 1A"
         },
         {
-            "title": "Method 1615 Quantal Data",
-            "description": "Groundwater samples and reageant grade water samples. \n\nThis dataset is associated with the following publication:\nFout , S., and J. Cashdollar. EPA Method 1615. Measurement of Enterovirus and Norovirus Occurrence in Water by Culture and RT-qPCR. II. Total Culturable Virus Assay.   Journal of Visualized Experiments. JoVE, Somerville, MA, USA, 115: e52437, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407572",
-            "keyword": [
-                "occurrence",
-                "total culturable virus assay",
-                "virus",
-                "waterborne"
-            ],
             "contactPoint": {
                 "fn": "Jennifer Cashdollar",
                 "hasEmail": "mailto:cashdollar.jennifer@epa.gov"
             },
+            "description": "Groundwater samples and reageant grade water samples. \n\nThis dataset is associated with the following publication:\nFout , S., and J. Cashdollar. EPA Method 1615. Measurement of Enterovirus and Norovirus Occurrence in Water by Culture and RT-qPCR. II. Total Culturable Virus Assay.   Journal of Visualized Experiments. JoVE, Somerville, MA, USA, 115: e52437, (2016).",
             "distribution": [
                 {
-                    "title": "Final Corrected quantal data for JoVE II 29Jun17.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407572/Final%20Corrected%20quantal%20data%20for%20JoVE%20II%2029Jun17.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Final Corrected quantal data for JoVE II 29Jun17.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407572",
+            "keyword": [
+                "occurrence",
+                "total culturable virus assay",
+                "virus",
+                "waterborne"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-09-17",
-            "references": [
-                "https://doi.org/10.3791/52437"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73592,20 +73586,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3791/52437"
+            ],
+            "rights": null,
+            "title": "Method 1615 Quantal Data"
         },
         {
-            "title": "Cookstove data",
-            "description": "No dataset available. This dataset is not publicly accessible because: The dataset was never touched by EPA employees. Data was collected, analyzed, and maintained solely by non-EPA collaborators. It can be accessed through the following means: Dataset can be accessed by contacting the senior PI on the research effort, Kristina Whitworth (Kristina.W.Whitworth@uth.tmc.edu). Format: Dataset was handled solely by non-EPA collaborators on this research effort. EPA employee role on this research effort was purely advisory. \n\nThis dataset is associated with the following publication:\nMisra, A., M. Longnecker, K. Dionisio, R. Bornman, G. Travlos, S. Brar, and K. Whitworth. Household fuel use and biomarkers of inflammation and respiratory illness among rural South African Women.   ENVIRONMENTAL RESEARCH. Academic Press Incorporated, Orlando, FL, USA, 166: 112-116, (2018).",
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
+                "fn": "Kathie Dionisio",
+                "hasEmail": "mailto:dionisio.kathie@epa.gov"
+            },
+            "description": "No dataset available. This dataset is not publicly accessible because: The dataset was never touched by EPA employees. Data was collected, analyzed, and maintained solely by non-EPA collaborators. It can be accessed through the following means: Dataset can be accessed by contacting the senior PI on the research effort, Kristina Whitworth (Kristina.W.Whitworth@uth.tmc.edu). Format: Dataset was handled solely by non-EPA collaborators on this research effort. EPA employee role on this research effort was purely advisory. \n\nThis dataset is associated with the following publication:\nMisra, A., M. Longnecker, K. Dionisio, R. Bornman, G. Travlos, S. Brar, and K. Whitworth. Household fuel use and biomarkers of inflammation and respiratory illness among rural South African Women.   ENVIRONMENTAL RESEARCH. Academic Press Incorporated, Orlando, FL, USA, 166: 112-116, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1390130",
             "keyword": [
                 "biomass",
@@ -73615,14 +73613,10 @@
                 "biomarkers",
                 "respiratory"
             ],
-            "contactPoint": {
-                "fn": "Kathie Dionisio",
-                "hasEmail": "mailto:dionisio.kathie@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-03-15",
-            "references": [
-                "https://doi.org/10.1016/j.envres.2018.05.016"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73632,19 +73626,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envres.2018.05.016"
+            ],
+            "rights": null,
+            "title": "Cookstove data"
         },
         {
-            "title": "A summary and detailed description of research elements and results that are the building block for the journal article",
-            "description": "The PPT file describes the results of research that serve as the basis for the journal article. \n\nThis dataset is associated with the following publication:\nWei, H., T. Zuo, H. Liu, and J. Yang. Integrating Land Use and Socioeconomic Factors into Scenario-Based Travel Demand and Carbon Emission Impact Study.   Urban Rail Transit. Springer International Publishing AG, Cham (ZG),  SWITZERLAND, 3(1): 3-14, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Yingping Yang",
+                "hasEmail": "mailto:yang.jeff@epa.gov"
+            },
+            "description": "The PPT file describes the results of research that serve as the basis for the journal article. \n\nThis dataset is associated with the following publication:\nWei, H., T. Zuo, H. Liu, and J. Yang. Integrating Land Use and Socioeconomic Factors into Scenario-Based Travel Demand and Carbon Emission Impact Study.   Urban Rail Transit. Springer International Publishing AG, Cham (ZG),  SWITZERLAND, 3(1): 3-14, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502494/WA4-45_Task2_Presentation_10_19_2015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "WA4-45_Task2_Presentation_10_19_2015.pdf"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502494",
             "keyword": [
@@ -73655,20 +73659,10 @@
                 "Transportation environmental",
                 "Carbon emission"
             ],
-            "contactPoint": {
-                "fn": "Yingping Yang",
-                "hasEmail": "mailto:yang.jeff@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "WA4-45_Task2_Presentation_10_19_2015.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502494/WA4-45_Task2_Presentation_10_19_2015.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-20",
-            "references": [
-                "https://doi.org/10.1007/s40864-017-0056-2"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73678,39 +73672,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s40864-017-0056-2"
+            ],
+            "rights": null,
+            "title": "A summary and detailed description of research elements and results that are the building block for the journal article"
         },
         {
-            "title": "Final QCd Ricin Attenuation Data",
-            "description": "Unzip the file to find a spreadsheet for each test.  Each spreadsheet contains the amt of ricin recovered from both positive and test coupons, for both crude and pure ricin forms. \n\nThis dataset is associated with the following publication:\nWood, J., W. Richter, A. Smiley, and J. Rogers. Influence of environmental conditions on the attenuation of ricin toxin on surfaces.   PLoS ONE. Public Library of Science, San Francisco, CA, USA,  9, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
-            "identifier": "https://doi.org/10.23719/1432984",
-            "keyword": [
-                "Ricin",
-                "attenuation"
-            ],
             "contactPoint": {
                 "fn": "Joseph Wood",
                 "hasEmail": "mailto:wood.joe@epa.gov"
             },
+            "description": "Unzip the file to find a spreadsheet for each test.  Each spreadsheet contains the amt of ricin recovered from both positive and test coupons, for both crude and pure ricin forms. \n\nThis dataset is associated with the following publication:\nWood, J., W. Richter, A. Smiley, and J. Rogers. Influence of environmental conditions on the attenuation of ricin toxin on surfaces.   PLoS ONE. Public Library of Science, San Francisco, CA, USA,  9, (2018).",
             "distribution": [
                 {
-                    "title": "TO17 Final Datav2.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1432984/TO17%20Final%20Datav2.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "TO17 Final Datav2.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1432984",
+            "keyword": [
+                "Ricin",
+                "attenuation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-13",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0201857"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73720,19 +73714,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0201857"
+            ],
+            "rights": null,
+            "title": "Final QCd Ricin Attenuation Data"
         },
         {
-            "title": "Links to USGS NWIS repositories of monitoring data",
-            "description": "These are quality-assured time series datasets from weather stations and runoff volume monitoring infrastructure, Cleveland OH. \n\nThis dataset is associated with the following publication:\nShuster, W., and R. Darner. Hydrologic Performance of Retrofit Rain Gardens in a Residential Neighborhood (Cleveland Ohio USA) with a Focus on Monitoring Methods. U.S. Environmental Protection Agency, Washington, DC, USA, 2018.",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "William Shuster",
+                "hasEmail": "mailto:shuster.william@epa.gov"
+            },
+            "description": "These are quality-assured time series datasets from weather stations and runoff volume monitoring infrastructure, Cleveland OH. \n\nThis dataset is associated with the following publication:\nShuster, W., and R. Darner. Hydrologic Performance of Retrofit Rain Gardens in a Residential Neighborhood (Cleveland Ohio USA) with a Focus on Monitoring Methods. U.S. Environmental Protection Agency, Washington, DC, USA, 2018.",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502452/Links%20to%20monitoring%20data%20_Slavic%20Village%20Rain%20Garden%20Study%202012-2016.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Links to monitoring data _Slavic Village Rain Garden Study 2012-2016.docx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502452",
             "keyword": [
@@ -73744,19 +73748,11 @@
                 "rain gardens",
                 "bioretention"
             ],
-            "contactPoint": {
-                "fn": "William Shuster",
-                "hasEmail": "mailto:shuster.william@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Links to monitoring data _Slavic Village Rain Garden Study 2012-2016.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502452/Links%20to%20monitoring%20data%20_Slavic%20Village%20Rain%20Garden%20Study%202012-2016.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-06",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -73765,42 +73761,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Links to USGS NWIS repositories of monitoring data"
         },
         {
-            "title": "GoldenHeather_A-f7mb_Data_20170619",
-            "description": "Output from model simulation runs and used for figures in the manuscript. An index for header terms can be found in the dataset. \n\nThis dataset is associated with the following publication:\nEvenson, G., H. Golden, C. Lane, D. McLaughlin, and E. D'Amico. Depressional wetlands affect watershed hydrological, biogeochemical, and ecological functions.   ECOLOGICAL APPLICATIONS. Ecological Society of America, Ithaca, NY, USA, 28(4): 953-966, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1366490",
-            "keyword": [
-                "wetlands",
-                "watersheds",
-                "hydrology",
-                "watershed models",
-                "Watershed"
-            ],
             "contactPoint": {
                 "fn": "Heather Golden",
                 "hasEmail": "mailto:golden.heather@epa.gov"
             },
+            "description": "Output from model simulation runs and used for figures in the manuscript. An index for header terms can be found in the dataset. \n\nThis dataset is associated with the following publication:\nEvenson, G., H. Golden, C. Lane, D. McLaughlin, and E. D'Amico. Depressional wetlands affect watershed hydrological, biogeochemical, and ecological functions.   ECOLOGICAL APPLICATIONS. Ecological Society of America, Ithaca, NY, USA, 28(4): 953-966, (2018).",
             "distribution": [
                 {
-                    "title": "GoldenHeather_A-f7mb_Data_20170619.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1366490/GoldenHeather_A-f7mb_Data_20170619.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GoldenHeather_A-f7mb_Data_20170619.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1366490",
+            "keyword": [
+                "wetlands",
+                "watersheds",
+                "hydrology",
+                "watershed models",
+                "Watershed"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-16",
-            "references": [
-                "https://doi.org/10.1002/eap.1701"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73810,40 +73804,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/eap.1701"
+            ],
+            "rights": null,
+            "title": "GoldenHeather_A-f7mb_Data_20170619"
         },
         {
-            "title": "Depressed Roadways",
-            "description": "This data set is associated with the results found in the journal article: Amini et al, 2018. Modeling Dispersion of Emissions from Depressed Roadways. Authors: Seyedmorteza Amini, Faraz Enayati Ahangar, David K. Heist, Steven G. Perry, Akula Venkatram. \nThis paper presents an analysis of data from a wind tunnel study of dispersion of emissions from three depressed roadway configurations; a 6 m deep depressed roadway with vertical sidewalls, a 6 m deep depressed roadway with 30\u00b0 sloping sidewalls, and a 9 m deep depressed roadway with vertical sidewalls. All these configurations induce complex flow fields, increase turbulence levels, and decrease surface concentrations downwind of the depressed road compared to those of the at-grade configuration. The parameters of flat terrain dispersion models are modified to describe concentrations measured downwind of the depressed roadways. In the first part of the paper, a flat terrain model proposed by van Ulden (1978) is adapted. It turns out that this model with increased initial vertical dispersion and friction velocity is able to explain the observed concentration field. The results also suggest that the vertical concentration profiles of all cases under neutral conditions are best explained by a vertical distribution function with an exponent of 1.3. In the second part of the paper, these modifications are incorporated into a model based on the RLINE  line-source dispersion model. While this model can be adapted to yield acceptable estimates of near-surface concentrations (z< 6m) measured in the wind tunnel, the Gaussian vertical distribution in RLINE, with an exponent of 2, cannot describe the concentration at higher elevations. Our findings suggest a simple method to account for depressed highways in models such as RLINE and AERMOD through two parameters that modify vertical plume spread. \n\nThis dataset is associated with the following publication:\nAmini, S., F. Ahangar, D. Heist, S. Perry, and A. Venkatram. Modeling Dispersion of Emissions from Depressed Roadways.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 186: 189-197, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1434500",
-            "keyword": [
-                "near-road",
-                "dispersion modeling",
-                "wind tunnel"
-            ],
             "contactPoint": {
                 "fn": "David Heist",
                 "hasEmail": "mailto:heist.david@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434500/documents/HeistDavid_A-j9kw_DataDictionary_DepressedRoadways.pdf",
+            "describedByType": "application/pdf",
+            "description": "This data set is associated with the results found in the journal article: Amini et al, 2018. Modeling Dispersion of Emissions from Depressed Roadways. Authors: Seyedmorteza Amini, Faraz Enayati Ahangar, David K. Heist, Steven G. Perry, Akula Venkatram. \nThis paper presents an analysis of data from a wind tunnel study of dispersion of emissions from three depressed roadway configurations; a 6 m deep depressed roadway with vertical sidewalls, a 6 m deep depressed roadway with 30\u00b0 sloping sidewalls, and a 9 m deep depressed roadway with vertical sidewalls. All these configurations induce complex flow fields, increase turbulence levels, and decrease surface concentrations downwind of the depressed road compared to those of the at-grade configuration. The parameters of flat terrain dispersion models are modified to describe concentrations measured downwind of the depressed roadways. In the first part of the paper, a flat terrain model proposed by van Ulden (1978) is adapted. It turns out that this model with increased initial vertical dispersion and friction velocity is able to explain the observed concentration field. The results also suggest that the vertical concentration profiles of all cases under neutral conditions are best explained by a vertical distribution function with an exponent of 1.3. In the second part of the paper, these modifications are incorporated into a model based on the RLINE  line-source dispersion model. While this model can be adapted to yield acceptable estimates of near-surface concentrations (z< 6m) measured in the wind tunnel, the Gaussian vertical distribution in RLINE, with an exponent of 2, cannot describe the concentration at higher elevations. Our findings suggest a simple method to account for depressed highways in models such as RLINE and AERMOD through two parameters that modify vertical plume spread. \n\nThis dataset is associated with the following publication:\nAmini, S., F. Ahangar, D. Heist, S. Perry, and A. Venkatram. Modeling Dispersion of Emissions from Depressed Roadways.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 186: 189-197, (2018).",
             "distribution": [
                 {
-                    "title": "HeistDavid_A-j9kw_Data-DepressedRoadways.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434500/HeistDavid_A-j9kw_Data-DepressedRoadways.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "HeistDavid_A-j9kw_Data-DepressedRoadways.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434500",
+            "keyword": [
+                "near-road",
+                "dispersion modeling",
+                "wind tunnel"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-11",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2018.04.058"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73854,20 +73850,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434500/documents/HeistDavid_A-j9kw_DataDictionary_DepressedRoadways.pdf",
-            "describedByType": "application/pdf"
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2018.04.058"
+            ],
+            "rights": null,
+            "title": "Depressed Roadways"
         },
         {
-            "title": "Fourier Transformed Infrared (FTIR) Spectroscopy Data for Soil Carbon, Extractable Carbon, Changes in Soil FTIR Spectra, FTIR Data Clustering & Discriminant Analysis ",
-            "description": "Here we report on a rapid, high throughput approach using fingerprint Fourier transformed infrared (FTIR) spectroscopy and chemometric modeling. Fingerprint FTIR incorporates all information embedded within the FTIR spectrum, thus producing a biogeochemical or ecological \u201cfingerprint\u201d of the soil. This methodology was applied in a highly disturbed forest ecosystem over a 19-year sampling period to detect, via spectral analysis, changes in dynamic soil properties (e.g., soil organic matter and reactive mineralogy) that can indicate changes in soil quality. Two chemometric statistical techniques (i.e., hierarchical clustering analysis [HCA] and discriminate analysis of principal components [DAPC]) were evaluated for interpreting and quantifying similarities/dissimilarities between samples utilizing the entire FTIR spectra from each sample. \n\nThis dataset is associated with the following publication:\nMaynard, J., and M. Johnson. Applying fingerprint Fourier transformed infrared spectroscopy and chemometrics to assess soil ecosystem disturbance and recovery.   JOURNAL OF SOIL AND WATER CONSERVATION. Soil and Water Conservation Society,    73(4): 443-451, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Mark Johnson",
+                "hasEmail": "mailto:johnson.markg@epa.gov"
+            },
+            "description": "Here we report on a rapid, high throughput approach using fingerprint Fourier transformed infrared (FTIR) spectroscopy and chemometric modeling. Fingerprint FTIR incorporates all information embedded within the FTIR spectrum, thus producing a biogeochemical or ecological \u201cfingerprint\u201d of the soil. This methodology was applied in a highly disturbed forest ecosystem over a 19-year sampling period to detect, via spectral analysis, changes in dynamic soil properties (e.g., soil organic matter and reactive mineralogy) that can indicate changes in soil quality. Two chemometric statistical techniques (i.e., hierarchical clustering analysis [HCA] and discriminate analysis of principal components [DAPC]) were evaluated for interpreting and quantifying similarities/dissimilarities between samples utilizing the entire FTIR spectra from each sample. \n\nThis dataset is associated with the following publication:\nMaynard, J., and M. Johnson. Applying fingerprint Fourier transformed infrared spectroscopy and chemometrics to assess soil ecosystem disturbance and recovery.   JOURNAL OF SOIL AND WATER CONSERVATION. Soil and Water Conservation Society,    73(4): 443-451, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502535/Maynard%20and%20Johnson%202018_JSWC_Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Maynard and Johnson 2018_JSWC_Data.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502535",
             "keyword": [
@@ -73882,20 +73886,10 @@
                 "redundancy analysis",
                 "variation partitioning"
             ],
-            "contactPoint": {
-                "fn": "Mark Johnson",
-                "hasEmail": "mailto:johnson.markg@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Maynard and Johnson 2018_JSWC_Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502535/Maynard%20and%20Johnson%202018_JSWC_Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-08",
-            "references": [
-                "https://doi.org/10.2489/jswc.73.4.443"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -73905,126 +73899,128 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2489/jswc.73.4.443"
+            ],
+            "rights": null,
+            "title": "Fourier Transformed Infrared (FTIR) Spectroscopy Data for Soil Carbon, Extractable Carbon, Changes in Soil FTIR Spectra, FTIR Data Clustering & Discriminant Analysis "
         },
         {
-            "title": "1990-2010 atmospheric deposition of Sulfur and nitrogen",
-            "description": "These data files associated with the Tables and Figures presented in the following manuscript:\nZhang, Y., Mathur, R., Bash, J. O., Hogrefe, C., Xing, J., and Roselle, S. J.: Long-term trends in total inorganic nitrogen and sulfur deposition in the US from 1990 to 2010, Atmos. Chem. Phys., 18, 9091-9106, https://doi.org/10.5194/acp-18-9091-2018, 2018. \n\nThis dataset is associated with the following publication:\nZhang, Y., R. Mathur, J. Bash, C. Hogrefe, J. Xing, and S. Roselle. Long-term trends in total inorganic nitrogen and sulfur deposition in the US from 1990 to 2010.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 9091-9106, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1434279",
-            "keyword": [
-                "atmospheric deosition",
-                "long term trends",
-                "nitrogen",
-                "sulfur"
-            ],
             "contactPoint": {
                 "fn": "Rohit Mathur",
                 "hasEmail": "mailto:mathur.rohit@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434279/documents/Data_Dictionary_acp-2018-116.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "These data files associated with the Tables and Figures presented in the following manuscript:\nZhang, Y., Mathur, R., Bash, J. O., Hogrefe, C., Xing, J., and Roselle, S. J.: Long-term trends in total inorganic nitrogen and sulfur deposition in the US from 1990 to 2010, Atmos. Chem. Phys., 18, 9091-9106, https://doi.org/10.5194/acp-18-9091-2018, 2018. \n\nThis dataset is associated with the following publication:\nZhang, Y., R. Mathur, J. Bash, C. Hogrefe, J. Xing, and S. Roselle. Long-term trends in total inorganic nitrogen and sulfur deposition in the US from 1990 to 2010.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 9091-9106, (2018).",
             "distribution": [
                 {
-                    "title": "Figs_1_3_Tables_1_stations.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_1_3_Tables_1_stations.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_1_3_Tables_1_stations.csv"
                 },
                 {
-                    "title": "Figs_4_TSO4_def.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_4_TSO4_def.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_4_TSO4_def.csv"
                 },
                 {
-                    "title": "Figs_4_TIN_abc.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_4_TIN_abc.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_4_TIN_abc.csv"
                 },
                 {
-                    "title": "Figs_6_def_DDEP_TIN.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_6_def_DDEP_TIN.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_6_def_DDEP_TIN.csv"
                 },
                 {
-                    "title": "Figs_7_abc_WDEP_S.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_7_abc_WDEP_S.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_7_abc_WDEP_S.csv"
                 },
                 {
-                    "title": "Figs_7_def_DDEP_S.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_7_def_DDEP_S.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_7_def_DDEP_S.csv"
                 },
                 {
-                    "title": "Figs_8_Total Deposition & Emissions trend.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_8_Total%20Deposition%20%26%20Emissions%20trend.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figs_8_Total Deposition & Emissions trend.xlsx"
                 },
                 {
-                    "title": "Figs_5_NHx_trend.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_5_NHx_trend.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_5_NHx_trend.csv"
                 },
                 {
-                    "title": "Table_2_Ecoregions_Evaluation_TNO3_Obs.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Table_2_Ecoregions_Evaluation_TNO3_Obs.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Table_2_Ecoregions_Evaluation_TNO3_Obs.csv"
                 },
                 {
-                    "title": "Table_3_Ecoregions_Evaluation_NHX_Obs.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Table_3_Ecoregions_Evaluation_NHX_Obs.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Table_3_Ecoregions_Evaluation_NHX_Obs.csv"
                 },
                 {
-                    "title": "Figs_5_TNO3_trend.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_5_TNO3_trend.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_5_TNO3_trend.csv"
                 },
                 {
-                    "title": "Figs_6_abc_WDEP_TIN.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_6_abc_WDEP_TIN.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_6_abc_WDEP_TIN.csv"
                 },
                 {
-                    "title": "Table_4_Ecoregions_Evaluation_TSO4_Obs.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Table_4_Ecoregions_Evaluation_TSO4_Obs.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Table_4_Ecoregions_Evaluation_TSO4_Obs.csv"
                 },
                 {
-                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_NHX.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Tables_5_6_Deposition_Trends_Ecoregions_NHX.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_NHX.csv"
                 },
                 {
-                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_TIN.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Tables_5_6_Deposition_Trends_Ecoregions_TIN.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_TIN.csv"
                 },
                 {
-                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_TNO3.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Tables_5_6_Deposition_Trends_Ecoregions_TNO3.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_TNO3.csv"
                 },
                 {
-                    "title": "Figs_9_TDEP_NHx_Ratio.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Figs_9_TDEP_NHx_Ratio.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figs_9_TDEP_NHx_Ratio.csv"
                 },
                 {
-                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_TSO4.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434279/Tables_5_6_Deposition_Trends_Ecoregions_TSO4.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tables_5_6_Deposition_Trends_Ecoregions_TSO4.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434279",
+            "keyword": [
+                "atmospheric deosition",
+                "long term trends",
+                "nitrogen",
+                "sulfur"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-15",
-            "references": [
-                "https://doi.org/10.5194/acp-18-9091-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74035,42 +74031,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1434279/documents/Data_Dictionary_acp-2018-116.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/acp-18-9091-2018"
+            ],
+            "rights": null,
+            "title": "1990-2010 atmospheric deposition of Sulfur and nitrogen"
         },
         {
-            "title": "Dataset for Identification of Biomarkers of Exposure to FTOHs  and PAPs in Humans Using a Targeted and Non-targeted Analysis Approach",
-            "description": "Dataset for Identification of Biomarkers of Exposure to FTOHs  and PAPs in Humans Using a Targeted and Non-targeted Analysis Approach. \n\nThis dataset is associated with the following publication:\nDagnino, A., M. Strynar, R. McMahen, C. Lau, C. Ball, S. Garantziosis, T. Webster, M. McClean, and A. Lindstrom. Identification of Biomarkers of Exposure to FTOHs  and PAPs in Humans Using a Targeted and Non-targeted Analysis Approach.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(0): 10216-10225, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1407650",
-            "keyword": [
-                "flurorotelomer alcohol",
-                "biomarkers",
-                "human",
-                "Metabolism",
-                "per and poly-fluorinated"
-            ],
             "contactPoint": {
                 "fn": "Mark Strynar",
                 "hasEmail": "mailto:strynar.mark@epa.gov"
             },
+            "description": "Dataset for Identification of Biomarkers of Exposure to FTOHs  and PAPs in Humans Using a Targeted and Non-targeted Analysis Approach. \n\nThis dataset is associated with the following publication:\nDagnino, A., M. Strynar, R. McMahen, C. Lau, C. Ball, S. Garantziosis, T. Webster, M. McClean, and A. Lindstrom. Identification of Biomarkers of Exposure to FTOHs  and PAPs in Humans Using a Targeted and Non-targeted Analysis Approach.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(0): 10216-10225, (2016).",
             "distribution": [
                 {
-                    "title": "Dagnino Dataset Information Document.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407650/Dagnino%20Dataset%20Information%20Document.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Dagnino Dataset Information Document.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407650",
+            "keyword": [
+                "flurorotelomer alcohol",
+                "biomarkers",
+                "human",
+                "Metabolism",
+                "per and poly-fluorinated"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2012-01-01",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -74079,19 +74075,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Dataset for Identification of Biomarkers of Exposure to FTOHs  and PAPs in Humans Using a Targeted and Non-targeted Analysis Approach"
         },
         {
-            "title": "EWRI World Water Congress 2018 Presentation Dataset",
-            "description": "Data and Tables and Figures in EWRI 2018 presentation. \n\nThis dataset is associated with the following publication:\nBlaisi, N., J. Roessler, W. Cheng, T. Townsend, and S. Al-Abed. Evaluation of the impact of lime softening waste disposal in natural environments.  R. Cossu  WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 43: 524-532, (2015).",
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
+            "description": "Data and Tables and Figures in EWRI 2018 presentation. \n\nThis dataset is associated with the following publication:\nBlaisi, N., J. Roessler, W. Cheng, T. Townsend, and S. Al-Abed. Evaluation of the impact of lime softening waste disposal in natural environments.  R. Cossu  WASTE MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 43: 524-532, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502476/EWRI2018PresentationDataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EWRI2018PresentationDataset.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502476",
             "keyword": [
@@ -74102,20 +74106,10 @@
                 "environmental impact assessment",
                 "mercury re-emission"
             ],
-            "contactPoint": {
-                "fn": "Craig Patterson",
-                "hasEmail": "mailto:patterson.craig@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "EWRI2018PresentationDataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502476/EWRI2018PresentationDataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-07-11",
-            "references": [
-                "https://doi.org/10.1016/j.wasman.2015.06.015"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74125,19 +74119,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.wasman.2015.06.015"
+            ],
+            "rights": null,
+            "title": "EWRI World Water Congress 2018 Presentation Dataset"
         },
         {
-            "title": "Intergenerational responses of wheat to CeO2 nanoparticles, growth and nutrient contents",
-            "description": "The intergenerational impact of engineered nanomaterials in plants is a key knowledge gap in the literature. A soil microcosm study was performed to assess the effects of multi-generational exposure of wheat (Triticum aestivum L.) to cerium oxide nanoparticles (CeO2-NPs). Seeds from plants that were exposed to 0, 125, and 500 mg CeO2-NPs/kg soil (Ce-0, Ce-125 or Ce-500, respectively) in first generation (S1) were cultivated in factorial combinations of Ce-0, Ce-125 or Ce-500 to produce second generation (S2) plants. The factorial combinations for first/second generation treatments in Ce-125 were S1-Ce-0/S2-Ce-0, S1-Ce-0/S2-Ce-125, S1-Ce-125/S2-Ce-0 and S1-Ce-125/S2-Ce-125, and in Ce-500 were S1-Ce-0/S2-Ce-0, S1-Ce-0/S2-Ce-500, S1-Ce-500/S2-Ce-0 and S1-Ce-500/S2-Ce-500. Agronomic, elemental, isotopic, and synchrotron X-ray fluorescence (XRF) and X-ray absorption near-edge spectroscopy (XANES) data were collected on second generation plants. Results showed that plants treated during the first generation only with either Ce-125 or Ce-500 (e.g. S1-Ce-125/S2-Ce-0 or S1-Ce-500/S2-Ce-0) had reduced accumulation of Ce (61 or 50%), Fe (49 or 58%) and Mn (34 or 41%) in roots, and \u03b415N (11 or 8%) in grains compared to the plants not treated in both generations (i.e. S1-Ce-0/S2-Ce-0). Plants treated in both generations with Ce-125 (i.e. S1-Ce-125/S2-Ce-125) produced grains that had lower Mn, Ca, K, Mg and P relative to plants treated in the second generation only (i.e. S1-Ce-0/S2-Ce-125). In addition, synchrotron XRF elemental chemistry maps of soil/plant thin-sections revealed limited transformation of CeO2-NPs with no evidence of plant uptake or accumulation. The findings demonstrated that first generation exposure of wheat to CeO2-NPs affects the physiology and nutrient profile of the second generation plants. However, the lack of concentration-dependent responses indicate that complex physiological processes are involved which alter uptake and metabolism of CeO2-NPs in wheat. \n\nThis dataset is associated with the following publication:\nRico, C., M. Johnson, M. Marcus, and C. Andersen. Intergenerational responses of wheat (Triticum aestivum L.) to cerium oxide nanoparticles exposure.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 4: 700-711, (2017).",
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
+            "description": "The intergenerational impact of engineered nanomaterials in plants is a key knowledge gap in the literature. A soil microcosm study was performed to assess the effects of multi-generational exposure of wheat (Triticum aestivum L.) to cerium oxide nanoparticles (CeO2-NPs). Seeds from plants that were exposed to 0, 125, and 500 mg CeO2-NPs/kg soil (Ce-0, Ce-125 or Ce-500, respectively) in first generation (S1) were cultivated in factorial combinations of Ce-0, Ce-125 or Ce-500 to produce second generation (S2) plants. The factorial combinations for first/second generation treatments in Ce-125 were S1-Ce-0/S2-Ce-0, S1-Ce-0/S2-Ce-125, S1-Ce-125/S2-Ce-0 and S1-Ce-125/S2-Ce-125, and in Ce-500 were S1-Ce-0/S2-Ce-0, S1-Ce-0/S2-Ce-500, S1-Ce-500/S2-Ce-0 and S1-Ce-500/S2-Ce-500. Agronomic, elemental, isotopic, and synchrotron X-ray fluorescence (XRF) and X-ray absorption near-edge spectroscopy (XANES) data were collected on second generation plants. Results showed that plants treated during the first generation only with either Ce-125 or Ce-500 (e.g. S1-Ce-125/S2-Ce-0 or S1-Ce-500/S2-Ce-0) had reduced accumulation of Ce (61 or 50%), Fe (49 or 58%) and Mn (34 or 41%) in roots, and \u03b415N (11 or 8%) in grains compared to the plants not treated in both generations (i.e. S1-Ce-0/S2-Ce-0). Plants treated in both generations with Ce-125 (i.e. S1-Ce-125/S2-Ce-125) produced grains that had lower Mn, Ca, K, Mg and P relative to plants treated in the second generation only (i.e. S1-Ce-0/S2-Ce-125). In addition, synchrotron XRF elemental chemistry maps of soil/plant thin-sections revealed limited transformation of CeO2-NPs with no evidence of plant uptake or accumulation. The findings demonstrated that first generation exposure of wheat to CeO2-NPs affects the physiology and nutrient profile of the second generation plants. However, the lack of concentration-dependent responses indicate that complex physiological processes are involved which alter uptake and metabolism of CeO2-NPs in wheat. \n\nThis dataset is associated with the following publication:\nRico, C., M. Johnson, M. Marcus, and C. Andersen. Intergenerational responses of wheat (Triticum aestivum L.) to cerium oxide nanoparticles exposure.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK, 4: 700-711, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502592/CeO2%20Wheat%20Intergenerational%20Data%20Repository%20for%208-24-18.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CeO2 Wheat Intergenerational Data Repository for 8-24-18.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502592",
             "keyword": [
@@ -74148,20 +74152,10 @@
                 "nitrogen",
                 "engineered nanomaterials (ENMs)"
             ],
-            "contactPoint": {
-                "fn": "Christian Andersen",
-                "hasEmail": "mailto:andersen.christian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "CeO2 Wheat Intergenerational Data Repository for 8-24-18.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502592/CeO2%20Wheat%20Intergenerational%20Data%20Repository%20for%208-24-18.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-08-27",
-            "references": [
-                "https://doi.org/10.1039/c7en00057j"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74171,19 +74165,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c7en00057j"
+            ],
+            "rights": null,
+            "title": "Intergenerational responses of wheat to CeO2 nanoparticles, growth and nutrient contents"
         },
         {
-            "title": "Changes in gene expression in Arabidopsis in response to nano CeO2 and nano TiO2",
-            "description": "- Changes in tissue transcriptomes and productivity of Arabidopsis thaliana were investigated during exposure of plants to two widely used engineered metal oxide nanoparticles, titanium dioxide (nano-titanium) and cerium dioxide (nano-cerium). Microarray analyses confirmed that exposure to either nanoparticle altered the transcriptomes of rosette leaves and roots, with comparatively larger numbers of differentially expressed genes (DEGs) found under nano-titania exposure. Nano-titania induced more DEGs in rosette leaves, whereas roots had more DEGs under nano-ceria exposure.  MapMan analyses indicated that while nano-titania up-regulated overall metabolism metabolism in both tissues, metabolic processes under nano-ceria remained mostly unchanged. Gene enrichment analysis indicated that both nanoparticles mainly enriched ontology groups such as responses to stress (abiotic and biotic), and defense responses (pathogens), and responses to endogenous stimuli (hormones). Nano-titania specifically induced genes associated with photosynthesis, whereas nano-ceria induced expression of genes related to activating transcription factors, most notably those belonging to the ethylene responsive element binding protein family.  Interestingly, there were also increased numbers of rosette leaves and plant biomass under nano-ceria exposure, but not under nano-titania. Other transcriptomic responses did not clearly relate to responses observed at the organism level. This may be due to functional and genomic redundancy in Arabidopsis, which may mask expression of morphological changes, despite discernable responses at the transcriptome level. Additionally, transcriptomic changes often relate with transgenerational phenotypic development, hence it may be productive to direct further experimental work to integrate high-throughput genomic results with longer-term changes in subsequent generations. \n\nThis dataset is associated with the following publication:\nTumburu, L., C. Andersen, P.T. Rygiewicz, and J. Reichman. Molecular and physiological responses to titanium dioxide and cerium oxide nanoparticles in arabidopsis.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 36(1): 71-82, (2017).",
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
+            "description": "- Changes in tissue transcriptomes and productivity of Arabidopsis thaliana were investigated during exposure of plants to two widely used engineered metal oxide nanoparticles, titanium dioxide (nano-titanium) and cerium dioxide (nano-cerium). Microarray analyses confirmed that exposure to either nanoparticle altered the transcriptomes of rosette leaves and roots, with comparatively larger numbers of differentially expressed genes (DEGs) found under nano-titania exposure. Nano-titania induced more DEGs in rosette leaves, whereas roots had more DEGs under nano-ceria exposure.  MapMan analyses indicated that while nano-titania up-regulated overall metabolism metabolism in both tissues, metabolic processes under nano-ceria remained mostly unchanged. Gene enrichment analysis indicated that both nanoparticles mainly enriched ontology groups such as responses to stress (abiotic and biotic), and defense responses (pathogens), and responses to endogenous stimuli (hormones). Nano-titania specifically induced genes associated with photosynthesis, whereas nano-ceria induced expression of genes related to activating transcription factors, most notably those belonging to the ethylene responsive element binding protein family.  Interestingly, there were also increased numbers of rosette leaves and plant biomass under nano-ceria exposure, but not under nano-titania. Other transcriptomic responses did not clearly relate to responses observed at the organism level. This may be due to functional and genomic redundancy in Arabidopsis, which may mask expression of morphological changes, despite discernable responses at the transcriptome level. Additionally, transcriptomic changes often relate with transgenerational phenotypic development, hence it may be productive to direct further experimental work to integrate high-throughput genomic results with longer-term changes in subsequent generations. \n\nThis dataset is associated with the following publication:\nTumburu, L., C. Andersen, P.T. Rygiewicz, and J. Reichman. Molecular and physiological responses to titanium dioxide and cerium oxide nanoparticles in arabidopsis.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 36(1): 71-82, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE80461",
+                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE80461"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502593",
             "keyword": [
@@ -74194,19 +74197,10 @@
                 "nitrogen",
                 "engineered nanomaterials (ENMs)"
             ],
-            "contactPoint": {
-                "fn": "Christian Andersen",
-                "hasEmail": "mailto:andersen.christian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE80461",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE80461"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-08-27",
-            "references": [
-                "https://doi.org/10.1002/etc.3500"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74216,42 +74210,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.3500"
+            ],
+            "rights": null,
+            "title": "Changes in gene expression in Arabidopsis in response to nano CeO2 and nano TiO2"
         },
         {
-            "title": "Dataset for modeling spatial and temporal variation in natural background specific conductivity",
-            "description": "This file contains the data set used to develop a random forest model predict background specific conductivity for stream segments in the contiguous United States. This Excel readable file contains 56 columns of parameters evaluated during development.  The data dictionary provides the definition of the abbreviations and the measurement units.  Each row is a unique sample described as R** which indicates the NHD Hydrologic Unit (underscore), up to a 7-digit COMID, (underscore) sequential sample month.\nTo develop models that make stream-specific predictions across the contiguous United States, we used StreamCat data set and process (Hill et al. 2016; https://github.com/USEPA/StreamCat). The StreamCat data set is based on a network of stream segments from NHD+ (McKay et al. 2012). These stream segments drain an average area of 3.1 km2 and thus define the spatial grain size of this data set. \nThe data set consists of minimally disturbed sites representing the natural variation in environmental conditions that occur in the contiguous 48 United States. More than 2.4 million SC observations were obtained from STORET (USEPA 2016b), state natural resource agencies, the U.S. Geological Survey (USGS) National Water Information System (NWIS) system (USGS 2016), and data used in Olson and Hawkins (2012) (Table S1). Data include observations made between 1 January 2001 and 31 December 2015 thus coincident with Moderate Resolution Imaging Spectroradiometer (MODIS) satellite data (https://modis.gsfc.nasa.gov/data/). Each observation was related to the nearest stream segment in the NHD+. Data were limited to one observation per stream segment per month. SC observations with ambiguous locations and repeat measurements along a stream segment in the same month were discarded. Using estimates of anthropogenic stress derived from the StreamCat database (Hill et al. 2016), segments were selected with minimal amounts of human activity (Stoddard et al. 2006) using criteria developed for each Level II Ecoregion (Omernik and Griffith 2014).  Segments were considered as potentially minimally stressed where watersheds had 0 - 0.5% impervious surface, 0 \u2013 5% urban, 0 \u2013 10% agriculture, and population densities from 0.8 \u2013 30 people/km2 (Table S3). Watersheds with observations with large residuals in initial models were identified and inspected for evidence of other human activities not represented in StreamCat (e.g., mining, logging, grazing, or oil/gas extraction). Observations were removed from disturbed watersheds, with a tidal influence or unusual geologic conditions such as hot springs. About 5% of SC observations in each National Rivers and Stream Assessment (NRSA) region were then randomly selected as independent validation data. The remaining observations became the large training data set for model calibration. \n\nThis dataset is associated with the following publication:\nOlson, J., and S. Cormier. Modeling spatial and temporal variation in natural background specific conductivity.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(8): 4316-4325, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500945",
-            "keyword": [
-                "drought",
-                "StreamCat",
-                "conductivity",
-                "Carbonate Salts",
-                "modeled conductivity"
-            ],
             "contactPoint": {
                 "fn": "Susan Cormier",
                 "hasEmail": "mailto:cormier.susan@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500945/documents/Data_Dictionary_RefModelData_20180611_508.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This file contains the data set used to develop a random forest model predict background specific conductivity for stream segments in the contiguous United States. This Excel readable file contains 56 columns of parameters evaluated during development.  The data dictionary provides the definition of the abbreviations and the measurement units.  Each row is a unique sample described as R** which indicates the NHD Hydrologic Unit (underscore), up to a 7-digit COMID, (underscore) sequential sample month.\nTo develop models that make stream-specific predictions across the contiguous United States, we used StreamCat data set and process (Hill et al. 2016; https://github.com/USEPA/StreamCat). The StreamCat data set is based on a network of stream segments from NHD+ (McKay et al. 2012). These stream segments drain an average area of 3.1 km2 and thus define the spatial grain size of this data set. \nThe data set consists of minimally disturbed sites representing the natural variation in environmental conditions that occur in the contiguous 48 United States. More than 2.4 million SC observations were obtained from STORET (USEPA 2016b), state natural resource agencies, the U.S. Geological Survey (USGS) National Water Information System (NWIS) system (USGS 2016), and data used in Olson and Hawkins (2012) (Table S1). Data include observations made between 1 January 2001 and 31 December 2015 thus coincident with Moderate Resolution Imaging Spectroradiometer (MODIS) satellite data (https://modis.gsfc.nasa.gov/data/). Each observation was related to the nearest stream segment in the NHD+. Data were limited to one observation per stream segment per month. SC observations with ambiguous locations and repeat measurements along a stream segment in the same month were discarded. Using estimates of anthropogenic stress derived from the StreamCat database (Hill et al. 2016), segments were selected with minimal amounts of human activity (Stoddard et al. 2006) using criteria developed for each Level II Ecoregion (Omernik and Griffith 2014).  Segments were considered as potentially minimally stressed where watersheds had 0 - 0.5% impervious surface, 0 \u2013 5% urban, 0 \u2013 10% agriculture, and population densities from 0.8 \u2013 30 people/km2 (Table S3). Watersheds with observations with large residuals in initial models were identified and inspected for evidence of other human activities not represented in StreamCat (e.g., mining, logging, grazing, or oil/gas extraction). Observations were removed from disturbed watersheds, with a tidal influence or unusual geologic conditions such as hot springs. About 5% of SC observations in each National Rivers and Stream Assessment (NRSA) region were then randomly selected as independent validation data. The remaining observations became the large training data set for model calibration. \n\nThis dataset is associated with the following publication:\nOlson, J., and S. Cormier. Modeling spatial and temporal variation in natural background specific conductivity.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 53(8): 4316-4325, (2019).",
             "distribution": [
                 {
-                    "title": "RefModelData_508.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500945/RefModelData_508.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "RefModelData_508.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500945",
+            "keyword": [
+                "drought",
+                "StreamCat",
+                "conductivity",
+                "Carbonate Salts",
+                "modeled conductivity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-14",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b06777"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74262,80 +74258,78 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500945/documents/Data_Dictionary_RefModelData_20180611_508.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b06777"
+            ],
+            "rights": null,
+            "title": "Dataset for modeling spatial and temporal variation in natural background specific conductivity"
         },
         {
-            "title": "2009 USVI",
-            "description": "EPA conducted a small regional coral reef assessment at 13 stations selected to represent a range of human influence around Charlotte Amalie (CA) Port in St. Thomas.  Sites were selected to represent an east-west gradient of human disturbance with CA at its center. In order to minimize habitat differences, all locations were selected in close proximity to land and at a similar depth (5-9 m). Multiple biological assemblages were measured, including stony corals, sponges and gorgonians, fish, and invertebrates. \n\nThis dataset is associated with the following publication:\nOliver, L., W. Fisher, L. Fore, A. Smith, and P. Bradley. Assessing Land Use, Sedimentation and Water Quality Stressors as Predictors of Coral Reef Condition in St. Thomas, U.S. Virgin Islands.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 190: 213, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1425905",
-            "keyword": [
-                "coral reef condition",
-                "stony coral",
-                "biocriteria",
-                "probability based sampling",
-                "reef assessments",
-                "Puerto Rico",
-                "USVI"
-            ],
             "contactPoint": {
                 "fn": "William Fisher",
                 "hasEmail": "mailto:fisher.william@epa.gov"
             },
+            "description": "EPA conducted a small regional coral reef assessment at 13 stations selected to represent a range of human influence around Charlotte Amalie (CA) Port in St. Thomas.  Sites were selected to represent an east-west gradient of human disturbance with CA at its center. In order to minimize habitat differences, all locations were selected in close proximity to land and at a similar depth (5-9 m). Multiple biological assemblages were measured, including stony corals, sponges and gorgonians, fish, and invertebrates. \n\nThis dataset is associated with the following publication:\nOliver, L., W. Fisher, L. Fore, A. Smith, and P. Bradley. Assessing Land Use, Sedimentation and Water Quality Stressors as Predictors of Coral Reef Condition in St. Thomas, U.S. Virgin Islands.   ENVIRONMENTAL MONITORING AND ASSESSMENT. Springer, New York, NY, USA, 190: 213, (2018).",
             "distribution": [
                 {
-                    "title": "Fish_USVI2009CA_FMay062016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/Fish_USVI2009CA_FMay062016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fish_USVI2009CA_FMay062016.xlsx"
                 },
                 {
-                    "title": "Inverts_USVI2009CA_FMay062016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/Inverts_USVI2009CA_FMay062016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Inverts_USVI2009CA_FMay062016.xlsx"
                 },
                 {
-                    "title": "Rugosity_USVI2009CA_FMay062016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/Rugosity_USVI2009CA_FMay062016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rugosity_USVI2009CA_FMay062016.xlsx"
                 },
                 {
-                    "title": "SpGorg_USVI2009CA_FMay062016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/SpGorg_USVI2009CA_FMay062016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SpGorg_USVI2009CA_FMay062016.xlsx"
                 },
                 {
-                    "title": "Stonycoral_USVI2009CA_FMay062016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/Stonycoral_USVI2009CA_FMay062016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Stonycoral_USVI2009CA_FMay062016.xlsx"
                 },
                 {
-                    "title": "Metric Table_Surveys.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/Metric%20Table_Surveys.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Metric Table_Surveys.docx"
                 },
                 {
-                    "title": "StationInfo_USVI2009CA_FMar2018.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/StationInfo_USVI2009CA_FMar2018.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "StationInfo_USVI2009CA_FMar2018.xlsx"
                 },
                 {
-                    "title": "FORAM Data StThomas-USVI 2009.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1425905/FORAM%20Data%20StThomas-USVI%202009.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FORAM Data StThomas-USVI 2009.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1425905",
+            "keyword": [
+                "coral reef condition",
+                "stony coral",
+                "biocriteria",
+                "probability based sampling",
+                "reef assessments",
+                "Puerto Rico",
+                "USVI"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-01",
-            "references": [
-                "https://doi.org/10.1007/s10661-018-6562-1"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74345,54 +74339,54 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10661-018-6562-1"
+            ],
+            "rights": null,
+            "title": "2009 USVI"
         },
         {
-            "title": "Differentiating Pathway-Specific From Nonspecific Effects in High-Throughput Toxicity Data: A Foundation for Prioritizing Adverse Outcome Pathway Development",
-            "description": "Previous work identified a \u2018cytotoxic burst\u2019 (CTB) phenomenon wherein large numbers of the ToxCast assays begin to respond at or near test chemical concentrations that elicit cytotoxicity, and a statistical approach to defining the bounds of the CTB was developed. To focus AOP development on the molecular targets corresponding to ToxCast assays indicating pathway-specific effects, we conducted a meta-analysis to identify which assays most frequently respond at concentrations below the CTB.  A preliminary list of potentially important, target-specific assays was determined by ranking assays by the fraction of chemical hits below the CTB compared to the number of chemicals tested.  Additional priority assays were identified using a diagnostic-odds-ratio approach which gives greater ranking to assays with high specificity but low responsivity. Combined, the two prioritization methods identified several novel targets (e.g., peripheral benzodiazepine and progesterone receptors) to prioritize for AOP development, and affirmed the importance of a number of existing AOPs aligned with ToxCast targets (e.g., thyroperoxidase, estrogen receptor, aromatase). \n\nThis dataset is associated with the following publication:\nFay, K., J. Swintek, D. Villeneuve, S. Edwards, M. Nelms, B. Blackwell, and G. Ankley. Differentiating pathway-specific from non-specific effects in high-throughput toxicity data: A foundation for prioritizing adverse outcome pathway development.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  163(2): 500-515, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1434917",
-            "keyword": [
-                "computational toxicology",
-                "ToxCast",
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
+            "description": "Previous work identified a \u2018cytotoxic burst\u2019 (CTB) phenomenon wherein large numbers of the ToxCast assays begin to respond at or near test chemical concentrations that elicit cytotoxicity, and a statistical approach to defining the bounds of the CTB was developed. To focus AOP development on the molecular targets corresponding to ToxCast assays indicating pathway-specific effects, we conducted a meta-analysis to identify which assays most frequently respond at concentrations below the CTB.  A preliminary list of potentially important, target-specific assays was determined by ranking assays by the fraction of chemical hits below the CTB compared to the number of chemicals tested.  Additional priority assays were identified using a diagnostic-odds-ratio approach which gives greater ranking to assays with high specificity but low responsivity. Combined, the two prioritization methods identified several novel targets (e.g., peripheral benzodiazepine and progesterone receptors) to prioritize for AOP development, and affirmed the importance of a number of existing AOPs aligned with ToxCast targets (e.g., thyroperoxidase, estrogen receptor, aromatase). \n\nThis dataset is associated with the following publication:\nFay, K., J. Swintek, D. Villeneuve, S. Edwards, M. Nelms, B. Blackwell, and G. Ankley. Differentiating pathway-specific from non-specific effects in high-throughput toxicity data: A foundation for prioritizing adverse outcome pathway development.   TOXICOLOGICAL SCIENCES. Society of Toxicology, RESTON, VA,  163(2): 500-515, (2018).",
             "distribution": [
                 {
-                    "title": "data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434917/data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data.zip"
                 },
                 {
-                    "title": "cytoburst code.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434917/cytoburst%20code.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "cytoburst code.zip"
                 },
                 {
-                    "title": "Science hub_Cytotoxic burst_2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1434917/Science%20hub_Cytotoxic%20burst_2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science hub_Cytotoxic burst_2.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434917",
+            "keyword": [
+                "computational toxicology",
+                "ToxCast",
+                "adverse outcome pathway",
+                "ecotoxicology",
+                "endocrine disruption",
+                "screening and prioritization",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-30",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfy049"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74402,19 +74396,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfy049"
+            ],
+            "rights": null,
+            "title": "Differentiating Pathway-Specific From Nonspecific Effects in High-Throughput Toxicity Data: A Foundation for Prioritizing Adverse Outcome Pathway Development"
         },
         {
-            "title": "HTTK R Package v1.7 - Evaluation and Calibration of High-Throughput Predictions of Chemical Distribution to Tissues",
-            "description": "httk: High-Throughput Toxicokinetics\n\nFunctions and data tables for simulation and statistical analysis of chemical toxicokinetics (\"TK\") using data obtained from relatively high throughput, in vitro studies. Both physiologically-based (\"PBTK\") and empirical (e.g., one compartment) \"TK\" models can be parameterized for several hundred chemicals and multiple species. These models are solved efficiently, often using compiled (C-based) code. A Monte Carlo sampler is included for simulating biological variability and measurement limitations. Functions are also provided for exporting \"PBTK\" models to \"SBML\" and \"JARNAC\" for use with other simulation software. These functions and data provide a set of tools for in vitro-in vivo extrapolation (\"IVIVE\") of high throughput screening data (e.g., ToxCast) to real-world exposures via reverse dosimetry (also known as \"RTK\"). \n\nThis dataset is associated with the following publication:\nPearce, R., W. Setzer, J. Davis, and J. Wambaugh. Evaluation and Calibration of High-Throughput Predictions of Chemical Distribution to Tissues.   JOURNAL OF PHARMACOKINETICS AND PHARMACODYNAMICS. Springer, New York, NY, USA, 44(6): 549-565, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "John Wambaugh",
+                "hasEmail": "mailto:wambaugh.john@epa.gov"
+            },
+            "description": "httk: High-Throughput Toxicokinetics\n\nFunctions and data tables for simulation and statistical analysis of chemical toxicokinetics (\"TK\") using data obtained from relatively high throughput, in vitro studies. Both physiologically-based (\"PBTK\") and empirical (e.g., one compartment) \"TK\" models can be parameterized for several hundred chemicals and multiple species. These models are solved efficiently, often using compiled (C-based) code. A Monte Carlo sampler is included for simulating biological variability and measurement limitations. Functions are also provided for exporting \"PBTK\" models to \"SBML\" and \"JARNAC\" for use with other simulation software. These functions and data provide a set of tools for in vitro-in vivo extrapolation (\"IVIVE\") of high throughput screening data (e.g., ToxCast) to real-world exposures via reverse dosimetry (also known as \"RTK\"). \n\nThis dataset is associated with the following publication:\nPearce, R., W. Setzer, J. Davis, and J. Wambaugh. Evaluation and Calibration of High-Throughput Predictions of Chemical Distribution to Tissues.   JOURNAL OF PHARMACOKINETICS AND PHARMACODYNAMICS. Springer, New York, NY, USA, 44(6): 549-565, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://cran.r-project.org/web/packages/httk/index.html",
+                    "title": "https://cran.r-project.org/web/packages/httk/index.html"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1390262",
             "keyword": [
@@ -74427,19 +74430,10 @@
                 "ExpoCast",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "John Wambaugh",
-                "hasEmail": "mailto:wambaugh.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://cran.r-project.org/web/packages/httk/index.html",
-                    "accessURL": "https://cran.r-project.org/web/packages/httk/index.html"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-15",
-            "references": [
-                "https://doi.org/10.1007/s10928-017-9548-7"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74449,19 +74443,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10928-017-9548-7"
+            ],
+            "rights": null,
+            "title": "HTTK R Package v1.7 - Evaluation and Calibration of High-Throughput Predictions of Chemical Distribution to Tissues"
         },
         {
-            "title": "Simmons_DeGroot_Metabolism_mRNA_transfection_ApplInVitroTox_Data",
-            "description": "The US EPA\u2019s ToxCast program is designed to assess chemical perturbations of molecular and cellular endpoints using a variety of high-throughput screening (HTS) assays. However, existing HTS assays have limited or no xenobiotic metabolism which could lead to false positive (chemical is detoxified in vivo) as well as false negative results (chemical is bioactivated in vivo) and thus potential mischaracterization of chemical hazard. We have addressed this challenge by introducing the ten most prevalent human liver cytochrome P450 (CYP) enzymes into a human cell line (HEK293T) with low endogenous metabolic capacity. The CYP enzymes were introduced via transfection of modified mRNAs as singlets or as a mixture in relative proportions expressed in the liver. Initial experiments using luminogenic CYP450 substrates demonstrate that cell models express metabolic enzymes from the transfected mRNAs and activities are significantly increased when co-transfected with a CYP accessory protein, P450 oxidoreductase (POR). Transfected HEK293T cells demonstrate the ability to produce predicted metabolites following treatment with well-studied CYP substrates, with metabolite formation occurring through 18 hours post-treatment. As a demonstration of how this method can be used to retrofit existing HTS assays, a proof-of-concept screen for cytotoxicity in HEK293T cells was conducted using 56 test compounds. The results demonstrate that the xenobiotic metabolism conferred by transfection of CYP-encoding mRNAs shifts the dose-response relationship for certain test chemicals such as aflatoxin B1 (bioactivation) and fenazaquin (detoxification). Overall, transfection of CYP-encoding mRNAs is an effective and portable solution for retrofitting metabolic competence to existing cell-based HTS assays. \n\nThis dataset is associated with the following publication:\nDeGroot, D., A. Swank, R. Thomas, M. Strynar, M. Lee, P. Carmichael, and S. Simmons. mRNA transfection retrofits cell-based assays with xenobiotic metabolism.   JOURNAL OF PHARMACOLOGICAL & TOXICOLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 92: 77-94, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Steven Simmons",
+                "hasEmail": "mailto:simmons.steve@epa.gov"
+            },
+            "description": "The US EPA\u2019s ToxCast program is designed to assess chemical perturbations of molecular and cellular endpoints using a variety of high-throughput screening (HTS) assays. However, existing HTS assays have limited or no xenobiotic metabolism which could lead to false positive (chemical is detoxified in vivo) as well as false negative results (chemical is bioactivated in vivo) and thus potential mischaracterization of chemical hazard. We have addressed this challenge by introducing the ten most prevalent human liver cytochrome P450 (CYP) enzymes into a human cell line (HEK293T) with low endogenous metabolic capacity. The CYP enzymes were introduced via transfection of modified mRNAs as singlets or as a mixture in relative proportions expressed in the liver. Initial experiments using luminogenic CYP450 substrates demonstrate that cell models express metabolic enzymes from the transfected mRNAs and activities are significantly increased when co-transfected with a CYP accessory protein, P450 oxidoreductase (POR). Transfected HEK293T cells demonstrate the ability to produce predicted metabolites following treatment with well-studied CYP substrates, with metabolite formation occurring through 18 hours post-treatment. As a demonstration of how this method can be used to retrofit existing HTS assays, a proof-of-concept screen for cytotoxicity in HEK293T cells was conducted using 56 test compounds. The results demonstrate that the xenobiotic metabolism conferred by transfection of CYP-encoding mRNAs shifts the dose-response relationship for certain test chemicals such as aflatoxin B1 (bioactivation) and fenazaquin (detoxification). Overall, transfection of CYP-encoding mRNAs is an effective and portable solution for retrofitting metabolic competence to existing cell-based HTS assays. \n\nThis dataset is associated with the following publication:\nDeGroot, D., A. Swank, R. Thomas, M. Strynar, M. Lee, P. Carmichael, and S. Simmons. mRNA transfection retrofits cell-based assays with xenobiotic metabolism.   JOURNAL OF PHARMACOLOGICAL & TOXICOLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 92: 77-94, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Simmons_Steve/Metabolism_mRNA_transfection/",
+                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Simmons_Steve/Metabolism_mRNA_transfection/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407700",
             "keyword": [
@@ -74471,19 +74474,10 @@
                 "ToxCast",
                 "High throughput screening"
             ],
-            "contactPoint": {
-                "fn": "Steven Simmons",
-                "hasEmail": "mailto:simmons.steve@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Simmons_Steve/Metabolism_mRNA_transfection/",
-                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Simmons_Steve/Metabolism_mRNA_transfection/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-16",
-            "references": [
-                "https://doi.org/10.1016/j.vascn.2018.03.002"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74493,47 +74487,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.vascn.2018.03.002"
+            ],
+            "rights": null,
+            "title": "Simmons_DeGroot_Metabolism_mRNA_transfection_ApplInVitroTox_Data"
         },
         {
-            "title": "Rapid Experimental Estimates of Physicochemical Properties",
-            "description": "We have performed high-throughput experimental estimates of five physicochemical properties for a set of 200 chemicals to evaluate the consistency with previous measurements, factors impacting consistency and experimental success, and the applicability domain of the new data in relation to previously measured data and predictive models. \n\nThis dataset is associated with the following publication:\nNicolas, C., K. Mansouri, K. Phillips, C. Grulke, A. Richard, A. Williams, J. Rabinowitz, K. Isaacs, A. Yau, and J. Wambaugh. (ENVIRONMENTAL SCIENCE and TECHNOLOGY) Rapid Experimental Estimates of Physicochemical Properties to Inform Models and Testing.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 636: 901-909, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1395223",
-            "keyword": [
-                "physicochemical properties",
-                "QSAR modeling",
-                "quantitative structure activity relationship (QSAR)",
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "We have performed high-throughput experimental estimates of five physicochemical properties for a set of 200 chemicals to evaluate the consistency with previous measurements, factors impacting consistency and experimental success, and the applicability domain of the new data in relation to previously measured data and predictive models. \n\nThis dataset is associated with the following publication:\nNicolas, C., K. Mansouri, K. Phillips, C. Grulke, A. Richard, A. Williams, J. Rabinowitz, K. Isaacs, A. Yau, and J. Wambaugh. (ENVIRONMENTAL SCIENCE and TECHNOLOGY) Rapid Experimental Estimates of Physicochemical Properties to Inform Models and Testing.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 636: 901-909, (2018).",
             "distribution": [
                 {
-                    "title": "SI_tables.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395223/SI_tables.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SI_tables.xlsx"
                 },
                 {
-                    "title": "Supplemental_PhysChem_Submitted.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1395223/Supplemental_PhysChem_Submitted.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplemental_PhysChem_Submitted.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1395223",
+            "keyword": [
+                "physicochemical properties",
+                "QSAR modeling",
+                "quantitative structure activity relationship (QSAR)",
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-27",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2018.04.266"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74543,46 +74537,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2018.04.266"
+            ],
+            "rights": null,
+            "title": "Rapid Experimental Estimates of Physicochemical Properties"
         },
         {
-            "title": "Suspect Screening Analysis of Chemicals in Consumer Products",
-            "description": "A suspect screening analysis method is presented to rapidly characterize chemicals in 100 consumer products -- whether they be formulations (shampoos, paints), articles (upholsteries, shower curtains), or foods (cereals) \u2013 and therefore supports broader efforts to prioritize chemicals based on potential human health risks. A two-dimensional gas chromatography-time of flight/mass spectrometry method was used to screen for chemicals in selected products. Analysis yielded 4270 unique chemical signatures across the products, with 1602 signatures tentatively identified using the National Institute of Standards and Technology 2008 spectral database. Chemical standards confirmed the presence of 119 compounds. Of the 1602 chemicals, 1404 were not present in a public database of known consumer product chemicals. \n\nThis dataset is associated with the following publication:\nPhillips, K., A. Yau, K. Favela, K. Isaacs, A. McEachran, C. Grulke, A. Richard, A. Williams, J. Sobus, R. Thomas, and J. Wambaugh. Suspect Screening Analysis of Chemicals in Consumer Products.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(5): 3125-3135, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1391810",
-            "keyword": [
-                "consumer products",
-                "Gas chromatography-mass spectrometry (GC/MS)",
-                "ExpoCast",
-                "exposure"
-            ],
             "contactPoint": {
                 "fn": "John Wambaugh",
                 "hasEmail": "mailto:wambaugh.john@epa.gov"
             },
+            "description": "A suspect screening analysis method is presented to rapidly characterize chemicals in 100 consumer products -- whether they be formulations (shampoos, paints), articles (upholsteries, shower curtains), or foods (cereals) \u2013 and therefore supports broader efforts to prioritize chemicals based on potential human health risks. A two-dimensional gas chromatography-time of flight/mass spectrometry method was used to screen for chemicals in selected products. Analysis yielded 4270 unique chemical signatures across the products, with 1602 signatures tentatively identified using the National Institute of Standards and Technology 2008 spectral database. Chemical standards confirmed the presence of 119 compounds. Of the 1602 chemicals, 1404 were not present in a public database of known consumer product chemicals. \n\nThis dataset is associated with the following publication:\nPhillips, K., A. Yau, K. Favela, K. Isaacs, A. McEachran, C. Grulke, A. Richard, A. Williams, J. Sobus, R. Thomas, and J. Wambaugh. Suspect Screening Analysis of Chemicals in Consumer Products.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(5): 3125-3135, (2018).",
             "distribution": [
                 {
-                    "title": "suspect_screening_of_chemicals_in_consumer_products_SI_tables_v4_0.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1391810/suspect_screening_of_chemicals_in_consumer_products_SI_tables_v4_0.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "suspect_screening_of_chemicals_in_consumer_products_SI_tables_v4_0.xlsx"
                 },
                 {
-                    "title": "supporting_information_product_deformulation_v4_2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1391810/supporting_information_product_deformulation_v4_2.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "supporting_information_product_deformulation_v4_2.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1391810",
+            "keyword": [
+                "consumer products",
+                "Gas chromatography-mass spectrometry (GC/MS)",
+                "ExpoCast",
+                "exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-15",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b04781"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74592,19 +74586,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b04781"
+            ],
+            "rights": null,
+            "title": "Suspect Screening Analysis of Chemicals in Consumer Products"
         },
         {
-            "title": "Dataset of Measurements of parameters controlling the emissions of organophoshpate flame retardants in indoor environments",
-            "description": "The data presented in this data file is a product of a journal publication. The dataset contains measurements of mass transfer, material/air, and surface/air partition coefficients and emission concentrations of OPFRs in chambers and diffusion tubes. It also contains modeling data. \n\nThis dataset is associated with the following publication:\nLiang, Y., X. Liu, and M. Allen. Measurements of Parameters Controlling the Emissions of Organophosphate Flame Retardants in Indoor Environments.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  5821-5829, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Xiaoyu Liu",
+                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
+            },
+            "description": "The data presented in this data file is a product of a journal publication. The dataset contains measurements of mass transfer, material/air, and surface/air partition coefficients and emission concentrations of OPFRs in chambers and diffusion tubes. It also contains modeling data. \n\nThis dataset is associated with the following publication:\nLiang, Y., X. Liu, and M. Allen. Measurements of Parameters Controlling the Emissions of Organophosphate Flame Retardants in Indoor Environments.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  5821-5829, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413225/XiaoyuLiu_A-zs87_Data%20Tables%26Dictionary-20180427.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "XiaoyuLiu_A-zs87_Data Tables&Dictionary-20180427.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1413225",
             "keyword": [
@@ -74615,20 +74619,10 @@
                 "Material/air partition",
                 "Material-phase diffusion"
             ],
-            "contactPoint": {
-                "fn": "Xiaoyu Liu",
-                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "XiaoyuLiu_A-zs87_Data Tables&Dictionary-20180427.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1413225/XiaoyuLiu_A-zs87_Data%20Tables%26Dictionary-20180427.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-14",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b00224"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74638,40 +74632,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b00224"
+            ],
+            "rights": null,
+            "title": "Dataset of Measurements of parameters controlling the emissions of organophoshpate flame retardants in indoor environments"
         },
         {
-            "title": "Model codes and run scripts developed for the addition of Four-Dimensional Data Assimilation (FDDA) to the Model for Prediction Across Scales - Atmosphere (MPAS-A)",
-            "description": "Web link to a Zenodo repository containing Model codes, run scripts, the computational mesh definition file, and user instructions for the addition of Four-Dimensional Data Assimilation (FDDA) to the Model for Prediction Across Scales - Atmosphere (MPAS-A). \n\nThis dataset is associated with the following publication:\nBullock, R., H. Foroutan, R. Gilliam, and J. Herwehe. Adding four-dimensional data assimilation by analysis nudging to the Model for Prediction Across Scales \u2013 Atmosphere (version 4.0).   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 11: 2897-2922, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1434298",
-            "keyword": [
-                "data assimilation",
-                "meteorological model",
-                "air quality",
-                "global"
-            ],
             "contactPoint": {
                 "fn": "Orren Bullock",
                 "hasEmail": "mailto:bullock.russell@epa.gov"
             },
+            "description": "Web link to a Zenodo repository containing Model codes, run scripts, the computational mesh definition file, and user instructions for the addition of Four-Dimensional Data Assimilation (FDDA) to the Model for Prediction Across Scales - Atmosphere (MPAS-A). \n\nThis dataset is associated with the following publication:\nBullock, R., H. Foroutan, R. Gilliam, and J. Herwehe. Adding four-dimensional data assimilation by analysis nudging to the Model for Prediction Across Scales \u2013 Atmosphere (version 4.0).   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 11: 2897-2922, (2018).",
             "distribution": [
                 {
-                    "title": "https://doi.org/10.5281/zenodo.1101204",
-                    "accessURL": "https://doi.org/10.5281/zenodo.1101204"
+                    "accessURL": "https://doi.org/10.5281/zenodo.1101204",
+                    "title": "https://doi.org/10.5281/zenodo.1101204"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434298",
+            "keyword": [
+                "data assimilation",
+                "meteorological model",
+                "air quality",
+                "global"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-11",
-            "references": [
-                "https://doi.org/10.5194/gmd-11-2897-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74681,69 +74675,69 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/gmd-11-2897-2018"
+            ],
+            "rights": null,
+            "title": "Model codes and run scripts developed for the addition of Four-Dimensional Data Assimilation (FDDA) to the Model for Prediction Across Scales - Atmosphere (MPAS-A)"
         },
         {
-            "title": "Clarksburg green infrastructure data",
-            "description": "This data set includes 5-minute time series runoff and precipitation data of neighborhood catchments with a variety of stormwater control measures, and definition of individual precipitation-runoff events and associated runoff metrics. Also included are geospatial data that delineates the neighborhood catchments with their land use/land cover and stormwater infrastructure. \n\nThis dataset is associated with the following publication:\nWoznicki, S., K. Hondula, and T. Jarnagin. Effectiveness of landscape\u2010based green infrastructure for stormwater management in suburban catchments.   Hydrological Processes. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 32(15): 2346-2361, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1435427",
-            "keyword": [
-                "Green Infrastructure",
-                "Stormwater control measures",
-                "best management practices",
-                "urbanization",
-                "stormwater management",
-                "Maryland",
-                "USA"
-            ],
             "contactPoint": {
                 "fn": "S Jarnagin",
                 "hasEmail": "mailto:jarnagin.taylor@epa.gov"
             },
+            "description": "This data set includes 5-minute time series runoff and precipitation data of neighborhood catchments with a variety of stormwater control measures, and definition of individual precipitation-runoff events and associated runoff metrics. Also included are geospatial data that delineates the neighborhood catchments with their land use/land cover and stormwater infrastructure. \n\nThis dataset is associated with the following publication:\nWoznicki, S., K. Hondula, and T. Jarnagin. Effectiveness of landscape\u2010based green infrastructure for stormwater management in suburban catchments.   Hydrological Processes. John Wiley & Sons, Ltd., Indianapolis, IN, USA, 32(15): 2346-2361, (2018).",
             "distribution": [
                 {
-                    "title": "Readme_ClarksburgGeospatialData.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435427/Readme_ClarksburgGeospatialData.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Readme_ClarksburgGeospatialData.txt"
                 },
                 {
-                    "title": "ClarksburgGeospatialData.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435427/ClarksburgGeospatialData.zip",
-                    "mediaType": "application/zip"
+                    "mediaType": "application/zip",
+                    "title": "ClarksburgGeospatialData.zip"
                 },
                 {
-                    "title": "Readme_ClarksburgMonitoringData.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435427/Readme_ClarksburgMonitoringData.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Readme_ClarksburgMonitoringData.txt"
                 },
                 {
-                    "title": "ClarksburgMonitoringData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435427/ClarksburgMonitoringData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ClarksburgMonitoringData.xlsx"
                 },
                 {
-                    "title": "Readme_ClarksburgEventData.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435427/Readme_ClarksburgEventData.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Readme_ClarksburgEventData.txt"
                 },
                 {
-                    "title": "ClarksburgEventData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435427/ClarksburgEventData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ClarksburgEventData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435427",
+            "keyword": [
+                "Green Infrastructure",
+                "Stormwater control measures",
+                "best management practices",
+                "urbanization",
+                "stormwater management",
+                "Maryland",
+                "USA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-14",
-            "references": [
-                "https://doi.org/10.1002/hyp.13144"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74753,20 +74747,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/hyp.13144"
+            ],
+            "rights": null,
+            "title": "Clarksburg green infrastructure data"
         },
         {
-            "title": "Placeholder",
-            "description": "Placeholder. This dataset is not publicly accessible because: This manuscript is based on literature review. No analysis was performed and there is no data associated with this product. It can be accessed through the following means: This manuscript is based on literature review. No analysis was performed and there is no data associated with this product. Format: This manuscript is based on literature review. No analysis was performed and there is no data associated with this product. \n\nThis dataset is associated with the following publication:\nBriski, E., F. Chan, J. Darling, V. Lauringson, H. MacIsaac, A. Zhan, and S. Bailey. Beyond propagule pressure: importance of selection during the transport stage of biological invasions.   FRONTIERS IN ECOLOGY AND THE ENVIRONMENT. Ecological Society of America, Ithaca, NY, USA, 16(6): 345-353, (2018).",
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
+                "fn": "John Darling",
+                "hasEmail": "mailto:darling.john@epa.gov"
+            },
+            "description": "Placeholder. This dataset is not publicly accessible because: This manuscript is based on literature review. No analysis was performed and there is no data associated with this product. It can be accessed through the following means: This manuscript is based on literature review. No analysis was performed and there is no data associated with this product. Format: This manuscript is based on literature review. No analysis was performed and there is no data associated with this product. \n\nThis dataset is associated with the following publication:\nBriski, E., F. Chan, J. Darling, V. Lauringson, H. MacIsaac, A. Zhan, and S. Bailey. Beyond propagule pressure: importance of selection during the transport stage of biological invasions.   FRONTIERS IN ECOLOGY AND THE ENVIRONMENT. Ecological Society of America, Ithaca, NY, USA, 16(6): 345-353, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1369042",
             "keyword": [
                 "genetic diversity",
@@ -74774,14 +74772,10 @@
                 "selection",
                 "transport"
             ],
-            "contactPoint": {
-                "fn": "John Darling",
-                "hasEmail": "mailto:darling.john@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-14",
-            "references": [
-                "https://doi.org/10.1002/fee.1820"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74791,19 +74785,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/fee.1820"
+            ],
+            "rights": null,
+            "title": "Placeholder"
         },
         {
-            "title": "Human health impact of non-potable reuse of distributed wastewater and greywater treated by membrane bioreactors",
-            "description": "This dataset contains simulated annual probabilities of infection for non-potable indoor use of greywater or wastewater treated by membrane bioreactors and chlorine disinfection.  The .zip file contains .csv files for each combination of source water and pathogen; see readme file (read me file.txt) for data dictionary and file naming convention. \n\nThis dataset is associated with the following publication:\nSchoen, M., M. Jahne, and J. Garland. Human health impact of non-potable reuse of distributed wastewater and greywater treated by membrane bioreactors (Microbial Risk Analysis).   Microbial Risk Analysis. Elsevier B.V., Amsterdam,  NETHERLANDS, 9: 72-81, (2018).",
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
+            "description": "This dataset contains simulated annual probabilities of infection for non-potable indoor use of greywater or wastewater treated by membrane bioreactors and chlorine disinfection.  The .zip file contains .csv files for each combination of source water and pathogen; see readme file (read me file.txt) for data dictionary and file naming convention. \n\nThis dataset is associated with the following publication:\nSchoen, M., M. Jahne, and J. Garland. Human health impact of non-potable reuse of distributed wastewater and greywater treated by membrane bioreactors (Microbial Risk Analysis).   Microbial Risk Analysis. Elsevier B.V., Amsterdam,  NETHERLANDS, 9: 72-81, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1420321/csv%20files.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "csv files.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1420321",
             "keyword": [
@@ -74819,20 +74823,10 @@
                 "QMRA",
                 "pathogens"
             ],
-            "contactPoint": {
-                "fn": "Michael Jahne",
-                "hasEmail": "mailto:jahne.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "csv files.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1420321/csv%20files.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-08",
-            "references": [
-                "https://doi.org/10.1016/j.mran.2018.01.003"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74842,40 +74836,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.mran.2018.01.003"
+            ],
+            "rights": null,
+            "title": "Human health impact of non-potable reuse of distributed wastewater and greywater treated by membrane bioreactors"
         },
         {
-            "title": "CAIRSENSE-Denver",
-            "description": "The databases contain continuous sensor information as well as time stamped equivalent reference data. \n\nThis dataset is associated with the following publication:\nFeinberg, S., R. Williams, G. Hagler, J. Rickard, R. Brown, D. Garver, G. Harshfield, P. Stauffer, E. Mattson, R. Judge, and S. Garvey. Long-term evaluation of air sensor technology under ambient conditions in Denver, Colorado.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 11(8): 4605-4615, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1411532",
-            "keyword": [
-                "CAIRSENSE",
-                "Sensors",
-                "performance evaluations"
-            ],
             "contactPoint": {
                 "fn": "Ronald Williams",
                 "hasEmail": "mailto:williams.ronald@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1411532/documents/CAIRSENSE_DataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The databases contain continuous sensor information as well as time stamped equivalent reference data. \n\nThis dataset is associated with the following publication:\nFeinberg, S., R. Williams, G. Hagler, J. Rickard, R. Brown, D. Garver, G. Harshfield, P. Stauffer, E. Mattson, R. Judge, and S. Garvey. Long-term evaluation of air sensor technology under ambient conditions in Denver, Colorado.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 11(8): 4605-4615, (2018).",
             "distribution": [
                 {
-                    "title": "CAIRSENSE_DataFiles.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411532/CAIRSENSE_DataFiles.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CAIRSENSE_DataFiles.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1411532",
+            "keyword": [
+                "CAIRSENSE",
+                "Sensors",
+                "performance evaluations"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-01",
-            "references": [
-                "https://doi.org/10.5194/amt-11-4605-2018"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74886,20 +74882,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1411532/documents/CAIRSENSE_DataDictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.5194/amt-11-4605-2018"
+            ],
+            "rights": null,
+            "title": "CAIRSENSE-Denver"
         },
         {
-            "title": "Evaluation of Formaldehyde Column Observations by Pandora Spectrometers",
-            "description": "Data collected for this research provides information on mixing heights, surface and column formaldehyde during the KORUS-AQ field campaign and over two research sites in South Korea. \n\nThis dataset is associated with the following publication:\nSpinei, E., A. Whitehill, A. Fried, M. Tiefengraber, T. Knepp, S. Herndon, J. Herman, M. Muller, N. Abuhassan, A. Cede, D. Richter, J. Walega, J. Crawford, J. Szykman, L. Valin, D. Williams, R. Long, R. Swap, Y. Lee, N. Nowak, and B. Poche. The first evaluation of formaldehyde column observations by improved Pandora spectrometers during the KORUS-AQ field study.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 11(9): 4943-4961, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "James Szykman",
+                "hasEmail": "mailto:szykman.jim@epa.gov"
+            },
+            "describedBy": "https://www-air.larc.nasa.gov/missions/korus-aq/",
+            "description": "Data collected for this research provides information on mixing heights, surface and column formaldehyde during the KORUS-AQ field campaign and over two research sites in South Korea. \n\nThis dataset is associated with the following publication:\nSpinei, E., A. Whitehill, A. Fried, M. Tiefengraber, T. Knepp, S. Herndon, J. Herman, M. Muller, N. Abuhassan, A. Cede, D. Richter, J. Walega, J. Crawford, J. Szykman, L. Valin, D. Williams, R. Long, R. Swap, Y. Lee, N. Nowak, and B. Poche. The first evaluation of formaldehyde column observations by improved Pandora spectrometers during the KORUS-AQ field study.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 11(9): 4943-4961, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://www-air.larc.nasa.gov/missions/korus-aq/",
+                    "title": "https://www-air.larc.nasa.gov/missions/korus-aq/"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1431211",
             "keyword": [
@@ -74911,19 +74915,10 @@
                 "mixing heights",
                 "column formaldehyde"
             ],
-            "contactPoint": {
-                "fn": "James Szykman",
-                "hasEmail": "mailto:szykman.jim@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www-air.larc.nasa.gov/missions/korus-aq/",
-                    "accessURL": "https://www-air.larc.nasa.gov/missions/korus-aq/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-21",
-            "references": [
-                "https://doi.org/10.5194/amt-11-4943-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74934,53 +74929,54 @@
                     }
                 }
             },
-            "describedBy": "https://www-air.larc.nasa.gov/missions/korus-aq/"
+            "references": [
+                "https://doi.org/10.5194/amt-11-4943-2018"
+            ],
+            "rights": null,
+            "title": "Evaluation of Formaldehyde Column Observations by Pandora Spectrometers"
         },
         {
-            "title": "Metals removal from mine influenced water",
-            "description": "The primary objective of this study was to evaluate the long-term effectiveness of a chitin (crushed crab shells) substrate compared to traditional ligneous (wood chips, hay, and manure) substrates on Zn, other metals (Al, Cu, Fe, Cd, Mn), and sulfate removal in MIW under anaerobic column bioreactor conditions. The secondary objective includes the evaluation of aeration and neutralization water pretreatment on the removal of the mentioned contaminants. \n\nThis dataset is associated with the following publication:\nPinto, P., S. Al-Abed, and J. McKernan. Comparison of the efficiency of chitinous and ligneous substrates in metal and sulfate removal from mining-influenced water.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 227(1): 321-328, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/10001",
-            "keyword": [
-                "acid mine drainage",
-                "zinc",
-                "manganese",
-                "sulfate reducing bacteria",
-                "anaerobic bioreactors",
-                "sulfate reduction rate"
-            ],
             "contactPoint": {
                 "fn": "Souhail Al-Abed",
                 "hasEmail": "mailto:al-abed.souhail@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/10001/documents/Data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The primary objective of this study was to evaluate the long-term effectiveness of a chitin (crushed crab shells) substrate compared to traditional ligneous (wood chips, hay, and manure) substrates on Zn, other metals (Al, Cu, Fe, Cd, Mn), and sulfate removal in MIW under anaerobic column bioreactor conditions. The secondary objective includes the evaluation of aeration and neutralization water pretreatment on the removal of the mentioned contaminants. \n\nThis dataset is associated with the following publication:\nPinto, P., S. Al-Abed, and J. McKernan. Comparison of the efficiency of chitinous and ligneous substrates in metal and sulfate removal from mining-influenced water.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 227(1): 321-328, (2018).",
             "distribution": [
                 {
-                    "title": "Key metals mass balance.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/10001/Key%20metals%20mass%20balance.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Key metals mass balance.xlsx"
                 },
                 {
-                    "title": "Sulfur Mass Balance.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/10001/Sulfur%20Mass%20Balance.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Sulfur Mass Balance.xlsx"
                 },
                 {
-                    "title": "Target metals in mol per liter Formosa Columns.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/10001/Target%20metals%20in%20mol%20per%20liter%20Formosa%20Columns.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Target metals in mol per liter Formosa Columns.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/10001",
+            "keyword": [
+                "acid mine drainage",
+                "zinc",
+                "manganese",
+                "sulfate reducing bacteria",
+                "anaerobic bioreactors",
+                "sulfate reduction rate"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-01-16",
-            "references": [
-                "https://doi.org/10.1016/j.jenvman.2018.08.113"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -74991,20 +74987,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/10001/documents/Data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.jenvman.2018.08.113"
+            ],
+            "rights": null,
+            "title": "Metals removal from mine influenced water"
         },
         {
-            "title": "Additional benefits of federal air quality rules: model estimates of controllable biogenic secondary organic aerosol",
-            "description": "Dataset is a link to the publically available CMAQ v5.1 model code. The following update was also implemented: \nhttps://github.com/USEPA/CMAQ/blob/5.2/CCTM/docs/Release_Notes/AH3OPJ_IEPOX_update.md. \n\nThis dataset is associated with the following publication:\nCarlton, A., H. Pye, K. Baker, and C. Hennigan. Additional Benefits of Federal Air-Quality Rules: Model Estimates of Controllable Biogenic Secondary Organic Aerosol.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(16): 9254\u20139265, (2018).",
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
+            "description": "Dataset is a link to the publically available CMAQ v5.1 model code. The following update was also implemented: \nhttps://github.com/USEPA/CMAQ/blob/5.2/CCTM/docs/Release_Notes/AH3OPJ_IEPOX_update.md. \n\nThis dataset is associated with the following publication:\nCarlton, A., H. Pye, K. Baker, and C. Hennigan. Additional Benefits of Federal Air-Quality Rules: Model Estimates of Controllable Biogenic Secondary Organic Aerosol.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(16): 9254\u20139265, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://dx.doi.org/10.5281/zenodo.1079909",
+                    "title": "https://dx.doi.org/10.5281/zenodo.1079909"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502526",
             "keyword": [
@@ -75015,19 +75018,10 @@
                 "Semivolatile Organic Compounds (SVOCs)",
                 "Biogenic VOC"
             ],
-            "contactPoint": {
-                "fn": "Havala Pye",
-                "hasEmail": "mailto:pye.havala@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://dx.doi.org/10.5281/zenodo.1079909",
-                    "accessURL": "https://dx.doi.org/10.5281/zenodo.1079909"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-01",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b01869"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75037,42 +75031,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b01869"
+            ],
+            "rights": null,
+            "title": "Additional benefits of federal air quality rules: model estimates of controllable biogenic secondary organic aerosol"
         },
         {
-            "title": "Ballast water exchange and invasion risk posed by intra-coastal vessel traffic: An evaluation using high throughput sequencing  ",
-            "description": "Dataset including all data for samples analyzed in Darling et al. 2018 Environmental Science & Technology. Includes OTU counts for all samples, taxonomic assignments for all OTUs, variables associated with vessels, and family-level counts across all vessels (used for indicator analysis). File also includes metadata describing all variables. \n\nThis dataset is associated with the following publication:\nDarling, J., J. Martinson, Y. Gong, S. Okum, E. Pilgrim, K. Pagenkopp Lohan, J. Carney, and G. Ruiz. Ballast Water Exchange and Invasion Risk Posed by Intracoastal Vessel Traffic: An Evaluation Using High Throughput Sequencing.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(17): 9926-9936, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1435417",
-            "keyword": [
-                "ballast water",
-                "invasive species",
-                "ballast water exchange",
-                "high throughput sequencing",
-                "metabarcoding"
-            ],
             "contactPoint": {
                 "fn": "John Darling",
                 "hasEmail": "mailto:darling.john@epa.gov"
             },
+            "description": "Dataset including all data for samples analyzed in Darling et al. 2018 Environmental Science & Technology. Includes OTU counts for all samples, taxonomic assignments for all OTUs, variables associated with vessels, and family-level counts across all vessels (used for indicator analysis). File also includes metadata describing all variables. \n\nThis dataset is associated with the following publication:\nDarling, J., J. Martinson, Y. Gong, S. Okum, E. Pilgrim, K. Pagenkopp Lohan, J. Carney, and G. Ruiz. Ballast Water Exchange and Invasion Risk Posed by Intracoastal Vessel Traffic: An Evaluation Using High Throughput Sequencing.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(17): 9926-9936, (2018).",
             "distribution": [
                 {
-                    "title": "ES&Tdata.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435417/ES%26Tdata.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ES&Tdata.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435417",
+            "keyword": [
+                "ballast water",
+                "invasive species",
+                "ballast water exchange",
+                "high throughput sequencing",
+                "metabarcoding"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-08-21",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b02108"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75082,78 +75076,78 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b02108"
+            ],
+            "rights": null,
+            "title": "Ballast water exchange and invasion risk posed by intra-coastal vessel traffic: An evaluation using high throughput sequencing  "
         },
         {
-            "title": "Plasma Standards",
-            "description": "Digital droplet PCR fluorsence amplitude values from which plasmid copy concentrations of DNA standards were determined as described in D-EMMD-MEB-018-SOP-01and Journal article. Summary of  stability testing results also provided. \n\nThis dataset is associated with the following publication:\nSivaganesan, M., M. Varma, S. Siefring, and R. Haugland. Quantification of plasmid DNA standards for U.S. EPA fecal indicator bacteria qPCR methods by droplet digital PCR analysis.   JOURNAL OF MICROBIOLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 152: 135-142, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500439",
-            "keyword": [
-                "digital droplet pcr",
-                "dna standards",
-                "draft method c",
-                "epa methods 1609.1",
-                "epa methods 1611.1",
-                "qPCR"
-            ],
             "contactPoint": {
                 "fn": "Richard Haugland",
                 "hasEmail": "mailto:haugland.rich@epa.gov"
             },
+            "description": "Digital droplet PCR fluorsence amplitude values from which plasmid copy concentrations of DNA standards were determined as described in D-EMMD-MEB-018-SOP-01and Journal article. Summary of  stability testing results also provided. \n\nThis dataset is associated with the following publication:\nSivaganesan, M., M. Varma, S. Siefring, and R. Haugland. Quantification of plasmid DNA standards for U.S. EPA fecal indicator bacteria qPCR methods by droplet digital PCR analysis.   JOURNAL OF MICROBIOLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 152: 135-142, (2018).",
             "distribution": [
                 {
-                    "title": "Batch2_Data_Dictionary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_Data_Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_Data_Dictionary.xlsx"
                 },
                 {
-                    "title": "Batch2_stability_summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_stability_summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_stability_summary.xlsx"
                 },
                 {
-                    "title": "Batch2_Tube1-5_Data_Dictionary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_Tube1-5_Data_Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_Tube1-5_Data_Dictionary.xlsx"
                 },
                 {
-                    "title": "Batch2_Tube4_plasmid_amplitudes_summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_Tube4_plasmid_amplitudes_summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_Tube4_plasmid_amplitudes_summary.xlsx"
                 },
                 {
-                    "title": "Batch2_Tube3_plasmid_amplitudes_summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_Tube3_plasmid_amplitudes_summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_Tube3_plasmid_amplitudes_summary.xlsx"
                 },
                 {
-                    "title": "Batch2_Tube2_plasmid_amplitudes_summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_Tube2_plasmid_amplitudes_summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_Tube2_plasmid_amplitudes_summary.xlsx"
                 },
                 {
-                    "title": "Batch2_Tube1_plasmid_amplitudes_summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_Tube1_plasmid_amplitudes_summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_Tube1_plasmid_amplitudes_summary.xlsx"
                 },
                 {
-                    "title": "Batch2_Tube5_plasmid_amplitudes_summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500439/Batch2_Tube5_plasmid_amplitudes_summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Batch2_Tube5_plasmid_amplitudes_summary.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500439",
+            "keyword": [
+                "digital droplet pcr",
+                "dna standards",
+                "draft method c",
+                "epa methods 1609.1",
+                "epa methods 1611.1",
+                "qPCR"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-09-22",
-            "references": [
-                "https://doi.org/10.1016/j.mimet.2018.07.005"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75163,19 +75157,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.mimet.2018.07.005"
+            ],
+            "rights": null,
+            "title": "Plasma Standards"
         },
         {
-            "title": "Evolution of the US energy system and related emissions under varying social and technological development paradigms Dataset",
-            "description": "This data is associated with the manuscript \"Evolution of the US energy system and related emissions under varying social and technological development paradigms: Plausible scenarios for use in robust decision making\" which will be submitted to Environmental Science & Technology (ES&T). The research considers how the US energy system might evolve under four possible scenarios, including different technologies and different emission outcomes. \n\nThis dataset is associated with the following publication:\nBrown, K., T. Hottle, R. Bandyopadhyay, S. Babaee, R. Dodder, O. Kaplan, C. Lenox, and D. Loughlin. Evolution of the US energy system and related emissions under varying social and technological development paradigms: Plausible scenarios for use in robust decision making.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  8027-8038, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Kristen Brown",
+                "hasEmail": "mailto:brown.kristen@epa.gov"
+            },
+            "description": "This data is associated with the manuscript \"Evolution of the US energy system and related emissions under varying social and technological development paradigms: Plausible scenarios for use in robust decision making\" which will be submitted to Environmental Science & Technology (ES&T). The research considers how the US energy system might evolve under four possible scenarios, including different technologies and different emission outcomes. \n\nThis dataset is associated with the following publication:\nBrown, K., T. Hottle, R. Bandyopadhyay, S. Babaee, R. Dodder, O. Kaplan, C. Lenox, and D. Loughlin. Evolution of the US energy system and related emissions under varying social and technological development paradigms: Plausible scenarios for use in robust decision making.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA,  8027-8038, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411860/PathwaysFutureScenarios_ScienceHubData.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PathwaysFutureScenarios_ScienceHubData.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1411860",
             "keyword": [
@@ -75187,20 +75191,10 @@
                 "externality",
                 "energy modeling"
             ],
-            "contactPoint": {
-                "fn": "Kristen Brown",
-                "hasEmail": "mailto:brown.kristen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "PathwaysFutureScenarios_ScienceHubData.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411860/PathwaysFutureScenarios_ScienceHubData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-08",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b00575"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75210,19 +75204,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b00575"
+            ],
+            "rights": null,
+            "title": "Evolution of the US energy system and related emissions under varying social and technological development paradigms Dataset"
         },
         {
-            "title": "Dry Dep Comp_Wu et al_2018",
-            "description": "Datasets present results of comparisons of five commonly dry deposition algorithms for ozone and sulfur dioxide, including diurnal patterns in deposition velocities, leaf-level processes such as stomatal conductance, and sensitivity to use of modeled versus measured meteorology. \n\nThis dataset is associated with the following publication:\nWu, Z., D. Schwede, R. Vet, J. Walker, M. Shaw, R. Staebler, and L. Zhang. Evaluation and Intercomparison of Five North American Dry Deposition Algorithms at a Mixed Forest Site.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 10(7): 1571-1586, (2018).",
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
+            "description": "Datasets present results of comparisons of five commonly dry deposition algorithms for ozone and sulfur dioxide, including diurnal patterns in deposition velocities, leaf-level processes such as stomatal conductance, and sensitivity to use of modeled versus measured meteorology. \n\nThis dataset is associated with the following publication:\nWu, Z., D. Schwede, R. Vet, J. Walker, M. Shaw, R. Staebler, and L. Zhang. Evaluation and Intercomparison of Five North American Dry Deposition Algorithms at a Mixed Forest Site.   Journal of Advances in Modeling Earth Systems. John Wiley & Sons, Inc., Hoboken, NJ, USA, 10(7): 1571-1586, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1422888/Wu%20et%20al_DryDepModComp_2017.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Wu et al_DryDepModComp_2017.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1422888",
             "keyword": [
@@ -75236,20 +75240,10 @@
                 "bidirectional flux",
                 "micrometeorology"
             ],
-            "contactPoint": {
-                "fn": "John Walker",
-                "hasEmail": "mailto:walker.johnt@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Wu et al_DryDepModComp_2017.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1422888/Wu%20et%20al_DryDepModComp_2017.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-02-28",
-            "references": [
-                "https://doi.org/10.1029/2017ms001231"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75259,41 +75253,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1029/2017ms001231"
+            ],
+            "rights": null,
+            "title": "Dry Dep Comp_Wu et al_2018"
         },
         {
-            "title": "ScienceHub Supplement",
-            "description": "The study created 45 3-year regional climate simulations by downscaling historical reanalysis data using the WRF model.  The simulations are not an ensemble, but rather are explorations of various nudging strategies to elucidate and recommend best practices.  The data available with this research effort are a suite of 2D fields of hourly data in WRF I/O API (built upon netCDF) for each simulation and for the full 3-year study period.  There are additional post-processed and statistical data that were generated and archived for this effort.  Metadata associated with each simulation are in standard netCDF format. \n\nThis dataset is associated with the following publication:\nSpero, T., C. Nolte, M. Mallard, and J. Bowden. A Maieutic Exploration of Nudging Strategies for Regional Climate Applications Using the WRF Model.   JOURNAL OF APPLIED METEOROLOGY AND CLIMATOLOGY. American Meteorological Society, Boston, MA, USA, 57: 1883-1906, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500862",
-            "keyword": [
-                "WRF",
-                "nudging",
-                "regional climate modeling",
-                "dynamical downscaling"
-            ],
             "contactPoint": {
                 "fn": "Tanya Spero",
                 "hasEmail": "mailto:spero.tanya@epa.gov"
             },
+            "description": "The study created 45 3-year regional climate simulations by downscaling historical reanalysis data using the WRF model.  The simulations are not an ensemble, but rather are explorations of various nudging strategies to elucidate and recommend best practices.  The data available with this research effort are a suite of 2D fields of hourly data in WRF I/O API (built upon netCDF) for each simulation and for the full 3-year study period.  There are additional post-processed and statistical data that were generated and archived for this effort.  Metadata associated with each simulation are in standard netCDF format. \n\nThis dataset is associated with the following publication:\nSpero, T., C. Nolte, M. Mallard, and J. Bowden. A Maieutic Exploration of Nudging Strategies for Regional Climate Applications Using the WRF Model.   JOURNAL OF APPLIED METEOROLOGY AND CLIMATOLOGY. American Meteorological Society, Boston, MA, USA, 57: 1883-1906, (2018).",
             "distribution": [
                 {
-                    "title": "ScienceHub supplement.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500862/ScienceHub%20supplement.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "ScienceHub supplement.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500862",
+            "keyword": [
+                "WRF",
+                "nudging",
+                "regional climate modeling",
+                "dynamical downscaling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-16",
-            "references": [
-                "https://doi.org/10.1175/jamc-d-17-0360.1"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75303,41 +75297,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1175/jamc-d-17-0360.1"
+            ],
+            "rights": null,
+            "title": "ScienceHub Supplement"
         },
         {
-            "title": "CADETS Results by Site 050918",
-            "description": "Measured, continuous, and intermittent Allegheny River conductivity by site. \n\nThis dataset is associated with the following publication:\nBrown, K., G. Norris, K. Kovalcik, A. Kamal, K. Patnode, and M. Landis. Signal Decomposition of Conductivity Sensor Measurements on the Allegheny River, Pennsylvania.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 144(10): 04018103, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1500033",
-            "keyword": [
-                "Allegheny River",
-                "conductivity",
-                "Frequency",
-                "water sensor"
-            ],
             "contactPoint": {
                 "fn": "Gary Norris",
                 "hasEmail": "mailto:norris.gary@epa.gov"
             },
+            "description": "Measured, continuous, and intermittent Allegheny River conductivity by site. \n\nThis dataset is associated with the following publication:\nBrown, K., G. Norris, K. Kovalcik, A. Kamal, K. Patnode, and M. Landis. Signal Decomposition of Conductivity Sensor Measurements on the Allegheny River, Pennsylvania.   JOURNAL OF ENVIRONMENTAL ENGINEERING. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 144(10): 04018103, (2018).",
             "distribution": [
                 {
-                    "title": "CADETS Results by Site 050918.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500033/CADETS%20Results%20by%20Site%20050918.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CADETS Results by Site 050918.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500033",
+            "keyword": [
+                "Allegheny River",
+                "conductivity",
+                "Frequency",
+                "water sensor"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-09",
-            "references": [
-                "https://doi.org/10.1061/(asce)ee.1943-7870.0001423"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75347,19 +75341,36 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/(asce)ee.1943-7870.0001423"
+            ],
+            "rights": null,
+            "title": "CADETS Results by Site 050918"
         },
         {
-            "title": "Defining the Taxonomic Domain of Applicability for Mammalian-Based High-Throughput Screening Assays",
-            "description": "Final Data SeqAPASS v3.0.zip contains datasets from Sequence Alignment to Predict Across Species Susceptibility (SeqAPASS) tool versions 3.0 for all 497 proteins evaluated using Level 1 (primary amino acid sequence comparisons) and Level 2 (functional domain(s) sequence comparisons) to understand conservation of HTS targets across species. Each folder is labeled by the protein accession (identification number and SeqAPASS version), with subfolders containing Level 1 and Level 2 output from the SeqAPASS tool.\nSeqAPASS v3.0 Data in Assay Groups.zip Contains all SeqAPASS data sorted by ToxCast Assay Group (as described in manuscript materials and methods). The original SeqAPASS data for each assay group are found in the folders titled Cell Adhesion, Cytochrome P450, Cytokine, DNA Binding, Esterase, G protein-coupled receptor, Growth Factor, Hydrolase, Ion Channel, Kinase, Lyase, Methyltransferase, Nuclear Receptor, Oxidoreductase, Phophatase, Protease, Protease Inhibitor, and Transporter. The Data_L1_Output folders and Data_L2_Output folders provide summaries of the Level 1 and Level 2 data comparing across datasets (See manuscript Supplemental Data, Legend for further details). \n\nThis dataset is associated with the following publication:\nLaLone, C., D. Villeneuve, J. Doering, B. Blackwell, T. Transue, C. Simmons, J. Swintek, S. Degitz, A. Williams, and G. Ankley. Defining the taxonomic domain of applicability for mammalian-based high-throughput screening assays..   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(23): 13960-13971, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Carlie Lalone",
+                "hasEmail": "mailto:lalone.carlie@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1432209/documents/Data%20Dictionary%232.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Final Data SeqAPASS v3.0.zip contains datasets from Sequence Alignment to Predict Across Species Susceptibility (SeqAPASS) tool versions 3.0 for all 497 proteins evaluated using Level 1 (primary amino acid sequence comparisons) and Level 2 (functional domain(s) sequence comparisons) to understand conservation of HTS targets across species. Each folder is labeled by the protein accession (identification number and SeqAPASS version), with subfolders containing Level 1 and Level 2 output from the SeqAPASS tool.\nSeqAPASS v3.0 Data in Assay Groups.zip Contains all SeqAPASS data sorted by ToxCast Assay Group (as described in manuscript materials and methods). The original SeqAPASS data for each assay group are found in the folders titled Cell Adhesion, Cytochrome P450, Cytokine, DNA Binding, Esterase, G protein-coupled receptor, Growth Factor, Hydrolase, Ion Channel, Kinase, Lyase, Methyltransferase, Nuclear Receptor, Oxidoreductase, Phophatase, Protease, Protease Inhibitor, and Transporter. The Data_L1_Output folders and Data_L2_Output folders provide summaries of the Level 1 and Level 2 data comparing across datasets (See manuscript Supplemental Data, Legend for further details). \n\nThis dataset is associated with the following publication:\nLaLone, C., D. Villeneuve, J. Doering, B. Blackwell, T. Transue, C. Simmons, J. Swintek, S. Degitz, A. Williams, and G. Ankley. Defining the taxonomic domain of applicability for mammalian-based high-throughput screening assays..   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(23): 13960-13971, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1432209/Final%20Data%20SeqAPASS%20v3.0.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Final Data SeqAPASS v3.0.zip"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1432209/SeqAPASS%20v3.0%20Data%20in%20Assay%20Groups.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "SeqAPASS v3.0 Data in Assay Groups.zip"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1432209",
             "keyword": [
@@ -75374,25 +75385,10 @@
                 "screening and prioritization",
                 "networks"
             ],
-            "contactPoint": {
-                "fn": "Carlie Lalone",
-                "hasEmail": "mailto:lalone.carlie@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Final Data SeqAPASS v3.0.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1432209/Final%20Data%20SeqAPASS%20v3.0.zip",
-                    "mediaType": "application/x-zip-compressed"
-                },
-                {
-                    "title": "SeqAPASS v3.0 Data in Assay Groups.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1432209/SeqAPASS%20v3.0%20Data%20in%20Assay%20Groups.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-09",
-            "references": [
-                "https://doi.org/10.23719/1432209"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75403,20 +75399,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1432209/documents/Data%20Dictionary%232.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.23719/1432209"
+            ],
+            "rights": null,
+            "title": "Defining the Taxonomic Domain of Applicability for Mammalian-Based High-Throughput Screening Assays"
         },
         {
-            "title": "Comparative Toxicity of Smoldering Versus Flaming Emissions from Various Biomass Fuels",
-            "description": "This dataset includes physico-chemical characteristics of biomass smoke of five different fuels (red oak, peat, pine needles, pine, and eucalyptus) generated from a tube furnace system at two different combustion phases (smoldering and flaming) and also provides two toxicological outcomes (lung toxicity in mice and mutagenicity in Salmonella) associated with exposures to the biomass smoke PM collected by a cryo-trap system. \n\nThis dataset is associated with the following publication:\nKim, Y.H., S. Warren, T. Krantz, C. King, R. Jaskot, W.T. Preston, B. George, M. Hays, M. Landis, M. Higuchi, D. DeMarini, and I. Gilmour. Mutagenicity and Lung Toxicity of Smoldering Versus Flaming Emissions from Various Biomass Fuels: Implications for Health Effects from Wildland Fires.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 126(1): 1, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Matthew Gilmour",
+                "hasEmail": "mailto:gilmour.ian@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1374721/documents/Dictionary_A-tb3d.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This dataset includes physico-chemical characteristics of biomass smoke of five different fuels (red oak, peat, pine needles, pine, and eucalyptus) generated from a tube furnace system at two different combustion phases (smoldering and flaming) and also provides two toxicological outcomes (lung toxicity in mice and mutagenicity in Salmonella) associated with exposures to the biomass smoke PM collected by a cryo-trap system. \n\nThis dataset is associated with the following publication:\nKim, Y.H., S. Warren, T. Krantz, C. King, R. Jaskot, W.T. Preston, B. George, M. Hays, M. Landis, M. Higuchi, D. DeMarini, and I. Gilmour. Mutagenicity and Lung Toxicity of Smoldering Versus Flaming Emissions from Various Biomass Fuels: Implications for Health Effects from Wildland Fires.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 126(1): 1, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1374721/Research%20Data_A-tb3d.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Research Data_A-tb3d.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1374721",
             "keyword": [
@@ -75428,20 +75434,10 @@
                 "Wildfires",
                 "particulate matter"
             ],
-            "contactPoint": {
-                "fn": "Matthew Gilmour",
-                "hasEmail": "mailto:gilmour.ian@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Research Data_A-tb3d.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1374721/Research%20Data_A-tb3d.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-10",
-            "references": [
-                "https://doi.org/10.1289/ehp2200"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75452,70 +75448,68 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1374721/documents/Dictionary_A-tb3d.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1289/ehp2200"
+            ],
+            "rights": null,
+            "title": "Comparative Toxicity of Smoldering Versus Flaming Emissions from Various Biomass Fuels"
         },
         {
-            "title": "Nitrogen and nitrogen isotope data for wheat and barley exposed to CeO2 nanoparticles",
-            "description": "The effects of cerium oxide nanoparticles (CeO2-NPs) on 15N/14N ratio (\u03b415N) in wheat and barley were investigated.  Seedlings were exposed to 0 and 500 mg CeO2-NPs/L (Ce-0 and Ce-500, respectively) in hydroponic suspension supplied with NH4NO3, NH4+, or NO3-.  N uptake and \u03b415N discrimination (i.e. differences in \u03b415N of plant and \u03b415N of N source) were measured.  Results showed that N content and 15N abundance decreased in wheat but increased in barley.  Ce-500 only induced whole-plant \u03b415N discrimination (-1.48\u2030, P \u2264 0.10) with a simultaneous decrease (P \u2264 0.05) in whole-plant \u03b415N (-3.24\u2030) compared to Ce-0 (-2.74\u2030) in wheat in NH4+.  Ce-500 decreased (P \u2264 0.01) root \u03b415N of wheat in NH4NO3 and NH4+ (3.23 and -2.25\u2030, respectively) compared to Ce-0 (4.96 and -1.27\u2030, respectively), but increased (P \u2264 0.05) root \u03b415N of wheat in NO3- (3.27\u2030) compared to Ce-0 (2.60\u2030).  Synchrotron micro-XRF revealed the presence of CeO2-NPs in shoots of wheat and barley regardless of N source.  Although the longer-term consequences of CeO2-NP exposure on N uptake and metabolism are unknown, the results clearly show the potential for ENMs to interfere with plant metabolism of critical plant nutrients such as N even when toxicity is not observed. \n\nThis dataset is associated with the following publication:\nRico, C.M., M. Johnson, M.A. Marcus, and C.P. Andersen. Shifts in N and \u03b415N in wheat and barley exposed to cerium oxide nanoparticles.   NanoImpact. Elsevier B.V., Amsterdam,  NETHERLANDS, 11: 156-163, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1411219",
-            "keyword": [
-                "Synchrotron micro XRF",
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
+            "description": "The effects of cerium oxide nanoparticles (CeO2-NPs) on 15N/14N ratio (\u03b415N) in wheat and barley were investigated.  Seedlings were exposed to 0 and 500 mg CeO2-NPs/L (Ce-0 and Ce-500, respectively) in hydroponic suspension supplied with NH4NO3, NH4+, or NO3-.  N uptake and \u03b415N discrimination (i.e. differences in \u03b415N of plant and \u03b415N of N source) were measured.  Results showed that N content and 15N abundance decreased in wheat but increased in barley.  Ce-500 only induced whole-plant \u03b415N discrimination (-1.48\u2030, P \u2264 0.10) with a simultaneous decrease (P \u2264 0.05) in whole-plant \u03b415N (-3.24\u2030) compared to Ce-0 (-2.74\u2030) in wheat in NH4+.  Ce-500 decreased (P \u2264 0.01) root \u03b415N of wheat in NH4NO3 and NH4+ (3.23 and -2.25\u2030, respectively) compared to Ce-0 (4.96 and -1.27\u2030, respectively), but increased (P \u2264 0.05) root \u03b415N of wheat in NO3- (3.27\u2030) compared to Ce-0 (2.60\u2030).  Synchrotron micro-XRF revealed the presence of CeO2-NPs in shoots of wheat and barley regardless of N source.  Although the longer-term consequences of CeO2-NP exposure on N uptake and metabolism are unknown, the results clearly show the potential for ENMs to interfere with plant metabolism of critical plant nutrients such as N even when toxicity is not observed. \n\nThis dataset is associated with the following publication:\nRico, C.M., M. Johnson, M.A. Marcus, and C.P. Andersen. Shifts in N and \u03b415N in wheat and barley exposed to cerium oxide nanoparticles.   NanoImpact. Elsevier B.V., Amsterdam,  NETHERLANDS, 11: 156-163, (2018).",
             "distribution": [
                 {
-                    "title": "hydroponics NHNO barley Isotope - data repository for Chris.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411219/hydroponics%20NHNO%20barley%20Isotope%20-%20data%20repository%20for%20Chris.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "hydroponics NHNO barley Isotope - data repository for Chris.xlsx"
                 },
                 {
-                    "title": "hydroponics NO wheat Isotope - data repository for Chris.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411219/hydroponics%20NO%20wheat%20Isotope%20-%20data%20repository%20for%20Chris.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "hydroponics NO wheat Isotope - data repository for Chris.xlsx"
                 },
                 {
-                    "title": "hydroponics NHNO wheat Isotope - data repository for Chris.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411219/hydroponics%20NHNO%20wheat%20Isotope%20-%20data%20repository%20for%20Chris.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "hydroponics NHNO wheat Isotope - data repository for Chris.xlsx"
                 },
                 {
-                    "title": "hydroponics NO barley Isotope - data repository for Chris.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411219/hydroponics%20NO%20barley%20Isotope%20-%20data%20repository%20for%20Chris.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "hydroponics NO barley Isotope - data repository for Chris.xlsx"
                 },
                 {
-                    "title": "hydroponics NH barley Isotope - data repository for Chris.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411219/hydroponics%20NH%20barley%20Isotope%20-%20data%20repository%20for%20Chris.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "hydroponics NH barley Isotope - data repository for Chris.xlsx"
                 },
                 {
-                    "title": "hydroponics NH wheat Isotope - data repository for Chris.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1411219/hydroponics%20NH%20wheat%20Isotope%20-%20data%20repository%20for%20Chris.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "hydroponics NH wheat Isotope - data repository for Chris.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1411219",
+            "keyword": [
+                "Synchrotron micro XRF",
+                "ammonium nitrate",
+                "intergenerational effects",
+                "isotope",
+                "isotopic discrimination",
+                "nitrogen",
+                "engineered nanomaterials (ENMs)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-03-15",
-            "references": [
-                "https://doi.org/10.1016/j.impact.2018.08.003"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75525,19 +75519,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.impact.2018.08.003"
+            ],
+            "rights": null,
+            "title": "Nitrogen and nitrogen isotope data for wheat and barley exposed to CeO2 nanoparticles"
         },
         {
-            "title": "Mass-spectrometric identification of cyclic phenone metabolites produced by rainbow trout liver slices ",
-            "description": "Dataset  consists of 2 main files as follows: \n1. All main and Supplemental MS final figures used for manuscript preparation for better viewing (pdf file). Figures are copies of raw or analyzed data directly from the mass spectrometers experimental files generated during research.   Explanation of figures is provided in manuscript's text \n2. Xcel file (Mass calculator CPK metabolites original), containing a significant amount of  MS raw data obtained during the research for parent chemicals and metabolites. Emphasis was provided to the analyses of CPK metabolites. The file contains an Index page stating the content of each sheet. Because CPK metabolites were labelled differently as the research progressed, a Legend with the different labeling of each metabolite is presented on each sheet. \n\nThis dataset is associated with the following publication:\nKolanczyk, R., J. Serrano, M. Tapper, and P. Schmieder. A comparison of fish pesticide metabolic pathways with those of the rat and goat.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 94: 124-143, (2018).",
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
+            "description": "Dataset  consists of 2 main files as follows: \n1. All main and Supplemental MS final figures used for manuscript preparation for better viewing (pdf file). Figures are copies of raw or analyzed data directly from the mass spectrometers experimental files generated during research.   Explanation of figures is provided in manuscript's text \n2. Xcel file (Mass calculator CPK metabolites original), containing a significant amount of  MS raw data obtained during the research for parent chemicals and metabolites. Emphasis was provided to the analyses of CPK metabolites. The file contains an Index page stating the content of each sheet. Because CPK metabolites were labelled differently as the research progressed, a Legend with the different labeling of each metabolite is presented on each sheet. \n\nThis dataset is associated with the following publication:\nKolanczyk, R., J. Serrano, M. Tapper, and P. Schmieder. A comparison of fish pesticide metabolic pathways with those of the rat and goat.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 94: 124-143, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502623/Publication%20Metabolite%20Identification%20%20Figures.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Publication Metabolite Identification  Figures.pdf"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502623/mass%20calculator%20cpk%20metabolites%20Original.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "mass calculator cpk metabolites Original.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502623",
             "keyword": [
@@ -75552,25 +75561,10 @@
                 "LC-MS/MS",
                 "LC-ToF-MS"
             ],
-            "contactPoint": {
-                "fn": "Jose Serrano",
-                "hasEmail": "mailto:serrano.jose@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Publication Metabolite Identification  Figures.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502623/Publication%20Metabolite%20Identification%20%20Figures.pdf",
-                    "mediaType": "application/pdf"
-                },
-                {
-                    "title": "mass calculator cpk metabolites Original.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502623/mass%20calculator%20cpk%20metabolites%20Original.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-12",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2018.01.019"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75580,49 +75574,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2018.01.019"
+            ],
+            "rights": null,
+            "title": "Mass-spectrometric identification of cyclic phenone metabolites produced by rainbow trout liver slices "
         },
         {
-            "title": "NWCA Enzyme Decomposition Model",
-            "description": "Dataset contains wetland site information, microbial respiration and ecoenzyme data, enzyme decomposition model, and the program file to run the data analyses. \n\nThis dataset is associated with the following publication:\nHill , B., C. Elonen , L. Seifert, A. May, and E. Tarquinio. Microbial ecoenzyme stoichiometry, nutrient limitation, and organic matter decomposition in wetlands of the conterminous United States.   Wetlands Ecology and Management. Springer Science and Business Media B.V;Formerly Kluwer Academic Publishers B.V.,   GERMANY, 26: 425-439, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1390085",
-            "keyword": [
-                "climate",
-                "decomposition",
-                "ecoenzymes",
-                "land cover",
-                "soil",
-                "stoichiometry",
-                "wetlands"
-            ],
             "contactPoint": {
                 "fn": "Brian Hill",
                 "hasEmail": "mailto:hill.brian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1390085/documents/NWCA%20EDM%20Data%20Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Dataset contains wetland site information, microbial respiration and ecoenzyme data, enzyme decomposition model, and the program file to run the data analyses. \n\nThis dataset is associated with the following publication:\nHill , B., C. Elonen , L. Seifert, A. May, and E. Tarquinio. Microbial ecoenzyme stoichiometry, nutrient limitation, and organic matter decomposition in wetlands of the conterminous United States.   Wetlands Ecology and Management. Springer Science and Business Media B.V;Formerly Kluwer Academic Publishers B.V.,   GERMANY, 26: 425-439, (2018).",
             "distribution": [
                 {
-                    "title": "NWCA_EDM.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390085/NWCA_EDM.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NWCA_EDM.csv"
                 },
                 {
-                    "title": "NWCA EDM Program File.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390085/NWCA%20EDM%20Program%20File.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "NWCA EDM Program File.docx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390085",
+            "keyword": [
+                "climate",
+                "decomposition",
+                "ecoenzymes",
+                "land cover",
+                "soil",
+                "stoichiometry",
+                "wetlands"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-02-29",
-            "references": [
-                "https://doi.org/10.1007/s11273-017-9584-5"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75633,20 +75629,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1390085/documents/NWCA%20EDM%20Data%20Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1007/s11273-017-9584-5"
+            ],
+            "rights": null,
+            "title": "NWCA Enzyme Decomposition Model"
         },
         {
-            "title": "Adrenergic and glucocorticoid receptor antagonists reduce ozone-induced lung injury and inflammation",
-            "description": "This data set contains one Excel file. In this file are all the data pertaining to the effects of propranolol and mifepristone on ozone induced lung injury and inflammation . The different tabs of the spreadsheet pertain to each figure found in the manuscript. \n\nThis dataset is associated with the following publication:\nHenriquez, A., S. Snow, M. Schladweiler, C. Miller, J. Dye, A. Ledbetter, J. Richards, K. Mauge-Lewis, M. McGee, and U. Kodavanti. Adrenergic and glucocorticoid receptor antagonists reduce ozone-induced lung injury and inflammation.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 339: 161-171, (2018).",
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
+            "description": "This data set contains one Excel file. In this file are all the data pertaining to the effects of propranolol and mifepristone on ozone induced lung injury and inflammation . The different tabs of the spreadsheet pertain to each figure found in the manuscript. \n\nThis dataset is associated with the following publication:\nHenriquez, A., S. Snow, M. Schladweiler, C. Miller, J. Dye, A. Ledbetter, J. Richards, K. Mauge-Lewis, M. McGee, and U. Kodavanti. Adrenergic and glucocorticoid receptor antagonists reduce ozone-induced lung injury and inflammation.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 339: 161-171, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375329/Henriquez%202017%20Manuscript%20for%20AJP%20-%20Data%20for%20ScienceHub%20-%20Kodavanti.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Henriquez 2017 Manuscript for AJP - Data for ScienceHub - Kodavanti.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1375329",
             "keyword": [
@@ -75657,20 +75661,10 @@
                 "lung injury",
                 "lung inflammation"
             ],
-            "contactPoint": {
-                "fn": "Urmila Kodavanti",
-                "hasEmail": "mailto:kodavanti.urmila@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Henriquez 2017 Manuscript for AJP - Data for ScienceHub - Kodavanti.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375329/Henriquez%202017%20Manuscript%20for%20AJP%20-%20Data%20for%20ScienceHub%20-%20Kodavanti.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-14",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2017.12.006"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75680,41 +75674,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2017.12.006"
+            ],
+            "rights": null,
+            "title": "Adrenergic and glucocorticoid receptor antagonists reduce ozone-induced lung injury and inflammation"
         },
         {
-            "title": "DEPS sulfate measurements",
-            "description": "data consist of measurements of outdoor and personal sulfate measurements. \n\nThis dataset is associated with the following publication:\nBreen, M., Y. Xu, A. Schneider, R. Williams, and R. Devlin. Modeling individual exposures to ambient PM2.5 in the diabetes and the environment panel study (DEPS).   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 626: 807-816, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1407621",
-            "keyword": [
-                "Building infiltration of air pollutants",
-                "Fine Particulate Matter",
-                "Exposure modeling",
-                "health study"
-            ],
             "contactPoint": {
                 "fn": "Michael Breen",
                 "hasEmail": "mailto:breen.michael@epa.gov"
             },
+            "description": "data consist of measurements of outdoor and personal sulfate measurements. \n\nThis dataset is associated with the following publication:\nBreen, M., Y. Xu, A. Schneider, R. Williams, and R. Devlin. Modeling individual exposures to ambient PM2.5 in the diabetes and the environment panel study (DEPS).   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 626: 807-816, (2018).",
             "distribution": [
                 {
-                    "title": "specialxrfSulfur-feb-20-08_data_dic.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407621/specialxrfSulfur-feb-20-08_data_dic.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "specialxrfSulfur-feb-20-08_data_dic.xls"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407621",
+            "keyword": [
+                "Building infiltration of air pollutants",
+                "Fine Particulate Matter",
+                "Exposure modeling",
+                "health study"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-09-07",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2018.01.139"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75724,41 +75718,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2018.01.139"
+            ],
+            "rights": null,
+            "title": "DEPS sulfate measurements"
         },
         {
-            "title": "Three-dimensional WRF and CMAQ 2-km simulation output for California for January/February 2013",
-            "description": "These data include three-dimensional meteorological (WRF) and air quality (CMAQ) model output for a 2-km domain covering the San Joaquin Valley (SJV) of California for January and February of 2013. The WRF and CMAQ parameters used in the analysis presented in the research effort are listed in the attached spreadsheet. The WRF/CMAQ data themselves are located on EPA's asm tape archive in the directories below. These data are available upon request from the authors, specifically K. Wyat Appel (appel.wyat@epa.gov).\n\n/asm/MOD3EVAL/DISCOVERAQ/SJV/2km_Meso/WRF\n/asm/MOD3EVAL/DISCOVERAQ/SJV/2km_Meso/CMAQ. \n\nThis dataset is associated with the following publication:\nFriberg, M., R. Kahn, J. Limbacher, W. Appel, and J. Mulholland. Constraining chemical transport PM2.5 modeling outputs using surface monitor measurements and satellite retrievals: application over the San Joaquin Valley.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 12891-12913, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1502511",
-            "keyword": [
-                "model evaluation",
-                "PM2.5 air quality modeling",
-                "air quality modeling",
-                "Satellite Air Quality"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502511/documents/WyatAppel_A-f7mf_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "These data include three-dimensional meteorological (WRF) and air quality (CMAQ) model output for a 2-km domain covering the San Joaquin Valley (SJV) of California for January and February of 2013. The WRF and CMAQ parameters used in the analysis presented in the research effort are listed in the attached spreadsheet. The WRF/CMAQ data themselves are located on EPA's asm tape archive in the directories below. These data are available upon request from the authors, specifically K. Wyat Appel (appel.wyat@epa.gov).\n\n/asm/MOD3EVAL/DISCOVERAQ/SJV/2km_Meso/WRF\n/asm/MOD3EVAL/DISCOVERAQ/SJV/2km_Meso/CMAQ. \n\nThis dataset is associated with the following publication:\nFriberg, M., R. Kahn, J. Limbacher, W. Appel, and J. Mulholland. Constraining chemical transport PM2.5 modeling outputs using surface monitor measurements and satellite retrievals: application over the San Joaquin Valley.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 18: 12891-12913, (2018).",
             "distribution": [
                 {
-                    "title": "WRFCMAQ_v502_DISCOVER-AQ_CA_2km_variable_list_used_MFRIBERG.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502511/WRFCMAQ_v502_DISCOVER-AQ_CA_2km_variable_list_used_MFRIBERG.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "WRFCMAQ_v502_DISCOVER-AQ_CA_2km_variable_list_used_MFRIBERG.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502511",
+            "keyword": [
+                "model evaluation",
+                "PM2.5 air quality modeling",
+                "air quality modeling",
+                "Satellite Air Quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-05-16",
-            "references": [
-                "https://doi.org/10.5194/acp-18-12891-2018"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75769,20 +75765,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1502511/documents/WyatAppel_A-f7mf_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/acp-18-12891-2018"
+            ],
+            "rights": null,
+            "title": "Three-dimensional WRF and CMAQ 2-km simulation output for California for January/February 2013"
         },
         {
-            "title": "Great Sippewissett Marsh 2016 Data",
-            "description": "Data in this spreadsheet include methane, carbon dioxide, and nitrous oxide fluxes; soil pH; surface and subsurface soil temperature; and surface elevation relative to mean high water for study plots at Great Sippewissett Marsh collected in July, August, September and October 2016. \n\nThis dataset is associated with the following publication:\nMartin, R., C. Wigand, E. Elmstrom, J. Lloret, and I. Valiela. Long-term nutrient addition increases respiration and nitrous oxide emissions in a New England salt marsh.   Ecology and Evolution. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 8(10): 4958\u20134966, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Rose Martin",
+                "hasEmail": "mailto:martin.rose@epa.gov"
+            },
+            "description": "Data in this spreadsheet include methane, carbon dioxide, and nitrous oxide fluxes; soil pH; surface and subsurface soil temperature; and surface elevation relative to mean high water for study plots at Great Sippewissett Marsh collected in July, August, September and October 2016. \n\nThis dataset is associated with the following publication:\nMartin, R., C. Wigand, E. Elmstrom, J. Lloret, and I. Valiela. Long-term nutrient addition increases respiration and nitrous oxide emissions in a New England salt marsh.   Ecology and Evolution. Wiley-Blackwell Publishing, Hoboken, NJ, USA, 8(10): 4958\u20134966, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1369029/SippewissettSciHub.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SippewissettSciHub.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1369029",
             "keyword": [
@@ -75793,20 +75797,10 @@
                 "Salt marsh",
                 "cape cod"
             ],
-            "contactPoint": {
-                "fn": "Rose Martin",
-                "hasEmail": "mailto:martin.rose@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "SippewissettSciHub.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1369029/SippewissettSciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-10",
-            "references": [
-                "https://doi.org/10.1002/ece3.3955"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75816,40 +75810,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/ece3.3955"
+            ],
+            "rights": null,
+            "title": "Great Sippewissett Marsh 2016 Data"
         },
         {
-            "title": "Soil organic matter and amphibian exposure dataset",
-            "description": "Dataset containing experimental data and R scripts used for data analyses. \n\nThis dataset is associated with the following publication:\nVan Meter, R., D. Glinski, M. Henderson , and T. Purucker. Soil organic matter content effects on dermal pesticide bioconcentration in American toads (Bufo americanus)..   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 35(11): 2734\u20132741, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "https://doi.org/10.23719/1500922",
-            "keyword": [
-                "amphibians",
-                "dermal exposure",
-                "soil organic matter",
-                "pesticides"
-            ],
             "contactPoint": {
                 "fn": "Steven Purucker",
                 "hasEmail": "mailto:purucker.tom@epa.gov"
             },
+            "description": "Dataset containing experimental data and R scripts used for data analyses. \n\nThis dataset is associated with the following publication:\nVan Meter, R., D. Glinski, M. Henderson , and T. Purucker. Soil organic matter content effects on dermal pesticide bioconcentration in American toads (Bufo americanus)..   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 35(11): 2734\u20132741, (2016).",
             "distribution": [
                 {
-                    "title": "https://github.com/puruckertom/vanmeteretal2016_etc_amphibian_exposure_som",
-                    "accessURL": "https://github.com/puruckertom/vanmeteretal2016_etc_amphibian_exposure_som"
+                    "accessURL": "https://github.com/puruckertom/vanmeteretal2016_etc_amphibian_exposure_som",
+                    "title": "https://github.com/puruckertom/vanmeteretal2016_etc_amphibian_exposure_som"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500922",
+            "keyword": [
+                "amphibians",
+                "dermal exposure",
+                "soil organic matter",
+                "pesticides"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-04",
-            "references": [
-                "https://doi.org/10.1002/etc.3439"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75859,40 +75853,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.3439"
+            ],
+            "rights": null,
+            "title": "Soil organic matter and amphibian exposure dataset"
         },
         {
-            "title": "Effect of contolled and spontaneous breathing on exhaled breath condensate characteristics",
-            "description": "The datasets provide physicochemical endpoint values (volumes, pH) for exhaled breath condensate collected with spontaneous breathing and \"controlled\" breathing patterns. The controlled breathing was enabled with audiovisual signals with a new instrument. The variability of the endpoint values was analyzed. \n\nThis dataset is associated with the following publication:\nWinters, B., J. Pleil, M. Angrish, M. Stiegel, T. Risby, and M. Madden. Standardization of the collection of exhaled breath condensate and exhaled breath aerosol using a feedback regulated sampling device.   Journal of Breath Research. Institute of Physics Publishing, Bristol,  UK, 11(4): 1, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503038",
-            "keyword": [
-                "cellular volatiles",
-                "high-throughput in vitro screening assay",
-                "cytochromeP450"
-            ],
             "contactPoint": {
                 "fn": "Michael Madden",
                 "hasEmail": "mailto:madden.michael@epa.gov"
             },
+            "description": "The datasets provide physicochemical endpoint values (volumes, pH) for exhaled breath condensate collected with spontaneous breathing and \"controlled\" breathing patterns. The controlled breathing was enabled with audiovisual signals with a new instrument. The variability of the endpoint values was analyzed. \n\nThis dataset is associated with the following publication:\nWinters, B., J. Pleil, M. Angrish, M. Stiegel, T. Risby, and M. Madden. Standardization of the collection of exhaled breath condensate and exhaled breath aerosol using a feedback regulated sampling device.   Journal of Breath Research. Institute of Physics Publishing, Bristol,  UK, 11(4): 1, (2017).",
             "distribution": [
                 {
-                    "title": "Winters 2017 SciHub data figs 3_4_5.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503038/Winters%202017%20SciHub%20data%20figs%203_4_5.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Winters 2017 SciHub data figs 3_4_5.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503038",
+            "keyword": [
+                "cellular volatiles",
+                "high-throughput in vitro screening assay",
+                "cytochromeP450"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-18",
-            "references": [
-                "https://doi.org/10.1088/1752-7163/aa8bbc"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75902,41 +75896,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1088/1752-7163/aa8bbc"
+            ],
+            "rights": null,
+            "title": "Effect of contolled and spontaneous breathing on exhaled breath condensate characteristics"
         },
         {
-            "title": "Ozone and IUGR CMiller",
-            "description": "Data related to the effects of peri-implantation ozone exposure on maternal and fetal health outcomes at the end of gestation. \n\nThis dataset is associated with the following publication:\nMiller, C., J. Dye, A. Ledbetter, M. Schladweiler, J. Richards, S. Snow, C. Wood, A. Henriquez, L. Thompson, A. Farraj, M. Hazari, and U. Kodavanti. Uterine Artery Flow and Offspring Growth in Long-Evans Rats following Maternal Exposure to Ozone during Implantation.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(12): 127005, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1375338",
-            "keyword": [
-                "Ozone",
-                "pregnancy",
-                "fetal growth assessment",
-                "preeclampsia"
-            ],
             "contactPoint": {
                 "fn": "Colette Miller",
                 "hasEmail": "mailto:miller.colette@epa.gov"
             },
+            "description": "Data related to the effects of peri-implantation ozone exposure on maternal and fetal health outcomes at the end of gestation. \n\nThis dataset is associated with the following publication:\nMiller, C., J. Dye, A. Ledbetter, M. Schladweiler, J. Richards, S. Snow, C. Wood, A. Henriquez, L. Thompson, A. Farraj, M. Hazari, and U. Kodavanti. Uterine Artery Flow and Offspring Growth in Long-Evans Rats following Maternal Exposure to Ozone during Implantation.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(12): 127005, (2017).",
             "distribution": [
                 {
-                    "title": "O3 and IUGR CMiller.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1375338/O3%20and%20IUGR%20CMiller.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "O3 and IUGR CMiller.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1375338",
+            "keyword": [
+                "Ozone",
+                "pregnancy",
+                "fetal growth assessment",
+                "preeclampsia"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-08-14",
-            "references": [
-                "https://doi.org/10.1289/ehp2019"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -75946,19 +75940,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp2019"
+            ],
+            "rights": null,
+            "title": "Ozone and IUGR CMiller"
         },
         {
-            "title": "Wetland Model Nitrogen and Carbon Data (Kent Island, MD, May 1995 - May 1997)",
-            "description": "This data are composed of precipitation, wetland water depth, volumetric soil moisture, nitrogen and carbon concentrations measured into and out of a wetland, and model computed soil moisture content as well as nitrogen and carbon loading from the wetland. The wetland is a restored treatment wetland, located in Kent Island, MD. \n\nThis dataset is associated with the following publication:\nSharifi, A., M. Hantush, and L. Kalin. Modeling Nitrogen and Carbon Dynamics in Wetland Soils and Water Using Mechanistic Wetland Model.  Rao S. Govindaraju  Journal of Hydrologic Engineering. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 22(1): 1-18, (2017).",
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
+            "description": "This data are composed of precipitation, wetland water depth, volumetric soil moisture, nitrogen and carbon concentrations measured into and out of a wetland, and model computed soil moisture content as well as nitrogen and carbon loading from the wetland. The wetland is a restored treatment wetland, located in Kent Island, MD. \n\nThis dataset is associated with the following publication:\nSharifi, A., M. Hantush, and L. Kalin. Modeling Nitrogen and Carbon Dynamics in Wetland Soils and Water Using Mechanistic Wetland Model.  Rao S. Govindaraju  Journal of Hydrologic Engineering. American Society of Civil Engineers  (ASCE), Reston, VA, USA, 22(1): 1-18, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502641/Mechansitic%20Wetland%20Model_unsaturated%20condition.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mechansitic Wetland Model_unsaturated condition.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1502641",
             "keyword": [
@@ -75978,20 +75982,10 @@
                 "GLUE",
                 "Monte Carlo method"
             ],
-            "contactPoint": {
-                "fn": "Mohamed Hantush",
-                "hasEmail": "mailto:hantush.mohamed@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Mechansitic Wetland Model_unsaturated condition.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502641/Mechansitic%20Wetland%20Model_unsaturated%20condition.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-02-01",
-            "references": [
-                "https://doi.org/10.1061/(asce)he.1943-5584.0001441"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76001,68 +75995,68 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/(asce)he.1943-5584.0001441"
+            ],
+            "rights": null,
+            "title": "Wetland Model Nitrogen and Carbon Data (Kent Island, MD, May 1995 - May 1997)"
         },
         {
-            "title": "Seasonal patterns of bole water content in old growth Douglas-fir",
-            "description": "Supporting data for figures and tables in publication. See Readme file. \n\nThis dataset is associated with the following publication:\nBeedlow, P., R. Waschmann, E. Lee, and D.T. Tingey. Seasonal patterns of bole water content in old growth Douglas-fir (Pseudotsuga menziesii (Mirb.) Franco).   AGRICULTURAL AND FOREST METEOROLOGY. Elsevier Science Ltd, New York, NY, USA, 242: 109-119, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1503045",
-            "keyword": [
-                "climate change",
-                "dendrochronology",
-                "Douglas-fir",
-                "Pacific Decadal Oscillation",
-                "Pacific Northwest",
-                "Swiss needle cast"
-            ],
             "contactPoint": {
                 "fn": "E. Lee",
                 "hasEmail": "mailto:lee.ehenry@epa.gov"
             },
+            "description": "Supporting data for figures and tables in publication. See Readme file. \n\nThis dataset is associated with the following publication:\nBeedlow, P., R. Waschmann, E. Lee, and D.T. Tingey. Seasonal patterns of bole water content in old growth Douglas-fir (Pseudotsuga menziesii (Mirb.) Franco).   AGRICULTURAL AND FOREST METEOROLOGY. Elsevier Science Ltd, New York, NY, USA, 242: 109-119, (2017).",
             "distribution": [
                 {
-                    "title": "Readme.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503045/Readme.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Readme.pdf"
                 },
                 {
-                    "title": "2004 - 2014 SGF(O) & SGF(Y) rBAI, RWC Bole and ASW Data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503045/2004%20-%202014%20SGF%28O%29%20%26%20SGF%28Y%29%20rBAI%2C%20RWC%20Bole%20and%20ASW%20Data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2004 - 2014 SGF(O) & SGF(Y) rBAI, RWC Bole and ASW Data.csv"
                 },
                 {
-                    "title": "2004 - YTD SGF(O) & SGF(Y) Theta Probe Hourly Data, w_ Climate Data.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503045/2004%20-%20YTD%20SGF%28O%29%20%26%20SGF%28Y%29%20Theta%20Probe%20Hourly%20Data%2C%20w_%20Climate%20Data.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2004 - YTD SGF(O) & SGF(Y) Theta Probe Hourly Data, w_ Climate Data.csv"
                 },
                 {
-                    "title": "Coefficient Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503045/Coefficient%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Coefficient Data.xlsx"
                 },
                 {
-                    "title": "Smoothed RWC, rBAI, Climate.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503045/Smoothed%20RWC%2C%20rBAI%2C%20Climate.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Smoothed RWC, rBAI, Climate.csv"
                 },
                 {
-                    "title": "Tissue Moisture, THETA_PROBE_TREES_SG_2004 - 2015.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503045/Tissue%20Moisture%2C%20THETA_PROBE_TREES_SG_2004%20-%202015.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tissue Moisture, THETA_PROBE_TREES_SG_2004 - 2015.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503045",
+            "keyword": [
+                "climate change",
+                "dendrochronology",
+                "Douglas-fir",
+                "Pacific Decadal Oscillation",
+                "Pacific Northwest",
+                "Swiss needle cast"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-24",
-            "references": [
-                "https://doi.org/10.1016/j.agrformet.2017.04.017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76072,19 +76066,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.agrformet.2017.04.017"
+            ],
+            "rights": null,
+            "title": "Seasonal patterns of bole water content in old growth Douglas-fir"
         },
         {
-            "title": "Varroapop sensitivity analysis scripts and output",
-            "description": "Code repository for scripts and model output associated with sensitivity analysis of the VarroaPop honeybee hive simulation model. \n\nThis dataset is associated with the following publication:\nKuan, C., G. DeGrandi-Hoffman, R. Curry, K. Garber, A. Kanarek, M. Snyder, K. Wolfe, and T. Purucker. Sensitivity analyses for simulating pesticide impacts on honey bee colonies.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 376: 15-27, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Steven Purucker",
+                "hasEmail": "mailto:purucker.tom@epa.gov"
+            },
+            "description": "Code repository for scripts and model output associated with sensitivity analysis of the VarroaPop honeybee hive simulation model. \n\nThis dataset is associated with the following publication:\nKuan, C., G. DeGrandi-Hoffman, R. Curry, K. Garber, A. Kanarek, M. Snyder, K. Wolfe, and T. Purucker. Sensitivity analyses for simulating pesticide impacts on honey bee colonies.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 376: 15-27, (2018).",
+            "distribution": [
+                {
+                    "accessURL": "https://github.com/puruckertom/kuanetal_varroapop_wrapper",
+                    "title": "https://github.com/puruckertom/kuanetal_varroapop_wrapper"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1500920",
             "keyword": [
@@ -76094,19 +76097,10 @@
                 "colony population model",
                 "pesticides"
             ],
-            "contactPoint": {
-                "fn": "Steven Purucker",
-                "hasEmail": "mailto:purucker.tom@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://github.com/puruckertom/kuanetal_varroapop_wrapper",
-                    "accessURL": "https://github.com/puruckertom/kuanetal_varroapop_wrapper"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-04",
-            "references": [
-                "https://doi.org/10.1016/j.ecolmodel.2018.02.010"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76116,47 +76110,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolmodel.2018.02.010"
+            ],
+            "rights": null,
+            "title": "Varroapop sensitivity analysis scripts and output"
         },
         {
-            "title": "HTAP_v2.2: a mosaic of regional and global emission gridmaps for 2008 and 2010 to study hemispheric transport of air pollution.",
-            "description": "This dataset provides the EPA portion of a compilation of different regional gridded inventories, including  data from Environment Canada for Canada, the European Monitoring and Evaluation Programme (EMEP) and Netherlands Organisation for Applied Scientific Research (TNO) for Europe, and the Model Inter-comparison Study in Asia (MICS-Asia)\u2019s for China, India and other Asian countries, and  gap-filled emission gridmaps of the Emissions Database for Global Atmospheric Research (EDGARv4.3) for the rest of the world (mainly South-America, Africa, Russia and Oceania).\nThe EPA data is included as netCDF formatted datasets at 0.1\u00ba \u00d7 0.1\u00ba resolution for 2010. This was the \u201craw\u201d data that was incorporated into the global mosaics.\nEmissions from seven main categories of human activities (power, industry, residential, agriculture, ground transport, aviation and shipping) were estimated and spatially distributed on a common grid of 0.1\u00ba \u00d7 0.1\u00ba longitude-latitude, to yield monthly, global, sector-specific gridmaps for each substance and year.\nEmission summaries from the supplemental information in the published journal article are also included. \n\nThis dataset is associated with the following publication:\nJanssens-Maenhout, G., M. Crippa, D. Guizzardi, F. Dentener, M. Muntean, G. Pouliot, T. Keating, Q. Zhang, J. Kurokawa, R. Wankmuller, H. Denier van der Gon, J.J.P. Kuenen, Z. Klimont, G. Frost, S. Darras, B. Koffi, and M. Li. HTAP_v2.2: a mosaic of regional and global emission grid maps for 2008 and 2010 to study hemispheric transport of air pollution.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 15(19): 11411-11432, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1502632",
-            "keyword": [
-                "HTAP",
-                "Global Emission Inventory",
-                "CMAQ",
-                "air quality modeling",
-                "model evaluation"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "description": "This dataset provides the EPA portion of a compilation of different regional gridded inventories, including  data from Environment Canada for Canada, the European Monitoring and Evaluation Programme (EMEP) and Netherlands Organisation for Applied Scientific Research (TNO) for Europe, and the Model Inter-comparison Study in Asia (MICS-Asia)\u2019s for China, India and other Asian countries, and  gap-filled emission gridmaps of the Emissions Database for Global Atmospheric Research (EDGARv4.3) for the rest of the world (mainly South-America, Africa, Russia and Oceania).\nThe EPA data is included as netCDF formatted datasets at 0.1\u00ba \u00d7 0.1\u00ba resolution for 2010. This was the \u201craw\u201d data that was incorporated into the global mosaics.\nEmissions from seven main categories of human activities (power, industry, residential, agriculture, ground transport, aviation and shipping) were estimated and spatially distributed on a common grid of 0.1\u00ba \u00d7 0.1\u00ba longitude-latitude, to yield monthly, global, sector-specific gridmaps for each substance and year.\nEmission summaries from the supplemental information in the published journal article are also included. \n\nThis dataset is associated with the following publication:\nJanssens-Maenhout, G., M. Crippa, D. Guizzardi, F. Dentener, M. Muntean, G. Pouliot, T. Keating, Q. Zhang, J. Kurokawa, R. Wankmuller, H. Denier van der Gon, J.J.P. Kuenen, Z. Klimont, G. Frost, S. Darras, B. Koffi, and M. Li. HTAP_v2.2: a mosaic of regional and global emission grid maps for 2008 and 2010 to study hemispheric transport of air pollution.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 15(19): 11411-11432, (2015).",
             "distribution": [
                 {
-                    "title": "Pouliot_A-k0pp_Dataset_20180829.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502632/Pouliot_A-k0pp_Dataset_20180829.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Pouliot_A-k0pp_Dataset_20180829.xlsx"
                 },
                 {
-                    "title": "Pouliot_A-k0pp_Dataset_20180910.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1502632/Pouliot_A-k0pp_Dataset_20180910.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Pouliot_A-k0pp_Dataset_20180910.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1502632",
+            "keyword": [
+                "HTAP",
+                "Global Emission Inventory",
+                "CMAQ",
+                "air quality modeling",
+                "model evaluation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2013-08-06",
-            "references": [
-                "https://doi.org/10.5194/acp-15-11411-2015"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76166,70 +76160,70 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-15-11411-2015"
+            ],
+            "rights": null,
+            "title": "HTAP_v2.2: a mosaic of regional and global emission gridmaps for 2008 and 2010 to study hemispheric transport of air pollution."
         },
         {
-            "title": "Role of TRPA1 in acrolein cardiac effects in mice",
-            "description": "Cardiac and ventilatory physiological data for mice exposed to acrolein. \n\nThis dataset is associated with the following publication:\nKurhanewicz, N., A. Ledbetter, A. Farraj, and M. Hazari. TRPA1 mediates the cardiac effects of acrolein through parasympathetic dominance but also sympathetic modulation in mice.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 347: 104-114, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1407607",
-            "keyword": [
-                "heart rate variability",
-                "ventilatory function",
-                "autonomic",
-                "air pollution",
-                "MICE",
-                "reflex",
-                "TRPA1",
-                "cardiovascular"
-            ],
             "contactPoint": {
                 "fn": "Mehdi Hazari",
                 "hasEmail": "mailto:hazari.mehdi@epa.gov"
             },
+            "description": "Cardiac and ventilatory physiological data for mice exposed to acrolein. \n\nThis dataset is associated with the following publication:\nKurhanewicz, N., A. Ledbetter, A. Farraj, and M. Hazari. TRPA1 mediates the cardiac effects of acrolein through parasympathetic dominance but also sympathetic modulation in mice.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 347: 104-114, (2018).",
             "distribution": [
                 {
-                    "title": "Autonomic redo HRV.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407607/Autonomic%20redo%20HRV.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Autonomic redo HRV.xlsx"
                 },
                 {
-                    "title": "Autonomic redo HRV_KO.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407607/Autonomic%20redo%20HRV_KO.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Autonomic redo HRV_KO.xlsx"
                 },
                 {
-                    "title": "Autonomic Redo Ventilatory Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407607/Autonomic%20Redo%20Ventilatory%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Autonomic Redo Ventilatory Data.xlsx"
                 },
                 {
-                    "title": "Autonomic Redo_effective dose.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407607/Autonomic%20Redo_effective%20dose.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Autonomic Redo_effective dose.xlsx"
                 },
                 {
-                    "title": "HRV_compiled_first drug administration.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407607/HRV_compiled_first%20drug%20administration.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HRV_compiled_first drug administration.xlsx"
                 },
                 {
-                    "title": "HRV Redo BAL and GPX data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407607/HRV%20Redo%20BAL%20and%20GPX%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HRV Redo BAL and GPX data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407607",
+            "keyword": [
+                "heart rate variability",
+                "ventilatory function",
+                "autonomic",
+                "air pollution",
+                "MICE",
+                "reflex",
+                "TRPA1",
+                "cardiovascular"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-01-31",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2018.03.027"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76239,42 +76233,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2018.03.027"
+            ],
+            "rights": null,
+            "title": "Role of TRPA1 in acrolein cardiac effects in mice"
         },
         {
-            "title": "Methane Transect Dataset",
-            "description": "This project area \u201cOTM 33 Mobile Emission Measurements\u201d covers research on remote emissions quantification with the various forms of mobile monitoring approaches. There will be multiple data sets included in this project. The metadata and data dictionaries are included with each data set. The data sets with metadata and data dictionaries are as follows:\r\n\r\nMethane Transect data Set:   The dataset contains mobile methane concentration measurements acquired at 10 samples per second data acquisition rate, collected while driving along transects downwind of a methane source.  The data consists of GPS coordinates, methane concetrion data and transect indicators.  The controlled methane release experiment was conducted on May 15, 2010 in Durham, North Carolina, where three passes were made for the one CR experiment and the point-source release rate was controlled at S = 0.6 g/s. Additionally, the dataset contains four field studies conducted in Colorado on four separate days in July 2010, with the number of passes for each study ranging from two to five. \n\nThis dataset is associated with the following publication:\nAlbertson, J., T. Foster-Wittig, A. Swingler, G. Foderaro, S. Ferrari, S. Amin, M. Modrak, H. Brantley , and E. Thoma. A Mobile Sensing Approach for Regional Surveillance of Fugitive Methane Emissions in Oil and Gas Production.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(5): 2487-2497, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1390071",
-            "keyword": [
-                "OTM 33",
-                "Mobile Measurements",
-                "GMAP",
-                "Methane",
-                "Fugitive Emissions"
-            ],
             "contactPoint": {
                 "fn": "Eben Thoma",
                 "hasEmail": "mailto:thoma.eben@epa.gov"
             },
+            "description": "This project area \u201cOTM 33 Mobile Emission Measurements\u201d covers research on remote emissions quantification with the various forms of mobile monitoring approaches. There will be multiple data sets included in this project. The metadata and data dictionaries are included with each data set. The data sets with metadata and data dictionaries are as follows:\r\n\r\nMethane Transect data Set:   The dataset contains mobile methane concentration measurements acquired at 10 samples per second data acquisition rate, collected while driving along transects downwind of a methane source.  The data consists of GPS coordinates, methane concetrion data and transect indicators.  The controlled methane release experiment was conducted on May 15, 2010 in Durham, North Carolina, where three passes were made for the one CR experiment and the point-source release rate was controlled at S = 0.6 g/s. Additionally, the dataset contains four field studies conducted in Colorado on four separate days in July 2010, with the number of passes for each study ranging from two to five. \n\nThis dataset is associated with the following publication:\nAlbertson, J., T. Foster-Wittig, A. Swingler, G. Foderaro, S. Ferrari, S. Amin, M. Modrak, H. Brantley , and E. Thoma. A Mobile Sensing Approach for Regional Surveillance of Fugitive Methane Emissions in Oil and Gas Production.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(5): 2487-2497, (2015).",
             "distribution": [
                 {
-                    "title": "Methane Transect Data Set.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390071/Methane%20Transect%20Data%20Set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Methane Transect Data Set.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390071",
+            "keyword": [
+                "OTM 33",
+                "Mobile Measurements",
+                "GMAP",
+                "Methane",
+                "Fugitive Emissions"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-27",
-            "references": [
-                "https://doi.org/10.1021/acs.est.5b05059"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76284,44 +76278,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.5b05059"
+            ],
+            "rights": null,
+            "title": "Methane Transect Dataset"
         },
         {
-            "title": "Li et al nitrification inhibition review",
-            "description": "Li et al nitrification inhibition review. \n\nThis dataset is associated with the following publication:\nKapoor, V., X. Li, C. Impellitteri , K. Chandran, and J. Santodomingo. Use of Functional Gene Expression and Respirometry to Study Wastewater Nitrification Activity after Exposure to Low Doses of Copper.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 23(7): 6443-6450, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1390094",
-            "keyword": [
-                "nitrification",
-                "RNA"
-            ],
             "contactPoint": {
                 "fn": "Jorge Santo Domingo",
                 "hasEmail": "mailto:santodomingo.jorge@epa.gov"
             },
+            "description": "Li et al nitrification inhibition review. \n\nThis dataset is associated with the following publication:\nKapoor, V., X. Li, C. Impellitteri , K. Chandran, and J. Santodomingo. Use of Functional Gene Expression and Respirometry to Study Wastewater Nitrification Activity after Exposure to Low Doses of Copper.   ENVIRONMENTAL SCIENCE AND POLLUTION RESEARCH. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY, 23(7): 6443-6450, (2016).",
             "distribution": [
                 {
-                    "title": "qPCR_results Ni Cd Zn Pb.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390094/qPCR_results%20Ni%20Cd%20Zn%20Pb.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "qPCR_results Ni Cd Zn Pb.xlsx"
                 },
                 {
-                    "title": "Nitrification_Inhibition-10_Inorganics.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390094/Nitrification_Inhibition-10_Inorganics.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Nitrification_Inhibition-10_Inorganics.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390094",
+            "keyword": [
+                "nitrification",
+                "RNA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.1007/s11356-015-5843-2"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76331,32 +76325,32 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11356-015-5843-2"
+            ],
+            "rights": null,
+            "title": "Li et al nitrification inhibition review"
         },
         {
-            "title": "The First Acid Ionization Constant of Cyanuric Acid from 5 to 35 \u00b0C",
-            "description": "No data set is provided. This dataset is not publicly accessible because: All the data is contained in the manuscript and supplementary information. It can be accessed through the following means: All the data is contained in the manuscript and supplementary information. Format: All the data is contained in the manuscript and supplementary information. \n\nThis dataset is associated with the following publication:\nWahman, D. First Acid Ionization Constant of the Drinking Water Relevant Chemical Cyanuric Acid from 5 to 35 \u00b0C.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 4: 1522-1530, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1412697",
-            "keyword": [
-                "cyanuric acid"
-            ],
             "contactPoint": {
                 "fn": "David Wahman",
                 "hasEmail": "mailto:wahman.david@epa.gov"
             },
+            "description": "No data set is provided. This dataset is not publicly accessible because: All the data is contained in the manuscript and supplementary information. It can be accessed through the following means: All the data is contained in the manuscript and supplementary information. Format: All the data is contained in the manuscript and supplementary information. \n\nThis dataset is associated with the following publication:\nWahman, D. First Acid Ionization Constant of the Drinking Water Relevant Chemical Cyanuric Acid from 5 to 35 \u00b0C.   Environmental Science: Water Research & Technology. Royal Society of Chemistry, Cambridge,  UK, 4: 1522-1530, (2018).",
             "distribution": [],
+            "identifier": "https://doi.org/10.23719/1412697",
+            "keyword": [
+                "cyanuric acid"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-12",
-            "references": [
-                "https://doi.org/10.1039/c8ew00431e"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76366,50 +76360,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c8ew00431e"
+            ],
+            "rights": null,
+            "title": "The First Acid Ionization Constant of Cyanuric Acid from 5 to 35 \u00b0C"
         },
         {
-            "title": "PM and levoglucosan data",
-            "description": "These are GC-MS data for producing the levoglucosan plot, black carbon data from an aethalometer, time series data of wind speed and normalized PM concentrations. As well as certain particle number and CO concentration data deltas. \n\nThis dataset is associated with the following publication:\nKimbrough , S., M. Hays , B. Preston, D. Vallero , and G. Hagler. Episodic Impacts from California Wildfires Identified in Las Vegas Near-Road Air Quality Monitoring.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(1): 18-24, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1390103",
-            "keyword": [
-                "levoglucosan",
-                "PM",
-                "BC",
-                "CO",
-                "wildfire",
-                "near-road",
-                "ambient air",
-                "air quality"
-            ],
             "contactPoint": {
                 "fn": "Evelyn Kimbrough",
                 "hasEmail": "mailto:kimbrough.sue@epa.gov"
             },
+            "description": "These are GC-MS data for producing the levoglucosan plot, black carbon data from an aethalometer, time series data of wind speed and normalized PM concentrations. As well as certain particle number and CO concentration data deltas. \n\nThis dataset is associated with the following publication:\nKimbrough , S., M. Hays , B. Preston, D. Vallero , and G. Hagler. Episodic Impacts from California Wildfires Identified in Las Vegas Near-Road Air Quality Monitoring.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(1): 18-24, (2016).",
             "distribution": [
                 {
-                    "title": "PM10_data_matlab_stepplot1.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390103/PM10_data_matlab_stepplot1.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "PM10_data_matlab_stepplot1.csv"
                 },
                 {
-                    "title": "Lg_data_matlab_stepplot2.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1390103/Lg_data_matlab_stepplot2.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Lg_data_matlab_stepplot2.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1390103",
+            "keyword": [
+                "levoglucosan",
+                "PM",
+                "BC",
+                "CO",
+                "wildfire",
+                "near-road",
+                "ambient air",
+                "air quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-08-20",
-            "references": [
-                "https://doi.org/10.1021/acs.est.5b05038"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76419,37 +76413,37 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.5b05038"
+            ],
+            "rights": null,
+            "title": "PM and levoglucosan data"
         },
         {
-            "title": "Data used and links to data and metadata",
-            "description": "The provided link will take users to all the data and metadata used in this project. \n\nThis dataset is associated with the following publication:\nAngradi, T., P. Ringold, and K. Hall. Water clarity measures as indicators of recreational benefits provided by U.S. lakes: Swimming and aesthetics.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 93: 1005-1019, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1434903",
-            "keyword": [
-                "EPA National Lake Assessment"
-            ],
             "contactPoint": {
                 "fn": "Theodore Angradi",
                 "hasEmail": "mailto:angradi.theodore@epa.gov"
             },
+            "description": "The provided link will take users to all the data and metadata used in this project. \n\nThis dataset is associated with the following publication:\nAngradi, T., P. Ringold, and K. Hall. Water clarity measures as indicators of recreational benefits provided by U.S. lakes: Swimming and aesthetics.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 93: 1005-1019, (2018).",
             "distribution": [
                 {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1434903",
+            "keyword": [
+                "EPA National Lake Assessment"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-04-27",
-            "references": [
-                "https://doi.org/10.1016/j.ecolind.2018.06.001"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76459,41 +76453,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolind.2018.06.001"
+            ],
+            "rights": null,
+            "title": "Data used and links to data and metadata"
         },
         {
-            "title": "Results for calcification and ingestion and retention rates of microbeads and microplastics. ",
-            "description": "Data is for three experiments. The first experiment examined calcification effects of ingested microbeads. The second experiment observed ingestion rates of four size classes of microbeads and how long they were retained. The third experiment observed and compared ingestion rates of one microbead size class and microfibers 3-5mm in length. \n\nThis dataset is associated with the following publication:\nHankins, C., A. Duffy, and K. Drisco. Scleractinian coral microplastic ingestion: Potential calcification effects, size limits, and retention.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 135: 587-593, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1435612",
-            "keyword": [
-                "coral",
-                "microplastic",
-                "ingestion",
-                "Retention"
-            ],
             "contactPoint": {
                 "fn": "Cheryl Hankins",
                 "hasEmail": "mailto:hankins.cheryl@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1435612/documents/DataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Data is for three experiments. The first experiment examined calcification effects of ingested microbeads. The second experiment observed ingestion rates of four size classes of microbeads and how long they were retained. The third experiment observed and compared ingestion rates of one microbead size class and microfibers 3-5mm in length. \n\nThis dataset is associated with the following publication:\nHankins, C., A. Duffy, and K. Drisco. Scleractinian coral microplastic ingestion: Potential calcification effects, size limits, and retention.   MARINE POLLUTION BULLETIN. Elsevier Science Ltd, New York, NY, USA, 135: 587-593, (2018).",
             "distribution": [
                 {
-                    "title": "AllData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435612/AllData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AllData.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435612",
+            "keyword": [
+                "coral",
+                "microplastic",
+                "ingestion",
+                "Retention"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-05-02",
-            "references": [
-                "https://doi.org/10.1016/j.marpolbul.2018.07.067"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76504,20 +76500,32 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1435612/documents/DataDictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.marpolbul.2018.07.067"
+            ],
+            "rights": null,
+            "title": "Results for calcification and ingestion and retention rates of microbeads and microplastics. "
         },
         {
-            "title": "Assessing the Social and Environmental Costs of Institutions Nitrogen Footprints",
-            "description": "This dataset allowed estimates the damage costs associated with the institutional nitrogen (N) footprint and explores how this information could be used to create more sustainable institutions. Potential damages associated with the release of nitrogen oxides (NOx), ammonia (NH3), and nitrous oxide (N2O) to air and release of nitrogen to water were estimated\nusing existing values and a cost per unit of nitrogen approach. These damage cost values were then applied to two universities. Annual potential damage costs to human health, agriculture, and natural ecosystems associated with the N footprint of institutions were $11.0 million (2014) at the University of Virginia (UVA) and $3.04 million at the University of New Hampshire (UNH). Costs associated with the release of nitrogen oxides to human health, in particular the use of coal-derived energy, were the largest component of damage at UVA. At UNH the energy N footprint is much lower because of a landfill cogeneration source, and thus the majority of damages were associated with food production. Annual damages associated with release of nitrogen from food production were very similar\nat the two universities ($1.80 million vs. $1.66 million at UVA and UNH, respectively). These damages also have implications for the extent and scale at which the damages are felt. For example, impacts to human health from energy and transportation are generally larger near the power plants and roads, while impacts from food production can be distant from the campus. Making this information available to institutions and communities can improve their understanding of the damages associated with the different nitrogen forms and sources, and inform decisions about\nnitrogen reduction strategies. \n\nThis dataset is associated with the following publication:\nCompton, J., A. Leach, E. Castner, and J. Galloway. Assessing the Social and Environmental Costs of Institutional Nitrogen Footprints.   Sustainability: The Journal of Record. Mary Ann Liebert, Inc., New Rochelle, NY, USA, 10(2): 114-122, (2017).",
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
+            "description": "This dataset allowed estimates the damage costs associated with the institutional nitrogen (N) footprint and explores how this information could be used to create more sustainable institutions. Potential damages associated with the release of nitrogen oxides (NOx), ammonia (NH3), and nitrous oxide (N2O) to air and release of nitrogen to water were estimated\nusing existing values and a cost per unit of nitrogen approach. These damage cost values were then applied to two universities. Annual potential damage costs to human health, agriculture, and natural ecosystems associated with the N footprint of institutions were $11.0 million (2014) at the University of Virginia (UVA) and $3.04 million at the University of New Hampshire (UNH). Costs associated with the release of nitrogen oxides to human health, in particular the use of coal-derived energy, were the largest component of damage at UVA. At UNH the energy N footprint is much lower because of a landfill cogeneration source, and thus the majority of damages were associated with food production. Annual damages associated with release of nitrogen from food production were very similar\nat the two universities ($1.80 million vs. $1.66 million at UVA and UNH, respectively). These damages also have implications for the extent and scale at which the damages are felt. For example, impacts to human health from energy and transportation are generally larger near the power plants and roads, while impacts from food production can be distant from the campus. Making this information available to institutions and communities can improve their understanding of the damages associated with the different nitrogen forms and sources, and inform decisions about\nnitrogen reduction strategies. \n\nThis dataset is associated with the following publication:\nCompton, J., A. Leach, E. Castner, and J. Galloway. Assessing the Social and Environmental Costs of Institutional Nitrogen Footprints.   Sustainability: The Journal of Record. Mary Ann Liebert, Inc., New Rochelle, NY, USA, 10(2): 114-122, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://online.liebertpub.com/doi/pdfplus/10.1089/sus.2017.29099.jec",
+                    "title": "https://online.liebertpub.com/doi/pdfplus/10.1089/sus.2017.29099.jec"
+                },
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407639/SciHub%20data%20ORD-019271.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub data ORD-019271.xlsx"
+                }
             ],
             "identifier": "https://doi.org/10.23719/1407639",
             "keyword": [
@@ -76530,24 +76538,10 @@
                 "point sources",
                 "N-fixation"
             ],
-            "contactPoint": {
-                "fn": "Jana Compton",
-                "hasEmail": "mailto:compton.jana@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://online.liebertpub.com/doi/pdfplus/10.1089/sus.2017.29099.jec",
-                    "accessURL": "https://online.liebertpub.com/doi/pdfplus/10.1089/sus.2017.29099.jec"
-                },
-                {
-                    "title": "SciHub data ORD-019271.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407639/SciHub%20data%20ORD-019271.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-09-27",
-            "references": [
-                "https://doi.org/10.1089/sus.2017.29099.jec"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76557,20 +76551,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1089/sus.2017.29099.jec"
+            ],
+            "rights": null,
+            "title": "Assessing the Social and Environmental Costs of Institutions Nitrogen Footprints"
         },
         {
-            "title": "Mineralogical Evidence of Galvanic Corrosion in Drinking Water Lead Pipe Joints",
-            "description": "The importance of galvanic corrosion as a mechanism of toxic lead release into drinking water has been under scientific debate in the U.S. for over 30 years. Visual and mineralogical analysis of 28 lead pipe joints, excavated after 60+ years by 8 U.S water utilities, provided the first direct view of galvanic corrosion presence/extent in practice. Three patterns were observed: (1) no galvanic corrosion; (2) galvanic corrosion with lead pipe cathodic relative to anodic copper/brass; (3) galvanic corrosion with lead pipe anodic relative to cathodic copper/brass. Pattern 3 is consistent with the order of increasing nobility found in empirical galvanic series (lead, brass, copper). Pattern 2 is consistent with galvanic battery reversion, possibly depending on certain water quality and/or flow conditions. A variety of copper-sulfate minerals (Pattern 2), and lead-sulfate and lead -chloride minerals (Pattern 3) were identified to form in the galvanic zones, with geochemical modeling confirming the required pH drop from the bulk water level to pH 3.0-4.0 (Pattern 2) and pH<5.5 (Pattern 3), as well as the migration of chloride and sulfate ions toward the sacrificial anode. Despite joints being over 60 years old, galvanic zones in Pattern 3 were active and possibly posed an important source of lead to drinking water. This dataset is not publicly accessible because: Overall, due to the nature of this observational research, no additional datasets would be useful to provide to the public. Most raw datasets in this research effort are not meaningful in x-y format and are not even readable by the public unless they own specialized software licenses, know how to use all of the software, and can interpret the data in its various formats as they relate to the project. The remainder of the information is photographs and tables with the raw data already included. It can be accessed through the following means: The data are generally very specific to the research topics explored, but could be shared with other researchers if requested. Interested parties who own and know how to use the specialized software involved in this research effort, may request the datasets by contacting the authors (our approved SDMP explains where all these records are located). Format: There is no single dataset and dataset format. The information is comprised of different files and electronic formats, mostly associated with specialized proprietary software that cannot be converted to x-y datasets in any meaningful way. The remainder of the information is photographs and tables with the raw data already included, so no additional raw data are needed for those. Our approved SDMP explains the data format for all figures and tables in this research effort. \n\nThis dataset is associated with the following publication:\nDeSantis, M., S. Triantafyllidou, M. Schock, and D. Lytle. Mineralogical Evidence of Galvanic Corrosion in Drinking Water Lead Pipe Joints.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(6): 3365-3374, (2018).",
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
+                "fn": "Michael Desantis",
+                "hasEmail": "mailto:desantis.mike@epa.gov"
+            },
+            "description": "The importance of galvanic corrosion as a mechanism of toxic lead release into drinking water has been under scientific debate in the U.S. for over 30 years. Visual and mineralogical analysis of 28 lead pipe joints, excavated after 60+ years by 8 U.S water utilities, provided the first direct view of galvanic corrosion presence/extent in practice. Three patterns were observed: (1) no galvanic corrosion; (2) galvanic corrosion with lead pipe cathodic relative to anodic copper/brass; (3) galvanic corrosion with lead pipe anodic relative to cathodic copper/brass. Pattern 3 is consistent with the order of increasing nobility found in empirical galvanic series (lead, brass, copper). Pattern 2 is consistent with galvanic battery reversion, possibly depending on certain water quality and/or flow conditions. A variety of copper-sulfate minerals (Pattern 2), and lead-sulfate and lead -chloride minerals (Pattern 3) were identified to form in the galvanic zones, with geochemical modeling confirming the required pH drop from the bulk water level to pH 3.0-4.0 (Pattern 2) and pH<5.5 (Pattern 3), as well as the migration of chloride and sulfate ions toward the sacrificial anode. Despite joints being over 60 years old, galvanic zones in Pattern 3 were active and possibly posed an important source of lead to drinking water. This dataset is not publicly accessible because: Overall, due to the nature of this observational research, no additional datasets would be useful to provide to the public. Most raw datasets in this research effort are not meaningful in x-y format and are not even readable by the public unless they own specialized software licenses, know how to use all of the software, and can interpret the data in its various formats as they relate to the project. The remainder of the information is photographs and tables with the raw data already included. It can be accessed through the following means: The data are generally very specific to the research topics explored, but could be shared with other researchers if requested. Interested parties who own and know how to use the specialized software involved in this research effort, may request the datasets by contacting the authors (our approved SDMP explains where all these records are located). Format: There is no single dataset and dataset format. The information is comprised of different files and electronic formats, mostly associated with specialized proprietary software that cannot be converted to x-y datasets in any meaningful way. The remainder of the information is photographs and tables with the raw data already included, so no additional raw data are needed for those. Our approved SDMP explains the data format for all figures and tables in this research effort. \n\nThis dataset is associated with the following publication:\nDeSantis, M., S. Triantafyllidou, M. Schock, and D. Lytle. Mineralogical Evidence of Galvanic Corrosion in Drinking Water Lead Pipe Joints.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(6): 3365-3374, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1404938",
             "keyword": [
                 "drinking water",
@@ -76581,14 +76579,10 @@
                 "brass",
                 "Copper"
             ],
-            "contactPoint": {
-                "fn": "Michael Desantis",
-                "hasEmail": "mailto:desantis.mike@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-10-11",
-            "references": [
-                "https://doi.org/10.1021/acs.est.7b06010"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76598,62 +76592,64 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.7b06010"
+            ],
+            "rights": null,
+            "title": "Mineralogical Evidence of Galvanic Corrosion in Drinking Water Lead Pipe Joints"
         },
         {
-            "title": "Data Set for A Call for an Aloft Air Quality Monitoring Network: Need and Feasibility",
-            "description": "This data set contains all relevant data used in the creation of the 4 illustrations in the manuscript. In all cases the data have been processed (averaged/aggregated over space and/or time) from the original data which was at finer spatial or temporal resolution. The observational data sets are publicly available from the CASTNET site. Raw model outputs can be made available by contacting the corresponding author. \n\nThis dataset is associated with the following publication:\nMathur, R., C. Hogrefe, A. Hakami, S. Zhao, J. Szykman, and G. Hagler. A Call for an Aloft Air Quality Monitoring Network: Need, Feasibility, and Potential Value.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(19): 10903\u201310908, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1408773",
-            "keyword": [
-                "long-range transport",
-                "background pollution",
-                "boundary layer",
-                "vertical profile",
-                "atmospheric mixing"
-            ],
             "contactPoint": {
                 "fn": "Rohit Mathur",
                 "hasEmail": "mailto:mathur.rohit@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1408773/documents/DataDictionary_AloftNetwork.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This data set contains all relevant data used in the creation of the 4 illustrations in the manuscript. In all cases the data have been processed (averaged/aggregated over space and/or time) from the original data which was at finer spatial or temporal resolution. The observational data sets are publicly available from the CASTNET site. Raw model outputs can be made available by contacting the corresponding author. \n\nThis dataset is associated with the following publication:\nMathur, R., C. Hogrefe, A. Hakami, S. Zhao, J. Szykman, and G. Hagler. A Call for an Aloft Air Quality Monitoring Network: Need, Feasibility, and Potential Value.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(19): 10903\u201310908, (2018).",
             "distribution": [
                 {
-                    "title": "Figure1_ptile_diurnal_pa_new.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408773/Figure1_ptile_diurnal_pa_new.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure1_ptile_diurnal_pa_new.txt"
                 },
                 {
-                    "title": "Figure1_InsetA_July2010_mod_obs_average_diurnal.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408773/Figure1_InsetA_July2010_mod_obs_average_diurnal.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure1_InsetA_July2010_mod_obs_average_diurnal.txt"
                 },
                 {
-                    "title": "Figure3_data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408773/Figure3_data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Figure3_data.zip"
                 },
                 {
-                    "title": "Figure4_data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408773/Figure4_data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Figure4_data.zip"
                 },
                 {
-                    "title": "Figure2_data_rate_8am9am_trends_21years_castnet_2seasons.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1408773/Figure2_data_rate_8am9am_trends_21years_castnet_2seasons.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure2_data_rate_8am9am_trends_21years_castnet_2seasons.csv"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1408773",
+            "keyword": [
+                "long-range transport",
+                "background pollution",
+                "boundary layer",
+                "vertical profile",
+                "atmospheric mixing"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-11-15",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b02496"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76664,53 +76660,51 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1408773/documents/DataDictionary_AloftNetwork.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b02496"
+            ],
+            "rights": null,
+            "title": "Data Set for A Call for an Aloft Air Quality Monitoring Network: Need and Feasibility"
         },
         {
-            "title": "Life Cycle Impact Assessment and Life Cycle Cost of both Legacy and Upgraded Systems",
-            "description": "LCIA and LCC data for legacy and updated systems under various scenarios. \n\nThis dataset is associated with the following publication:\nMorelli, B., S. Cashman, C. Ma, J. Garland, J. Turgeon, L. Fillmore, D. Bless, and M. Nye. Effect of Nutrient Removal and Resource Recovery on Life Cycle Cost and Environmental Impacts of a Small Scale Water Resource Recovery Facility.   Sustainability. MDPI AG, Basel,  SWITZERLAND, 10(10): 1-19, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "https://doi.org/10.23719/1407683",
-            "keyword": [
-                "biogas",
-                "chp",
-                "biological nutrient removal",
-                "resource recovery",
-                "energy recovery"
-            ],
             "contactPoint": {
                 "fn": "Xin Ma",
                 "hasEmail": "mailto:ma.cissy@epa.gov"
             },
+            "description": "LCIA and LCC data for legacy and updated systems under various scenarios. \n\nThis dataset is associated with the following publication:\nMorelli, B., S. Cashman, C. Ma, J. Garland, J. Turgeon, L. Fillmore, D. Bless, and M. Nye. Effect of Nutrient Removal and Resource Recovery on Life Cycle Cost and Environmental Impacts of a Small Scale Water Resource Recovery Facility.   Sustainability. MDPI AG, Basel,  SWITZERLAND, 10(10): 1-19, (2018).",
             "distribution": [
                 {
-                    "title": "Bath AD & Compost Model_v2_5.8.17.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407683/Bath%20AD%20%26%20Compost%20Model_v2_5.8.17.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Bath AD & Compost Model_v2_5.8.17.xlsx"
                 },
                 {
-                    "title": "Bath LCI_Legacy_v2_5.8.17.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407683/Bath%20LCI_Legacy_v2_5.8.17.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Bath LCI_Legacy_v2_5.8.17.xlsx"
                 },
                 {
-                    "title": "Bath_LCIA Results_v3_5.30.17.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1407683/Bath_LCIA%20Results_v3_5.30.17.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Bath_LCIA Results_v3_5.30.17.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1407683",
+            "keyword": [
+                "biogas",
+                "chp",
+                "biological nutrient removal",
+                "resource recovery",
+                "energy recovery"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-06-06",
-            "references": [
-                "https://doi.org/10.3390/su10103546"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76720,20 +76714,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/su10103546"
+            ],
+            "rights": null,
+            "title": "Life Cycle Impact Assessment and Life Cycle Cost of both Legacy and Upgraded Systems"
         },
         {
-            "title": "Supplementary material for Lee et al. in review: Harmonization and Revision of a National Diatom Dataset for Use in the Development of Water Quality Indicators",
-            "description": "ABSTRACT\nDiatom data have been collected in large-scale biological assessments in the United States, such as the U.S. Environmental Protection Agency\u2019s National Rivers and Streams Assessment (NRSA). However, the effectiveness of diatoms as indicators may suffer if inconsistent taxon identifications across different analysts obscure the relationships between assemblage composition and environmental variables. To reduce these inconsistencies, we harmonized the 2008-2009 NRSA data from nine analysts by updating names to current synonyms and by statistically identifying taxa with high analyst signal (taxa with more variation in relative abundance explained by the analyst factor, relative to environmental variables). We then screened a subset of samples with QA/QC data and combined taxa with mismatching identifications by the primary and secondary analysts. When these combined \u201cslash groups\u201d did not reduce analyst signal, we elevated taxa to the genus level or omitted taxa in difficult species complexes. We examined the variability explained by analyst in the original and revised datasets. Further, we examined how revising the datasets to reduce analyst signal can reduce inconsistency, thereby uncovering the variation in assemblage composition explained by total phosphorus (TP), an environmental variable of high priority for water managers. To produce a revised dataset with the greatest taxonomic consistency, we ultimately made 124 slash groups, omitted 7 taxa in the small naviculoid (e.g., Sellaphora atomoides) species complex, and elevated Nitzschia, Diploneis, and Tryblionella taxa to the genus level. Relative to the original dataset, the revised dataset had more overlap among samples grouped by analyst in ordination space, less variation explained by the analyst factor, and more than double the variation in assemblage composition explained by TP. Elevating all taxa to the genus level did not eliminate analyst signal completely, and analyst remained the most important predictor for the genera Sellaphora, Mayamaea, and Psammodictyon, indicating that these taxa present the greatest obstacle to consistent identification in this dataset. Although our process did not completely remove the analyst signal, this work clarifies the extent of the problem and provides a method to minimize analyst signal. Resolution of these taxonomic issues makes large datasets such as the NRSA more suitable for the development of diatom-based water quality indicators. This dataset is associated with the following publication:\nLee, S., I. Bishop, S. Spaulding, R. Mitchell, and L. Yuan. Taxonomic harmonization may reveal a stronger association between diatom assemblages and total phosphorus in large datasets..   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 102: 166-174, (2019). NOTE: This dataset has been removed from public access due to revocation. Please refer inquiries regarding this dataset to the listed contact person.",
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
+                "fn": "Sylvia Lee",
+                "hasEmail": "mailto:lee.sylvia@epa.gov"
+            },
+            "description": "ABSTRACT\nDiatom data have been collected in large-scale biological assessments in the United States, such as the U.S. Environmental Protection Agency\u2019s National Rivers and Streams Assessment (NRSA). However, the effectiveness of diatoms as indicators may suffer if inconsistent taxon identifications across different analysts obscure the relationships between assemblage composition and environmental variables. To reduce these inconsistencies, we harmonized the 2008-2009 NRSA data from nine analysts by updating names to current synonyms and by statistically identifying taxa with high analyst signal (taxa with more variation in relative abundance explained by the analyst factor, relative to environmental variables). We then screened a subset of samples with QA/QC data and combined taxa with mismatching identifications by the primary and secondary analysts. When these combined \u201cslash groups\u201d did not reduce analyst signal, we elevated taxa to the genus level or omitted taxa in difficult species complexes. We examined the variability explained by analyst in the original and revised datasets. Further, we examined how revising the datasets to reduce analyst signal can reduce inconsistency, thereby uncovering the variation in assemblage composition explained by total phosphorus (TP), an environmental variable of high priority for water managers. To produce a revised dataset with the greatest taxonomic consistency, we ultimately made 124 slash groups, omitted 7 taxa in the small naviculoid (e.g., Sellaphora atomoides) species complex, and elevated Nitzschia, Diploneis, and Tryblionella taxa to the genus level. Relative to the original dataset, the revised dataset had more overlap among samples grouped by analyst in ordination space, less variation explained by the analyst factor, and more than double the variation in assemblage composition explained by TP. Elevating all taxa to the genus level did not eliminate analyst signal completely, and analyst remained the most important predictor for the genera Sellaphora, Mayamaea, and Psammodictyon, indicating that these taxa present the greatest obstacle to consistent identification in this dataset. Although our process did not completely remove the analyst signal, this work clarifies the extent of the problem and provides a method to minimize analyst signal. Resolution of these taxonomic issues makes large datasets such as the NRSA more suitable for the development of diatom-based water quality indicators. This dataset is associated with the following publication:\nLee, S., I. Bishop, S. Spaulding, R. Mitchell, and L. Yuan. Taxonomic harmonization may reveal a stronger association between diatom assemblages and total phosphorus in large datasets..   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 102: 166-174, (2019). NOTE: This dataset has been removed from public access due to revocation. Please refer inquiries regarding this dataset to the listed contact person.",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1502631",
             "keyword": [
                 "taxonomy",
@@ -76741,13 +76739,11 @@
                 "diatoms",
                 "rivers and streams"
             ],
-            "contactPoint": {
-                "fn": "Sylvia Lee",
-                "hasEmail": "mailto:lee.sylvia@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-10-09",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -76756,40 +76752,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Supplementary material for Lee et al. in review: Harmonization and Revision of a National Diatom Dataset for Use in the Development of Water Quality Indicators"
         },
         {
-            "title": "Meta data ",
-            "description": "the data that was used to populate the tables and figures in the document. \n\nThis dataset is associated with the following publication:\nHuang, X., and T. Tolaymat. Gas Quantity and Composition from the Hydrolysis of Salt Cake from Secondary Aluminum Processing.  Majid Abbaspour  International Journal of Environmental Science and Technology. Springer, Heidelburg,  GERMANY,  1-12, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1435606",
-            "keyword": [
-                "reactive waste",
-                "aluminum dross",
-                "landfills"
-            ],
             "contactPoint": {
                 "fn": "Thabet Tolaymat",
                 "hasEmail": "mailto:tolaymat.thabet@epa.gov"
             },
+            "description": "the data that was used to populate the tables and figures in the document. \n\nThis dataset is associated with the following publication:\nHuang, X., and T. Tolaymat. Gas Quantity and Composition from the Hydrolysis of Salt Cake from Secondary Aluminum Processing.  Majid Abbaspour  International Journal of Environmental Science and Technology. Springer, Heidelburg,  GERMANY,  1-12, (2018).",
             "distribution": [
                 {
-                    "title": "Tolaymat SC hydrolysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1435606/Tolaymat%20SC%20hydrolysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tolaymat SC hydrolysis.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1435606",
+            "keyword": [
+                "reactive waste",
+                "aluminum dross",
+                "landfills"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-12-25",
-            "references": [
-                "https://doi.org/10.1007/s13762-018-1820-x"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76799,57 +76793,57 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s13762-018-1820-x"
+            ],
+            "rights": null,
+            "title": "Meta data "
         },
         {
-            "title": "Estimated floodplain map for the conterminous United States",
-            "description": "Understanding the relationship between flood inundation and floodplains is critical for ecosystem and community health and well-being, as well as targeting floodplain and riparian restoration. Many communities in the United States, particularly those in rural areas, lack inundation maps due to the high cost of flood modeling. Only 60% of the conterminous United States has Flood Insurance Rate Maps (FIRMs) through the U.S. Federal Emergency Management Agency (FEMA). This EnviroAtlas dataset provides an estimate of the 100-year floodplain for the conterminous United States at 30-meter resolution to fill the gaps in the FIRM. The model hit rate for the CONUS was 0.79 compared to the FIRM, indicating that the model captured 79% of the 100-year floodplain identified by FEMA. This product provides complete coverage for the CONUS by identifying floodplains in areas without FIRMs, while also identifying floodplains in tributaries sometimes excluded by FEMA. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets) or journal article (https://doi.org/10.1016/j.scitotenv.2018.07.353). This dataset is useful for evaluating the potential value of ecosystem services provided by floodplains. The overall goal of EnviroAtlas is to employ and develop the best available science to map indicators of ecosystem services production, demand, and drivers for the nation. These data are not meant to replace or supplement FEMA Flood Insurance Rate Maps. \n\nThis dataset is associated with the following publication:\nWoznicki, S., J. Baynes, S. Panlasigui, M. Mehaffey, and A. Neale. Development of a spatially complete floodplain map of the conterminous United States using random forest.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 647: 942-953, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "https://doi.org/10.23719/1503085",
-            "keyword": [
-                "Floodplain",
-                "random forest",
-                "EnviroAtlas",
-                "GIS",
-                "machine learning",
-                "ecosystem services"
-            ],
             "contactPoint": {
                 "fn": "Sean Woznicki",
                 "hasEmail": "mailto:woznicki.sean@epa.gov"
             },
+            "description": "Understanding the relationship between flood inundation and floodplains is critical for ecosystem and community health and well-being, as well as targeting floodplain and riparian restoration. Many communities in the United States, particularly those in rural areas, lack inundation maps due to the high cost of flood modeling. Only 60% of the conterminous United States has Flood Insurance Rate Maps (FIRMs) through the U.S. Federal Emergency Management Agency (FEMA). This EnviroAtlas dataset provides an estimate of the 100-year floodplain for the conterminous United States at 30-meter resolution to fill the gaps in the FIRM. The model hit rate for the CONUS was 0.79 compared to the FIRM, indicating that the model captured 79% of the 100-year floodplain identified by FEMA. This product provides complete coverage for the CONUS by identifying floodplains in areas without FIRMs, while also identifying floodplains in tributaries sometimes excluded by FEMA. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets) or journal article (https://doi.org/10.1016/j.scitotenv.2018.07.353). This dataset is useful for evaluating the potential value of ecosystem services provided by floodplains. The overall goal of EnviroAtlas is to employ and develop the best available science to map indicators of ecosystem services production, demand, and drivers for the nation. These data are not meant to replace or supplement FEMA Flood Insurance Rate Maps. \n\nThis dataset is associated with the following publication:\nWoznicki, S., J. Baynes, S. Panlasigui, M. Mehaffey, and A. Neale. Development of a spatially complete floodplain map of the conterminous United States using random forest.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 647: 942-953, (2018).",
             "distribution": [
                 {
-                    "title": "EnviroAtlas - Estimated floodplain map for CONUS - Random Forest Model Performance by HUC-4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503085/EnviroAtlas%20-%20Estimated%20floodplain%20map%20for%20CONUS%20-%20Random%20Forest%20Model%20Performance%20by%20HUC-4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EnviroAtlas - Estimated floodplain map for CONUS - Random Forest Model Performance by HUC-4.xlsx"
                 },
                 {
-                    "title": "EnviroAtlas - Estimated floodplain map for CONUS - Random Forest Model Performance by landscape classifications.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503085/EnviroAtlas%20-%20Estimated%20floodplain%20map%20for%20CONUS%20-%20Random%20Forest%20Model%20Performance%20by%20landscape%20classifications.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EnviroAtlas - Estimated floodplain map for CONUS - Random Forest Model Performance by landscape classifications.xlsx"
                 },
                 {
-                    "title": "EnviroAtlas - Estimated floodplain map for CONUS - Random Forest Scaled Variable Importance by HUC-4.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1503085/EnviroAtlas%20-%20Estimated%20floodplain%20map%20for%20CONUS%20-%20Random%20Forest%20Scaled%20Variable%20Importance%20by%20HUC-4.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EnviroAtlas - Estimated floodplain map for CONUS - Random Forest Scaled Variable Importance by HUC-4.xlsx"
                 },
                 {
-                    "title": "https://gaftp.epa.gov/epadatacommons/ORD/EnviroAtlas/Estimated_floodplain_CONUS.zip",
-                    "accessURL": "https://gaftp.epa.gov/epadatacommons/ORD/EnviroAtlas/Estimated_floodplain_CONUS.zip"
+                    "accessURL": "https://gaftp.epa.gov/epadatacommons/ORD/EnviroAtlas/Estimated_floodplain_CONUS.zip",
+                    "title": "https://gaftp.epa.gov/epadatacommons/ORD/EnviroAtlas/Estimated_floodplain_CONUS.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1503085",
+            "keyword": [
+                "Floodplain",
+                "random forest",
+                "EnviroAtlas",
+                "GIS",
+                "machine learning",
+                "ecosystem services"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2018-06-04",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2018.07.353"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76859,34 +76853,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2018.07.353"
+            ],
+            "rights": null,
+            "title": "Estimated floodplain map for the conterminous United States"
         },
         {
-            "title": "NEEAR Water Study-human markers",
-            "description": "Data set consists of survey data containing PII, water quality sample test results for fecal indicator bacteria and additional supporting information. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Upon request to Tim Wade (wade.tim@epa.gov). Format: Data are stored in SAS datasets with codebooks in MS Word  documenting variables. \n\nThis dataset is associated with the following publication:\nNapier, M., R. Haugland, C. Poole, A. Dufour, J. Stewart, D. Weber, M. Varma, J. Lavender, and T. Wade. Exposure to human-associated fecal indicators and self-reported illness among swimmers at recreational beaches: A cohort study.   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 16(1): 103, (2017).",
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
+                "fn": "Timothy Wade",
+                "hasEmail": "mailto:wade.tim@epa.gov"
+            },
+            "description": "Data set consists of survey data containing PII, water quality sample test results for fecal indicator bacteria and additional supporting information. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Upon request to Tim Wade (wade.tim@epa.gov). Format: Data are stored in SAS datasets with codebooks in MS Word  documenting variables. \n\nThis dataset is associated with the following publication:\nNapier, M., R. Haugland, C. Poole, A. Dufour, J. Stewart, D. Weber, M. Varma, J. Lavender, and T. Wade. Exposure to human-associated fecal indicators and self-reported illness among swimmers at recreational beaches: A cohort study.   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 16(1): 103, (2017).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1503031",
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
             "modified": "2017-10-01",
-            "references": [
-                "https://doi.org/10.1186/s12940-017-0308-3"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76896,34 +76890,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12940-017-0308-3"
+            ],
+            "rights": null,
+            "title": "NEEAR Water Study-human markers"
         },
         {
-            "title": "NEEAR Water Study-Chemicals",
-            "description": "data includes human health survey data, linked records of chemical measures and measures of water quality. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Upon request to Tim Wade (wade.tim@epa.gov). Format: Data are stored in SAS datasets with documented codebooks. \n\nThis dataset is associated with the following publication:\nNapier, M., C. Poole, J. Stewart, D. Weber, S. Glassmeyer, D. Kolpin, E. Furlong, A. Dufour, and T. Wade. Exposure to human-associated chemical markers of fecal contamination and self-reported illness among swimmers at recreational beaches.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(13): 7513-7523, (2018).",
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
+                "fn": "Timothy Wade",
+                "hasEmail": "mailto:wade.tim@epa.gov"
+            },
+            "description": "data includes human health survey data, linked records of chemical measures and measures of water quality. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Upon request to Tim Wade (wade.tim@epa.gov). Format: Data are stored in SAS datasets with documented codebooks. \n\nThis dataset is associated with the following publication:\nNapier, M., C. Poole, J. Stewart, D. Weber, S. Glassmeyer, D. Kolpin, E. Furlong, A. Dufour, and T. Wade. Exposure to human-associated chemical markers of fecal contamination and self-reported illness among swimmers at recreational beaches.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 52(13): 7513-7523, (2018).",
+            "distribution": [],
             "identifier": "https://doi.org/10.23719/1408779",
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
             "modified": "2017-11-15",
-            "references": [
-                "https://doi.org/10.1021/acs.est.8b00639"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76933,40 +76927,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.8b00639"
+            ],
+            "rights": null,
+            "title": "NEEAR Water Study-Chemicals"
         },
         {
-            "title": "Adaptation and application of multivariate AMBI (M-AMBI) in US coastal waters data",
-            "description": "extensively in Europe, but not in the United States. In a previous study, we adapted AMBI for use in US coastal waters (US AMBI), but saw biases in salinity and score distribution when compared to locally calibrated indices.\nIn this study we modified M-AMBI for US waters and compared its performance to that of US AMBI. Index performance was evaluated in three ways: 1) concordance with local indices presently being used as management\ntools in three geographic regions of US coastal waters, 2) classification accuracy for sites defined a priori as good or bad and 3) insensitivity to natural environmental gradients. US M-AMBI was highly correlated with all three local indices and removed the compression in response seen in moderately disturbed sites with US AMBI.  This data set provides the data used to conduct these analyses and produce the tables and figures in the paper. \n\nThis dataset is associated with the following publication:\nPelletier, P., D. Gillett, A. Hamilton, T. Grayson, V. Hansen, E. Leppo, S. Weisberg, and A. Borja. Adaptation and application of multivariate AMBI (M-AMBI) in US coastal waters.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 89: 818-827, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "https://doi.org/10.23719/1427171",
-            "keyword": [
-                "Benthos",
-                "Marine benthic invertebrates",
-                "benthic index"
-            ],
             "contactPoint": {
                 "fn": "Marguerite Pelletier",
                 "hasEmail": "mailto:pelletier.peg@epa.gov"
             },
+            "description": "extensively in Europe, but not in the United States. In a previous study, we adapted AMBI for use in US coastal waters (US AMBI), but saw biases in salinity and score distribution when compared to locally calibrated indices.\nIn this study we modified M-AMBI for US waters and compared its performance to that of US AMBI. Index performance was evaluated in three ways: 1) concordance with local indices presently being used as management\ntools in three geographic regions of US coastal waters, 2) classification accuracy for sites defined a priori as good or bad and 3) insensitivity to natural environmental gradients. US M-AMBI was highly correlated with all three local indices and removed the compression in response seen in moderately disturbed sites with US AMBI.  This data set provides the data used to conduct these analyses and produce the tables and figures in the paper. \n\nThis dataset is associated with the following publication:\nPelletier, P., D. Gillett, A. Hamilton, T. Grayson, V. Hansen, E. Leppo, S. Weisberg, and A. Borja. Adaptation and application of multivariate AMBI (M-AMBI) in US coastal waters.   ECOLOGICAL INDICATORS. Elsevier Science Ltd, New York, NY, USA, 89: 818-827, (2018).",
             "distribution": [
                 {
-                    "title": "M-AMBI_ScienceHub_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1427171/M-AMBI_ScienceHub_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "M-AMBI_ScienceHub_data.xlsx"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1427171",
+            "keyword": [
+                "Benthos",
+                "Marine benthic invertebrates",
+                "benthic index"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-07-24",
-            "references": [
-                "https://doi.org/10.1016/j.ecolind.2017.08.067"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -76976,34 +76970,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolind.2017.08.067"
+            ],
+            "rights": null,
+            "title": "Adaptation and application of multivariate AMBI (M-AMBI) in US coastal waters data"
         },
         {
-            "title": "Coliphages and gastrointestinal illness in recreational waters: pooled analysis of six coastal beach cohorts",
-            "description": "Data consists of health and survey data from epidemiological studies at beach sites and water quality measurements. This dataset is not publicly accessible because: EPA cannot release personally identifiable information regarding living individuals, according to the Privacy Act and the Freedom of Information Act (FOIA). This dataset contains information about human research subjects. Because there is potential to identify individual participants and disclose personal information, either alone or in combination with other datasets, individual level data are not appropriate to post for public access. Restricted access may be granted to authorized persons by contacting the party listed. It can be accessed through the following means: Data can be accessed by request to Tim Wade: wade.tim@epa.gov. Format: Data are stored in comma delimited text files with codebooks in MS Word. \n\nThis dataset is associated with the following publication:\nBenjamin-Chung, J., B. Arnold, T. Wade, K. Schiff, J. Griffith, A. Dufour, S. Weisberg, and J. Colford. Coliphages and gastrointestinal illness in recreational waters: pooled analysis of six coastal beach cohorts.   EPIDEMIOLOGY. Lippincott Williams & Wilkins, Philadelphia, PA, USA, 28(5): 644-652, (2017).",
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
+                "fn": "Timothy Wade",
+                "hasEmail": "mailto:wade.tim@epa.gov"
+            },
```

