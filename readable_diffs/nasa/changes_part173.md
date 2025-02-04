# Change History for nasa.json (Part 173)

### Changes from 31606f9 to dd2190f (Part 162/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000201",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Wide Field Camera (WFC)  L1B Science 125 m Native Science Data V1-10",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_wfc_l1_125m-prov-v1-10_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2010-09-21",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Wide Field Camera (WFC)  L1B Science 125 m Native Science Data V1-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/437/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marilyn Smith",
                 "hasEmail": "mailto:marilyn.smith@ae.gatech.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_437",
             "description": "This is the RSW fully tetrahedral unstructured mesh dataset for a cell-centered code, including the viscous wind tunnel wall.\r\n\r\nUG3      : Grid File Name    = rsw_coarse_tetcc.b8.ugrid\r\nUG3      : Quad Surface Faces=         0\r\nUG3      : Tria Surface Faces=     61750\r\nUG3      : Nodes             =   1357828\r\nUG3      : Total Elements    =   8050193\r\nUG3      : Hex Elements      =         0\r\nUG3      : Pent_5 Elements   =         0\r\nUG3      : Pent_6 Elements   =         0\r\nUG3      : Tet Elements      =   8050193\r\nUG3      : BL Tet Elements   =   7507013",
-            "title": "RSW Fully Tet Coarse Cell-Centered Mesh",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.b8.ugrid",
-                    "description": "ugrid file",
                     "@type": "dcat:Distribution",
+                    "description": "ugrid file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.b8.ugrid",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tetcc.b8.ugrid"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.cgns",
-                    "description": "CGNS Format Grid File",
                     "@type": "dcat:Distribution",
+                    "description": "CGNS Format Grid File",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.cgns",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tetcc.cgns"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.info",
-                    "description": "Grid Information",
                     "@type": "dcat:Distribution",
+                    "description": "Grid Information",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.info",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tetcc.info"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.mapbc",
-                    "description": "Mapbc file (FUN3D)",
                     "@type": "dcat:Distribution",
+                    "description": "Mapbc file (FUN3D)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.mapbc",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tetcc.mapbc"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.surf.gz",
-                    "description": "surface grid (gzipped)",
                     "@type": "dcat:Distribution",
+                    "description": "surface grid (gzipped)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.surf.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "rsw_coarse_tetcc.surf.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.tags",
-                    "description": "tag file",
                     "@type": "dcat:Distribution",
+                    "description": "tag file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tetcc.tags",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tetcc.tags"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_437",
+            "issued": "2011-07-18",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/437/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW Fully Tet Coarse Cell-Centered Mesh"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/611",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gower, S.T., O.N. Krankina, R.J. Olson, M.J. Apps, S. Linder, and C. Wang. 2012. NPP Boreal Forest: Consistent Worldwide Site Estimates, 1965-1995, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/611",
-            "issued": "2021-12-06",
-            "temporal": "1965-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "vegetation",
-                "ecological dynamics",
-                "earth science",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2751948194-ORNL_CLOUD",
             "description": "This data set provides estimates of above- and below-ground biomass, above- and below-ground NPP (ANPP and BNPP), and total NPP(TNPP) for selected North American and Eurasian boreal forests located between 66.37 degrees N and 47.5 degrees N. Each stand was selected through a review of published literature and classified into one of three classes, depending upon completeness of NPP budget, ancillary site data, and stand information. Within the overall 1965-1995 temporal range, data available for individual sites varies widely.There are two ASCII files (comma-separated-value format) of NPP data.\tThe first file provides carbon distribution in above- and below-ground vegetation biomass, above- and below-ground net primary production, and mean annual biomass increment for twenty-four (24) Class I sites which have complete NPP budgets (ANPP + BNPP). Information about site characteristics and NPP measurement approaches are also provided.\tThe second file provides stand information, carbon distribution in above-ground vegetation biomass, and ANPP data for forty-five (45) Class II boreal forest stands that have incomplete NPP budgets. Revision Notes:Above- and below-ground biomass, ANPP, and TNPP values for several sites have been corrected to agree with primary published sources and related data sets. The temporal coverage for both has been corrected to agree with primary published sources. Please see the Data Set Revision section of this document for detailed information.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Boreal Forest: Consistent Worldwide Site Estimates, 1965-1995, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F611",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F611",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/boreal_forest/NPP_BOREAL/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/boreal_forest/NPP_BOREAL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BOREAL.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BOREAL.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/611",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/611",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/boreal_forest/NPP_BOREAL/comp/NPP_BOREAL.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/boreal_forest/NPP_BOREAL/comp/NPP_BOREAL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+            "identifier": "C2751948194-ORNL_CLOUD",
