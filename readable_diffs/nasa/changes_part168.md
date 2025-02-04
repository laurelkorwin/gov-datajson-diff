# Change History for nasa.json (Part 168)

### Changes from 31606f9 to dd2190f (Part 157/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                "hasEmail": "mailto:linda.j.connell@nasa.gov"
+            },
+            "description": "A sampling of reports concerning Emergency Medical Service (EMS) incidents.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://asrs.arc.nasa.gov/docs/rpsts/ems.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-810",
+            "issued": "2018-06-25",
             "keyword": [
                 "service",
                 "medical",
@@ -1656847,204 +1656856,209 @@
                 "emergency",
                 "aviation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Linda J. Connell",
-                "hasEmail": "mailto:linda.j.connell@nasa.gov"
-            },
+            "landingPage": "http://asrs.arc.nasa.gov/search/reportsets.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:021"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-810",
-            "description": "A sampling of reports concerning Emergency Medical Service (EMS) incidents.",
-            "title": "Aviation Safety Reporting System: Emergency Medical Service Incidents",
-            "programCode": [
-                "026:021"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://asrs.arc.nasa.gov/docs/rpsts/ems.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://asrs.arc.nasa.gov/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Aviation Safety Reporting System: Emergency Medical Service Incidents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_Ground_InSitu_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-07-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/FIREXAQ_Ground_InSitu_Data_1.",
-            "issued": "2020-04-07",
-            "temporal": "2019-08-07T00:00:00Z/2019-08-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-15",
-            "keyword": [
-                "aerosols",
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Crawford",
                 "hasEmail": "mailto:james.h.crawford@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1917874435-LARC_ASDC",
             "description": "FIREXAQ_Ground_InSitu_Data are in-situ ground measurements collected during FIREX-AQ. Data collection for this product is complete.\r\n\r\nCompleted during summer 2019, FIREX-AQ utilized a combination of instrumented airplanes, satellites, and ground-based instrumentation. Detailed fire plume sampling was carried out by the NASA DC-8 aircraft, which had a comprehensive instrument payload capable of measuring over 200 trace gas species, as well as aerosol microphysical, optical, and chemical properties. The DC-8 aircraft completed 23 science flights, including 15 flights from Boise, Idaho and 8 flights from Salina, Kansas. NASA\u2019s ER-2 completed 11 flights, partially in support of the FIREX-AQ effort. The ER-2 payload was made up of 8 satellite analog instruments and provided critical fire information, including fire temperature, fire plume heights, and vegetation/soil albedo information. NOAA provided the NOAA-CHEM Twin Otter and the NOAA-MET Twin Otter aircraft to measure chemical processing in the lofted plumes of Western wildfires. The NOAA-CHEM Twin Otter focused on nighttime plume chemistry, from which data is archived at the NASA Atmospheric Science Data Center (ASDC). The NOAA-MET Twin Otter collected measurements of air movements at fire boundaries with the goal of understanding the local weather impacts of fires and the movement patterns of fires. NOAA-MET Twin Otter data will be archived at the ASDC in the future. Additionally, a ground-based station in McCall, Idaho and several mobile laboratories provided in-situ measurements of aerosol microphysical and optical properties, aerosol chemical compositions, and trace gas species. \r\n\r\nThe Fire Influence on Regional to Global Environments and Air Quality (FIREX-AQ) campaign was a NOAA/NASA interagency intensive study of North American fires to gain an understanding on the integrated impact of the fire emissions on the tropospheric chemistry and composition and to assess the satellite\u2019s capability for detecting fires and estimating fire emissions. The overarching goal of FIREX-AQ was to provide measurements of trace gas and aerosol emissions for wildfires and prescribed fires in great detail, relate them to fuel and fire conditions at the point of emission, characterize the conditions relating to plume rise, and follow plumes downwind to understand chemical transformation and air quality impacts.",
-            "title": "FIREX-AQ In-Situ Ground Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_Ground_InSitu_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_Ground_InSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/firex-aq/",
-                    "description": "ESPO home page for FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for FIREX-AQ",
+                    "downloadURL": "https://espo.nasa.gov/firex-aq/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_Ground_InSitu_Data_1",
-                    "description": "DOI data set landing page for FIREXAQ_Ground_InSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIREXAQ_Ground_InSitu_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_Ground_InSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917874435-LARC_ASDC",
-                    "description": "Earthdata Search for FIREXAQ_Ground_InSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIREXAQ_Ground_InSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917874435-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://esrl.noaa.gov/csl/projects/firex-aq/",
-                    "description": "NOAA Chemical Sciences Laboratory (CSL) Overview of FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA Chemical Sciences Laboratory (CSL) Overview of FIREX-AQ",
+                    "downloadURL": "https://esrl.noaa.gov/csl/projects/firex-aq/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/whitepaper.pdf",
-                    "description": "FIREX-AQ Mission Overview/White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "FIREX-AQ Mission Overview/White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/whitepaper.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/DMT_FIREXAQ_v02.pptx",
-                    "description": "Data Management Plan for FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Management Plan for FIREX-AQ",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/DMT_FIREXAQ_v02.pptx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/FIREX-AQ_ER-2_Instrument_data_archive_pointer.docx",
-                    "description": "ER-2 instrument suite for the Summer 2019 FIREX-AQ field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "ER-2 instrument suite for the Summer 2019 FIREX-AQ field campaign",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/docs/FIREX-AQ_ER-2_Instrument_data_archive_pointer.docx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/",
-                    "description": "FIREX-AQ Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "FIREX-AQ Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/firex-aq/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/30/plumes-go-the-distance/",
-                    "description": "NASA Earth Expeditions Article \u201cPlumes Go The Distance\u201d (July 30, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions Article \u201cPlumes Go The Distance\u201d (July 30, 2019)",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/30/plumes-go-the-distance/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/145494/sampling-the-castle-fire/",
-                    "description": "NASA Earth Observatory Article \u201cSampling the Castle Fire\u201d (August 13, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article \u201cSampling the Castle Fire\u201d (August 13, 2019)",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/145494/sampling-the-castle-fire/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/145446/flying-through-a-fire-cloud/",
-                    "description": "NASA Earth Observatory Article \u201cFlying through a Fire Cloud\u201d (August 7, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article \u201cFlying through a Fire Cloud\u201d (August 7, 2019)",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/145446/flying-through-a-fire-cloud/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/29/fire-weather-pyro-weather/",
-                    "description": "NASA Earth Expeditions Article \u201cFire Weather, Pyro Weather\u201d (July 29, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions Article \u201cFire Weather, Pyro Weather\u201d (July 29, 2019)",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/2019/07/29/fire-weather-pyro-weather/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/FIREXAQ/2019",
-                    "description": "FIREX-AQ Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "FIREX-AQ Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/FIREXAQ/2019",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aeronet.gsfc.nasa.gov/new_web/DRAGON-FIREX-AQ_2019.html",
-                    "description": "AERONET Data for FIREX-AQ",
                     "@type": "dcat:Distribution",
+                    "description": "AERONET Data for FIREX-AQ",
+                    "downloadURL": "https://aeronet.gsfc.nasa.gov/new_web/DRAGON-FIREX-AQ_2019.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/Ground_InSitu_Data_1/",
-                    "description": "ASDC Direct Data Download for FIREXAQ_Ground_InSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIREXAQ_Ground_InSitu_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/Ground_InSitu_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1917874435-LARC_ASDC",
+            "issued": "2020-04-07",
+            "keyword": [
+                "aerosols",
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_Ground_InSitu_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>15.0 -135.0 15.0 -75.0 60.0 -75.0 60.0 -135.0 15.0 -135.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-08-07T00:00:00Z/2019-08-10T23:59:59.999Z",
             "theme": [
                 "FIREX-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FIREX-AQ In-Situ Ground Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xx28-ywgh",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "In the   Rocket Science   citizen science project Eruca sativa (salad rocket) seeds stored for six months on board of the International Space Station caused delayed crop establishment. Here we investigated the physiological and molecular mechanisms underpinning the spaceflight effects on dry seeds. We found that   Space   seed germination vigor was reduced and aging sensitivity increased but the spaceflight did not compromise seed viability and the development of normal seedlings. Comparative analysis of the transcriptomes (using RNASeq) in dry seeds and upon controlled artificial aging treatment (CAAT) revealed differentially expressed genes (DEGs) associated with spaceflight and ageing. DEG categories enriched by spaceflight and CAAT included transcription and translation with reduced transcript abundances for 40S and 60S ribosomal subunit genes. Among the   spaceflight-up   DEGs were Heat Shock Protein (HSP) DNAJ-related chaperones a Heat Shock Factor (HSFA7a-like) and components of several DNA repair pathways (e.g. ATM DNA ligase1). The   response to radiation   category was especially enriched in   spaceflight-up   DEGs including HSPs catalases and the transcription factor HY5. The major finding from the physiological and transcriptome analysis is that spaceflight causes vigor loss and partial ageing during air-dry seed storage for which space environmental factors and consequences for seed storage during spaceflights are discussed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-301",
+                    "mediaType": "text/html",
+                    "title": "Eruca sativa Rocket Science RNA-seq"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-301_xx28-ywgh",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "nucleic acid sequencing",
@@ -1657054,175 +1657068,175 @@
                 "spaceflight",
                 "library construction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xx28-ywgh",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-301_xx28-ywgh",
-            "description": "In the   Rocket Science   citizen science project Eruca sativa (salad rocket) seeds stored for six months on board of the International Space Station caused delayed crop establishment. Here we investigated the physiological and molecular mechanisms underpinning the spaceflight effects on dry seeds. We found that   Space   seed germination vigor was reduced and aging sensitivity increased but the spaceflight did not compromise seed viability and the development of normal seedlings. Comparative analysis of the transcriptomes (using RNASeq) in dry seeds and upon controlled artificial aging treatment (CAAT) revealed differentially expressed genes (DEGs) associated with spaceflight and ageing. DEG categories enriched by spaceflight and CAAT included transcription and translation with reduced transcript abundances for 40S and 60S ribosomal subunit genes. Among the   spaceflight-up   DEGs were Heat Shock Protein (HSP) DNAJ-related chaperones a Heat Shock Factor (HSFA7a-like) and components of several DNA repair pathways (e.g. ATM DNA ligase1). The   response to radiation   category was especially enriched in   spaceflight-up   DEGs including HSPs catalases and the transcription factor HY5. The major finding from the physiological and transcriptome analysis is that spaceflight causes vigor loss and partial ageing during air-dry seed storage for which space environmental factors and consequences for seed storage during spaceflights are discussed.",
-            "title": "Eruca sativa Rocket Science RNA-seq",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-301",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Eruca sativa Rocket Science RNA-seq"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Eruca sativa Rocket Science RNA-seq"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2097",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lober, C., and J.V. Fayne. 2022. ABoVE: Bias-Corrected IMERG Monthly Precipitation for Alaska and Canada, 2000-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2097",
-            "issued": "2022-11-17",
-            "temporal": "2000-06-01T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C2550019170-ORNL_CLOUD",
             "description": "This dataset is a modification to the Integrated Multi-satellitE Retrievals for GPM (IMERG) Final Run microwave-only, daily precipitation Version 06 data. It provides bias-corrected IMERG monthly precipitation data for Alaska and Canada from June 2000 through December 2020 in Cloud-Optimized GeoTIFF (*.tif) format. Data are provided in the units of mm/day. NASA's IMERG data product is one of the most advanced satellite precipitation products with a 0.1-degree spatial resolution and near global coverage. This dataset bias-corrected IMERG's HQprecipitation precipitation estimates, which are based on passive microwave (PMW)-only retrievals, using a linear regression method. This method utilizes empirical measurements from rain gauge stations from the Global Historical Climatology Network (GHCN) and a digital elevation model. This bias correction approach improves estimates at elevations above 500 m a.s.l., which are typically underestimated.",
-            "graphic-preview-description": "Two examples of uncorrected and corrected months Canada-Alaska domain. The correction is applied to pixels > 500 m, so the correction is seen primarily in mountainous areas. Figure from Lober et al. (in review).",
-            "title": "ABoVE: Bias-Corrected IMERG Monthly Precipitation for Alaska and Canada, 2000-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/IMERG_Precip_Canada_Alaska_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2097",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2097",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/IMERG_Precip_Canada_Alaska/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/IMERG_Precip_Canada_Alaska/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/IMERG_Precip_Canada_Alaska.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/IMERG_Precip_Canada_Alaska.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2097",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2097",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/IMERG_Precip_Canada_Alaska/comp/IMERG_Precip_Canada_Alaska.pdf",
-                    "description": "ABoVE: Bias-Corrected IMERG Monthly Precipitation for Alaska and Canada, 2000-2020: IMERG_Precip_Canada_Alaska.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Bias-Corrected IMERG Monthly Precipitation for Alaska and Canada, 2000-2020: IMERG_Precip_Canada_Alaska.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/IMERG_Precip_Canada_Alaska/comp/IMERG_Precip_Canada_Alaska.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/IMERG_Precip_Canada_Alaska_Fig1.png",
-                    "description": "Two examples of uncorrected and corrected months Canada-Alaska domain. The correction is applied to pixels > 500 m, so the correction is seen primarily in mountainous areas. Figure from Lober et al. (in review).",
                     "@type": "dcat:Distribution",
+                    "description": "Two examples of uncorrected and corrected months Canada-Alaska domain. The correction is applied to pixels > 500 m, so the correction is seen primarily in mountainous areas. Figure from Lober et al. (in review).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/IMERG_Precip_Canada_Alaska_Fig1.png",
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
+            "graphic-preview-description": "Two examples of uncorrected and corrected months Canada-Alaska domain. The correction is applied to pixels > 500 m, so the correction is seen primarily in mountainous areas. Figure from Lober et al. (in review).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/IMERG_Precip_Canada_Alaska_Fig1.png",
+            "identifier": "C2550019170-ORNL_CLOUD",
+            "issued": "2022-11-17",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2097",
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
             "spatial": "-179.3 40.8 -48.5 72.0",
+            "temporal": "2000-06-01T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Bias-Corrected IMERG Monthly Precipitation for Alaska and Canada, 2000-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1211-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-25T10:48:15.000 to 2015-11-25T15:06:28.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1211-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1211-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1211-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-25T10:48:15.000 to 2015-11-25T15:06:28.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1211 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1211 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xx7s-2w3d",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "One of the most likely risks astronauts on long duration space missions face is exposure to ionizing radiation associated with highly energetic and charged heavy (HZE) particles. Since access to medical expertise on such a mission is limited at best early diagnosis and mitigation of such exposure is critical. In order to accurately determine the dosage within 1 hour post-exposure dose-dependent biomarkers are needed. Therefore we performed a dose-course transcriptional analysis for radiation exposure at 0 0.3 1.5 and 3.0 Gy with corresponding time point at 1 hour (hr) post-exposure using Affymetrix GeneChip Human Gene 1.0 ST v1 Array chips. The analysis of our data suggests a set of sensitive genetic biomarkers specific to each radiation level as well as generic radiation response biomarkers. Upregulated biomarkers can then be used within lab-on-a-chip (LOC) systems to detect exposure to ionizing radiation. A total of sixteen human samples representing radiation exposure at levels 0 Gy 0.3 Gy 1.5 Gy and 3.0 Gy at time point 1 hour (hr) post-exposure were constructed. Blood samples were extracted from four human volunteers and were irradiated. Leukocytes were extracted and gene expression was measured. Samples for all four volunteers were measured at 1 hr for all four dose levels resulting in four replicates at each dose level. Thus a total of 4 samples at each of the four radiation levels were sampled yielding the total of 16 samples.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-71",
+                    "mediaType": "text/html",
+                    "title": "Immediate Transcriptional Changes in Response to High Dose Radiation Exposure"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-71_xx7s-2w3d",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid hybridization",
                 "sample treatment protocol",
@@ -1657240,967 +1657254,955 @@
                 "p-gse64375-4",
                 "p-gse64375-5"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xx7s-2w3d",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-71_xx7s-2w3d",
-            "description": "One of the most likely risks astronauts on long duration space missions face is exposure to ionizing radiation associated with highly energetic and charged heavy (HZE) particles. Since access to medical expertise on such a mission is limited at best early diagnosis and mitigation of such exposure is critical. In order to accurately determine the dosage within 1 hour post-exposure dose-dependent biomarkers are needed. Therefore we performed a dose-course transcriptional analysis for radiation exposure at 0 0.3 1.5 and 3.0 Gy with corresponding time point at 1 hour (hr) post-exposure using Affymetrix GeneChip Human Gene 1.0 ST v1 Array chips. The analysis of our data suggests a set of sensitive genetic biomarkers specific to each radiation level as well as generic radiation response biomarkers. Upregulated biomarkers can then be used within lab-on-a-chip (LOC) systems to detect exposure to ionizing radiation. A total of sixteen human samples representing radiation exposure at levels 0 Gy 0.3 Gy 1.5 Gy and 3.0 Gy at time point 1 hour (hr) post-exposure were constructed. Blood samples were extracted from four human volunteers and were irradiated. Leukocytes were extracted and gene expression was measured. Samples for all four volunteers were measured at 1 hr for all four dose levels resulting in four replicates at each dose level. Thus a total of 4 samples at each of the four radiation levels were sampled yielding the total of 16 samples.",
-            "title": "Immediate Transcriptional Changes in Response to High Dose Radiation Exposure",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-71",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Immediate Transcriptional Changes in Response to High Dose Radiation Exposure"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Immediate Transcriptional Changes in Response to High Dose Radiation Exposure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M10-STR-REFL-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m10-str-refl-v1.0_xxa8-zr2t",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M10-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m10-str-refl-v1.0_xxa8-zr2t",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR-STR-REFL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-OCC-PROF-RTPD-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "magellan",
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes vertical profiles of refractivity, temperature, pressure and density in the neutral Venus atmosphere. The data set is composed of the following parameter fields (listed as the field name followed by a description).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-occ-prof-rtpd-v1.0_xxaj-4vt3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-OCC-PROF-RTPD-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-occ-prof-rtpd-v1.0_xxaj-4vt3",
-            "description": "This data set includes vertical profiles of refractivity, temperature, pressure and density in the neutral Venus atmosphere. The data set is composed of the following parameter fields (listed as the field name followed by a description).",
-            "title": "MAGELLAN V RSS 5 OCCULTATION PROFILE REF TEMP PRES DENS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MAGELLAN V RSS 5 OCCULTATION PROFILE REF TEMP PRES DENS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC2-MTP014-V1.0",
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
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 2 MTP014 phase, which occurred from 2015-03-11 to 2015-04-08",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc2-mtp014-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC2-MTP014-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc2-mtp014-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 2 MTP014 phase, which occurred from 2015-03-11 to 2015-04-08",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 2 MTP014 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 2 MTP014 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M11-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m11-v1.0_xxbr-bny5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M11-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m11-v1.0_xxbr-bny5",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP011 RDR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP011 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/415/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
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
-            "identifier": "DASHLINK_415",
             "description": "This is the RSW Coarse Tet Only grid with the root viscous tunnel wall.  This grid is for a node-based unstructured solver.\r\n\r\nQuad Surface Faces=         0\r\nTria Surface Faces=    119854\r\nNodes             =   2861927\r\nTotal Elements    =  16981322\r\nHex Elements      =         0\r\nPent_5 Elements   =         0\r\nPent_6 Elements   =         0\r\nTet Elements      =  16981322\r\nBL Tet Elements   =  15310361",
-            "title": "NEW RSW & Wall Coarse Tet Only Grid",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.b8.ugrid",
-                    "description": "Ugrid Format Grid file",
                     "@type": "dcat:Distribution",
+                    "description": "Ugrid Format Grid file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.b8.ugrid",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tet.b8.ugrid"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.info",
-                    "description": "grid information",
                     "@type": "dcat:Distribution",
+                    "description": "grid information",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.info",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tet.info"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.mapbc",
-                    "description": "Mapbc (for FUN3D)",
                     "@type": "dcat:Distribution",
+                    "description": "Mapbc (for FUN3D)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.mapbc",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tet.mapbc"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.tags",
-                    "description": "tags for bc",
                     "@type": "dcat:Distribution",
+                    "description": "tags for bc",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.tags",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tet.tags"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet14.surf",
-                    "description": "surface grid",
                     "@type": "dcat:Distribution",
+                    "description": "surface grid",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet14.surf",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tet14.surf"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.cgns",
-                    "description": "CGNS Format Grid File",
                     "@type": "dcat:Distribution",
+                    "description": "CGNS Format Grid File",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_coarse_tet.cgns",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_coarse_tet.cgns"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_415",
+            "issued": "2011-07-01",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/415/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "NEW RSW & Wall Coarse Tet Only Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-CRS-3-RDR-D1-6SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set describes the data of the high time resolution counting rate from the D1 detector in the Cosmic Ray System (CRS) electron telescope (TET) on Voyager 2 during the Neptune encounter. The D1 detector nominally responds to electrons with kinetic energies above approximately 1 MeV (see detector description for details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-crs-3-rdr-d1-6sec-v1.0_xxc5-iht5",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "neptune",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-CRS-3-RDR-D1-6SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-crs-3-rdr-d1-6sec-v1.0_xxc5-iht5",
-            "description": "This data set describes the data of the high time resolution counting rate from the D1 detector in the Cosmic Ray System (CRS) electron telescope (TET) on Voyager 2 during the Neptune encounter. The D1 detector nominally responds to electrons with kinetic energies above approximately 1 MeV (see detector description for details).",
-            "title": "VG2 NEP CRS CALIB RDR D1 RATE HI RESOLUTION ELEC 6SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP CRS CALIB RDR D1 RATE HI RESOLUTION ELEC 6SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/4ZL43A4619AF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Mosaic of Antarctica 2008-2009 (MOA2009) Image Map, Version 2. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/4ZL43A4619AF.",
-            "issued": "2008-11-01",
-            "temporal": "2008-11-01T00:00:00Z/2009-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-02-28",
-            "keyword": [
-                "glaciers/ice sheets",
-                "cryosphere",
-                "ngda",
-                "earth science",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ted Scambos",
                 "hasEmail": "mailto:scambos@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C2008241421-NSIDCV0",
             "description": "This data set includes two image maps - a snow grain size map and a surface morphology map - provided at two different resolutions of 125 m and 750 m. The maps were produced from composited image swath data acquired by the Moderate Resolution Imaging Spectroradiometer (MODIS) over Antarctica for the 2008-2009 austral summer season.",
-            "title": "MODIS Mosaic of Antarctica 2008-2009 (MOA2009) Image Map, Version 2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4ZL43A4619AF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4ZL43A4619AF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0593_moa2009_v02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4ZL43A4619AF",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/4ZL43A4619AF",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4ZL43A4619AF",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/4ZL43A4619AF",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2008241421-NSIDCV0",
+            "issued": "2008-11-01",
+            "keyword": [
+                "glaciers/ice sheets",
+                "cryosphere",
+                "ngda",
+                "earth science",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/4ZL43A4619AF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-02-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -60.0",
+            "temporal": "2008-11-01T00:00:00Z/2009-02-28T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Mosaic of Antarctica 2008-2009 (MOA2009) Image Map, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/198/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashok Srivastava",
                 "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_198",
             "description": "Modern aircraft are producing data at an unprecedented rate with hundreds of parameters being recorded on a second by second basis. The data can be used for studying the condition of the hardware systems of the aircraft and also for studying the complex interactions between the pilot and the aircraft. NASA is developing novel data mining algorithms to detect precursors to aviation safety incidents from these data sources. This talk will cover the theoretical aspects of the algorithms and practical aspects of implementing these techniques to study one of the most complex dynamical systems in the world: the national airspace.",
-            "title": "Discovering Precursors to Aviation Safety Incidents: KDD 2010",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Srivastava-KDD_2010-1.pdf",
-                    "description": "Srivastava-KDD_2010-1.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Srivastava-KDD_2010-1.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Srivastava-KDD_2010-1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Srivastava-KDD_2010-1.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_198",
+            "issued": "2010-09-22",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/198/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Discovering Precursors to Aviation Safety Incidents: KDD 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/13679",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-10-01",
-            "temporal": "2012-10-01T00:00:00Z/2014-09-01T00:00:00Z",
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
-                "johnson space center",
-                "element"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Gaddis",
                 "hasEmail": "mailto:stephen.w.gaddis@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_13679",
             "description": "&lt;p&gt;The goal of the Robonaut 2 (R2) Technology Project Element within Human Robotic Systems (HRS) is to developed advanced technologies for infusion into the Robonaut 2 project leading to new capabilities for Robonaut. In FY14, HRS and the Technology Demonstration Mission (TDM) Human Exploration Telerobotics (HET) will collaborate to deliver a mobile IVA Robonaut 2 to ISS.&lt;/p&gt;&lt;p&gt;During 2014, the &amp;ldquo;&lt;em&gt;Robonaut 2 Technologies&amp;rdquo;&lt;/em&gt; project element will develop two technologies:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Mobile IVA Robonaut 2&lt;/li&gt;&lt;li&gt;Natural User Interfaces for Advanced Telerobotic Operations&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;The primary work area in this project element is to contribute to sending a mobile IVA Robonaut to the International Space Station (ISS) and to begin using it as a mobile system.&amp;nbsp; The main area where HRS will contribute to Robonaut 2 in FY14 will be in the area of battery development.&amp;nbsp; HRS will perform component testing of the engineering development unit (EDU) and complete assembly of the certification unit battery. The development will eventually lead to a robotic system moving and working safely in the same space as Astronauts on ISS.&amp;nbsp;&lt;/p&gt;&lt;p&gt;The second work area under this project element will be to use body-tracking input devices (i.e. Microsoft Xbox Kinect and accelerometer gloves) to immerse an operator in an accurate virtual model of the robot&amp;rsquo;s environment, capture the intent of the operator, and safely execute mobility and manipulation tasks suitable for platforms such as Robonaut 2. Initially, the operator&amp;rsquo;s head position will be tracked in order to render an appropriate point of view in the virtual environment. Next, model-based recognizers will be developed and trained to detect gestures by the human operator and trigger autonomous behaviors on the robotic system. Initial efforts will use the Kinect sensor, with additional potential investigations into other similar or complementary sensors.&lt;/p&gt;&lt;p&gt;In FY14, development will focus on further extending our natural user interface system to address the concurrent operation of manipulation and mobility aspects of hybrid robotic systems such as Robonaut 2 with legs (ground only in FY14) or an ATHLETE robot driving while manipulating a payload.&lt;/p&gt;",
-            "title": "Human Robotic Systems (HRS): Robonaut 2 Technologies Element",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/13679",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_13679",
+            "issued": "2012-10-01",
+            "keyword": [
+                "active",
+                "johnson space center",
+                "element"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/13679",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Space Technology Mission Directorate"
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
+            "temporal": "2012-10-01T00:00:00Z/2014-09-01T00:00:00Z",
+            "title": "Human Robotic Systems (HRS): Robonaut 2 Technologies Element"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-3-SDSSMOC-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Sloan Digital Sky Survey (SDSS) Moving Object Catalog 3rd release lists astrometric and photometric data for moving objects detected in the SDSS. The catalog includes various identification parameters, SDSS astrometric measurements (five SDSS magnitudes and their errors), and orbital elements for previously cataloged asteroids. The data set also includes a list of the runs from which data are included, and filter response curves.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-3-sdssmoc-v2.0_xxkx-6t62",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "support archives",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-3-SDSSMOC-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-3-sdssmoc-v2.0_xxkx-6t62",
-            "description": "The Sloan Digital Sky Survey (SDSS) Moving Object Catalog 3rd release lists astrometric and photometric data for moving objects detected in the SDSS. The catalog includes various identification parameters, SDSS astrometric measurements (five SDSS magnitudes and their errors), and orbital elements for previously cataloged asteroids. The data set also includes a list of the runs from which data are included, and filter response curves.",
-            "title": "SDSS MOVING OBJECT CATALOG V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SDSS MOVING OBJECT CATALOG V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10733",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2012-12-01T00:00:00Z",
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
-                "nasa headquarters",
-                "project",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pietro Bernasconi",
                 "hasEmail": "mailto:pietro.bernasconi@jhuapl.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10733",
             "description": "&lt;p&gt;\r\n\tN/A&lt;/p&gt;",
-            "title": "Solar Bolometric Imager for Investigating the Sources of Solar Irradiance Variability Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10733",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10733",
+            "issued": "2010-01-01",
+            "keyword": [
+                "nasa headquarters",
+                "project",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10733",
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
+            "temporal": "2010-01-01T00:00:00Z/2012-12-01T00:00:00Z",
+            "title": "Solar Bolometric Imager for Investigating the Sources of Solar Irradiance Variability Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/8LMUGJ8X1ZXB",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2O3CRSFS. Version 1. TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8LMUGJ8X1ZXB. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSFS_1.html. Digital Science Data.",
-            "issued": "2021-05-18",
-            "temporal": "2021-02-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-18",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1029/2006JD007258",
-                "https://doi.org/10.5194/acp-10-9901-2010",
-                "https://doi.org/10.1029/2007JD008819",
-                "https://doi.org/10.5194/amt-6-1413-2013",
-                "https://doi.org/10.5194/amt-11-5587-2018"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2041966826-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of ozone (O3), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2O3CRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3CRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8LMUGJ8X1ZXB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8LMUGJ8X1ZXB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2O3CRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2O3CRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-O3_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-O3_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/TROPESS_ATBDv1.1.pdf",
-                    "description": "ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/TROPESS_ATBDv1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/tropess/",
-                    "description": "TROPESS Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS Project Home Page.",
+                    "downloadURL": "https://tes.jpl.nasa.gov/tropess/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "TROPESS CrIS-SNPP O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSFS_Sample.png",
+            "identifier": "C2041966826-GES_DISC",
+            "issued": "2021-05-18",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/8LMUGJ8X1ZXB",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.1029/2006JD007258",
+                "https://doi.org/10.5194/acp-10-9901-2010",
+                "https://doi.org/10.1029/2007JD008819",
+                "https://doi.org/10.5194/amt-6-1413-2013",
+                "https://doi.org/10.5194/amt-11-5587-2018"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2O3CRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3CRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1218",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ranson, K.J., P.M. Montesano, and R.F. Nelson. 2014. Tree Canopy Cover for the Circumpolar Taiga-Tundra Ecotone: 2000-2005. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1218",
-            "issued": "2023-10-15",
-            "temporal": "2000-01-01T00:00:00Z/2005-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-16",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
-                "earth science",
-                "vegetation",
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
-            "identifier": "C2784383956-ORNL_CLOUD",
             "description": "This data set provides a map of selected areas with defined tree canopy cover over the circumpolar taiga-tundra ecotone (TTE). Canopy cover was derived from the 500-meter MODIS Vegetation Continuous Fields (VCF) product as averaged over six years from 2000-2005 and processed as described in Ranson et al. (2011). This process identified patches of low tree canopy cover which are indicative of the transition from forest to tundra and differentiate the circumpolar taiga-tundra ecotone for the 2000-2005 period. The TTE is the Earth's longest vegetation transition zone and stretches for more than 13,400 km around Arctic North America, Scandinavia, and Eurasia. In Eurasia, the map extends from 60 degrees N to 70 degrees N, and in North America from 50 degrees N to 70 degrees N, excluding Baffin Island in northeastern Canada and the Aleutian Peninsula in southwestern Alaska. Note that for this product, taiga is being used one and the same as boreal forest.This circumpolar TTE area was classified according to VCF tree canopy cover.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Tree Canopy Cover for the Circumpolar Taiga-Tundra Ecotone: 2000-2005",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1218",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1218",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Taiga_Tundra_Tree_Cover/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Taiga_Tundra_Tree_Cover/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Taiga_Tundra_Ecotone_Tree_Cover.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Taiga_Tundra_Ecotone_Tree_Cover.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1218",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1218",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Taiga_Tundra_Tree_Cover/comp/Taiga_Tundra_Ecotone_Tree_Cover.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Taiga_Tundra_Tree_Cover/comp/Taiga_Tundra_Ecotone_Tree_Cover.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
+            "identifier": "C2784383956-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "earth science",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1218",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 50.0 180.0 70.0",
+            "temporal": "2000-01-01T00:00:00Z/2005-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tree Canopy Cover for the Circumpolar Taiga-Tundra Ecotone: 2000-2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-BIBLIOGRAPHY-V1.0",
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
-                "asteroid",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A comprehensive compilation of asteroid-related references, produced by Clifford Cunningham (1990). [CUNNINGHAM1990]",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-bibliography-v1.0_xxqi-hv7a",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-BIBLIOGRAPHY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-bibliography-v1.0_xxqi-hv7a",
-            "description": "A comprehensive compilation of asteroid-related references, produced by Clifford Cunningham (1990). [CUNNINGHAM1990]",
-            "title": "ASTEROID BIBLIOGRAPHY V1.0",
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
+            "title": "ASTEROID BIBLIOGRAPHY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/XPOL/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Krajewski, Witold F and Kumar Vijay Mishra.2016. GPM GROUND VALIDATION IOWA X-BAND POLARIMETRIC MOBILE DOPPLER WEATHER RADARS IFLOODS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/XPOL/DATA201",
-            "issued": "2016-09-15",
-            "temporal": "2013-04-30T22:09:14Z/2013-06-16T05:32:05Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
-            "keyword": [
-                "earth science",
-                "radar",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-ghrc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/MSFC/GHRC"
-            },
-            "identifier": "C1983632696-GHRC_DAAC",
             "description": "The GPM Ground Validation Iowa X-band Polarimetric Mobile Doppler Weather Radars IFloodS dataset was gathered during the IFloodS campaign from April to June 2013 throughout central and northeastern Iowa. The Iowa Flood Studies (IFloodS) was a ground measurement campaign that took place throughout Iowa from May 1 to June 15, 2013. The main goal of IFloodS was to evaluate how well the GPM satellite rainfall data can be used for flood forecasting. Four X-band Polarimetric (XPOL) Mobile Doppler Weather Radars were used to collected high-resolution observations of precipitation. The data consists of reflectivity, Doppler velocity, spectrum width, differential reflectivity, differential phase, copolar correlation coefficient, and sound-to-noise ratios. These data are available in netCDF, and browse image files are available in .png format.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION IOWA X-BAND POLARIMETRIC MOBILE DOPPLER WEATHER RADARS IFLOODS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FXPOL%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FXPOL%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmxpolifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmxpolifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/browse/XPOL4/2013-05-03/RHI/RHI-Psidp-MXPOL4-5-20130503-0316-09-170.0_RR_30_RGS_30.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/browse/XPOL4/2013-05-03/RHI/RHI-Psidp-MXPOL4-5-20130503-0316-09-170.0_RR_30_RGS_30.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IFLOODS/DATA101",
-                    "description": "IFloodS Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IFloodS Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IFLOODS/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://pmm.nasa.gov/GPM",
-                    "description": "GPM Mission Concept",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Mission Concept",
+                    "downloadURL": "http://pmm.nasa.gov/GPM",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://link.springer.com/article/10.1007/s10712-009-9079-x",
-                    "description": "Review of the different sources of uncertainty in single polarization radar-based estimates of rainfall",
                     "@type": "dcat:Distribution",
+                    "description": "Review of the different sources of uncertainty in single polarization radar-based estimates of rainfall",
+                    "downloadURL": "http://link.springer.com/article/10.1007/s10712-009-9079-x",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/doc/gpmxpolifld_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/doc/gpmxpolifld_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/browse/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/XPOL/browse/",
+            "identifier": "C1983632696-GHRC_DAAC",
+            "issued": "2016-09-15",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/XPOL/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-92.3511 41.5293 -90.9114 43.5375",
+            "temporal": "2013-04-30T22:09:14Z/2013-06-16T05:32:05Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION IOWA X-BAND POLARIMETRIC MOBILE DOPPLER WEATHER RADARS IFLOODS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-THREEMICRON-V1.2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "3-micron spectrophotometric data on asteroids collected from several papers by Lebofsky, Jones, and Feierberg and their collaborators, published 1980-1990.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-threemicron-v1.2_xxwz-q9jm",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "423 diotima",
                 "410 chloris",
@@ -1658257,219 +1658259,195 @@
                 "70 panopaea",
                 "704 interamnia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-THREEMICRON-V1.2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-threemicron-v1.2_xxwz-q9jm",
-            "description": "3-micron spectrophotometric data on asteroids collected from several papers by Lebofsky, Jones, and Feierberg and their collaborators, published 1980-1990.",
-            "title": "LEBOFSKY ET AL. 3-MICRON ASTEROID DATA V1.2",
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
+            "title": "LEBOFSKY ET AL. 3-MICRON ASTEROID DATA V1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL08QL.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3A Land and Vegetation Height Quick Look V006. Version 006. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL08QL.006.",
-            "issued": "2024-08-29",
-            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "landscape"
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
-            "identifier": "C2548345108-NSIDC_ECS",
             "description": "ATL08QL is the quick look version of ATL08. Once final ATL08 files are available the corresponding ATL08QL files will be removed. \nATL08 contains along-track heights above the WGS84 ellipsoid (ITRF2014 reference frame) for the ground and canopy surfaces. The canopy and ground surfaces are processed in fixed 100 m data segments, which typically contain more than 100 signal photons. The data were acquired by the Advanced Topographic Laser Altimeter System (ATLAS) instrument on board the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) observatory.",
-            "title": "ATLAS/ICESat-2 L3A Land and Vegetation Height Quick Look V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL08QL.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL08QL.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL08QL.006/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL08QL.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL08QL+V006",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL08QL+V006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL08QL/versions/6/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL08QL/versions/6/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08QL.006",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08QL.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08QL.006",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08QL.006",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2548345108-NSIDC_ECS",
+            "issued": "2024-08-29",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "landscape"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL08QL.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3A Land and Vegetation Height Quick Look V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-LSPN-2-DIDR-GZ-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "halley",
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-lspn-2-didr-gz-v1.0_xxzj-ysdq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-LSPN-2-DIDR-GZ-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-lspn-2-didr-gz-v1.0_xxzj-ysdq",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET LSPN EDITED DIGITALIZED IMAGE DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET LSPN EDITED DIGITALIZED IMAGE DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3371-V1.0",
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
-                "mars express",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-19T03:02:23.000 to 2012-08-19T05:56:00.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3371-v1.0_xy24-bf74",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3371-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3371-v1.0_xy24-bf74",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-19T03:02:23.000 to 2012-08-19T05:56:00.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3371 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3371 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2237418306-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering. 2022-03-01. OCO2_Att. Version 11. OCO-2 Level 0 spacecraft attitude data V11. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_Att_11.html. Digital Science Data.",
-            "issued": "2022-03-01",
-            "temporal": "2019-11-30T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-01",
-            "keyword": [
-                "spectral/engineering",
-                "platform characteristics",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KRISTAN MORGAN",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2237418306-GES_DISC",
-            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectralelements.This product contains pointing angles of the spacecraft for each orbit.It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_Att",
             "creator": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering",
-            "title": "OCO-2 Level 0 spacecraft attitude data V11 (OCO2_Att) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectralelements.This product contains pointing angles of the spacecraft for each orbit.It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1658478,405 +1658456,408 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Att_11.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Att_11.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Att",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Att",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Att.11/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Att.11/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov2.jpl.nasa.gov/",
-                    "description": "OCO-2 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 Project Home Page",
+                    "downloadURL": "https://ocov2.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Att.11/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Att.11/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Attde.V5.pdf",
-                    "description": "Software interface specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software interface specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Attde.V5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
-                    "description": "README document.",
                     "@type": "dcat:Distribution",
+                    "description": "README document.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_B10_DUG.pdf",
-                    "description": "USER'S GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "USER'S GUIDE",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_B10_DUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/nasa/RtRetrievalFramework",
-                    "description": "This software (NASA NTR-49044) retrieves a set of atmospheric/surface/instrument parameters from a simultaneous fit to spectra from multiple absorption bands. The software uses an iterative, non-linear retrieval technique (optimal estimation). After the retrieval process has converged, the software performs an error analysis. The products of the software include all quantities needed to understand the information content of the measurement, its uncertainty, and its dependence on interfering atmospheric properties.\n\nJet Propulsion Laboratory, California Institute of Technology.\nCopyright 2016 California Institute of Technology.\nU.S. Government sponsorship acknowledged.",
                     "@type": "dcat:Distribution",
+                    "description": "This software (NASA NTR-49044) retrieves a set of atmospheric/surface/instrument parameters from a simultaneous fit to spectra from multiple absorption bands. The software uses an iterative, non-linear retrieval technique (optimal estimation). After the retrieval process has converged, the software performs an error analysis. The products of the software include all quantities needed to understand the information content of the measurement, its uncertainty, and its dependence on interfering atmospheric properties.\n\nJet Propulsion Laboratory, California Institute of Technology.\nCopyright 2016 California Institute of Technology.\nU.S. Government sponsorship acknowledged.",
+                    "downloadURL": "https://github.com/nasa/RtRetrievalFramework",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov2.jpl.nasa.gov/science/publications/",
-                    "description": "Publications from the Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "Publications from the Science Team",
+                    "downloadURL": "https://ocov2.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO+Known+Data+Issues",
-                    "description": "OCO-2 Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 Data Gaps",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO+Known+Data+Issues",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
-                    "description": "OCO-2 Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
+            "identifier": "C2237418306-GES_DISC",
+            "issued": "2022-03-01",
+            "keyword": [
+                "spectral/engineering",
+                "platform characteristics",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2237418306-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_Att",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 0 spacecraft attitude data V11 (OCO2_Att) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/208",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hulett, G.K., and G.W. Tomanek. 2014. NPP Grassland: Hays, USA, 1970, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/208",
-            "issued": "2023-08-17",
-            "temporal": "1867-01-01T00:00:00Z/1994-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "earth science",
-                "vegetation",
-                "biosphere",
-                "ecological dynamics"
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
-            "identifier": "C2752578763-ORNL_CLOUD",
             "description": "This data set contains three ASCII files (.txt format). Two files contain above- and below-ground biomass and productivity data for a mixed prairie grassland, one file for an ungrazed treatment and the other for a moderately grazed treatment. The study site (38.87 N, - 99.38 W, Elevation 714 m) is located in the central Great Plains near the city of Hays, Kansas, about 400-km west of Kansas City. The third file contains monthly and annual climate data for the period 1891-1994 obtained from a weather station (38.87 N, -99.38 W, Elevation 613 m) located at the Hays grassland study site. Dynamics of above-ground living and dead plant biomass were monitored by the harvest technique at roughly 2-week intervals during the growing season of 1970. Total below-ground biomass was sampled at the same intervals by manual coring within the harvested plots to a depth sufficient to include at least 90% of the root mass. Data were collected as part of a coordinated study over 1-3 years at ten grassland sites of the central and western United States, under the US Grassland Biome Project of the International Biological Program (IBP).Annual above-ground net primary production (ANPP) was estimated conservatively by summing peak biomass of individual species. These values were 363 g/m2/year for ungrazed and 372 g/m2/year for grazed grassland plots. Annual below-ground net primary production (BNPP) was estimated as the sum of positive increments in total root biomass (including root crowns); 1,062 g/m2/year for ungrazed and 855 g/m2/year for grazed grassland plots.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Hays, USA, 1970, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F208",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F208",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_HYS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_HYS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_HYS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_HYS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/208",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/208",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_HYS/comp/NPP_HYS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_HYS/comp/NPP_HYS.pdf",
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
+            "identifier": "C2752578763-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/208",
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
             "spatial": "38.87 -99.38",
+            "temporal": "1867-01-01T00:00:00Z/1994-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Hays, USA, 1970, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1099-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-13T20:37:35.000 to 2015-10-13T23:45:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1099-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1099-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1099-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-13T20:37:35.000 to 2015-10-13T23:45:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1099 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1099 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FIRAS-C-FPA-5-9P-IMAGES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains radiance and noise maps based on reprocessed IRAS images from 1983 of comet 9P/Tempel 1 in support of the NASA Deep Impact Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-iras-c-fpa-5-9p-images-v1.0_xyae-5n73",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "9p/tempel 1 (1867 g1)",
                 "infrared astronomical satellite",
                 "deep impact"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FIRAS-C-FPA-5-9P-IMAGES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-iras-c-fpa-5-9p-images-v1.0_xyae-5n73",
-            "description": "This data set contains radiance and noise maps based on reprocessed IRAS images from 1983 of comet 9P/Tempel 1 in support of the NASA Deep Impact Mission.",
-            "title": "DEEP IMPACT: IRAS IMAGES OF COMET 9P/TEMPEL 1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT: IRAS IMAGES OF COMET 9P/TEMPEL 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MacPherson, J. I. 1994. Aircraft Flux - Detrended: NRCC (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/3",
-            "issued": "2024-05-02",
-            "temporal": "1987-06-26T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-03",
-            "keyword": [
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "vegetation",
-                "atmospheric temperature",
-                "earth science",
-                "atmospheric water vapor",
-                "biosphere",
-                "atmospheric winds",
-                "altitude",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C2968494372-ORNL_CLOUD",
             "description": "Detrended boundary layer fluxes recorded on aircraft flights over the Konza",
-            "graphic-preview-description": "Browse Image",
-            "title": "Aircraft Flux-Detrended: NRCC (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_dtrnd_nae/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_dtrnd_nae/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_det_nrcc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_det_nrcc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/3",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_nae/comp/aflux_mc.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_nae/comp/aflux_mc.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_nae/comp/af_dtrnd.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_nae/comp/af_dtrnd.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_nae/comp/air_flux_det_nrcc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_nae/comp/air_flux_det_nrcc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
+            "identifier": "C2968494372-ORNL_CLOUD",
+            "issued": "2024-05-02",
+            "keyword": [
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "vegetation",
+                "atmospheric temperature",
+                "earth science",
+                "atmospheric water vapor",
+                "biosphere",
+                "atmospheric winds",
+                "altitude",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-102.0 37.0 -95.0 40.0",
+            "temporal": "1987-06-26T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aircraft Flux-Detrended: NRCC (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VLBI/VLBI_daily_ind_soln_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/VLBI/VLBI_daily_ind_soln_001.",
-            "issued": "1984-02-03",
-            "temporal": "1984-02-03T00:00:00Z/2020-11-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "geodetics",
-                "earth science",
-                "solid earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDDIS"
-            },
-            "identifier": "C3241567254-CDDIS",
             "description": "The daily solution files are an analysis product that provides estimates of Earth orientation and site positions for each 24-hour session, the covariance matrix of the estimates, and decomposed normal equations. The solution files are in SINEX format. The SINEX product files are available on the same frequency as the EOP-S products: 24 hours after each new session data base is available.",
-            "title": "Very Long Baseline Interferometry (VLBI) Daily SINEX Independent Solution product (DSNX) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2FVLBI_daily_ind_soln_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2FVLBI_daily_ind_soln_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1658886,93 +1658867,114 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C3241567254-CDDIS",
+            "issued": "1984-02-03",
+            "keyword": [
+                "geodetics",
+                "earth science",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/VLBI/VLBI_daily_ind_soln_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-11-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1984-02-03T00:00:00Z/2020-11-03T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Very Long Baseline Interferometry (VLBI) Daily SINEX Independent Solution product (DSNX) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206550-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Active layer and permafrost properties, including snow depth, soil temperature, and soil moisture, Barrow, Alaska, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1962-01-01",
-            "temporal": "1962-01-01T00:00:00Z/1993-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1993-12-31",
-            "keyword": [
-                "snow/ice",
-                "frozen ground",
-                "soils",
-                "earth science",
-                "land surface",
-                "cryosphere",
-                "agriculture",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jerry Brown",
                 "hasEmail": "mailto:jerrybrown@igc.apc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206550-NSIDCV0",
             "description": "This data set contains soil temperature, soil moisture, thaw depth, and snow depth data collected at test sites near Barrow, Alaska, during the following years.\n\nSoil temperature data - 1963-1966, 1993  Soil moisture data - 1963  Thaw depth - 1962-1968, 1991-1993  Snow depth - 1963-1964  This study focused on characterizing the active soil layer at Barrow, and determining the relationships between and among these physical properties at permafrost sites in the Arctic.\n\nThis site is U1 of the IPA's Circumpolar Active Layer Monitoring (CALM) Program and later measurements are available at the CALM Web site.",
-            "title": "Active layer and permafrost properties, including snow depth, soil temperature, and soil moisture, Barrow, Alaska, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD222_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD222_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD222/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD222/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD222/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD222/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206550-NSIDCV0",
+            "issued": "1962-01-01",
+            "keyword": [
+                "snow/ice",
+                "frozen ground",
+                "soils",
+                "earth science",
+                "land surface",
+                "cryosphere",
+                "agriculture",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206550-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1993-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-156.78872 71.29058 -156.78872 71.29058",
+            "temporal": "1962-01-01T00:00:00Z/1993-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Active layer and permafrost properties, including snow depth, soil temperature, and soil moisture, Barrow, Alaska, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-3-JUPITER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-3-jupiter-v1.0_xyia-uhzd",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "new horizons",
@@ -1658982,175 +1658984,175 @@
                 "j1 io",
                 "j2 europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-3-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-3-jupiter-v1.0_xyia-uhzd",
-            "description": "This data set contains Calibrated data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS MVIC JUPITER ENCOUNTER V1.0",
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
+            "title": "NEW HORIZONS MVIC JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2019-04-01. TEMPO solar irradiance (BETA). Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.002. https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.002.",
-            "issued": "2019-03-27",
-            "temporal": "2023-08-01T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-04-01",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Raid Suleiman",
                 "hasEmail": "mailto:rsuleiman@cfa.harvard.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2842852230-LARC_CLOUD",
             "description": "Level 1 irradiance files provide solar irradiance measured using the working solar diffuser. Each file includes the measured solar irradiance for all the North-South cross-track pixels. The files are provided in netCDF4 format, and contain information on radiometrically and wavelength calibrated solar irradiance for the UV and visible bands, corresponding noise, parameterized wavelength grid, solar viewing geometry, quality flags and other ancillary information. The product is produced using the L0-1b processor which includes multiple steps: (1) Image processing to produce radiometrically calibrated radiance, and (2) Additional wavelength calibration to improve wavelength registration. Please refer to the ATBD for details.\r\nThese data are beta. Beta maturity is defined as: the product is minimally validated but may still contain significant errors; it is based on product quick looks using the initial calibration parameters.\r\nBecause the products at this stage have minimal validation, users should refrain from making conclusive public statements regarding science and applications of the data products until a product is designated at the provisional validation status.\r\nThe TEMPO Level 1 ATBD is still being finalized. For access to Version 1.0 ATBD, please contact the ASDC at larc-dl-asdc-tempo@mail.nasa.gov.",
-            "graphic-preview-description": "TEMPO Logo",
-            "title": "TEMPO solar irradiance V02 (BETA)",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FIRR_L1.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FIRR_L1.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tempo.si.edu",
-                    "description": "TEMPO project page",
                     "@type": "dcat:Distribution",
+                    "description": "TEMPO project page",
+                    "downloadURL": "https://tempo.si.edu",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.002",
-                    "description": "DOI data set landing page for TEMPO_IRR_L1_V02",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TEMPO_IRR_L1_V02",
+                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-                    "description": "TEMPO Logo",
                     "@type": "dcat:Distribution",
+                    "description": "TEMPO Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
-                    "description": "ASDC Data and Information for TEMPO",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for TEMPO",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2842852230-LARC_CLOUD",
-                    "description": "Earthdata Search for TEMPO_IRR_L1_V02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TEMPO_IRR_L1_V02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2842852230-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_Level-1_user_guide_V1.0.pdf",
-                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Level 1 Data Products: User Guide V1.0",
                     "@type": "dcat:Distribution",
+                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Level 1 Data Products: User Guide V1.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_Level-1_user_guide_V1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "TEMPO Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+            "identifier": "C2842852230-LARC_CLOUD",
+            "issued": "2019-03-27",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>10.0 -170.0 10.0 -10.0 80.0 -10.0 80.0 -170.0 10.0 -170.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2023-08-01T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "TEMPO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TEMPO solar irradiance V02 (BETA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-3-KEM1-V3.0",
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
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 3.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach and departure field around MU69 (Arrokoth). The data also cover the actual MU69 encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-3-kem1-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-3-KEM1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-3-kem1-v3.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 3.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach and departure field around MU69 (Arrokoth). The data also cover the actual MU69 encounter.",
-            "title": "NEW HORIZONS\n      LORRI KEM1\n      CALIBRATED V3.0",
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
+            "title": "NEW HORIZONS\n      LORRI KEM1\n      CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-3-RDR-HIGHRES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains high time resolution magnetic field vectors acquired by the Galileo magnetometer (MAG). It includes both satellite flyby and non-flyby data. These data were acquired in order to characterize various portions of the Jovian magnetosphere at high time resolution. The Galileo Magnetospheres Working Group (MWG) collectively acquired high time resolution data for short intervals in order to try and regain some of the magnetospheric science lost due to the low data rates of the phase 2 mission (no high gain antenna) mission. These observations are scattered in Jovian distance, local time, System III longitude, etc. in order to provide some insight into processes that may be active in different regions of the magnetosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-3-rdr-highres-v1.0_xymi-mcg6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "amalthea",
                 "io plasma torus",
@@ -1659161,529 +1659163,503 @@
                 "io",
                 "europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-3-RDR-HIGHRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-3-rdr-highres-v1.0_xymi-mcg6",
-            "description": "This data set contains high time resolution magnetic field vectors acquired by the Galileo magnetometer (MAG). It includes both satellite flyby and non-flyby data. These data were acquired in order to characterize various portions of the Jovian magnetosphere at high time resolution. The Galileo Magnetospheres Working Group (MWG) collectively acquired high time resolution data for short intervals in order to try and regain some of the magnetospheric science lost due to the low data rates of the phase 2 mission (no high gain antenna) mission. These observations are scattered in Jovian distance, local time, System III longitude, etc. in order to provide some insight into processes that may be active in different regions of the magnetosphere.",
-            "title": "GALILEO ORBITER AT JUPITER CALIBRATED MAG HIGH RES V1.0",
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
+            "title": "GALILEO ORBITER AT JUPITER CALIBRATED MAG HIGH RES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-3-CR4A-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains calibrated data (CODMAC level 3) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR4A phase. During this phase, CONSERT instrument has performed a ranging between Rosetta and Philae. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-3-cr4a-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-3-CR4A-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-3-cr4a-v1.0",
-            "description": "This archive contains calibrated data (CODMAC level 3) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR4A phase. During this phase, CONSERT instrument has performed a ranging between Rosetta and Philae. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 3 CR4A V1.0",
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
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 3 CR4A V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-MIMI-4-LEMMS-CALIB-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "cassini-huygens",
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Magnetospheric Imaging Instrument (MIMI) Low Energy Magnetospheric Measurements (LEMMS) measures ions and electrons in the energy range 0.03 to 18 MeV for ions and 0.015 to 0.884 MeV for electrons. The LEMMS calibrated data set includes two types of daily plots -- one presenting energy-time spectorgrams in units of intensity, and one with plots of particle pressures. There are also four types of averaged data -- minute and hourly averages for accumulator rate data and PHA data (ions and electrons). These data have been created at the Johns Hopkins University Applied Physics Laboratory by applying the calibrations and averaging. Averaging is done by first defining time periods, and then averaging all data points within those fixed intervals. The time reported is the midpoint time of the interval.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-mimi-4-lemms-calib-v1.0_xypf-gbf3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-MIMI-4-LEMMS-CALIB-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-mimi-4-lemms-calib-v1.0_xypf-gbf3",
-            "description": "The Cassini Magnetospheric Imaging Instrument (MIMI) Low Energy Magnetospheric Measurements (LEMMS) measures ions and electrons in the energy range 0.03 to 18 MeV for ions and 0.015 to 0.884 MeV for electrons. The LEMMS calibrated data set includes two types of daily plots -- one presenting energy-time spectorgrams in units of intensity, and one with plots of particle pressures. There are also four types of averaged data -- minute and hourly averages for accumulator rate data and PHA data (ions and electrons). These data have been created at the Johns Hopkins University Applied Physics Laboratory by applying the calibrations and averaging. Averaging is done by first defining time periods, and then averaging all data points within those fixed intervals. The time reported is the midpoint time of the interval.",
-            "title": "CASSINI S MIMI LEMMS SENSOR CALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI S MIMI LEMMS SENSOR CALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-MRFLRO-2%2F3%2F5-BISTATIC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "lunar reconnaissance orbiter",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains radar data of the lunar surface from bistatic measurements utilizing the Aricebo Observatory transmitter and LRO Mini-RF receiver.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-mrflro-2-3-5-bistatic-v1.0_xyq5-uzsi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar reconnaissance orbiter",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-MRFLRO-2%2F3%2F5-BISTATIC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-mrflro-2-3-5-bistatic-v1.0_xyq5-uzsi",
-            "description": "This data set contains radar data of the lunar surface from bistatic measurements utilizing the Aricebo Observatory transmitter and LRO Mini-RF receiver.",
-            "title": "LRO MOON MINI-RF 2/3/5 BISTATIC RADAR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LRO MOON MINI-RF 2/3/5 BISTATIC RADAR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RSR12-L2C10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Remote Sensing Systems. 2016-11-14. Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid. Version 1.0. Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/RSR12-L2C10. http://images.remss.com/papers/rsstech/2016_081816_RSS_Radiometers_RapidScat_colocations.pdf. Remote Sensing Systems, PO.DAAC, 2016-11-14, Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid, http://images.remss.com/papers/rsstech/2016_081816_RSS_Radiometers_RapidScat_colocations.pdf.",
-            "issued": "2016-08-24",
-            "temporal": "2014-10-03T19:28:21Z/2016-02-11T15:56:16Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "ocean winds",
-                "atmosphere",
-                "clouds",
-                "earth science",
-                "oceans",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2526576258-POCLOUD",
-            "description": "This dataset contains the multi-sourced microwave radiometer wind speed, rain and cloud liquid water data collocated to RapidScat Level 2B wind vector cell (WVC) locations. The corresponding NASA mission is officially referred to as ISS-RapidScat. This dataset is produced by Remote Sensing Systems (RSS) with direct funding from the JPL RapidScat project. All of the collocated radiometer data is produced by RSS. The co-located radiometer sources include: 1) DMSP SSM/I (F15) and SSMIS (F16/F17), 2) Coriolis WindSat, 3) GCOM-W1 AMSR2 and 4) GPM Core GMI; more details on these radiometer sources and sensors can be extracted by scrolling down to the \"Platform/Sensor\" section below this description. RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. This dataset is provided in a netCDF-4 file format that follows the netCDF \"classic\" model and made available via FTP and OPeNDAP. For data access, please click on the \"Data Access\" tab above.",
-            "release-place": "PO.DAAC",
-            "series-name": "Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Remote Sensing Systems",
-            "title": "Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_COLOCATED_RSS_RADIOMETER_LEVEL_2B_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the multi-sourced microwave radiometer wind speed, rain and cloud liquid water data collocated to RapidScat Level 2B wind vector cell (WVC) locations. The corresponding NASA mission is officially referred to as ISS-RapidScat. This dataset is produced by Remote Sensing Systems (RSS) with direct funding from the JPL RapidScat project. All of the collocated radiometer data is produced by RSS. The co-located radiometer sources include: 1) DMSP SSM/I (F15) and SSMIS (F16/F17), 2) Coriolis WindSat, 3) GCOM-W1 AMSR2 and 4) GPM Core GMI; more details on these radiometer sources and sensors can be extracted by scrolling down to the \"Platform/Sensor\" section below this description. RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. This dataset is provided in a netCDF-4 file format that follows the netCDF \"classic\" model and made available via FTP and OPeNDAP. For data access, please click on the \"Data Access\" tab above.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSR12-L2C10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSR12-L2C10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/windsat",
-                    "description": "Wentz, F.J., L.Ricciardulli, C.Gentemann, T. Meissner, K.A. Hilburn, J. Scott, 2013:  Remote Sensing Systems Coriolis WindSat [indicate whether you used Daily, 3-Day, Weekly, or Monthly]  Environmental Suite on 0.25 deg grid, Version 7.0.1. Remote Sensing Systems, Santa Rosa, CA.",
                     "@type": "dcat:Distribution",
+                    "description": "Wentz, F.J., L.Ricciardulli, C.Gentemann, T. Meissner, K.A. Hilburn, J. Scott, 2013:  Remote Sensing Systems Coriolis WindSat [indicate whether you used Daily, 3-Day, Weekly, or Monthly]  Environmental Suite on 0.25 deg grid, Version 7.0.1. Remote Sensing Systems, Santa Rosa, CA.",
+                    "downloadURL": "http://www.remss.com/missions/windsat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/i/iss-rapidscat",
-                    "description": "Detailed background information on the ISS-RapidScat mission published by the eoPortal.",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed background information on the ISS-RapidScat mission published by the eoPortal.",
+                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/i/iss-rapidscat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/rapidscat/ancillary/revtime.csv",
-                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
                     "@type": "dcat:Distribution",
+                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/rapidscat/ancillary/revtime.csv",
+                    "mediaType": "text/csv",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_COLOCATED_RSS_RADIOMETER_LEVEL_2B_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_COLOCATED_RSS_RADIOMETER_LEVEL_2B_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/dataset/RSCAT_LEVEL_2B_OWV_CLIM_12_V1",
-                    "description": "Access to Climate quality L2B data record.",
                     "@type": "dcat:Distribution",
+                    "description": "Access to Climate quality L2B data record.",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/dataset/RSCAT_LEVEL_2B_OWV_CLIM_12_V1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.jpl.nasa.gov/news/fact_sheets/issrapidscat_factsheet.pdf",
-                    "description": "Summary of Facts on the ISS-RapidScat Mission",
                     "@type": "dcat:Distribution",
+                    "description": "Summary of Facts on the ISS-RapidScat Mission",
+                    "downloadURL": "http://www.jpl.nasa.gov/news/fact_sheets/issrapidscat_factsheet.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://winds.jpl.nasa.gov/missions/RapidScat/",
-                    "description": "Website providing more detailed information about the ISS-RapidScat Mission.",
                     "@type": "dcat:Distribution",
+                    "description": "Website providing more detailed information about the ISS-RapidScat Mission.",
+                    "downloadURL": "https://winds.jpl.nasa.gov/missions/RapidScat/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/gmi",
-                    "description": "Wentz, F.J., T. Meissner, J. Scott, K.A. Hilburn, 2015:  Remote Sensing Systems GPM GMI [indicate whether you used Daily, 3-Day, Weekly, or Monthly]  Environmental Suite on 0.25 deg grid, Version 8.1. Remote Sensing Systems, Santa Rosa, CA.",
                     "@type": "dcat:Distribution",
+                    "description": "Wentz, F.J., T. Meissner, J. Scott, K.A. Hilburn, 2015:  Remote Sensing Systems GPM GMI [indicate whether you used Daily, 3-Day, Weekly, or Monthly]  Environmental Suite on 0.25 deg grid, Version 8.1. Remote Sensing Systems, Santa Rosa, CA.",
+                    "downloadURL": "http://www.remss.com/missions/gmi",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://images.remss.com/papers/rsstech/2016_081816_RSS_Radiometers_RapidScat_colocations.pdf",
-                    "description": "Ricciardulli, L., 2016: Radiometer rain colocations with JPL RapidScat winds on L2B swath grid.  Technical Report 081816, Remote Sensing Systems, Santa Rosa, CA, p. 6.",
                     "@type": "dcat:Distribution",
+                    "description": "Ricciardulli, L., 2016: Radiometer rain colocations with JPL RapidScat winds on L2B swath grid.  Technical Report 081816, Remote Sensing Systems, Santa Rosa, CA, p. 6.",
+                    "downloadURL": "http://images.remss.com/papers/rsstech/2016_081816_RSS_Radiometers_RapidScat_colocations.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://images.remss.com/papers/ricciardulli/ricciardulli_jaot_2015.pdf",
-                    "description": "Ricciardulli, L. and F.J. Wentz, 2015: A Scatterometer Geophysical Model Function for Climate-Quality Winds: QuikSCAT Ku-2011. Journal of Atmospheric and Oceanic Technology, 32, 1829-1846.",
                     "@type": "dcat:Distribution",
+                    "description": "Ricciardulli, L. and F.J. Wentz, 2015: A Scatterometer Geophysical Model Function for Climate-Quality Winds: QuikSCAT Ku-2011. Journal of Atmospheric and Oceanic Technology, 32, 1829-1846.",
+                    "downloadURL": "http://images.remss.com/papers/ricciardulli/ricciardulli_jaot_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/ssmi",
-                    "description": "Wentz, F.J., K.A. Hilburn, D.K. Smith, 2012: Remote Sensing Systems DMSP [SSM/I or SSMIS] [Daily, 3-Day, Weekly, Monthly] Environmental Suite on 0.25 deg grid, Version 7. Remote Sensing Systems, Santa Rosa, CA.",
                     "@type": "dcat:Distribution",
+                    "description": "Wentz, F.J., K.A. Hilburn, D.K. Smith, 2012: Remote Sensing Systems DMSP [SSM/I or SSMIS] [Daily, 3-Day, Weekly, Monthly] Environmental Suite on 0.25 deg grid, Version 7. Remote Sensing Systems, Santa Rosa, CA.",
+                    "downloadURL": "http://www.remss.com/missions/ssmi",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/amsre",
-                    "description": "Wentz, F.J., T. Meissner, C. Gentemann, K.A. Hilburn, J. Scott, 2014:  Remote Sensing Systems GCOM-W1 AMSR2  [indicate whether you used Daily, 3-Day, Weekly, or Monthly]  Environmental Suite on 0.25 deg grid, Version 7.2. Remote Sensing Systems, Santa Rosa, CA.",
                     "@type": "dcat:Distribution",
+                    "description": "Wentz, F.J., T. Meissner, C. Gentemann, K.A. Hilburn, J. Scott, 2014:  Remote Sensing Systems GCOM-W1 AMSR2  [indicate whether you used Daily, 3-Day, Weekly, or Monthly]  Environmental Suite on 0.25 deg grid, Version 7.2. Remote Sensing Systems, Santa Rosa, CA.",
+                    "downloadURL": "http://www.remss.com/missions/amsre",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://manati.star.nesdis.noaa.gov/rscat_images/monitor/RapidScat_Scheduled_Outages.txt",
-                    "description": "Text file containing reverse chronological list of future scheduled outages and past outages. A start/stop date/time and description is provided for each outage. This list is maintained by NOAA/NESDIS to service near-real-time data users.",
                     "@type": "dcat:Distribution",
+                    "description": "Text file containing reverse chronological list of future scheduled outages and past outages. A start/stop date/time and description is provided for each outage. This list is maintained by NOAA/NESDIS to service near-real-time data users.",
+                    "downloadURL": "http://manati.star.nesdis.noaa.gov/rscat_images/monitor/RapidScat_Scheduled_Outages.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/colocated/rss/radiometer/v1.0/README.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/colocated/rss/radiometer/v1.0/README.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2526576258-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2526576258-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2526576258-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2526576258-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_COLOCATED_RSS_RADIOMETER_LEVEL_2B_V1.jpg",
+            "identifier": "C2526576258-POCLOUD",
+            "issued": "2016-08-24",
+            "keyword": [
+                "ocean winds",
+                "atmosphere",
+                "clouds",
+                "earth science",
+                "oceans",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/RSR12-L2C10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid",
             "spatial": "-180.0 -61.0 180.0 61.0",
+            "temporal": "2014-10-03T19:28:21Z/2016-02-11T15:56:16Z",
             "theme": [
                 "ISS_RapidScat",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/460",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Roulet, N.T. 1999. BOREAS TGB-04 NSA-BVP Tower Flux and Meteorological Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/460",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-28T00:00:00Z/1994-09-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "biosphere",
-                "ground water",
-                "surface water",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2808091300-ORNL_CLOUD",
             "description": "The flux and ancillary data collected at the NSA-BP tower flux site by the TGB-04 group.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-04 NSA-BVP Tower Flux and Meteorological Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F460",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F460",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb4flux/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb4flux/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB04_NSA-BP_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB04_NSA-BP_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/460",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/460",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/TGB04_NSA-BP_Flux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/TGB04_NSA-BP_Flux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/TGB04_NSA-BP_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/TGB04_NSA-BP_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/TGB04_NSA-BP_Flux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/TGB04_NSA-BP_Flux.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/tgb4flux.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb4flux/comp/tgb4flux.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
+            "identifier": "C2808091300-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "biosphere",
+                "ground water",
+                "surface water",
+                "terrestrial hydrosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/460",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "55.84 -98.03",
+            "temporal": "1994-05-28T00:00:00Z/1994-09-17T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-04 NSA-BVP Tower Flux and Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NOAA21/GPROFCLIM/3A-MONTH/07",
             "citation": "GPM Science Team. 2023-05-30. GPM_3GPROFNOAA21ATMS_CLIM. Version 07. GPM ATMS on NOAA-21 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/ATMS/NOAA21/GPROFCLIM/3A-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFNOAA21ATMS_CLIM_07.html. Digital Science Data.",
-            "issued": "2023-05-30",
-            "temporal": "2023-02-01T00:00:00Z/2023-06-26T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-30",
-            "keyword": [
-                "atmosphere",
-                "precipitation",
-                "atmospheric water vapor",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRISTIAN KUMMEROW",
                 "hasEmail": "mailto:kummerow@atmos.colostate.edu"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2712827637-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions are no longer available and have been superseded by Version 07. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_3GPROFNOAA21ATMS_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM ATMS on NOAA-21 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA21ATMS_CLIM) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from GPM ATMS on NOAA-21 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA21ATMS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA21ATMS_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNOAA21%2FGPROFCLIM%2F3A-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNOAA21%2FGPROFCLIM%2F3A-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA21ATMS_CLIM_07.png",
-                    "description": "Surface Precipitation from GPM ATMS on NOAA-21 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA21ATMS)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from GPM ATMS on NOAA-21 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA21ATMS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA21ATMS_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFNOAA21ATMS_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFNOAA21ATMS_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFNOAA21ATMS_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFNOAA21ATMS_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFNOAA21ATMS_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFNOAA21ATMS_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFNOAA21ATMS_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFNOAA21ATMS_CLIM_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm.nasa.gov",
-                    "description": "GPM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Project Home Page",
+                    "downloadURL": "https://gpm.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/stout/helpdesk/filespec.GPM.V7.pdf",
-                    "description": "FILE SPECIFICATION DOCUMENT",
                     "@type": "dcat:Distribution",
+                    "description": "FILE SPECIFICATION DOCUMENT",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/stout/helpdesk/filespec.GPM.V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
@@ -1659693,40 +1659669,78 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
-                    "description": "Instrument Description from NOAA",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from NOAA",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/gpm_anomalous.html",
-                    "description": "GPM and partner sensors anomalous events",
                     "@type": "dcat:Distribution",
+                    "description": "GPM and partner sensors anomalous events",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/gpm_anomalous.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 }
             ],
+            "graphic-preview-description": "Surface Precipitation from GPM ATMS on NOAA-21 GPROF (0.25 degree x 0.25 degree) (GPM_3GPROFNOAA21ATMS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFNOAA21ATMS_CLIM_07.png",
+            "identifier": "C2712827637-GES_DISC",
+            "issued": "2023-05-30",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NOAA21/GPROFCLIM/3A-MONTH/07",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GPM_3GPROFNOAA21ATMS_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-02-01T00:00:00Z/2023-06-26T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM ATMS on NOAA-21 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA21ATMS_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566211-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "EROS Long Term Archive. 1993-01-01. Aircraft Scanners. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. Remote Sensing Image.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EROS CENTER",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "creator": "EROS Long Term Archive",
+            "data-presentation-form": "Remote Sensing Image",
+            "description": "The National Aeronautics and Space Administration (NASA) Aircraft \n      Scanners data set contains digital imagery acquired from several \n      multispectral scanners, including Daedalus thematic mapper simulator\n      scanners and  the thermal infrared multispectral scanner.  Data are\n      collected from  selected areas over the conterminous United States,\n      Alaska, and Hawaii by  NASA ER-2 and NASA C-130B aircraft, operating\n      from the NASA Ames Research  Center in Moffett Field, California, and by\n      NASA Learjet aircraft, operating  from Stennis Space Center in Bay St.\n      Louis, Mississippi.  Limited  international acquisitions also are\n      available.\n      \n      In cooperation with the Jet Propulsion Laboratory and Daedalus \n      Enterprises,Inc., NASA developed several multispectral sensors.  The\n      data  acquired from these sensors supports NASA's Airborne Science and\n      Applications  Program and have been identified as precursors to the\n      instruments scheduled to  fly on Earth Observing System platforms.\n      \n      THEMATIC MAPPER SIMULATOR\n      \n      The Thematic Mapper Simulator (TMS) sensor is a line scanning device   \n      designed for a variety of Earth science applications.  Flown aboard       \n      NASA ER-2 aircraft, the TMS sensor has a nominal Instantaneous Field  of       \n      View of 1.25 milliradians with a ground resolution of 81 feet (25  meters)     \n        at 65,000 feet. The TMS sensor scans at a rate of 12.5 scans per  second     \n        with 716 pixels per scan line.  Swath width is 8.3 nautical miles       \n      (15.4 kilometers) at 65,000 feet while the scanner's Field of View  is       \n      42.5 degrees.  \n      \n      NS-001 MULTISPECTRAL SCANNER \n      \n      The NS-001multispectral scanner is a line scanning device designed  to       \n      simulate Landsat thematic mapper (TM) sensor performance, including  a       \n      near infrared/short-wave infrared band used in applications similar  to those  \n      of the TM sensor (e.g., Earth resources mapping, vegetation/land  cover   \n      mapping, geologic studies).  Flown aboard NASA C-130B aircraft, the  NS-001\n      sensor has a nominal Instantaneous Field of View of 2.5 milliradians     with a\n      ground resolution of 25 feet (7.6 meters) at 10,000 feet.  The sensor has a\n      variable scan rate (10 to 100 scans per second) with 699  pixels per scan line,\n      but the available motor drive supply restricts the  maximum stable scan speed\n      to approximately 85 revolutions per second. A scan rate  of 100 revolutions per\n      second is possible, but not probable, for short  scan lines; therefore, a\n      combination of factors, including aircraft  flight requirements and maximum\n      scan speed, prevent scanner operation below 1,500 feet.  Swath width is 3.9\n      nautical miles (7.26 kilometers) at 10,000 feet, and the total scan angle or\n      field of regard for the sensor is 100 degrees, plus or minus 15 degrees for\n      roll compensation.         \n      \n      THERMAL INFRARED MULTISPECTRAL SCANNER         \n      \n      The Thermal Infrared Multispectral Scanner (TIMS) sensor is a line  scanning  \n      device originally designed for geologic applications.  Flown aboard NASA\n      C-130B, NASA ER-2, and NASA Learjet aircraft, the TIMS sensor  has a       \n      nominal Instantaneous Field of View of 2.5 milliradians with a  ground       \n      resolution of 25 feet (7.6 meters) at 10,000 feet.  The sensor has a       \n      selectable scan rate (7.3, 8.7, 12, or 25 scans per second) with 698  pixels   \n      per scan line.  Swath width is 2.6 nautical miles (4.8 kilometers)  at     \n      10,000 feet while the scanner's Field of View is 76.56 degrees.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1220566211-USGS_LTA",
             "issued": "1987-10-06",
-            "temporal": "1987-10-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "visible wavelengths",
                 "earth science",
@@ -1659735,55 +1659749,49 @@
                 "atmosphere",
                 "atmospheric radiation"
             ],
-            "data-presentation-form": "Remote Sensing Image",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EROS CENTER",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566211-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-25",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DOI/USGS/EROS"
             },
-            "identifier": "C1220566211-USGS_LTA",
-            "description": "The National Aeronautics and Space Administration (NASA) Aircraft \n      Scanners data set contains digital imagery acquired from several \n      multispectral scanners, including Daedalus thematic mapper simulator\n      scanners and  the thermal infrared multispectral scanner.  Data are\n      collected from  selected areas over the conterminous United States,\n      Alaska, and Hawaii by  NASA ER-2 and NASA C-130B aircraft, operating\n      from the NASA Ames Research  Center in Moffett Field, California, and by\n      NASA Learjet aircraft, operating  from Stennis Space Center in Bay St.\n      Louis, Mississippi.  Limited  international acquisitions also are\n      available.\n      \n      In cooperation with the Jet Propulsion Laboratory and Daedalus \n      Enterprises,Inc., NASA developed several multispectral sensors.  The\n      data  acquired from these sensors supports NASA's Airborne Science and\n      Applications  Program and have been identified as precursors to the\n      instruments scheduled to  fly on Earth Observing System platforms.\n      \n      THEMATIC MAPPER SIMULATOR\n      \n      The Thematic Mapper Simulator (TMS) sensor is a line scanning device   \n      designed for a variety of Earth science applications.  Flown aboard       \n      NASA ER-2 aircraft, the TMS sensor has a nominal Instantaneous Field  of       \n      View of 1.25 milliradians with a ground resolution of 81 feet (25  meters)     \n        at 65,000 feet. The TMS sensor scans at a rate of 12.5 scans per  second     \n        with 716 pixels per scan line.  Swath width is 8.3 nautical miles       \n      (15.4 kilometers) at 65,000 feet while the scanner's Field of View  is       \n      42.5 degrees.  \n      \n      NS-001 MULTISPECTRAL SCANNER \n      \n      The NS-001multispectral scanner is a line scanning device designed  to       \n      simulate Landsat thematic mapper (TM) sensor performance, including  a       \n      near infrared/short-wave infrared band used in applications similar  to those  \n      of the TM sensor (e.g., Earth resources mapping, vegetation/land  cover   \n      mapping, geologic studies).  Flown aboard NASA C-130B aircraft, the  NS-001\n      sensor has a nominal Instantaneous Field of View of 2.5 milliradians     with a\n      ground resolution of 25 feet (7.6 meters) at 10,000 feet.  The sensor has a\n      variable scan rate (10 to 100 scans per second) with 699  pixels per scan line,\n      but the available motor drive supply restricts the  maximum stable scan speed\n      to approximately 85 revolutions per second. A scan rate  of 100 revolutions per\n      second is possible, but not probable, for short  scan lines; therefore, a\n      combination of factors, including aircraft  flight requirements and maximum\n      scan speed, prevent scanner operation below 1,500 feet.  Swath width is 3.9\n      nautical miles (7.26 kilometers) at 10,000 feet, and the total scan angle or\n      field of regard for the sensor is 100 degrees, plus or minus 15 degrees for\n      roll compensation.         \n      \n      THERMAL INFRARED MULTISPECTRAL SCANNER         \n      \n      The Thermal Infrared Multispectral Scanner (TIMS) sensor is a line  scanning  \n      device originally designed for geologic applications.  Flown aboard NASA\n      C-130B, NASA ER-2, and NASA Learjet aircraft, the TIMS sensor  has a       \n      nominal Instantaneous Field of View of 2.5 milliradians with a  ground       \n      resolution of 25 feet (7.6 meters) at 10,000 feet.  The sensor has a       \n      selectable scan rate (7.3, 8.7, 12, or 25 scans per second) with 698  pixels   \n      per scan line.  Swath width is 2.6 nautical miles (4.8 kilometers)  at     \n      10,000 feet while the scanner's Field of View is 76.56 degrees.",
             "release-place": "Sioux Falls, South Dakota, USA",
-            "creator": "EROS Long Term Archive",
-            "title": "Aircraft Scanners",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-180.0 24.0 -60.0 72.0",
+            "temporal": "1987-10-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "EOSDIS",
                 "ELTA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aircraft Scanners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xywd-e9yg",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://lpdaac.usgs.gov/dataset_discovery/modis"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Earthdata User Services",
+                "hasEmail": "mailto:support@earthdata.nasa.gov"
+            },
+            "description": "This dataset represents multiple products archived at the multiple archive centers for the MODIS (Moderate Resolution Imaging Spectroradiometer) instrument aboard the Aqua Satellite. This dataset is provided by NASA EOSDIS as a single point of entry for this suite of products. The provided access URL is link to EOSDIS's Earthdata Search tool with a pre-populated query that will bring up all products archived by EOSDIS with imagery provided by the MODIS instrument on Aqua.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MODIS&ff=Map+Imagery&fp=AQUA",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "MODIS_AQUA_NASA_EOSDIS_xywd-e9yg",
+            "issued": "2021-05-20",
             "keyword": [
                 "atmospheric radiation",
                 "land temperature",
@@ -1659803,233 +1659811,206 @@
                 "earth science",
                 "atmospheric water vapor"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Earthdata User Services",
-                "hasEmail": "mailto:support@earthdata.nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "EOSDIS"
-            },
-            "identifier": "MODIS_AQUA_NASA_EOSDIS_xywd-e9yg",
-            "description": "This dataset represents multiple products archived at the multiple archive centers for the MODIS (Moderate Resolution Imaging Spectroradiometer) instrument aboard the Aqua Satellite. This dataset is provided by NASA EOSDIS as a single point of entry for this suite of products. The provided access URL is link to EOSDIS's Earthdata Search tool with a pre-populated query that will bring up all products archived by EOSDIS with imagery provided by the MODIS instrument on Aqua.",
-            "title": "Moderate Resolution Imaging Spectroradiometer (MODIS) - Aqua",
+            "landingPage": "https://data.nasa.gov/d/xywd-e9yg",
+            "modified": "2023-01-26",
             "programCode": [
                 "026:001"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MODIS&ff=Map+Imagery&fp=AQUA",
-                    "mediaType": "application/html"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "EOSDIS"
+            },
+            "references": [
+                "https://lpdaac.usgs.gov/dataset_discovery/modis"
             ],
             "spatial": "-180.0, -90.0, 180.0, 90.0",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Moderate Resolution Imaging Spectroradiometer (MODIS) - Aqua"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-MAR-2-REDR-RAW-DATA-V1.0",
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
-                "mars",
-                "2001 mars odyssey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The MARIE (Martian Radiation Environment Experiment), aboard the 2001 Mars Odyssey spacecraft, was launched on April 7, 2001, and arrived at Mars on October 24, 2001.  Data were collected intermittently during the cruise phase, starting in late April and ending in late July.  A problem with MARIE&apos;s onboard computer occurred in early August, and the instrument was turned off until early March 2002, after Odyssey &apos;s mapping orbit had been established.  Data have been collected from that time to the present without major interruption.  Routine minor interruptions of up to 48 hours have occurred during the orbital phase when the instrument&apos;s data is erased from local storage (after having been downloaded).  MARIE is oriented to point in the direction opposite Odyssey&apos;s velocity vector.  Space radiation is for the most part isotropic, so the orientation of Odyssey is usually not critical and references to external coordinate systems are not a part of the data returned by MARIE.  There is one exception to the statement that space radiation is isotropic: During the early stages of solar particle events, there can be directionality in the particle flux.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-mar-2-redr-raw-data-v1.0_xz37-nkjd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "2001 mars odyssey"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-MAR-2-REDR-RAW-DATA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-mar-2-redr-raw-data-v1.0_xz37-nkjd",
-            "description": "The MARIE (Martian Radiation Environment Experiment), aboard the 2001 Mars Odyssey spacecraft, was launched on April 7, 2001, and arrived at Mars on October 24, 2001.  Data were collected intermittently during the cruise phase, starting in late April and ending in late July.  A problem with MARIE&apos;s onboard computer occurred in early August, and the instrument was turned off until early March 2002, after Odyssey &apos;s mapping orbit had been established.  Data have been collected from that time to the present without major interruption.  Routine minor interruptions of up to 48 hours have occurred during the orbital phase when the instrument&apos;s data is erased from local storage (after having been downloaded).  MARIE is oriented to point in the direction opposite Odyssey&apos;s velocity vector.  Space radiation is for the most part isotropic, so the orientation of Odyssey is usually not critical and references to external coordinate systems are not a part of the data returned by MARIE.  There is one exception to the statement that space radiation is isotropic: During the early stages of solar particle events, there can be directionality in the particle flux.",
-            "title": "ODYSSEY MARS MARIE REFORMATTED RAW DATA V1.0",
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
+            "title": "ODYSSEY MARS MARIE REFORMATTED RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1779",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rollinson, C., M. Dietze, J.H. Mathes, J. Steinkamp, T. Hickler, B. Poulter, A.M. Raiho, J. Mclachlan, T. Quaife, Y. Liu, D.J.P. Moore, K. Schaefer, and B. Brooks. 2023. PalEON: Terrestrial Ecosystem Model Drivers for the Northeastern U.S., 0850-2010. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1779",
-            "issued": "2024-01-18",
-            "temporal": "0850-01-01T00:00:00Z/2010-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-22",
-            "keyword": [
-                "paleoclimate indicators",
-                "climate indicators",
-                "ecosystems",
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
-            "identifier": "C2840815089-ORNL_CLOUD",
             "description": "This dataset from the PalEON Ecosystem Model Intercomparison Project (PEMIP) provides harmonized regional environmental and meteorological drivers at a resolution of 0.5 degrees for the North-central and Northeastern U.S. over the time period 0850-01-01 to 2010-12-31. This dataset consists of the regional environmental and meteorological drivers. The environmental drivers include (1) dominant biome type, (2) plant functional type, (3) annual carbon dioxide concentration, (4) monthly carbon dioxide concentration, (5) land use-land cover change, (6) nitrogen concentrations, and (7) soil measurements. The meteorological drivers include (1) incident longwave radiation, (2) incident shortwave radiation, (3) precipitation, (4) surface pressure, (5) specific humidity, (6) air temperature, and (7) wind speed. The PEMIP is a coordinated effort to develop a set of terrestrial ecosystem model simulations with the ability to evaluate high-resolution ecophysiological causes and consequences of forest responses to climatic variability and change over the past millennium.",
-            "graphic-preview-description": "The spatial extent of the dataset.",
-            "title": "PalEON: Terrestrial Ecosystem Model Drivers for the Northeastern U.S., 0850-2010",
-            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/NACP_PalEON_MIP_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1779",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1779",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/nacp/NACP_PalEON_MIP/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/nacp/NACP_PalEON_MIP/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_PalEON_MIP.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_PalEON_MIP.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1779",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1779",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.earthdata.nasa.gov/",
-                    "description": "USE SERVICE API",
                     "@type": "dcat:Distribution",
+                    "description": "USE SERVICE API",
+                    "downloadURL": "https://opendap.earthdata.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_PalEON_MIP/comp/NACP_PalEON_MIP.pdf",
-                    "description": "PalEON: Terrestrial Ecosystem Model Drivers for the Northeastern U.S., 0850-2010: NACP_PalEON_MIP.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "PalEON: Terrestrial Ecosystem Model Drivers for the Northeastern U.S., 0850-2010: NACP_PalEON_MIP.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_PalEON_MIP/comp/NACP_PalEON_MIP.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_PalEON_MIP_Fig1.png",
-                    "description": "The spatial extent of the dataset.",
                     "@type": "dcat:Distribution",
+                    "description": "The spatial extent of the dataset.",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_PalEON_MIP_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "The spatial extent of the dataset.",
+            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/NACP_PalEON_MIP_Fig1.png",
+            "identifier": "C2840815089-ORNL_CLOUD",
+            "issued": "2024-01-18",
+            "keyword": [
+                "paleoclimate indicators",
+                "climate indicators",
+                "ecosystems",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1779",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-100.0 35.0 -60.0 50.0",
+            "temporal": "0850-01-01T00:00:00Z/2010-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PalEON: Terrestrial Ecosystem Model Drivers for the Northeastern U.S., 0850-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-PRL-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains CODMAC\nlevel 3 science data acquired by the DFMS and RTOF ROSINA sensors\nbetween 2014-03-29 and 2014-11-18 during the Prelanding phase of\nthe Rosetta mission to comet 67P/CG. COPS data do not need on-\nground calibration and are included in the level 2 dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-prl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-PRL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-prl-v1.0",
-            "description": "This data set contains CODMAC\nlevel 3 science data acquired by the DFMS and RTOF ROSINA sensors\nbetween 2014-03-29 and 2014-11-18 during the Prelanding phase of\nthe Rosetta mission to comet 67P/CG. COPS data do not need on-\nground calibration and are included in the level 2 dataset.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 3 PRL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 3 PRL V1.0"
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
-                "nasaview",
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
-            "identifier": "NASA-597",
             "description": "Nasaview (3.2.0)",
-            "title": "PDS Software Release Nasaview (3.2.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1660037,20 +1660018,51 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-597",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nasaview",
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
+            "title": "PDS Software Release Nasaview (3.2.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/xz85-cw4y",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "This table lists all of the triggers observed by one or more of the 14 GBM detectors (12 NaI and 2 BGO). Note that there are two Browse catalogs resulting from GBM triggers. All GBM triggers are entered in the Trigger Catalog, but only those triggers classified as bursts are entered in the Fermi GBM Burst Catalog. Thus, a burst will be found in both the Trigger and Burst Catalogs. The Burst Catalog analysis requires human intervention; therefore, GRBs will be entered in the Trigger Catalog before the Burst Catalog. The latency requirements are 1 day for triggers and 3 days for bursts.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigtrig.html",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000229",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "gbm",
                 "lat",
@@ -1660064,65 +1660076,33 @@
                 "astrophysics",
                 "light arcs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/xz85-cw4y",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000229",
-            "description": "This table lists all of the triggers observed by one or more of the 14 GBM detectors (12 NaI and 2 BGO). Note that there are two Browse catalogs resulting from GBM triggers. All GBM triggers are entered in the Trigger Catalog, but only those triggers classified as bursts are entered in the Fermi GBM Burst Catalog. Thus, a burst will be found in both the Trigger and Burst Catalogs. The Burst Catalog analysis requires human intervention; therefore, GRBs will be entered in the Trigger Catalog before the Burst Catalog. The latency requirements are 1 day for triggers and 3 days for bursts.",
-            "title": "FERMIGTRIG - Fermi GBM Trigger Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigtrig.html",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "FERMIGTRIG - Fermi GBM Trigger Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers#GIBSAPIforDevelopers-TiledWebMapService%28TWMS%29",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "tiles",
-                "maps",
-                "digital",
-                "twms",
-                "imagery",
-                "geography"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ryan Boller",
                 "hasEmail": "mailto:ryan.a.boller@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-424",
             "description": "The TWMS specification is a custom extension to the OGS WMS standard developed by the NASA Jet Propulsion Laboratory.  Similar to the OGC WMTS specification, TWMS introduces a 'tiled' approach to imagery requests so that tiles may be pre-generated and cached for fast response.  Unlike WMTS, the TWMS standard retains the usage of requests containing geographic coordinates for imagery.  However, it only responds to a limited number of predefined geographic regions, creating a gridded access pattern.",
-            "title": "GIBS Tiled Web Mapping Service (TWMS)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1660130,124 +1660110,120 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-424",
+            "issued": "2018-06-25",
+            "keyword": [
+                "tiles",
+                "maps",
+                "digital",
+                "twms",
+                "imagery",
+                "geography"
+            ],
+            "landingPage": "https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers#GIBSAPIforDevelopers-TiledWebMapService%28TWMS%29",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GIBS Tiled Web Mapping Service (TWMS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-LEMMS-UNCALIB-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Low Energy Magnetospheric Measurement System (LEMMS) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values for each energy channel for the LEMMS sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI LEMMS archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI LEMMS archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-lemms-uncalib-v1.1_xzdw-85qg",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "jupiter",
                 "cassini-huygens",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-LEMMS-UNCALIB-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-lemms-uncalib-v1.1_xzdw-85qg",
-            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Low Energy Magnetospheric Measurement System (LEMMS) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values for each energy channel for the LEMMS sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI LEMMS archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI LEMMS archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
-            "title": "CASSINI E/J/S/SW MIMI LEMMS SENSOR UNCALIBRATED DATA V1.1",
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
+            "title": "CASSINI E/J/S/SW MIMI LEMMS SENSOR UNCALIBRATED DATA V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-CR2-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the CRUISE 2 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-cr2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-CR2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-cr2-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the CRUISE 2 mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 2 CRUISE 2\n    V1.0",
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
+            "title": "ROSETTA-ORBITER X SREM 2 CRUISE 2\n    V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-09-09",
-            "temporal": "2021-09-09T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coordinates",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "iss",
-                "location",
-                "international",
-                "ephemeris",
-                "coords"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Scott Goodwin",
                 "hasEmail": "mailto:scott.goodwin@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "TOPO"
-            },
-            "identifier": "nasa-iss-data_2021-09-09_xzic-t2zw",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-09-09",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1660370,294 +1660346,320 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-09-09_xzic-t2zw",
+            "issued": "2021-09-09",
+            "keyword": [
+                "coordinates",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "iss",
+                "location",
+                "international",
+                "ephemeris",
+                "coords"
+            ],
+            "landingPage": "https://spotthestation.nasa.gov",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:004"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "TOPO"
+            },
+            "temporal": "2021-09-09T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-09-09"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/1D34X7T1LGGY",
             "citation": "Bjorn Lambrigtser. 2023-06-09. SNDRJ1ML3DRMS. Version 3. Sounder SIPS: JPSS-1 ATMS Level 3 RAMSES2 Standard Gridded Daily V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/1D34X7T1LGGY. https://disc.gsfc.nasa.gov/datacollection/SNDRJ1ML3DRMS_3.html. Digital Science Data.",
-            "issued": "2017-12-11",
-            "temporal": "2017-12-11T00:00:00Z/2024-12-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1109/JSTARS.2017.2670504",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020"
-            ],
-            "keyword": [
-                "earth science",
-                "land surface",
-                "oceans",
-                "ocean temperature",
-                "precipitation",
-                "surface thermal properties",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Bjorn Lambrigtser",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2560858503-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "This level 3 daily product is generated from the RAMSES (Retrieval Algorithm for Microwave Sounders in Earth Science) II algorithm.The RAMSES II algorithm is a microwave only retrieval algorithm using observations from the NOAA-20 (National Oceanic and Atmospheric Administration) also know as Joint Polar Satellite System (JPSS-1) Advanced Technology Microwave Sounder (ATMS) instrument. The ATMS instrument used for this product is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz. The RAMSES II retrieval products contain a variety of geophysical parameters retrieved from ATMS measurements, including profiles of temperature, water in all phases as well as surface properties. The RAMSES II algorithm doesn't have a cloud clearing process and produces all weather retrieval\n\nThis daily one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products with QC values of 0 (best), 1 (good), and 2 (don't use) which are provided for each variable.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRJ1ML3DRMS",
-            "creator": "Bjorn Lambrigtser",
-            "graphic-preview-description": "Sample plot of JPSS-1 (NOAA-20) RAMSES II Level 3 retrieval.",
-            "title": "Sounder SIPS: JPSS-1 ATMS Level 3 RAMSES2 Standard Gridded Daily V3 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1ML3DRMS_3.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1D34X7T1LGGY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1D34X7T1LGGY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1ML3DRMS_3.png",
-                    "description": "Sample plot of JPSS-1 (NOAA-20) RAMSES II Level 3 retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of JPSS-1 (NOAA-20) RAMSES II Level 3 retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1ML3DRMS_3.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1ML3DRMS_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1ML3DRMS_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level3/SNDRJ1ML3DRMS.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level3/SNDRJ1ML3DRMS.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level3/SNDRJ1ML3DRMS.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level3/SNDRJ1ML3DRMS.3/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1ML3DRMS+3",
-                    "description": "Search the Earthdata website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1ML3DRMS+3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/RAMSES.v3.L3.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/RAMSES.v3.L3.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/RAMSESII-ATBD-V1.noprecip.pdf",
-                    "description": "ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/RAMSESII-ATBD-V1.noprecip.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of JPSS-1 (NOAA-20) RAMSES II Level 3 retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1ML3DRMS_3.png",
+            "identifier": "C2560858503-GES_DISC",
+            "issued": "2017-12-11",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "oceans",
+                "ocean temperature",
+                "precipitation",
+                "surface thermal properties",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/1D34X7T1LGGY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/10.1109/JSTARS.2017.2670504",
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRJ1ML3DRMS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-12-11T00:00:00Z/2024-12-16T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: JPSS-1 ATMS Level 3 RAMSES2 Standard Gridded Daily V3 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-PALS0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stephen Riser & Jie Yang. 2019-10-24. SPURS-2 Passive Accoustic Listener (PAL) data from ARGO float deployments during the E. Tropical Pacific field campaign. Version 1.0. SPURS Field Campaign PALS Products. Applied Physics Laboratory, University of Washington, Seattle, WA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-PALS0. http://podaac.jpl.nasa.gov/SPURS. Stephen Riser & Jie Yang, SPURS Data Management PI, Fred Bingham, 2019-10-24, SPURS-2 Passive Accoustic Listener (PAL) data from  ARGO float deployments during the E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-09-18",
-            "temporal": "2016-08-30T15:10:13Z/2018-08-22T01:58:35Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-09-18",
-            "keyword": [
-                "precipitation",
-                "ocean winds",
-                "oceans",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491772341-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Part of the Argo global network of autonomous, self-reporting samplers, Argo floats drift horizontally and move vertically through the water column generally on 10 day cycles, collecting high-quality temperature, conductivity and salinity depth (CTD) profiles from the upper 2000m. Four of the Twenty five floats deployed during SPURS-2 within the campaign spatial domain and time period were additionally equipped with acoustic rain gauges (PAL - Passive Acoustic Listeners). SPURS-2 ARGO-PAL data files are in netCDF/CF-compliant data format and organized per float.  Float identifiers associated with ARGO CTD data are referenced in the metadata of the related PAL files.",
-            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
-            "series-name": "SPURS-2 Passive Accoustic Listener (PAL) data from ARGO float deployments during the E. Tropical Pacific field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Stephen Riser & Jie Yang",
-            "title": "SPURS-2 Passive Accoustic Listener (PAL) data from  ARGO float deployments during the E. Tropical Pacific field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_PALS.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Part of the Argo global network of autonomous, self-reporting samplers, Argo floats drift horizontally and move vertically through the water column generally on 10 day cycles, collecting high-quality temperature, conductivity and salinity depth (CTD) profiles from the upper 2000m. Four of the Twenty five floats deployed during SPURS-2 within the campaign spatial domain and time period were additionally equipped with acoustic rain gauges (PAL - Passive Acoustic Listeners). SPURS-2 ARGO-PAL data files are in netCDF/CF-compliant data format and organized per float.  Float identifiers associated with ARGO CTD data are referenced in the metadata of the related PAL files.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-PALS0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-PALS0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
-                    "description": "Data Submission Report, Instrument Calibration Report, etc",
                     "@type": "dcat:Distribution",
+                    "description": "Data Submission Report, Instrument Calibration Report, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_PALS.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_PALS.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772341-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772341-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772341-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772341-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic data readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic data readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_PALS.jpg",
+            "identifier": "C2491772341-POCLOUD",
+            "issued": "2019-09-18",
+            "keyword": [
+                "precipitation",
+                "ocean winds",
+                "oceans",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-PALS0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-09-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
+            "series-name": "SPURS-2 Passive Accoustic Listener (PAL) data from ARGO float deployments during the E. Tropical Pacific field campaign",
             "spatial": "-129.129 8.861 -116.57 12.106",
+            "temporal": "2016-08-30T15:10:13Z/2018-08-22T01:58:35Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Passive Accoustic Listener (PAL) data from  ARGO float deployments during the E. Tropical Pacific field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-POS-6-GASPRA-FLYBY-TRAJ-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "gaspra",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Orbiter 60 second sampled trajectory data from the Gaspra flyby in Gaspra-centric Solar Ecliptic (GaSE) and RTN coordinates. These data cover the interval 1991-10-29T06:00 to 1991-10-31 00:00.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pos-6-gaspra-flyby-traj-v1.0_xzmj-52yh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "gaspra",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-POS-6-GASPRA-FLYBY-TRAJ-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pos-6-gaspra-flyby-traj-v1.0_xzmj-52yh",
-            "description": "Galileo Orbiter 60 second sampled trajectory data from the Gaspra flyby in Gaspra-centric Solar Ecliptic (GaSE) and RTN coordinates. These data cover the interval 1991-10-29T06:00 to 1991-10-31 00:00.",
-            "title": "GALILEO ORBITER A POS GASPRA FLYBY TRAJ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO ORBITER A POS GASPRA FLYBY TRAJ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HST-J-WFPC2-3-SL9-IMPACT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hst-j-wfpc2-3-sl9-impact-v1.0_xzn8-9zj5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "saturn ring plane crossing 1995",
@@ -1660665,650 +1660667,657 @@
                 "comet sl9/jupiter collision",
                 "sl9"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HST-J-WFPC2-3-SL9-IMPACT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hst-j-wfpc2-3-sl9-impact-v1.0_xzn8-9zj5",
-            "description": "Abstract TBD",
-            "title": "HST J WFPC2 SL9 IMPACT V1.0",
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
+            "title": "HST J WFPC2 SL9 IMPACT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-PCO20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "David Ho. 2020-05-14. SPURS-2 underway surface pCO2, DIC and pH data for the E. Tropical Pacific field campaign R/V Revelle cruises. Version 1.0. SPURS-2 Field Campaign Underway Surface pCO2, DIC, pH Data Products. SOEST, University of Hawaii, 1680 East West Rd, POST 802, Honolulu, HI 96822, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-PCO20. http://podaac.jpl.nasa.gov/SPURS. David Ho, SPURS Data Management PI, Fred Bingham, 2020-05-14, SPURS-2 underway surface pCO2, DIC and pH data for the E. Tropical Pacific field campaign R/V Revelle cruises, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2020-04-21",
-            "temporal": "2017-10-21T20:26:57Z/2017-11-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-04-21",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "ocean chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491772353-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. During both Revelle cruises, continuous measurements of the partial pressure of CO2 (pCO2), dissolved inorganic carbon (DIC), and pH at surface (0m) and 5m depths were made on water pumped continuously from the Salinity Snake and the ship's intake port.  In addition to these measurements, observational data from the salinity snake and thermosalinograph also include water temperature and salinity time series at the same depths. The temporal resolution of the observations range from 3 seconds (pH) to 3 minutes (DIC). All pCO2 and associated underway data comprising this dataset are in netCDF file format with standards compliant metadata.  Due to issues with the quality of the 2016 underway data, only the data file for the 2017 cruise is available.",
-            "release-place": "SOEST, University of Hawaii, 1680 East West Rd, POST 802, Honolulu, HI 96822, USA",
-            "series-name": "SPURS-2 underway surface pCO2, DIC and pH data for the E. Tropical Pacific field campaign R/V Revelle cruises",
-            "graphic-preview-description": "Thumbnail",
             "creator": "David Ho",
-            "title": "SPURS-2 underway surface pCO2, DIC and pH data for the E. Tropical Pacific field campaign R/V Revelle cruises",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_UNDERWAY_pCO2_DIC_pH.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. During both Revelle cruises, continuous measurements of the partial pressure of CO2 (pCO2), dissolved inorganic carbon (DIC), and pH at surface (0m) and 5m depths were made on water pumped continuously from the Salinity Snake and the ship's intake port.  In addition to these measurements, observational data from the salinity snake and thermosalinograph also include water temperature and salinity time series at the same depths. The temporal resolution of the observations range from 3 seconds (pH) to 3 minutes (DIC). All pCO2 and associated underway data comprising this dataset are in netCDF file format with standards compliant metadata.  Due to issues with the quality of the 2016 underway data, only the data file for the 2017 cruise is available.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-PCO20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-PCO20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
-                    "description": "Field Campaign and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_UNDERWAY_pCO2_DIC_pH.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_UNDERWAY_pCO2_DIC_pH.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://spurs.jpl.nasa.gov/",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
+                    "downloadURL": "http://spurs.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
-                    "description": "Data Submission Report, Instrument Calibration Report, etc",
                     "@type": "dcat:Distribution",
+                    "description": "Data Submission Report, Instrument Calibration Report, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772353-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772353-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772353-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772353-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic data readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic data readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_UNDERWAY_pCO2_DIC_pH.jpg",
+            "identifier": "C2491772353-POCLOUD",
+            "issued": "2020-04-21",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-PCO20",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-04-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "SOEST, University of Hawaii, 1680 East West Rd, POST 802, Honolulu, HI 96822, USA",
+            "series-name": "SPURS-2 underway surface pCO2, DIC and pH data for the E. Tropical Pacific field campaign R/V Revelle cruises",
             "spatial": "-125.572 1.383 -121.545 16.411",
+            "temporal": "2017-10-21T20:26:57Z/2017-11-13T00:00:00Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 underway surface pCO2, DIC and pH data for the E. Tropical Pacific field campaign R/V Revelle cruises"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-3-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "lunar crater observation and sensing satellite",
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Calibrated flash mode spectra from the Near Infrared Spectrometer 1 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-3-cal-v1.0_xzpi-hgfv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar crater observation and sensing satellite",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-3-CAL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-3-cal-v1.0_xzpi-hgfv",
-            "description": "Calibrated flash mode spectra from the Near Infrared Spectrometer 1 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 3 CAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 3 CAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1839",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Holmquist, J.R., L.N. Brown, and G.M. Macdonald. 2021. Resilience of Coastal Wetlands to Sea Level Rise, CONUS, 1996-2100. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1839",
-            "issued": "2021-11-30",
-            "temporal": "1996-01-01T00:00:00Z/2100-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "geomorphic landforms/processes",
-                "biosphere",
-                "land surface",
-                "atmospheric/ocean indicators",
-                "coastal processes",
-                "climate indicators",
-                "land use/land cover",
-                "oceans",
-                "tides",
-                "ecosystems"
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
-            "identifier": "C2345893268-ORNL_CLOUD",
             "description": "This dataset provides information about the resilience of tidal wetlands to sea-level rise under three scenarios of global change. With rising seas, regularly inundated tidal wetlands may persist by vertical accretion of sediments (vertical resilience) and/or by migrating inland (lateral resilience), but local and regional conditions constrain these options. This dataset provides a vertical resilience index (VR) for coastal wetlands at 30 m resolution across the continental US predicted for 2100. The VR index was computed for current sea levels, local tidal dynamics, and coastal topography. It was also calculated for future sea levels predicted for 2100 by three IPCC Realized Concentration Pathway (RCP) scenarios: 2.5, 4.5, and 8.5. Moreover, the VR index incorporates estimated rates of sediment accretion. Relevant to lateral resiliency, the data include current and future tidal areas identified by mapping mean higher high water spring tide locations under the RCP scenarios. A shapefile outlining watershed units with tidal wetlands is included along with land cover classes for these areas for 1996 and 2011.",
-            "graphic-preview-description": "Contrasting levels of resilience of tidal marshes to sea-level rise in eastern North Carolina (A) and coastal South Carolina (B), U.S. Lower values of resilience indicate increased vulnerability of these wetlands to impacts of rising sea levels as modeled from RCP 4.5. Source: vertical_resilience_index_30m_2000to2100_RCP4p5.tif",
-            "title": "Resilience of Coastal Wetlands to Sea Level Rise, CONUS, 1996-2100",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Coastal_Wetland_Resilience_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1839",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1839",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Coastal_Wetland_Resilience/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Coastal_Wetland_Resilience/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Coastal_Wetland_Resilience.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Coastal_Wetland_Resilience.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1839",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1839",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Coastal_Wetland_Resilience/comp/CMS_Coastal_Wetland_Resilience.pdf",
-                    "description": "Resilience of Coastal Wetlands to Sea Level Rise, CONUS, 1996-2100: CMS_Coastal_Wetland_Resilience.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Resilience of Coastal Wetlands to Sea Level Rise, CONUS, 1996-2100: CMS_Coastal_Wetland_Resilience.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Coastal_Wetland_Resilience/comp/CMS_Coastal_Wetland_Resilience.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Coastal_Wetland_Resilience_Fig1.jpg",
-                    "description": "Contrasting levels of resilience of tidal marshes to sea-level rise in eastern North Carolina (A) and coastal South Carolina (B), U.S. Lower values of resilience indicate increased vulnerability of these wetlands to impacts of rising sea levels as modeled from RCP 4.5. Source: vertical_resilience_index_30m_2000to2100_RCP4p5.tif",
                     "@type": "dcat:Distribution",
+                    "description": "Contrasting levels of resilience of tidal marshes to sea-level rise in eastern North Carolina (A) and coastal South Carolina (B), U.S. Lower values of resilience indicate increased vulnerability of these wetlands to impacts of rising sea levels as modeled from RCP 4.5. Source: vertical_resilience_index_30m_2000to2100_RCP4p5.tif",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Coastal_Wetland_Resilience_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Contrasting levels of resilience of tidal marshes to sea-level rise in eastern North Carolina (A) and coastal South Carolina (B), U.S. Lower values of resilience indicate increased vulnerability of these wetlands to impacts of rising sea levels as modeled from RCP 4.5. Source: vertical_resilience_index_30m_2000to2100_RCP4p5.tif",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Coastal_Wetland_Resilience_Fig1.jpg",
+            "identifier": "C2345893268-ORNL_CLOUD",
+            "issued": "2021-11-30",
+            "keyword": [
+                "earth science",
+                "geomorphic landforms/processes",
+                "biosphere",
+                "land surface",
+                "atmospheric/ocean indicators",
+                "coastal processes",
+                "climate indicators",
+                "land use/land cover",
+                "oceans",
+                "tides",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1839",
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
             "spatial": "-127.98 22.73 -64.97 49.21",
+            "temporal": "1996-01-01T00:00:00Z/2100-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Resilience of Coastal Wetlands to Sea Level Rise, CONUS, 1996-2100"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRGAB-20J06",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GRACE. 2018-07-05. GRACE Non-Tidal Ocean Geopotential Coefficients JPL (GAB). Version 6.0. GRACE_GAB_L2_GRAV_JPL_RL06. JPL PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, JPL. https://doi.org/10.5067/GRGAB-20J06. https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/. GRACE, JPL, 2018-07-05, GRACE NON-TIDAL OCEAN GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 GAB, https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/.",
-            "issued": "2018-06-11",
-            "temporal": "2002-04-04T00:00:00Z/2017-06-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-06-11",
-            "keyword": [
-                "oceans",
-                "ocean pressure",
-                "gravity/gravitational field",
-                "earth science",
-                "solid earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491772117-POCLOUD",
-            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of geopotential field derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements and a non-tidal oceanic model produced by the Jet Propulsion Laboratory (JPL).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
-            "release-place": "JPL PO.DAAC",
-            "series-name": "GRACE Non-Tidal Ocean Geopotential Coefficients JPL (GAB)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GRACE",
-            "title": "GRACE NON-TIDAL OCEAN GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 GAB",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAB_L2_GRAV_JPL_RL06.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of geopotential field derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements and a non-tidal oceanic model produced by the Jet Propulsion Laboratory (JPL).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGAB-20J06",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGAB-20J06",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
-                    "description": "Product Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product Specification Document",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_jpl_RL06.pdf",
-                    "description": "Release Notes for GRACE L-2 products - version JPL RL-06",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes for GRACE L-2 products - version JPL RL-06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_jpl_RL06.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAB_L2_GRAV_JPL_RL06.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAB_L2_GRAV_JPL_RL06.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-UserHandbook_v4.0.pdf",
-                    "description": "Level-2 Gravity Field Product User Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Level-2 Gravity Field Product User Handbook",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-UserHandbook_v4.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-JPL_ProcStds_v6.0.pdf",
-                    "description": "JPL Level-2 Processing Standards Document For Level-2 Product Release 06",
                     "@type": "dcat:Distribution",
+                    "description": "JPL Level-2 Processing Standards Document For Level-2 Product Release 06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-JPL_ProcStds_v6.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "GRACE Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE Mission Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/JPL/RL06/README.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/JPL/RL06/README.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772117-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772117-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772117-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772117-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAB_L2_GRAV_JPL_RL06.jpg",
+            "identifier": "C2491772117-POCLOUD",
+            "issued": "2018-06-11",
+            "keyword": [
+                "oceans",
+                "ocean pressure",
+                "gravity/gravitational field",
+                "earth science",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRGAB-20J06",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-06-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL PO.DAAC",
+            "series-name": "GRACE Non-Tidal Ocean Geopotential Coefficients JPL (GAB)",
             "spatial": "-180.0 -88.0 180.0 88.0",
+            "temporal": "2002-04-04T00:00:00Z/2017-06-30T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRACE NON-TIDAL OCEAN GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 GAB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-LAUNCH-V3.0",
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
-                "dust",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    post-launch checkout                                                   mission phase.  This is VERSION 3.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-launch-v3.0_xzxa-geu7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-LAUNCH-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-launch-v3.0_xzxa-geu7",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    post-launch checkout                                                   mission phase.  This is VERSION 3.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SDC POST-LAUNCH CHECKOUT                                                \n      CALIBRATED V3.0",
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
+            "title": "NEW HORIZONS                            \n      SDC POST-LAUNCH CHECKOUT                                                \n      CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-GAS-5-SKY-MAPS-V1.0",
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
-                "jupiter",
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Ulysses interstellar neutral gas (GAS) experiment sky maps of the count rates of interstellar helium particles (in the NG-mode) or from celestial UV-intensities (UV-mode).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-gas-5-sky-maps-v1.0_xzxi-zez4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-GAS-5-SKY-MAPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-gas-5-sky-maps-v1.0_xzxi-zez4",
-            "description": "Ulysses interstellar neutral gas (GAS) experiment sky maps of the count rates of interstellar helium particles (in the NG-mode) or from celestial UV-intensities (UV-mode).",
-            "title": "ULY JUPITER INTERSTELLAR NEUTRAL-GAS\n                                        EXPERIMENT SKY MAPS",
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
+            "title": "ULY JUPITER INTERSTELLAR NEUTRAL-GAS\n                                        EXPERIMENT SKY MAPS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-5-VIRS-DAP-V1.0",
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
-                "mercury",
-                "messenger"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS derived analysis product, also known as the DAP. The DAP is a 500 meter per pixel mosaic map of 1 wavelength (750 nm) of VIRS spectral data for footprints covering the planet Mercury. Data products are derived from science data collected by the VIRS detector during orbital operations of Mercury.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-5-virs-dap-v1.0_xzyi-v7e4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mercury",
+                "messenger"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-5-VIRS-DAP-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-5-virs-dap-v1.0_xzyi-v7e4",
-            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS derived analysis product, also known as the DAP. The DAP is a 500 meter per pixel mosaic map of 1 wavelength (750 nm) of VIRS spectral data for footprints covering the planet Mercury. Data products are derived from science data collected by the VIRS detector during orbital operations of Mercury.",
-            "title": "MESSENGER E/V/H MASCS 5 VIRS DERIVED ANALYSIS DATA V1.0",
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
+            "title": "MESSENGER E/V/H MASCS 5 VIRS DERIVED ANALYSIS DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0545.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs InSAR-Based Ice Velocity of the Amundsen Sea Embayment, Antarctica V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0545.001.",
-            "issued": "1996-01-01",
-            "temporal": "1996-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-12-31",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "snow/ice"
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
-            "identifier": "C1353062858-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) Program, provides high-resolution, digital mosaics of ice motion in the Amundsen Sea Embayment (ASE) and West Antarctica, including the Pine Island, Thwaites, Haynes, Pope, Smith, and Kohler glaciers. The mosaics were assembled from interferometric synthetic-aperture radar (InSAR) data acquired in 1996, 2000, 2002, and 2006-2012 by various satellites.\n\nSee <a href=\"https://nsidc.org/data/measures/aiv\">Antarctic Ice Sheet Velocity and Mapping Data</a> for related data.",
-            "title": "MEaSUREs InSAR-Based Ice Velocity of the Amundsen Sea Embayment, Antarctica V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FCRYOSPHERE%2Fnsidc-0545.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FCRYOSPHERE%2Fnsidc-0545.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0545.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0545.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1353062858-NSIDC_ECS&q=nsidc-0545&m=-58.20364688829667%21-90.3%210%212%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1353062858-NSIDC_ECS&q=nsidc-0545&m=-58.20364688829667%21-90.3%210%212%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0545/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0545/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0545.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0545.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1353062858-NSIDC_ECS&q=nsidc-0545&m=-58.20364688829667%21-90.3%210%212%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1353062858-NSIDC_ECS&q=nsidc-0545&m=-58.20364688829667%21-90.3%210%212%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0545/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0545/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0545.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0545.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1353062858-NSIDC_ECS&q=nsidc-0545&m=-58.20364688829667%21-90.3%210%212%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1353062858-NSIDC_ECS&q=nsidc-0545&m=-58.20364688829667%21-90.3%210%212%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0545/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0545/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0545.001",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0545.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0545.001",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0545.001",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1353062858-NSIDC_ECS",
+            "issued": "1996-01-01",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/CRYOSPHERE/nsidc-0545.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-127.3826 -80.4614 82.8345 -71.9876",
+            "temporal": "1996-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs InSAR-Based Ice Velocity of the Amundsen Sea Embayment, Antarctica V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://aeronet.gsfc.nasa.gov/cgi-bin/combined_data_access_new",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://aeronet.gsfc.nasa.gov/new_web/data_usage.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "description": "The aerosol optical depth processing includes the spectral de-convolution algorithm (SDA) described in O'Neill et al. (2003). This algorithm yields fine (sub-micron) and coarse (super-micron) aerosol optical depths at a standard wavelength of 500 nm (from which FMF*, the fraction of fine mode to total aerosol optical depth can be computed).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/AOT_Level2_Monthly.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
             ],
+            "identifier": "NASA-0000008__2",
+            "issued": "2018-06-26",
             "keyword": [
                 "aerosols",
                 "earth science",
@@ -1661318,642 +1661327,611 @@
                 "clouds",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brent Holben",
-                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
-            },
+            "landingPage": "http://aeronet.gsfc.nasa.gov/cgi-bin/combined_data_access_new",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000008__2",
-            "description": "The aerosol optical depth processing includes the spectral de-convolution algorithm (SDA) described in O'Neill et al. (2003). This algorithm yields fine (sub-micron) and coarse (super-micron) aerosol optical depths at a standard wavelength of 500 nm (from which FMF*, the fraction of fine mode to total aerosol optical depth can be computed).",
-            "title": "AERONET Level 2.0 AOD",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/AOT_Level2_Monthly.tar.gz",
-                    "mediaType": "application/x-tar"
-                }
+            "references": [
+                "http://aeronet.gsfc.nasa.gov/new_web/data_usage.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "AERONET Level 2.0 AOD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-PRL-MTP009-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Prelanding Phase from 24th Oct 2014 to 21st Nov 2014 before reaching target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-prl-mtp009-v1.0_xzzg-zesn",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-PRL-MTP009-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-prl-mtp009-v1.0_xzzg-zesn",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Prelanding Phase from 24th Oct 2014 to 21st Nov 2014 before reaching target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 PRELANDING MTP009 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 PRELANDING MTP009 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2232",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huemmrich, K.F., and J.A. Gamon. 2023. Spectral Reflectance and Ancillary Data, Tundra Transect, North Slope, AK, 2000-2022. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2232",
-            "issued": "2024-01-18",
-            "temporal": "2000-06-30T00:00:00Z/2022-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-22",
-            "keyword": [
-                "soils",
-                "earth science",
-                "biosphere",
-                "ecosystems",
-                "infrared wavelengths",
-                "vegetation",
-                "land surface",
-                "spectral/engineering"
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
-            "identifier": "C2840820936-ORNL_CLOUD",
             "description": "This dataset provides visible-near infrared spectral reflectance, descriptions of vegetation cover, surface temperature, the total fraction of absorbed photosynthetically active radiation (fAPAR, 2001 only), permafrost active layer depth, elevation, and soil temperature at 5 cm depth. Measurements were made at every meter along a 100-m transect aligned mainly in an east-west direction, located approximately 300 m southeast of the National Oceanic and Atmospheric Administration (NOAA) Global Monitoring Laboratory (GML) baseline observatory near Utqiagvik, Alaska. Reflectance measurements were collected at nearly weekly intervals through the growing seasons of 2000 to 2002 to describe characteristics of green-up, peak growth, and senescence. Reflectance measurements were also collected once near peak growth in 2022. Ancillary measurements were collected at intervals through the 2001 and 2002 growing seasons.",
-            "graphic-preview-description": "Photograph of field plot on August 8, 2001, located 73 m from western end of transect. Source: 010811METER73.JPG.",
-            "title": "Spectral Reflectance and Ancillary Data, Tundra Transect, North Slope, AK, 2000-2022",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/TundraTransect_VegRefl_Soil_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2232",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2232",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/TundraTransect_VegRefl_Soil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/TundraTransect_VegRefl_Soil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/TundraTransect_VegRefl_Soil.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/TundraTransect_VegRefl_Soil.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2232",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2232",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/TundraTransect_VegRefl_Soil/comp/TundraTransect_VegRefl_Soil.pdf",
-                    "description": "Spectral Reflectance and Ancillary Data, Tundra Transect, North Slope, AK, 2000-2022: TundraTransect_VegRefl_Soil.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Spectral Reflectance and Ancillary Data, Tundra Transect, North Slope, AK, 2000-2022: TundraTransect_VegRefl_Soil.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/TundraTransect_VegRefl_Soil/comp/TundraTransect_VegRefl_Soil.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/TundraTransect_VegRefl_Soil_Fig1.png",
-                    "description": "Photograph of field plot on August 8, 2001, located 73 m from western end of transect. Source: 010811METER73.JPG.",
                     "@type": "dcat:Distribution",
+                    "description": "Photograph of field plot on August 8, 2001, located 73 m from western end of transect. Source: 010811METER73.JPG.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/TundraTransect_VegRefl_Soil_Fig1.png",
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
+            "graphic-preview-description": "Photograph of field plot on August 8, 2001, located 73 m from western end of transect. Source: 010811METER73.JPG.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/TundraTransect_VegRefl_Soil_Fig1.png",
+            "identifier": "C2840820936-ORNL_CLOUD",
+            "issued": "2024-01-18",
+            "keyword": [
+                "soils",
+                "earth science",
+                "biosphere",
+                "ecosystems",
+                "infrared wavelengths",
+                "vegetation",
+                "land surface",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2232",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "71.32 -156.6",
+            "temporal": "2000-06-30T00:00:00Z/2022-08-08T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Spectral Reflectance and Ancillary Data, Tundra Transect, North Slope, AK, 2000-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD09.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. MODIS/Aqua Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYD09.061. https://doi.org/10.5067/MODIS/MYD09.061.",
-            "issued": "2002-07-04",
-            "temporal": "2002-07-04T00:45:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "land surface",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASAD ULLAH",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1713215948-LAADS",
-            "description": "The MODIS/Aqua Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km (MYD09) product is computed from the MODIS Level 1B land bands 1, 2, 3, 4, 5, 6, and 7 (centered at 648 nm, 858 nm, 470 nm, 555 nm, 1240 nm, 1640 nm, and 2130 nm, respectively). The product is an estimate of the surface spectral reflectance for each band as it would have been measured at ground level if there were no atmospheric scattering or absorption. The surface-reflectance product is the input for product generation for several land products: vegetation Indices (VIs), Bidirectional Reflectance Distribution Function (BRDF), thermal anomaly, snow/ice, and Fraction of Photosynthetically Active Radiation/Leaf Area Index (FPAR/LAI).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, and 1km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km (MYD09) product is computed from the MODIS Level 1B land bands 1, 2, 3, 4, 5, 6, and 7 (centered at 648 nm, 858 nm, 470 nm, 555 nm, 1240 nm, 1640 nm, and 2130 nm, respectively). The product is an estimate of the surface spectral reflectance for each band as it would have been measured at ground level if there were no atmospheric scattering or absorption. The surface-reflectance product is the input for product generation for several land products: vegetation Indices (VIs), Bidirectional Reflectance Distribution Function (BRDF), thermal anomaly, snow/ice, and Fraction of Photosynthetically Active Radiation/Leaf Area Index (FPAR/LAI).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD09.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD09.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/306/MOD09_User_Guide_V6.pdf",
-                    "description": "MODIS Surface Reflectance Product User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Surface Reflectance Product User\u2019s Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/306/MOD09_User_Guide_V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf",
-                    "description": "MODIS Atmosphere Monthly Global product combined user's guide and ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Atmosphere Monthly Global product combined user's guide and ATBD",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYD09--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYD09--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD09/",
-                    "description": "Direct access to MOD09 C61 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD09 C61 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD09/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYD09/contents.html",
-                    "description": "Direct link to Collection's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct link to Collection's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYD09/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1713215948-LAADS",
+            "issued": "2002-07-04",
+            "keyword": [
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD09.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:45:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, and 1km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/599/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-06-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Schweiker",
                 "hasEmail": "mailto:kevin.schweiker@honeywell.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_599",
             "description": "The following SAL model is an abstraction of a module that implements a fault-tolerant mid-value select on asynchronously produced inputs. This is part of a larger system that has both discrete and continuous dynamics, Our goal is to model the full system using Hybrid SAL and we have adapted the timed relational abstraction techique supported by Hybrid SAL to abstract asynchronous sampling of continous signals. This approach will be fully automated in future releases of Hybrid SAL.\r\n\r\nThe following model (05/14/2012) shows the resulting abstraction, for the aysnchronous mid-value select module and includes proofs of various properties.",
-            "title": "Asynchronous Mid-Value Select in Hybrid SAL",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/MVS_2.sal",
-                    "description": "Hybrid SAL model of Mid-Value Select Module",
                     "@type": "dcat:Distribution",
+                    "description": "Hybrid SAL model of Mid-Value Select Module",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/MVS_2.sal",
+                    "mediaType": "application/octet-stream",
                     "title": "MVS.sal"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_599",
+            "issued": "2012-06-11",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/599/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Asynchronous Mid-Value Select in Hybrid SAL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA320",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRH3STM. Version 006. AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA320. https://disc.gsfc.nasa.gov/datacollection/AIRH3STM_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2003-03-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-01",
-            "keyword": [
-                "surface radiative properties",
-                "surface thermal properties",
-                "ocean temperature",
-                "oceans",
-                "land surface",
-                "earth science",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517238-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. This product is similar to AIRX3STM. However, it contains science retrievals that use the Humidity Sounder for Brazil (HSB). Because the HSB instrument lived only from September 2002 through January 2003 when it terminally failed, the data set covers these five months only. The AIRS Level 3 Monthly Gridded Retrieval Product contains standard retrieval means, standard deviations and input counts. Each file covers a calendar month. The mean values are simply the arithmetic means of the daily products, weighted by the number of input counts for each day in that grid box. The geophysical parameters have been averaged and binned into 1 x 1 grid cells, from -180.0 to +180.0 deg longitude and from -90.0 to +90.0 deg latitude. For each grid map of 4-byte floating-point mean values there is a corresponding 4-byte floating-point map of standard deviation and a 2-byte integer grid map of counts. The counts map provides the user with the number of points per bin that were included in the mean and can be used to generate custom multi-day maps from the daily gridded products. The thermodynamic parameters are: Skin Temperature (land and sea surface), Air Temperature at the surface, Profiles of Air Temperature and Water Vapor, Tropopause Characteristics, Column Precipitable Water, Cloud Amount/Frequency, Cloud Height, Cloud Top Pressure, Cloud Top Temperature, Reflectance, Emissivity, Surface Pressure, Cloud Vertical Distribution. The trace gases parameters are: Total Amounts and Vertical Profiles of Carbon Monoxide, Methane, and Ozone. The actual names of the variables in the data files should be inferred from the Processing File Description document.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRH3STM",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "title": "AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3STM) at GES DISC",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3STM_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA320",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA320",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3STM_006.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3STM_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3STM_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3STM_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3STM.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3STM.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3STM.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3STM.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3STM+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3STM+006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
-                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument, algorithms, and other AIRS-related activities can be found.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument, algorithms, and other AIRS-related activities can be found.",
+                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=AIRS+Documentation",
-                    "description": "AIRS Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Documentation Page",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=AIRS+Documentation",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRS_V6.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRS_V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/V6_Released_Processing_Files_Description.pdf",
-                    "description": "AIRS Version 6 Processing Files Description Document.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Version 6 Processing Files Description Document.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/V6_Released_Processing_Files_Description.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (With HSB)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3STM_006.png",
+            "identifier": "C1238517238-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "surface radiative properties",
+                "surface thermal properties",
+                "ocean temperature",
+                "oceans",
+                "land surface",
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA320",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRH3STM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2003-03-01T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3STM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-IRPBT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "2001 mars odyssey",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The THEMIS IR-PBT data set contains the spatially registered, infrared brightness temperature images derived from the projected radiance (IR-GEO) products. Each image header includes basic parameters describing the observation and image specific details of processing.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-irpbt-v2.0_y2bt-zwzh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "2001 mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-IRPBT-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-irpbt-v2.0_y2bt-zwzh",
-            "description": "The THEMIS IR-PBT data set contains the spatially registered, infrared brightness temperature images derived from the projected radiance (IR-GEO) products. Each image header includes basic parameters describing the observation and image specific details of processing.",
-            "title": "ODYSSEY THEMIS IR PBT V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ODYSSEY THEMIS IR PBT V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/GULF_OF_MAINE_OPTICS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/GULF_OF_MAINE_OPTICS/DATA001.",
-            "issued": "1979-08-22",
-            "temporal": "1979-08-22T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "ocean optics",
-                "earth science",
-                "oceans",
-                "ocean chemistry",
-                "salinity/density"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360359-OB_DAAC",
             "description": "Measurements of optics from the Gulf of Maine region spanning 1979 to 1996.",
-            "title": "Gulf of Maine optical measurements from 1933 to 1991",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGULF_OF_MAINE_OPTICS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGULF_OF_MAINE_OPTICS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Gulf_of_Maine_Optics/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Gulf_of_Maine_Optics/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360359-OB_DAAC",
+            "issued": "1979-08-22",
+            "keyword": [
+                "ocean temperature",
+                "ocean optics",
+                "earth science",
+                "oceans",
+                "ocean chemistry",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/GULF_OF_MAINE_OPTICS/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1979-08-22T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gulf of Maine optical measurements from 1933 to 1991"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V1.0",
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
-                "asteroid",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes names, designations, and discovery circumstances for the numbered asteroids, sorted in order of catalog number. A similar file sorted in alphabetic order by name is also available in the Small Bodies Node asteroid data archive.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v1.0_y2e2-7xvf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v1.0_y2e2-7xvf",
-            "description": "This data set includes names, designations, and discovery circumstances for the numbered asteroids, sorted in order of catalog number. A similar file sorted in alphabetic order by name is also available in the Small Bodies Node asteroid data archive.",
-            "title": "ASTEROID NAMES AND DISCOVERY V1.0",
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
+            "title": "ASTEROID NAMES AND DISCOVERY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-HFT-3-RDR-FLUX-HIRES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "ulysses",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains ion flux data recorded by the COSPIN High Flux Telescope (HFT) during the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-hft-3-rdr-flux-hires-v1.0_y2ex-g3ru",
+            "issued": "2018-06-26",
+            "keyword": [
+                "ulysses",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-HFT-3-RDR-FLUX-HIRES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-hft-3-rdr-flux-hires-v1.0_y2ex-g3ru",
-            "description": "This data set contains ion flux data recorded by the COSPIN High Flux Telescope (HFT) during the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-18.",
-            "title": "ULY JUP COSPIN HIGH FLUX TELESCOPE HIGH RES. ION FLUX",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULY JUP COSPIN HIGH FLUX TELESCOPE HIGH RES. ION FLUX"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA308",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gille, John and Gray, Lesley J.. 2013-08-19. H3ZFCHNO3. Version 007. HIRDLS/Aura Level 3 Nitric Acid (HNO3) 1deg Lat Zonal Fourier Coefficients V007. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/HIRDLS/DATA308. https://disc.gsfc.nasa.gov/datacollection/H3ZFCHNO3_007.html. Digital Science Data.",
-            "issued": "2013-05-31",
-            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-31",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOHN GILLE",
                 "hasEmail": "mailto:gille@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1251100929-GES_DISC",
-            "description": "The \"HIRDLS/Aura Level 3 Nitric Acid (HNO3) Zonal Fourier Coefficients\" version 7 data product (H3ZFCHNO3) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 215 to 5.1 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "H3ZFCHNO3",
             "creator": "Gille, John and Gray, Lesley J.",
-            "title": "HIRDLS/Aura Level 3 Nitric Acid (HNO3) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCHNO3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFCHNO3_007.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The \"HIRDLS/Aura Level 3 Nitric Acid (HNO3) Zonal Fourier Coefficients\" version 7 data product (H3ZFCHNO3) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 215 to 5.1 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA308",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA308",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1661963,411 +1661941,411 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFCHNO3_007.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFCHNO3_007.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFCHNO3.007/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFCHNO3.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFCHNO3.007/HIRDLS-Aura_L3ZFCHNO3_v07-00-20-c02_2005d022-2008d077.he5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFCHNO3.007/HIRDLS-Aura_L3ZFCHNO3_v07-00-20-c02_2005d022-2008d077.he5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFCHNO3_007",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFCHNO3_007",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.5_Product_Quality/HIRDLS-DQD_V7.pdf",
-                    "description": "README and Data Quality document",
                     "@type": "dcat:Distribution",
+                    "description": "README and Data Quality document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.5_Product_Quality/HIRDLS-DQD_V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFCHNO3_007.png",
+            "identifier": "C1251100929-GES_DISC",
+            "issued": "2013-05-31",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA308",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "H3ZFCHNO3",
             "spatial": "-180.0 -64.0 180.0 80.0",
+            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIRDLS/Aura Level 3 Nitric Acid (HNO3) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCHNO3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC4-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 4 mission phase, which took place between 2015-10-22 and 2015-12-31.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc4-v2.0_y2fn-ktk5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC4-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc4-v2.0_y2fn-ktk5",
-            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 4 mission phase, which took place between 2015-10-22 and 2015-12-31.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC4 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC4 V2.0"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL22.003",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "ATLAS/ICESat-2 L3B Mean Inland Surface Water Data V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL22.003.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-14T00:00:00Z/2024-10-28T00:00:00Z",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-31",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "surface water"
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "ATLAS/ICESat-2 L3B Mean Inland Surface Water Data V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL22.003.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSIDC Services",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C2761722214-NSIDC_CPRD",
             "description": "ATL22 is a derivative of the continuous Level 3A ATL13 Along Track Inland Surface Water Data product. ATL13 contains the high-resolution, along-track inland water surface profiles derived from analysis of the geolocated photon clouds from the ATL03 product. Starting from ATL13, ATL22 computes the mean surface water quantities with no additional photon analysis. The two data products, ATL22 and ATL13, can be used in conjunction as they include the same orbit and water body nomenclature independent from version numbers.",
-            "title": "ATLAS/ICESat-2 L3B Mean Inland Surface Water Data V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL22.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL22.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL22+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL22+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2761722214-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2761722214-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL22.003",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL22.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL22.003",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL22.003",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2761722214-NSIDC_CPRD",
+            "issued": "2018-10-14",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL22.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -88.0 180.0 88.0",
+            "temporal": "2018-10-14T00:00:00Z/2024-10-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3B Mean Inland Surface Water Data V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSRU/AU_OCEAN_NRT_R01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kummerow, C., R. Ferraro, and D. Duncan. 2020. NRT AMSR2 Unified L2B Global Swath Ocean Products. [Indicate subset used]. Boulder, Colorado USA. NASA National Snow and Ice Data Center Distributed Active Archive Center. doi: http://dx.doi.org/10.5067/AMSRU/AU_OCEAN_NRT_R01. [Date Accessed].",
-            "issued": "2020-06-09",
-            "temporal": "2020-06-01T08:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-09",
-            "keyword": [
-                "ocean temperature",
-                "atmospheric winds",
-                "earth science",
-                "oceans",
-                "atmosphere",
-                "atmospheric water vapor",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-ghrc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1841273046-LANCEAMSR2",
             "description": "The Advanced Microwave Scanning Radiometer 2 (AMSR2) instrument on the Global Change Observation Mission - Water 1 (GCOM-W1) provides global passive microwave measurements of terrestrial, oceanic, and atmospheric parameters for the investigation of global water and energy cycles.  Near real-time (NRT) products are generated within 3 hours of the last observations in the file, by the Land Atmosphere Near real-time Capability for EOS (LANCE) at the AMSR Science Investigator-led Processing System (AMSR SIPS), which is collocated with the Global Hydrology Resource Center (GHRC) DAAC.  The GCOM-W1 NRT AMSR2 Unified L2B Global Swath Ocean Products is a swath product containing global sea surface temperature over ocean, wind speed over ocean, water vapor over ocean and cloud liquid water over ocean, using resampled NRT Level-1R data provided by JAXA.  This is the same algorithm that generates the corresponding standard science products in the AMSR SIPS. The NRT products are generated in HDF-EOS-5 augmented with netCDF-4/CF metadata and are available via HTTPS from the EOSDIS LANCE system at https://lance.nsstc.nasa.gov/amsr2-science/data/level2/ocean/.  If data latency is not a primary concern, please consider using science quality products.  Science products are created using the best available ancillary, calibration and ephemeris information.  Science quality products are an internally consistent, well-calibrated record of the Earth's geophysical properties to support science.  The AMSR SIPS produces AMSR2 standard science quality data products, and they are available at the NSIDC DAAC.",
-            "graphic-preview-description": "Sample browse image",
-            "title": "NRT AMSR2 Unified L2B Global Swath Ocean Products V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_Ocean.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSRU%2FAU_OCEAN_NRT_R01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSRU%2FAU_OCEAN_NRT_R01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lance.nsstc.nasa.gov/amsr2-science/data/level2/ocean/R01/",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://lance.nsstc.nasa.gov/amsr2-science/data/level2/ocean/R01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lance.itsc.uah.edu/amsr2-science/data/level2/ocean/R01/",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://lance.itsc.uah.edu/amsr2-science/data/level2/ocean/R01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LANCE"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?l=AMSRU2_Wind_Speed_Night%2CAMSRU2_Wind_Speed_Day%2CAMSRU2_Cloud_Liquid_Water_Night%2CAMSRU2_Cloud_Liquid_Water_Day%2CAMSRU2_Total_Precipitable_Water_Night%2CAMSRU2_Total_Precipitable_Water_Day%2CCoastlines%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "Interactively browse imagery in EOSDIS Worldview",
                     "@type": "dcat:Distribution",
+                    "description": "Interactively browse imagery in EOSDIS Worldview",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?l=AMSRU2_Wind_Speed_Night%2CAMSRU2_Wind_Speed_Day%2CAMSRU2_Cloud_Liquid_Water_Night%2CAMSRU2_Cloud_Liquid_Water_Day%2CAMSRU2_Total_Precipitable_Water_Night%2CAMSRU2_Total_Precipitable_Water_Day%2CCoastlines%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/all-data-recipes#drp-formatcon",
-                    "description": "Data Format Conversion Recipes",
                     "@type": "dcat:Distribution",
+                    "description": "Data Format Conversion Recipes",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/all-data-recipes#drp-formatcon",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_Ocean.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_Ocean.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse image",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_Ocean.png",
+            "identifier": "C1841273046-LANCEAMSR2",
+            "issued": "2020-06-09",
+            "keyword": [
+                "ocean temperature",
+                "atmospheric winds",
+                "earth science",
+                "oceans",
+                "atmosphere",
+                "atmospheric water vapor",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSRU/AU_OCEAN_NRT_R01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
             "spatial": "-180.0 -89.0 180.0 89.0",
+            "temporal": "2020-06-01T08:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NRT AMSR2 Unified L2B Global Swath Ocean Products V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1730",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hanisco, T.F., R.A. Hannun, J.M. St.Clair, and G.M. Wolfe. 2019. ATom: L2 Measurements of In Situ Airborne Formaldehyde (ISAF). ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1730",
-            "issued": "2021-06-28",
-            "temporal": "2016-07-29T14:33:18Z/2018-05-07T06:29:50Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "air quality",
-                "atmosphere"
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
-            "identifier": "C2676907210-ORNL_CLOUD",
             "description": "This dataset provides the atmospheric volume mixing ratio of formaldehyde measured during airborne campaigns conducted by NASA's Atmospheric Tomography (ATom) mission. ATom deploys an extensive gas and aerosol payload on the NASA DC-8 aircraft for systematic, global-scale sampling of the atmosphere, profiling continuously from 0.2 to 12 km altitude. Flights occurred in each of 4 seasons from 2016 to 2018. The NASA In Situ Airborne Formaldehyde (ISAF) instrument, based at the Goddard Space Flight Center, measures formaldehyde on high-altitude NASA aircraft. The instrument uses laser-induced fluorescence (LIF) to obtain the high detection sensitivity needed to detect formaldehyde in the upper troposphere and lower stratosphere where abundances are 10 parts per trillion. LIF also enables a fast time response needed to measure the abundance of formaldehyde in the finely structured outflow of convective storms. These measurements of formaldehyde will be used elucidate mechanisms of convective transport and quantify the effects of boundary layer pollutants on the ozone photochemistry and cloud microphysics of the upper atmosphere.",
-            "graphic-preview-description": "Measurements of atmospheric formaldehyde concentrations from the ISAF instrument during ATom-3 flights in 2017.",
-            "title": "ATom: L2 Measurements of In Situ Airborne Formaldehyde (ISAF)",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_ISAF_Instrument_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1730",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1730",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_ISAF_Instrument_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_ISAF_Instrument_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_ISAF_Instrument_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_ISAF_Instrument_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1730",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1730",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_ISAF_Instrument_Data/comp/ATom_ISAF_Instrument_Data.pdf",
-                    "description": "ATom: L2 Measurements of In Situ Airborne Formaldehyde (ISAF): ATom_ISAF_Instrument_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: L2 Measurements of In Situ Airborne Formaldehyde (ISAF): ATom_ISAF_Instrument_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_ISAF_Instrument_Data/comp/ATom_ISAF_Instrument_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_ISAF_Instrument_Data_Fig1.png",
-                    "description": "Measurements of atmospheric formaldehyde concentrations from the ISAF instrument during ATom-3 flights in 2017.",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of atmospheric formaldehyde concentrations from the ISAF instrument during ATom-3 flights in 2017.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_ISAF_Instrument_Data_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/campaign/",
-                    "description": "ATom campaign page",
                     "@type": "dcat:Distribution",
+                    "description": "ATom campaign page",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/campaign/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Measurements of atmospheric formaldehyde concentrations from the ISAF instrument during ATom-3 flights in 2017.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_ISAF_Instrument_Data_Fig1.png",
+            "identifier": "C2676907210-ORNL_CLOUD",
+            "issued": "2021-06-28",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1730",
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
             "spatial": "-180.0 -80.12 180.0 80.52",
+            "temporal": "2016-07-29T14:33:18Z/2018-05-07T06:29:50Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: L2 Measurements of In Situ Airborne Formaldehyde (ISAF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2501",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Livesey, N. and Read, W.. 2020-06-11. ML2BRO. Version 005. MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2501. https://disc.gsfc.nasa.gov/datacollection/ML2BRO_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATHANIEL LIVESEY",
                 "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1729925083-GES_DISC",
-            "description": "ML2BRO is the EOS Aura Microwave Limb Sounder (MLS) standard product for bromine monoxide derived from radiances measured by the 640 GHz radiometer. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 10 and 3.16 hPa, and the vertical resolution is about 5.5 km (6 km at 3.16 hPa). Users of the ML2BRO data product should read section 3.2 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2BRO",
             "creator": "Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V005 (ML2BRO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2BRO_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2BRO is the EOS Aura Microwave Limb Sounder (MLS) standard product for bromine monoxide derived from radiances measured by the 640 GHz radiometer. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 10 and 3.16 hPa, and the vertical resolution is about 5.5 km (6 km at 3.16 hPa). Users of the ML2BRO data product should read section 3.2 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2501",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2501",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1662377,222 +1662355,218 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2BRO_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2BRO_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2BRO.005/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2BRO.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2BRO.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2BRO.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2BRO_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2BRO_005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
-                    "description": "Data Quality and Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality and Description Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/publications.php",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/forms/reguser.php",
-                    "description": "Users are encouraged to register with the MLS science team to obtain updates and information about this data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Users are encouraged to register with the MLS science team to obtain updates and information about this data product.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/forms/reguser.php",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/eos_algorithm_atbd.pdf",
-                    "description": "EOS MLS Retrieval Process Algorithm Theoretical Basis",
                     "@type": "dcat:Distribution",
+                    "description": "EOS MLS Retrieval Process Algorithm Theoretical Basis",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/eos_algorithm_atbd.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/",
-                    "description": "MLS Science Team Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "MLS Science Team Home Page.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2BRO_005.png",
+            "identifier": "C1729925083-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2501",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML2BRO",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V005 (ML2BRO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2015-05-28. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/ATTREX/0001. https://asdc.larc.nasa.gov/project/ATTREX.",
-            "issued": "2015-01-30",
-            "temporal": "2011-10-01T00:00:00Z/2013-03-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-02",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "altitude",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1536056465-LARC_ASDC",
             "description": "ATTREX-Aircraft_RemoteSensing_Temperature_Measurements are remotely sensed temperature profiles collected onboard the Global Hawk Unihabited Aerial System (UAS) during the Airborne Tropical TRopopause EXperiment (ATTREX) campaign. This collection consists of remotely sensed temperature profiles collected by the Microwave Temperature Profiler (MTP) during the 2011 and 2013 deployments over California, and 2014 deployment over Guam. Data collection is complete.\nEven though it is typically found in low concentrations, stratospheric water vapor has large impacts on the Earth\u2019s climate and energy budget. Studies have suggested that even relatively small changes in stratospheric humidity may have significant climate impacts and future changes in stratospheric humidity and ozone concentration in response to a changing climate are significant climate feedback. Tropospheric water vapor climate feedback is typically well represented in global models. However, predictions of future changes in stratospheric humidity are highly uncertain due to gaps in our understanding of physical processes occurring in the region of the atmosphere that controls the composition of the stratosphere, the Tropical Tropopause Layer (TTL, ~13-18 km). The ability to predict future changes in stratospheric ozone are also limited due to uncertainties in the chemical composition of the TTL. In order to address these uncertainties, the Airborne Tropical Tropopause Experiment (ATTREX) was completed. Instruments during ATTREX provided measurements to trace the movement of reactive halogen-containing compounds and other important chemical species, the size and shape of cirrus cloud particles, water vapor, and winds in three dimensions through the TTL. Bromine-containing gases were measured to improve understanding of stratospheric ozone. ATTREX consisted of four NASA Global Hawk Uninhabited Aerial System (UAS) campaigns deployed from NASA\u2019s Armstrong Flight Research Center (formally Dryden Flight Research Center). Campaigns were deployed over Edwards, CA, Guam, Hawaii, and Darwin, Australia in Boreal summer, winter, fall, and summer, respectively.",
-            "title": "ATTREX-Aircraft_RemoteSensing_Temperature_Measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FATTREX%2F0001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FATTREX%2F0001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/ATTREX",
-                    "description": "ASDC Data and Information for ATTREX",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for ATTREX",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/ATTREX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0001",
-                    "description": "DOI data set landing page for ATTREX-Aircraft_RemoteSensing_Temperature_Measurements_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ATTREX-Aircraft_RemoteSensing_Temperature_Measurements_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536056465-LARC_ASDC",
-                    "description": "Earthdata Search for ATTREX-Aircraft_RemoteSensing_Temperature_Measurements_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ATTREX-Aircraft_RemoteSensing_Temperature_Measurements_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536056465-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/attrex/",
-                    "description": "ESPO home page for ATTREX",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for ATTREX",
+                    "downloadURL": "https://espo.nasa.gov/attrex/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espoarchive.nasa.gov/archive/browse/attrex",
-                    "description": "ESPO Data Archive for ATTREX",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Data Archive for ATTREX",
+                    "downloadURL": "https://espoarchive.nasa.gov/archive/browse/attrex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ATTREX/Aircraft_RemoteSensing_Temperature_Measurements_1/",
-                    "description": "ASDC Direct Data Download for ATTREX-Aircraft_RemoteSensing_Temperature_Measurements_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ATTREX-Aircraft_RemoteSensing_Temperature_Measurements_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ATTREX/Aircraft_RemoteSensing_Temperature_Measurements_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1536056465-LARC_ASDC",
+            "issued": "2015-01-30",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "altitude",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-135.62 -12.33 -113.17 36.12",
+            "temporal": "2011-10-01T00:00:00Z/2013-03-01T23:59:59Z",
             "theme": [
                 "ATTREX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATTREX-Aircraft_RemoteSensing_Temperature_Measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SQSWDF366LDY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2019-05-30. CAR_ARCTAS_BRDF. Version 2. CAR ARCTAS BRDF Measurements L1 V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SQSWDF366LDY. https://disc.gsfc.nasa.gov/datacollection/CAR_ARCTAS_BRDF_2.html.",
-            "issued": "2019-01-27",
-            "temporal": "2008-04-06T00:00:00Z/2008-07-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-05",
-            "keyword": [
-                "earth science",
-                "ocean optics",
-                "oceans",
-                "surface radiative properties",
-                "atmosphere",
-                "land surface",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHARLES GATEBE",
                 "hasEmail": "mailto:gatebe@climate.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1617621679-GES_DISC",
-            "description": "ARCTAS focuses on advancing understanding of the factors driving current changes in the Arctic region including transport of mid-latitude pollution, boreal forest fires, aerosol radiative forcing, and chemical processes. ARCTAS aimed to use detailed observations from aircraft to provide the validation, retrieval constraints, correlative data, and process information needed to better achieve the potential of satellites for Arctic research. The plan is for the combination of satellite and aircraft data to provide together powerful information for constraining and evaluating models of Arctic atmospheric composition and climate, and thus improve model projections of future change. \n\nThe first phase of ARCTAS was based in Fairbanks and Barrow, Alaska with some flights to Thule, Greenland in April and focused on thick aerosol layers known as &#8220;arctic haze.&#8221; The second phase followed in July based from Cold Lake, Alberta and the Northwest Territories focusing on the emissions from large boreal forest fires in northwest Canada. \n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_ARCTAS_BRDF",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR ARCTAS BRDF Measurements  V2 (CAR_ARCTAS_BRDF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_ARCTAS_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "ARCTAS focuses on advancing understanding of the factors driving current changes in the Arctic region including transport of mid-latitude pollution, boreal forest fires, aerosol radiative forcing, and chemical processes. ARCTAS aimed to use detailed observations from aircraft to provide the validation, retrieval constraints, correlative data, and process information needed to better achieve the potential of satellites for Arctic research. The plan is for the combination of satellite and aircraft data to provide together powerful information for constraining and evaluating models of Arctic atmospheric composition and climate, and thus improve model projections of future change. \n\nThe first phase of ARCTAS was based in Fairbanks and Barrow, Alaska with some flights to Thule, Greenland in April and focused on thick aerosol layers known as &#8220;arctic haze.&#8221; The second phase followed in July based from Cold Lake, Alberta and the Northwest Territories focusing on the emissions from large boreal forest fires in northwest Canada. \n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSQSWDF366LDY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSQSWDF366LDY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1662602,17 +1662576,17 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_ARCTAS_BRDF_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_ARCTAS_BRDF_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://car.gsfc.nasa.gov/",
-                    "description": "CAR Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CAR Project Home Page",
+                    "downloadURL": "https://car.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
@@ -1662622,217 +1662596,245 @@
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_ARCTAS_BRDF.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_ARCTAS_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_ARCTAS_BRDF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_ARCTAS_BRDF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_ARCTAS_L1C_1.jpg",
+            "identifier": "C1617621679-GES_DISC",
+            "issued": "2019-01-27",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "oceans",
+                "surface radiative properties",
+                "atmosphere",
+                "land surface",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/SQSWDF366LDY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_ARCTAS_BRDF",
             "spatial": "-156.458 33.2106 -75.2635 80.6429",
+            "temporal": "2008-04-06T00:00:00Z/2008-07-10T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR ARCTAS BRDF Measurements  V2 (CAR_ARCTAS_BRDF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0107",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0107.",
-            "issued": "1999-11-08",
-            "temporal": "1991-11-09T00:00:00Z/1991-12-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "spectral/engineering",
-                "precipitation",
-                "clouds",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric winds",
-                "radar",
-                "earth science",
-                "altitude",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREW HEYMSFIELD",
                 "hasEmail": "mailto:heyms1@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001168-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems. The microphysical parameters in the data set were derived from 2D probe data collected by the NCAR aircraft during FIRE II. The 2D-C data are converted to size spectra according to the guidelines given in Heymsfield and Baumgardner (1985, Bull. Amer. Meteoro. Soc.), where one element is added to the size of a particle along the the flight direction to account for the probe's intrinsic start-up time. Size is determined as the maximum dimension ($D_{max}$) along the flight direction or optical array axis. The nominal size resolution for the Sabreliner 2D probe is 50 microns/per shadowed optical array element, for the King Air is 25 microns/bin. Sample area (SA) is derived using the depth of field estimates reported by Knollenberg (1970). Particles are binned into 32 size categories, nonuniformly spaced with higher resolution in the smaller classes. Particles within each size bin are subdivided into 10 ``area ratio (AR)'' bins, where AR represents the ratio of particle area to the area of discs of diameter $D_{max}$. The microphysical parameters in the data set were derived from 2D probe data collected by the NCAR Sabreliner during FIRE II. The derivation of the microphysical parameters is outlined in the later reference to Heymsfield (1977). The vertical velocity is the steady-state velocity in cm s-1 to keep the relative humidity at it's currently measured value. Differential growth rate represents the growth rate of the particle population of different sizes at the current relative humidity. The Total differential growth rate is the sum of the growth rate in all channels. The assumptions used for the IWC calculations are reported in Heymsfield; also, generic size to mass equations are used. Precipitation rate is calculated from particle size and terminal velocity data, integrated over the size spectrum. Concentration data are as derived above. Number of crystal-crystal collisions are derived from the data reported by Hindman and the crystal terminal velocities. Water vapor density andsupersaturation information in this data set should not be used--it is unreliable. Curve fits to the data using least squares methods are provided. VARIABLE DESCRIPTION UNITS ------------------------------------------------------------------------------- IT1, ITMEASUREMENT TIME INTERVAL HH/MM/SS PS STATIC PRESSURE mb TEMP AMBIENT TEMPERATURE degreesC ALT PRESSURE ALTITUDE m USTAR VERTICAL VELOCITY NEEDED TO KEEP THE cm/s RELATIVE HUMIDITY CONSTANT DBARM MEDIAN PARTICLE MASS WEIGHTED DIAMETER cm DMAX MAXIMUM PARTICLE DIAMETER cm W1 DIFFUSIONAL GROWTH RATE IN CHANNEL 1 g/sec W2 DIFFUSIONAL GROWTH RATE IN CHANNEL 2 g/sec W3 DIFFUSIONAL GROWTH RATE IN CHANNEL 3 g/sec W4 DIFFUSIONAL GROWTH RATE IN CHANNEL 4 g/sec WTOT TOTAL DIFFUSTIONAL GROWTH RATE g/sec DT8 DEPLETION TIME (8 micron droplets) sec DT12 DEPLETION TIME (12 micron droplets) sec TM",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II NCAR Kingair Aircraft Microphysical Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0107",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0107",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
-                    "description": "ASDC Data and Information for FIRE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for FIRE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001168-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_KINGAIR_IWC_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_KINGAIR_IWC_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001168-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_kingair_iwc_dataset.pdf",
-                    "description": "FIRE Cirrus 2 NCAR Kingair Aircraft Ice Water Concentrations Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 NCAR Kingair Aircraft Ice Water Concentrations Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_kingair_iwc_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_kingair_iwc_info1.txt",
-                    "description": "FIRE Sabreline and KING Air Microphysical Data Sets Readme for C-based Read Software",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Sabreline and KING Air Microphysical Data Sets Readme for C-based Read Software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_kingair_iwc_info1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_kingair_iwc.txt",
-                    "description": "Data Set Description for FIRE II Microphysical Data for the NCAR KING Air Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Description for FIRE II Microphysical Data for the NCAR KING Air Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_kingair_iwc.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_ci2_iwc_read.c",
-                    "description": "Read program for reading the FIRE Sabreliner and Kingair Microphysical Data Sets - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Read program for reading the FIRE Sabreliner and Kingair Microphysical Data Sets - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_ci2_iwc_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/makefile_kingair_iwc.txt",
-                    "description": "Read Software - kingair_iwc",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software - kingair_iwc",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/makefile_kingair_iwc.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-Cirrus.tar",
-                    "description": "FIRE II-Cirrus Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II-Cirrus Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-Cirrus.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0107",
-                    "description": "DOI data set landing page for FIRE_CI2_KINGAIR_IWC_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_KINGAIR_IWC_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0107",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Cirrus.tar",
-                    "description": "FIRE I-Cirrus Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE I-Cirrus Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Cirrus.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Extended-Time-Observation.tar",
-                    "description": "FIRE I-Extended-Time-Observation Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE I-Extended-Time-Observation Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Extended-Time-Observation.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-ASTEX.tar",
-                    "description": "FIRE II-ASTEX Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II-ASTEX Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-ASTEX.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
-                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_KINGAIR_IWC/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_KINGAIR_IWC_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_KINGAIR_IWC_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_KINGAIR_IWC/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_KINGAIR_IWC/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_KINGAIR_IWC_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_KINGAIR_IWC_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_KINGAIR_IWC/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001168-LARC_ASDC",
+            "issued": "1999-11-08",
+            "keyword": [
+                "spectral/engineering",
+                "precipitation",
+                "clouds",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric winds",
+                "radar",
+                "earth science",
+                "altitude",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0107",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>34.0 -106.3 34.0 -93.0 43.0 -93.0 43.0 -106.3 34.0 -106.3</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1991-11-09T00:00:00Z/1991-12-06T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II NCAR Kingair Aircraft Microphysical Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. This version V2.0 supersedes previous deliveries of the same dataset. Note that the two datasets RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V1.0 and RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04B-V1.0 have been merged into one dataset: RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m04-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "beta car",
@@ -1662843,69 +1662845,45 @@
                 "achernar",
                 "fomalhaut"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m04-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. This version V2.0 supersedes previous deliveries of the same dataset. Note that the two datasets RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V1.0 and RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04B-V1.0 have been merged into one dataset: RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M04-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
-            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP004 V2.0",
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
+            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP004 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/L64GCHMXAHPM",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Martin Snow. 2021-01-06. SOR3SOLS_MGII_018. Version 018. SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio As-Measured Cadence V018. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/L64GCHMXAHPM. https://disc.gsfc.nasa.gov/datacollection/SOR3SOLS_MGII_018.html. Digital Science Data.",
-            "issued": "2020-12-29",
-            "temporal": "2003-03-05T00:00:00Z/2020-02-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-29",
-            "keyword": [
-                "earth science",
-                "sun-earth interactions",
-                "solar activity"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MARTIN SNOW",
                 "hasEmail": "mailto:martin.snow@lasp.colorado.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1993479669-GES_DISC",
-            "description": "The SORCE SOLSTICE Level 3 MgII Core to Wing Ratio As-Measured Cadence product consists of all measurements of the magnesium II core-to-wing index from the SOLSTICE instrument. The SOLSTICE instrument makes measurements during each daytime orbit portion, 15 orbits per day. A complete solar spectrum is made in about 30 minutes, a quick scan mode in about 5 minutes. The spectral resolution of SOLSTICE is 0.1 nm, allowing the Mg-II doublet to be fully resolved and modeled with Gaussians. The Mg-II core-to-wing ratio is used as a measurement of solar activity.\n\nThe Mg-II data are arranged in a single file in a tabular ASCII text file which can be easily read into a spreadsheet application. The columns contain the date (calendar and Julian Day), the core/wing ratio, and the absolute uncertainty. The rows are arranged with one daily average measurment, repeating for each day for the length of the measurement period.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SOR3SOLS_MGII_018",
             "creator": "Martin Snow",
-            "title": "SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio As-Measured Cadence V018 (SOR3SOLS_MGII_018) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SOR3SOLS_MGII_018.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The SORCE SOLSTICE Level 3 MgII Core to Wing Ratio As-Measured Cadence product consists of all measurements of the magnesium II core-to-wing index from the SOLSTICE instrument. The SOLSTICE instrument makes measurements during each daytime orbit portion, 15 orbits per day. A complete solar spectrum is made in about 30 minutes, a quick scan mode in about 5 minutes. The spectral resolution of SOLSTICE is 0.1 nm, allowing the Mg-II doublet to be fully resolved and modeled with Gaussians. The Mg-II core-to-wing ratio is used as a measurement of solar activity.\n\nThe Mg-II data are arranged in a single file in a tabular ASCII text file which can be easily read into a spreadsheet application. The columns contain the date (calendar and Julian Day), the core/wing ratio, and the absolute uncertainty. The rows are arranged with one daily average measurment, repeating for each day for the length of the measurement period.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL64GCHMXAHPM",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL64GCHMXAHPM",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1662915,295 +1662893,296 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SOLS_MGII.018/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SOLS_MGII.018/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SOLS_MGII_018",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SOLS_MGII_018",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/data/sorce/file_readers/read_lasp_ascii_file.pro",
-                    "description": "IDL-based read software.",
                     "@type": "dcat:Distribution",
+                    "description": "IDL-based read software.",
+                    "downloadURL": "http://lasp.colorado.edu/data/sorce/file_readers/read_lasp_ascii_file.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/",
-                    "description": "SORCE Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "SORCE Project Home Page.",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/instruments/solstice/solstice-data-product-release-notes/",
-                    "description": "SOLSTICE Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SOLSTICE Release Notes",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/instruments/solstice/solstice-data-product-release-notes/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eospso.nasa.gov/sites/default/files/atbd/ATBD-SOR-01.pdf",
-                    "description": "SORCE ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "SORCE ATBD",
+                    "downloadURL": "https://eospso.nasa.gov/sites/default/files/atbd/ATBD-SOR-01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/reference/publications/",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/reference/publications/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SOR3SOLS_MGII_018.png",
+            "identifier": "C1993479669-GES_DISC",
+            "issued": "2020-12-29",
+            "keyword": [
+                "earth science",
+                "sun-earth interactions",
+                "solar activity"
+            ],
+            "landingPage": "https://doi.org/10.5067/L64GCHMXAHPM",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SOR3SOLS_MGII_018",
+            "temporal": "2003-03-05T00:00:00Z/2020-02-24T23:59:59.999Z",
             "theme": [
                 "SORCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio As-Measured Cadence V018 (SOR3SOLS_MGII_018) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3XMCS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Yueh. 2018-10-01. Aquarius CAP Sea Surface Salinity and Wind Products. Version 5.0. Aquarius CAP Sea Surface Salinity and Wind Products. Jet Propulsion Laboratory, 4800 Oak Grove Drive, Pasadena, CA91109, USA. Archived by National Aeronautics and Space Administration, U.S. Government, JPL - Simon Yueh. https://doi.org/10.5067/AQR50-3XMCS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. Simon Yueh, JPL - Simon Yueh, 2018-10-01, Aquarius CAP Level 3 Wind Speed Standard Mapped Image Monthly Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2018-08-22",
-            "temporal": "2011-09-01T00:00:00Z/2015-06-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-22",
-            "keyword": [
-                "ocean winds",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "User Services",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491757162-POCLOUD",
-            "description": "Version 5.0 Aquarius CAP Level 3 products are the fourth release of the AQUARIUS/SAC-D mapped salinity and wind speed data based on the Combined Active Passive (CAP) algorithm. CAP Level 3 standard mapped image products contain gridded 1 degree spatial resolution salinity and wind speed data averaged over 7 day and monthly time scales.  This particular dataset is the monthly wind speed V5.0 Aquarius CAP product. CAP is a P.I. produced dataset developed and provided by JPL.  The CAP algorithm utilizes data from both the onboard radiometer and scatterometer to simultaneously retrieve salinity, wind speed and direction by minimizing the sum of squared differences between model and observations. The main improvements in CAP V5.0 relative to the previous version include: updates to the Geophysical Model Functions to 4th order harmonics with the inclusion of sea surface temperature (SST) and stability at air-sea interface effects; use of the Canadian Meteorological Center (CMC) SST product as the new source ancillary sea surface temperature data in place of NOAA OI SST. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Jet Propulsion Laboratory, 4800 Oak Grove Drive, Pasadena, CA91109, USA",
-            "series-name": "Aquarius CAP Sea Surface Salinity and Wind Products",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Simon Yueh",
-            "title": "Aquarius CAP Level 3 Wind Speed Standard Mapped Image Monthly Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_CAP_MONTHLY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Version 5.0 Aquarius CAP Level 3 products are the fourth release of the AQUARIUS/SAC-D mapped salinity and wind speed data based on the Combined Active Passive (CAP) algorithm. CAP Level 3 standard mapped image products contain gridded 1 degree spatial resolution salinity and wind speed data averaged over 7 day and monthly time scales.  This particular dataset is the monthly wind speed V5.0 Aquarius CAP product. CAP is a P.I. produced dataset developed and provided by JPL.  The CAP algorithm utilizes data from both the onboard radiometer and scatterometer to simultaneously retrieve salinity, wind speed and direction by minimizing the sum of squared differences between model and observations. The main improvements in CAP V5.0 relative to the previous version include: updates to the Geophysical Model Functions to 4th order harmonics with the inclusion of sea surface temperature (SST) and stability at air-sea interface effects; use of the Canadian Meteorological Center (CMC) SST product as the new source ancillary sea surface temperature data in place of NOAA OI SST. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3XMCS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3XMCS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/aquarius",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/aquarius",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_CAP_MONTHLY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_CAP_MONTHLY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
-                    "description": "Aquarius CAP V5.0 Algorithm and Data Users Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius CAP V5.0 Algorithm and Data Users Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://aquarius.nasa.gov/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "http://aquarius.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757162-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757162-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757162-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757162-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
-                    "description": "ATBD, Validation & Uncertainty Analyses, Publications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation & Uncertainty Analyses, Publications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/CAPv5/Aquarius-CAP-User-Guide-v5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic data readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic data readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_CAP_MONTHLY_V5.jpg",
+            "identifier": "C2491757162-POCLOUD",
+            "issued": "2018-08-22",
+            "keyword": [
+                "ocean winds",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3XMCS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Jet Propulsion Laboratory, 4800 Oak Grove Drive, Pasadena, CA91109, USA",
+            "series-name": "Aquarius CAP Sea Surface Salinity and Wind Products",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-09-01T00:00:00Z/2015-06-01T00:00:00Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius CAP Level 3 Wind Speed Standard Mapped Image Monthly Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-LECP-3-RDR-FAR-ENC-400MSEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This far encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Uranus. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Uranus far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection. Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-lecp-3-rdr-far-enc-400msec-v1.0_y2wm-f6di",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-LECP-3-RDR-FAR-ENC-400MSEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-lecp-3-rdr-far-enc-400msec-v1.0_y2wm-f6di",
-            "description": "This far encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Uranus. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Uranus far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection. Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG2 LECP 0.4S HIGH RESOLUTION URANUS FAR ENCOUNTER DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 LECP 0.4S HIGH RESOLUTION URANUS FAR ENCOUNTER DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/y2xm-n2qx",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "nucleic acid sequencing",
-                "treatment protocol",
-                "ionizing radiation",
-                "library construction",
-                "nucleic acid extraction",
-                "hindlimb unloading"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GeneLab Outreach",
                 "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "nasa_genelab_GLDS-334_y2xm-n2qx",
             "description": "Biological risks associated with space radiation and microgravity are major concerns for long-term space travel. Through a Systems Biology approach our previous NASA work has shown both TGF xce xb2 signaling pathways and miRNAs have a critical impact on defining health risks with and without space irradiation. We hypothesize that circulating microRNA (miRNA) signatures are driving microvascular disease and muscle degeneration associated with accelerating aging and will be enhanced by exposure to the space environment (radiation and microgravity). We investigated this hypothesis both in vivo and in vitro and test novel antagonist therapies to these miRNA signatures as countermeasures to reduce space radiation-induced health risks. A comprehensive Systems Biology approach was used to examine the influence by high atomic number by high (H) atomic number (Z) and energy (E) (HZE) irradiation. To simulate low-dose exposure due to galactic cosmic rays (GCR) we used the ions energy and doses determined by a NASA consensus formula of 7 different ions to represent GCR (referred to as GCR sim model). To simulate high-dose radiation exposure due to solar particle events (SPE) we used an acute dose of SPE simulated beam at 1Gy which has energies ranging from 50MeV to 150MeV. C57BL/6 wild-type mice were utilized for irradiation with our established simulated microgravity model (hindlimb suspension model) and an in vitro 3D microvasculature tissue model under simulated microgravity (clinostat) conditions will also be irradiated. To expand on the circulating miRNA signature determined from our preliminary data we determined a group of conserved miRNAs which are commonly being regulated in the majority of the organs and tissues throughout the host using our established techniques. MiRNA-sequencing on serum (before IR and at time of sacrifice) liver heart and muscle tissue for all radiation groups revealed the key circulating miRNA signature (consisting of multiple miRNAs) impacting disease risk. Collectively understanding of how whole body space radiation impacts microvascular and tissue degeneration through circulating miRNAs will greatly enhance health risk prognostication and provide possible new mechanisms for protection against space radiation.",
-            "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Heart tissue",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-334",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-334",
+                    "mediaType": "text/html",
                     "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Heart tissue"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-334_y2xm-n2qx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "nucleic acid sequencing",
+                "treatment protocol",
+                "ionizing radiation",
+                "library construction",
+                "nucleic acid extraction",
+                "hindlimb unloading"
+            ],
+            "landingPage": "https://data.nasa.gov/d/y2xm-n2qx",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Heart tissue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/ask-academy/ask-the-academy-past-issues/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://km.nasa.gov/knowledge-map/"
-            ],
-            "keyword": [
-                "appel",
-                "knowledge",
-                "sharing",
-                "ask the academy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ed Hoffman",
                 "hasEmail": "mailto:ehoffman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-862__5",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1663211,561 +1663190,560 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__5",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "knowledge",
+                "sharing",
+                "ask the academy"
+            ],
+            "landingPage": "http://appel.nasa.gov/ask-academy/ask-the-academy-past-issues/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-MSA-HRSC-5-REFDR-PHOBOS-MAPS-V1.0",
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
-                "mars express",
-                "phobos"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-msa-hrsc-5-refdr-phobos-maps-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "phobos"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-MSA-HRSC-5-REFDR-PHOBOS-MAPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-msa-hrsc-5-refdr-phobos-maps-v1.0",
-            "description": "N/A",
-            "title": "MARS EXPRESS MARS SATELLITE HRSC REFDR PHOBOS MAPS V1.0",
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
+            "title": "MARS EXPRESS MARS SATELLITE HRSC REFDR PHOBOS MAPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1125",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ellis, E.E., J.E. Richey, P.B. de Camargo, A.V. Krusche, P.D. Quay, C.I. Salimon, and H.B. da Cunha. 2012. LBA-ECO CD-06 Carbon Cycling in Rivers in Amazonas and Acre, Brazil: 2005-2006. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1125",
-            "issued": "2023-10-03",
-            "temporal": "2005-07-16T00:00:00Z/2006-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "land surface",
-                "vegetation",
-                "soils",
-                "water quality/water chemistry",
-                "biosphere",
-                "earth science",
-                "surface water"
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
-            "identifier": "C2780951173-ORNL_CLOUD",
             "description": "This data set provides measured and calculated variables describing the carbon pools in river waters, CO2 respired from the water and total amount of CO2 evaded, dissolved oxygen isotopes (delta 18O-O2), and concentration of bacterial cells in river water. Samples were collected from 10 white-water rivers, two clear-water streams (one each in Amazonas and Acre), and two black-water rivers in Amazonas from July to September 2005, which coincided with a severe drought in the western and southern regions of the Amazon Basin (Zeng et al. 2008). Eight of these sites were resampled during August through September 2006 of the following year (no drought).",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-06 Carbon Cycling in Rivers in Amazonas and Acre, Brazil: 2005-2006",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1125",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1125",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD06_Carbon_respiration/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD06_Carbon_respiration/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD06_Carbon_respiration.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD06_Carbon_respiration.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1125",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1125",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD06_Carbon_respiration/comp/CD06_Carbon_respiration.PDF",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD06_Carbon_respiration/comp/CD06_Carbon_respiration.PDF",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+            "identifier": "C2780951173-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "land surface",
+                "vegetation",
+                "soils",
+                "water quality/water chemistry",
+                "biosphere",
+                "earth science",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1125",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-72.7 -10.07 -58.75 -2.59",
+            "temporal": "2005-07-16T00:00:00Z/2006-09-25T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-06 Carbon Cycling in Rivers in Amazonas and Acre, Brazil: 2005-2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945980-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "national geospatial data asset",
-                "ocean temperature",
-                "ngda",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1641945980-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Mapped 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
-                    "description": "NASA Ocean Color Web - Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
-                    "description": "NASA Ocean Color Web - Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Citation Policy",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/SST/R2019.0",
-                    "description": "MODIS-Aqua L3M 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/SST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1641945980-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "national geospatial data asset",
+                "ocean temperature",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945980-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OB.DAAC"
+            },
             "spatial": "-180.0 90.0 -180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua MODIS Global Mapped 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADEOS-II/AMSR/AA_L2A.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR/ADEOS-II L2A Global Swath Spatially-Resampled Brightness Temperatures V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ADEOS-II/AMSR/AA_L2A.001.",
-            "issued": "2003-01-18",
-            "temporal": "2003-01-18T00:00:00Z/2003-10-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-10-24",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Peter Ashcroft",
                 "hasEmail": "mailto:ashcroft@remss.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1241435536-NSIDC_ECS",
             "description": "The AMSR Level-2A product (AA_L2A) contains brightness temperatures at 6.9 GHz, 10.65 GHz, 18.7 GHz, 23.8 GHz, 36.5 GHz, 89.0 GHz, 50.3 GHz, and 52.8GHz. Data are resampled to be spatially consistent except for the 50.3GHz and 52.8GHz data, and therefore are available at a variety of resolutions that correspond to the footprint sizes of the observations such as 56 km, 38 km, 24 km, 21 km, 12 km, and 5.4 km, respectively.",
-            "title": "AMSR/ADEOS-II L2A Global Swath Spatially-Resampled Brightness Temperatures V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-II%2FAMSR%2FAA_L2A.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-II%2FAMSR%2FAA_L2A.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AA_L2A.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AA_L2A.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AA_L2A/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AA_L2A/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ADEOS-II/AMSR/AA_L2A.001",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ADEOS-II/AMSR/AA_L2A.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ADEOS-II/AMSR/AA_L2A.001",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ADEOS-II/AMSR/AA_L2A.001",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1241435536-NSIDC_ECS",
+            "issued": "2003-01-18",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS-II/AMSR/AA_L2A.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-10-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2003-01-18T00:00:00Z/2003-10-24T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR/ADEOS-II L2A Global Swath Spatially-Resampled Brightness Temperatures V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0533-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-12T11:54:00.000 to 2015-01-12T22:15:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0533-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0533-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0533-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-12T11:54:00.000 to 2015-01-12T22:15:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0533 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0533 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D21.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D21. Version 001. VIIRS/NPP BRDF/Albedo Parameter 3 Band M8 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D21.001. https://doi.org/10.5067/VIIRS/VNP43D21.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
-                "land surface"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1607319341-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 Band M8 product (VNP43D21) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D21 is the BRDF geometric parameter for VIIRS band M8 (1.240 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for VIIRS band M8.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D21",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 Band M8 Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 Band M8 product (VNP43D21) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D21 is the BRDF geometric parameter for VIIRS band M8 (1.240 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for VIIRS band M8.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D21.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D21.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
-                    "description": "Product Quality information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Product Quality information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D21.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D21.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D21.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D21.001/",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607319341-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607319341-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D21.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D21.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43d_cmg_30_arc-second_products",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43d_cmg_30_arc-second_products",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D21",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D21",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
-                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
-                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 }
             ],
+            "identifier": "C1607319341-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D21.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP43D21",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 Band M8 Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/CORAL/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/CORAL/DATA001.",
-            "issued": "2014-07-21",
-            "temporal": "2014-07-21T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "ocean temperature",
-                "salinity/density",
-                "ocean chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360196-OB_DAAC",
             "description": "The CORAL experiment is a Earth Venture Suborbital-2 (EVS-2) mission designed to provide an extensive, uniform picture of coral reef composition through the use of the Portable Remote Imaging Spectrometer (PRISM) instrument aboard the Tempus Applied Solutions Gulfstream-IV (G-IV) aircraft combined with a variety of in situ data to identify reef composition and model primary production. The CORAL experiment covers the Mariana Islands, Palau, portions of the Great Barrier Reef, and the Main Hawaiian Islands.INTERNAL LINKSCORAL-PRISM Browser (Aircraft data)EXTERNAL LINKSBIOS CORAL Page",
-            "title": "CORAL Experiment",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCORAL%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCORAL%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CORAL/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CORAL/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360196-OB_DAAC",
+            "issued": "2014-07-21",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "ocean temperature",
+                "salinity/density",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/CORAL/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-07-21T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CORAL Experiment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652157-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goddard Space Flight Center (GSFC). MRIRN3IM. Version 001. MRIR/Nimbus-3 Images of Daytime Brightness Temperature on 4 x 5 inch Film Sheets V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MRIRN3IM_001.html. Digital Science Data.",
-            "issued": "1969-04-15",
-            "temporal": "1969-04-15T00:00:00Z/1970-02-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1970-02-04",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1273652157-GES_DISC",
-            "description": "MRIRN3IM is the Nimbus-3 Medium Resolution Infrared Radiometer (MRIR) data product consisting of 4 x 5 inch photographic film sheets. Each film sheet contains an entire orbit (daylight portion) of brightness temperatures measured at five wavelength bands: 6.5-7.0, 10-11, 14.5-15.5, 5-30, and 0.2-4.0 micrometers. There are also associated latitude grids, time, and gray scales representing different temperatures. The images are saved as JPEG 2000 digital files. About 3 weeks of images are archived into a TAR file. The processing techniques used to produce the data set and a full description of the data set are contained in section 4 of the \"Nimbus III Users' Guide.\"\n\nThe MRIR experiment measured the intensity and distribution of electromagnetic radiation emitted by and reflected from the earth and its atmosphere in five selected wavelength intervals from 0.2 to 30 micrometers. Data for heat balance of the earth-atmosphere system were obtained, as well as measurements of water vapor distribution, surface or near-surface temperatures, and seasonal changes of stratospheric temperature distribution. The MRIR experiment obtained data from April 15 1969 until February 4, 1970.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00184 (old ID 69-037A-05A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MRIRN3IM",
             "creator": "Goddard Space Flight Center (GSFC)",
-            "title": "MRIR/Nimbus-3 Images of Daytime Brightness Temperature on 4 x 5 inch Film Sheets V001 (MRIRN3IM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MRIRN3IM_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "MRIRN3IM is the Nimbus-3 Medium Resolution Infrared Radiometer (MRIR) data product consisting of 4 x 5 inch photographic film sheets. Each film sheet contains an entire orbit (daylight portion) of brightness temperatures measured at five wavelength bands: 6.5-7.0, 10-11, 14.5-15.5, 5-30, and 0.2-4.0 micrometers. There are also associated latitude grids, time, and gray scales representing different temperatures. The images are saved as JPEG 2000 digital files. About 3 weeks of images are archived into a TAR file. The processing techniques used to produce the data set and a full description of the data set are contained in section 4 of the \"Nimbus III Users' Guide.\"\n\nThe MRIR experiment measured the intensity and distribution of electromagnetic radiation emitted by and reflected from the earth and its atmosphere in five selected wavelength intervals from 0.2 to 30 micrometers. Data for heat balance of the earth-atmosphere system were obtained, as well as measurements of water vapor distribution, surface or near-surface temperatures, and seasonal changes of stratospheric temperature distribution. The MRIR experiment obtained data from April 15 1969 until February 4, 1970.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00184 (old ID 69-037A-05A).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1663774,73 +1663752,107 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MRIRN3IM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MRIRN3IM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3IM.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3IM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MRIRN3IM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MRIRN3IM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3IM.001/doc/README.MRIRN3L1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3IM.001/doc/README.MRIRN3L1.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIIIUG.pdf",
-                    "description": "Nimbus 3 Users Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 3 Users Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIIIUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus3.tar.gz",
-                    "description": "Nimbus 3 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 3 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus3.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/nimbus/data-sets.html",
-                    "description": "Additional Nimbus data and images can be found at NSIDC",
                     "@type": "dcat:Distribution",
+                    "description": "Additional Nimbus data and images can be found at NSIDC",
+                    "downloadURL": "https://nsidc.org/data/nimbus/data-sets.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MRIRN3IM_001.png",
+            "identifier": "C1273652157-GES_DISC",
+            "issued": "1969-04-15",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652157-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1970-02-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MRIRN3IM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1969-04-15T00:00:00Z/1970-02-04T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MRIR/Nimbus-3 Images of Daytime Brightness Temperature on 4 x 5 inch Film Sheets V001 (MRIRN3IM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/bigview/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis Koga",
+                "hasEmail": "mailto:dennis.koga@nasa.gov"
+            },
+            "description": "BigView allows for interactive panning and zooming of images of arbitrary size on desktop PCs running linux. Additionally, it can work in a multi-screen environment where multiple PCs cooperate to view a single large image. Using this software, one can explore -- on relatively modest machines -- images such as the Mars Orbiter Camera mosaic [92160x33280 pixels].",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ti.arc.nasa.gov/m/opensource/downloads/bigView.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
+            ],
+            "identifier": "OCIO-Fitara-112",
             "issued": "2015-07-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "image",
                 "linux",
@@ -1663850,167 +1663862,126 @@
                 "code ti",
                 "image processing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dennis Koga",
-                "hasEmail": "mailto:dennis.koga@nasa.gov"
-            },
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/bigview/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Ames Research Center"
             },
-            "identifier": "OCIO-Fitara-112",
-            "description": "BigView allows for interactive panning and zooming of images of arbitrary size on desktop PCs running linux. Additionally, it can work in a multi-screen environment where multiple PCs cooperate to view a single large image. Using this software, one can explore -- on relatively modest machines -- images such as the Mars Orbiter Camera mosaic [92160x33280 pixels].",
-            "title": "ARC Code TI: BigView",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ti.arc.nasa.gov/m/opensource/downloads/bigView.tar.gz",
-                    "mediaType": "application/x-tar"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "ARC Code TI: BigView"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4QN64NG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN. 1996-12-31. Archive of Census Related Products (ACRP): 1990 Public Use Microdata Sample Areas (PUMA) Boundary Files. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4QN64NG. https://doi.org/10.7927/H4QN64NG.",
-            "issued": "1996-12-31",
-            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4Z60KZ9",
-                "https://doi.org/10.7927/H4G44N6R",
-                "https://doi.org/10.7927/H4BG2KWB",
-                "https://doi.org/10.7927/H47P8W9V",
-                "https://doi.org/10.7927/H43X84KH",
-                "https://doi.org/10.7927/H4057CV3",
-                "https://doi.org/10.7927/H46Q1V51",
-                "https://doi.org/10.7927/H4TD9V7F",
-                "https://doi.org/10.7927/H42Z13FP"
-            ],
-            "keyword": [
-                "human dimensions",
-                "population",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:metadata@ciesin.columbia.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "SEDAC"
-            },
-            "identifier": "C179001893-SEDAC",
-            "description": "The 1990 Public Use Microdata Sample Areas (PUMA) Boundary Files portion of the Archive of Census Related Products (ACRP) consists of 5% sample (apuma) and 1% sample (bpuma) areas for the mapping of 1990 PUMS data covering the continental United States, Alaska, and Hawaii. These boundary files are created based on equivalency files generated by the Geographic Correspondence Engine (GeoCorr). A national census tract to PUMA geography correspondence file is used in merging the two files resulting in the PUMA geographies. An additional file is also available consisting of geographic centroids for the PUMA coverages calculated by UIC (Urban Information Center/Office of Computing, University of Missouri). This portion of the ACRP is produced by the Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN",
-            "title": "Archive of Census Related Products (ACRP): 1990 Public Use Microdata Sample Areas (PUMA) Boundary Files",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-sample-areas-boundary-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 1990 Public Use Microdata Sample Areas (PUMA) Boundary Files portion of the Archive of Census Related Products (ACRP) consists of 5% sample (apuma) and 1% sample (bpuma) areas for the mapping of 1990 PUMS data covering the continental United States, Alaska, and Hawaii. These boundary files are created based on equivalency files generated by the Geographic Correspondence Engine (GeoCorr). A national census tract to PUMA geography correspondence file is used in merging the two files resulting in the PUMA geographies. An additional file is also available consisting of geographic centroids for the PUMA coverages calculated by UIC (Urban Information Center/Office of Computing, University of Missouri). This portion of the ACRP is produced by the Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4QN64NG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4QN64NG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-sample-areas-boundary-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-sample-areas-boundary-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-sample-areas-boundary-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-sample-areas-boundary-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-sample-areas-boundary-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-sample-areas-boundary-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-sample-areas-boundary-1990/sedac-logo.jpg",
+            "identifier": "C179001893-SEDAC",
+            "issued": "1996-12-31",
+            "keyword": [
+                "human dimensions",
+                "population",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4QN64NG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4Z60KZ9",
+                "https://doi.org/10.7927/H4G44N6R",
+                "https://doi.org/10.7927/H4BG2KWB",
+                "https://doi.org/10.7927/H47P8W9V",
+                "https://doi.org/10.7927/H43X84KH",
+                "https://doi.org/10.7927/H4057CV3",
+                "https://doi.org/10.7927/H46Q1V51",
+                "https://doi.org/10.7927/H4TD9V7F",
+                "https://doi.org/10.7927/H42Z13FP"
+            ],
+            "release-place": "Saginaw, MI",
             "spatial": "-180.0 18.0 -66.0 72.0",
+            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
             "theme": [
                 "ACRP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Archive of Census Related Products (ACRP): 1990 Public Use Microdata Sample Areas (PUMA) Boundary Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/8MO7DEDYTBH7",
             "citation": "Natalya A. Kramarova. 2023-01-24. OMPS_NPP_LP_L2_O3_DAILY. Version 2.6. OMPS-NPP L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8MO7DEDYTBH7. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_LP_L2_O3_DAILY_2.6.html. Digital Science Data.",
-            "issued": "2022-12-20",
-            "temporal": "2012-02-07T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-20",
-            "references": [
-                "https://doi.org/10.5194/amt-9-1239-2016",
-                "https://doi.org/10.1002/2013JD020482",
-                "https://doi.org/10.1029/2011JD017006",
-                "https://doi.org/10.5194/amt-10-167-2017",
-                "https://doi.org/10.1109/TGRS.2012.2213093"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATALYA KRAMAROVA",
                 "hasEmail": "mailto:Natalya.A.Kramarova@nasa.gov"
             },
+            "creator": "Natalya A. Kramarova",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2567918494-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 2.6 is the current version of this data product, and supersedes all previous versions.\n\nThe OMPS-NPP L2 LP Ozone (O3) Vertical Profile swath daily Center slit collection contains ozone measured by the Ozone Mapping and Profiling Suite (OMPS) Limb-Profiler (LP) sensor on the Suomi-NPP satellite. The LP ozone product measures the vertical distribution of ozone in the stratosphere and lower mesosphere. The algorithm derives ozone profile values along with errors in the UV from 29.5 km and 52.5 km, and in the visible from cloud top to 37.5 km (when there are no clouds the lower limit is 12.5 km). See the README for full description of the product and updated retrieval algorithm. \n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-90 to  90 degrees latitude), and there are about 14.5 orbits per day, the data from the center of the LP three slits are used to make a vertical profile. The profile is measured from the ground up to about 60 km with a vertical resolution of the retrieved profiles of approximately 1.8 km.\n\nThe data are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_LP_L2_O3_DAILY",
-            "creator": "Natalya A. Kramarova",
-            "title": "OMPS-NPP L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6 (OMPS_NPP_LP_L2_O3_DAILY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_LP_L2_O3_DAILY_2.6.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8MO7DEDYTBH7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8MO7DEDYTBH7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1664020,722 +1663991,753 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_LP_L2_O3_DAILY_2.6.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_LP_L2_O3_DAILY_2.6.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_LP_L2_O3_DAILY.2.6/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_LP_L2_O3_DAILY.2.6/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_LP_L2_O3_DAILY.2.6/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_LP_L2_O3_DAILY.2.6/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_LP_L2_O3_DAILY_2.6",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_LP_L2_O3_DAILY_2.6",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_LP_L2_O3_DAILY.2.6/doc/README.OMPS_NPP_LP_L2_O3_DAILY_V2.6.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_LP_L2_O3_DAILY.2.6/doc/README.OMPS_NPP_LP_L2_O3_DAILY_V2.6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nesdis.noaa.gov/current-satellite-missions/currently-flying/joint-polar-satellite-system",
-                    "description": "Joint Polar Satellite System (JPSS) mission home page",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) mission home page",
+                    "downloadURL": "https://www.nesdis.noaa.gov/current-satellite-missions/currently-flying/joint-polar-satellite-system",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_LP_L2_O3_DAILY_2.6.jpeg",
+            "identifier": "C2567918494-GES_DISC",
+            "issued": "2022-12-20",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/8MO7DEDYTBH7",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-9-1239-2016",
+                "https://doi.org/10.1002/2013JD020482",
+                "https://doi.org/10.1029/2011JD017006",
+                "https://doi.org/10.5194/amt-10-167-2017",
+                "https://doi.org/10.1109/TGRS.2012.2213093"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_NPP_LP_L2_O3_DAILY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-02-07T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-NPP L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6 (OMPS_NPP_LP_L2_O3_DAILY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/CAMERA/DATA102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Munchak, Stephen J.2013. GPM GROUND VALIDATION DC-8 CAMERA NADIR GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/CAMERA/DATA102",
-            "issued": "2013-04-09",
-            "temporal": "2012-02-20T14:06:19Z/2012-02-20T17:51:18Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "platform characteristics",
-                "land surface",
-                "earth science",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-ghrc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/MSFC/GHRC"
-            },
-            "identifier": "C1979637994-GHRC_DAAC",
             "description": "The GPM Ground Validation DC-8 Camera Nadir GCPEx dataset contains geo-located, visible-wavelength imagery of the ground obtained from the nadir camera aboard the NASA DC-8 in Canada during the Cold-season Precipitation Experiment (GCPEx). GCPEx addressed shortcomings in the GPM snowfall retrieval algorithm by collecting microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. These data sets were collected to aid in the achievement of the over arching goal of GCPEx which is to characterize the ability of multi-frequency active and passive microwave sensors to detect and estimate falling snow. The data is available only for February 20, 2012, a clear-air flight day. DC-8 Camera nadir data may be useful for determining snow cover and lake ice cover for emissivity studies. The dataset also includes, for convenience and reproducibility, aircraft navigation information and ground temperatures to aid in emissivity retrievals.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION DC-8 CAMERA NADIR GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FCAMERA%2FDATA102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FCAMERA%2FDATA102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmncamdc8gcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmncamdc8gcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/browse/gcpex_nadir_cameraDC8_20120220_160619.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/browse/gcpex_nadir_cameraDC8_20120220_160619.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/GCPEX/DATA101",
-                    "description": "GCPEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "GCPEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/GCPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmncamdc8gcpex/gpmncamdc8gcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmncamdc8gcpex/gpmncamdc8gcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/doc/AXIS_ds_223m_32713_en_0809_lo.pdf",
-                    "description": "AXIS 223M Network Camera specifications",
                     "@type": "dcat:Distribution",
+                    "description": "AXIS 223M Network Camera specifications",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/doc/AXIS_ds_223m_32713_en_0809_lo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/doc/read_nadircam.pro",
-                    "description": "PROGRAM - Read nadircam",
                     "@type": "dcat:Distribution",
+                    "description": "PROGRAM - Read nadircam",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/doc/read_nadircam.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GCPEx",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GCPEx",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/browse/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/dc8_camera_nadir/browse/",
+            "identifier": "C1979637994-GHRC_DAAC",
+            "issued": "2013-04-09",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "platform characteristics",
+                "land surface",
+                "earth science",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/CAMERA/DATA102",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-80.4001 43.4044 -67.495 47.0861",
+            "temporal": "2012-02-20T14:06:19Z/2012-02-20T17:51:18Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION DC-8 CAMERA NADIR GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2491731827-POCLOUD.html",
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "JASON-1. 2015-10-08. Jason-1 GDR netCDF Geodetic. Version E. JASON-1_L2_OST_GPN_E_GEODETIC. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, JASON-1. JASON-1, JASON-1, 2015-10-08, Jason-1 GDR version E NetCDF Geodetic, N/A.",
-            "issued": "2014-03-17",
-            "temporal": "2012-05-07T16:00:00Z/2013-06-21T00:56:55Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "sea surface topography",
-                "ocean waves"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jessica Hausman",
-                "hasEmail": "mailto:Jessica.K.Hausman@jpl.nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491731827-POCLOUD",
-            "description": "The Jason-1 Geophysical Data Records (GDR) Geodetic Mission contain full accuracy altimeter data, with a high precision orbit, provided approximately 35 days after data collection. The data are sorted into cycles that are approximately 11 days long and contain 280 pass files.  The instruments on Jason-1 make direct observations of the following quantities: altimeter range, significant wave height, ocean radar backscatter cross-section (a measure of wind speed), ionospheric electron content (derived by a simple formula), tropospheric water content, mean sea surface, and position relative to the GPS satellite constellation. The GDR contain all relevant corrections needed to calculate the sea surface height.",
-            "release-place": "JPL",
-            "series-name": "Jason-1 GDR netCDF Geodetic",
-            "graphic-preview-description": "Thumbnail",
-            "creator": "JASON-1",
-            "title": "Jason-1 GDR version E NetCDF Geodetic",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_L2_OST_GPN_E_GEODETIC.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "citation": "JASON-1. 2015-10-08. Jason-1 GDR netCDF Geodetic. Version E. JASON-1_L2_OST_GPN_E_GEODETIC. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, JASON-1. JASON-1, JASON-1, 2015-10-08, Jason-1 GDR version E NetCDF Geodetic, N/A.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jessica Hausman",
+                "hasEmail": "mailto:Jessica.K.Hausman@jpl.nasa.gov"
+            },
+            "creator": "JASON-1",
+            "description": "The Jason-1 Geophysical Data Records (GDR) Geodetic Mission contain full accuracy altimeter data, with a high precision orbit, provided approximately 35 days after data collection. The data are sorted into cycles that are approximately 11 days long and contain 280 pass files.  The instruments on Jason-1 make direct observations of the following quantities: altimeter range, significant wave height, ocean radar backscatter cross-section (a measure of wind speed), ionospheric electron content (derived by a simple formula), tropospheric water content, mean sea surface, and position relative to the GPS satellite constellation. The GDR contain all relevant corrections needed to calculate the sea surface height.",
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_L2_OST_GPN_E_GEODETIC.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_L2_OST_GPN_E_GEODETIC.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/j1_safehold.txt",
-                    "description": "Jason-1 safeholds and known data outages",
                     "@type": "dcat:Distribution",
+                    "description": "Jason-1 safeholds and known data outages",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/j1_safehold.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/j1_maneuver.txt",
-                    "description": "Jason-1 maneuvers",
                     "@type": "dcat:Distribution",
+                    "description": "Jason-1 maneuvers",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/j1_maneuver.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/Handbook_Jason-1_v5.1_April2016.pdf",
-                    "description": "Jason-1 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Jason-1 User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/Handbook_Jason-1_v5.1_April2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/j1_cyclelist.txt",
-                    "description": "Jason-1 cycle start list",
                     "@type": "dcat:Distribution",
+                    "description": "Jason-1 cycle start list",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/docs/j1_cyclelist.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/gdr_netcdf_e_geodetic/docs/Handbook_Jason-1_v5.1_April2016.pdf",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/open/L2/gdr_netcdf_e_geodetic/docs/Handbook_Jason-1_v5.1_April2016.pdf",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491731827-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491731827-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491731827-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491731827-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic data readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic data readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_L2_OST_GPN_E_GEODETIC.jpg",
+            "identifier": "C2491731827-POCLOUD",
+            "issued": "2014-03-17",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "sea surface topography",
+                "ocean waves"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2491731827-POCLOUD.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "Jason-1 GDR netCDF Geodetic",
             "spatial": "-180.0 -66.15 180.0 66.15",
+            "temporal": "2012-05-07T16:00:00Z/2013-06-21T00:56:55Z",
             "theme": [
                 "JASON-1",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Jason-1 GDR version E NetCDF Geodetic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2PLNTR-F08",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2023-07-31. Sentinel-6A MF Jason-CS L2P P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08. Version F08. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2PLNTR-F08.",
-            "issued": "2023-02-09",
-            "temporal": "2020-11-30T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-23",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "sea surface topography",
-                "ocean waves"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2619443920-POCLOUD",
-            "description": "Provides L2P low resolution (LR) non-time critical (NTC; 60-day latency) altimetry from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft, and contains L2-equivalent geophysical sea-state data at a slightly different latency than the other L2 NRT products. The sea-state data were derived from L1B altimetry, and include range, orbital altitude, time, and water vapour. Environmental and geophysical corrections, significant wave height, and wind-speed information are supplied by the AMR-C. The S6A NTC product is analogous to the Jason-3 GDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2P P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2P_ALT_HR_OST_NTC_F08.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides L2P low resolution (LR) non-time critical (NTC; 60-day latency) altimetry from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft, and contains L2-equivalent geophysical sea-state data at a slightly different latency than the other L2 NRT products. The sea-state data were derived from L1B altimetry, and include range, orbital altitude, time, and water vapour. Environmental and geophysical corrections, significant wave height, and wind-speed information are supplied by the AMR-C. The S6A NTC product is analogous to the Jason-3 GDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2PLNTR-F08",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2PLNTR-F08",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/sentinel-6/docs/D-14a_S3_L2P_handbook_SALP-MU-P-EA-23014-CLSv3_3.pdf",
-                    "description": "Along-track Level-2+ (L2P) Sea Level Anomaly Sentinel-3 / Jason-CS-Sentinel-6 Product Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Along-track Level-2+ (L2P) Sea Level Anomaly Sentinel-3 / Jason-CS-Sentinel-6 Product Handbook",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/sentinel-6/docs/D-14a_S3_L2P_handbook_SALP-MU-P-EA-23014-CLSv3_3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/missions/sentinel-6/",
-                    "description": "The mission page for Sentinel-6A MF on the NASA Jet Propulsion Laboratory (JPL) website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the NASA Jet Propulsion Laboratory (JPL) website.",
+                    "downloadURL": "https://www.jpl.nasa.gov/missions/sentinel-6/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sealevel.jpl.nasa.gov/missions/jasoncs/",
-                    "description": "The mission page for Sentinel-6A MF on the NASA Ocean Surface Topography (OST) website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the NASA Ocean Surface Topography (OST) website.",
+                    "downloadURL": "https://sealevel.jpl.nasa.gov/missions/jasoncs/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-6",
-                    "description": "The mission page for Sentinel-6A MF on the European Space Agency (ESA) website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the European Space Agency (ESA) website.",
+                    "downloadURL": "https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Sentinel-6",
-                    "description": "The mission page for Sentinel-6A MF on the PO.DAAC website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the PO.DAAC website.",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Sentinel-6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eumetsat.int/sentinel-6",
-                    "description": "The mission page for Sentinel-6A MF on the EUMETSAT website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the EUMETSAT website.",
+                    "downloadURL": "https://www.eumetsat.int/sentinel-6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://github.com/podaac/sentinel6",
-                    "description": "Jupyter notebooks to access and manipulate data from Sentinel-6A MF.",
                     "@type": "dcat:Distribution",
+                    "description": "Jupyter notebooks to access and manipulate data from Sentinel-6A MF.",
+                    "downloadURL": "https://github.com/podaac/sentinel6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eumetsat.int/altimetry-resources",
-                    "description": "Documentation hosted by EUMETSAT including the Generic File Naming Convention, and the Level 1 and Level 2 Product Format Specifications.",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation hosted by EUMETSAT including the Generic File Naming Convention, and the Level 1 and Level 2 Product Format Specifications.",
+                    "downloadURL": "https://www.eumetsat.int/altimetry-resources",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=97",
-                    "description": "PO.DAAC Forum Page for Sentinel-6A MF",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Forum Page for Sentinel-6A MF",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=97",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2P_ALT_LR_OST_NTC_F08",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2P_ALT_LR_OST_NTC_F08",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2P_ALT_HR_OST_NTC_F08.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2P_ALT_HR_OST_NTC_F08.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443920-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443920-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443920-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443920-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2P_ALT_HR_OST_NTC_F08.jpg",
+            "identifier": "C2619443920-POCLOUD",
+            "issued": "2023-02-09",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2PLNTR-F08",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2021.112395"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
+            "temporal": "2020-11-30T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L2P P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SAV_PLYMOUTH_BAY/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SAV_PLYMOUTH_BAY/DATA001.",
-            "issued": "2010-09-15",
-            "temporal": "2010-09-15T16:45:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "earth science",
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
-                "ocean chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360638-OB_DAAC",
             "description": "The Compact Hydrographic Airborne Rapid Total Survey (CHARTS) is jointly operated and maintained by the U.S. Army Corps of Engineers and the U.S. Naval Oceanographic Office. This system was flown by JALBTCX over Buttermilk and Plymouth Bays in Massachusetts, USA during Sept. 2010 to study Submersed aquatic vegetation species discrimination using an airborne hyperspectral/lidar system. A large, collaborative ground truth sampling campaign was undertaken. Components included bathymetric surveys, laboratory and diver reflectivity measurements of sediment and SAV, camera and diver SAV surveys, water column IOPs, and pigment sampling.",
-            "title": "Submersed Aquatic Vegetation (SAV) over Buttermilk and Plymouth Bays, Massachusetts",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSAV_PLYMOUTH_BAY%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSAV_PLYMOUTH_BAY%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SAV_Plymouth_Bay/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SAV_Plymouth_Bay/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360638-OB_DAAC",
+            "issued": "2010-09-15",
+            "keyword": [
+                "ocean optics",
+                "earth science",
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SAV_PLYMOUTH_BAY/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-09-15T16:45:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Submersed Aquatic Vegetation (SAV) over Buttermilk and Plymouth Bays, Massachusetts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/854",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rice, A.H., E.P. Hammond, S.R. Saleska, L.R. Hutyra, M.W. Palace, M.M. Keller, P.B. de Camargo, K. Portilho, D. Marques, and S.C. Wofsy. 2007. LBA-ECO CD-10 Ground-based Biometry Data at km 67 Tower Site, Tapajos National Forest. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/854",
-            "issued": "2023-10-03",
-            "temporal": "1999-07-01T00:00:00Z/2005-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "biosphere",
-                "earth science",
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
-            "identifier": "C2777344455-ORNL_CLOUD",
             "description": "This data sets contains a single text file which reports biometry measurements of the old-growth upland forest at the Parao Western (Santarem) - km 67, Primary Forest Tower Site. This site is in the Tapajos National Forest located in north central Brazil. Measurements extend from July 1999 through March 2005.To monitor tree woody increment, metal dendrometer bands (Figure 1) were placed on a sub-sample of 1000 trees in December 1999. The data set contains estimates of tree diameter at breast height (cm) based on caliper measurements made approximately every six weeks. The first column of data refers to the tree identification number. For a more detailed description of the biometry study refer to Rice et al. 2004.The data file contains a time series of  DBH (cm) values from July 1999 through March 2005.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-10 Ground-based Biometry Data at km 67 Tower Site, Tapajos National Forest",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F854",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F854",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD10_Biometry_Tapajos/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD10_Biometry_Tapajos/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD10_Biometry_Tapajos.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD10_Biometry_Tapajos.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/854",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/854",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD10_Biometry_Tapajos/comp/CD10_Biometry_Tapajos.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD10_Biometry_Tapajos/comp/CD10_Biometry_Tapajos.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+            "identifier": "C2777344455-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/854",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-2.86 -54.96",
+            "temporal": "1999-07-01T00:00:00Z/2005-03-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-10 Ground-based Biometry Data at km 67 Tower Site, Tapajos National Forest"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-10-16. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1.",
-            "issued": "1995-12-06",
-            "temporal": "1995-12-03T00:00:00Z/1996-02-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-02-19",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2736753162-LARC_ASDC",
             "description": "TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1 is the in situ collected onboard the DC-8 aircraft during the Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign. Data from the Multiple-Angle Spectrometer Probe (MASP), 2D-C Aerosol Probe, and FSSP Aerosol Size distributions are featured in this data product. Data collection is complete.\r\n\r\nThe Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign was conducted by NASA from December 1995 to February 1996. TOTE-VOTE took place in the Pacific region with the goal of gaining a better understanding of background transport processes from tropical/polar regions to midlatitudes. Nineteen flights were conducted using the NASA DC-8 aircraft and balloon sondes with the purpose of measuring the transport of filaments of air moved in or out of the arctic polar vortex and the tropical stratospheric reservoir. TOTE-VOTE also utilized ground-based instruments along with aircrafts.\r\n\r\nVarious instrumentation was used during TOTE-VOTE in order to achieve the mission objectives. The DC-8 aircraft was equipped with the NCAR NOxyO3 instrument, the NASA Langley Airborne Differential Absorption Lidar (DIAL) system, the Forward Scattering Spectrometer Probe (FSSP), the Microwave Temperature Profiler (MTP), the Multiple-Angle Aerosol Spectrometer Probe (MASP), and the diode laser spectrometer system, historically known as the Differential Absorption Carbon monOxide Measurement (DACOM). The NCAR NOxyO3 is a type of 4-channel chemiluminescence instrument that was used to quantify NOx (NO and NO2), NOy (total reactive nitrogen), and ozone (O3) in the air. The DIAL system used four lasers to make DIAL O3 profiles, along with collecting data on aerosol backscattering, aerosol depolarization ratio, aerosol extinction, and aerosol optical depth. The FSSP is an optical particle counter that measured particle size distribution. The MTP is a passive microwave radiometer that measured natural thermal emissions and was used during TOTE-VOTE to record temperature. The MASP spectrometer collected in-situ measurements of particle concentration, particle size distribution, and particle extinction. Along with the MASP\u2019s in-situ measurements, the DACOM spectrometer utilized three diode lasers at different wavelengths to take in-situ measurements of N2O, CO, CH4, and CO2 for TOTE-VOTE. Ground-based instruments collected lidar data while balloon sondes gathered information on wind direction, wind speed, atmospheric pressure, and air temperature.",
-            "title": "Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) DC-8 In Situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to Cite ASDC Data",
                     "@type": "dcat:Distribution",
+                    "description": "How to Cite ASDC Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/lidar/tvo/totevote.html",
-                    "description": "TOTE-VOTE DIAL Aerosol and Ozone Distribution Images",
                     "@type": "dcat:Distribution",
+                    "description": "TOTE-VOTE DIAL Aerosol and Ozone Distribution Images",
+                    "downloadURL": "https://science-data.larc.nasa.gov/lidar/tvo/totevote.html",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900648",
-                    "description": "Aircraft observations of thin cirrus clouds near the tropical tropopause",
                     "@type": "dcat:Distribution",
+                    "description": "Aircraft observations of thin cirrus clouds near the tropical tropopause",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900648",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1998GL900066",
-                    "description": "The in-flight sensitivity of Gold-Tube NOy converters to HCN",
                     "@type": "dcat:Distribution",
+                    "description": "The in-flight sensitivity of Gold-Tube NOy converters to HCN",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1998GL900066",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JD03129",
-                    "description": "Lidar temperature measurements during the Tropical Ozone Transport Experiment (TOTE)/Vortex Ozone Transport Experiment (VOTE) mission",
                     "@type": "dcat:Distribution",
+                    "description": "Lidar temperature measurements during the Tropical Ozone Transport Experiment (TOTE)/Vortex Ozone Transport Experiment (VOTE) mission",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JD03129",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98GL00231",
-                    "description": "Correlative stratospheric ozone measurements with the airborne UV DIAL system during TOTE/VOTE",
                     "@type": "dcat:Distribution",
+                    "description": "Correlative stratospheric ozone measurements with the airborne UV DIAL system during TOTE/VOTE",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98GL00231",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/Aerosol_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/Aerosol_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736753162-LARC_ASDC",
-                    "description": "Earthdata Search for TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736753162-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI for TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2736753162-LARC_ASDC",
+            "issued": "1995-12-06",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Aerosol_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-02-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-23.1 -180.0 -23.1 180.0 90.0 180.0 90.0 -180.0 -23.1 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-12-03T00:00:00Z/1996-02-20T00:00:00Z",
             "theme": [
                 "TOTE-VOTE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) DC-8 In Situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-2-JUPITER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Alice UV Imager instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v1.0_y3xg-ckzx",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "callisto",
@@ -1664746,447 +1664748,459 @@
                 "jupiter",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-2-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v1.0_y3xg-ckzx",
-            "description": "This data set contains Raw data taken by the New Horizons Alice UV Imager instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V1.0",
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
+            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V3.0",
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
-                "support archives",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset is intended to include all groundbased asteroid radar detections. These data were collected from the published literature by Dr. Steven J. Ostro. Observations which have not yet been published, or which have been reported only in an abstract, are included in the dataset as an entry with blank data fields, for the purpose of informing the dataset users of the existence of these detections. As the data from these detections are published, the data are added to this dataset in yearly updates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v3.0_y3z8-iy2h",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v3.0_y3z8-iy2h",
-            "description": "This dataset is intended to include all groundbased asteroid radar detections. These data were collected from the published literature by Dr. Steven J. Ostro. Observations which have not yet been published, or which have been reported only in an abstract, are included in the dataset as an entry with blank data fields, for the purpose of informing the dataset users of the existence of these detections. As the data from these detections are published, the data are added to this dataset in yearly updates.",
-            "title": "ASTEROID RADAR V3.0",
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
+            "title": "ASTEROID RADAR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-2-EGHEDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "phoenix",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Raw, uncalibrated engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-2-eghedr-v1.0_y3zr-tbua",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-2-EGHEDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-2-eghedr-v1.0_y3zr-tbua",
-            "description": "Raw, uncalibrated engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 2 EGHEDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 2 EGHEDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MI-3-RDR-SCI-V1.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive volume is one of a set of volumes containing raw and\nderived data from the Mars Exploration Rover mission. This volume\ncontains 'science' data products, which were generated by the\ninstrument team for archiving, as distinguished from 'operations' data\nproducts, which were generated by the Multi-Mission Image Processing\nFacility (MIPL) at JPL for using during mission operations.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mi-3-rdr-sci-v1.0_y43z-fsg6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MI-3-RDR-SCI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mi-3-rdr-sci-v1.0_y43z-fsg6",
-            "description": "This archive volume is one of a set of volumes containing raw and\nderived data from the Mars Exploration Rover mission. This volume\ncontains 'science' data products, which were generated by the\ninstrument team for archiving, as distinguished from 'operations' data\nproducts, which were generated by the Multi-Mission Image Processing\nFacility (MIPL) at JPL for using during mission operations.",
-            "title": "MER 2 MI RADIOMETRICALLY CALIBRATED RDR\n                                      V1.0",
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
+            "title": "MER 2 MI RADIOMETRICALLY CALIBRATED RDR\n                                      V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M01-V2.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m01-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M01-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m01-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP001 RDR V2.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP001 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3YACE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Annual Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3YACE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Annual Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "User Services",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491756799-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over\ndaily, 7 day, monthly, and seasonal time scales. This particular data set is the Annual rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Annual Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Annual Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_ANNUAL_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over\ndaily, 7 day, monthly, and seasonal time scales. This particular data set is the Annual rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YACE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YACE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
-                    "description": "Information on observatory maneuvers, anomalies and other events",
                     "@type": "dcat:Distribution",
+                    "description": "Information on observatory maneuvers, anomalies and other events",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aquarius.nasa.gov/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "https://aquarius.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "Aquarius Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius Data User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_ANNUAL_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_ANNUAL_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756799-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756799-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756799-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756799-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_ANNUAL_V5.jpg",
+            "identifier": "C2491756799-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3YACE",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Annual Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Annual Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2004.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY04 NASA Budget Highlights",
+                    "downloadURL": "http://www.nasa.gov/pdf/1995main_2004_Budget_Highlights.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FY04 NASA Budget Highlights"
+                }
+            ],
+            "identifier": "OCIO-Fitara-93",
             "issued": "2003-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "strategic",
                 "plan",
@@ -1665195,2194 +1665209,2191 @@
                 "finance",
                 "budget"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA HQ"
             },
-            "identifier": "OCIO-Fitara-93",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2004.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2004: NASA Budget Highlights",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/1995main_2004_Budget_Highlights.pdf",
-                    "description": "FY04 NASA Budget Highlights",
-                    "@type": "dcat:Distribution",
-                    "title": "FY04 NASA Budget Highlights"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2004: NASA Budget Highlights"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3Y7DE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 7-Day Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3Y7DE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 7-Day Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "earth science",
-                "salinity/density",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "User Services",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491757144-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the 7-Day, Descending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 7-Day Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 7-Day Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_7DAY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the 7-Day, Descending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y7DE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y7DE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "Aquarius Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius Data User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aquarius.nasa.gov/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "https://aquarius.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
-                    "description": "Information on observatory maneuvers, anomalies and other events",
                     "@type": "dcat:Distribution",
+                    "description": "Information on observatory maneuvers, anomalies and other events",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_7DAY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_7DAY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757144-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757144-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757144-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757144-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_7DAY_V5.jpg",
+            "identifier": "C2491757144-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3Y7DE",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 7-Day Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 7-Day Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-ROUGHNESS-OPS-V1.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-roughness-ops-v1.0_y47p-eyxb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-ROUGHNESS-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-roughness-ops-v1.0_y47p-eyxb",
-            "description": "NULL",
-            "title": "MER 2 MARS PANORAMIC CAMERA SURFACE\n                                     ROUGH RDR OPS V1.0",
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
+            "title": "MER 2 MARS PANORAMIC CAMERA SURFACE\n                                     ROUGH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-NORMAL-OPS-V1.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-normal-ops-v1.0_y48i-v775",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-NORMAL-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-normal-ops-v1.0_y48i-v775",
-            "description": "NULL",
-            "title": "MER 1 MARS NAVIGATION CAMERA\n                                     SURFACE NORMAL RDR OPS V1.0",
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
+            "title": "MER 1 MARS NAVIGATION CAMERA\n                                     SURFACE NORMAL RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1217",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gitelson, A.A. 2014. NACP MCI: Cropland Productivity and Biophysical Properties, Nebraska, USA, 2001-2008. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1217",
-            "issued": "2022-11-21",
-            "temporal": "2001-06-12T00:00:00Z/2008-08-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "ecological dynamics",
-                "surface radiative properties",
-                "ecosystems",
-                "land surface",
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2631228736-ORNL_CLOUD",
             "description": "This data set provides an integrated collection of (1) ground-based meteorological, radiometric, and vegetation measurements, (2) flux-based estimates of gross primary production (GPP), and (3) numerous vegetation indices derived from satellite imagery for three eddy covariance flux tower locations near Lincoln, Nebraska, USA. Land use surrounding the towers is cropland with corn and soybeans. Data are reported for selected days during the growing seasons of 2001 through 2008 only when ground-based crop canopy reflectance was measured. Algorithms developed to relate ground-based and satellite spectral information to GPP of the cropland adjacent to the towers are provided. AmeriFlux tower-based Level 2 measurements included photosynthetically active radiation (PAR), heat flux, and GPP estimates; see Section 2 for specific towers.Ground-based measurements on the corn and soybean vegetation surrounding the towers included total chlorophyll content (Chl) and leaf area index (LAI). Ground-based crop canopy reflectance was measured at 5.4 m above the corn and soybean canopy using hyperspectral radiometers (range 400 to 1100 nm) during the growing season from May to October in eight different years (2001-2008). This resulted in 173 measurement campaigns (18 in 2001, 31 in 2002, 34 in 2003, 31 in 2004, 21 in 2005, 15 in 2006, 14 in 2007, and 9 in 2008). Spectral bands from Landsat TM and ETM+, MERIS , and MODIS instruments were used to calculate vegetation indices. Vegetation indices related to chlorophyll can be used as a proxy for GPP because of the observed close relationship between GPP and Chl content in crops. Algorithms developed to relate spectral information to the GPP of the cropland adjacent to the towers are provided as companion files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP MCI: Cropland Productivity and Biophysical Properties, Nebraska, USA, 2001-2008",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1217",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1217",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_MCI_Crop_GPP/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_MCI_Crop_GPP/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_MCI_Crop_GPP.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_MCI_Crop_GPP.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1217",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1217",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_Crop_GPP/comp/Equations_for_calculated_variables.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_Crop_GPP/comp/Equations_for_calculated_variables.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_Crop_GPP/comp/NACP_MCI_Crop_GPP.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_Crop_GPP/comp/NACP_MCI_Crop_GPP.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_Crop_GPP/comp/Table_of_Algorithms.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_Crop_GPP/comp/Table_of_Algorithms.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+            "identifier": "C2631228736-ORNL_CLOUD",
+            "issued": "2022-11-21",
+            "keyword": [
+                "ecological dynamics",
+                "surface radiative properties",
+                "ecosystems",
+                "land surface",
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1217",
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
             "spatial": "-96.48 41.18 -96.44 41.18",
+            "temporal": "2001-06-12T00:00:00Z/2008-08-15T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP MCI: Cropland Productivity and Biophysical Properties, Nebraska, USA, 2001-2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3Y7CE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3Y7CE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "User Services",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491756797-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over\ndaily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over\ndaily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y7CE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y7CE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aquarius.nasa.gov/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "https://aquarius.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
-                    "description": "Information on observatory maneuvers, anomalies and other events",
                     "@type": "dcat:Distribution",
+                    "description": "Information on observatory maneuvers, anomalies and other events",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "Aquarius Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius Data User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756797-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756797-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756797-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756797-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY_V5.jpg",
+            "identifier": "C2491756797-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3Y7CE",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3807-V1.0",
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
-                "mars",
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-03T10:26:15.050 to 2015-09-05T12:01:59.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3807-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3807-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3807-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-03T10:26:15.050 to 2015-09-05T12:01:59.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3807 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3807 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-AND-V1.0",
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
-                "mars",
-                "2001 mars odyssey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The ODY MARS GAMMA RAY SPECTROMETER 5 AND data set is a table of neutron data from the NS sub-system of the Mars Odyssey Gamma-Ray Spectrometer that have been averaged (AND) over 5-degree latitude by 5-degree longitude spatial grids and 15-degrees of aerocentric solar longitude (Ls). The AND are an intermediate data product. These data are calculated from the derived neutron data (DND) and result in maps of thermal,epithermal, and fast neutron counting rates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-and-v1.0_y4ha-jfh4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "2001 mars odyssey"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-AND-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-and-v1.0_y4ha-jfh4",
-            "description": "The ODY MARS GAMMA RAY SPECTROMETER 5 AND data set is a table of neutron data from the NS sub-system of the Mars Odyssey Gamma-Ray Spectrometer that have been averaged (AND) over 5-degree latitude by 5-degree longitude spatial grids and 15-degrees of aerocentric solar longitude (Ls). The AND are an intermediate data product. These data are calculated from the derived neutron data (DND) and result in maps of thermal,epithermal, and fast neutron counting rates.",
-            "title": "ODY MARS GAMMA RAY SPECTROMETER 5 AND V1.0",
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
+            "title": "ODY MARS GAMMA RAY SPECTROMETER 5 AND V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-ROUGHNESS-OPS-V1.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-roughness-ops-v1.0_y4kj-4i5w",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-ROUGHNESS-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-roughness-ops-v1.0_y4kj-4i5w",
-            "description": "NULL",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                     SURFACE ROUGH RDR OPS V1.0",
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
+            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                     SURFACE ROUGH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0221-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-19T07:11:45.000 to 2014-08-19T13:09:58.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0221-v1.0_y4nd-7t5u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0221-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0221-v1.0_y4nd-7t5u",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-19T07:11:45.000 to 2014-08-19T13:09:58.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0221 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0221 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC3-MTP019-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 3 from 28th July 2015 to 25th Aug 2015 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc3-mtp019-v1.0_y4qw-j4is",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "alpha lyr",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC3-MTP019-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc3-mtp019-v1.0_y4qw-j4is",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 3 from 28th July 2015 to 25th Aug 2015 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 3 MTP019 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 3 MTP019 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_OCEAN.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/Aqua L2B Global Swath Ocean Products derived from Wentz Algorithm V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/AMSR-E/AE_OCEAN.002.",
-            "issued": "2002-06-19",
-            "temporal": "2002-06-19T00:00:00Z/2011-10-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-10-03",
-            "keyword": [
-                "atmospheric water vapor",
-                "clouds",
-                "ocean winds",
-                "ocean temperature",
-                "earth science",
-                "oceans",
-                "atmosphere",
-                "atmospheric winds"
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
-            "identifier": "C130038008-NSIDC_ECS",
             "description": "This daily Level-2B swath data set includes Sea Surface Temperature (SST), Near-Surface Wind Speed, Columnar Water Vapor, and Cloud liquid Water data arrays, and was used as input to generate the following daily, weekly, and monthly Level-3 gridded ocean products;  AE_DyOcn, AE_WkOcn, and AE_MoOcn.",
-            "title": "AMSR-E/Aqua L2B Global Swath Ocean Products derived from Wentz Algorithm V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_OCEAN.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_OCEAN.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_Ocean.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_Ocean.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C130038008-NSIDC_ECS&m=-30.515625%210.5625%211%211%210%210%2C2&q=AE_Ocean",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C130038008-NSIDC_ECS&m=-30.515625%210.5625%211%211%210%210%2C2&q=AE_Ocean",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_Ocean/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_Ocean/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_OCEAN.002",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_OCEAN.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_OCEAN.002",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_OCEAN.002",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C130038008-NSIDC_ECS",
+            "issued": "2002-06-19",
+            "keyword": [
+                "atmospheric water vapor",
+                "clouds",
+                "ocean winds",
+                "ocean temperature",
+                "earth science",
+                "oceans",
+                "atmosphere",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_OCEAN.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-10-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -89.24 180.0 89.24",
+            "temporal": "2002-06-19T00:00:00Z/2011-10-03T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua L2B Global Swath Ocean Products derived from Wentz Algorithm V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP21C1.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley, Simon Hook. 2023-06-29. VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 0.05Deg CMG V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP21C1.002. https://doi.org/10.5067/VIIRS/VNP21C1.002. This data set was provided by the NASA/NOAA NPP Project..",
-            "issued": "2023-06-29",
-            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-29",
-            "keyword": [
-                "surface thermal properties",
-                "land surface",
-                "earth science",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Glynn Hulley",
                 "hasEmail": "mailto:glynn.hulley@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2545314566-LPCLOUD",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Land Surface Temperature and Emissivity (LST&E) Climate Modeling Grid Version 2 product (VNP21C) is compiled daily from daytime Level 2 Gridded (L2G) intermediate products. The L2G process maps the daily (VNP21) (https://doi.org/10.5067/VIIRS/VNP21.002) swath granules onto a sinusoidal MODIS grid and stores all observations overlapping a gridded cell for a given day. The VNP21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all cloud-free observations that have good LST accuracies. The 0.05 degree (5600 m) dataset is derived through resampling the native 750 meter VIIRS resolution in the input product. The overall objective for NASA VIIRS products is to ensure the algorithms and products are compatible with the MODIS Terra and Aqua algorithms to promote the continuity of the Earth Observation System (EOS) mission. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley, Simon Hook",
-            "title": "VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 0.05Deg CMG V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917655271-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Land Surface Temperature and Emissivity (LST&E) Climate Modeling Grid Version 2 product (VNP21C) is compiled daily from daytime Level 2 Gridded (L2G) intermediate products. The L2G process maps the daily (VNP21) (https://doi.org/10.5067/VIIRS/VNP21.002) swath granules onto a sinusoidal MODIS grid and stores all observations overlapping a gridded cell for a given day. The VNP21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all cloud-free observations that have good LST accuracies. The 0.05 degree (5600 m) dataset is derived through resampling the native 750 meter VIIRS resolution in the input product. The overall objective for NASA VIIRS products is to ensure the algorithms and products are compatible with the MODIS Terra and Aqua algorithms to promote the continuity of the Earth Observation System (EOS) mission. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP21C1.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP21C1.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314566-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314566-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
-                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP21C1.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP21C1.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1662/VNP21_User_Guide_V2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1662/VNP21_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917655271-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917655271-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LST_Val.html",
-                    "description": "Validation at stage 1 has been achieved for the VIIRS Land Surface Temperature and Emissivity product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the VIIRS Land Surface Temperature and Emissivity product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LST_Val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
-                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2917655271-LPCLOUD?h=85&w=85",
+            "identifier": "C2545314566-LPCLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "surface thermal properties",
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP21C1.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 0.05Deg CMG V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206892-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Monthly Summaries of Soil Temperature and Soil Moisture at Sites in Alaska, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1995-09-01",
-            "temporal": "1995-09-01T00:00:00Z/2001-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2001-08-31",
-            "keyword": [
-                "soils",
-                "frozen ground",
-                "earth science",
-                "cryosphere",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chien-Lu Ping",
                 "hasEmail": "mailto:pfclp@uaa.alaska.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206892-NSIDCV0",
             "description": "This data set contains soil temperature and soil moisture from 17 sites in Alaska. Temporal coverage varies by station; the earliest record is from September 1995, and the latest is from August 2001. Data from individual stations are available in tab-delimited ASCII text files. An Excel spreadsheet contains the same data compiled together in a single file. NSIDC currently provides these summary data via ftp; the full soil temperature and moisture data set is available from Ron Paetzold, USDA.",
-            "title": "Monthly Summaries of Soil Temperature and Soil Moisture at Sites in Alaska, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD624_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD624_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD624/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD624/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD624/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD624/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206892-NSIDCV0",
+            "issued": "1995-09-01",
+            "keyword": [
+                "soils",
+                "frozen ground",
+                "earth science",
+                "cryosphere",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206892-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2001-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-159.6722 59.7583 -147.9139 70.475",
+            "temporal": "1995-09-01T00:00:00Z/2001-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Summaries of Soil Temperature and Soil Moisture at Sites in Alaska, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/B03/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/B03/DATA001.",
-            "issued": "2005-03-30",
-            "temporal": "2005-03-30T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "ocean temperature",
-                "ocean optics",
-                "ocean chemistry",
-                "oceans",
-                "salinity/density"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360127-OB_DAAC",
             "description": "Measurements made near the mid-Atlantic coastal region and Monterey Bay in 2005 and 2006.",
-            "title": "Mid-Atlantic coastal region and Monterey Bay measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FB03%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FB03%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/B03/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/B03/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360127-OB_DAAC",
+            "issued": "2005-03-30",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "ocean optics",
+                "ocean chemistry",
+                "oceans",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/B03/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-03-30T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Mid-Atlantic coastal region and Monterey Bay measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43DNBA2.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43DNBA2. Version 001. VIIRS/NPP DNB BRDF/Albedo Quality Daily L3 Global 1km SIN Grid V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43DNBA2.001. https://doi.org/10.5067/VIIRS/VNP43DNBA2.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1632561158-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Day/Night Band (DNB) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality (VNP43DNBA2) Version 1 product provides BRDF and Albedo quality at 1 kilometer (km) resolution. The VNP43DNBA2 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VNP43DNBA2 product gives information regarding band quality and days of valid observation within a 16-day period for the VIIRS DNB. The VNP43 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite.\r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VNP43DNBA1 to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43DNBA4), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43DNBA3). Researchers can use the BRDF model parameters with a simple polynomial to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nThe VNP43DNBA2 data product provides a total of seven SDS layers, including BRDF/Albedo band quality and days of valid observation within a 16-day period for the VIIRS DNB, as well as land water type class flag, snow BRDF albedo class flag, local solar noon, and the platform name.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43DNBA2",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP DNB BRDF/Albedo Quality Daily L3 Global 1km SIN Grid V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Day/Night Band (DNB) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality (VNP43DNBA2) Version 1 product provides BRDF and Albedo quality at 1 kilometer (km) resolution. The VNP43DNBA2 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VNP43DNBA2 product gives information regarding band quality and days of valid observation within a 16-day period for the VIIRS DNB. The VNP43 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite.\r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VNP43DNBA1 to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43DNBA4), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43DNBA3). Researchers can use the BRDF model parameters with a simple polynomial to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nThe VNP43DNBA2 data product provides a total of seven SDS layers, including BRDF/Albedo band quality and days of valid observation within a 16-day period for the VIIRS DNB, as well as land water type class flag, snow BRDF albedo class flag, local solar noon, and the platform name.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43DNBA2.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43DNBA2.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43DNBA2.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43DNBA2.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43DNBA2.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43DNBA2.001/",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1632561158-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1632561158-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43dnba2_brdf_albedo_quality_product",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43dnba2_brdf_albedo_quality_product",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43DNBA2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43DNBA2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP101/VIIRS/VNP43DNBA2.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP101/VIIRS/VNP43DNBA2.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
-                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
-                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 }
             ],
+            "identifier": "C1632561158-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43DNBA2.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP43DNBA2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP DNB BRDF/Albedo Quality Daily L3 Global 1km SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2157",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chen, D., M. Billmire, N.H.F. French, T.V. Loboda, and A.E. Bredder. 2023. Simulated Fine Particulate Matter (PM2.5) Estimates over Alaska, 2001-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2157",
-            "issued": "2024-04-24",
-            "temporal": "2001-05-10T00:00:00Z/2015-09-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-25",
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "atmosphere",
-                "air quality",
-                "aerosols",
-                "natural hazards"
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
-            "identifier": "C2951624721-ORNL_CLOUD",
             "description": "The dataset provides simulated PM2.5 concentration estimates over Alaska, U.S. PM2.5 (particulate matter with diameter <= 2.5 microns) concentrations  in air (micrograms m-3) are gridded at 0.1-degree resolution for May to September for the years 2001 through 2015. The data were created in a modeling process utilizing the Wildland Fire Emissions Inventory System (WFEIS), the Arctic-Boreal Vulnerability Experiment (ABoVE) Wildfire Date of Burning (WDoB) dataset,  and multiple models including the Hybrid Single-Particle Lagrangian Integrated Trajectory (HYSPLIT) model. The data are provided in GeoTIFF format.",
-            "graphic-preview-description": "Maximum PM2.5 concentration maps for May and June of 2001-2015.",
-            "title": "Simulated Fine Particulate Matter (PM2.5) Estimates over Alaska, 2001-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Daily_FineParticulateMatter_AK_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2157",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2157",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Daily_FineParticulateMatter_AK/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Daily_FineParticulateMatter_AK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Daily_FineParticulateMatter_AK.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Daily_FineParticulateMatter_AK.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2157",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2157",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Daily_FineParticulateMatter_AK/comp/Daily_FineParticulateMatter_AK.pdf",
-                    "description": "Simulated Fine Particulate Matter (PM2.5) Estimates over Alaska, 2001-2015: Daily_FineParticulateMatter_AK.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Simulated Fine Particulate Matter (PM2.5) Estimates over Alaska, 2001-2015: Daily_FineParticulateMatter_AK.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Daily_FineParticulateMatter_AK/comp/Daily_FineParticulateMatter_AK.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Daily_FineParticulateMatter_AK_Fig1.jpg",
-                    "description": "Maximum PM2.5 concentration maps for May and June of 2001-2015.",
                     "@type": "dcat:Distribution",
+                    "description": "Maximum PM2.5 concentration maps for May and June of 2001-2015.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Daily_FineParticulateMatter_AK_Fig1.jpg",
+                    "mediaType": "image/jpeg",
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
+            "graphic-preview-description": "Maximum PM2.5 concentration maps for May and June of 2001-2015.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Daily_FineParticulateMatter_AK_Fig1.jpg",
+            "identifier": "C2951624721-ORNL_CLOUD",
+            "issued": "2024-04-24",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "atmosphere",
+                "air quality",
+                "aerosols",
+                "natural hazards"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2157",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-178.0 51.0 -128.0 71.0",
+            "temporal": "2001-05-10T00:00:00Z/2015-09-28T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Simulated Fine Particulate Matter (PM2.5) Estimates over Alaska, 2001-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1509",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Loboda, T.V., and E.E. Hoy. 2017. CMS: Fire Weather Indices for Interior Alaska, 2001-2010. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1509",
-            "issued": "2018-01-25",
-            "temporal": "2001-01-01T00:00:00Z/2010-09-18T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "climate indicators",
-                "earth science",
-                "land surface/agriculture indicators"
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
-            "identifier": "C2391444072-ORNL_CLOUD",
             "description": "This dataset provides daily fire weather indices for interior Alaska during the active fire seasons from 2001 to 2010. Data are gridded at 60-m resolution. The active fire season is defined as May 24-September 18 (days of the year 144-261) in this dataset. Fire weather is the use of meteorological parameters such as relative humidity, wind speed and direction, cloud cover, mixing heights, and soil moisture to determine whether conditions are favorable for fire growth and smoke dispersion. The six indices provided in this dataset are defined and produced following the methodology of the Canadian Forest Fire Weather Index System: Fine Fuel Moisture Code, Duff Moisture Code, Drought Code, Initial Spread Index, Buildup Index, Fire Weather Index. The dataset was developed following point source data interpolation from weather station observations.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CMS: Fire Weather Indices for Interior Alaska, 2001-2010",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Fire_Weather_Data_AK_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1509",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1509",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Fire_Weather_Data_AK/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Fire_Weather_Data_AK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Fire_Weather_Data_AK.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Fire_Weather_Data_AK.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1509",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1509",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Fire_Weather_Data_AK/comp/CMS_Fire_Weather_Data_AK.pdf",
-                    "description": "CMS: Fire Weather Indices for Interior Alaska, 2001-2010: CMS_Fire_Weather_Data_AK.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CMS: Fire Weather Indices for Interior Alaska, 2001-2010: CMS_Fire_Weather_Data_AK.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Fire_Weather_Data_AK/comp/CMS_Fire_Weather_Data_AK.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Fire_Weather_Data_AK_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Fire_Weather_Data_AK_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1509",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1509",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Fire_Weather_Data_AK_Fig1.png",
+            "identifier": "C2391444072-ORNL_CLOUD",
+            "issued": "2018-01-25",
+            "keyword": [
+                "climate indicators",
+                "earth science",
+                "land surface/agriculture indicators"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1509",
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
             "spatial": "-171.59 56.62 -131.8 73.66",
+            "temporal": "2001-01-01T00:00:00Z/2010-09-18T23:59:59Z",
             "theme": [
                 "CMS",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS: Fire Weather Indices for Interior Alaska, 2001-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2239",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Casta\u00f1eda-Moya, E., and E. Solohin. 2023. Delta-X: Soil Properties for Herbaceous Wetlands, MRD, Louisiana, 2021, V3. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2239",
-            "issued": "2023-09-21",
-            "temporal": "2021-03-21T00:00:00Z/2021-08-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-26",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "soils",
-                "biosphere",
-                "ecosystems"
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
-            "identifier": "C2772852265-ORNL_CLOUD",
             "description": "This dataset contains properties of soil core samples for herbaceous wetlands collected in the Atchafalaya and Terrebonne basins in southeastern coastal Louisiana for the period 2021-03-21 to 2021-04-02 and on 2021-08-19. Field measurements were conducted at six sites in the Atchafalaya (N = 3) and Terrebonne (N = 3) basins. Five sites were adjacent to sites from the Coastwide Reference Monitoring System (CRMS). The other site is in the Wax Lake Delta (WLD) without appropriate adjacent CRMS sites. Herbaceous wetland sites in both basins were chosen to represent a salinity gradient including freshwater, brackish and saline ecosystems. Soil properties include bulk density, organic matter content, total densities of carbon, nitrogen, phosphorus, along with 13C and 15N isotopic signatures. The data are provided in comma-separated values (.csv) format.",
-            "graphic-preview-description": "Typical soil core from herbaceous wetland collected during March 2021 in coastal Louisiana. This image shows the top 50 cm of soil collected using a Russian corer.",
-            "title": "Delta-X: Soil Properties for Herbaceous Wetlands, MRD, Louisiana, 2021, V3",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Herb_WetlandSoil_V3_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2239",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2239",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Herb_WetlandSoil_V3/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Herb_WetlandSoil_V3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Herb_WetlandSoil_V3.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Herb_WetlandSoil_V3.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2239",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2239",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Herb_WetlandSoil_V3/comp/DeltaX_Herb_WetlandSoil_V3.pdf",
-                    "description": "Delta-X: Soil Properties for Herbaceous Wetlands, MRD, Louisiana, 2021, V3: DeltaX_Herb_WetlandSoil_V3.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Soil Properties for Herbaceous Wetlands, MRD, Louisiana, 2021, V3: DeltaX_Herb_WetlandSoil_V3.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Herb_WetlandSoil_V3/comp/DeltaX_Herb_WetlandSoil_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Herb_WetlandSoil_V3_Fig1.jpg",
-                    "description": "Typical soil core from herbaceous wetland collected during March 2021 in coastal Louisiana. This image shows the top 50 cm of soil collected using a Russian corer.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical soil core from herbaceous wetland collected during March 2021 in coastal Louisiana. This image shows the top 50 cm of soil collected using a Russian corer.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Herb_WetlandSoil_V3_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://deltax.jpl.nasa.gov/",
-                    "description": "Delta-X Project Site",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X Project Site",
+                    "downloadURL": "https://deltax.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Typical soil core from herbaceous wetland collected during March 2021 in coastal Louisiana. This image shows the top 50 cm of soil collected using a Russian corer.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Herb_WetlandSoil_V3_Fig1.jpg",
+            "identifier": "C2772852265-ORNL_CLOUD",
+            "issued": "2023-09-21",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils",
+                "biosphere",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2239",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-91.45 29.17 -90.82 29.51",
+            "temporal": "2021-03-21T00:00:00Z/2021-08-19T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Soil Properties for Herbaceous Wetlands, MRD, Louisiana, 2021, V3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0108",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0108.",
-            "issued": "1999-11-05",
-            "temporal": "1991-11-13T00:00:00Z/1991-12-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-12",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOSE ALVAREZ",
                 "hasEmail": "mailto:j.m.alvarez@larc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001192-LARC_ASDC",
             "description": "FIRE_CI2_LARC8_LIDAR is the First ISCCP (International Satellite Cloud Climatology Project) Regional Experiments (FIRE) Cirrus Phase II Langley Research Center (LARC) Eight Inch Lidar data product. It was designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE were to: seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles ; and investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). \r\n\r\nEach mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The Langley Research Center (LARC) Cloud Lidar is a dual-channel polarization sensitive lidar using a frequency doubled Nd: YAG laser as a linearly polarized transmitter and an eight inch Cassegrainian telescope as a receiver. Backscattered laser light collected by the receiver is collimated, directed through a half wave plate, and then passed through polarizing optics which decompose the signal into two components, one parallel and the other perpendicular to the polarization plane of the transmitted beam. Separate amplification and digitization paths are employed for each component, resulting in two arrays of back scatter data for each measured laser pulse. The LARC Cloud Lidar is designed for optimum cloud monitoring operations at altitudes between 3 km and 18 km. To prevent saturation of the detectors at lower altitudes, a gating circuit is used to delay the activation of the first dynode in the Photomultiplier (PMT). The PMT is brought to full sensitivity only after this delay time has elapsed.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Langley Research Center (LARC) Eight Inch Lidar",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0108",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0108",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
-                    "description": "ASDC Data and Information for FIRE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for FIRE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001192-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_LARC8_LIDAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_LARC8_LIDAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001192-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_larc8_lidar_dataset.pdf",
-                    "description": "FIRE LaRC Eight Inch Lidar Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE LaRC Eight Inch Lidar Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_larc8_lidar_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar_info1.txt",
-                    "description": "Readme for The Langley 8\" Lidar System at Parsons, Kansas Original Version: 11/19/91",
                     "@type": "dcat:Distribution",
+                    "description": "Readme for The Langley 8\" Lidar System at Parsons, Kansas Original Version: 11/19/91",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar_info1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar_info2.txt",
-                    "description": "List of list of FIRE CIRUS 2 files submitted to the archive as of July 1994 Readme",
                     "@type": "dcat:Distribution",
+                    "description": "List of list of FIRE CIRUS 2 files submitted to the archive as of July 1994 Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar_info2.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar.ps",
-                    "description": "FIRE Cirrus 2 Read-Me- Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 Read-Me- Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar_user_guide.txt",
-                    "description": "LaRC Lidar Data User's Guide Readme",
                     "@type": "dcat:Distribution",
+                    "description": "LaRC Lidar Data User's Guide Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_larc8_lidar_user_guide.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_lib.c",
-                    "description": "fci2_lib Program for reading FIRE Cirrus II data sets - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "fci2_lib Program for reading FIRE Cirrus II data sets - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_lib.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.c",
-                    "description": "Sample read routines for all FIRE Cirrus II data sets in ASCII format - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read routines for all FIRE Cirrus II data sets in ASCII format - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.h",
-                    "description": "Subroutines to read DX data from a DX file - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Subroutines to read DX data from a DX file - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci2_sw.h",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/genpro.c",
-                    "description": "Program to read GENPRO Formatted Files - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to read GENPRO Formatted Files - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/genpro.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci2",
-                    "description": "Makefile.fci2 Release: 1.1 Date: 3/22/94",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile.fci2 Release: 1.1 Date: 3/22/94",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_larc8_lidar.c",
-                    "description": "Reads the Langley Research Center Cloud Lidar (LaRC-CL) - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Reads the Langley Research Center Cloud Lidar (LaRC-CL) - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_larc8_lidar.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0108",
-                    "description": "DOI data set landing page for FIRE_CI2_LARC8_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_LARC8_LIDAR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0108",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/fire_project.pdf",
-                    "description": "Project/Campaign Document: Project/Campaign Document: FIRE Langley DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "Project/Campaign Document: Project/Campaign Document: FIRE Langley DAAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/fire_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-Cirrus.tar",
-                    "description": "FIRE II-Cirrus Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II-Cirrus Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-Cirrus.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Cirrus.tar",
-                    "description": "FIRE I-Cirrus Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE I-Cirrus Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Cirrus.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Extended-Time-Observation.tar",
-                    "description": "FIRE I-Extended-Time-Observation Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE I-Extended-Time-Observation Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Extended-Time-Observation.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-ASTEX.tar",
-                    "description": "FIRE II-ASTEX Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II-ASTEX Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-ASTEX.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
-                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
-                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_LARC8_LIDAR/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_LARC8_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_LARC8_LIDAR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_LARC8_LIDAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_LARC8_LIDAR/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_LARC8_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_LARC8_LIDAR_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_LARC8_LIDAR/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001192-LARC_ASDC",
+            "issued": "1999-11-05",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0108",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "37.18 -95.7",
+            "temporal": "1991-11-13T00:00:00Z/1991-12-07T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Langley Research Center (LARC) Eight Inch Lidar"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4TT4NWQ",
             "bureauCode": [
                 "026:00"
             ],
```