+            "issued": "2021-12-06",
+            "keyword": [
+                "vegetation",
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/611",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-148.25 -47.5 128.27 66.37",
+            "temporal": "1965-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Boreal Forest: Consistent Worldwide Site Estimates, 1965-1995, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/yw48-ec8a",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Whole seedlings of wild type (4d) and atm mutants (4d) have been analyzed after a gamma ray irradiation of 0.75h 1.5h 3h & 5h (time course). Roots of wt (4d) atm (3d) and atr (4d) mutants have been analyzed after a 1h irradiation. Ataxia Telangiectasia Mutated (ATM) encodes a large protein with a phosphatidylinositol 3-kinase (PI3K)-like domain at the C terminus (reviewed by Rotman and Shiloh 1998). PI3K-related proteins make up a large family of Ser-Thr protein kinases numerous members of which are involved in the regulation of cell cycle progression responses to DNA damage and the maintenance of genomic stability (Hoekstra 1997). AtATM plays an essential role in meiosis and in the somatic response to DNA damage in plants similar to the function of ATM in mammals and other eukaryotes. Ataxia telangiectasia-mutated and Rad3-related (ATR) plays a central role in cell-cycle regulation transmitting DNA damage signals to downstream effectors of cell-cycle progression.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-329",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of atm mutant adm mutant and wild type whole plants and roots of Arabidopsis after gamma ray irradiation in a time series"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-329_yw48-ec8a",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "time",
                 "nucleic acid hybridization",
@@ -1710350,106 +1710364,71 @@
                 "p-mexp-27469",
                 "growth protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/yw48-ec8a",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-329_yw48-ec8a",
-            "description": "Whole seedlings of wild type (4d) and atm mutants (4d) have been analyzed after a gamma ray irradiation of 0.75h 1.5h 3h & 5h (time course). Roots of wt (4d) atm (3d) and atr (4d) mutants have been analyzed after a 1h irradiation. Ataxia Telangiectasia Mutated (ATM) encodes a large protein with a phosphatidylinositol 3-kinase (PI3K)-like domain at the C terminus (reviewed by Rotman and Shiloh 1998). PI3K-related proteins make up a large family of Ser-Thr protein kinases numerous members of which are involved in the regulation of cell cycle progression responses to DNA damage and the maintenance of genomic stability (Hoekstra 1997). AtATM plays an essential role in meiosis and in the somatic response to DNA damage in plants similar to the function of ATM in mammals and other eukaryotes. Ataxia telangiectasia-mutated and Rad3-related (ATR) plays a central role in cell-cycle regulation transmitting DNA damage signals to downstream effectors of cell-cycle progression.",
-            "title": "Transcription profiling of atm mutant adm mutant and wild type whole plants and roots of Arabidopsis after gamma ray irradiation in a time series",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-329",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of atm mutant adm mutant and wild type whole plants and roots of Arabidopsis after gamma ray irradiation in a time series"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of atm mutant adm mutant and wild type whole plants and roots of Arabidopsis after gamma ray irradiation in a time series"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-MAG-4-SUMM-GASPRA-SUMMARY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "galileo",
-                "gaspra"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Orbiter Magnetometer (MAG) calibrated averaged data from the Gaspra flyby in RTN coordinates. These data cover the interval 1991-10-29 06:03 to 1991-10-30 02:51.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-mag-4-summ-gaspra-summary-v1.0_yw79-fset",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "gaspra"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-MAG-4-SUMM-GASPRA-SUMMARY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-mag-4-summ-gaspra-summary-v1.0_yw79-fset",
-            "description": "Galileo Orbiter Magnetometer (MAG) calibrated averaged data from the Gaspra flyby in RTN coordinates. These data cover the interval 1991-10-29 06:03 to 1991-10-30 02:51.",
-            "title": "GALILEO ORBITER A MAG SUMM GASPRA SUMMARY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO ORBITER A MAG SUMM GASPRA SUMMARY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://pds.jpl.nasa.gov/"
-            ],
-            "keyword": [
-                "dictionary",
-                "data",
-                "index",
-                "pds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-547",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r82)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1710457,268 +1710436,269 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-547",
+            "issued": "2018-06-25",
+            "keyword": [
+                "dictionary",
+                "data",
+                "index",
+                "pds"
+            ],
+            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "https://pds.jpl.nasa.gov/"
+            ],
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PDS Data Dictionary (1r82)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/NGSARJ2J4XZQ",
             "citation": "NASA/GSFC. 2021-08-02. EXP7L1TRTALL. Version 001. Explorer-7 Thermal Radiation Experiment Temperature Values from All Sensors V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/NGSARJ2J4XZQ. https://disc.gsfc.nasa.gov/datacollection/EXP7L1TRTALL_001.html. Digital Science Data.",
-            "issued": "2014-09-24",
-            "temporal": "1959-10-19T00:00:00Z/1960-06-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-22",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2099719148-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Explorer-7 Thermal Radiation Experiment Temperature Values from All Sensors product contains temperature readings from all five bolometers in order to measure solar, reflected and terrestrial radiation. There are two files for the entire mission (Oct. 19, 1959 to April 16, 1960 and April 16, 1960 to June 4, 1960. Note there is no geolocation information included with these data. The data were originally written on IBM 7094 machines on magnetic tapes. The data have been restored and are archived in their original IBM 36-bit word binary format.\n\nThe Explorer-7 satellite was successfully launched on October 13, 1959. The radius of the circle of coverage was about 23 deg (~2500 km) at perigee and 31.5 deg (~3500 km) at apogee. Half the radiation is received from an area below the satellite with a radius of 5.3 deg (545 km) at perigee and 9 deg (~1015 km) at apogee. The Thermal Radiation Experiment successfully returned the first set of Earth looking data from space. The instrument was operational from launch until Feb. 28, 1961.\n\nThe Principal Investigator for these data was Verner E. Suomi from the University of Wisconsin. This product was previously available from the NSSDC with the identifier ESAD-00249 (old ID 59-009A-01B).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "EXP7L1TRTALL",
-            "creator": "NASA/GSFC",
-            "title": "Explorer-7 Thermal Radiation Experiment Temperature Values from All Sensors V001 (EXP7L1TRTALL) at GES DISC",
-            "graphic-preview-description": "Image of the Explorer-7 satellite.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EXP7L1TRTALL_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNGSARJ2J4XZQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNGSARJ2J4XZQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EXP7L1TRTALL_Sample.png",
-                    "description": "Image of the Explorer-7 satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "Image of the Explorer-7 satellite.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EXP7L1TRTALL_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Explorer/EXP7L1TRTALL.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Explorer/EXP7L1TRTALL.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=EXP7L1TRTALL",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=EXP7L1TRTALL",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Explorer/EXP7L1TRTALL.001/doc/README.EXP7L1TRT.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Explorer/EXP7L1TRTALL.001/doc/README.EXP7L1TRT.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataSetCatalog_2_Explorer7.pdf",
-                    "description": "Explorer VII Thermal Radiation Experiment Users' Note and Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Explorer VII Thermal Radiation Experiment Users' Note and Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataSetCatalog_2_Explorer7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Explorer7/Explorer7_Inventory.xlsx",
-                    "description": "Explorer Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "Explorer Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Explorer7/Explorer7_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Image of the Explorer-7 satellite.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EXP7L1TRTALL_Sample.png",
+            "identifier": "C2099719148-GES_DISC",
+            "issued": "2014-09-24",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NGSARJ2J4XZQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "EXP7L1TRTALL",
             "spatial": "-180.0 -81.5 180.0 81.5",
+            "temporal": "1959-10-19T00:00:00Z/1960-06-04T23:59:59.999Z",
             "theme": [
                 "EOSDIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Explorer-7 Thermal Radiation Experiment Temperature Values from All Sensors V001 (EXP7L1TRTALL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/I8VVYNAZP887",
             "citation": "Nadia Smith. 2019-01-15. SNDRAQIML2PLEVCPS. Version 2.1. Sounder SIPS: AQUA AIRS IR + MW Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/I8VVYNAZP887. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML2PLEVCPS_2.1.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-25",
-            "references": [
-                "https://doi.org/DOI  10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "atmospheric temperature",
-                "oceans",
-                "ocean temperature",
-                "surface thermal properties",
-                "altitude",
-                "air quality",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Nadia Smith",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2791404157-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the AIRS (Atmospheric Infrared Sounder)/AMSU (Advanced Microwave Sounding Unit) instruments aboard the Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. This file contains the fixed Pressure Level product (PLEV) variables derived from the CLIMCAPS algorithm using data. They include including gas mixing ratio profiles, column totals, surface values, tropopause properties, and relative humidity, together with per-field quality flagging. The profiles are specified at the surface and layer boundaries and are estimated from layer amounts using the L2 algorithm\n\nAn AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day. \n\nThe CLIMCAPS algorithm uses data from the second Modern-Era Retrospective analysis for Research and Applications (MERRA-2) as a first-guess for the atmospheric state.  Because MERRA-2 products typically have a latency from 3 to 7 weeks, so too do the CLIMCAPS products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIML2PLEVCPS",
-            "creator": "Nadia Smith",
-            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
-            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRAQIML2PLEVCPS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2PLEVCPS_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FI8VVYNAZP887",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FI8VVYNAZP887",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2PLEVCPS_2.1.png",
-                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2PLEVCPS_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML2PLEVCPS.2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML2PLEVCPS.2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIML2PLEVCPS.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIML2PLEVCPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIML2PLEVCPS.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIML2PLEVCPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML2PLEVCPS+2.1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML2PLEVCPS+2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
-                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
-                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
                     "@type": "dcat:Distribution",
+                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
-                    "description": "CLIMCAPS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2PLEVCPS_2.1.png",
+            "identifier": "C2791404157-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "atmospheric temperature",
+                "oceans",
+                "ocean temperature",
+                "surface thermal properties",
+                "altitude",
+                "air quality",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/I8VVYNAZP887",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/DOI  10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIML2PLEVCPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRAQIML2PLEVCPS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/aim",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/aim"
-            ],
-            "keyword": [
-                "spacecraft",
-                "satellite",
-                "3d model"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Meaney",
                 "hasEmail": "mailto:christopher.r.meaney@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-305",
             "description": "AIM is a two-year mission to study Polar Mesospheric Clouds (PMCs), the Earth's highest clouds, which form an icy membrane 50 miles (80.4 km) above the surface at the edge of space.",
-            "title": "NASA 3D Models: Aeronomy of Ice",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1710726,567 +1710706,565 @@
                     "mediaType": "image/x-lwo"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-305",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spacecraft",
+                "satellite",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/aim",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/aim"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Aeronomy of Ice"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0759-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-08T12:27:55.000 to 2015-05-08T14:29:32.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0759-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0759-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0759-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-08T12:27:55.000 to 2015-05-08T14:29:32.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0759 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0759 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1A.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. 2001-04-30. AST_L1A.003. ASTER Level 1A Data Set - Reconstructed, unprocessed instrument data. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/ASTER/AST_L1A.003. https://doi.org/10.5067/ASTER/AST_L1A.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2002-03-14",
-            "temporal": "2000-03-04T20:34:04Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-30",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "national geospatial data asset",
-                "ngda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C14758250-LPDAAC_ECS",
-            "description": "The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Level 1A (AST_L1A) contains reconstructed, instrument digital numbers (DNs) derived from the acquired telemetry streams of the telescopes: Visible and Near Infrared (VNIR), Shortwave Infrared (SWIR), and Thermal Infrared (TIR). Additionally, geometric correction coefficients and radiometric calibration coefficients are calculated and appended to the metadata, but not applied.\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.",
-            "series-name": "AST_L1A.003",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER L1A Reconstructed Unprocessed Instrument Data V003",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_032_012.1.TIR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Level 1A (AST_L1A) contains reconstructed, instrument digital numbers (DNs) derived from the acquired telemetry streams of the telescopes: Visible and Near Infrared (VNIR), Shortwave Infrared (SWIR), and Thermal Infrared (TIR). Additionally, geometric correction coefficients and radiometric calibration coefficients are calculated and appended to the metadata, but not applied.\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1A.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1A.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1A.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1A.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://asterweb.jpl.nasa.gov/",
-                    "description": "  The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.      ",
                     "@type": "dcat:Distribution",
+                    "description": "  The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.      ",
+                    "downloadURL": "http://asterweb.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C14758250-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C14758250-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/69/AST_L1_User_Guide_V3.pdf",
-                    "description": "ASTER Level-1 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Level-1 User Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/69/AST_L1_User_Guide_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/175/ASTER_L1_Product_Specifications.pdf",
-                    "description": "The ASTER Level-1 Products Specification provides a description of the data file.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER Level-1 Products Specification provides a description of the data file.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/175/ASTER_L1_Product_Specifications.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_032_012.1.TIR.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_032_012.1.TIR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1010/ASTER_User_Handbook_v3.pdf",
-                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1010/ASTER_User_Handbook_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_032_012.1.TIR.jpg",
+            "identifier": "C14758250-LPDAAC_ECS",
+            "issued": "2002-03-14",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1A.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "series-name": "AST_L1A.003",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-04T20:34:04Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER L1A Reconstructed Unprocessed Instrument Data V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10886",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://techport.nasa.gov/home",
-                "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
-                "http://techport.nasa.gov/fetchFile?objectId=6561",
-                "http://techport.nasa.gov/fetchFile?objectId=3456",
-                "http://techport.nasa.gov/fetchFile?objectId=3447",
-                "http://techport.nasa.gov/fetchFile?objectId=6584",
-                "http://techport.nasa.gov/fetchFile?objectId=6560",
-                "http://techport.nasa.gov/fetchFile?objectId=3448"
-            ],
-            "keyword": [
-                "active",
-                "project"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bruce Woodgate",
                 "hasEmail": "mailto:bruce.e.woodgate@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10886",
             "description": "We propose to continue our program of emission line astronomy featuring three areas of emphasis: 1) The distribution and nature of high redshift emission line galaxies, using the Lyman alpha and other rest-frame UV lines; and the study of planetary systems in formation in the first 10 Myrs, with the interplay of circumstellar disks and jets; and spectral differencing of transiting planets. 2) We are extending the capability of our Goddard Fabry-Perot Imager by incorporating a Coronagraphic Integral Field Spectrograph (CIFS), and will continue our observations with the improved instrument. We request support for completing the commissioning of the instrument, and for its maintenance and operation. The CIFS, which has been delivered to the Apache Point Observatory's 3.5-m telescope, consists of a custom microlens array and magnifier section, a grating wheel assembly, and a photon-counting electron-multiplying CCD (EMCCD), within the optical train of the Fabry-Perot. The instrument is switchable between Fabry-Perot and IFS modes. It provides observational support to interpret data from the HST, Spitzer, Chandra, Herschel and soon JWST space observatories with capabilities not available on them, and will be used to develop technology for future NASA flight programs such as WFIRST, and NWO, THEIA, ATLAST and other planet-finding missions. In this period we propose to extend the wavelength coverage of the CIFS, by extending the format of the EMCCD.",
-            "title": "Emission Line Astronomy - Coronagraphic Tunable Narrow Band Imaging and Integral Field Spectroscopy. Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10886",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10886",
+            "issued": "2010-01-01",
+            "keyword": [
+                "active",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10886",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Science Mission Directorate"
+            },
+            "references": [
+                "http://techport.nasa.gov/home",
+                "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
+                "http://techport.nasa.gov/fetchFile?objectId=6561",
+                "http://techport.nasa.gov/fetchFile?objectId=3456",
+                "http://techport.nasa.gov/fetchFile?objectId=3447",
+                "http://techport.nasa.gov/fetchFile?objectId=6584",
+                "http://techport.nasa.gov/fetchFile?objectId=6560",
+                "http://techport.nasa.gov/fetchFile?objectId=3448"
+            ],
+            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
+            "title": "Emission Line Astronomy - Coronagraphic Tunable Narrow Band Imaging and Integral Field Spectroscopy. Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PGZVDAVFWVYQ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX12 PALS Soil Moisture Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/PGZVDAVFWVYQ.",
-            "issued": "2012-06-12",
-            "temporal": "2012-06-12T00:00:00Z/2012-07-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-07-19",
-            "keyword": [
-                "vegetation",
-                "spectral/engineering",
-                "land use/land cover",
-                "soils",
-                "microwave",
-                "earth science",
-                "land surface",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSIDC Services",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1387182865-NSIDC_ECS",
             "description": "This data set contains soil moisture data obtained by the Passive Active L-band System  (PALS) aircraft instrument. The data were collected as part of SMAPVEX12, the Soil Moisture Active Passive Validation Experiment 2012.",
-            "title": "SMAPVEX12 PALS Soil Moisture Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPGZVDAVFWVYQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPGZVDAVFWVYQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV12PLSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV12PLSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1387182865-NSIDC_ECS&m=43.48828125%21-97.400390625%214%211%210%210%2C2&q=SMAPVEX12&ok=SMAPVEX12",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1387182865-NSIDC_ECS&m=43.48828125%21-97.400390625%214%211%210%210%2C2&q=SMAPVEX12&ok=SMAPVEX12",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV12PLSM/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV12PLSM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PGZVDAVFWVYQ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/PGZVDAVFWVYQ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PGZVDAVFWVYQ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/PGZVDAVFWVYQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1387182865-NSIDC_ECS",
+            "issued": "2012-06-12",
+            "keyword": [
+                "vegetation",
+                "spectral/engineering",
+                "land use/land cover",
+                "soils",
+                "microwave",
+                "earth science",
+                "land surface",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/PGZVDAVFWVYQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.51 49.44 -97.85 49.96",
+            "temporal": "2012-06-12T00:00:00Z/2012-07-19T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX12 PALS Soil Moisture Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MODSA-MO9N9",
             "citation": "NASA OBPG. 2020-01-15. MODIS Aqua Level 3 SST Thermal IR Monthly 9km Nighttime. Version 2019.0. MODIS Aqua Global Level 3 Mapped SST. OBPG, Goddard Space Flight Center  Greenbelt, MD,US. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/MODSA-MO9N9. https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html.",
-            "issued": "2019-12-14",
-            "temporal": "2002-07-03T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-14",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2015.04.023",
-                "https://doi.org/10.1175/JTECH-D-18-0103.1"
-            ],
-            "keyword": [
-                "oceans",
-                "national geospatial data asset",
-                "ngda",
-                "ocean temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036877952-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Aqua satellite.  Average daily, weekly (8 day), monthly and annual skin SST products at are available at both 4.63 and 9.26 km spatial resolution. Aqua was launched by NASA on May 4, 2002, into a sun synchronous, polar orbit with a daylight ascending node at 13:30, formation flying in the A-train with other Earth Observation Satellites (EOS), to study the global dynamics of the Earth atmosphere, land and oceans. MODIS captures data in 36 spectral bands at a variety of spatial resolutions.  Two SST products can be present in these files. The first is a skin SST produced for both day and night (NSST) observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity of SST derived from heritage and current NASA sensors. At night, a second SST product is generated using the mid-infrared 3.95 and 4.05 micron  wavelength channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be used at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) and Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS)  are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires MODIS ocean L3 SST data from the OBPG and is the official Physical Oceanography Data Archive (PO.DAAC) for SST.  The R2019.0 supersedes the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODSA-MO9N4",
-            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
-            "series-name": "MODIS Aqua Level 3 SST Thermal IR Monthly 9km Nighttime",
             "creator": "NASA OBPG",
-            "title": "MODIS Aqua Level 3 SST Thermal IR Monthly 9km Nighttime V2019.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Aqua satellite.  Average daily, weekly (8 day), monthly and annual skin SST products at are available at both 4.63 and 9.26 km spatial resolution. Aqua was launched by NASA on May 4, 2002, into a sun synchronous, polar orbit with a daylight ascending node at 13:30, formation flying in the A-train with other Earth Observation Satellites (EOS), to study the global dynamics of the Earth atmosphere, land and oceans. MODIS captures data in 36 spectral bands at a variety of spatial resolutions.  Two SST products can be present in these files. The first is a skin SST produced for both day and night (NSST) observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity of SST derived from heritage and current NASA sensors. At night, a second SST product is generated using the mid-infrared 3.95 and 4.05 micron  wavelength channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be used at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) and Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS)  are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires MODIS ocean L3 SST data from the OBPG and is the official Physical Oceanography Data Archive (PO.DAAC) for SST.  The R2019.0 supersedes the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODSA-MO9N4",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODSA-MO9N9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODSA-MO9N9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://oceancolor.gsfc.nasa.gov",
-                    "description": "Ocean Biology Processing Group homepage",
                     "@type": "dcat:Distribution",
+                    "description": "Ocean Biology Processing Group homepage",
+                    "downloadURL": "http://oceancolor.gsfc.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/modis/open/L3/docs/modis_sst.html",
-                    "description": "describes all the level 3 MODIS data",
                     "@type": "dcat:Distribution",
+                    "description": "describes all the level 3 MODIS data",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/modis/open/L3/docs/modis_sst.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic Data Readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic Data Readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
-                    "description": "OBPG SST Reprocessing v2019.0 summary",
                     "@type": "dcat:Distribution",
+                    "description": "OBPG SST Reprocessing v2019.0 summary",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "Additional resource to help better understand the algorithm(s) used in producing and/or calibrating/validating the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "Additional resource to help better understand the algorithm(s) used in producing and/or calibrating/validating the dataset",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
-                    "description": "Data Use and Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "Data Use and Citation Policy",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877952-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877952-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877952-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877952-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0.jpg",
+            "identifier": "C2036877952-POCLOUD",
+            "issued": "2019-12-14",
+            "keyword": [
+                "oceans",
+                "national geospatial data asset",
+                "ngda",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODSA-MO9N9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2015.04.023",
+                "https://doi.org/10.1175/JTECH-D-18-0103.1"
+            ],
+            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
+            "series-name": "MODIS Aqua Level 3 SST Thermal IR Monthly 9km Nighttime",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-03T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "EOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Aqua Level 3 SST Thermal IR Monthly 9km Nighttime V2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2024",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hmimina, G., R. Yu, R. Wang, K.F. Huemmrich, and J.A. Gamon. 2022. ABoVE: Light-Curve Modelling of Gridded GPP Using MODIS MAIAC and Flux Tower Data. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2024",
-            "issued": "2022-09-14",
-            "temporal": "2000-01-01T00:00:00Z/2018-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "national geospatial data asset",
-                "land use/land cover",
-                "ngda",
-                "land surface",
-                "ecological dynamics",
-                "earth science",
-                "soils",
-                "climate indicators",
-                "carbon flux",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2445456434-ORNL_CLOUD",
             "description": "This dataset contains gridded estimations of daily ecosystem Gross Primary Production (GPP) in grams of carbon per day at a 1 km2 spatial resolution over Alaska and Canada from 2000-01-01 to 2018-01-01. Daily estimates of GPP were derived from a light-curve model that was fitted and validated over a network of ABoVE domain Ameriflux flux towers then upscaled using MODIS Multi-Angle Implementation of Atmospheric Correction (MAIAC) data to span the extended ABoVE domain. In general, the methods involved three steps; the first step involved collecting and processing mainly carbon-flux site-level data, the second step involved the analysis and correction of site-level MAIAC data, and the final step developed a framework to produce large-scale estimates of GPP. The light-curve parameter model was generated by upscaling from flux tower sub-daily temporal resolution by deconvolving the GPP variable into 3 components: the absorbed photosynthetically active radiation (aPAR), the maximum GPP or maximum photosynthetic capacity (GPPmax), and the photosynthetic limitation or amount of light needed to reach maximum capacity (PPFDmax). GPPmax and PPFDmax were related to satellite reflectance measurements sampled at the daily scale. GPP over the extended ABoVE domain was estimated at a daily resolution from the light-curve parameter model using MODIS MAIAC daily reflectance as input. This framework allows large-scale estimates of phenology and evaluation of ecosystem sensitivity to climate change.",
-            "graphic-preview-description": "Average daily GPP for 2000-2017 in units of grams of carbon per square meter per day.",
-            "title": "ABoVE: Light-Curve Modelling of Gridded GPP Using MODIS MAIAC and Flux Tower Data",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/GPP_MODIS_Alaska_Canada_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2024",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2024",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/GPP_MODIS_Alaska_Canada/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/GPP_MODIS_Alaska_Canada/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/GPP_MODIS_Alaska_Canada.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/GPP_MODIS_Alaska_Canada.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2024",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2024",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/GPP_MODIS_Alaska_Canada/comp/GPP_MODIS_Alaska_Canada.pdf",
-                    "description": "ABoVE: Light-Curve Modelling of Gridded GPP Using MODIS MAIAC and Flux Tower Data: GPP_MODIS_Alaska_Canada.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Light-Curve Modelling of Gridded GPP Using MODIS MAIAC and Flux Tower Data: GPP_MODIS_Alaska_Canada.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/GPP_MODIS_Alaska_Canada/comp/GPP_MODIS_Alaska_Canada.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/GPP_MODIS_Alaska_Canada/comp/MAIAC_GPP_ATBD.pdf",
-                    "description": "ABoVE: Light-Curve Modelling of Gridded GPP Using MODIS MAIAC and Flux Tower Data: MAIAC_GPP_ATBD.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Light-Curve Modelling of Gridded GPP Using MODIS MAIAC and Flux Tower Data: MAIAC_GPP_ATBD.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/GPP_MODIS_Alaska_Canada/comp/MAIAC_GPP_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/GPP_MODIS_Alaska_Canada_Fig1.png",
-                    "description": "Average daily GPP for 2000-2017 in units of grams of carbon per square meter per day.",
                     "@type": "dcat:Distribution",
+                    "description": "Average daily GPP for 2000-2017 in units of grams of carbon per square meter per day.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/GPP_MODIS_Alaska_Canada_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://above.nasa.gov",
-                    "description": "ABoVE project site",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE project site",
+                    "downloadURL": "https://above.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Average daily GPP for 2000-2017 in units of grams of carbon per square meter per day.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/GPP_MODIS_Alaska_Canada_Fig1.png",
+            "identifier": "C2445456434-ORNL_CLOUD",
+            "issued": "2022-09-14",
+            "keyword": [
+                "biosphere",
+                "national geospatial data asset",
+                "land use/land cover",
+                "ngda",
+                "land surface",
+                "ecological dynamics",
+                "earth science",
+                "soils",
+                "climate indicators",
+                "carbon flux",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2024",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-172.08 50.06 -73.64 79.75",
+            "temporal": "2000-01-01T00:00:00Z/2018-01-01T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Light-Curve Modelling of Gridded GPP Using MODIS MAIAC and Flux Tower Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://curator.jsc.nasa.gov/lunar/catalogs/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://curator.jsc.nasa.gov/lunar/catalogs/apollo14catalog.cfm"
-            ],
-            "keyword": [
-                "catalog",
-                "jsc",
-                "sample",
-                "apollo",
-                "lunar"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carlton Allen",
                 "hasEmail": "mailto:carlton.c.allen@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-877__2",
             "description": "Apollo 16 Sample Catalog by Graham Ryder and Marc D. Norman",
-            "title": "Apollo 16 Sample Catalog",
-            "programCode": [
-                "026:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1711294,231 +1711272,253 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-877__2",
+            "issued": "2018-06-25",
+            "keyword": [
+                "catalog",
+                "jsc",
+                "sample",
+                "apollo",
+                "lunar"
+            ],
+            "landingPage": "http://curator.jsc.nasa.gov/lunar/catalogs/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://curator.jsc.nasa.gov/lunar/catalogs/apollo14catalog.cfm"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Apollo 16 Sample Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/HNA0RBAECQ9L",
             "citation": "Nadia Smith. 2019-01-15. SNDRSNIML2PLEVCPS. Version 2.1. Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/HNA0RBAECQ9L. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2PLEVCPS_2.1.html. Digital Science Data.",
-            "issued": "2015-11-02",
-            "temporal": "2015-11-02T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://doi.org/DOI  10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "air quality",
-                "earth science",
-                "altitude",
-                "atmosphere",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Nadia Smith",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2791415461-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). This file contains the fixed Pressure Level product (PLEV) variables derived from the CLIMCAPS algorithm using full spectral resolution inputs. They include including gas mixing ratio profiles, column totals, surface values, tropopause properties, and relative humidity, together with per-field quality flagging. The profiles are specified at the surface and layer boundaries and are estimated from layer amounts using the L2 algorithm\n\nAn level 2 granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day. \n\nThe CLIMCAPS algorithm uses data from the second Modern-Era Retrospective analysis for Research and Applications (MERRA-2) as a first-guess for the atmospheric state.  Because MERRA-2 products typically have a latency from 3 to 7 weeks, so too do the CLIMCAPS products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML2PLEVCPS",
-            "creator": "Nadia Smith",
-            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRSNIML2PLEVCPS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPS_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHNA0RBAECQ9L",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHNA0RBAECQ9L",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPS_2.1.png",
-                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPS_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2PLEVCPS_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2PLEVCPS_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPS.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPS.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2PLEVCPS+2.1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2PLEVCPS+2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
-                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
-                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
                     "@type": "dcat:Distribution",
+                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
-                    "description": "CLIMCAPS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPS_2.1.png",
+            "identifier": "C2791415461-GES_DISC",
+            "issued": "2015-11-02",
+            "keyword": [
+                "atmospheric water vapor",
+                "air quality",
+                "earth science",
+                "altitude",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/HNA0RBAECQ9L",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/DOI  10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRSNIML2PLEVCPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-11-02T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRSNIML2PLEVCPS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-POS-6-GASPRA-FLYBY-TRAJ-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "galileo",
-                "gaspra"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Orbiter 60 second sampled trajectory data from the Gaspra flyby in Gaspra-centric Solar Ecliptic (GaSE) and RTN coordinates. These data cover the interval 1991-10-29T06:00 to 1991-10-31 00:00.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pos-6-gaspra-flyby-traj-v1.0_ywka-2e6a",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "gaspra"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-POS-6-GASPRA-FLYBY-TRAJ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pos-6-gaspra-flyby-traj-v1.0_ywka-2e6a",
-            "description": "Galileo Orbiter 60 second sampled trajectory data from the Gaspra flyby in Gaspra-centric Solar Ecliptic (GaSE) and RTN coordinates. These data cover the interval 1991-10-29T06:00 to 1991-10-31 00:00.",
-            "title": "GALILEO ORBITER A POS GASPRA FLYBY TRAJ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO ORBITER A POS GASPRA FLYBY TRAJ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805835-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2024-07-19",
-            "temporal": "2017-11-29T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "ocean temperature",
-                "earth science",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C3166805835-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-20 VIIRS Level-3 Global Binned 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version 2024.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/reprocessing/",
-                    "description": "NASA Ocean Color Web - Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/reprocessing/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/how-to-cite/",
-                    "description": "NASA Ocean Color Web - Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Citation Policy",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/how-to-cite/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 }
             ],
+            "identifier": "C3166805835-OB_DAAC",
+            "issued": "2024-07-19",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805835-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-11-29T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-20 VIIRS Level-3 Global Binned 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version 2024.0"
         }
-    ]
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

